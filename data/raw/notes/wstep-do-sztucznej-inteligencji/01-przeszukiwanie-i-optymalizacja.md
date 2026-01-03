# Przeszukiwanie i optymalizacja

## Inżynierski podział
* Uczenie maszynowe
	* modelowanie zjawisk i ich objaśnianie
	* predykcja zjawisk
	* analiza scenariuszy na podstawie modeli
* Wspomaganie decyzji
	* doradzanie optymalnej decyzji
	* wybór optymalnej decyzji i jej wykonanie


## Problem plecakowy
* Jest $n$ przedmiotów
* Każdy przedmiot ma wagę $w_i$ i wartość $p_i$
* Trzeba wybrać przedmioty o największej możliwej wartości i łącznej wadze nie większej niż $W$

$$max \Sigma_{i=1}^{n}x_ip_i$$
$$ \Sigma_{i=1}^n x_iw_i \le W$$
$$x_i \in \{0, 1\}$$
Problem można zamodelować jako drzewo z etykietami, gdzie liście to finalne decyzje (który element wchodzi do plecaka, a który nie wchodzi), węzły nieterminalne są pośrednimi decyzjami. Etykieta liścia to sumaryczna wartość, etykieta węzła nieterminalnego to najlepsza z etykiet dzieci.


### Algorytm best-first
```python
A = PriorityQueue(root)
while !stop:
	x = A.pop()
	if x.isTerminal():
		stop = true
	Y = x.neighbors()
	A = A.push(Y)
```

Trzeba wykonać $2n$ operacji odczytania etykiet z węzłów - wysokość drzewa to $n$, każdy węzeł ma $2$ sąsiadów (dzieci)

Ale to działa przy założeniu że znamy etykiety (a nie znamy).

Jeśli etykiety są tylko przybliżone to nie można zakończyć przeszukiwania od razu po osiągnięciu węzła terminalnego. Trzeba sprawdzić każdy węzeł dopuszczalny.

## Algorytm A*
Algorytm best-first + funkcja kosztu (zysku) + funkcja heurystyczna

Elementy na pewno zapakowane w węźle nieterminalnym - funkcja zysku.
Finalny zysk w węźle terminalnym będzie większy lub równy od wcześniejszego (z węzła nieterminalnego)

Można zastosować heurystykę - wolne jednostki wagi * uśredniona wartość na kg z niezapakowanych przedmiotów. Zakłada, że przedmioty można podzielić - optymistyczne oszacowanie. Upycha się przedmioty do plecaka od najlepszych do najgorszych ucinając ostatni, który nie wejdzie w całości

Funkcja zysku i funkcja heurystyczna nie mogą być od siebie zupełnie niezależne. Funkcja zysku wynika z definicji problemu. Każda kolejna decyzja nie zmniejsza zysku. Funkcja heurystyczna ma szacować przyrost funkcji zysku (w tych samych jednostkach miary).

### Funkcja heurystyczna powinna być 
* dopuszczalność - $g(x) + h(x) \ge g(x_t)$
	* wartość szacowana zawsze musi być większa lub równa od prawdziwej
	* nadmierny optymizm
* monotoniczna $g(x_{i+1}) + h(x_{i+1}) \le g(x_i) + h(x_i)$
	* w kolejnym kroku szacowana wartość musi zmaleć względem poprzedniego
	* błąd musi maleć w miarę zbliżania się do węzła terminalnego

```python
q = PriorityQueue(root)
best = 0
while not q.empty():
	x = q.pop()

	if x.isTerminal() and g(x) > best
		best = g(x)

	if g(x) + h(x) >= best:
		y = x.neighbors()
		q.push(y)
```

Gwarancja optymalnego wyniku jest dopiero po wyczerpaniu kolejki, w najgorszym przypadku, nawet przy poprawnie zdefiniowanej funkcji heurystycznej rozwiązanie może być tak samo złe jak przy pełnym przeszukaniu

Skoro etykiety są przeszacowane i błąd maleje to po znalezieniu jednego rozwiązania już nie trzeba rozważać poddrzew o niższej etykiecie bo na pewną nie dadzą lepszego rozwiązania

### Modelowanie problemu
Żeby wykorzystać algorytm A* do rozwiązania problemu
* Zamodelować rozwiązanie problemu jako wektor o wartościach 0, 1 lub ?
	* ? oznacza jeszcze nie podjętą decyzję, będzie zastąpiony przez 0 lub 1
* Uporządkować rozwiązania i pośrednie rozwiązania w drzewo jak na obrazku
* Określić kryteria dopuszczalności rozwiązania
* Określić funkcję zysku
* Określić funkcję heurystyczną tak, żeby spełniała warunki dopuszczalności i monotoniczności

![[img-drzewo-przeszukiwan.png]]

## Inny model przestrzeni przeszukiwań
Węzły są połączone ze sobą relacją sąsiedztwa jeśli różnią się 1 bitem (hipersześcian?). Nie ma hierarchii i narzuconego kierunku jak w drzewie.

Węzły bez sąsiadów o lepszych wartościach funkcji zysku - optima lokalne, utrudniają przeszukiwanie.

## Algorytm wspinaczkowy
Rozważyć wszystkich sąsiadów i wybrać najlepszego dopuszczalnego dopóki istnieje taki sąsiad. Zatrzyma się na pierwszym napotkanym optimum lokalnym. 

Można np. kilkukrotnie wylosować węzeł początkowy żeby wykonać lepszą eksplorację przestrzeni.


## Optymalizacja w przestrzeni ciągłej
W przestrzeni $\mathbb{R}^n$ jest continuum sąsiadów (np. problem uczenia sieci neuronowej) - nie da się zbadać wszystkich elementów.

### Metdoa najszybszego wzrostu (gradient ascent)
$\beta_t$ - ciąg dodatnich współczynników kroku (nie musi być stały)
$\nabla q(x)$ - gradient funkcji celu w punkcie x
$x$ - punk roboczy

```python
x = x_0
while !stop:
	wektor_poprawy = gradient(q(x))
	x += krok * wektor_poprawy
```

W praktyce może bardziej się opłacać szacowanie gradientu przez losowe próbkowanie - metoda stochastycznego wzrostu / spadku

Wyzwaniem jest dobranie właściwej wartości kroku, to zależy od funkcji celu, są różne strategie adaptacji.

Współczynnik kroku
* za mały - algorytm bardzo wolno zbliża się do optimum lokalnego
* za duży - algorytm w kolejnych krokach przeskakuje przez minimum, może eksplodować do nieskończoności zamiast zbiegać do optimum lokalnego
* można uruchomić algorytm kilka razy z różnymi wartościami i zobaczyć dla której zadziała najlepiej

### Metoda Newtona
Macierz drugich pochodnych cząstkowych (hesjan - gradient gradientu), mówi o tym jak zmienia się gradient. Na tej podstawie można dostosowywać wartość $\beta_t$ 

Korekta o odwrotność hesjanu - kierunek przechodzi przez optimum funkcji kwadratowej, a wiele funkcji można przybliżyć funkcją kwadratową (szererg Taylora)

Metoda bazuje na przybliżeniu funkcji kosztu funkcją kwadratową (Taylora), dla funkcji niepodobnych do funkcji kwadratowej może dawać słabe rezultaty

$d = H_q^{-1}(x) \cdot \nabla q(x)$

Funkcje zysku zazwyczaj są wynikiem jakiejś procedury obliczeniowej, nie da się wyliczyć gradientu analitycznie - szacuje się go numerycznie (różniczki) i hesjan też (BFGS, DFP)