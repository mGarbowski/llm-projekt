# Uczenie się przestrzeni wersji

## Kompleks
* Rozszerzenie koniunkcji boolowskich
* Atrybuty dyskretne (niekoniecznie binarne)
* Kompleks - historyczna nazwa (rozszerzona koniunkcja boolowska)
* $\langle v_1, v_2 \vee v_3, ? \rangle \equiv a_1 = v_1 \wedge a_2 \in \{v_2, v_3\}$
	* atrybut 1 ma wartość $v_1$
	* atrybut 2 ma wartość $v_2$ lub $v_3$
	* atrybut 3 ma dowolną wartość
* Określa warunek (spełniony/niespełniony, klasa 0/1)
	* warunki - selektory (pojedynczy, dysjunkcyjny, uniwersalny, pusty)
	* kolejne selektory dotyczą kolejnych atrybutów
* $\langle v_1, \varnothing, ? \rangle \equiv \langle \varnothing \rangle$
	* warunek nigdy nie spełniony
	* 0 logiczne
	* kompleks pusty
* $\langle ?, ?, ? \rangle \equiv \langle ? \rangle$
	* warunek zawsze spełniony
	* 1 logiczne
	* kompleks uniwersalny
* Kompleks jako model
	* $h(x)=1$ wtedy i tylko wtedy, gdy kompleks reprezenetujący $h$ jest *spełniony* dla przykładu $x$
	* kompleks *pokrywa* $x$

## Porównywanie modeli ze względu na ogólność
Model $h_1$ jest bardziej ogólny niż $h_2$ ($h_1 \succ h_2$) jeśli

$$\{x \in X | \quad h_2(x)=1 \} \subset \{ x\in X | \quad h_1(x) =1\}$$

* Relacja częściowego porządku
	* niektóre pary modeli nie są porównywalne
* Definicja odwołuje się do relacji zawierania podzbiorów dziedziny
	* dla przestrzeni modeli o ustalonej reprezentacji porównywanie jest możliwe bez ich jawnego wyznaczania

### Przykład
* Model - prostokąt
* $h_1 \succ h_2$ jeśli prostokąt $h_2$ jes zawarty w prostokącie $h_1$
* Modele nie są porównywalne jeśli żaden nie jest zawarty w drugim

### Przykład
* Model - koniunkcja boolowska
* $h_1 \succ h_2$ jeśli zbiór literałów koniunkcji reprezentujących $h_1$ jest zawarty w zbiorze literałów koniunkcji reprezentującej $h_2$
* Jeśli zbiór literałów jednego nie jest zawarty w drugim to nie są porównywalne

### Przykład
* Kompleksy
* $X$ - zbiór figur geometrycznych o atrybutach rozmiar, kolor, kształt
	* rozmiar: mały, średni, duży
	* kolor: czerwony, zielony, niebieski
	* kształt: koło, kwadrat, trójkąt
* $\langle ma \vee śr, ?, kw \rangle \succ \langle ma, cz, kw \rangle$
* $\langle ma \vee śr, ?, kw \rangle$ i $\langle ma, ?, ? \rangle$ nieporównywalne
* W ogólności $h_1 \succ h_2$ dla $h_1 = \langle s_1', s_2',  \ldots s_n' \rangle$,  $h_2 = \langle s_1'', s_2'',  \ldots s_n'' \rangle$ jeśli
	* $\forall i \quad V_{s_i''} \subseteq V_{s_i'}$
	* $\exists i \quad V_{s_i''} \subsetneq V_{s_i'}$

## Uczenie się przestrzeni wersji
* Relacja większej ogólności może prowadzić nas w procesie uczenia się zgodnie z porządkiem
	* w stornę bardziej ogólnych modeli lub bardziej szczegółowych modeli
* Przestrzeń wersji $VS$ - modele idealnie pasujące do danych trenujących
	* zależna od przestrzeni modeli, zbioru trenującego i pojęcia
* Korzystając z relacji mniejszej/większej ogólności, możemy trzymać tylko reprezentantów przestrzeni wersji, którzy pozwoliliby odtworzyć całą przestrzeń
	* najbardziej ogólne i najbardziej szczegółowe modele
* Dwie skrajne strony $VS$
	* $G$ - general
	* $S$ - specific
	* $G = \{h \in \mathbb{H} | \quad \neg(\exists h' \in VS) \quad h' \succ h \}$
	* $S = \{h \in \mathbb{H} | \quad \neg(\exists h' \in VS) \quad h' \prec h \}$
* $h \in G \vee (\exists h' \in G) \quad h \prec h'$
	* skrótowo $h \preceq G$
* $h \in S \vee (\exists h' \in S) \quad h \succ h'$
	* skrótowo $h \succeq S$
* Wszystkie modele przestrzeni wersji mieszczą się między jakimś modelem z $G$, a jakimś modelem z $S$ lub należą do $G$ albo $S$
* Nie ma modeli, które byłyby nieporównywalne z żadnym z modeli z $G$ i $S$
* $G$ i $S$ wyznaczają całą przestrzeń wersji
	* jeśli algorytm wyznacza $VS$ to wystarczy że znajdzie $G$ i $S$

## Algorytm eliminacji kandydatów (CAE)
* Znajduje przestrzeń wersji
* Dobry tylko dla ubogich modeli
	* wartość dydaktyczna
* Na początku, przed przejrzeniem zbioru danych trenujących - cała przestrzeń modeli to przestrzeń wersji
	* nie ma jeszcze żadnego elementu który przeszkadza
	* np. dla koniunkcji boolowskich G - stałe 1, S - stałe 0
	* dla kompleksów G - kompleks uniwersalny, S - kompleks pusty
* Pojawia się przykład klasy 1
	* trzeba zmienić S żeby dopasować się do danych
	* zastępujemy szczegółowe bardziej ogólnymi
* Pojawia się przykład klasy 0
	* trzeba zmienić G żeby dopasować się do danych
	* zastępujemy ogólne, bardziej szczegółowymi
* Zaciska się przestrzeń z obu stron
* Modele, które zostaną na końcu - przestrzeń wersji - modele pasujące do danych

### Działanie
* Inicjalizacja
	* $G :=$ zbiór modeli maksymalnie ogólnych w przestrzeni modeli
	* $S :=$ zbiór modeli maksymalnie szczegółowych w przestrzeni modeli
* Dla każdego $x \in T$
* Jeśli $c(x)=1$
	* $G := G - \{h\in G | h(x)=0 \}$ - wyrzucamy z G te modele które nie pasują (nie można bardziej uogólnić)
	* dla każdego $h \in \{h' \in S | h'(x)=0 \}$
		* $S := S - \{h\} \cup generalizacje(h,x,G)$ - nie bardziej ogólne niż modele z G
	* $S := S - \{ h \in S | (\exists h' \in S) h' \prec h\}$ - weryfikacja że spełniona jest własność zbioru S
* Jeśli $c(x) = 0$
	* $S := S - \{h\in S | h(x)=1 \}$ 
	* dla każdego $h \in \{h' \in G | h'(x)=1 \}$
		* $G := G - \{ h \} \cup specjalizacje(h,x,S)$
	* $G := G - \{ h \in G | (\exists h' \in G) h' \succ h\}$
* Zwróć $(G,S)$

### Generalizacja
* $generalizacja(h, x, G)$
* $h$ - model który mamy zgeneralizować
* $x$ - przykład, który nie pasuje
* $G$ - ograniczenie jak bardzo generalny może być model
* Wynik - zbiór maksymalnie szczegółowych modeli $h'$ spełniających warunki
	* maksymalnie szczegółowych bo chcemy krok minimalny, wystarczający
	* $h' \succ h$
	* $h'(x)=1$ (problemem jest że $h(x)=0$)
	* $h' \preceq G \equiv h' \in G \vee (\exists h'' \in G) h' \prec h''$ (nie może być bardziej ogólny niż modele z $G$)
* Wynikiem generalizacje są modele wystarczająco ogólne, żeby pokryć $x$, ale poza tym maksymalnie szczegółowe i niewykraczające poza ograniczenia $G$
	* minimalna generalizacja
* Realizacja jest zależna od reprezentacji modeli

### Specjalizacja
* $specjalizacja(h, x, S)$
* Wynik - zbiór maksymlanie ogólnych modeli $h'$ spełniających warunki
	* $h' \prec h$
	* $h'(x)=0$
	* $h' \succeq S$
* Wynikiem są modele wystarczająco szczegółowe żeby wykluczyć pokrywanie $x$, ale poza tym maksymalnie ogólne i niewykraczające poza ograniczenie $S$

### Przykład
* Generalizacja prostokąta
	* jednoznaczna
	* trzeba rozciągnąć prostokąt tak, żeby zawierał nowy przykład
	* konieczna weryfikacja, czy zawiera się w prostokącie reprezentującym jakiś model z $G$
* Specjalizacja prostokąta
	* minimalne zawężenie prostokąta reprezentującego $h$ wystarczające do wykluczenia przykładu $x$
	* wynikiem jest zbiór wszystkich modeli reprezentowanych przez prostokąty uzyskane przez minimalne przesunięcie jednego z boków do wewnątrz
	* nie jest jednoznaczne, można wybrać dowolny bok to zawężenia
	* dla każdego nowego prostokąta trzeba sprawdzić czy zawiera jakiś prostokąt z $S$
* Model prostokątów ma charakter koniunkcyjny
	* 4 warunki
	* generalizacja daje 1 nowy model
	* specjalizacja może dawać więcej
* Generalizacja koniunkcji boolowskich
	* usunięcie tych i tylko tych literałów, które nie są spełnione dla przykładu $x$
	* konieczna weryfikacja czy zbiór literałów zawiera się w zbiorze literałów jakiejś koniunkcji reprezentującej model z $G$
* Specjalizacja koniunkcji boolowskich
	* dodanie jednego literału niespełnionego dla przykładu $x$
	* wynikiem jest zbiór wszystkich koniunkcji uzyskanych przez dodanie literału
	* $a_i$ jeśli $a_i(x) = 0$
	* $\neg a_i$ jeśli $a_i(x)=1$
	* konieczna weryfikacja czy zbiór literałów zawiera zbiór literałów jakiejś koniunkcji z $S$
	* nie jest jednoznaczne który literał dodać
* Generalizacja kompleksu
	* minimalne wystarczające rozszerzenie zbiorów wartości dozwolonych selektorów
	* do każdego zbioru selektora dającego $0$ dokładamy wartość atrybutu przykładu
	* $V_{s_i} := V_{s_i} \cup \{ a_i(x)\}$
	* musi być spełniony warunek $h' \preceq G$ albo generalizacja da pusty wynik
* Specjalizacja kompleksu
	* minimalne wystarczające zawężenie zbioru wartości dozwolonych jednego selektora
	* wynikiem jest zbiór wszystkich modeli różniących się od $h$ wyłącznie jednym selektorem $s_i'$
	* $V_{s_i'} = V_{s_i} - \{ a_i(x) \}$
	* tylko jeśli $h' \succ S$

### Przykład

| x   | $a_1$ | $a_2$ | $a_3$ | klasa |
| --- | ----- | ----- | ----- | ----- |
| 1   | du    | cze   | ko    | 1     |
| 2   | ma    | cze   | kw    | 0     |
| 3   | ma    | cze   | ko    | 1     |
| 4   | du    | nie   | ko    | 0     |

* CAE dla figur geometrycznych
* Na początku
	* $G = \{ \langle ? \rangle \}$
	* $S = \{ \langle \varnothing \rangle \}$
* $x=1$
	* $G = \{ \langle ? \rangle \}$
	* $S = \{ \langle du, cze, ko \rangle \}$
* $x=2$
	* Nie można wykluczyć koloru czerwonego bo model będzie mniej ogólny niż model z $S$
	* $G = \{ \langle sr \vee du, ?, ? \rangle,\langle ?, ?, ko \vee tr \rangle\}$
	* $S = \{ \langle du, cze, ko \rangle \}$
* $x=3$
	* $G$ - pierwszy daje $0$, trzeba usunąć
	* $S$ - trzeba uogólnić
	* $G = \{ \langle ?, ?, ko \vee tr \rangle\}$
	* $S = \{ \langle du \vee ma, cze, ko \rangle \}$
* $x=4$
	* w $G$ jedna możliwość specjalizacji, która jest bardziej ogólna niż $S$
	* $G = \{ \langle ?, cze \vee zie, ko \vee tr \rangle\}$
	* $S = \{ \langle du \vee ma, cze, ko \rangle \}$
* Przestrzeń wersji między $G$ i $S$
* Wybieramy kierunek (z góry albo z dołu)
	* np. wykonujemy wszystkie dopuszczone specjalizacje $G$

### Zastosowanie przestrzeni wersji do predykcji
* Algorytm nie ma obciążanie, nie preferuje żadnego modelu o ile pasuje do danych
* Na końcu można wprowadzić obciążenie przez wybór jednego modelu z $VS$
	* najbardziej ogólny
	* najbardziej szczegółowy
	* *ze środka*
	* wymagający sprawdzenia najmniejszej liczby atrybutów
* Wiele modeli może głosować nad predykcją
	* model komitetowy może dać coś nie do osiągnięcia przez żaden pojedynczy kompleks
* Możliwość aktywnego uczenia się
	* chcemy jak najmniej porównań
	* trzeba zawęzić przestrzeń modeli
	* uczeń pyta o przykład
	* najlepiej podać taki, które przez połowę modeli będzie, a przez połowę nie będzie pokrywany
	* poznanie klasy przykładu zmniejszy przestrzeń wersji o połowę

## Podsumowanie
* Sformułowanie uczenia jako przeszukiwania
	* kamień milowy w uczeniu maszynowym
* Dwukierunkowe przeszukiwanie przestrzeni modeli
	* od maksymalnie ogólnych do maksymalnie szczegółowych i na odwrót
	* bez pomijania żadnego modelu spójnego
* Przyrostowy tryb uczenia się z użyciem jednego przykładu trenującego na raz
* Zbyt duża złożoność dla bogatych przestrzeni modeli
	* eksplozja zbiorów $G$ i $S$
* Brak modeli spójnych dla ubogich przestrzeni modeli
	* pusty wynik
* Konieczne dostosowanie do wymogów praktycznych
	* zawężenie zakresu przeszukiwania
	* tolerowanie niespójności
