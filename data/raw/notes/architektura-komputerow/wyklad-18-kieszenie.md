# Kieszenie

## Zasada lokalności odwołań
* zbiór roboczy

## Kieszeń pełnoasocjacyjna
* Każde chybienie wymaga zapamiętania danej i adresu z pamięci do kieszeni
* Niepraktyczna w prawdziwej implementacji (problemy elektryczne)
* Heurystyka LRU - wyrzuć to co najdłużej nie było używane
* Działa bardzo źle kiedy zbiór roboczy jest większy od pojemności kieszeni - gwarantuje 100% chybień

## Budowa kieszeni
* linie - długie bloki danych z pojedynczym adresem
* długość linii jest potęgą 2
* nie trzeba przechowywać najmniej znaczących bitów adresu ze względu na wyrównanie naturalne (pomija się najmniej znaczące bity służące do indeksowania bajtów wewnątrz bloku)
* użyteczna jest ta część pamięci, która trzyma dane, dlatego nie trzyma się pojedynczych bajtów
* zazwyczaj linia jest 4x większa od słowa pamięci

## Kieszeń bezpośrednio adresowana
* Zbudowana na bazie pamięci RAM i komparatora równościowego
* Dostęp swobodny do linii przez podanie adresu
* Najmniej znaczące bity adresu będą wybierać bajt w obrębie linii w przypadku trafienia
* Środkowe bity adresu są wprowadzone na wejście adresowe pamięci - wybierają pojedynczą linię
* Odczytany z kieszeni znacznik adresu zawiera bardziej znaczące bity adresu głównej pamięci
* Komparator porównuje najbardziej znaczące bity adresu z wejścia z wartością znacznika z początku linii kieszeni - jeśli są równe to jest trafienie
* W przypadku chybienia to zastępowana jest ta wybrana linia - algorytm narzucony przez budowę

### Pętla dłuższa od kieszeni
* Kolejne instrukcje nie zastępują najdawniejszych tylko instrukcje o takich samych środkowych częściach adresów.
* Instrukcje ze środka pętli zostaną w kieszeni
* 100% chybień przy pętli 2x większej od kieszeni, skuteczna ale coraz mniej kiedy pętla jest dłuższa od kieszeni

### Dwie części obszaru roboczego o takich samych środkowych bitach adresu
* Złośliwy przypadek ale występuje rzadko
* Dwie części będą się zamieniać naprzemian
* Taka sama sytuacja jest bezbolesna dla LRU

## Kieszeń zbiorowo-asocjacyjna
* Połączenie kilku kieszeni bezpośrednio adresowanych - bloków
* Uniewrażliwienie na pokrywające się adresy - takie dane mogą trafić do różnych bloków

### Działanie
* Z każdego bloku jest wybierana jedna linia
* Każdy znacznik jest porównywany ze znacznikiem z procesora w komparatorze każdego bloku - działanie jak dla małej kieszeni pełnoasocjacyjnej
* Grupa linii wybranych z każdego bloku na podstawie adresu procesora - zbiór

Blok zachowuje się jak kieszeń bezpośrednio adresowana
Zbiór zachowuje się jak kieszeń pełnoasocjacyjna
Łączy zalety obu rozwiązań


### Algorytm zastępowania
* W zbiorze w przypadku chybienia jest wiele możliwości
* Automat musi być oddzielny dla każdego zbioru
* LRU jest użyteczne dla 3 bloków (3 przerzutniki)
* Dla więcej niż 3 bloków stosuje się pseudoLRU - drzewo binarne z przerzutników
* Algorytm losowy z wykluczeniem ostatnio używanego - często używany w praktyce - tani i prosty


## Podsumowanie
* Najczęściej używa się zbiorowo-asocjacyjnych
* Pełnoasocjacyjne nie są używane do instrukcji i danych

## Współczynnik trafień
liczba trafień / całkowita liczba odwołań

### Zależy od
* pojemności kieszeni
* organizacji kiesezeni i algorytmu wymiany
* specyfiki wykonywanego programu (zbioru roboczego) - do benchmarku używa się różnych typów programów
* dla każdej kieszeni da się dobrać program, który da współczynnik trafień 0 i taki który da blisko 1

Zazwyczaj między 8-16 KiB pojemności kieszeni osiąga się współczynnik rzędu 0.9, dla wyższych warrtości korzyść się wypłaszcza
Dla małych pojemności zależy głównie od pojemności, dla większych głównie od algorytmu wymiany


## Wydajność
Miarodajną wartością jest liczba B/s (albo analogicznie odwrotność), sam niemianowany współczynnik nie bardzo

Dwa poziomy kieszenie dają średni czas na granicy akteptowalności, w wydajniejszych procesorach stosuje się 3 poziomy

L3 przechowuje jednocześnie dane i kod kilku zadań
L2 generalnie przechowuje kod jednego zadania


## Zachowanie kieszeni przy zapisie
* zapis przezroczysty - zawsze do pamięci, a przy trafieniu też do kieszeni (jednocześnie)
* zapis zwrotny - zapis do pamięci tylko wtedy kiedy jest to potrzebne
    * bez alokacji przy chybieniu zapisu - przy chybieniu odczytu trzeba będzie zapisać linię kieszeni do pamięci (ofiarę)
    * z alokacją przy chybieniu zapisu - żeby zapisać tylko do kieszeni to trzeba najpierw pobrać linię z pamięci i może wcześniej zapisać linię kieszeni do pamięci

Kieszeń może inicjować transakcje

Chybienie odczytu - wyznacza się ofiarę - linię wyrzucaną z kieszeni


## Kieszenie inkluzywne
* Już nie stosowane
* Każdy obiekt zawarty w wyższej warstwie jest też obecny w niższej warstwie
* Efektywna pojemność to zestawu kieszeni to pojemność największej (L3)

## Kieszenie wyłączne
* Linia może się znajdować tylko w jednej kieszeni na raz
* Współczesna
* Efektywna pojemność jest sumą pojemności wszystkich kieszeni
* Kieszeń niższa nigdy nie jest napełniana danymi z pamięci tylko danymi wyrzucanymi z wyższej kieszeni
* tzw. victim cache - napełniony ofiarami wyższej kieszeni
* schemat ścieżek przepływu ...
* Przy chybieniu L1 odczytu danej z L2 linia z L1 jest wymieniana z linią w L2 (narzucony algorytm wymieniania)
* Przy chybieniu odczytu w L1 i L2 - cykl duży - z pamięci do L1, ofiara z L1 do L2, ofiara z L2 do pamięci

Dotyczą połączenia dwóch kieszeni, można na jeden sposób połączyć L1 z L2 a na drugi L2 z L3


Przy większych pojemnościach kieszeni większą rolę na wydajność kieszeni zaczyna odgrywać algorytm wymiany.
L2 powinno mieć większą asocjacyjność od L1


## Spójność hierarchii pamięci
Każdy odczyt danej z hierarchii musi zwrócić najbardziej aktualną wartość, dla każdego czytającego

Zagrożenie przy więcej niż 1 ścieżce dostępu
* architektura Harvard-Princeton z oddzielnym L1 dla kodu i danych
* komputer wieloprocesorowy
* urządzenia IO czytające / piszące bezpośrednio do pamięci (sterowniki sieciowe)

Spójność fizyczna - na każdym poziomie jest to samo
Spójność logiczna - wiadomo gdzie jest aktualna kopia, unieważnianie linii kieszeni (mechanizm gwarantowany sprzętowo)

### Protokoły utrzymania spójności
Automat zrealizowany oddzielnie dla każdej linii, minimalizuje liczbę unieważnień linii

Więcej stanów linii wyróżnianych przez protokół - mniej unieważnień linii
