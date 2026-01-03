# x86 (2023-03-27)

## Jednostka zmiennopozycyjna x87
* 8 rejestrów 80-bitowych tworzących stos
* st0 - aktualny wierzchołek stosu
* ładowanie i składowanie przesuwa wierzchołek stosu
* st0 jest zawsze akumulatorem

## Wspieranie formaty
* IEEE754 binary32 (float)
* IEEE754 binary64 (double)
* Binary80 (specyficzny dla x87)
* Całkowitoliczbowy BCD
* Wszystkie dane są wewnętrznie przetwarzane jako Binary80, formaty służą do wymiany z pamięcią

## Jednostka wektorowa MMX/3DNow
(stara)

* na wektorowych danych stałopozycyjnych
* 8 64-bitowych rejestrów MM0, MM1, ... MM7
* nałożone w modelu programowym na rejestry x87 - nie można używać obu na raz
* są specjalne instrukcje do zainicjowania logiki stosu

## Architektura x86-64

* zgodna z x86
* Rejestry stałopozycyjne rozszerzone do 64 bitów
* 8 dodatkowych rejestrów R8..15 - jakościowa zmiana względem x86, lepsze wykorzystanie przez kompilatory
* Każdego rejestru można używać w trybie 64, 32, 16 i 8 bitowym
* operacje na danych 32-bitowych powodują zerowanie górnej połowy rejestru
* rozbudowana jednostka wektorowa SSE/AVX
  * XMM0..15 / YMM0..15
* W trybie 64-bitowym usunięto niektóre nieużywane instrukcje

### Tryby adresowania
* 8 lub 32-bitowe przemieszczenie
* zastąpienie trybu absolutnego trybem z bazą w PC - wymusza umieszczenie sekcji danych statycznych blisko sekcji kodu

### Jednostka wektorowa SSE
128-bitowe rejestry danych wektorowych

#### Obsługiwane formaty
* Zmiennopozycyjne
  * 2 * double
  * 4 * float
  * 8 * 16b


### Jednostka wektorowa AVX
* 256-bitowe rejestry
* wspiera wszystkie instrukcje SSE
* nowe, 3-argumentowe instrukcje


### Jednostka wektorowa AVX-512
* 512-bitowe rejestry
* wycofana
* rejestr predykatów
* rejestry ZMM0..31


## Format instrukcji 
Od 1 do 15 bajtów

* prefiksy (opcjonalnie) 0B..4B
* kod operacji 1B..3B
* ModRM - bajt specyfikacji argumentów 0B..1B
* SIB - rejestr bazowy, docelowy i skala 0B..1B
* przemieszczenie 0B..4B
* stała natychmiastowa 0B..4B

Procesor nie interpretuje instrukcji dłuższych niż 15 bajtów


## Długość argumentów stałopozycyjnych
* Asembler x86 określa długość argumentów na podstawie użytej nazwy rejestru
  * trzeba podać jawnie w instrukcjach pamięć-stała
* Jeden bit kodu operacyjnego określa długość (np. 32 albo 8 bitów, zależnie od trybu), dodatkowo są wykorzystywane prefiksy do innych ustawień


## Podstawowe instrukcje
### Przesyłanie
* mov - kopiowanie
* xchg - zamiana miejscami
* movsx - kopiowanie z rozszerzeniem bitu znaku
* movzx - kopwiowanie z rozszerzeniem zerami
* push, pop - operacje na stosie
* bswap - zamiana klejności bajtów w rejestrze (np konwersja z big-endian)

### Arytmetyka
* inc, dec - modyfikują znaczniki zera i znaku
* not - negacja bitów, bez ustawiania znaczników
* neg - zmiana znaku
* add, adc - zwykłe i z przeniesieniem wchodzącym (ze znacnzika)
* sub, sbb - zwykłe i z pożyczką wchodzącą (znacznik przeniesienia)
* cmp - porównanie (ustawienie znacznika)
* and, or, xor
* test - test logiczny z ustawieniem znaczników

### Przesunięcia i rotacje
O stałą albo zmienną w rejestrze CL

* shl, shr - przesunięcie z dopełnieniem zerami
* sar - arytmetyczne w prawo
* rol, ror - rotacja
* rcl, rcr - rotacja przez znacznik przeniesienia
* shld, shrd - ?

### Instrukcja LEA
* Load Effective Address
* ładuje adres do rejestru, mie przesyła danych
* służy do obliczenia adresu bazowego struktury (albo tablicy struktur) i następnie prosto adresować atrybuty
* może być użyta do 2, 3 lub 4-argumentowego dodawania / mnożenia / przesuwania
* ładuje jakąś liczbę, która może być wyrażeniem adresowym
* np. `a  *= 3` - `LEA EAX, [EAX + EAX*2]`
* nie ustawia znaczników

### Operacje bitowe
* bt, btc, btr, bts - test wartości bitu (z zerowaniem, negacją, ustawieniem)
* bsf/bsr - szukanie bitu o wartości 1
* popcnt - zliczanie jedynek w słowie
* lzcnt - zliczanie zer wiodących

### Mnożenie i dzielenie
Dziwne

3 sposoby zapisu mnożenia
* jednoargumentowe
  * komplementarne do dzielenia
  * wynik 2* dłuższy od argumentów
* dwuargumentowe
  * normalne, wynik w argumencie docelowym, nie może być stałej
  * wynik o długości argumentów
* trójargumentowe
  * rejestr docelowy, zmienna w rejestrze / pamięci, stała natychmiastowa 
  * potrzebne do indeksowania tablic
  * wynik o długości argumentów

2 instrukcje
* MUL - bez znaku, tylko jednoargumentowe
* IMUL - ze znakiem (1, 2 i 3-argumentowe)

Dzielenie i mnożenie jednoargumentowe
* jawny argument - mnożnik / dzielnik
* domyślne argumenty - mnożna, dzielna - różne rejestry (tabelka)
* trzeba uważać na zamazywanie rejestrów
* sensowne tylko wtedy kiedy potrzeba wyniku o pełnej długości
* dzielenie generuje jednocześnie iloraz i resztę
* dzielna jest zawsze 2 razy dłuższa od dzielnika
* dzielna w parze rejestrów, iloraz w jeddnym, reszta w drugim
* żeby podzielić 32-bity przez 32-bity, zawsze trzeba rozszerzyć dzielną (wyzerowanie albo przekopiowanie znaku dla liczb ze znakiem)
* instrukcje cbw, cwd, cdq, cqdq - kopiowanie znaku przed dzieleniem
* jeśli nie ustawi się górnej połówki to najczęściej wyleci błąd - (w Unixach błąd zmiennopozycyjny?!?!)


### Operacje na znacznikach
* clc, stc, cmc - zerowanie, ustawienie, negacja znacznika przeniesienia
* lahf, sahf - kopiowanie między najmniej znaczącym bajtem EFLAGS i rejestrem AH
  * dla zachowania kompatybilności z 8-bitowym 8080
  * dla instrukcji warunkowych zależnych od danych zmiennopozycyjnych

### Skoki
Ze stałym adresem docelowym - jmp, call, jcc, jecxz, loop - dekrementacja ecx i skok jeśli nie 0

Powroty z procedur
* ret - zwykł powrót
* ret n - ze zdjęciem argumentów (wymagane przez konwencję wołania Pascala)

Ze zmiennym adresem docelowym
* jmp eax
* jmp [code_pointer]
* jmp [table+ecx*4]

### Inne instrukcje warunkowe
* CMOVcc - przesłanie warunkowe
* SETcc - zamiana warunku na wartość boolowską


### Instrukcje wspierające implementacje języków wysokiego poziomu
* ret n - powrót z przesunięciem wskaźnika stosu o n bajtów po zdjęciu śladu
* enter n, 0 - prolog procedury
* leave - epilog procedury (bez powrotu)
* bound - sprawdzenie zakresu zmiennej (weryfikacja zakresu tablicy)


### Dziwne ale przydatne
* Skoki warunkowe korzystające z rejestru licznika iteracji
  * cx, ecx, rcx
* nie ustawiają znaczników
* dekrementacja i skok jeśli != 0, albo ustawiony/nieustawiony znacznik
  * loop, loopz, loope, loopnz, loopne
* skocz jeśli licznik pętli == 0
  * jcxz, jecxz, jrcxz


### Instrukcje iteracyjne
* korzystają z predefiniowanych rejestrów
  * rejestr danej (eax)
  * licznik iteracji (ecx)
  * wskaźnik źródła (esi)
  * wskaźnik przeznaczenia (edi)
* dwa warianty
  * pojedynczy - operacja na danej i modyfikacja wskaźnika
  * iterowany - instrukcja powtarzana określoną liczbę iteracji
  * lods, stos, mods - instrukcja pamięć-pamięć, scas, cmps
  * trzeba dopisać literę odpowiadają wielkości danych
  * dekrementuje albo inkrementuje na podstawie bitu DF rejestru stanu
  * konwencja wołania wymaga, żeby między przekazaniem sterowania, DF był ustawiony na 0
* tylko niektóre instrukcje jest sens zapętlać (jak pętla while może się nie wykonać i po wykonaniu wskaźnik jest przesunięty)
  * rep stos - wypełnianie wektora wzorcem
  * rep movs - kopiowanie wektora
  * repe scas - szukanie elementu różnego
  * repne scas - szukanie wzorca
  * repe cmps - szukanie różnicy
  * repne cmps - szukanie elementów zgodnych
* do ecx ładuje się maksymalną długość wektora


### Instrukcja CPUID
* informacje o własnościach procesora
* parametry fizyczne
* dostępne jednostki