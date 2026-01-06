# Indukcyjne uczenie się

## Definicja uczenia się
System uczący się - autonomiczna poprawa jakościa wykonywania zadania na podstawie zewnętrznej informacji trenującej

### Program uczący się
* Algorytm wykonywania zadania
	* niedoskonały, niepełny
* Algorytm uczenia się
	* dostarczający wiedzy / umiejętności uzupełniającej/doskonalącej algorytm wykonywania zadania
* Zaczynamy od szczątkowego zrozumienia problemu z lukami, które będzie wypełniał algorytm uczenia się
* Uczenie się nie musi startować z niczego, jest nałożona pewna ramowa struktura

### Informacja trenująca
* Przykłady etykietowane
	* uczenie się z nauczycielem (z nadzorem)
	* znane wejście, znane wyjście
	* algorytm ma przewidzieć wyjście na podstawie wejścia
* Odpowiedzi na zapytania
	* uczenie się z nauczycielem (z nadzorem)
	* program pyta o etykietę dla wybranego wejścia
	* aktywne uczenie się
* Przykłady nieetykietowane
	* uczenie bez nauczyciela (bez nadzoru)
* Nagrody / kary
	* uczenie się ze wzmocnieniem
	* nagrody i kary mogą być opóźnione
	* np. gra planszowa - po iluś ruchach zobaczymy konsekwencje ruchu

### Wynik uczenia się
* Wiedza
	* jakie coś jest
* Umiejętność
	* jak coś zrobić

Podział nie jest ostry

### Uogólnianie informacji trenującej
* Wnioskowanie indukcyjne
* Uogólnianie obserwacji
	* bywa zawodne

## Uporządkowanie pojęć
* Dziedzina $X$
	* zbiór tego o czym się wypowiadamy
	* może być bardzo precyzyjnie zdefiniowany
	* może być zdefiniowany luźno, nieprecyzyjnie
* Przykład / obserwacja / próbka $x \in X$
	* wektor atrybutów (cech)
* Atrybut $a: X \rightarrow A$
	* funkcja
	* np. wiek człowieka
	* dyskretne (kategoryczne)
		* nominalne $(=, \neq)$
		* porządkowe $(\lt, \gt, \le, \ge)$
	* ciągłe (numeryczne, o interpretacji liczbowej)

### Zadanie klasyfikacji
* Zadanie uczenia się pojęć (concept)
* Skończony zbiór klas $C$
* Pojęcie $c: X \rightarrow C$
	* wyróżniony atrybut dyskretny
	* w ogólności nieznany (inaczej nie trzeba było by się go uczyć)
	* znany dla oetykietowanych przykładów
* Zbiór danych $D \subset X$
	* dla $x \in D$ znane $c(x)$
* Zbiór trenujący $T \subseteq D$
	* wejście dla algorytmu uczenia się
	* na jego podstawie znajduje się **model**
* Model $h: X \rightarrow C$
	* przewiduje klasy
	* model jest wytworem algorytmu uczenia się
* Predykcja $h(x)$
	* zastosowanie modelu
	* konkretna klasa przewidziana przez model
* Przestrzeń modeli $\mathbb{H}$
	* jest właściwością algorytmu
	* może być nieskończona, skończona
* Klasa pojęć $\mathbb{C}$

#### Przykład 1
$X = \mathbb{R}^2$ - płaszczyzna
przykład - punkt na płaszczyźnie
atrybuty - współrzędne
Zbiór klas $C=\{0,1\}$ - czy punkt należy do obszaru na płaszczyźnie
Przykładowe pojęcie - prostokąt o bokach równoległych do osi
Uczenie się pojęcia - znalezienie parametrów prostokąta
znamy przykłady - punkty leżący w lub poza prostokątem

Model - może też być prostokątem, np. najciaśniej dopasowany do przykładów

#### Przykład 2
$X = \{0,1\}^n$ - wektor binarny
$c: X \rightarrow \{0,1\}$ - funkcje boolowskie
$h(x) = a_1(x) \wedge \neg a_3(x)$

### Zadanie regresji
* Przewiduje liczby
* Funkcja docelowa $f: X \rightarrow \mathbb{R}$
* Zbiór trenujący $T \subseteq D \subset X$
	* dla $x \in D$ znane $f(x)$
* Model $h \simeq f$

## Jakość modelu

### Błąd klasyfikacji na zbiorze
Do policzenia testując na zbiorze 

$$ e_{S,c}=\frac{|\{x\in S | h(x) \neq c(x)\}|}{|S|} $$

### Błąd rzeczywisty klasyfikacji
* Jak dobry jest model w ogóle
* Nie do policzenia dokładnie
* Jak prawdopodobna jest pomyłka modelu na dowolnym przykładzie z dziedziny
* Oparty na rozkładzie prawdopodobieństwa $\Omega$

 $$ e_{\Omega,c}(h) = P(h(x) \neq c(x) \quad | \quad x \in X, x \sim \Omega) $$

### Błąd średniokwadratowy na zbiorze
Jak dobry jest model regresji na zbiorze

$$ mse_{S,f}(h) = \frac{\sum_{x \in S}(f(x)-h(x))^2}{|S|} $$

### Błąd średniokwadratowy rzeczywisty
Oszacowanie jak dobry naprawdę jest model
$$ mse_{\Omega,f}(h) = \mathbb{E}[(f(x) - h(x))^2 | x \in X, x \sim \Omega] $$

## Obciążenie indukcyjne
Obciążenie indukcyjne (inductive bias) - przykłady na wejściu nie determinują tego jaki model można wybrać, algorytm uczenia ma swobodę do tego jaki algorytm wybierze, obciążenie to skłonność do wyboru jakiegoś algorytmu (np. w stronę prostszego modelu, modelu zajmującego mniej pamięci itd.). Może ograniczać wybór modeli lub narzucać preferencje.

* Właściwość algorytmu uczenia się
	* determinuje wybór $h$ na podstawie $T$
	* sposób uogólnienia przykładów trenujących
* Realizacja
	* obciążenie reprezentacji - zawężenie przestrzeni modeli dostępnej dla algorytmu
	* obciążenie preferencji - wprowadzenie kryteriów preferencji modeli (np. preferencja dla prostszych)

## Nadmierne dopasowanie (overfitting)
Model $h_1$ jest nadmiernie dopasowany do zbioru trenującego $T$, jeśli istnieje model $h_2$ taki, że $e_{T,c}(h_1) < e_{T,c}(h_2)$ (ma mniejszy błąd na zbiorze trenującym) i $e_{\Omega,c}(h_1) > e_{\Omega,c}(h_2)$ (ma większy błąd rzeczywisty).

* Model wydaje się lepszy, a naprawdę jest gorszy
* Zasadnicze wyzwanie przy tworzeniu modeli przez uczenie się
* Definicja nie jest zbyt wygodna
* Błąd rzeczywisty w ogólnym przypadku nie jest znany
* W rzeczywistości sygnałem, że model może być nadmiernie dopasowany jest mały błąd na zbiorze trenującym i większy na zbiorze testowym
	* ale nie wiemy tego na pewno, nie mamy drugiego modelu ani nie znamy błędu rzeczywistego
* Łatwiej o nadmierne dopasowanie jeśli mamy mniej danych
* Zapobieganie i kontrola
	* stosowanie algorytmów o mniejszym ryzyku nadmiernego dopasowania
	* wprowadzenie do algorytmu mechanizmów zmniejszających ryzyko nadmiernego dopasowania
	* staranna ocena jakości modeli

## Estymacja błędu rzeczywistego
* Substytutem dla błędu rzeczywistego może być błąd na konkretnym zbiorze $S$ (testowym)
* Żeby błąd na zbiorze był wiarygodnym estymatorem błędu rzeczywistego, zbiór $S$ powinien być
	* wystarczająco duży
	* wybrany z dziedziny niezależnie od $h$ (nie korzystamy z wiedzy o modelu)
	* wybrany z dziedziny zgodnie z rozkładem $\Omega$
* W praktyce
	* $S \subset D$
	* $T \subset D$
	* $D \subset X$ jest zbiorem przykładów o znanych klasach
	* $S \cap T = \varnothing$ - zbiór danych dzieli się na rozłączne podzbiory
* Uproszczone praktyczne kryterium ryzyka nadmiernego dopasowania
	* $e_{s,c}(h) \gg e_{T,c}(h)$
* $S$ i $T$ mogą też być niezależnie wylosowane ze zbioru danych
* Dysponujemy ograniczonym zbiorem danych $D$

### Estymacja przedziałowa błędu
* Estymacja przedziałowa - narzędzie statystyczne to estymowania błędu rzeczywistego
* Pozwala oszacować z jakiego przedziału jest błąd rzeczywisty na podstawie błędu na zbiorze $S$
* Zajrzeć do podręcznika od statystyki
* Przedział ufności
	* przedział eokół $e_{S,c}(h)$, który z prawdopodobieństwem $1-\delta$ zawiera $e_{\Omega,c}(h)$
	* $\delta$ - poziom ufności
* Przedział Walda
	* tylko jeśli błąd na zbiorze nie jest zbyt bliski $0$ ani $1$
* Przedział Wilsona
	* także jeśli błąd na zbiorze jest bliski 0 lub 1
* $u_\delta$ - współczynnik skalujący
	* dla $U \sim N(0,1)$: $P(|U| < u_\delta) = 1 - \delta$
* $\delta$ - prawdopodobieństwo że prawdziwy błąd jest w przedziale, często przyjmuje się $0.95$

#### Przedział Walda
$$ |e_{\Omega,c}(h) - e_{S,c}(h)| 
< u_\delta \sqrt{\dfrac{e_{S,c}(h)(1-e_{S,c}(h))}{|S|}} $$
