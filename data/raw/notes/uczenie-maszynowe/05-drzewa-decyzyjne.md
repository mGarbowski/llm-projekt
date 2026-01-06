# Drzewa decyzyjne
Reguły i drzewa decyzyjne - metody symboliczne - model zrozumiały dla człowieka

## Budowa drzewa
* Węzły
	* warunki odpowiadające selektorom
	* dzieli zbiór na podzbiory, gdzie warunek jest spełniony lub nie
	* warunki równości, przynależności do zbioru, nierówności
* Drzewa binarne i niebinarne
* W liściach estymacje prawdopodobieństwa dla każdej klasy
	* reprezentują decyzję o klasyfikacji

* Węzły
	* podziały (testy) na podstawie warunków dotyczących wartości atrybutów
	* analogiczna rola jak selektory w regułach
	* $t: X \rightarrow R_t$ - funkcja, podział nie musi być binarny
* Gałęzie
	* dla każdego wyniku podziału $t$ w węźle prowadzą z tego węzła do jego węzłów potomnych
* Liście
	* klasy
	* prawdopodobieństwa klas
* Proces predykcji
	* przykład $x$ przechodzi od korzenia do liścia
	* podziały w węzłach wyznaczają ścieżkę na podstawie atrybutów $x$
	* klasa z osiągniętego liścia


## Podziały dla atrybutów dyskretnych
* Wielowartościowe na podstawie wartości atrybutu
	* po 1 gałęzi dla każdej możliwej wartości atrybutu
	* $t(x) = a(x)$
* Binarne na podstawie równości
	* $1$ jeśli $a(x) = v$
	* $0$ w przeciwnym przypadku
* Wielowartościowe na podstawie podzbiorów wartości atrybutów
* Binarne na podstawie przynależności do zbioru

* Nie miesza się rodzajów podziału w ramach jednego modelu
* Model powinien obejmować każdą możliwą wartość atrybutu
* Dla każdego możliwego przykładu chcemy żeby model potrafił dać predykcję

## Podziały dla atrybutów ciągłych
* Binarne na podstawie nierówności
* Wielowartościowe na podstawie przedziałów wartości atrybutu
	* kubełkowanie

## Dekompozycja dziedziny
* Cały model jest podziałem dziedziny na regiony (prostokąty, hiperprostopadłościany)
	* dobrze widoczne dla 2 atrybutów ciągłych
* W regionach da się dobrze przewidywać klasy

## Historia
* Quinlan
	* wielowartościowe podziały
	* algorytm ID3, C4, C4.5, C50
	* Weka J48
* Breiman
	* podziały binarne
	* algorytm CART
	* scikit-learn, rpart

## Wymiar VC
* Teoretyczny, bez atrybutów ciągłych
	* liczba możliwych kombinacji wartości atrybutów
	* w skrajnym przypadku można zbudować drzewo, gdzie każdy przykład trafia do oddzielnego liścia
* Teoretyczny, z atrybutami ciągłymi - $\infty$
	* nieskończenie wiele sposobów etykietowania
* Efektywny
	* redukowany przez zastosowanie kryteriów stopu i przycinania

## Schemat algorytmu
* Sekwencja decyzji
	* kryterium stopu - węzeł czy liść
	* wybór klasy dla liścia - jaka predykcja najlepsza w liściu
	* wybór podziału dla węzła - jaki podział najlepszy w węźle
* Ten sam schemat powtarza się dla korzenia, jego węzłów potomnych, ich węzłów potomnych itd.
* Kolejność jest zazwyczaj nieistotna
	* w głąb albo wszerz

### Kryterium stopu
* Decyzja czy węzeł, któremu odpowiada podzbiór $T_n$ powinien być liściem
* $T_n$ - podzbiór zbioru trenującego w węźle $n$
* Prawdopodobieńśtwa klas w liściu
	* na podstawie rozkładu przykładów trenujących w $T_n$
* Jednolita klasa w $T_n$
	* idealna klasyfikacja
* $T_n = \varnothing$
	* mógł być taki podział
	* wybór klasy dominującej w rodzicu
* Brak możliwości podziału
	* wyczerpanie atrybutów
	* każdy możliwy podział skutkuje tylko 1 gałęzią
	* na ścieżce do tego węzła wszystkie podziały zostały wykorzystane
	* 2 przykłady o jednakowych wartościach atrybutów i różnych klasach
* Te 3 to najpóźniejsze kryteria jakie rozsądnie jest zastosować
	* można rozluźnić te kryteria - stosować wcześniej
	* służy ograniczeniu nadmiernego dopasowania
	* dla kryteriów powyżej model pomyli się na zbiorze trenującym tylko, kiedy pomyłka jest nieuchronna (niespójne dane)
* Rozluźnienie kryterium jednolitej klasy
	* któraś klasa jest istotnie dominująca w $T_n$
* Rozluźnienie kryterium pustego zbioru przykładów
	* zbiór jest dostatecznie mały
	* wybór dominującej klasy
* Rozluźnienie kryterium braku możliwości podziału
	* jeśli najlepszy podział jest słaby
	* wymaga oceny jakości, ale wybór podziału i tak wymaga oceny jakości

### Wybór podziału
* Istotny do kontrolowania poziomu dopasowania do danych
* Można wprowadzić do algorytmu obciążenie w stronę bardziej generalnych modeli
	* brzytwa Ockhama - preferujemy prostsze modele (heurystyka)
	* intuicja - mniej decyzji - mniejsze uzależnienie modelu od zbioru danych trenujących
* Wybrać podział tak, żeby przyspieszył osiągnięcie kryterium stopu
	* będzie krótsza ściezka - prostszy model
	* najlepiej kryterium jednolitej klasy
	* podział powinien sprzyjać wyłanianiu się jednolitych klas
* Na podstawie entropii
	* miara jednolitości rozkładu
	* $E_{T_{n,t=r}}(c) = \sum_{d \in C} -P_{T_{n,t=r}}(c=d) \cdot \log P_{T_{n,t=r}}(c=d)$ 
	* prawdopodobieństwa zbliżone do siebie - większa entropia
	* któraś klasa dominuje - mniejsza entropia
	* można uśrednić wartość po gałęziach podziału i dostać miarę dla podziału
	* nie ma znaczenia jaka podstawa logarytmu
* Entropia warunkowa
	* $E_{T_n}(c|t) = \sum_{r \in R_t} \frac{|T_{n,t=r}|}{|T_n|} \cdot E_{T_{n,t=r}}(c)$
	* minimalizowana
* Redukcja nieczystości w wyniku podziału
	* przyrost informacji
	* $\Delta E_{T_n}(c|t) = E_{T_n}(c) - E_{T_n}(c|t)$
	* przydatne do kryterium stopu
	* pokzauje co wnosi podział
* Indeks Giniego
	* $G_{T_{n,t=r}}(c) = 1 - \sum_{d \in C} P_{T_{n,t=r}}^2(c=d)$
	* zachowanie podobne jak entropia

### Przykład
Obliczanie entropii podziału na podstawie atrybutu overcast ze zbiou pogoda

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


dla outlook=sunny 3x no, 2x yes
$$
-2/5 \log(2/5) - 3/5 \log(3/5)
$$
dla outlook=rainy
$$
-3/5\log(3/5) - 2/5\log(2/5)
$$
dla outlook=overcast 5x yes, 0x no
$$
0
$$

### Przykład
Podział binarny, warunek równościowy

dla outlook=sunny, waga 5/14
$$
-2/5 \log(2/5) - 3/5 \log(3/5)
$$
dla outlook!=sunny, waga 9/14
$$
-6/9\log(6/9) - 3/9\log(3/9)
$$
## Przycinanie drzew decyzyjnych
* Cel
	* zapobieganie nadmiernemu dopasowaniu
	* bardziej wymagające ale potencjalnie skuteczniejsze niż kryterium stopu
* Operator
	* zastąpienie dodrzewa liściem
* Kryterium
	* oczekiwana redukcja błędu rzeczywistego
	* wiele różnych szczegółowych wariantów
* Strategia
	* najczęściej występująca
	* zstępująca
	* najpierw najlepszy
	* większość metod działa wstępująco (od liści do korzenia, odwrotnie niż rosło drzewo)
* W praktyce
	* przy tworzeniu jak najlepszego modelu ma sens budowanie zbyt głębokiego węzła i przycinanie
	* współcześnie coraz rzadziej są stosowane jako docelowe modele
	* czasami jako części składowe modeli - wtedy raczej bez przycinania
	* częściej dostrajanie kryterium stopu niż przycinanie
	* trzeba budować głębokie drzewo, żeby było z czego przycinać

### Reduced Error Pruning (REP)
* Kryteriium przycinania oparte na estymacji błędu rzeczywistego z wykorzystaniem osobnego podzbioru przykładów $R$ nieużywanego w trakcie budowy drzewa
* Węzeł $n$ jest zastępowany liściem $l$ jeśli
	* $e_R(l) \le e_R(n)$
	* błąd wyznacza się na podstawie tych przykładów z $R$, które docierają do tego miejsca w drzewie
* Dobre podejście jeśli możemy poświęcić osobną pulę przykładów
	* $R$ wyjęte ze zbioru trenującego
	* bardziej rzędu 50% niż 5%
	* inne metody nie wymagają odkładania przykładów na boku (np. estymacja na zbiorze trenującym, ale wprowadzona kara za wielkość drzewa, pesymistyczna korekta itp.)
* Może czasem lepiej przycinać trochę gorzej, ale budować lepiej
	* poza zakresem wykładu

### Konwersja drzewa do zbioru reguł
* Każda ścieżka od korzenia do liścia jest koniunkcją warunków - reguła
	* tyle reguł ile liści
	* klasa z liścia
* Czasem uważana za bardziej czytelną
* Można przycinać nie samo drzewo, a reguły
	* bardziej elastyczne
	* można usunąć warunek z tylko jednej reguły
	* usunięcie węzła modyfikuje wiele ścieżek

## Właściwości drzew decyzyjnych
* Zwykle dobra jakość predykcji, chociaż często inne algorytmy dają nieco lepsze modele
* Obecnie rzadziej stosowane, po czasach świetności
* Użyteczne jeśli model ma być zrozumiały dla człowieka
	* każdą decyzję modelu można wytłumaczyć
* Podatne na nadmierne dopasowanie
	* konieczne staranne dobranie kryteriów stopu lub zastosowanie przycinania
* Po niewielkiej modyfikacji mogą służyć jako modele regresji
	* poza zakresem wykładu
* Stosowane jako komponenty modeli zespołowych
	* las losowy
	* gradient boosting
	* jedne z najlepszych modeli dla danych tabelarycznych
