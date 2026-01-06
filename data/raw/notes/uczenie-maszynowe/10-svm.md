# SVM

## SVM z twardym marginesem
* Reprezentacja liniowo-progowa
* Funkcja liniowa $g(x) = w \cdot a(x)$ - hiperpłaszczyzna
	* dla uproszczenia zapisu przyjmujemy $a_{n+1}(x)=1$
* Predykcja $1$ jeśli $g(x) \ge0$, $0$ jeśli $g(x) < 0$
* Szuka liniowej granicy decyzyjnej między klasami
	* dąży do separacji z jak największym zapasem
* $\gamma_w(x) = \frac{c_-(x) w \cdot a(x)}{\|w_{1:n}\|}$
	* margines geometryczny
	* odległość od hiperpłaszczyzny ze znakiem
	* dodatni jeśli przykład klasyfikowany poprawnie
	* $c_-(x)$ - $1$ dla klasy $1$, $-1$ dla klasy $0$
* $\hat{\gamma}_w(x) = c_-(x) w \cdot a(x)$ 
	* margines funkcyjny
	* nieznormalizowany
* $\gamma(T) = \min_{x \in T} \gamma_w(x)$
	* dążymy do maksymalizacji
	* dla poprawnie klasyfikowanych jest dodatni - chcemy jak największy zapas
	* dla niepoprawnie klasyfikowanych jest ujemny - chcemy jak najmniejszego błędu
* Mnożenie $w$ przez stałą nie zmieni położenia granicy decyzyjnej, ani jej orientacji
	* porównujemy iloczyn skalarny z zerem
	* żeby pozbyć się niejednoznaczności  wprowadzamy postulat $\hat{\gamma}(T) = 1$
	* z tym założeniem maksymalizacja $\gamma_w(T)$ to minimalizacja $\frac{1}{2}\|w\|^2$
* Minimalizacja $\frac{1}{2}\|w\|^2$ przy ograniczeniu
	* $(\forall x \in T) c_-(x) w \cdot a(x) \ge 1$
	* niemożliwe do spełnienia jeśli klasy nie są liniowo separowalne
	* to jest równoważne z postulatem $\hat{\gamma}(T) = 1$
* To wszystko przy założeniu że istnieje liniowa granica decyzyjna między klasami
	* SVM z twardym marginesem (hard margin)
* $(\forall x \in T) c_-(x) w \cdot a(x) \ge 1$
	* dla najbliższych punktów do granicy wartość jest dokładnie równa 1
	* będą co najmniej 2 (po 1 z każdej strony) - wektory nośne/podpierające
	* one determinują przebieg granicy

## SVM z miękkim marginesem
* Zbiór trenujące niekoniecznie liniowo separowalny
	* granica decyzyjna nie musi separować wszystkich przykładów
* Minimalizacja
	* $\frac{1}{2} \|w_{1:n}\|^2 + \mathcal{C} \cdot \sum_{x \in T} \xi_x$
* Przy ograniczeniach 
	* $(\forall x \in T) c_-(x) w \cdot a(x) \ge 1 - \xi_x$
	* $\xi_x$ - zmienna luzująca (slack variable)
	* $(\forall x \in T) \xi_x \ge 0$
* Margines wyznaczany przez przykłady o $\xi_x = 0$
* Są przykłady poprawnie klasyfikowane o $\xi_x > 0$
* Są przykłady niepoprawnie klasyfikowane o $\xi_x > 1$
* Jako wektory podpierające traktujemy te o $c_-(x)w \cdot a(x) \le 1$

### Co daje parametr $\mathcal{C}$
* Wysoka wartość $\mathcal{C}$
	* niechętne luzowanie
	* wąski margines
	* dążenie do liniowej separacji za wszelką cenę
	* większa podatność na nadmierne dopasowanie
	* wrażliwe na pojedyncze przykłady trudne do separacji
* Mała wartość $\mathcal{C}$
	* ignorowanie niektórych przykładów, żeby dla wielu przykładów uzyskać szeroki margines
* Warto dostroić
	* nie bardzo da się polegać na wartości domyślnej ($1$)

## SVM z funkcjami jądrowymi
* To co jest stosowane w praktyce
* Mnożniki Lagrange'a
* Dualne zadanie optymalizacji
	* wynikiem jest tyle współczynników ile jest przykładów
* W nowej postaci używa się iloczynów skalarnych par przykładów trenujących
	* to umożliwa zastosowanie bardziej efektywnego algorytmu optymalizacji
	* iloczyn skalarny można zastąpić funkcją jądrową
	* funkcja, która jest iloczynem skalarnym od jakichś innych atrybutów
	* niejawny sposób na przekształcenie przykładów do innej przestrzeni atrybutów
	* nowe atrybuty zależą nieliniowo od pierwotnych
	* algorytm zdobywa większą zdolność do separacji klas

## SVR
* SVM do regresji
* Minimalizacja kwadratu normy wektora parametrów
	* dla ograniczenia ryzyka nadmiernego dopasowania
* Ograniczenia wymuszające dokładnośc predykcji
* Szczegóły poza zakresem wykładu

## Podsumowanie
* Bardzo powszechnie używany algorytm
	* trudniejszy do użycia
	* wrażliwy na wybór parametrów, wybór funkcji jądrowych
	* konkurencyjny do lasu losowego
	* odporny na nadmierne dopasowanie nawet przy dużej liczbie atrybutów
	* możliwość reprezentowania nieliniowych zależności
* Wymaga starannego doboru parametrów
* Brak możliwości prostej interpretacji modelu
* Skalowanie Platta
	* mechanizm przewidywania prawdopodobieństw klas
	* nakładka na model
