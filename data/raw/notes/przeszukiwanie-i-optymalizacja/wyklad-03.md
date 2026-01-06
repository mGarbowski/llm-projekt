# 2024-10-23
* Algorytm wspinaczkowy - w sąsiedztwie punktu wybieramy najlepszy
* Algorytm gradientowy - dla różniczkowalnej funkcji celu, najlepszy punkt jest jednoznacznie określony - nieskończenie mały krok w stronę gradientu lub przeciwnym (minimalizacja albo maksymalizacja)
* W praktyce - gradient przemnożony przez współczynnik kroku
	* nie daje gwarancji że kolejny punkt jest najlepszy (może przeskoczyć optimum)

Co jeśli funkcja ma wiele optimów lokalnych, a dysponujemy algorytmem, który znajduje optimum lokalne?
* Można wystartować wielokrotnie z różnych punktów startowych
* Wprowadzić element losowości
	* w wyborze sąsiada - losowy wybór (stochastyczny algorytm wspinaczkowy)
	* w podejmowanej decyzji - akceptacja niekoniecznie lepszego punktu (błądzenie przypadkowe)
	* akcpetacja gorszego punktu z określonym prawdopodobieństwem (symulowane wyżarzanie)
* Dostosowanie współczynnika kroku
	* np. większy w okolicy optimum żeby z niego wyskoczyć
	* wprowadza szum do algorytmu
* Zwiększenie promienia sąsiedztwa
	* analogicznie do zwiększenia parametru kroku
	* optima lokalne przestaną być optimami lokalnymi - bo w szerszym sąsiedztwie jest lepszy


Stochastyczny algorytm wspinaczkowy - dalej zmierza do optimum lokalnych ale mniej konsekwentnie

## Algorytm wspinaczkowy ze zmiennym sąsiedztwem (VNS)

```
init(x)
H = {x}
while !stop
	k = 1
	repeat
		Y = N_k(x)
		H.add(Y)
		y = selectBest(Y)
		k += 1
	until q(y) > q(x) or k > K
	if k > K
		exit
	x = y
```

* Najpierw szukamy sąsiadów w mniejszym promieniu
	* jeśli się nie uda to zwiększamy promień i szukamy w większym sąsiedztwie
* Jeśli przy największym dopuszczalnym promieniu nie da się znaleźć lepszego to kończymy algorytm
* Algorytm do dyskretnej przestrzeni przeszukiwań
* Zależy jaka jest liczba sąsiadów
	* może się bardziej opłacać spróbkować wiele razy przy mniejszym promieniu niż raz z większym
* VNS i algorytm wspinaczkowy o promieniu K nie zawsze dojdą do tego samego punktu końcowego wystartowane z tego samego punktu

Zastosowanie idei VNS do przestrzeni ciągłych

* Zwiększanie współczynnika kroku w algorytmie gradientowym
	* większy sens przy algorytmie stochastycznym

## Algorytm prawie wspinaczkowy

```
initialize(x)
H = {x}
while !stop
	Y = N(x)
	x = selectBest(Y)
	H = H union Y
```

* Może oscylować między dwoma punktami
* Nie ma sensu wracać do już odwiedzonego punktu
* Wyjmujemy krawędzie z przestrzeni przeszukiwań

## Przeszukiwanie z Tabu
```
T = empty
init(x)
H = {x}
while !stop
	Y = N(x) \ T
	x = selBest(Y)
	T_j = define_for_deletion()
	T = T union {x} \ T_j
	H = H union Y
```

dekoracja do algorytmu, niekoniecznie do algorytmu prawie wspinaczkowego

* Optimum lokalne trafia do tabu
* Najpierw podchodzi pod górę, potem próbuje jak najmniej schodzić w dół
* Po osiągnięciu oiptimum lokalnego punkty są wypychane
* Tabu - np. kolejka FIFO
* Dobra wielkość tabu zależy od
	* liczebności sąsiedztwa
	* odległości między optimami
	* potęgowanie
* Kolejka priorytetowa
	* według funkcji celu
	* według szacowanej funkcji celu
	* według podobieńśtwa
	* według wiedzy dziedzinowej
* Można zastosować jako dekorację do innych algorytmów
	* do symulowanego wyżarzania
	* do przestrzeni ciągłych - z sąsiedztwa punktu roboczego usuwa się sąsiedztwa wzsystkich punktów z tabu (sam punkt jest miary 0)

dodawanie krawędzi - VNS
usuwanie krawędzi - tabu