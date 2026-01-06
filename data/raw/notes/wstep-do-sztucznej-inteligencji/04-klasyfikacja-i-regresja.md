# Klasyfikacja i regresja
Dwa najczęstsze zadania w uczeniu maszynowym

## Wysokopoziomowy obraz
* Istnieje jakaś zależność w świecie rzeczywistym
* Mamy dane o tym zjawisku - pomiary
* Trenujemy model na zbiorze uczącym - proces optymalizacji
* Model jest funkcją, przybliżeniem zależności ze świata rzeczywistego

### Zastosowania
* Sterowniki dla systemów o nieznanej dynamice
* Budowa modeli na podstawie napływających danych

### Techniki
* Aproksymacja funkcji (regresja)
* Klasyfikacja
* Grupowanie
* Uczenie się ze wzmocnieniem

### Narzędzia
* Sieci neuronowe
* Drzewa decyzyjne
* Modele Bayesowskie
* ...

## Aproksymacja funkcji
Szukamy przybliżenia $\hat{f}$ funkcji $f: X \rightarrow Y$ mając dany zbiór próbek uczących w postaci $(x_i, f(x_i) + \xi_i)$ , gdzie:
* $X$ - przestrzeń wejściowa
* $Y$ - przestrzeń wyjściowa (np. $\mathbb{R}^n$)
* $x_i \in X$
* $\xi_i$ to losowe błędy (szumy, niedokładności) pomiaru wartości funkcji $f$

Określenia regresja i aproksymacja stosuje się wymiennie (względy historyczne)
$\hat{f}(x) = E(y|x)$ - oczekiwana (średnia, odszumiona) wartość $y$ pod warunkiem $x$

## Klasyfikacja
Przyporządkowanie argumentowi jednej z etykiet

* $X$ - przestrzeń wejść
* $Y$ - przestrzeń **dyskretnych** wyjść
* mamy dany zbiór uczący $(x_i, y_i)$
* $x_i, y_i$ to zmienne losowe opisane rozkładem łącznym $P_{XY}$
* poszukujemy przybliżonej postaci klasyfikatora $\hat{f}(x)$, który dla danego $x$ wskaże najbardziej prawdopodobną wawrtość $y$ (zgodnie z $P_{XY}$)
* inaczej: poszukujemy klasyfikatora $\hat{f}(x) = P_{X,Y}=(y|x)$

Mówimy o najbardziej prawdopodobnej wartości $y$, ponieważ w świecie rzeczywistym te same dane wejściowe mogą oznaczać różne wyniki (zdarzenie są z natury losowe na pewnym poziomie).

Klasyfikator można przedstawić jako granicę decyzyjną (linia rozdzielająca punkty)

## Uogólnienie - problem decyzji statystycznych
* $X$ - przestrzeń wejść
* $Y$ - przestrzeń wyjść
* mamy dany zbiór uczący $(x_i, y_i)$
* $x_i, y_i$ to zmienne losowe opisane rozkładem łącznym $P_{XY}$
* $q$ określa stratę poniesioną na skutek podjęcia danej decyzji
* poszukujemy funkcji decyzyjnej $f: X \rightarrow Y$, która dla danego $x$ wskazuje decyzję minimalizującą $q(f(x))$

### Wskaźniki jakości
#### Globalny wskaźnik jakości
Dla funkcji decyzyjnej
$$J(f) = E[q(f(x))]$$
#### Problem klasyfikacji
$q(f(x)) =$ $0$ gdy $f(x) = y$ (poprawna klasyfikacja), $1$ w przeciwnym przypadku 

#### Problem regresji
Np. błąd średniokwadratowy szacowany na zbiorze $\{(x_i, y_i)\}$
$$q(f) = MSE(f) = \frac{1}{N} \sum_{i=1}^N ||f(x_i) - y_i||^2$$
## Aproksymacja parametryczna
* $\Theta = \mathbb{R}^m$ - przestrzeń parametrów modelu
* Model (aproksymator) ma postać $\hat{f}: X \times \Theta \rightarrow Y$

Przykłady
* model liniowy
	* jednowymiarowy - $\hat{f}(x, \theta) = \theta_0 + \theta_1 \cdot x$ 
	* wielowymiarowy - $\hat{f}(x, w) = w_{[0]} + \sum_{i=1}^n w_{[i]}x_{[i]} = [1, x^T] \cdot w$
* model wielomianowy
	* $\hat{f}(x, \theta) = \theta_0 + \sum_{i=1}^m \theta_i \cdot x^i$ 
* uogólniony model liniowy
	* model liniowy w innej przestrzeni niż ta wejściowa
	* stosujemy przekształcenie
	* jeśli w przestrzeni wejściowej dane nie dają się przybliżyć linią to można je przekształcić do takiej przestrzeni, w której się da
	* $\hat{f}(x, \theta) = \theta_0 + \sum_{i=1}^m \theta_i g_i(x)$
* złożenie funkcji stałych
	* $\hat{f}(x, \theta) = \sum_{i=1}^m \theta_i \phi_i(x)$
	* $\phi_i$ to indykator ($1$ jeśli $x$ należy do podzbioru, $0$ jeśli nie należy)


## Uczenie off-line
Założenia
* Mamy dany w całości skończony zbiór uczący $U$
* Parametry $\theta$ aproksymatora określamy optymalizując funkcję straty

$$
J(\theta) = \frac{1}{N} \sum ||y_i - \hat{f}(x_i, \theta) ||^2
$$

Uczenie modelu sprowadza się do rozwiązania zadania optymalizacji
$$
\hat{\theta} = arg min_{\theta\in\mathbb{R}^m} J(\theta)
$$
Jeżeli da się policzyć gradient $\nabla J(\theta)$ (np. dla modelu liniowego) to dla znalezienia najlepszych parametrów można wykorzystać dowolną metodę gradientową (gradient descent)


## Uczenie on-line
* Potencjalnie nieskończony zbiór danych
* Dany jest generator próbek uczących $\{x_i, y_i\} \sim P_{X,Y}$
* Uczenie przebiega sukcesywnie - po przetworzeniu $i$-tej próbki parametry aproksymatora aktualizowane są do wartości $\theta_i$
* Ciąg wartości $\theta_i$ powinien zbiegać do minimum funkcji straty

$$
J(\theta) = E || y - \hat{f}(x, \theta) ||^2
= \int \int ||y - \hat{f}(x, \theta) ||^2 P_{XY}(x,y) dydx
$$

$X$, $Y$ traktujemy jak zmienne losowe

Nie da się policzyć gradientu funkcji celu ale gradient szacowany na jednej próbce jest nieobciążonym estymatorem gradientu $\nabla J(\theta)$

Wstawiając estymator gradientu $g_i$ do metody gradientu prostego otrzymujemy metodę stochastycznego najszybszego spadku (sformułowany tak samo ale liczony nie względem całego zbioru danych tylko aktualizowany dla każdej kolejnej próbki)

$$
\theta_{i+1} 
= \theta_i - \beta_i \frac{d}{d \theta^T_i} ||y_i - \hat{f}(x_i, \theta_i)||^2
$$

### Ogólny algorytm
* $\theta_1$ - początkowe oszacowanie parametrów
* Wylosuj parę $\{x_i, y_i\} \sim P_{X,Y}$
* Oblicz kolejne przybliżenie $\theta_{i+1}$
* Jeśli spełnione są kryteria stopu - zakończ i zwróć $\theta_{i+1}$, w przeciwnym przypadku powtarzaj

## Maszyny wektorów nośnych
Support Vector Machines (SVM)

* Model ma przewidywać wartości dyskretne - klasy (jest algorytmem klasyfikacji)
* Przypadek binarny $Y = \{-1, 1\}$
* Poszukujemy funkcji decyzyjnej rozgraniczającej kiedy $f > 0$,  a kiedy $f \le 0$
* Obszar gdzie $f(x_i) = 0$ jest granicą decyzyjną między klasami

Liniowa separowalność - klasy w przestrzeni można rozdzielić linią (hiperpłaszczyzną)
Brak liniowej separowalności - nie ma takiej linii (hiperpłaszczyzny), która oddziela klasy

Może być potencjalnie nieskończenie wiele płaszczyzn które rozdzielają klasy ale SVM szuka takiej, która maksymalizuje szerokość obszaru separującego (korytarza) między klasami

### Przypadek liniowo separowalny
* Model $\hat{f}(x) = w^Tx - b$ opisuje linię (hiperpłaszczyznę)
	* oddziela od siebie obie klasy w przestrzeni
	* $w^Tx-b = 0$ to środek obszaru separującego
	* z jednej strony granicą jest prosta $w^Tx-b =1$ a z drugiej strony $-1$
	* obszar separujący jest jak najszerszy
	* $w$ i $b$ to parametry hiperpłaszczyzny
* Szerokość regionu separującego $\frac{2}{||w||}$
* Odległość wektora $x_0$ od prostej $w^Tx + b = 0$ to $d = \frac{|w^T x_0 + b|}{||w||}$


Maksymalizujemy szerokość regioniu separującego
Pojedyncze punkty po obu stronach dotykają granicy - wektory nośne
Minimalizujemy $||w||$ przy założeniu że hiperpłaszczyzna musi oddzielać od siebie klasy
zwięźle: $y_i(w^T x_i - b) \ge 1$ 
$y = -1$ dla $f(x) \le 0$, $y=1$ dla $f(x) > 0$
$(w,b) = argmin_{w,b} ||w||^2$

W praktyce wygodniej minimalizować $||w||^2$ 

### Brak liniowej separacji
Jeśli elelmentów psujących liniową separację jest niewiele to można określić funkcję kary za te naruszenia i minimalizować funkcję kary

$$(w,b) = argmin_{w,b} \sum_i \xi_i + \lambda ||w||^2, \lambda > 0$$
$\lambda$ to parametr sterujący, określa na jak duże naruszenia możemy pozwolić
im mniejsza $\lambda$ tym większy wpływ naruszeń

Przy ograniczeniach
$$\xi_i \ge 0$$
$$y_i(w^Tx_i - b) \ge 1 - \xi_i$$
(dopuszczamy przekroczenia)

Więc
$$\xi_i = max(1-f(x_i)y_i, 0)$$

### Twierdzenie o reprezentacji
Wektor $w$ określający separującą hiperpłaszczyznę daje się wyrazić jako kombinacja elementów dotykających granic

$$w = \sum_{i=1}^N \alpha_ix_iy_i$$
$\alpha_i = 0$ dla elementów, które nie dotykają granicy, żeby optymalizować $w$ wystarczy zoptymalizować $\alpha_i$


Dla punktów dotykających obszaru
$$y_i(w^Tx_i - b) = 1 - \xi_i$$


### Postać nieliniowa
Każdy zbiór danych jest liniowo separowalny, jeśli odpowiednio zrzutuje się wcześniej przestrzeń.
Trzeba znaleźć przekształcenie do przestrzeni, w której zadanie będzie prostsze - liniowo separowalne albo prawie liniowo separowalne

$$\phi: X \rightarrow \mathcal{X}$$

$$w = \sum_{i=1}^N \alpha_i \phi(x_i) y_i$$
$$f(x) = w^T \phi(x) - b$$
$$(\alpha_1, \ldots, \alpha_N, b) = argmin_{(\alpha_1, \ldots, \alpha_N, b)} \sum_i max(1-f(x_i)y_i,0) + \lambda ||w||^2$$

### Przekształcenia jądrowe
Przekształcając poprzednie wzory

$$
f(x) = \sum_{i=1}^N \alpha_i y_i \phi(x_i)^T \phi(x) - b
= \sum_{i=1}^N \alpha_i y_i k(x, x_i) - b
$$

Wyliczanie $\phi(x)$ może być kosztowne, więc używa się funkcji jądrowej
$$k(u,v) = \phi(u)^T \phi(v)$$

Katalog funkcji jądrowych
* liniowe
* wielomianowe
* gaussowskie / radialne / RBF
	* wzory....

Za pomocą tych wzorów można taniej liczyć iloczyn skalarny bez faktycznego rzutowania do nowej przestrzeni
Praktyka wygląda tak, że trzeba dostroić parametry wybranej funkcji jądrowej

## Drzewa decyzyjne
* Reprezentują mechanizm decyzyjny
* Węzły odpowiadają atrybutom
* Krawędzie odpowiadają wyborom podejmowanym na podstawie atrybutów
* Liście reprezentują finalne decyzje
* W uczeniu maszynowym - konstruujemy drzewa na podstawie danych trenujących

### Algorytm ID3
Indukcja drzew decyzyjnych (klasyfikacyjnych)

* Drzewa budowane rekurencyjnie
* Liście zawierają klasy
* Predykcja to znalezienie liścia przechodząc po ścieżce wyznaczonej przez wartość atrybutów i zwrócenie jego klasy
* Wady algorytmu
	* budowanie zbyt rozbudowanych drzew
	* nadmierne dopasowanie do zbioru uczącego

#### Selekcja atrybutów do testu
Chcemy wybrać taki atrybut który najbardziej uporządkuje zbiór

* Entropia zbioru $U$
	* $I(U) = - \sum_i f_i ln(f_i)$
	* $f_i$ - częstość i-tej klasy
* Entropia zbioru podzielonego na podzbiory przez atrybut $d$ 
	* $Inf(d,U) = \sum_j \frac{|U_j|}{|U|}I(U_j)$
* Zdobycz informacyjna
	* $InfGain(d, U) = I(U) - Inf(d,U)$

### Algorytm C4.5
Algorytm ID3 może konstruować zbyt rozbudowane drzewa i nadmiernie dopasowane do zbioru uczącego. C4.5 to algorytm ID3 uzupełniony o przycinanie drzewa, ma rozwiązywać te problemy.

* Przycinanie można robić na oddzielnym zbiorze danych (innym niż uczący i testowy)
* Wadą jest zachłanne wybieranie atrybutów do węzłów drzewa

#### Działanie
* Zbudowanie drzewa algorytmem ID3
* Dla każdego liścia sprawdzane są wszystkie węzły na ścieżce liść-korzeń
* Szacuje się błąd w poddrzewie węzła
* Szacuje się błąd gdyby zamienić poddrzewo na liść z najczęstszą klasą w poddrzewie
* Jeśli oszacowanie błędu po przycięciu jest mniejsze to zamienia się poddrzewo na liść

### Las losowy
* Solidny klasyfikator w praktyce
* Buduje się wiele drzew, wynikiem predykcji jest najczęściej zwracana klasa spośród wszystkich drzew
* Zapobiega przeuczaniu modelu
* Zagregowanie predykcji z wielu zaszumionych predyktorów wyeliminuje szumy

#### Działanie
* Wylosować $n$ elementów ze zbioru uczącego ze zwracaniem
* Wylosować $\sqrt{|D|}$ atrybutów ze zbioru wszystkich atrybutów $D$ bez zwracania
* Zbudować drzewo na podstawie tych zbiorów


## Gradient boosting
Model jest budowany iteracyjnie, dodanie kolejnego elementu powinno poprawiać predykcję poprzedniego modelu. Dodaje się kolejne drzewa kompensujące błędy poprzedniego drzewa

* Funkcja straty dla $i$-tego elementu zbioru uczącego np. $q_i(y) = ||y-y_i||^2$
* Model o postaci $\hat{f_k}(x) = \hat{f_0}(x) + \sum_{i=1}^k \gamma_i \widetilde{f_i}(x)$
	* $\widetilde{f_i}$ może być np. modelem drzewiastym
* Psudo residua $r_{ij}$ 
	* błąd w $j$-tej iteracji modelu dla zadanego $i$-tego argumentu
	* podobne rozumienie jak gradient

#### Działanie
* Początkowy model stały $\hat{f_0} = argmin_y \sum_i q_i(y)$
* Powtarzaj $k$ razy
	* oblicz pseudo residua dla obecnej iteracji np. $r_{ij} = 2(y_i - \hat{f}_{j-1}(x_i))$
	* wytrenuj nowy model $\widetilde{f_j}$ na zbiorze $U_j = \{ \langle x_i, r_{ij} \rangle \}$
	* znajdź wagę $\gamma_j$ która zminimalizuje funkcję starty modelu po rozszerzeniu o $\widetilde{f_j}$
	* rozszerz model $\hat{f_j}(x) = \hat{f}_{j-1}(x) + \gamma_j \widetilde{f_j}(x)$


## Naiwny klasyfikator bayesowski
* $y$ to przewidywana klasa, $x_i$ to atrybuty
* Z twierdzenia Bayesa $P(y|x_1, \ldots, x_n) = \frac{P(x_1, \ldots, x_n | y)P(y)}{P(x_1, \ldots, x_n)}$
* Przyjmuje się naiwne założenie, że atrybuty są niezależne
	* wtedy $P(x_1, \ldots, x_n | y) = \Pi_{i=1}^n P(x_i|y)$
* $P(y)$ i $P(x_i|y)$ estymuje się na podstawie zliczania w zbiorze uczącym
* Predykcja to wybór klasy o największym prawdopodobieństwie $P(y)\Pi_{i=1}^n P(x_i|y)$


## Ocena modeli ML
* Generalizacja - jakość modelu dla danych spoza zbioru uczącego
* Przeuczenie (overfitting) - nadmierne dopasowanie modelu do zbioru uczącego
* Niedotrenowanie (underfitting) - niezdolność modelu do dopasowania do zbioru uczącego
### Przeuczenie
* Nadmierne dopasowanie modelu do zbioru uczącego, brak zdolności generalizacji
* Przyczyny
	* zbyt skomplikowana postać
	* zbyt długa optymalizacja parametrów modelu
	* za mały zbiór danych uczących
	* niereprezentatywny zbiór danych uczących
* Przeciwdziałanie
	* kontrolowanie struktury modelu - uproszczenie struktury może dać lepsze efekty
	* stosowanie agregacji - jak w lasach losowych
	* stosowanie regularyzacji podczas trenowania
	* dropout w modelach neuronowych

### Regularyzacja
* Rozszerzenie funkcji straty o dodatkową składową karzącą za zbyt rozbudowany model
* Regularyzacja $L_1$: $J(\theta) = \frac{1}{N} \sum_{i=1}^N ||y_i - \hat{f}(x_i, \theta)||^2 + \lambda ||\theta||$
* Regularyzacja $L_2$: $J(\theta) = \frac{1}{N} \sum_{i=1}^N ||y_i - \hat{f}(x_i, \theta)||^2 + \lambda ||\theta||^2$

### Ocena jakości modelu
Żeby uniknąć przeuczenia, działanie modelu należy oceniać na danych, które nie były używane do uczenia. Podstawowa strategia to podział zbioru danych na uczący i testowy (typowo w proporcjach $80:20$, $75:25$)

#### k-krotna walidacja krzyżowa
* Zbiór danych $U$ tasuje się i dzieli na $k$ równych części
* Dla każdego podzbioru $U_i$
	* uczy się model na zbiorze $U-U_i$
	* oblicza się średnią stratę na zbiorze $U_i$
* Wylicza się finalną stratę jako średnią stratę ze wszystkich modeli
* Trenuje się finalny model na całym zbiorze $U$