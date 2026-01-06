# Reprezentacja liczb całkowitych (2022-10-20)

Zmienna typu boolean na większości architektur zajmie conajmniej 1 bajt (najmniejsza adresowalna jednostka)

## Naturalny kod binarny

| liczba bitów | liczba stanów | zakres wartości |
| ------------ | ------------- | --------------- |
| $n$          | $2^n$         | $0$ - $2^n-1$   |
| 8            | 256           | 0 - 255         |

Najbardziej znaczący bit - waga $2^n-1$

Najmniej znaczący bit - waga $1$

Występują 2 spodoby zapisu liczb wielobajtowych w pamięci
### Big-endian (TCP, UDP, IP)
Najbardziej znaczący bajt jest pod najmniejszym adresem (od lewej do prawej)

### Little-endian (x86)
Najbardziej znaczący bajt pod największym adresem

### Przekształcanie liczb dziesiętnych na NKB
1. Dzielić przez 2 i zapisywać resztę z dzielenia
2. Przewrócić kolumnę w prawo

| 57  |     |
| --- | --- |
| 28  | 1   |
| 14  | 0   |
| 7   | 0   |
| 3   | 1   |
| 1   | 1   |
| 0   | 1   |

| 32  | 16  | 8   | 4   | 2   | 1   |
| --- | --- | --- | --- | --- | --- |
| 1   | 1   | 1   | 0   | 0   | 1   |

$$57_{(10)} = 111001_{NB}$$


## Kodowanie znak-moduł (ZM)
Najbardziej znaczący bit określa znak

$$(-1)^{b_{N-1}}\sum_{i=0}^{N-2} 2^i * b_i$$
$$11001001_{ZM} = -(64+8+1) = -73$$

* Dwie reprezentacje dla $0$
* Negacja przez zamainę jednego bitu
* Zakres wartości od $-(2^{N-1}-1)$ do $2^{N-1}-1$ (niesymetryczny)
* Niewygodne do operacji arytmetycznych


## Kod uzupełnień do 1 (U1)
Najbardziej znaczący bit ma ujemną wagę

$$(-2^{N-1}+1) * b_{N-1} + \sum_{i=0}^{N-2}2^i*b_i$$
$$11001001_{U1} = -127 + 64 + 8 + 1 = -54$$

* Negacja przez zanegowanie wszystkich bitów
* Zakres wartości od $-(2^{N-1}-1)$ do $2^{N-1}-1$
* Dwie reprezentacje dla 0
* Odejmowanie - dodawanie liczby zanegowanej
* Dodawanie tak samo jak w NKB + dodajemy 1 do wyniku przy przeniesieniu poza bit znaku

## Kod uzupełnień do 2 (U2)
Najbardziej znaczący bit ma ujemną wagę

$$(-2^{N-1}) * b_{N-1} + \sum^{N-2}_{i=0}2^i*b_i$$
$$11001001_{U2}=-128+64+8+1=-55$$

* Niesymetryczny zakres od $-2^{N-1}$ do $2^{N-1}$
* Jedna reprezentacja 0
* Negacja - zanegowanie bitów i dodanie 1
* Dodawanie - tak samo jak w NKB!
* Odejmowanie - dodanie liczby zanegowanej
* Używany w implementacjach C/C++

### Przepełnienie w U2
Przepełnienie występuje kiedy przeniesienie poza granicę słowa jest różne od ostatniego przeniesienia
* 01, 10 - przepełnienie
* 00, 11 - nie ma przepełnienia

### Wydłużenie liczby w zapisie U2
0 na pierwszym bicie jest znaczące.

Trzeba powielić najbardziej znaczący bit
* $-3$ na 4 bitach $1101$
* $-3$ na 8 bitach $11111101$


## Przesunięcie arytmetyczne w lewo 
(mnożenie przez 2)

Wynik się zgadza pod warunkiem, że przed i po przesunięciu bit znaku zostaje taki sam


## Przesunięcie arytmetyczne w prawo
(dzielenie przez 2)

* Najmniej znaczący bit ginie
* Pierwszy bit (znaku) się kopiuje w U2
* Problem przy ujemnych liczbach nieparzystych U2!


### Obcinanie vs zaokrąglanie
Kiedy jest w góre, a kiedy w dół?

### Dzielenie i przesunięcie w assemblerze
Przesunięcie i dzielenie nie zawsze jest równoważne! Kompilator sam sobie poradzi i zoptymalizuje operację. Nie warto kombinować!


## Przesuwanie
* Arytmetyczne (ASL, ASR) - uwzględnia bit znaku
* Logiczne  (LSL, LSR) - traktuje sekwencję bitów jako zwykły ciąg znaków
* Cykliczne  - wysunięty bit wchodzi z drugiej strony


## Mnożenie w U2
* Rozszerzenie operandów razy 2 (z 8 bitów do 16 itd.)
* Przesunięcie mnożnika w lewo i dodanie do pośredniego wyniku


Wszystkimi operacjami zajmuje się ALU


|     | Zakres wartości słowa kodowego |                              |
| --- | ------------------------------ | ---------------------------- |
| NBC | $b_{n-1}b_{n-2}...b_1b_0$      | $0$ - $2^n-1$                |
| ZM  | $b_{z}b_{n-2}...b_1b_0$        | $-(2^{N-1}-1)$ - $2^{N-1}-1$ |
| U1  | $b_{n-1}b_{n-2}...b_1b_0$      | $-(2^{N-1}-1)$ - $2^{N-1}-1$ |
| U2  | $b_{n-1}b_{n-2}...b_1b_0$      | $-2^{N-1}$ - $2^{N-1}$       |


## Oznaczenie
Liczby podawane w innych systemach oznacza się np, prefixem
* 0b - binarne
* 0o - oktalne
* 0x - heksadecymalne

## Binary coded decimal
Każda cyfra od 0 do 9 reprezentowana na 4 bitach w postaci NKB
od 0000 do 1001

Nibble / tetrada - połówka bajtu