# Procesy i wątki (2023-11-14)

Program nie ma stanu, jest reprezentacją algorytmu
Proces to wykonujący się program wraz z jego śrdoowiskiem obliczeniowym.
Proces stanowi podstawowy obiekt dynamiczny w systemie operacyjnym

Kontekst to np. zmienne środowiskowe, zawartość rejestrów, pamięci

## Wymagania systemu zarządzania procesami
* Umożliwienie przeplatania się wykonywania procesów
* Akceptowalnie krótki czas odpowiedzi systemu
* Zarządzanie przydziałem zasobów poszczególnym procesom
* Udostępnienie mechanizmów do komunikacji międzyprocesowej
* Udostępnienie mechanizmów do tworzenia procesów

Procesor wykonuje na przemian kod procesów i planisty (scheduler), nigdy proces od razu po procesie
Każdy proces ma atrybut stanu (tylko jeden z procesów w stanie READY będzie wybrany do wykonania przez scheduler)

System operacyjny to ogólnie jądro systemu i grupa procesów (petentów oczekujących na usługę)

Na maszynie wieloprocesorowej dalej jest tylko jedno jądro systemu, tylko inaczej zarządza procesami

Wzbudzenie schedulera kosztuje czas procesora

W oryginalnym Unixie było 18 przerwań na sekundę, dzisiaj sa rzędu >10000 ze względu na wymagania czasowe z przetwarzaniem multimediów
Unix nie nadaje się jako system do przetwarzania multimediów

Jeśli może być wiele procesów, to jądro musi zapewniać mechanizmy do komunikacji międzyprocesowej

## Wieloprogramowanie
* procsy współbieżne - nie ma wymogu, żeby kolejny proces startował po zakończeniu poprzedniego (nie muszą być szeregowe)
* procesy równoległe - może istnieć chwila czasu, kiedy wykonują się dokładnie w tej samej chwili czasu (nie muszą ale nie można tego wykluczyć)
    * musi być więcej niż jedno ALU (w praktyce wiele rdzeni, wiele procesorów)
    * przereklamowana? (zysk zależy od poziomu ziarnistości dekompozycji problemu, są obliczenia które świetnie się nadają do zrównoleglania (grafika))
* procesy rozproszone - wykonują się na sprzęcie rozproszonym
    * Nie mają współdzielonej pamięci
    * Scentralizowany sprzęt nie wymaga komunikacji sieciowej
    * Są z założenia równoległe

## Tworzenie i kończenie procesów
Utworzenie procesu może być rezultatem
* inicjalizacji systemu
* wywołanie funkcji systemowej przez działający proces 
* zlecenia użytkownika utworzenia nowego procesu
* uruchomienia zadania wsadowego
* w UNIXie
    * wszystko poza inicjalizacją obsługuje funkcja `fork`
    * `/etc/inittab` opisuje działanie procesu init

Zakończenie działania procesu
* zakończenie działania algorytmu (`return 0;`)
* celowe zakończenie w wyniku wystąpienia błędu
* wykonanie niedozwolonej operacji (wymuszone zakończenie, np SegFault)
* otrzymanie sygnału od innego procesu (zakończenie wymuszone)
    * informacją jest numer sygnału
    * proces może przygotować się na obsługę sygnału
    * jeśli nie ma funkcji obsługi to proces od razu zostanie zabity
    * 15 Terminate - proces powinien zamknąć pliki, wypłukać bufory itp (graceful)
    * 9 Kill - zabija natychmiast
    * można obsługiwać w językach programowania i w skryptach shellowych
    * Kill nie zabije procesu zombie (nie żyje, ma zwolnione zasoby ale jest na liście procesów)


## Graf przejść stanów procesów
* Running
* Ready
* Blocked

Nie można przejść ze stanu blocked to stanu running

* Running -> Blocked - blokowanie oczekiwania na IO
* Running -> Ready - scheduler wybrał inny proces
* Ready -> Running - scheduler wybrał ten proces
* Blocked -> Ready - koniec operacji IO, po przyjściu przerwania informującego o gotowości wyniku operacji IO

Funkcja obsługi przerwania powinna być możliwie krótka

W prawdziwych systemach graf jest bardziej skomplikowany

wywłaszczenie procesu - gorsza wydajność algorytmu szeregowania ale lepsza reaktywność systemu obsługującego multimedia

procesy zombie - na następnym wykładzie
