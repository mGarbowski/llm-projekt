# Liczby rzeczywiste (2022-10-27)

Tak samo jak w systemie dziesiętnym, nie każdą liczbę da się przedstawić dokładnie $\frac{1}{3}=0.(3)_{10}$, $\frac{1}{10}=0.0(0011)_2$

## Zamiana liczby z częścią ułamkową na postać binarną
3.14

* Część całkowitą traktujemy oddzielnie, zamiana znanym algorytmem na 11
* Zostaje 0.14
* Mnożymy razy 2 i zapisujemy cyfrę jedności
* Odejmujemy 1 jeśli cyfrą jedności było 1

| wartość | razy 2 | bit |
| ------- | ------ | --- |
| 0.14    | 0.28   | 0   |
| 0.28    | 0.56   | 0   |
| 0.56    | 1.12   | 1   |
| 0.12    | 0.24   | 0   |
| 0.24    | 0.48   | 0   |
| 0.48    | 0.96   | 0   |
| 0.96    | 1.92   | 1   |
| 0.92    | 1.84   | 1   |

|      | 1   | 1   | .   | 0   | 0   | 1   | 0    | 0    | 0    | 1     | 1     |
| ---- | --- | --- | --- | --- | --- | --- | ---- | ---- | ---- | ----- | ----- |
| waga | 2   | 1   |     | 1/2 | 1/4 | 1/8 | 1/16 | 1/32 | 1/64 | 1/128 | 1/256 |

Otrzymujemy przybliżony wynik $3\frac{35}{256}=3.13671875$


## IEEE 754
Standardowa specyfikacja reprezentacji liczby ziennoprzecinkowej na 32 bitach określa IEEE 754

$$
(-1)^S \cdot M \cdot 2^{E-127}
$$

SEEEEEEEEMMMMMMMMMMMMMMMMMMMMMMM

* S (sign)
    * 1 bit
    * znak liczby
* M (mantissa)
    * 23 bity (hidden MSB)
    * znormalizowana mantysa
    * liczba z przedziału [1,2)
    * najbardziej znaczący bit ma zawsze wartość1 i nie jest zapisywany (hidden MSB)
* E (exponent)
    * 8 bitów 
    * wykładnik / cecha 
    * przesunięty o 127 (prawdziwy wykładnik to E-127)
    * bias 127

Wartości, które można reprezentować nie są rozłożone równomiernie na osi liczbowej

## Typ float w C/C++
|                |                 |                                                       |
| -------------- | --------------- | ----------------------------------------------------- |
| FLT_EPSILON    | 1.19209290E-07F | Różnica między 1 i najmniejszą wartością większą od 1 |
| FLT_DIG        | 6               | Liczba cyfr po przecinku, które są dokładne           |
| FLT_MIN        | 1.17549435E-38F | Najmniejsza możliwa wawrtość                          |
| FLT_MIN_10_EXP | -37             | Najmniejsza potęga 10 jaka się zmieści                |
| FLT_MAX        | 3.40282347E+38F | Największa możliwa wartość                            |
| FLT_MAX_10_EXP | 38              | Największa potęga 10 jaka się zmieści                 |

* Float - 32 bity, pojedyncza precyzja
* Double - 64 bity, podwójna precyzja

## Zamiana liczby na postać IEEE 754
* 2019 = 0111 1110 0011
* Znormalizowanie: 1.11 1110 0011 * 2^10
* Zaokrąglenie do odpowiedniej liczby bitów
  * Dodać 1 do pierwszsego nie mieszczącego się bitu
  * Obciąć nie mieszczące się bity
* Obciążenie wykładnika 10 + 127 = 137
* Znak (S): 0
* Wykładnik (E): 1000 1001
* Mantysa (M): 111 1100 0110 0000 0000 0000
* Otzrymujemy 0100 0100 1111 1100 0110 0000 0000 0000
* Kodując heksadecymalnie 0x44FC6000

Procesor musi pracować na szerszym zakresie bitów, żeby obsłużyć zaokrąglenia

## Wartości specjalne i przykłady
| Typ            | Wykładnik | Mantysa                      | Wartość          |
| -------------- | --------- | ---------------------------- | ---------------- |
| Zero           | 0000 0000 | 000 0000 0000 0000 0000 0000 | 0.0 ($1^{-127}$) |
| Jeden          | 0111 1111 | 000 0000 0000 0000 0000 0000 | 1.0              |
| Max            | 1111 1110 | 111 1111 1111 1111 1111 1111 | 3.4e+38          |
| Min            | 0000 0001 | 000 0000 0000 0000 0000 0000 | 1.8e-388         |
| Nieskończoność | 1111 1111 | 000 0000 0000 0000 0000 0000 | $\plusmn\infty$  |
| NaN            | 1111 1111 | non-zero                     | NaN              |

## Operacje
* Rzutowanie FLP na INT
* Zaokrąglenie
* Sufit
* Podłoga


## Operacje arytmetyczne
* Mnożenie i dzielenie
  * Suma wykładników
  * Iloczyn mantysy
  * Znormalizować wynik
* Dodawanie i odejmowanie
  * Sprowadzenie do wspólnego wykładnika
  * Suma mantys
  * Znormalizować wynik

Operacje wykonuje koprocesor FPU (Floating Point Unit)

Operacje arytmetyczne na liczbach zmiennoprzecinkowych są parami operacji na liczbach stałoprzecinkowych


## Ważne
* Reprezentacje i wyniki operacji są przybliżone
* Wynik może zależeć od kolejności wykonywania $a+b \ne b+a$
* Nie należy używać relacji równości, tylko `abs(a-b) < epsilon`
* Nie stosować tam, gdzie przybliżony wynik jest niedopuszczalny (np. w finansach)

