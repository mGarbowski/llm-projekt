# IPC cd (2024-04-22)

## Timery
* Czas rzeczywisty
	* mogą być zmiany na czas zimowy, sekundy przestępne itd
* Monotoniczny
* Czas astronomiczny
	* ignoruje sekundy przestępne
* Działa asynchronicznie, po upływie czasu wysyła sygnał
* W przypadku obsługi sygnału, funkcja musi mieć *async-signal safety*
	* wielobieżność (reentrance) i thread safety nie wystarczy
	* jest lista funkcji wg specyfikacji POSIX, które powinny być bezpieczne do wywołania w tym kontekście

### timerfd
* Timer powiązany z deskryptorem pliku
* Można korzystać przy `select`, `poll`, `epoll`
	* odczyt z pliku timera usypia proces do upłynięcia czasu
	* można tak realizować programowanie zdarzeniowe

## Ustalanie priorytetu zadań przetwarzających dane
* `sched_setscheduler`
	* określenie polityki szeregowania
	* parametry (np. priorytet)
* Typy przydziału
	* `SCHED_OTHER` - zadania dostają po kolei kwanty czasu procesora (typowy)
	* `SCHED_BATCH` - zoptymalizowane pod kątem zadań wsadowych (nieinteraktywnych)
	* `SCHED_IDLE` - dla zadań realizowanych w tle
* Typy przydziału dla zadań czasu rzeczywistego
	* `SCHED_FIFO` - pierwszy zgłoszony proces będzie wykonywany jako pierwszy, może się zawiesić na IO lub zostać wywłaszczony przez proces o wyższym priorytecie
	* `SCHED_RR` - jak FIFO, trafia na koniec kolejki po wykorzystaniu kwantu czasu
	* `SCHED_DEADLINE` - dla rzadko wykonywanych zadań terminowych
* `setpriority`, `nice`
	* najwyższy priorytet - `-20`
	* najmniejszy - `19`
	* najwyższy priorytet może doprowadzić do zakleszczenia (jeśli wymaga odpowiedzi od daemonów systemowych)
* Kazde przełączenie procesu to niezerowy nakład pracy dla CPU
* Linux zwykle rezerwuje część czasu procesora (typowo 5%) dla zadań niebędących zadaniami czasu rzeczywistego
	* określane w plikach w `/proc/sys/kernel`

## Użycie Linuxa w zastosowaniach czasu rzeczywistego
* Opóźnienia związane z pracą planisty
* Opóźnienia związane z reakcją na zdarzenia sprzętowe
* Najwazniejsze jest terminowe wykonywanie zadań i obsługa zdarzeń, a nie najlepsza wydajność

### Tryb `SCHED_DEADLINE`
* Programiście trudniej doprowadzić do zagłodzenia
* Dla każdego procesu definiowane są
	* czas wykonania (runtime)
	* termin wykonania (deadline)
	* okres wykonania (period)
	* runtime <= deadline <= period
* Proces po zakończeniu pracy powinien wywołać `sched_yield`
* Można wykorzystać ten mechanizm do dzielenia czasu procesora
	* jeśli proces nie wyrobi się w runtime, to zostanie zawieszony przez planistę do następnego okresu
* Próba ustawienia parametrów niemożliwych do spełnienia zwróci błąd

## Oczekiwanie aktywne
* Zazwyczaj usypiamy proces w oczekiwaniu na zdarzenie sprzętowe (`poll`, `select`)
	* zostanie wzbudzony przerwaniem
* W pewnych warunkach aktywne oczekiwanie daje krótszy czas
	* krótszy czas oczekiwania na obsługę zdarzenia
	* nie ma straty czasu na przełączenie kontekstu procesora
	* trzeba pamiętać że to zajmuje magistralę
* Dla większej liczby procesów może być długi czas oczekiwania na przydział kwantu czasu procesora
	* można zabezpieczyć zadania przed wywłaszczeniem
* Dla procesora wielordzeniowego jest możliwość zarezerwowania konkretnego rdzenia dla konkretnego procesu (lub grupy procesów)
	* `sched_setaffinity`
	* `sched_getaffinity`
* Można wyłączyć rdzeń z kontroli planisty
* Przerwania
	* `/proc/irq`
	* jest określone które rdzenie mogą obsługiwać dane przerwanie
	* można zabronić przerwaniom korzystać z określonych rdzeni
	* obsługa przerwania i programu obsługującego urządzenie przez ten sam rdzeń może być korzystne ze względu na cache

program `chrt`

## Optymalizacja obsługi przerwań
* Opóźnienie może wzrosnąć względem aktywnego oczekiwania
* Może ograniczyć maksymalne opóźnienie
* Można podizelić obsługę przerwania
	* górna połówka - zasadnicza procedura obsługi przerwania, może ograniczyć możliwość obsługi innych przerwań, wykonywana natychmiast, zleca wykonanie dolnej połówki
	* dolna połówka - odroczona procedura obsługi przerwania, wykonywana najszybciej jak to możliwe ale po uporządkowaniu stanu systemu
* Sposoby obsługi dolnej połówki
	* tasklets
	* workqueues
	* threaded interrupts

Książka Linux Device Drivers

## Co można poprawić w sprzęcie i sterowniku
* Unikać niepotrzebnego kopiowania danych
* Urządzenie powinno dostarczać dane przez bezpośredni dostęp do pamięci (DMA)
	* IOMMU - pozwala urządzneiom korzystać z DMA dla konkretnych adresów
* Wymaga dobrej obsługi w sterowniku urządzenia

### Korzystanie z DMA
* Wpisanie do rejestrów urządzenia adresu bufora w pamięci, w którym ma umieścić dane
* Procesor wpisuje do rejestrów urządzenia długość przesyłanego bloku danych
* Procesor uruchamia transfer i przechodzi do innych zadań
* ...

### Problemy przy korzystaniu z DMA
* Urządzenie obsługujące DMA może używać specyficznej przestrzeni adresowej
* Są różne magistrale i każda korzysta ze specyficznych adresów
	* to jest obsługiwane przez jądro
	* procedura mapowania buforów DMA
* Trudności z alokacją dużych ciągłych buforów dla DMA
	* proste urządzenia mogą wymagać bufora zajmującego ciągły obszar w przestrzeni adresowej
	* rozwiązanie - CMA - Contiguous Memory Allocator
	* bufory rozproszone - bufor podzielony na segmenty, każdy segment odpowiada ciągłemu kawałkowi pamięci, lista deskryptorów segmentów (SG - scatter-gather DMA)

## DMA i pamięć podręczna
* Procesor odwołuje się do pamięci przez pamięć cache
* Bufory DMA są w pamięci RAM
* Urządzenie piszą bezpośrednio do pamięci, a procesor tego nie widzi
* Rozwiązania
	* wyłączenie korzystania z pamięci cache dla konkretnego bufora - ogromne spowolnienie
	* procedury synchronizacji


Nie będzie na kolokwium sekcji o adaptacji linuxa