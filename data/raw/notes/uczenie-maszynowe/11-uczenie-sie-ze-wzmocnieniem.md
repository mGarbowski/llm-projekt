# Uczenie się ze wzmocnieniem

## Scenariusz
* Uczeń i środowisko
* W chwili $t$
	* obserwacja stanu środowiska $x_t$
	* wybór akcji $a_t$ dla stanu $x_t$
	* wykonanie akcji $a_t$
	* obserwacja nagrody $r_t$ i następnego stanu $x_{t+1}$
	* uczenie z wykorzystaniem danych $(a_t, a_t, r_t, x_{t+1})$

## Zadanie ucznia
Długookresowa maksymalizacja nagród

$$ E[\sum_{t=0}^\infty \gamma^t r_t] $$
* Współczynnik dyskontowania $\gamma$
	* $0 < \gamma \le 1$
* Wymaga uwzględnienia opóźnionych efektów wykonanych akcji

### Zadania epizodyczne
* Seria prób (epizodów) o skończonej liczbie kroków
	* w każdym epizodzie jakość działania jest oceniana niezależnie
* Do-sukcesu
	* próby kończy się po osiągnięciu sukcesu
	* należy jak najszybciej dążyć do sukcesu
	* wartość nagrody na końcu próby dodatnia (lub 0)
	* wartość nagrody we wcześniejszych krokach 0 (lub ujemna)
* Do-porażki
	* próba kończy się po odniesieniu porażki
	* należy ją opóźniać jak najdłużej
	* wartość nagrody na końcu próby ujemna (lub 0)
	* wartość nagrody we wcześniejszych krokach 0 (lub dodatnia)

## Proces decyzyjny Markowa

$$\langle X, A, \delta, \rho \rangle $$

* $X$ - skończony zbiór stanów
* $A$ - skończony zbiór akcji
* $\delta$ - funkcja przejść
* $\rho$ - funkcja nagród

### Funkcja przejść
* $\delta(x, a)$
* Zmienna losowa oznaczająca stan osiągany po wykonaniu akcji $a$ w stanie $x$
* $P_{xy}(a) = P(\delta(x,a) = y)$

### Funkcja nagród
* $\rho(x,a)$
* Zmienna losowa oznaczająca nagrodę po wykonaniu akcji $a$ w stanie $x$
* $R(x,a) = E[\rho(x,a)]$

### Własność Markowa
Nagrody i przejścia zależą tylko od aktualnego stanu i akcji, a nie od historii

## Strategie i funkcje wartości

### Strategia
Stacjonarna, deterministyczna
$$ \pi: X \rightarrow A $$

### Funkcja wartości ze względu na strategię $\pi$
$$ V^\pi(x) = E_\pi[\sum_{t=0}^\infty \gamma^t r_t | x_0=x] $$
* $E_\pi$ - wartość oczekiwana pod warunkiem posługiwania się strategią $\pi$

### Funkcja wartości akcji ze względu na strategię $\pi$
$$ Q^\pi(x,a) = E_\pi[\rho(x,a) + \sum_{t=0}^\infty \gamma^t r_t | x_0=x, a_0=a ] $$
* $V^\pi(x) = Q^\pi(x, \pi(x))$

## Optymalność
* Strategia $\pi_1$ jest lepsza niż strategia $\pi_2$ jeśli
	* $(\forall x \in X) V^{\pi_1}(x) \ge V^{\pi_2}(x)$
	* $(\exists x \in X) V^{\pi_1}(x) > V^{\pi_2}(x)$
* Strategia jest optymalna jeśli nie istnieje lepsza
* Istnieje co najmniej jedna strategia optymalna
	* może być więcej
	* Wszystkie strategie optymalne mają tę samą optymalną funkcję wartości $V^*$ i optymalną funkcję wartości akcji $Q^*$

## Równania Bellmana
Rekurencyjne zależności dla funkcji wartości i wartości akcji, umożliwiają wyznacznie przez rozwiązanie układu równań.

$$ V^\pi(x) = R(x, \pi(x)) + \gamma \sum_y P_{xy}(\pi(x)) V^\pi(y) $$
$$ Q^\pi(x, a) = R(x, a) + \gamma \sum_y P_{xy}(a) Q^\pi(y, \pi(y)) $$
$$ V^*\pi*(x) = \max_a[ R(x, a) + \gamma \sum_y P_{xy}(a) V^*(y) ] $$
$$ Q^*\pi*(x, a) = R(x, a) + \gamma \sum_y P_{xy}(a) \max_{a'} Q^*(y, a') $$

## Algorytmy programowania dynamicznego
* Optymalizacja dyskretna
* Rozwiązanie konstruowane przez sekwencję decyzji
* Rozwiązanie całościowe jest złożeniem początkowej decyzji i reszty decyzji
* Podjęcie pierwszej decyzji i rozwiązanie podproblemu tej samej natury, skróconego o pierwszą decyzję
* Jakość całego rozwiązania można wyrazić jako sumę jakości pierwszej decyzji i jakości rozwiązania podproblemu

### Strategia zachłanna
Zakładamy że mamy jakąś wcześniejszą strategię $\pi$ dla której znamy funkcję wartości $V^\pi$ (lub $Q^\pi$)

$$ \pi'(x) = \arg \max_a [R(x,a) + \gamma \sum_y P_{xy}(a) \cdot V^\pi(y)] $$
Alternatywna postać

$$ \pi'(x) = \arg \max_a Q^\pi(x,a) $$

* Nagroda z pierwszego kroku + to co będzie dalej
* Może wybrać inną akcję niż $\pi$
* Strategia zachłanna względem $\pi$
* Strategia $\pi'$ jest lepsza niż $\pi$ albo obie są optymalne

### Iteracja strategii
Jeśli na początek znajdziemy dowolną strategię, a potem będziemy wyznaczać coraz lepsze tym sposobem, dla skończonego zbioru strategii znaleziemy strategię optymalną

* $\pi_0$ - strategia początkowa
* dla $k = 0, 1, \ldots$
	* wyznacz $V^{\pi_k}$ (lub $Q^{\pi_k}$)
	* wyznacz $\pi_{k+1}$ jako strategię zachłanną względem $V^{\pi_k}$
* stop kiedy $V^{\pi_{k+1}} = V^{\pi_k}$

### Iteracja wartości
Sekwencja funkcji wartości

* $V^*_0$ - dowolna funkcja wartości
* dla $k = 0, 1, \ldots$
	* $V^*_{k+1}(x) := \max_a [R(x,a) + \gamma \sum_y P_{xy}(a) V^*_k(y)]$
	* (iteracyjne stosowanie równania Bellmana)
* stop: $V^*_{k+1} \simeq V^*_k$

Dla funkcji $Q$

* $Q^*_0$ - dowolna funkcja wartości
* dla $k = 0, 1, \ldots$
	* $Q^*_{k+1}(x, a) := R(x,a) + \gamma \sum_y P_{xy}(a) \max_{a'} Q^*_k(y,a')$
	* (iteracyjne stosowanie równania Bellmana)
* stop: $Q^*_{k+1} \simeq Q^*_k$


* Wyznaczana jest funkcja wartości dla optymalnej strategii
* Wyznaczanie strategii optymalnej - wyznaczenie strategii zachłannej względem wyznaczonego $V^*$

### Różnica między programowaniem dynamicznym a RL
* To jeszcze nie jest uczenie się ze wzmocnieniem (ani żadne uczenie)
	* to tylko przepis na znalezienie strategii optymalnej
	* zakładamy że $R$ i $P_{xy}$ są znane - środowisko jest w pełni znane
	* nie wymaga kontaktu ze środowiskiem ani wykonywania żadnych akcji
* W uczeniu się - środowisko nie jest w pełni znane
	* uczeń wykonuje akcję i wtedy dowiaduje się o nagrodzie i następnym stanie
	* nie są znane oczekiwane wartości i prawdopodobieństwa przejść
* W uczeniu ze wzmocnieniem wystarczy, że uczeń będzie zachowywał się optymalnie
	* wybierze najlepszą akcję w tych stanach, które spotyka
	* mogą istnieć stany, których uczeń nie spotka - nie wie co w nich zrobić ale to nie szkodzi
	* więc w uczeniu się wyznaczamy trochę mniej niż strategię optymalną
* W uczeniu się ze wzmocnieniem
	* sbiór stanów może nie być skończony
	* można stosować aproksymację dla stanów nieznanych wcześniej, ale podobnych do już znanych

## Q-learning
$$ t: \quad x_t, a_t, r_t, x_{t+1} $$
$$ Q_{t+1}(x_t, a_t) := (1-\beta)Q_t(x_t,a_t) + \beta[r_t + \gamma \max_a Q_t(x_{t+1}, a)] $$

 
* Z wagą $\beta$ czynnik odpowiadający prawej stronie równania Bellmana (jak w algorytmie iteracji wartości wyżej)
* Parametr $\beta$ - współczynnik uczenia się / rozmiar kroku
	* $0 < \beta < 1$
	* nie zastępujemy starej wartości, bo dopuszczamy że środowisko nie jest deterministyczne
	* następny stan nie musi być jedynym możliwym
	* nie ufamy w pełni pojedynczej obserwacji
* Zamiast oczekiwanej wartości nagrody $R(x,a)$ jest faktyczna wartość $r_t$
* Symlacja Monte-Carlo równania Bellmana dla $Q^*$

### Warunki zbieżności
$Q$ zbiega do $Q^*$ pod warunkiem, że

* Możliwa jest tablicowa reprezentacja funkcji $Q$
	* nie wykorzystujemy żadnego podobieństwa między stanami itp.
* W każdym stanie, każda akcja ma prawdopodobieństwo wyboru większe od $0$
	* nie wybieramy zawsze akcji o maksymalnej wartości $Q$
* Do $i$-tej aktualizacji stosujemy $\beta_i(x,a)$ takie że $\sum_{i=1}^\infty \beta_i(x,a) = \infty$ ale $\sum_{i=1}^\infty \beta_i^2(x,a) < \infty$ 
	* zależy np. który raz spotykmay taką parę
	* może być ważniejsze, żeby system szybko znajdował wystarczająco dobrą wartość

Warunki nie muszą być spełnione żeby w praktyce algorytm dawał zadowalające rezultaty

### Wybór akcji
* Z punktu widzenia zbieżności algorytmu w ogóle nie trzeba posługiwać się $Q$ przy wyborze akcji
* Algorytmy off-policy (niezależne od strategii)
	* nie musi posługiwać się tą strategią, której się uczy
* Balans między eksploracją a eksploatacją
	* różne podejścia
	* w symulacji gdzie błędne decyzje nie bolą można ustawić wysoką losowość
	* można zmniejszać losowość w miarę uczenia się

#### Strategia $\epsilon$-zachłanna
* Wybór $a_t$
	* akcja jednostajnie losowana z prawdopodobieńśtwem $\epsilon$
	* akcja maksymalizująca $Q(x_t, \ldots)$ z prawdopodobieństwem $1-\epsilon$

#### Strategia Boltzmanna (soft-max)
* Prawdopodobieństwo wyboru akcji
* Dla dużego $T$ - mniej ważna wartość $Q$ - bardziej zlbiżony do rozkładu jendostajnego
* Małe $T$ - większa preferencja dla największych wartości $Q$ - bliżej strategii zachłannej

$$P(x, a) = \frac{\exp(Q(x,a)/T}{\sum_{a'} \exp(x, a')/T} $$

## Aproksymator funkcji
* Coś w rodzaju modelu regresji
* Na wejściu stan (i może akcja)
* Na wyjściu produkuje liczbę
* Stan to wektor wartości atrybutów
* Zakładamy że akcji jest niewiele (kilka)
	* będzie osobny model dla każdej akcji
	* nie dajemy akcji na wejście
* Stosujemy model regresji, który przetwarza po jednym przykładzie na raz
	* np. alternatywna postać regresji liniowej
	* $Q_{t+1}(x_t,a_t) = Q_t(x_t,a_t) + \beta(r_t + \gamma \max_a Q_t(x_{t+1},a) - Q_t(x_t,a_t))$ 
	* wartość dotychczasowa + poprawka
	* to można podstawić w miejsce $(f-h)$ wzoru regresji
	* $f = r_t + \gamma \max_a Q_t(x_{t+1},a)$
	* $h = Q_t(x_t,a_t)$
* Powszechnie stosuje się inne, bardziej złożone modele
	* np. sieci neuronowe głębokie
	* deep Q-network
* Umożliwia generalizację uczenia i możliwość stosowania kiedy nie ma tablicowej reprezentacji funkcji $Q$

## Sarsa
State-action-reward-state-action

$$ Q_{t+1}(x_t,a_t) = (1-\beta)Q_t(x_t,a_t) + \beta[r_t + \gamma Q_t(x_{t+1},a_{t+1})] $$

* Opóźniona aktualizacja do wyboru następnej akcji
* Uczy się wartości Q względem aktualnej strategii, a nie strategii optymalnej
* Chociaż nie ma jawnego zachłannego wyboru
* Nie ma teoretycznych gwarancji zbieżności jak w Q-learning
	* w praktyce Sarsa uczy się szybciej

## Co dalej
* Aktualnie mamy okres renesansu uczenia ze wzmocnieniem - można obsługiwać bardziej złożone stany na wejściu (obraz z kamery, tekst w języku naturalnym) wykorzystując głębokie sieci neuronowe
* Duże modele językowe wykorzystują mechanizm RLHF (uczenie ze wzmocnieniem z oceną użytkownika)
* Badania zastosowania dla problemów bez własności Markowa
