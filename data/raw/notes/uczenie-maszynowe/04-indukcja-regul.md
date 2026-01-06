# Indukcja reguł

## Reguły
* Rozszerzenie kompleksów
	* zamiast ubogiej reprezentacji koniunkcyjnej bogata reprezentacja DNF
	* alternatywa koniunkcji
* Reguła $k \rightarrow d$
	* część warunkowa - kompleks $k$
	* część decyzyjna - klasa $d$
* Pokrywanie
	* reguła $k \rightarrow d$ pokrywa przykład $x$ gdy jej część warunkowa pokrywa $x$
	* $k \rhd x$
* Zbiór przykładów pokrywanych
	* dla dowolnego $D \subseteq X$ i kompleksu $k$ i zbioru kompleksów $K$
	* $D_k = \{ x \in D | k \rhd x \}$
	* $D_K = \{ x \in D | (\exists k \in K) k \rhd x \}$

## Zbiór reguł
* Model - zbiór reguł, który może zawierać wiele reguł dla tej samej klasy
	* koniunkcyjne części warunkowe traktuje się jak połączone alternatywą
* Nieuporządkowany
	* każda reguła stosowana niezależnie od pozostałych
	* wymaga rozstrzygnięcia sposób wyznaczania przewidywanej klasy dl aprzykładów niepokrywanych przez żadną regułę lub pokrytych przez więcej niż jedną regułę o różnych klasach
	* to wiele reguł dla tej samej klasy działa jak alternatywa
* Uporządkowany
	* każda reguła stosowana tylko dla przykładów niepokrytych przez wcześniejsze reguły
	* ostatnia reguła określa klasę domyślną
	* brak możliwości konfliktu reguł o różnych klasach
	* działanie jak `if ... else if ... else ...`
* Są algorytmy, które mogą być stosowane dla obu wariantów
	* decyzję trzeba podjąć na początku
	* proces tworzenia reguł powinien uwzględniać sposób ich użycia
* Wymiar $VC$ równy liczbie wszystkich możliwych różnych wektorów wartości atrybutów dla atrybutów dyskretnych
	* ryzyko nadmiernego dopasowania

## Schemat sekwencyjnego pokrywania

```
Reguły := zbiór pusty
Reszta := zbiór trenujący (T) // zbiór przykładów nie pokrytych do tej pory

dopóki rezta != zbiór pusty
	k := kompleks(Reszta, T)  // nie każdy algorytm używa obu
	d := klasa(k, Reszta, T) // klasa większościowa, dla jakich przykładów?
	Reguły := Reguły unia {k -> d}
	Reszta := Reszta - {przykłady z reszty pokryte przez k}
```

* Wysokopoziomowy schemat algorytmu
	* różne konkretyzacje dla `kompleks` i `klasa`
* `kompleks` - znalezienie kompleksu pokrywającego możliwie wiele przykładów z Reszty z możliwie dużą dokładnością
	* jednolita lub wyraźnie dominująca klasa
* `klasa` - wybór klasy dla przykładów pokrywanych przez znaleziony kompleks
	* klasa dominująca
* Znajdowanie kompleksu zwykle przez specjalizację
	* przeszukiwanie od maksymalnie ogólnych do maksymalnie szczegółowych
* Generuje reguły pokrywające jakąś część danych
* Kompleks powinien być możliwie ogólny i możliwie jednoznaczy co do klasy
* Chcemy żeby kolejne reguły pokrywały nowe przykłady
* Dla uporządkowanych reguł chcemy żeby klasa dominowała w niepokrytych wczesniej przykładach

### Specjalizacja kompleksów
* Podobna operacja do wyznaczania przestrzeni wersji w algorytmie CAE
	* wprowadzone obciążenie - preferencja dla maksymalnie ogólnych kompleksów
	* wyznaczane tylko ograniczenie ogólne (zbiór $G$)
	* poszukiwane maksymalnie ogólne kompleksy pokrywające wyłącznie lub w większości przykłady jednej klasy
	* eliminowanie pokrywania przykładów innych klas  przez stosowanie operacji specjalizacji
* Zwykle zbiór $G$ przycinany do ograniczonego podzbioru najlepszych kompleksów
	* w celu ograniczenia złożoności
* Najlepszy znaleziony kompleks wykorzystywany do utworzenia reguły
* Potrzebna funkcja oceny jakości
* Różne szczegółowe algorytmy

## Specjalizacja AQ (uporządkowany zbiór reguł)
* $G := \{ \langle ? \rangle \}$
* wybierz $x_s \in R$ (ziarno)
* $R^{(1)} := R_{c=c(x_s)}$ (zbiór przykładów o tej samej klasie co $x_s$)
* $R^{(0)} := R_{c \neq c(x_s)}$ (zbiór przykładów o innej klasie niż $x_s$)
* dopóki $R^{(0)}_G \neq \varnothing$ (chcemy wykluczyć ich pokrywanie)
	* wybierz $x_n \in R^{(0)}_G$ (ziarno negatywne)
	* dla wszystkich $k$ z $G$, które pokrywają $x_n$
		* $G := G - \{k\} \cup specjalizacja(k, x_n, x_s)$
	* $G := G - \{k \in G| (\exists k' \in G) k\ \succ k \}$ (tylko maksymalnie ogólne)
	* $G :=$ $m$ najlepszych kompleksów z $G$ według miary jakości $v_{R^{(0)}, R^{(1)}}(k)$ 
* zwróc najlepszy kompleks z $G$ według miary jakości $v$

* Ocena jakości kompleksów $v$
	* dobre są te kompleksy, które pokrywają dużo przykładów z klasy, którą chcemy pokrywać i niepokrywają tych, których nie chcemy
	* np. suma liczby przykładów pokrytych z $R^{(1)}$ i niepokrytych z $R^{(0)}$
* Specjalizacja - zbiór maksymalnie ogólnych kompleksów $k'$ takich że
	* $k' \prec k$ - mniej ogólne
	* $\neg(k' \rhd x_n)$ 
	* $k' \rhd x_s$ (zamiast warunku z $S$ jak w CAE)
* Uporządkowanie zbioru reguł
	* eliminacja pokrywania przykładów klas innych niż $c(x_s)$
	* wyłącznie w zbiorze $R$ - przykłady niepokryte przez wcześniejsze reguły
* Dla uporządkowanego zbioru danych algorytm musi zadbać o to, żeby reguła poprawnie klasyfikowała przykład pokrywany przez nią, a niepokrywany przez wcześniejsze reguły
* Decyzja o uporządkowaniu - czy reguła ma być dokładna na wszystkich przykładach, czy na tych niepokrytych przez wcześniejsze reguły
	* dla algorytmu z nieuporządkowanym zbiorem używalibyśmy $T$ - zbioru uczącego zamiast $R$

### Alternatywny zapis
* dopóki $R^{(0)}_G \neq \varnothing$ 
	* wybierz $x_n \in R^{(0)}_G$
	* $G' := dyskryminacja(x_n, x_s)$
	* $G := G \wedge G'$

* Dyksryminacja - zbiór maksymalnie ogólnych kompleksów $k'$ takich, że
	* $\neg(k' \rhd x_n)$
	* $k' \rhd x_s$
	* jak specjalizowanie kompleksu ogólnego żeby pokrywał $x_s$, a nie $x_n$
* Koniunkcja zbiorów kompleksów 
	* $G \wedge G' = \{ k \wedge k' | k \in G, k' \in G' \}$

### Przykład

| x   | outlook  | temperature | humidity | wind   | play |
| --- | -------- | ----------- | -------- | ------ | ---- |
| 1   | sunny    | hot         | high     | normal | no   |
| 2   | sunny    | hot         | high     | high   | no   |
| 3   | overcast | hot         | high     | normal | yes  |
| 4   | rainy    | mild        | high     | normal | yes  |
| 5   | rainy    | cold        | normal   | normal | yes  |
| 6   | rainy    | cold        | normal   | high   | no   |
| 7   | overcast | cold        | normal   | high   | yes  |
| 8   | sunny    | mild        | high     | normal | no   |
| 9   | sunny    | cold        | normal   | normal | yes  |
| 10  | rainy    | mild        | normal   | normal | yes  |
| 11  | sunny    | mild        | normal   | high   | yes  |
| 12  | overcast | mild        | high     | high   | yes  |
| 13  | overcast | hot         | normal   | normal | yes  |
| 14  | rainy    | mild        | high     | high   | no   |

* $x_s = x_1$ (shhn|n)
* `G = {<?>}`
* R = T
* R1 - przykłady klasy no
* R0 - przykłady klasy yes

* $x_n = x_3$ (ohhn|y) - przykład klasy yes
* jedyny kompleks w G pokrywa $x_n$ a ma nie pokrywać - specjalizacja
* `G = {<s|r, ?, ?, ?>}`
* można zmienić warunek tylko dla pierwszego atrybutu bo reszta jest jednakowa
* tyle wyników specjalizaji ile różniących się atrybutów
* $R^0_G = \{4, 5, 9, 10, 11\}$

* $x_n = x_4$ (rmhn|y)
* `G = {<s, ?, ?, ?>, <s|r, h|c, ?, ?>}`
* $R^0_G = \{5, 9, 10, 11\}$

* $x_n = x_5$ (rcnn|y)
* pokrywany przez drugi kompleks z $G$, specjalizacja
* pierwszego kompleksu nie ruszamy bo nie pokrywa $x_n$

 ```
G = {
<s, ?, ?, ?>, 
<s, h|c, ?, ?>, - bardziej szczegółowy niż pierszy, usunięty w kroku czyszczącym
<s|r, h, ?, ?>, 
<s|r, h|c, h, ?>,
}
```

* Trzeba ustalić wartość $m$ - do ilu kompleksów ograniczamy $G$
	* i kryterium jakości
### Przykład
* Dyskryminacja przy alternatywnym zapisie
* $dyskryminacja(x_s=x_1, x_n=x_5)$
	* $x_1$ (shhn|n)
	* $x_5$ (rcnn|y)
* Na początku `G = {<s, ?, ?, ?>, <s|r, h|c, ?, ?>}`
* Wyznaczamy `G' = {<s|o, ?, ?, ?>, <?, h|m, ?, ?>, <?, ?, h, ?>}`

```
G' & G = {
<s, ?, ?, ?> 1 z 1
<s, h|c, ?, ?> 1 z 2 bardziej szczegółowy niż 1
<s, h|m, ?, ?> 2 z 1 bardziej szczegółowy niż 1
<s|r, h, ?, ?> 2 z 2
<s, ?, h, ?> 3 z 1 bardziej szczegółowy niż 1
<s|r, h|c, h, ?> 3 z 2 
}
```

Po kroku czyszczącym wychodzi to samo co w poprzednim przykładzie

## Specjalizacja CN2
* Clark-Niblett
* Nie używa konkretnych przykładów jako ziaren
* Każdy kompleks specjalizowany na wszystkie możliwe sposoby modyfikujące jeden selektor
	* jako nowe zbiory wartości dozwolonych brane pod uwagę wszystkie podzbiory obecnego zbioru wartości dozwolonych selektora
* Kompleksy nie muszą być dokładne
* Ocena jakości na podstawie rozkładu klas w zbiorze $R_k$
	* premiowana dominacja jednej klasy
* Przechowywany i aktualizowany najlepszy dotychczas statystycznie istotny kompleks
	* testy statystycznej istotności między pokryciem / niepokryciem przez kompleks a klasą przykładu
	* np. test $\chi^2$, test $G$
	* statystyczna istotność wymaga wyraźne różnego rozkładu klas wśród przykładów pokrywanych i niepokrywanych oraz wystarczająco dużej liczby przykładów pokrywanych
* Do dalszej specjalizacji przechodzi $m$ najlepszych kompleksów
* Specjalizacja do oporu
	* tak długo jak da się specjalizować - po drodze jest filtrowanie
* Zwraca się wynik najlepszej jakości

### Przykład
* Specjalizacja kompleksu `<ma|sr, ?, ko|kw>` (figury geometryczne)
* `<sr, ?, ko|kw>`
* `<ma, ?, ko|kw>`
* `<ma|sr, cze|nie, ko|kw>`
* `<ma|sr, nie|zie, ko|kw>`
* `<ma|sr, cze|zie, ko|kw>`
* `<ma|sr, cze, ko|kw>`
* `<ma|sr, nie, ko|kw>`
* `<ma|sr, zie, ko|kw>`
* `<ma|sr, ?, ko>`
* `<ma|sr, ?, kw>`

## Specjalizacja FOIL
* First Order Inductive Logic
* Najbardziej praktyczny z omawianych do tej pory
	* raczej historyczne podejście do algorytmów
	* bardziej rozbudowane algorytmy oparte na tym pomyśle - IREP, RIPPER
* Algorytm do indukcji reguł w rachunku predykatów, ale tutaj dostosowany do zwykłych (zdaniowych) reguł
	* przycięty algorytm jest użyteczny do prostszego zadania
* Specjalizacja bez użycia wybranych pojedynczych przykładów (ziaren)
* Każdy kompleks specjalizowany na wszystkie możliwe sposoby modyfikujące dokładnie jeden selektor uniwersalny
	* jako nowe zbiory wartości dozwolonych brane pod uwagę wszystkie podzbiory zbioru wartości odpowiedniego atrybutu
* Ocena jakości na podstawie rozkładu klas w zbiorze $R_k$
	* premiowana dominacja jednej klasy
	* z uwzględnieniem pokrycia - premiowane pokrywanie wielu przykładów
* W każdje iteracji pozostawiany jeden najlepszy kompleks
* Koniec specjalizacji gdy nie poprawia się jakość
* Nie ma testów istotności jak w CN2

### Przykład
* Specjalizacja kompleksu `<ma|sr, ?, ko|kw>`
	* bierzemy pod uwagę tylko drugi selektor - `?`
* `<ma|sr, cze|nie, ko|kw>`
* `<ma|sr, nie|zie, ko|kw>`
* `<ma|sr, cze|zie, ko|kw>`
* `<ma|sr, cze, ko|kw>`
* `<ma|sr, nie, ko|kw>`
* `<ma|sr, zie, ko|kw>`

## Ocena jakości kompleksów
* Poniżej tylko przykłady
	* zagadnienie jest rozbudowane, jest wiele możliwości
* Uproszczona notacja, charakterystyczna tylko dla algorytmu AQ
* Dla nieuporządkowanego zbioru reguł - ocena jakości na $T_k$
	* ta postać ma sens dla uporządkowanego zbioru reguł

### Pokrycie
$$ v_{R^{(1)}, R^{(0)}}(k) = |R^1_k| + |R^0 - R^0_k| $$

* Na podstawie liczby pokrywanych/niepokrywanych przykładów właściwej/niewłaściwej klasy
* Liczba poprawnie pokrytych i poprawnie niepokrytych

### Dokładność
$$ v_{R^{(1)}, R^{(0)}}(k) = \frac{|R^1_k| + 1}{|R^1_k \cup R^0_k| + |C|} $$

* Na podstawie ilorazu liczby pokrywanych przykładów właściwej i liczby wszystkich pokrywanych przykładów
* Kompensowana niemiarodajność kompleksu pokrywającego małą liczbę przykładów
* $+1$ - załóżmy że jest jeszcze jeden przykład
* $+|C|$ - tyle ile jest klas
* Dodajemy fikcyjne przykłady, takie w których wszystkie klasy są jednakowo prawdopodobne
* Wygładzanie prawdopodobieństwa
* Większa różnica jak jest mało przykładów, mniejsza jeśli jest wiele

### Dominacja klasy z uwzględnieniem pokrycia

$$ v_{R^{(1)}, R^{(0)}}(k) = |R^1_k| \log \frac{|R^1_k|}{|R^1_k \cup R^0_k|} $$

* Z algorytmu FOIL

## Przycinanie zbiorów reguł
* Motywacja
	* zbiór reguł dokładnie dopasowany do zbioru trenującego może być nadmiernie dopasowany
	* trudno określić odpowiednie kryterium stopu specjalizacji
* Operatory
	* generalizacja reguły - zamiana wybranego selektora na uniwersalny ($?$)
	* eliminacja reguły - usunięcie wybranej reguły ze zbioru reguł
* Kryteria
	* ocena wpływu zostosowania operatora przycinania na błąd rzeczywisty zbioru reguł
	* np. estymowany na oddzielnym zbiorze przykładów
	* patrzymy czy klasyfikacja się poprawi jeśli usunie się jakąś regułę
* W algorytmach IREP, RIPPER