# Regresja

## Regresja liniowa

### Model liniowy

$$ 
h(x) 
= \sum_{i=1}^n w_i a_i(x) + w_{n+1} 
= \sum_{i=1}^{n+1}w_i a_i(x) 
= \mathbf{w} \cdot \mathbf{a}(x)
$$

* Kombinacja liniowa
* Wektor wag $\mathbf{w}$
* Wektor atrybutów $\mathbf{a}(x)$ (ciągłych)
* Wyraz wolny oznaczamy jako $w_{n+1}$
* Zapis w postaci iloczynu skalarnego, zakładamy, że $a_{n+1}(x) = 1$
* Estymacja parametrów
	* minimalizacja *funkcji straty* proporcjonalnej do błędu średniokwadratowego na zbiorze trenującym
	* $E_{T,f}(h) = \frac{1}{2} \sum_{x\in T}(f(x)-h(x))^2$
	* nie ma dzielenia przez liczbę przykładów - dla wygody zapisu, nie robi różnicy
* Cały model jest reprezentowany przez wektor parametrów
	* uczenie polega na doborze (dopasowaniu) parametrów

### Metoda gradientowa
$$ w := w + \beta (-\nabla_w E_{T,f}(h)) $$
$$ \nabla_wE_{T,f}(h) = 1/2 \sum_{x \in T} 2(f(x)-h(x)) \nabla_w(-h(x)) $$
$$ = \sum_{x \in T} (f(x)-h(x))(-a(x)) $$
* Stosowane iteracyjnie
* Wymaga wyliczenia gradientu na całym zbiorze trenującym
* Inicjalizacja wag
	* same 1
	* małe wartości losowe
* Bardziej zaawansowane metody gradientowe
	* metoda Newtona
	* Adam
	* AdaGrad

### Stochastyczny spadek gradientu
* SGD
* Aktualizacja dla pojedynczych przykładów w kolejności losowej
* Poprawia jakość dla jednego przykładu na raz
	* wielokrotne powtarzanie daje efekt uśredniający
* Częściej używany
	* nie wymaga obliczeń na całym zbiorze trenującym na raz
	* zbiór trenujący nie musi być dostępny cały w pamięci, można po 1 na raz

$$ w := w + \beta(f(x)-h(x))a(x) $$

### Metoda najmniejszych kwadratów
* Zamknięta formuła na wyznaczenie parametrów
* Układ równań
	* $a_1(x_i)w_1 + \ldots + a_n(x_i)w_n + a_{n+1}(x_i)w_{n+1} = f(x)$
	* niewiadome to współczynniki modelu
	* tyle równań ile przykładów
	* liczba przykładów znacznie większa niż liczba atrybutów
* Zapis macierzowy $Aw=f$
	* A - macierz wartości atrybutów
	* $|T|$ wierszy
	* $n+1$ kolumn
	* $A^TAw=A^Tf$
	* $A^TA$ - macierz $(n+1) \times (n+1)$
	* $w = (A^TA)^{-1}A^Tf$
* Tą metodą oblicza się w praktyce parametry dla modeli liniowych

## Klasyfikacja liniowo-progowa

### Reprezentacja liniowo-progowa
* Wewnętrzna reprezentacja liniowa $g(x) = \mathbf{w} \cdot \mathbf{a}(x)$
* Zewnętrzna funkcja progowa $h(x) = 1$ jeśli $g(x) \ge 0$, $0$ w przeciwnym przypadku
	* klasyfikacja binarna
	* granica decyzyjna
* Odrzuca się jeden wymiar z hiperpłaszczyzny
* Wymiar VC $n+1$
	* ograniczone ryzyko nadmiernego dopasowania

### Odległość od granicy decyzyjnej

Odległość ze znakiem (dla klasy 1 dodatnia, dla klasy 0 ujemna)

$$ \delta_w(x) = \frac{w \cdot a(x)}{\|w_{1:n}\|} $$

Odległość bezwzględna dla przykładów niepoprawnie klasyfikownanych (sztuczka) $-c_-(x) \delta_w(x)$

$$ c_-(x) = 2c(x) - 1 = \begin{cases}
	+1 \quad dla \quad c(x)=1 \\
	-1 \quad dla \quad c(x) = 0 \\
\end{cases}
$$
Funkcja decyzyjna $g(x) = w \cdot a(x)$ podejmuje decyzje o przewidywanej klasie używając jakiejś funkcji rzeczywistoliczbowej, odległość od granicy określa ufność predykcji

### Algorytm prosty perceptron
* Nieprzydatny
* Pokazany dla odniesienia z innymi metodami
* Inicjalizacja dowolna, np. same 0
* Aktualizowane parametry jeśli predykcja jest niepoprawna
	* $w:= w + c_-  a(x)$
	* jak algorytm gradientowy
* Zmniejszanie odległości od granicy decyzyjnej dla przykładów źle klasyfikowanych
* Jeśli istnieje granica decyzyjna to algorytm ją znajdzie
* Dla wszystkich przykładów łącznie lub przyrostowo dla pojedynczych przykładów
* Kryterium stopu - poprawna klasyfikacja wszystkich przykładów
	* daje się zastosować tylko dla liniowo serparowalnych klas
* Zbieżność
	* gwarantowana tylko jeśli w zbiorze trenującym klasy są liniowo separowalne
	* dlatego niepraktyczny

## Regresja logistyczna

Wewnętrzna reprezentacja liniowa $g(x) = w \cdot a(x)$

Zewnętrzna logistyczna funkcja łącząca 

$$ logit(p) = \ln \frac{p}{1-p} $$
$$ logit^{-1}(q) = \frac{e^q}{e^q+1} = \frac{1}{1+e^{-q}} $$
$$ logit^{-1}(g(x)) = \pi(x) = P(1|x) $$

Interpretacja

$$ logit(P(1|x)) = \ln \frac{P(1|x)}{P(0|x)} $$

Chcemy powiązać wartości z prawdopodobieństwami klas

Jeśli wyjście modelu liniowego możemy potraktować jako logarytm z ilorazu prawdopodobieństw to stosując funkcję odwrotną możemy odzyskać prawdopodobieństwo klasy

### Wyznaczanie parametrów regresji logistycznej
Logarytm wiarygodności (log-likelihood) - miara zgodności predykcji prawdopodobieństw klas z prawdziwymi klasami

$$ LL_{T,c}(\pi) = \ln P(T,c; \pi) = \ln \prod_{x \in T} P(c(x) | x; \pi) $$


Prawdopodobieństwo klas jakie mają przykłady trenująca w świetle tego jaki jest model

$$P(c(x)|x;\pi) = \begin{cases}
P(1|x) = \pi(x), \quad c(x)=1 \\
P(0|x) = 1 - \pi(x), \quad c(x)=0
\end{cases}$$

Dobry model mówi, że prawdziwe klasy są bardzo prawdopodobne, a nieprawdziwe mało prawdopodobne

Stosujemy sztuczkę, żeby zapisać wzór w jednej formule bez rozejść warunkowych, traktujemy klasę jako wartość liczbową

$$ \ln \prod_{x \in T} \pi(x)^{c(x)} (1-\pi(x))^{1-c(x)} $$
$$ \sum_{x \in T} (c(x) \ln \pi(x) + (1-c(x)) \ln (1-\pi(x))) $$

Oblicza się gradient z tego wzoru i stosuje do metody gradientowej, taka sama postać jak gradient w regresji liniowej

$$ \nabla_w LL_{T,c}(\pi) = \sum_{x \in T} (c(x) - \pi(x))a(x) $$
$$ w := w + \beta \nabla_2 LL_{T,c}(\pi) $$

* W efekcie uzyskuje się maksymalną zgodność predykcji z prawdopodobieństwami prawdziwych klas
* Radzi sobie z klasami, które nie są liniowo separowalne
* Pojawia się w sieciach neuronowych

## Zagadnienia praktyczne

### Atrybuty dyskretne
* Kodowanie binarne - zastąpienie przez $k-1$ atrybutów binarnych
	* one hot encoding
	* dummy variables
	* lepiej kodować przez o 1 mniej atrybutów - nie można reprezentować nielegalnej wartości
* Kodowanie przez $k$ atrybutów binarnych jest szkodliwe
	* liniowa zależność
	* gdzieś może powstać macierz nieosobliwa

### Klasyfikacja wieloklasowa
* 1 kontra reszta (one vs rest, OVR)
	* osobny model binarny dla każdej klasy
	* predykcja przez wybór klasy o maksymalnej wartości funkcji decyzyjnej
	* może się zdarzyć, że więcej niż jeden model daje predykcję pozytywną
	* trzeba użyć prawdopodobieństwa lub wartości funkcji decyzyjnej dla rozstrzygnięcia 
* 1 kontra 1 (one vs one, OvO)
	* osobny model binarny dla każdej pary klas
	* predykcja przez głosowanie

### Właściwośi modeli liniowych
* Wyłącznie zalezności przynajmniej w przybliżeniu liniowe lub liniowo separowalne
* Dobór parametrów odporny na optima lokalne
* Efektywna metoda najmniejszych kwadratów (dla regresji liniowej)
* Interpretowalne parametry modelu
* Ograniczone ryzyko nadmiernego dopasowania
* Możliwe bardziej zaawansowane warianty
	* częściowo lub cał…owicie pokonują ograniczenia liniowości
	* np. SVM/SVR
