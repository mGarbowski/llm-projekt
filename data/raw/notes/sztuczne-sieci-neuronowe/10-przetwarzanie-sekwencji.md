# Przetwarzanie sekwencji i tłumaczenie maszynowe

## Sieci dwukierunkowe
* Dwie sieci rekurencyjne
* Zadanie - wskazywanie specyficznych fragmentów sekwencji
* Problem - dopiero później dowiemy się że to był ten interesujący nas fragment
* Rozwiązanie - jedna sieć przechodzi sekwencję w jedną stronę, a druga w drugą
	* wyjścia z obu sieci produkujących stan ($m$ i $m'$) trafiają do sieci produkującej wyjście ($g$)

## Sieci wielowymiarowe
* Więcej wymiarów, które potraktujemy analogicznie jak czas
	* np. współrzędne $x$ i $y$ piksela w obrazie
* Możemy traktować wielowymiarowe dane jako sekwencje
	* np. obraz 2D
* Dostęp do poprzedniego elementu sekwencji jednego i drugiego wymiaru
* Jest jedna sieć, która idzie np. od lewego dolnego piksela do prawego górnego
* Oblicza stan na podstawie
	* wartości piksela
	* stanu dla piksela po lewej
	* stanu dla piksela po prawej
* $h_{x,y} = m(h_{x-1,y}, h_{x, y-1}, x_{x,y}; \theta)$

## Sieci wielowymiarowe-dwukierunkowe
* Przed sieciami splotowymi
* Mamy $n$ wymiarów takich jak czas
* Po każdym wymiarze sieci chodzą w oba kierunki
* Sieci jest tyle ile kombinacji kierunków - $2^n$
	* dla 2D lewo-góra, lewo-dół, prawo-góra, prawo-dół

## Alternatywy dla rekurencji rozwiązujące ten sam problem

### Przesuwające się okno
* Sliding window
* $y_t = f(x_t, \ldots, x_{t-w+1}; \theta)$
	* $w$ - szerokość okna
* Oprócz elementu aktualnego bierze też określoną liczbę poprzednich elementów
* Bez operacji rekurencyjnych
* Działa szybko
* Nie ma dostępu do stanu, nie wiemy co było przed oknem
* Waga każdego elementu jest jednakowa
	* sieć może przypisać wagę co najwyżej do pozycji w oknie

### Atencja
* Liczba głów uwagi $m$
	* wynik z wielu głów agreguje się na końcu
* Szerokość okna $w$
* Dopisujemy do każdego $x_i$ znaczniki pozycji
	* $\sin((t-i)/p)$, $\cos((t-i)/p)$
	* między $-1$ i $1$
	* relatywna pozycja elementu w całej sekwencji
	* kilka różnych $p$ - skala (bardziej lokalne / bardziej globalne)
	* ten sam token ale na różnych pozycjach dostaje różne zanurzenia
* Każdej głowie odpowiada sieć $b_j$
	* $a_{i,j} = b_j(x_i, \ldots, x_{i-w+1}; \nu)$
	* wyjście sieci - $a_{i,j}$ - waga konkretnego elementu
* Dla każdej głowy sieć $g_j$
	* przetwarza okno sekwencji wejściowej w wynik
	* wyjście ważone wagami $a_{i,j}$
	* $o_j = (\sum_{i=w}^t \exp(a_{i,j}) g_j(x_i, \ldots, x_{i-w+1}; \nu) / (\sum_{i=w}^t \exp(a_{i,j}))$
* Wyjścia z każdej głowy agregowane przez kolejną sieć acykliczną
	* $f(o_1, \ldots, o_m; \theta)$
* Sprawdza się dużo lepiej niż przesuwające się okno

## Dowolne przekształcenie sekwencja-sekwencja

* Architektury
* Wejście - sekwencja o dowolnej długości
* Wyjście - sekwencja o dowolnej długości
* Zadania
	* tłumaczenie maszynowe
	* transkrypcja mowy
	* przetwarzanie sekwencji DNA

## Tłumaczenie maszynowe

### Słowa w wektorach
* Cel - reprezentacja słów wektorami
* Wektory reprezentacji (embeddings)
	* wektor liczb rzeczywistych reprezentujących dane słowo (token)
* Zagnieżdżenia
	* Word2Vec
	* GloVe
	* BERT
* Zagnieżdżenia dla języków bierze się z bibliotek
	* nie trenuje się tego na własną rękę
	* użycie gotowców jest wskazane

### Word2Vec
* Technika uczenia modelu generującego zanurzenia z tokenów
* Trenuje się model z dwoma warstwami
	* pierwsza warstwa zamienia indeks w słowniku na embedding
	* druga zamienia embedding na rozkład prawdopodobieństwa
	* po treningu używa się tylko tej pierwszej do generowania zanurzeń
	* są 2 podejścia do uczenia - zadania optymalizacji na tym rozkładzie prawdopodobieństw
* Continuous Bag Of Words
	* Okno - słowa wcześniej i później
	* promień okna - $C$
	* maksymalizujemy prawdopodobieństwo słowa na miejscu $t$ pod warunkiem że przed i po są określone słowa
	* $\max P(x_t | x_{t+i}), \quad i \in \{-C, \ldots, -1, 1, \ldots, C\}$
	* przewiduje docelowe słowo na podstawie kontekstu
	* model oblicza zanurzenia dla wszystkich słów z kontekstu a potem je uśrednia
* Skip-Gram
	* odwrotnie niż CBOW
	* wiedząc że w miejscu $t$ jest słowo $x_t$ maksymalizujemy prawdopodobieństwo że dookoła (w oknie) są określone słowa
	* przewidywanie okna kontekstu na podstawie jednego słowa
* W porządku dla małych słowników
* Zagnieżdżenia dotyczą całych słów

### Enkoder-dekoder
* Najczęściej symetryczne części
* Koder
	* koduje sekwencję wejściową
	* nie ma wyjść
	* produkuje swój stan ukryty
* Dekoder
	* produkuje wyjściową sekwencję na podstawie stanu ukrytego kodera
	* ostatni element to EOS (end of sentence)
* Prosta architektura
* Zbija całą sekwencję w stałowymiarowy wektor
	* może być duża strata informacji
* Nie ma ważenia elementów w sekwencji wejściowej

### Enkoder-dekoder z atencją
* Koder - dwukierunkowa, rekurencyjna sieć
	* produkuje adnotacje
* Warstwa atencji tworzy wagi adnotacji
	* poprawia działanie dekodera bo dzięki wagom skupia się bardziej na ważniejszych elementach
* Dekoder wykorzystuje ważone adnotacje i stan kodera do produkowania wyjścia

### Enkoder-dekoder z atencją v2
* Dodatkowo rekurencyjna część dekodera i sprzężenie zwrotne
* Przy atencji bierze pod uwagę stan ukryty z części kodera i z części dekodera
* Zakodowana informacja o wszystkich elementach wyjścia i wejścia do momentu $t$
	* lepsze ważenie
	* lepsze określenie co jest ważne
