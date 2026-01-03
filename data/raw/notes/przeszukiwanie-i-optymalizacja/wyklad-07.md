# Algorytmy ewolucyjne c.d. (2024-11-27)

## Uporządkowanie nazewnictwa
* Wiele podobnych pomysłów było opisywanych niezależnie w różnych ośrodkach

### Algorytm genetyczny
* Sukcesja proporcjonalna
* sukcesja generacyjna lub elitarna
* Reprezentacja binarna
* Krzyżowanie jednopunktowe
* Mutacja bitowa
* Populacje ok. 100 elementów
	* prawdopodobieństwo mutacji ok 0.01
	* prawdopodobieństwo krzyżowania ok. 0.7

### Strategia ewolucyjna
* $\mu$ punktów w populacji bazowej
* powstaje $\lambda$ punktów potomnych (mutantów)
	* raczej $\lambda > \mu$
* z nich robi się kolejne $\mu$ punktów następnej populacji
* warianty $\mu, \lambda$ i $\mu + \lambda$
* równoważne selekcji progowej $\mu, \lambda$
	* nie widać tego przy klasycznym przedstawieniu algorytmu
	* sukcesja prosta
* sukcesja elitarna z elitą wielkości $\mu$ - $\mu + \lambda$
* wbudowany w algorytm mechanizm adaptacji długości kroku
* Reprezentacja rzeczywistoliczbowa
* Krzyżowanie - brak lub uśredniające
* Populacja ok. 100
	* próg około 1/7

### Programowanie ewolucyjne
* Ewolucja automatu skończonego
* Późniejsze warianty podobne do strategii ewolucyjnych
* Selekcja turniejowa
	* 2 osobniki
* Sukcesja elitarna lub generacyjna
* Reprezentacja rzeczywistoliczbowa
* Bez krzyżowania
* Mutacja Gaussowska z adaptacją
* Populacje około 100

### Programowanie genetyczne
* Oryginalnie - ewoluowanie programów w języku LISP
	* drzewiasta przestrzeń danych i przestrzeń kodu (wspólne)
	* program może się zapisywac i potem sam się wykonywać
* Później regresja lub klasyfikacja modelem drzewiastym
* Jak największe populacje >10000
* główny nacisk na krzyżowanie
	* czasami bez mutacji
* trudna analiza formalna przestrzeni drzew

### Programy ewolucji
* Oddzielona warstwa przetwarzania danych od warstwy reprezentacji
	* to na co kładziemy nacisk na wykładach
* Uwzględnienie ograniczeń dziedzinowych

### Poszukiwanie z miekką selekcją
* Galar, PWr
* quasi-species
	* nasze przykłady z chmurami punktów z małym zróżnicowaniem wewnętrznym
* Wniosek, że małe populacje też są dobre
	* rzędu np. 5
	* tym łatwiej przeżyć najgorszemu osobnikowi
* Model procesu przekraczania siodeł

## Ewolucja różnicowa

* inicjuj $P^0$ (populacja, mu elementowe)
* $H$ (historia) = $P^0$
* t$ = 0$
* while !stop
	* for $i = 1..\mu$
		* $P^t_j = select(P^t)$
		* $P^t_k, P^t_l = sample(P^t)$ - wybór z jednakowym prawdopodobieństwem
		* $M^t_i = P^t_j + F(P^t_k - P^t_l)$
		* $O^t_i = crossover(P^t_i, M^t_i)$ - krzyżowanie wymieniające
		* $H = H \cup \{ O^t_i\}$
		* $P^{t+1}_i = tournament(P^t_i, O^t_i)$
	* $t = t + 1$


* Początkowa populacja punktów
* W kolejnej iteracji powstaje kolejna populacja
* Na koniec iteracji wybór w turnieju punktu z początkowej populacji i mutantem
	* każdy punkt ma indywidualnie dobranego potomka
	* potomek trafi do populacji tylko jeśli będzie lepszy niż stary punkt
* Szczególny rodzaj sukcesji elitarnej
	* możliwe że żaden z nowych punktów potomnych nie trafi do nowej populacji
	* jak algorytm wspinaczkowy - nie ma działania populacyjnego
* Generowanie potomka
	* krzyżowanie wymieniające oryginalnego punktu i mutanta
	* mutant przez dodanie do punktu różnicy między dwoma punktami z populacji bazowej (rekombinacja, sumowanie ważone 3 punktów z populacji bazowej)
	* nie przypomina mutacji, nie ma generowania sąsiada
	* mutacja różnicowa
* F to stała
	* np. 0.7
* Nie ma dodawania szumu
* Jest niedeterministyczny przez wybór $P_k$ i $P_l$
	* selekcja może ale nie musi być niedeterministyczna
* Krzyżowanie wymieniające
	* równomierne lub jednopunktowe
* Jeden z najlepszych algorytmów do optymalizacji globalnej w przestrzeni liczb rzeczywistych

### Typy ewolucji różnicowej
* Typ selekcji
	* wybór losowego (rand)
	* wybór nalepszego w populacji (best)
* Typ krzyżowania
	* dwumianowe (bin)
	* wykładnicze (exp)
* Liczba par różnicowanych punktów
	* 1 albo 2
	* powyżej przykład z jedną parą
* Konwencja oznaczeń
	* `DE/rand/1/bin`

### Krzyżowanie dwumianowe

* for $i = 1..n$
	* if $a < c_r$
		* $z_i = y_i$
	* else
		* $z_i = x_i$
* return $z$

* x i y to wektory liczb rzeczywistych
* dla każdej pozycji w wektorze
	* losowa decyzja z prawdopodobieństwem $c_r$ z którego wektora wybierze się współrzędną
* jak krzyżowanie równomierne
	* w równomiernym każda konfiguracja zer i jedynek jest równie prawdopodobna
	* tak samo dla $c_r = 1/2$
	* ale dla innych wartości $c_r$ - prawdopodobieństwo pojawienia się k jedynek w masce jest rozkładem dwumianowym

### Krzyżowanie wykładnicze

* $i = 1$
* while $i \le n$
	* if $a < c_r$
		* $z_i = y_i$
	* else break
* while $i \le n$
	* $z_i = x_i$
* return $z$

* z prawdopodobieństwem $c_r$ bierze się do pierwszej porażki z pierwszego przodka
* po pierwszej porażce dopełnia się drugim
* jak krzyżowanie jednopunktowe
	* w krzyżowaniu jednopunktowym punkt podziału jest wybierany z rozkładu jednostajnego
	* tutaj z rozkładem wykładniczym
* Denerwujące dla użytkowników
	* czasami dokonuje się losowej permutacji indeksów wektora
	* bardziej zbliżone działanie do krzyżowania równomiernego
* Dla $c_r = 0$ - $O_i = P_i$
* Dla $c_r = 1$ - $O_i = M_i$
	* wyłączenie krzyżowania
* Operator krzyżowania jest asymetryczny
* $c_r$ to nie prawdopodobieństwo

### Kształt chmury punktów po krzyżowaniu
* W wariancie rand
	* $\mu^3$
	* nowa chmura rozciągnięta tak samo jak populacja na początku
	* adaptacja do kształtu populacji
	* symetryczna względem środka geometrycznego (reguła generowania jest symetryczna co do kierunku)
	* sięga dalej niż sięga populacja
* W wariancie best
	* $\mu^2$ - bo jeden punkt jest ustalony
	* symetryczna wokół najlepszego punktu
	* naśladuje kształt populacji bazowej
* Krzyżowanie
	* wprowadza szum
	* charakterystyczny kształt
	* nie w kierunku poprzecznym
* Przy rand/1
	* $E[M^t] = \bar{P_t}$
	* środek ciężkości
	* $C[M^t]$
	* $P^t_k$ - wartość oczekiwana to średnia (środek populacji), macierz kowariancji ...
	* $E[X-Y] = E[X] - E[Y]$
	* $V[X \pm Y] = V[X] + V[Y]$ - jeśli niezależne
	* $E[aX] = aE[X]$
	* $V[aX] = a^2 V[X]$
	* więc $E[M^t] = E[P^t_j + F(P^t_k - P^t_l)]$ 
	* więc $C[M^t] = \sum(P^t) \cdot (1 + 2F^2)$
* Przy best/1
	* $E[M^t] = P^t_{best}$
	* $C[M^t] = \sum(P^t)(2F^2)$
	* mniejsze rozproszenie mutantów w stosunku do populacji bazowej
* Przy best/2
	* $C[M^t] = \sum(P^t)(4F^2)$

### Inne metody selekcji
* rand-to-best
	* na odcinku pomiędzy najlepszym punktem a $P_j$
	* punkt poddawany mutacji
* current-to-rand
	* na odcinku między $P_i$ a $P_j$
* pbest
	* p% najlepszych
	* punkt poddawany mutacji to losowy spośród p% najlepszych

Ślad programu

pojawia się *cień* przez dodanie wektora różnicy z dwóch optimów do punktu z jenego z nich
doadtkowe artefakty z krzyżowania punktu z optimum z punktem z cienia