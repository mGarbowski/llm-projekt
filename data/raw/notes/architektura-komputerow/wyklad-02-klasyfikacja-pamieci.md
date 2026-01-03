# Wyklad 02 (2023-02-22)

## Maszyna von Neumanna

Program i dane są przechowywane w tej samej pamięci.

Pamięć składa się z ponumerowanych komórek, do zawartości komórki można odwołać się przez jej numer - adres.

Najwygodniej żeby instrukcje znajdowały się w kolejnych komórkach.

Rejestr PC (program counter) przechowuje adres następnej instrukcji i jest inkrementowany po jej pobraniu

Pojęcia są dosyć płynne i współczesne rozumienie odbiega od historycznych komputerów

### Harvard
* oddzielne hierarchie pamięci programu i danych
* szybkie działanie
* operacje na danych i instrukcjach można zrównoleglić dzięi oddzieleniu hierarchii pamięci
* nieprogramowalny, program jest wbity na stałe
  * nadaje się do rozwiązań embedded
  * nie nadaje się do uniwersalnych komputerów

### Princeton
* wspólna hierarchia pamięci programu i danych
* układ arbitra dostępu do pamięci między procesor danych i procesor instrukcji
* wolniejszy, bo tylko jeden z procesorów ma w danej chwili dostęp do pamięci
* programowalny, program jako daną można umieścić w pamięci i odczytać jako instrukcje
* von Neumann bottleneck
* wąskie gardło w dostępie do pamięci - nie można jednocześnie pobierać danych i instrukcji


## Komputer szybki i programowalny (Harvard-Princeton)
Wspólna pamięć dla danych i instrukcji ale oddzielne cache'e (L1 / L1 i L2).

Odczyt z oddzielnych cache'ów może się odbywać równolegle.

Styk między cache'em i pamięcią jest zarządzany przez sprzęt, a nie software

Zachowanie programu piszącego samego siebie jest niedeterministyczna.
Operacja dająca niedeterministyczny wynik powinna być zabroniona.

System operacyjny ma pewną kontrolę (nie pełną) nad stykiem cache/pamięć.
Może wymusić opróżnienie cache'y (wyczyścić), np. przed wykonaniem programu po załadowaniu go do pamięci.


## Klasyfikacja pamięci
Idealna pamięć jest nieulotna, tania, pojemna i szybka

### Ze względu na trwałość
* ulotne
  * tracą informacje po odcięciu zasilania
  * dynamiczne
    * wymagają odświeżania
  * statyczne
* nieulotne
  * potrzebuje energii tylko do zmiany zawartości
  * powolny zapis

### Ze względu na mechanizm dostępu
* Bezpośredni (przez adres)
* Sekwencyjny (według kolejności) - pobierz następny, zapisz następny
  * kolejka
  * stos
* Asocjacyjny (przez porównanie z wzorcem)
* Hybrydowy (np. bezpośrednio sekwencyjny - odczyt kolejnych bajtów z adresowanego bloku)


## Technologie pamięci
| Typ         | Nieulotna | Pojemność |
|-------------|-----------|-----------|
| DRAM (DDR5) | nie       | 8 Gib     |
| SRAM        | nie       | 64 Mib    |
| MRAM        | tak       | 32 Mib    |
| NOR Flash   | tak       | 1 Gib     | 
| NAND Flash  | tak       | 512 Gib   |


### Pamięć Flash
* tani
* wymaga kasowania przed zapisem
* ograniczona trwałość (liczba kasowań)
* kasuje się duże bloki na raz
* wymaga kodów korekcyjnych, nie jest wiarygodna bez nich


Potocznie RAM jest rozumiany jako pamięć ulotna, bardziej poprawnie RWM (read-write memory) - pamięć o takiej samej szybkości zapisu i odczytu