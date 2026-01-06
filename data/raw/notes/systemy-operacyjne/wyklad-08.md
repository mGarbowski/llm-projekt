# Wykład 8 (2023-11-21)

## O zadaniu
* Wywołania systemowe
* Fork
* Algorytmy szeregowania z wywłaszczaniem i bez wywłaszczani
* Przeanalizować obecny algorytm szeregowania, na tym musi bazować koncepcja

Pytanie na kolokwium o pełny graf przejść stanów procesu w System V

Scheduler rozpatruje tlyko procesy uruchomione lub gotowe do uruchomienia
Szeregowanie bez wywłaszczania nie dzieli czasu na kwanty, tylko czeka się na przerwanie systemowe
- nie nadają się do systemów interaktywnych ale są bardziej wydajne do zadań intensywnych obliczeniowo

## Stany procesów
Proces który w poprzednim kwancie czasu był wykonywany ma flagę preempted (wywłaszczony)
Proces przechodzi do stanu preempted po wyjściu z wywołania systemowego
Jesli nie ma lepszego kandydata najlepiej wybrać ten wywłaszczony bo jest załadowany cache

### Stan zombie
* Proces może być tworzony tylko przez fork
* Pamięć procesu jest chroniona
* Jest gwarantowane że zawsze będzie można zobaczyć kod wyjścia procesu dziecka

Jeśli proces dziecko się zakończył to nie ma potrzeby trzymać jego zasobów ale trzeba dostarczyć kodu wyjścia jeśli proces rodzic
o to zapyta.
Kod wyjścia jest przechowywany jako jedno z pól w strukturze reprezentującej proces w tablicy procesów.

Proces zombie ma zwolnioną pamięć, nie reaguje na sygnały, zostaje tylko wpis w tablicy procesów, istnieje tylko po to żeby przepisać kod wyjścia.

Proces zombie ma ustawioną flagę `IN_USE`

Tablica deskryptorów emuluje zachowanie listy dynamicznej ale jest tablicą bo tak jest wydajniej

Zombie już nie żyje i nie można go zabić (sygnał 9 SIGKILL)

Po zakończeniu wykonania procesu nadrzędnego, procesy potomne zostają sierotami
Każdy proces sierota jest natychmiastowo przejmowany przez proces init (zostaje procesem dzieckiem procesu init)
Init wykonuje w nieskończonej pętli `wait` umożliwiając odejście procesów sierot

Procesy zaczynają się od pid=1 (proces init)

## Planista
Tablica deskryptorów nie musi być zrealizowana jako tablica, jest kwestią implementacyjną danego systemu programowania
(w Minixie to zwykład tablica w C)

Element tablicy (struktura) opisujący proces to deskryptor procesu

Zwykłe dane procesu (TEXT, DATA, STACK) znajdują się w jego pamięci
Metadane procesu wykorzystywane przez planistę to mała struktura w pamięci jądra
(priorytet do algorytmu szeregowania, informacje statystyczne ile dany proces się wykonuje)

## Typowa budowa deskryptora procesu
* Zarządzanie procesem
    * Rejestry
    * Licznik instrukcji
    * Słowo stanu procesora
    * Wskaźnik stosu
    * stan procesu (READY, RUNNING, BLOCKED)
    * priorytet
    * Parametry szeregowania
    * ID procesu
    * Proces rodzic
    * Grupa procesu
    * Sygnały
    * czas startu procesora
    * użyty czas CPU
    * czas następnego alarmu
* Zarządzanie pamięcią
    * Wskaźnik do segmentu kodu
    * Wskaźnik do segemntu danych
    * Wskaźnik do segmentu stosu
* Zarządzanie plikami
    * Katalog root (umożliwia separację, już raczej nie stosowany ale ważne np przy instalowaniu bootloadera)
    * Katalog bieżący
    * Deskryptory plików
    * ID użytkownika
    * ID grupy

## Obsługa przerwań
* Odebranie czasu procesora na rzecz planisty po przerwaniu zegarowym
* Procesor ma jedną linię połączenia z kontrolerem przerwań
* Wskaźniki na funkcje obsługi przerwań są trzymane w tzw wektorze przerwań, indeksowane numerem przerwania

Jądro systemu właściwie składa się ze sterowników urządzeń zewnętrznych i funkcje obsługujące ich przerwania

### Przebieg
* Sprzętowo zapamiętanie na stosie licznika rozkazów itd
* Sprzętowe załadowanie nowej wartości licznika rozkazów z wektora przerwań (`jmp`, `call`)
* Procedura assemblerowa zapamiętuje wartość rejestrów
* Procedura assemblerowa ustala nowy stos
* Obsługa przerwania w języku C (często odczyt i buforowanie wejścia)
* Planista wybiera następny proces do wznowienia
* Procedura w języku assemblera przygotowuje i wznawia nowy bieżący proces


## Wątki
Proces dostarcza środowisko uruchomieniowe dla strumienia przetwarzania i ma zapewnioną ochronę pamięci
Wątki nie są chronione w obrębie jednego procesu

Wątki mogą komunikować się przez wspólną pamięć procesu, wymagają jawnej synchronizacji

Przekazanie danych - komunikacja, wymuszenie porządku - synchronizacja

Błąd w kodzie wykonywanym przez wątek może nadpisać/zamazać pamięć innego wątku

### Wady
* Nie umożliwiają rzeczywistej równoległości
* Nie można podzielić jednego procesu na wiele węzłów

