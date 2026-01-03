# Kolokwium 2

## Drzewo urządzeń - co to jest, do czego służy, jakie są możliwości jego modyfikacji?
* Standard opisu połączenia między CPU a sprzętem
* Pliki DTS
* Pozwala na łatwą rozbudowę
* Pozwala na dynamiczną zmianę opisu systemu
* Mechanizm nakładek
	* bezpieczna modyfikacja przez bootloader
	* potencjalnie niebezpieczna modyfikacja podczas pracy - `dtoverlay`
## Obsługa magistral zapewniających autodetekcję urządzeń (np. USB, PCI Express) w systemie Linux
* Jądro monitoruje stan magistrale i ładuje odpowiedni sterownik po wykryciu urządzenia
* Program `udev` tworzy odpowiednie wpisy w `/dev`
	* można definiować własne reguły
## Komunikacja z urządzeniami we/wy - rejestry mapowane w pamięć, lub w oddzielną przestrzeń adresową I/O, sposoby ich obsługi
* Dla rejestrów w przestrzeni adresowej IO
	* niektóre architektury wspierają operacje typu `in` i `out` w przestrzeni adresowej IO
	* określenie praw dostępu przez instrukcje `ioperm` i `iopl`
* Dla rejestrów zmapowanych do pamięci
	* dostęp przez `/dev/mem` do fizycznej przstrzeni adresowej CPU
	* sterownik `uio` pozwala tworzyć mikrosterowniki w przestrzeni użytkownika
	* po zmapowaniu odpowiedniego obszaru pamięci do przestrzeni adresowej procesu można odwoływać się do rejestrów np. jako do pól struktury

## Szeregowanie procesów - zwykłe tryby szeregowania, tradycyjne tryby szeregowania czasu rzeczywistego, używanie trybu terminowego. Jak ich używać? Jak system radzi sobie z "błędnymi" procesami szeregowanymi w trybach czasu rzeczywistego?
* Zwykłe tryby szeregowanie
	* `SCHED_OTHER` - podstawowy tryb, zadania po kolei dostają kwanty czasu (round robin)
	* `SCHED_BATCH` - dla zadań wsadowych, większa przepustowość kosztem opóźnień
	* `SCHED_IDLE` - dla zadań w tle
* Tryby szeregowania czasu rzeczywistego
	* `SCHED_FIFO` - FIFO bez ograniczeń czasowych, proces o wyższym priorytecie może wywłaszczyć
	* `SCHED_RR` - round robin, FIFO ale tylko na przydzielony kwant czasu
	* `SCHED_DEADLINE`
* Błędne procesy
	* FIFO i RR - proces z wyższym priorytetem może uniemożliwić wykonanie procesów o niższych priorytetach
	* DEADLINE - nie może, jeśli proces nie zakończy działania w terminie to jest zawieszany do następnego okresu (throttling)
* `SCHED_DEADLINE`
	* czas wykonywania (runtime)
	* termin (deadline)
	* okres (period)
	* runtime <= deadline <= period
	* po wykonaniu dobrowolnie wywołuje `sched_yield`, albo zawiesza się na IO
* Tryb szeregowania wybiera się przez wywołanie `sched_setscheduler`
	* `pid` - wybrany lub wołający
	* `policy` - jedna z wymienionych
	* `sched_param` - parametry (np. priorytet)
## Jak powinno zachowywać się zadanie czasu rzeczywistego, żeby nie zakłócić działania systemu?
* Używać odpowiedniego priorytetu i polityki harmonogramowania
* Ograniczenie do minimum sekcji krytycznych, blokowania
* Nie posiadać błędów
* Nie powodować zakleszczeń

## Emulator QEMU i jego możliwości - emulowane platformy, standardowo dostępne modele urządzeń, możliwości dodawania własnych modeli urządzeń. Sposoby jego wykorzystania do testowania naszego obrazu systemu operacyjnego i aplikacji.
* Emulowane platformy
	* ARM
	* Intel
	* RISC-V
	* wiele innych
* Standardowo dostępne modele urządzeń
	* karty sieciowe
	* urządzenia USB
	* urządzenia pamięci masowej
* Można definiować własne urządzenie i dodawać je wykorzystując mechanizm device tree
* Może być wykorzystany do testowania aplikacji i systemu
	* w wirtualnym środowisku
	* bez dostępu do fizycznego sprzętu
	* przy różnych emulowanych konfiguracjach sprzętowych
	* przy różnej dostępności zasobów

## Komunikacja międzyprocesowa - dostępne mechanizmy komunikacji, ich właściwości i sposoby wykorzystania, mechanizmy synchronizacji i ich wykorzystanie. Uruchamianie poszczególnych procesów systemu. Sposoby nawiązywania komunikacji między procesami - np. dostęp przez nazwy do kolejek itp.

### Kolejki komunikatów
* Jednokierunkowa komunikacja między 2 procesami
	* przy wielu procesach trzeba użyć tyle samo kolejek
	* do dwustronnej komunikacji potrzeba 2 kolejek
* Wymiana komunikatów
	* nie trzeba ich wyodrębniać ze strumienia danych
* Dane są kopiowane 2 razy
	* przy nadawaniu i odbieraniu
	* niewydajne dla dużych ilości danych
	* można przesyłać kolejkami same deskryptory, a duże dane przesyłać w inny sposób
* Identyfikowane przez nazwę
	* nazwa zaczyna się od `/`
* Funkcje
	* `mq_open` - otwarcie / utworzenie
	* `mq_setattr` - ustawienie parametrów
	* `mq_close` - zamknięcie
	* `mq_unlink` - usunięcie
	* `mq_send` - wysłanie komunikatu
	* `mq_receive` - odbiór komunikatu
	* `mq_notify` - powiadomienie z użyciem sygnału
	* `poll`, `epoll`, `select` - do oczekiwania na komunikat, jak do plików

### Semafory
* Zezwala na dostęp do dzielonego zasobu przez ustaloną liczbę procesów
* Użycie do synchronizacji procesów (a nie wątków) wymaga ustawienia flagi `PTHREAD_PROCESS_SHARED`
* Mogą być nazwane
* Funkcje
	* `sem_init` - tworzenie (podanie początkowej wartości)
	* `sem_destroy` - usunięcie
	* `sem_wait` - próba uzyskania dostępu i zamknięcie blokady
	* `sem_post` - zwolnienie blokady
	* `sem_open` - tworzenie / otwieranie nazwanego semafora
	* `sem_close` - zamknięcie nazwanego semafora
	* `sem_unlink` - usunięcie nazwanego semafora

### Mutex
* Mutual exclusion
	* semafor binarny
	* realizacja sekcji krytycznej
	* tylko jeden proces / wątek może mieć zamkniętą blokadę
* Funkcje
	* `pthread_mutex_init` - tworzenie
	* `pthread_mutex_destroy` - niszczenie
	* `pthread_mutex_lock` - pozyskanie blokady (też opcje z timeoutem i nieblokująca)
	* `pthread_mutex_unlock` - zwolnienie blokady
	* `pthread_mutexattr_setpshared` - umożliwienie synchronizacji procesów
	* `pthread_mutexattr_setrobust` - dodatkowe funkcji (np. zachowanie po śmierci procesu bez zwalniania mutexu)

### Zmienne warunkowe
* Pozwalają oczekiwać na spełnienie określonego warunku
* Funkcje
	* `pthread_cond_init` - tworzenie
	* `pthread_cond_destroy` - niszczenie
	* `pthread_condattr_setpshared` - umożliwienie synchronizacji procesów
	* `pthread_cond_wait` - oczekiwanie na zdarzenie
	* `pthread_cond_braodcast` - wybudzenie wszystkich oczekujących procesów
	* `pthread_cond_signal` - wybudzenie jednego z oczekujących procesów
* Poprawne użycie z mutexem
	* oczekiwanie na zdarzenie przy zamkniętym mutexie
	* wątek jest zablokowany do czasu wystąpienia zdarzenie (broadcast/signal), a mutex zostaje zwolniony
	* po wystąpieniu zdarzenia sterowanie wraca do wątku, wątek ma zamknięty mutex

### Blokada zapis/odczyt
* Równeczesny dostęp wielu konsumentów danych przy równoczesnej synchronizacji producenta danych z konsumentami
* Proble czytelników i pisarza
	* semafor się nie nadaje, bo chcemy rozróżnić konsumentów nielbokujących się nawzajem od producenta blokującego wszystkich
* Bez dodatkowych mechanizmów jest ryzyko zagłodzenia producenta
	* któryś z konsumentów zawsze będzie blokował dostęp producentowi
* Funkcje
	* `pthread_rwlockattr_setkind_np` - ustawienie właściwości (np. zapobieganie zagłodzeniu)
	* `pthread_rwlock_init` - tworzenie
	* `pthread_rwlock_destroy` - niszczenie
	* `pthread_rwlockattr_setpshared` - umożliwienie synchronizacji procesów
	* `pthread_rwlock_wrlock` - pozyskanie blokady do zapisu
	* `pthread_rwlock_rdlock` - pozyskanie blokady do odczytu
	* są też wersje z timeoutem i nieblokujące
	* `pthread_rwlock_unlock` - zwolnienie blokady

### Bariera
* Synchronizacja wykonania kodu (a nie dostępu do zasobów)
* Wątek może wykonywać kod dalej, kiedy określona liczba wątków dojdzie do wybranego punktu
* Funkcje
	* `pthread_barrier_init` - utworzenie z określeniem liczby wątków
	* `pthread_barrier_wait` - dojście do bariery / oczekiwanie aż wszystkie wątki dojdą do bariery
	* `pthread_barrier_destroy` - niszczenie
	* `pthread_barrierattr_setpshared` - umożliwienie synchronizacji procesów

### Spinlock
* Jak semafor, ale oczekuje aktywnie na zwolnienie zajętej blokady zamiast usypiać wątek
* Ma sens tylko w systemie wieloprocesowym i kiedy czas oczekiwania na zwolnienie blokady jest krótki
* Pozwala uniknąć narzutu na przełączanie procesów
* Funkcje
	* `pthread_spin_init` - tworzenie
	* `pthread_spin_destroy` - niszczenie
	* `pthread_spin_lock` - pozyskanie blokady
	* `pthread_spin_unlock` - zwolnienie blokady
### Pamięć dzielona
* Są nazwane
* Pliki w `/dev/shm`
* Trzeba je usuwać ręcznie, bo przeżywają koniec procesu
* Równoczesny dostęp wymaga użycia mechanizmów synchronizacji
* Funkcje
	* `shm_open` - otwarce / utworzenia
	* `close` - zamknięcie
	* `shm_unlink` - usunięcie
	* `ftruncate` - nadanie wielkości
	* `mmap` - zmapowanie obszaru do przestrzeni adresowej procesu
	* `munmap` - odmapowanie

### Uruchamianie procesów
* Dwa podejścia do uruchamiania aplikacji wieloprocesowej
	* proces główny uruchamia inne procesy jako potomne
	* procesy uruchamiane niezależnie (np. z linii poleceń)
* `fork`
	* proces potomny dziedziczy otwarte pliki i kolejki komunikatów
	* do uruchomienia programu używa się `execve`
* Inne dostępne funkcje
	* `posix_spawn`
	* `clone`
	* `system`, `popen` - uruchomienie przez powłokę
## Możliwości rezerwacji rdzenia CPU - realizacja, do czego się przydaje, jak z tego skorzystać?
* Przydatne kiedy zdarzenie wymaga szybkiej obsługi przy aktywnym oczekiwaniu
* Funkcje
	* `sched_setaffinity`
	* `sched_getaffinity`

## Oczekiwanie na zdarzenie sprzętowe - oczekiwanie aktywne, wykorzystanie przerwań, porównanie tych rozwiązań. Rola sterownika urządzenia w oczekiwaniu z wykorzystaniem przerwań. Sposoby optymalizacji obsługi przerwań w sterownikach.
* Obsługa sprzętu w procedurze obsługi przerwania
	* jest asynchroniczna, nie trzeba czekać na przydział czasu od planisty
	* rozpoczęcie i zakończenie ma własny narzut
	* może być opóźnione przez przerwanie o wyższym priorytecie
* To czy aktywne oczekiwanie, czy przerwania dadzą lepszy wynik zależy od warunków pracy systemu
* Dla optymalizacji można podzielić obsługę przerwanie na
	* górną połówkę - zasadnicza obsługa, może wyłączyć inne przerwania
	* dolna połówka - odroczona procedura obsługi przerwania
	* obsługa dolnej połówki przez tasklets, workqueues lub theaded interrupts
## System przetwarzający dane zbudowany jest z aplikacji dwóch rodzajów - serwera, pobierającego dane z czujników pomiarowych i udostępniającego je przez bufor w pamięci dzielonej, oraz z programów klienckich. Liczba programów klienckich nie jest z góry znana i mogą one być uruchamiane i zamykane niezależnie. W jaki sposób programy klienckie powinny uzyskiwać dostęp do bufora w pamięci dzielonej? W jaki sposób powinniśmy zapewnić zwolnienie tego bufora przy kończeniu działania systemu?
* Bufor powinien być umieszczony w nazwanym obszarze pamięci dzielonej
* Dostęp do bufora musi wykorzystać odpowiedni dla parametrów systemu mechanizm synchronizacji (mutex, semafor, blokada zapis/odczyt, zmienne warunkowe)
	* muszą być nazwane i mieć znane, ustalone nazwy, lub znajdować się w tej samej pamięci współdzielonej co bufor
* Pamięć dzielona z buforem powinna być usuwana przez `shm_unlink` przez ostatni korzystający z niego proces
	* np. proces serwera po zakończeniu pracy

## W jaki sposób standardowe drzewo urządzeń systemu wbudowanego umożliwia opis ''maksymalnej'' konfiguracji tego systemu i ''aktualnie używanej'' konfiguracji? W jaki sposób możemy wybrać jakich podsystemów chcemy używać? W jaki sposób możliwe jest dostosowanie drzewa urządzeń do niestandardowych rozszerzeń, które dodaliśmy do systemu?
* Można to osiągnąć przez mechanizm nakładek na drzewo urządzeń
* *Maksymalna* konfiguracja w pliku drzewa urządzeń
	* opcjonalne podsystemy mają odpowiedni parametr - są domyślnie wyłączone 
	* `status = "disabled"
* Aktualnie używana konfiguracja
	* nakładka na bazowe drzewo urządzeń
	* korzysta z referencji (`&`) do węzłów zdefiniowanych w hierarchii drzewa urządzeń
	* nadpisuje wybrane parametry dla używanych urządzeń
	* `status = "okay"`
## Jak możemy zapewnić minimalny czas reakcji naszego oprogramowania (sterownika urządzenia i/lub programu w przestrzeni użytkownika) na oczekiwane zdarzenie sprzętowe. Proszę uwzględnić dwie możliwości: a) system z jednym rdzeniem CPU, b) system z kilkoma rdzeniami CPU.
* Z jednym rdzeniem
	* ustawienie wysokiego priorytetu
	* w zależności od potrzeb użycie odpowiedniego trybu szeregowania czasu rzeczywistego
	* obsługa z wykorzystaniem przerwania
* Z wieloma rdzeniami
	* zarezerwowanie rdzenia CPU pod to zadanie
	* obsługa z aktywnym oczekiwaniem
	* obsługa z wykorzystaniem przerwania i zarezerwowanie rdzenia wyłącznie na obsługę tego przerwania
## Dlaczego wykorzystanie DMA wymaga sterownika działającego w przestrzeni jądra?
* Sterownik musi komunikować się ze sprzętowym kontrolerem DMA
* Sterownik musi obsłużyć przerwanie zgłaszane przez kontroler DMA po zakończeniu transferu
## Proszę porównać komunikację między procesami za pomocą kolejek komunikatów z komunikacją za pomocą potoków. Proszę wymienić cechy wspólne i różnice.
* Kolejki i potoki mogą być nazwane
* Kolejki i potki zapewniają jednokierunkową komunikację między 2 procesami
* Kolejka przesyła dane zorganizowane w komunikaty (o określonej strukturze)
* Potok przesyła strumień bajtów
* Komunikatom w kolejce można ustawiać priorytety
## Na czym polega mapowanie rejestrów urządzenia w pamięć? Jak to jest realizowane? Jakie mechanizmy są tu niezbędne? Jakie potencjalne problemy są z tym związane? Jakie funkcje w języku C musimy wykorzystać aby móc odwołać się do tak udostępnionych rejestrów urządzenia?
* Adresy z wirtualnej przestrzeni adresowej procesu odpowiadają rejestrom urządzenia
	* można korzystać z obszaru pamięci jak ze struktury o określonych polach
	* rejestry jako pola struktury - pisanie i czytanie zmiennych
	* urządzenie jest podłączone do magistrali systemowej
* Potencjalne problemy
	* błędy wyrównania
	* zapis nieprawidłowej wartości może wysłać fizyczny sygnał na magistralę
	* optymalizacje kompilatora mogą spowodować nieprawidłowe działanie
	* optymalizacje odczytów z pamięci przez procesor mogą spowodować nieprawidłowe działanie
* Do mapowania pliku specjalnego `/dev/mem` do pamięci służy funkcja `mmap`
	* `open` i `close` do otwarcia / zamknięcia pliku

## W systemie komputerowym używanym do sterowania działa kilka procesów (nie wątków!). W pewnym momencie konieczne jest wstrzymanie działania pozostałych procesów do chwili, gdy jeden z nich zainicjalizuje pewną strukturę danych. Proszę opisać, jak należy rozwiązać ten problem. Jakiego mechanizmu synchronizującego należy użyć?
* Do rozwiązania problemu można użyć zmiennej warunkowej i mutexu
	* zmienna warunkowa pozwala wybudzić wszystkie oczekujące procesy
	* mutex zapewnia synchronizację dostępu do zmiennej warunkowej
* Pozostałe wątki kolejno pozyskują mutex i zawieszają się na zmiennej warunkowej
* Wątek inicjujący
	* pozyskuje mutex
	* inicjuje strukturę danych
	* wykonuje operację broadcast na zmiennej warunkowej
	* zwalnia mutex
* Oczekujące wątki są kolejno wybudzane po otrzymaniu sygnału i zwalniają mutex

## System komputerowy jest wyposażony w czterordzeniowy procesor. Dwa urządzenia peryferyjne wymagają bardzo szybkiej obsługi, przy czym potrzebę obsługi zgłaszają przez wygenerowanie przerwania (które można maskować) oraz przez zmianę wartości w swoim rejestrze statusu. Jak skonfigurować system, aby jak najlepiej spełnić wymagania tych dwóch urządzeń, a zarazem umożliwić realizację innych zadań?
* Aktywne oczekiwanie
	* oba urządzenia są obsługiwane w oddzielnych procesach
	* te procesy mają zarezerwowane po 1 rdzeniu procesora
	* przerwania są maskowane
	* obsługa wykorzystuje aktywne oczekiwanie na rejestrze statusu
* Przerwania
	* zarezerwować po 1 (oddzielnym) rdzeniu procesora na obsługę przerwań związanych z urządzeniem
* W obu przypadkach pozostają 2 wolne rdzenie na realizację innych zadań
* To, które rozwiązanie będzie lepsze może zależeć od różnych parametrów pracy systemu
	* najlepiej przeprowadzić pomiary w różnych warunkach

## W systemie komputerowym z procesorem ARM, pewne urządzenie peryferyjne jest podłączone do magistrali systemowej, przy czym do pracy wymaga pewnego sygnału zegarowego, który nie jest zawsze aktywny. W jaki sposób system operacyjny powinien zostać poinformowany o potrzebie włączenia tego sygnału, oraz o adresach rejestrów tego urządzenia i wykorzystywanej przez nie linii przerwań?
* Adresy rejestrów i inne informacje są określone w drzewie urządzeń
* Do obsługi podłączonego urządzenia w czasie pracy systemu można użyć `udev` z odpowiednimi regułami
* Po wykryciu podłączenia urządzenia do magistrali systemowej (np. przez monitorowanie jej stanu) można dynamicznie załadować nakładkę na drzewo urządzeń aktywującą sygnał zegarowy
	* potencjalnie niebezpieczna operacja

## Co to są bufory rozproszone (SG) z czego wynika potrzeba ich stosowania?
* Zaalokowanie dużego ciągłego bufora może nie być możliwe
* Proste urządzenia używające DMA potrzebują dużych ciągłych buforów do transferów danych
* Bufory rozproszone składają się z wielu mniejszych segmentów i deskryptorów
	* tworzą listę
## W systemie komputerowym (pracującym pod kontrolą Linuxa) zbierającym dane i sterującym na ich podstawie pewnym urządzeniem działa kilka procesów: Proces "A" obsługuje czujniki pomiarowe, przetwarza ich dane i na ich podstawie generuje sygnały sterujące. Proces "B" obsługuje graficzny interfejs użytkownika, wyświetlając przebiegi mierzonych parametrów dla operatora nadzorującego urządzenie. Proces "C" zajmuje się archiwizacją danych pomiarowych i komend sterujących, w celu ewentualnej późniejszej analizy zaistniałych nieprawidłowości. Proszę zaproponować, uzasadniając, jakie parametry szeregowania powinny zostać nadane poszczególnym procesom.
* Proces A
	* najwyższy priorytet
	* kluczowe dla działania systemu
	* opóźnienia powinny być możliwie jak najniższe
	* można użyć trybu czasu rzeczywistego, np. `SCHED_DEADLINE` zależnie od potrzeb
* Proces B
	* średni priorytet
	* GUI powinno być wystarczająco responsywne, ale tolerowane opóźnienia są na ogół większe
* Proces C
	* najniższy priorytet
	* zadanie nie jest krytyczne czasowo
	* proces może działać w tle
	* ważniejsze jest poprwane działanie niż szybkość reakcji
## Czy do synchronizacji dostępu do danych, współużywanych przez dwa procesy, mogę użyć semafora, tworzonego jako globalna zmienna statyczna, przed wywołaniem funkcji "fork"? Jeśli nie, to dlaczego i jak poprawie utworzyć taki semafor?
* Nie można, proces potomny ma własną, oddzielną kopię globalnej zmiennej semafora
* Poprawne użycie to wykorzystanie nazwanego semafora lub semafora w pamięci współdzielonej
	* należy ustawić flagę do pracy z wieloma procesami
## Jakie jest zastosowanie nakładek na drzewo urządzeń? Kiedy i jak je stosujemy? Odpowiedź może być oparta na konkretnych rozwiązaniach dla Raspberry Pi.
* Pozwala dostosować konfigurację sprzętu (z drzewa urządzeń) do własnych potrzeb
* Nakładka może być użyta do modyfikacji drzewa urządzeń przez bootloader
* Można załadować nakładkę podczas pracy systemu przez `dtoverlay` ale to potencjalnie niebezpieczne
## Co powinniśmy zrobić, żeby w Linuksie zbudowanym za pomocą środowiska OpenWRT (np. w pobranej prekompilowanej wersji) zapewnić automatyczne uruchomienie karty dźwiękowej USB po jej podłączeniu do systemu?
* Zainstalować program `udev` / `eudev`
* Dodać właściwą regułę dla karty wybranej karty dźwiękowej
* Upewnić się że działa daemon

## Na czym polega mapowanie rejestrów urządzenia w pamięć aplikacji? W przypadku jak podłączonych urządzeń daje się zastosować takie podejście? Jakie są zalety i wady takiego rozwiązania?
* Urządzenie musi być podłączone do magistrali systemowej
* Fizyczne rejestry urządzenia są widoczne pod określonymi adresami w przestrzeni adrresowej procesu (po zmapowaniu przez `mmap`)
* Zalety
	* możliwosć odwoływania się do rejestrów jak do zwykłych zmiennych
	* proste sterowniki można tworzyć w przestrzeni użytkownika
* Wady
	* możliwe błędy wyrównania
	* możliwe błędy wynikające z cahce'owania, optymalizacji kompilatora i procesora (trzeba wyłączać dane mechanizmy)

## W jaki sposób możemy za pomocą drzewa urządzeń włączać i wyłączać komponenty systemu? W jaki sposób możemy dodawać do drzewa urządzeń informacje o nowo dołączonych urządzeniach?
* Przez zastosowanie mechanizmu nakładek na drzewo urządzeń
	* nakładane z poziomu bootloadera
	* nakłądane podczas pracy systemu przez `dtoverlay` (niebezpieczne)
* Włączanie/wyłączanie
	* komponent jest zdefiniowany w bazowym drzewie urządzeń jako wyłączony
	* nakładka odwołuje się do węzła z bazowego drzewa i nadpisuje jego status na aktywny
* W nakładce możne dodać nowy komponent, nieznajdujący się w bazowym drzewie (nowy węzeł)

## Pewne urządzenie może obsługiwać równocześnie maksymalnie 4 zlecenia. Jaki mechanizm pozwoli najłatwiej zsynchronizować dostęp do niego tak, aby zapewnić spełnienie tego warunku? Czym różni się użycie tego mechanizmu w następujących sytuacjach: a) o dostęp do tego urządzenia konkurują różne wątki tego samego procesu; b) o dostęp do tego urządzenia konkurują różne procesy.
* Można użyć semafora inicjowanego wartością 4
	* liczba jest znana
	* zapewni, że tylko tyle procesów / wątków może mieć jednocześnie dostęp
* Konkurują wątki jednego procesu
	* semafor może być zmienną globalną
	* przestrzeń adresowa jest wspólna dla wątków w obrębie jednego procesu
* Konkurują różne procesy
	* przestrzenie adresowe są izolowane
	* trzeba użyć semafora nazwanego lub semafora w pamięci współdzielonej

## Jak działa tryb szeregowania terminowego (SCHED_DEADLINE)? Jakimi parametrami opisujemy wymagania dotyczące szeregowania procesu? Jakie wymagania są weryfikowane przez system?
* Służy do szeregowania okresowych zadań czasu rzeczywistego
* Parametry
	* runtime - czas wykonywania
	* deadline - termin
	* period - okres
* Proces powinien zakończyć działanie przed upływem czasu wykonania
	* `sched_yield`
	* zablokowanie się na IO
* Jeśli proces nie wyrobi się przed końcem czasu zostanie zawieszony do następnego okresu
* System weryfikuje spełnienie warunku $runtime \le deadline \le period$

## Pewna struktura danych, umieszczona w pamięci współdzielonej (shared memory) jest często odczytywana przez wiele procesów, a dość rzadko modyfikowana przez małą liczbę procesów. Jakiego prymitywu synchronizacyjnego powinniśmy użyć do synchronizacji dostępu wszystkich użytkowników tej struktury? Gdzie powinien on być umieszczony? Jak powinien on być zainicjalizowany?
* Można użyć blokady zapisu/odczytu
	* pozwoli na wydajny, jednoczesny dostęp wielu konsumentów
* Powinna być umieszczona w pamięci współdzielonej
	* np. w tym samym bloku co wspomniana struktura
* Powinna być zainicjowana z flagą umożliwiającą synchronizację procesów

## W jakim celu wprowadzono mechanizm podziału procedury obsługi przerwania na dwie części? Proszę opisać przynajmniej dwie możliwe realizacje tego mechanizmu.
* Mechanizm wprowadzono w celu optymalizacji
	* oddzielenie górnej połówki blokującej inne przerwania od dolnej (odroczonej)
* Sposoby obsługi dolnej połówki
	* tasklets - w kontekście obsługi przerwania
	* workqueue - w kontekście procesu

## Używamy systemu wbudowanego z procesorem ARM. Skąd system Linux uzyskuje informacje, jaki sterownik wybrać do obsługi konkretnego urządzenia sprzętowego? W jaki sposób dowiaduje się, jak uzyskać dostęp do jego rejestrów? Co i jak możemy zmienić w konfiguracji systemu, żeby umożliwić obsługę nowo dołączonego urządzenia?
* Informacje o sterownikach, adresach mapowania rejestrów itp znajdują się w drzewie urządzeń
* Nowe urządzenia można obsłużyć przez załadowanie nakładki na drzewo urządzeń

## Strategie szeregowania zadań
* Szeregowanie stałe
	* znany, powtarzalny rozkład zadań
	* długie okresy powtarzania (w stosunku do czasu wykonania)
	* cykliczny program sekwencyjny (bez wywłaszczania)
* Szeregowanie na bieżąco
	* brak powtarzalnego schematu wykonania zadań
	* czasy wkonania przekraczają okresy powtarzania
	* system wielozadaniowy z wywłaszczaniem

## Algorytm RMS
* Rate Monotonic Scheduling
* Priorytety zadań proporcjonalne do częstotliwości
* Optymalny warunek stało-priorytetowy
* Warunek dostateczny $\sum_{i=1}^n t_i/c_i \le n(2^{1/n} - 1)$
	* $n$ - liczba zadań
	* $t_i$ - czas wykonania
	* $c_i$ - okres powtarzania

## Algorytm EDF
* Earliest Deadline First
* Priorytety zadań związane z terminem zakończenia
* Optymalny algorytm zmienno-priorytetowy
* Warunek dostateczny $\sum_{i=1}^n t_i/c_i \le 1$

## Zadania sporadyczne
* Charakterystyka
	* nieznany z góry czas zgłoszenia
	* możliwe zgłoszenia *stadne* (wiele, nagle)
* Obsługa w tle
	* niższy priorytet od zadań cyklicznych
	* nie narusza terminów zadań cyklicznych
	* długi czas odpowiedzi dla zadań sporadycznych
* Obsługa w przerwaniach
	* najwyższy priorytet
	* krótki czas odpowiedzi zadań sporadycznych
	* możliwe opóźnienia zadań cyklicznych

## Serwer sporadyczny
* Zadanie obsługujące zgłoszenia sporadyczne
* Parametry
	* $s$ - budżet czasu
	* $c$ - okres odnowienia
	* $p$ - wysoki priorytet
	* $l$ - niski priorytet
* Algorytm
	* przez czas $s$ pracuje na priorytecie $p$
	* pracuje na priorytecie $l$
	* po okresie $c$ odnawia budżet i znowu pracuje na priorytecie $p$


## Bezpieczeństwo
### Bezpieczeństwo
Brak nieakceptowalnego ryzyka śmierci lub uszczerbku na zdrowiu człowieka wynikającego z działania systemu lub pośrednio z uszkodzenia środowiska

### System związany z bezpieczeństwem
System, którego prawidłowe działanie jest niezbędne do zapewnienia lub utrzymania bezpieczeństwa ludzi

### Zdarzenie zagrażające
Zdarzenie którego wynikiem jest fizyczny uraz lub pogorszenie stanu zdrowia ludzi, zarówno bezpośrednio jak i pośrednio na skutek szkód w środowisku

### Ryzyko
Prawdopodobieństwo $\times$ stopień szkodliwości

### Funkcja bezpieczeństwa
Funkcja przeznaczona do utrzymania bezpiecznego stanu instalacji w odniesieniu do konkretnego zdarzenia zagrażającego. Może być integralną częścią sterownika lub odrębnym urządzeniem

## Analiza drzewa niezdatności
* Fault Tree Analysis (FTA)
* Analiza systemu i celów jego działania
* Identyfikacja zdarzeń zagrażających
* Budowa drzewa niezdatności dla każdego zdarzenia
* Badania drzewa w celu określenia
	* zdarzeń prostych powodujących uszkodzenie systemu
	* oszacowanie tolerancji na uszkodzenia
	* prawdopodobieństwa uszkodzenia systemu
	* lokalizacji elementów krytycznych

## Cykl utrzymania bezpieczeństwa
* Identyfikacja i ocena zagrożeń
* Analiza bezpieczeństwa
* Określenie i alokacja wymagań bezpieczeństwa
* Planowanie i realizacja funkcji bezpieczeństwa
* Ocena i zatwierdzenie
* Eksploatacja obsługa, naprawy

## Poziom nienaruszalności bezpieczeństwa
* Safety Integrity Level
* Od 1 do 4
* Prawdopodobieństwo, że system wykona wymagane funkcje bezpieczeństwa w zadanych warunkach i czasie
* Tryby pracy
	* na rzadkie przywołanie - prawdopodobieństwo nie zadziałania w trakcie obsługi
	* na częste lub ciągłe przywołanie - prawdopodobieństwo nie zadziałania na godzinę
* Szacowane na podstawie
	* skutków awarii
	* częstotliwości / czasu przebywania ludzi w warunkach zagrożenia
	* nieuchronności zagrożenia
	* prawdopodobieństwa zdarzenia

## Protokoły dostępu do kabla

### Ehernet CSMA/CD
* Działanie
	* obserwacja stanu kabla i nadawanie jeśli wolny
	* przerwanie nadawania po wykryciu kolizji
	* odczekanie losowego czasu i ponowna próba
* Właściwości
	* niedeterministyczny czas
	* minimalna długość komunikatu
	* bardzo szybka transmisja

### Odpytywanie
* Węzeł master i węzły slave
	* węzeł master odpytuje węzły slave
	* węzły slave odpowiadają na zapytania
	* węzły slave nadają tylko w odpowiedzi na zapytanie węzła master
* Właściwości
	* czas przekazu określa master
	* awaria mastera zatrzymuje całą sieć
	* brak komunikacji między węzłami slave
	* brak kolizji
	* możliwe krótkie komunikaty

### Przekazywanie znacznika
* Znacznik - przechodnie prawo nadawania
* Właściwości
	* deterministyczny czas przekazu
	* możliwe krótkie komunikaty
	* równoprawne węzły
	* narzut przekazywania znacznika
* Problemy
	* utrata znacznika
	* rozmnożenie znacznika
	* dołączanie nowego węzła
* Można połączyć z odpytywaniem

## I2C
* Szyna
	* linia danych SDA
	* linia zegara SCL
* Jeden master i wiele slave
	* slave wybierany po numerze (adresie)
* Komunikacja przez ramki
	* start
	* adres
	* odczyt/zapis
	* potwierdzenie
	* dane
	* potwierdzenie
	* stop
* Zastosowania
	* sterowanie audio, video
	* odczyt EPROM i RTC
	* sterowanie LED/OLED
	* dostęp A/C, C/A i czujników
	* pętle regulacji
	* włączanie zasilania modułów
* Driver w jądrze Linuxa
	* zapis
	* odczyt
	* transfer

## Standardy

### Interbus
* Topologia
	* główna magistrala - master i slave
	* lokalne magistrale - peryferia
* Protokół dostępu
	* odpytywanie
	* jeden master

### CAN bus
* Topologia magistrali
* Protokół bezpołączeniowy
* Rozgłaszanie komunikatów
* Bez adresowania węzłów
* Arbitraż kolizji
* Stan 0 dominujący przy nadawaniu

### Profibus
* Topologia magistrali z odgałęzieniami
* Wiele węzłów master z przekazywaniem znacznika
* Wiele węzłów slave - odpytywanie
* Zdefiniowana warstwa aplikacyjna
	* API
	* słownik obiektów
	* klient-serwer
	* określenie dostępnych usług
	* definiowane relacje komunikacyjne

### EtherCAT
* Ethernet ze zmienioną warstwą MAC
* Sprzęg sieciowy
	* master - karta ethernet + software
	* slave - sprzętowy (ASIC/FPGA)
* Ramki Ethernet
* Warstwa aplikacyjna CANopen

## Ethernet przemysłowy
* Szybki
* Wykorzystuje standardowe narzędzia
* Łatwy do integracji ze standardowymi sieciami Ethernet
* Standardowe lub własne / zmodyfikowane protokoły modelu ISO/OSI