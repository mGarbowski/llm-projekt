# Metaheurystyki w R^n (2024-12-18)

Populacja punktów, przyjmujemy najlepszy za nowy punkt roboczy

Wygenerowanie lambda sąsiadów i wybranie jednego najlepszego jako punkt roboczy - ES-(1,$\lambda$)
ES-(1+1) - algorytm stochastycznego wzrostu (wspinaczkowy)
ES-(1,1) - błądzenie przypadkowe

Każdy punkt z populacji ma losowanego sąsiada z rozkładem normalnym, jaki jest rozkład łączny


---
Przyjmijmy że populacja to punkty na prostej (1 wymiar)
Są znane położenia punktów populacji bazowej, gdzie będą znajdowały się punkty populacji potomnej
Badamy funkcję gęstości prawdopodobieństwa tego, że w miejscu x zostanie wygenerowany punkt populacji potomnej pod warunkiem że populacja bazowa ma daną zawartość P

Prawdopodobieństwo mutacji jest określone $f_m(y|x)$
Prawdpopodobieństwo selekcji jest określone przez $p_s(i|P)$
Funkcja celu $q$

$$ f_O(x|P) = \sum_{i=1}^\mu p_s(i|P) \cdot f_m(x|P_i) $$ Suma prawdopodobieństw osiągnięcia punktu x z każdego punktu z populacji bazowej

Mutacja rozkładem jednostajnym na [-2,2], selekcja turniejowa binarna
Minimalizacja

| i   | P_i | q(P_i) | p_s(i $\|$P) |
| --- | --- | ------ | ------------ |
| 1   | 0   | 3      | 5/16         |
| 2   | 2   | 4.5    | 1/16         |
| 3   | 6   | 3.12   | 3/16         |
| 4   | 6.5 | 0.31   | 7/16         |

Sumujemy prostokąty rozkładu jednostajnego przemnożone przez $p_s$
prostokąty o środku w $P_i$

Punkty populacji potomnej powstają tam gdzie jest gęsto i tam gdzie są punkty lepszej jakości

Dynamika algorytmu ewolucyjnego - rozkład łączny zbija się 
Możemy przybliżyć rozkład rozkładem normalnym, obliczyć macierz kowariancji na podstawie punktów populacji

rozkład położenia punktów populacji potomnej - rozkład próbkowania
## Metoda EDA
Estimation of Distribution Algorithm

podobny do algorytmu PBIL dla przestrzeni kombinatorycznych - probability based incremental learning

ES(1,$\lambda$)
rozrzucenie punktów wokół wartości oczekiwanej

ale macierz kowariancji nie jest pod kontrolą użytkownika
macierz dostosowuje się do potrzeb procesu optymalizacji

obserwujemy że rozkład próbkowania przypomina rozkład normalny, wracamy do rozkładu normalnego

parametry - wektor wartości oczekiwanych, macierz kowariancji

próbkowanie punktów rozkładem normalnym
poddanie punktów ocenie
wybór części z wygenerowanych punktów
na podstawie wybranych punktów robi się korektę wektora i macierzy kowariancji

wyznaczanie środka nowej populacji
obliczenie wektorów różnicowych
nowa macierz kowariancji - dla każdego wektora robi się iloczyn zewnętrzny - wychodzi macierz kwadratowa, sumuje się macierze - na slajdzie brakuje dzielenia przez $1/(\mu-1)$
iloczyn zewnętrzny - analogia podnoszenia do kwadratu - jak we wzorze na wariancję próby $\sum(x-\bar{x})^2$

poziomice funkcji gęstości powstałego rozkładu - elipsa wycięgniąta w tą stornę co punkty
podobnie do ewolucji różnicowej

algorytm może mieć tendencję do zmniejszania różnorodności, zapadania się
można wprowadzić
można dodać szum do macierzy kowariancji

Można nową macierz kowariancji wyznaczyć przez uśrednienie poprzedniej i nowej estymowanej

Dynamika EDA na zboczu
próbkowanie będzie się rozszerzać w kierunku w którym funkcja celu zmienia się mało
próbkowanie będzie się zwężać w kierunku, w którym funkcja celu zmienia się znacznie

Dynamika EDA na wzgórzu
dopasowuje się kontur - poziomice gęstości nowego rozkładu będą dążyły do pokrywania się z poziomicami funkcji celu
położenie wartości oczekiwanej pokrywa się z optimum

z iteracji na iteracje przechowuje się tylko parametry rozkładu, nie populację punktów

Algorytm CMA-ES - podobny ideowo do EDA

## Rój cząstek
Wiele piłeczek staczających się w dół
Wchodzą w interakcje między sobą
Zapamiętują najlepszy punkt w jakim były (mogą jechać pod górę)
Mają bezwładność

P - położenia piłezek
V - wektory przesunięć (analogia prędkość)
do położenia dodaje się przesunięcie

znajdowane jest najlepsze położenie znalezione przez którąkolwiek piłeczkę w którejkolwiek iteracji - g (global best)
najlepsze położenie dla piłeczki - b (local best)

Do starej wartości prędkości dodaje się 2 wektory
od położenia do global best
od położenia do local best
sumowanie jest z losowymi wagami

Dynamika na zboczu
Zaczynamy z zerową prędkością
Najlepszy nie rusza się wcale
Pozostałe ruszają się w stronę lepszego
Wszystkie zbiegają do najlepszego

Dynamika na zboczu, niezerowe prędkości początkowe
...
Istnieje ryzyko, że proces się zatrzyma

Dynamika dla roju rozproszonego wokół opt lokalnego
Ściskanie roju we wszystkich kierunkach

Chcemy żeby rój był w stanie wyjechać z optimum ze względu na bezwładność (prędkość jest wytracana stopniowo)

Żeby rój ruszył z miejsca powinien mieć duże rozproszenie i niezerowe prędkości początkowe