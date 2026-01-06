# Naiwny klasyfikator bayesowski

$$ P(A|B) = \frac{P(A) \cdot P(B|A)}{P(B)} $$
$$ P(d|x) = P(c=d|a_1=v_1, a_2=v_2, \ldots a_n=v_n) $$

$$ P(d|x) = \frac{P(c=d) \cdot P(a_1=v_1, \ldots, a_n=v_n | c=d)}{P(a_1=v_1, \ldots, a_n=v_n)}$$

$$
P(d|x) \simeq
\frac
{P(c=d) \cdot \prod_{i=1}^n P(a_i=v_i | c=d)}
{\sum_{d' \in C} P(c=d') \prod_{i=1}^n P(a_i=v_i | c=d')}
$$

* $A$ - klasa
* $B$ - wartości atrybutów przykładu
* Jeden z najczęściej używanych algorytmów uczenia maszynowego
	* to jest wystarczające do klasyfikacji
	* porównujemy prawdopodobieństwa wszystkich klas
	* wybieramy klasę najbardziej prawdopodobną
* $P(c=d)$ - prawdopodobieństwo a priori
	* trywialne do estymacji ze zbioru uczącego
	* jak często występuje w czasie trenującym
	* $|T_{c=d}|/|T|$
* Prawdopodobieństwa z koniunkcjami
	* nie jest oczywiste do estymacji
	* wiele kombinacji może w ogóle nie wystąpić w zbiorze trenującym
	* zastępowane iloczynem prawdopodobieństw - zakładamy niezależność
	* warunkowa niezależność atrybutów względem klas - naiwne, prawie nigdy nie jest spełnione
* $P(a_i=v_i | c=d)$ daje się estymować na zbiorze uczącym
	* $|T_{a_i=v_i, c=d}|/|T_{c=d}|$
	* może się zdarzyć, że wartość atrybutu nie wystąpi w danej klasie - wyzerowałoby iloczyn
	* stosuje się wygładzanie prawdopodobieństw
* Niezależność bezwarunkowa to jescze mocniejsze założenia niż niezależność warunkowa
	* nie chcemy przyjmować kolejnego nieprawdziwego założenia, które jest jeszcze mocniejsze
	* zamiast mianownika wprowadzamy taką wielkość, która wymusi, żeby prawdopodobieństwa sumowały się do 1
	* mianownik to stała normalizująca
* Jedna pętla przez dane
* W drzewie pojedyncza ścieżka sprawdzi tylko kilka atrybutów
	* tutaj nawet jeśli atrybutów jest bardzo dużo, to każdy coś wnosi do predykcji
	* NKB może działać lepiej niż drzewo jeśli granice między klasami są nieostre

## Wygładzanie
* Wygładzanie przez przypisanie stałej wartości dodatniej $\epsilon$ jeśli zbiór $T_{a_i=v_i, c=d}$ jest pusty
* Wygładzanie Laplace'a
	* $|A_i|$ - liczba wartości atrybutu $a_i$
	* interpretacja - dokładamy $l$ fikcyjnych przykładów, gdzie wszystkie wartości atrybutu $a_i$ są jednakowo prawdopodobne
	* $l$ - liczba typu $1$, $2$, ...
	* $\frac{|T_{a_i=v_i, c=d}| + l}{|T_{c=d}| + l \cdot |A_i|}$

## Implementacja
* Prowadzi się obliczenia na logarytmach prawdopodobieństw
* Zamiast iloczynu liczy się sumę logarytmów
* Bardziej odporne na błędy numeryczne
* Można przeliczyć z powrotem na prawdopodobieństwa przez funkcję wykładniczą

## Atrybuty ciągłe
* Można zastąpić $P(a_i=v_i|c=d)$ przez $g_{d,i}(v_i)$ - funkcję gęstości atrybutu $a_i$ w klasie $d$
	* zakładamy rozkład normalny z parametrami estymowanymi jako

$$ m_{T_{c=d}}(a_i) = \frac{1}{|T_{c=d}|} \sum_{x \in T_{c=d}} a_i(x) $$

$$ s_{T_{c=d}} (a_i) = \sqrt{\frac{1}{|T_{c=d}|-1} \sum_{c \in T_{c=d}} (a_i(x) - m_{T_{c=d}}(a_i))^2} $$
* Dyskretyzacja
	* często lepsze
	* bardziej pracochłonne
	* podział wartości atrybutu ciągłego na przedziały

## Obsługa brakujących wartości
* Tworzenie modelu
	* pomijanie brakujących wartości przy estymacji prawdopodobieństw $P(a_i=v_i|c=d)$
* Predykcja
	* pomijanie prawdopodobieństw $P(a_i=v_i|c=d)$ jeśli wartość $a_i$ nie jest znana dla klasyfikowanego przykładu
* Przy mnożeniu to zastąpienie przez $1$

## Właściwości naiwnego klasyfikatora bayesowskiego
* Prosty koncepcyjnie i obliczeniowo
* Często wykorzystywany w praktyce
	* klasyfikacja danych tekstowych
	* atrybuty - czy słowo ze słownika wystąpiło czy nie (tysiące atrybutów)
	* trudny do pobicia do tego typu zadań
* Odporny na nadmierne dopasowanie
	* wymiar VC liniowy względem liczby atrybutów
* Nie wymaga strojenia parametrów
* Naruszenie założenia o niezależności nie wyklucza wartości predykcyjnej
* Skuteczny jeśli
	* trzeba uwzględnić nieznaczny wpływ znacznej liczby atrybutów (np. klasyfikacja tekstu)
	* liczba przykładów jest stosunkowo mała w porównaniu z liczbą atrybutów
	* występują liczne brakujące wartości
