# Sieci rekurencyjne

## Rozwiązanie równania ruchu kuli pod wpływem sił
* Rozwiązanie z oknem czasowym i rozwiązanie ze stanem
* Musimy wiedzieć wszystko na raz
* Ze stanem - z aktualnego stanu wyprowadzamy jakie będzie zachowanie
	* stanem jest pęd kuli
	* nie musimy pamiętać jaki był pęd od początku historii
	* wystarczy wiedzieć jaki jest teraz

## Zarys problemu
* Czas dyskretny $t=1,2,\ldots$
* Wejścia i wyjścia - wektory liczb rzeczywistych
* Sieć ma nauczyć się $y_t = f(x_t, x_{t-1}, \ldots)$
* Zastosowania
	* prognozowanie
	* szeregi czasowe
	* przetwarzanie dźwięku
	* przetwarzanie języka naturalnego

### Przykład - zapotrzebowanie na energię elektryczną
* Autoregresja - bierzemy to co było tydzień temu
	* można wziąć informacje o pogodzie z tego co było 1 dzień temu
* Nie wszystkie dane wejściowe są równie użyteczne
	* np. dzień temu i tydzień temu, a pomiędzy nie
	* okno historii - nie musi być pełne
* Oszustwo przy modelowaniu - zakładamy że wiemy jaka będzie np temperatura za 24h i na tej podstawie robimy swoją prognozę
* Pomija się odstęp między momentem wystawienia prognozy i momentem na który ma być wystawiona prognoza
	* np. prognozę na cały czwartek trzeba znać w środę rano
	* nie znamy wartości poprzedzających moment prognozy
* Mamy 2 podejścia
* Podejście 1
	* model przewiduje na godzinę do przodu, prognozujemy od teraz do końca czwartku
	* błąd może się kumulować
	* gdyby błędy nie były z sobą skorelowane to wartość oczekiwana byłaby 0
	* ale błędy są skorelowane bo kolejny używa poprzedniego
* Podejście 2 - zwiększyć krok prognozy
	* nie o godzinę do przodu tylko od teraz do momentu na który ma być prognoza
	* błąd się nie kumuluje

## Sieć rekurencyjna
* $m$ - moduł (sieć neuronowa) generujący stan
	* $h_t = m(h_{t-i}, x_t; \theta)$
* $g$ - moduł (sieć neuronowa) generujący wyjście
	* $y_t = g(h_t, x_t; \theta)$
* Wartość stanu zostaje zapamiętana (zatrzaśnięta)
	* na wejście do kolejnej iteracji wchodzi stan z poprzedniej iteracji
* Jak interpretować stan, co ma być stanem
	* raczej stan powinien mieć nie mniejszą wymiarowość niż wejście
	* w sieci rekurencyjnej nie dbamy o interpretację
* Mamy źródło generujące sekwencję danych i model generujący sekwencję danych
* Jak policzyć gradient względem wag modułów $m$ i $g$
	* jest zależność czasowa - element zatrzaskujący stan
	* musimy policzyć wpływ wszystkich poprzednich modułów - rekurencja
* Funkcja straty
	* $q_t(y_t)$ - strata dla pojedynczego elementu sekwencji wyjściowej
	* w treningu minimalizujemy $\bar{q}(\theta) = \sum_t q_t(y_t)$
* Częściowy wskaźnik jakości
	* $\bar{q}_t(h_{t-1}, \theta) = q_t(y_t) + \bar{q}_{t+1}(h_t, \theta)$


## Wsteczna propagacja przez czas
* Pochodna skumulowanej straty bezpośrednio po parametrach - regularyzacja
* Sieć musi najpierw działać przez jakiś czas żeby było z czego przepropagować gradient
* Przy przejściu w przód są wyliczane $h_0, h_1, \ldots h_T$
* Przy propagacji wstecz jest przejście od $t=T$ do $t=0$
* Po epizodzie - aktualizacja $\theta$ na podstawie $\frac{\partial \bar{q}(\theta)}{\partial \theta}$
	* jeden epizod - jedna aktualizacja
	* problem z długimi epizodami
	* rozwiązanie - traktować krótsze fragmenty historii jako epizody

## Uczenie z gradientem obliczanym w przód
* Real-Time Recurrent Learning
* Rekurencja obliczana od $t=0$ do $t=T$
* Po każdej chwili $t$ aktualizacja wag $\theta$ na podstawie $\frac{d q_t}{d \theta}$
	* trzeba aktualizować $\frac{d h_t}{d \theta}$

## Problem zanikającego / eksplodującego gradientu
* Wpływ wagi na wyjście $y_t$ może rosnąć wraz z $t$
	* dla prostego liniowego modelu $y_t = \theta^t y_0$
	* $\frac{dy_t}{d\theta} = t \theta^{t-1} y_0$
	* bardzo szybko rośnie / zanika wraz z $t$
* Okno czasowe zawsze będzie używane w całości
* Koncepcja rozwiązania
	* podobnie do mechanizmu atencji
	* moduł stanu z bramkami
	* zawartość pamięci sieci ($h_t$) pozostaje stała, no chyba że coś ją zmienia
	* bramka mówi czy stan powinien się zmienić pod wpływem wejścia (wykrywa okoliczności do zmiany)

## GRU
* Pomija się niektóre z przeszłych stanów
* Update gate
	* model, który na podstawie stanu poprzedniego i wejścia generuje wagę $z$
	* jeśli $z$ jest bliskie $1$ to stan będzie zależał w dużym stopniu od wyjścia novum gate
	* jeśli $z$ jest bliskie $0$ to stan bieżący będzie zbliżony do stanu poprzedniego
* Novum gate
	* $\tanh$ - wartość od $-1$ do $+1$
	* zależy od wejścia i od tego czy reset gate przepuszcza stan czy nie
* Reset gate
	* sigmoid - wartość od $0$ do $1$
	* określa czy stan ma czy nie ma być propagowany dalej
* Możliwe działania
	* przepuszczenie poprzedniego stanu
	* na wyjściu funkcja wejścia
	* na wyjściu funkcja wejścia i poprzedniego stanu

```python
if update(h[t-1], x[t]):
	if reset(h[t-1], x[t]):
		h[t] = novum(h[t-1], x[t])
	else:
		h[t] = novum(0, x[t])
else:
	h[t] = h[t-1]
```


![GRU network diagram](./obrazy/gru-network.png)

## LSTM
* Long Short-Term Memory
* Dodatkowo sygnał sterujący $c$ - kolejny stan
	* stan kontrolny
* Forget gate
	* steruje stanem kontrolnym
	* zerowany
	* bez zmian
	* wyjście update
	* wyjście update + poprzedni stan kontrolny
* Output gate
	* czy pod stan $h$ podstawiany stan kontrolny czy $0$

```python
if forget(h[t-1], x[t]):
	if input(h[t-1], x[t]):
		c[t] = update(h[t-1], x[t]) + c[t-1]
	else:
		c[t] = c[t-1]
else:
	if input(h[t-1], x[t]):
		c[t] = update(h[t-1], x[t])
	else:
		c[t] = 0

if output(h[t-1], x[t]):
	h[t] = c[t]
else:
	h[t] = 0
```

![LSTM network diagram](./obrazy/lstm-network.png)
