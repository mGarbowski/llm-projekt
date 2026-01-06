# Adaptacja i samoczynna adaptacja parametrów AE (2025-01-15)

Co to znaczy że algorytm działa lepiej
Mówimy o algorytmach, które służą do zadań, gdzie nie jesteśmy w stanie uzyskać dokładnych rozwiązań w sensownym czasie
To są generalnie metody drugiego wyboru
Jeśli zadanie ma wiele optimów lokalnych to sięgamy po metody heurystyczne

Jak wykreślimy krzywe ECDF, ułamek poziomów ambicji osiągniętych przez algorytm w określonym czasie stosunkowo szybko narasta

Ustawienie parametrów nie jest oczywiste, a istotnie wpływa na efektywność metody optymalizacyjnej

Nie wiadomo z góry jakie wybrać parametry dla np. algorytmu ewolucyjnego
bardziej miękkie vs bardziej twarde warianty selekcji
mniejsze szranki - większa odporność na optima lokalne ale mniejsza precyzja
pamiętać jak działą selekcja progowa!
przy selekcji proporcjonalnej możemy dodać dużą stałą do wszystkich wartości funkcji celu - zmniejszając ruchliwość i uodparniając na optima lokalne

wpływ siły mutacji na krzywą ecdf

są pewne intuicje ale nie ma analitycznych rozwiązań

## Różnica między algorytmem i programem
* maszynowe reprezentacje liczb rzeczywistych
* błędy implementacyjne
* realizacja rozkładów prawdopodobieństwa - w praktyce rozkład normalny jest obcięty
* poprawność programu nie może się opierać na asymptotycznych zależnościach

unikanie nadmiernego dopasowanie - nie można tego zakładać w algorytmach optymalizacji


Rozważany algorytm
populacja lambda
wybieramy mi najlepszych
następny punkt roboczy to średnia z mi najlepszych

![[Pasted image 20250124172803.png]]

odcinek step-size too large na wykresie - algorytm jest w okolicy optimum, ale przez dużą siłę mutacji kręci się po otoczeniu optimum

odcinek step-size too small - daleko od optimum, mała siła mutacji powoduje powolne zmierzanie w stronę optimum

potrzeba jakiejś reguły do adaptacji siły mutacji (zwiększenia zbyt małego kroku i zmniejszenia zbyt dużego)
możemy porównać średnie wartości funkcji celu w kolejnych iteracjach
możemy wyliczyć iloraz różnicowy

i przy za dużym kroku i przy za małym są wypłaszczenia krzywej zbieżności

Znane strategie

## Strategia oparta o wartość funkcji celu

Daleko od optimum i mały krok - porządany jest większy krok
połowa punktów mutantów będzie lepsza, a połowa gorsza (średnio) - należy zwiększać zasięg mutacji

Blisko optimum - większość nowych punktów będzie gorsza - należy zmniejszyć zasięg mutacji

Reguła 1/5 liczby sukcesów - wartość progu została wyznaczona empirycznie
pierwotnie dla ES-(1+1) (algorytm wspinaczkowy)
liczymy proporcję zakończonych sukcesem mutacji (liczby punktów lepszych od punktu środkowego)

PPMF - współczesny odpowiednik

## Algorytm CSA
Reguła adaptacji oparta o kierunek

m - punkt środkowy

wektor $p_\sigma$ - zakumulowany wektor przesunięcia punktu środkowego
$\Delta$ - średni wektor, który doprowadził do poprawy
w zalezności od długości wektora $p_\sigma$ krok wzrasta lub maleje

przy stałej funkcji celu (lub bardzo gęstym sinusie)
mutanty generowane rozkładem normalnym, nie ma związku między oddaleniem od punktu środkowego a jakością mutanta
z chmury mutantów którykolwiek może być lepszy
uśredniamy je
rozkład uśrednionego $\Delta$ - średnia z $\mu$ realizacji rozkładu standardowego
$\Delta \sim N(0, \frac{1}{\mu} I) \implies \sqrt{\mu} \Delta \sim N(0, I)$

p jest średnią ważoną dwóch zmiennych o rozkładzie normalnym standaryzowanym
Współczynniki uśredniania są tak dobrane że wynik też jest zmienną o rozkładzie nromalnym ustandaryzowanym
to wszystko przy założeniu że rozkład mutantów ma właściwość szumu

Wartość oczekiwana ilorazu w przedostatniej linijce ma wartość oczekiwaną 1
odejmujemy 1 więc równie często będzie dodatny wykładnik co ujemny


### Sytuacja z kwadratową funkcją celu
Punkt zaczyna daleko od optimum
wektory d będą zgodne ze sobą - w stronę optimum
wektor $p_\sigma$ będzie się wydłużać, iloraz będzie częściej większy od 1 więc $\sigma$ częściej będzie się zwiększać

Kiedy m pokrywa się z optimum lokalnym
$\Delta$ zbliża się do 0
do $p_\sigma$ są akumulowane wartości bliskie 0
częściej $\sigma$ będzie zmniejszana

### Zdolność przeskakiwania dołków
Blisko optimum zacznie wygaszać zasięg mutacji
Algorytm da radę wyskoczyć z optimum lokalnego jeśli będzie wystarczająco rozpędzony i nie zdąży wygasić na tyle zasięgu mutacji

## Metoda najszybszego wzrostu
Dodajemy do punktu roboczego przeskalowany gradient w punkcie
Wymnożenie gradientu przez odwrotność hesjanu daje kierunek, który dla funkcji kwadratowej przechodzi przez optimum

Trudne zadania, które są gradientowe - uczenie sieci neuronowych
można obliczyć gradient funkcji straty w sposób analityczny

metoda wstecznej propagacji błędu to po prostu metoda najszybszego wzrostu

## Metoda momentum
metoda momentum - krok wynikający z gradientu jest akumulowany
zachowuje się jakby zachowywał pęd

## Metoda Adam

### Metody zmiennej metryki
Alternatywa do metody Newtona (z mnożeniem przez odwrotność hesjanu)
nie ma sensu algorytm gdzie odwraca się macierz 10k x 10k
stosuje się metody zmiennej metryki (BFGS, DFP) do szacowania odwrotności hesjanu (hesjan to intuicyjnie gradient gradientu)

### Adam
x jest przesuwany wektorem m
dzielenie wektorowe - po współrzędnych
epsilon to maly szum losowy
v to czynnik normujący
m i v od mean i variance (przez analogię)

m to zakumulowany wektor gradientu (wypadkowa między poprzednim i aktualnym)
v to zakumulowany wektor kwadratu wektora gradientu - wartość kwadratów współrzędnych wektora

jak kierunki są zgodne to przyspiesza w tym kierunku
jeśli kierunki niezgodne, to deformuje wektor gradientu podobnie do odwrotności hesjanu