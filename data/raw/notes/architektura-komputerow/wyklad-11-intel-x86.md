# Wykład 11 (2023-03-29)

## Assemblery x86
Są różne assemblery do x86

Wersje składni

* AT&T
  * system Unix
  * domyślna dla gcc
  * Odwrócona kolejność argumentów
* Intel/Microsoft
  * w dokumentacji Intel i assemblerze MASM
  * niejednoznaczna
* NASM
  * najpopularniejsza
  * podobna do Intel
  * zwarta i jednoznaczna
  * nawiasy kwadratowe oznaczają odwołanie do pamięci

## Formaty danych
* Byte 8b
* Word 16b
* Dword 32b
* Fword 48b
* QWord 64b
* Tword 80b
* Dqword 128b

## Specyfikacja rozmiaru argumentu
Na ogół wynika po prostu z użytej nazwy rejestru

Problem dla instrukcji bez argumentów rejestrowych, albo z argumentami o różnej długości

`inc [ebx]` -> `inc word [ebx]`

Assembler musi wiedzieć gdzie kończy się dana w pamięci

## Zerowanie rejestru
Najlepiej przez `xor eax, eax` - krótki kod binarny ale ustawia znaczniki, zeruje rejestr 64-bitowy w trybie 64-bitowym

## Tesotwanie rejestru
```
test eax, eax
js ujemne
jz zero
```
będzie traktowane jako jedna instrukcja


## Zastosowanie LEA
* trójargumentowe mnożenie
* trójargumentowe przesunięcie w lewo
* przesunięcie w lewo z dodawaniem(?)

## Programowanie hybrydowe
Tworzenie programu, którego moduły są pisane w różnych językach programowania

* używanie gotowych modułów
* realizacja w języku niższego poziomu operacji niemożliwych w preferowanym języku wyższego poziomu
* optymalizacja krytycznych fragmentów programu

Kod wołający musi przestrzegać konwencji określonej przez ABI wołanego kodu

## Konwencja wołania
* Sposób przekazywania argumentów
* Sposób wywoływania procedur
* Sposób odbierania wartości
* Sposób korzystania z zasobów systemowych

### Definiowana przez
* projektantów procesora
* projektantów systemu operacyjnego
* projektantów kompilatora

### Przypisanie funkcji rejestrom
* wskaźnik stosu - położenie wierzchołka
* wskaźnik ramki
* rejestry argumentów
  * przekazywanie argumentów do wołanej procedury
  * te które się nie zmieszczą w rejestrach są przekazywane przez stoa
* rejestry wartości
  * zwracanie wartości skalarnych funkcji
  * te które się nie mieszczą są zwracane na stos

### Grupy rejestrów
* rejestry zachowywane (saved)
  * wartości zachowywane przez procedurę
  * procedura wołana albo ich nie używa albo zachowuje ich wartości na stosie i odtwarza przed powrotem
  * alokacja zmiennych lokalnych procedur nie-liści
  * np. wskaźnik ramki
* rejestry tymczasowe (temporary, caller safe)
  * używane dowolnie
  * nie można polegać na ich wartości po wywołaniu innej procedury
  * tymczasowe wyniki
  * trwałe wyniki, które trzeba zachować przed wywołaniem
  * zmienne lokalne w procedurach liściach
  * rejestry argumentów i wartości

### Prolog procedury
* wyrównanie stosu (zależy od konwencji)
* zachowanie wskaźnika ramki (jeśli trzeba)
* alokacja miejsca na rejestry argumentów
* składowanie na stosie rejestrów argumentów (jeśli trzeba)
* ustanowienie nowej wartości wskaźnika ramki
* alokacja miejsca na zmienne lokalne
* składowanie rejestrów zachowywanych (jeśli trzeba)

### Epilog
Odwrotność tego co było w prologu, w odwrotnej kolejności

* odtworzenie rejestrów zachowanych
* dealokacja zmiennych lokalnych
* ...

## Konwencja wołania Unix System V dla x86
* Używana w systemach rodziny Unix i Linux
* Zgodna w podstawowych aspektach z konwencją C dla Windowsa 32-bitowego
* wyrównanie danych
  * naturalne dla danych 2B i 4B
  * typy dłuższe niż 4B wyrównane tylko do 4B

### Ważne!!!!
| Rejestr | Zastosowanie     | Zachowywany |
|---------|------------------|-------------|
| EAX     | rejestr wartości | nie         |
| ECX     | rejestr roboczy  | nie         |
|         |                  |             |
...

### Prolog i epilog - ważne !!!
ściąga:

```x86
myfunc:
; prolog funkcji - część wspólna dla wszystkich procedur
...
; zapamiętanie rejestrów zachowywanych
...
; ciało procedury
...
; odtworzenie rejestrów, które były zapamiętane
...
; epilog - część wspólna dla wszystkich procedur
...
```

W programie używa się tylko tego co jest potrzebne

Trzeba zachować kolejność (najpierw zmienne lokalne, potem zachowanie rejestrów)

Konwencja wołania z C obowiązuje te procedury, które mają być wołane z poziomu C, wewnątrz można dowolnie optymalizować.

Jeśli się da to używać rejestrów tymczasowych, jeśli się nie da to trzeba zachować rejestr zachowywany na stosie

Wywołanie procedury kosztuje, czytelność kodu i wydajność stoją w sprzeczności, nie należy tworzyć procedur które są wywoływane tylko raz