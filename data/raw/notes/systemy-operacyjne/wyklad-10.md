# Synchronizacja procesów (2023-12-05)

Nawet jak jest tylko jeden rdzeń to lepiej mieć wiele procesów w pamięci głównej, żeby móc przełączać na IO. Nie może też być za dużo bo większość wyląduje na swapie i będzie spowalniać działanie

## Algorytmy szeregowania
W systemach wsadowych
* First-Come First-Served - kolejka FIFO
* SJF - najszybciej najkrótsza praca
* SRTN - shortest remaining time next
* szeregowanie trzypoziomowe (Three-Level Scheduling)


### Szeregowanie trzypoziomowe
* CPU scheduler - planista w jądrze systemu
* Admission scheduler - kolejka uruchamiająca zadania
* Memory scheduler


### Szeregowanie z klasami priorytetowymi
Priorytet można dynamicznie zmieniać (np zmniejszać w miare zużywania czasu procesora)

### Szeregowanie w systemach czasu rzeczywistego
Ograniczenia twarde i miękkie (nie są faktycznie real-time)
System real-time nie musi być szybki, musi być pewny
QNX, RT Linux (nie jest tak naprawdę Linuxem)

System jest szeregowalny musi spełniać

$$
\sum_{i=1}^m \frac{C_i}{P_i} \le 1
$$

* $C_i$ - czas wykonania zadania okresowego
* $P_i$ - okres wykonania zadania okresowego

# Wzajemne wykluczanie i synchronizacja
Jest dużo linków i materiałów na stronie

## Wyścig
Race conditions

Sytuacja w której dwa lub więcej procesów wykonuje operację na zasobach dzielonych, a ostateczny wynik tej operacji jest zależny od momentu jej realizacji

## Sekcja krytyczna
Fragment programu, w którym występują instrukcje dostępu do zasobów dzielonych. Instrukcje tworzące sekcje krytyczne muszą być poprzedzone i zakończone operacjami realizującymi wzajemne wykluczanie.

Potężny koszt wydajnościowy ale są konieczne żeby poprawnie wykonać algorytm.
Im mniejsza ziarnistość tym mniejsze będą spowolnienia i lepsza wydajność

Mechanizmy do realizowania wzajemnego wykluczenia muszą być dostarczone przez system operacyjny

### Warunki konieczne implementacji sekcji krytycznej
* Wewnątrz sekcji krytycznej może przebywać tylko jeden proces
* Jakikolwiek proces znajdujący się poza sekcją krytyczną, nie może zablokować innego procesu pragnącego wejść do sekcji krytycznej
* Każdy proces oczekujący na wejście do sekcji krytycznej powinien otrzymać prawo dostępu w rozsądnym czasie

### Mechanizmy realizujące wzajemne wykluczanie
* Mechanizmy z aktywnym oczekiwaniem na wejście do sekcji krytycznej
	* blokowanie przerwań
	* zmienne blokujące - niepoprawne
	* ścisłe następstwo - niepoprawne
	* algorytm Petersona
	* instrukcja TSL
* Mechanizmy z zawieszaniem procesu oczekującego na wejście do sekcji krytycznej
	* proces jest zatrzymywany przez jądro, czeka aż będzie mógł wejść do sekcji
	* sleep i wakeup - niepoprawne
	* semafory
	* monitory
	* komunikaty

Niepoprawne też trzeba znać - nie robić takich błędów
Wszystkie trzeba znać i rozumieć, na pewno będą na kolosie i egzaminie


### Blokowanie przerwań
Przerwanie zegarowe też jest zablokowane, więc nie wzbudzi się planista więc nie przełączy się na żaden inny proces i nie zostanie przerwany.

Nie nadaje się do procesów użytkowych ale może być ok w implementacji jądra (ale się ich unika)

### Zmienne blokujące - **niepoprawne**
Odczytanie zmiennej i zapisanie zmiennej to dwie oddzielne instrukcje - pomiędzy może się wcisnąć inny proces (nastąpi przełączenie kontekstu)

Oba procesy wejdą do sekcji krytycznej, bo drugi proces odczyta flagę zanim pierwszy zdążył ją zapisać

Trzeba umieć wyjaśnić czemu to nie działa!

### Ścisłe następstwo
Strict alteration, "algorytm brytyjskich dżentelmenów"

zmienna `turn` i pętla sprawdzająca czy moja kolej 

Nie ma wyścigu ale jest możliwe zagłodzenie

Proces poza sekcją, przez niepodanie pozwolenia może zablokować inny proces od wejścia do sekcji krytycznej

### `sleep` i `wakeup` - **niepoprawne**
Dla problemu producent - konsument

`wakeup` może zostać wysłany zanim drugi pójdzie spać
sprawdzenie stanu bufora i wywołanie `sleep` to oddzielne instrukcje, pomiędzy może być context switch

sygnał wakeup zostanie utracony


### Semafor
Jest jak zmienna...

Zmienna nazywana semaforem jest inicjowana nieujemną wartością całkowitą i zdefiniowana poprzez definicje niepodzielnych operacji P(s) i V(s)  (z holenderskiego)

P - jeśli <= 0 czekaj, opuszczenie semafora o 1
V - podniesienie semafora o 1

Jak proces ma pójść spać - każdy proces ma swój indywidualny semafor zainicjowany na 0, kiedy idzie spać ustawia go na 1, ustawienie go przez inny proces z porotem na 0 go obudzi

wakeup nie zostanie zgubione tylko zmieni wartość semafora