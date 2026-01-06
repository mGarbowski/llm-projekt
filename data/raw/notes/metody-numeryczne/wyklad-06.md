# Rozwiązywanie równań nieliniowych (2024-11-21)
Obliczanie zer funkcji, może być 0, skończona liczba, nieskończenie wiele.

Metody iteracyjne znajdowania pojedynczego zera, zaczyna się od wyznaczenia przedziału w którym szukamy (przedziały izolacji pierwiastka)

w przedziale izolacji pochodna powinna nie zmieniać znaku

## Metody iteracyjne
Rząd (wykładnik zbieżności) metody to największa liczba p >= 1 taka że 

$$
\lim_{n \rightarrow \infty} \frac{|x_{n+1} - 
\alpha|}{|x_n - \alpha|^p} = k < \infty
$$

$\alpha$ - szukany pierwiastek
największe p, dla którego granica jest skończona,
im większe p tym szybsza metoda
k to iloraz zbieżności (convergence rate)

dla k > 0 można zapisać 

$$
|x_{n+1} - \alpha| \simeq k \cdot |x_n - \alpha|
$$

p=1 - zbieżność liniowa - zbieżność ciągu liczbowego, k musi być <1
p=1 i $k \rightarrow 0$ - zbieżność superliniowa
p=2 - zbieżność kwadratowa

metody iteracyjne dla problemów nieliniowych są zbieżne tylko lokalnie (na przedziale izolacji pierwiastka)

### Metoda bisekcji
$[a,b] = [a_0, b_0]$ - początkowy przedział izolacji pierwiastka
W każdej (n-tej) iteracji

dzielimy przedział na pół i sprawdzamy, w której połówce leży rozwiązanie
przez sprawdzenie znaków na krańcach przedziału i na środku - wybieramy ten gdzie na skraju i środku są różne znaki - pierwiastek musi leżeć pomiędzy

powtarzamy do spełnienia $f(c_n) < \delta$

Metoda jest zbieżna liniowo (p=1) z k=0.5

Metoda wolna ale gwarantowane że znajdzie rozwiązanie w przedziale (brute force)

### Metoda Regula Falsi
n-ta iteracja - dzielimy podział na 2 części
prowadzimy sieczną między punktami odpowiadającymi krańcom przedziału i jako c_n punkt przecięcia siecznej z osią x

wzór na c_n ...

do następnej iteracji jest wzięty przedział zawierający pierwiastek (jak w bisekcji)

generalnie szybsza od bisekcji ale są przykłady dla których jest wolniej zbieżna (rysunek)

niezalecana w klasycznej postaci

### Zmodyfikowana metoda Regula Falsi
Jeśli punkt się zagwoździ to zmniejszenie dwukrotne wartości funkcji z jednej strony (wzory...)

Zbieżność nadal jest globalna, ale superliniowa (znacznie lepsza)

### Metoda siecznych
Sieczna prowadzona zawsze przez 2 ostatnio wyznaczone punkty

wzór ...

zbieżna tylko lokalnie, może zawieść
rząd zbieżności ok 1.618

### Metoda Newtona (stycznych)
Bazuje na rozwinięciu funkcji do szeregu taylora (tylko pierwszaw pochodna) - styczna do wykresu w punkcie x_n

następny punkt to x w którym styczna przecina się z osią x

zbieżność lokalna
rząd zbieżności p=2 (kwadratowa)

wzór na współczynnik zbieżności -> jak funkcja płasko przechodzi przeez oś x to będzie wolna zbieżność

### Zabezpieczenie przed brakiem zbieżności
Schemat blokowy algorytmu ...

algorytm podstawowy to ten szybszy (np. Newton)
jeśli punkt nie należy do przedziału to przełączamy się na metodę bisekcji (niezawodną, może być jakaś inna niezawodna)
jeśli potencjalnie szybszy algorytm nie spełnia kryterium szybkości to przełączenie na metodę bisekcji (w zależności od stromości funkcji mogą działać wolniej)

Przykładowy test szybkości
szybka metoda powinna zmniejszać przedział bardziej niż bisekcja (czyli bardziej niż 2 razy)

jeśli równanie pochodzi z modelu o dokładnosci 1% to nie ma sensu obliczać rozwiązania z dokładnością 10^-6

na projekt!


## Układ równań nieliniowych
Dla 2 zmiennych to powierzchnia w 3 wymiarach
Przecinają płaszczyznę zerową (z=0) po jakichś krzywych

punkt M na rysunku - wredny przykład, metoda może się zagnieździć

Trudno jest określić przedziały izolacji
zwłaszcza dla więcej niż 3 wymiarów

Uogólniona metoda bisekcji
Dzielimy przestrzeń na podobszary (prostokąty)

Metoda losowa
losowo generujemy punkty startowe dla metod lokalnie zbieżnych

Metody globalnie zbieżne
zbliżony problem do optymalizacji globalnej
(sprowadzalne do siebie)

nie ma uniwersalnej, najlepszej metody na rozwiązywanie równań nieliniowych

### Metoda Newtona (wielowymiarowa)
Taka sama filozofia - rozwinięcie szeregu Taylora w pierwszej pochodnej
pochodna to macierz (jakobian)
wiersz to kolejne pochodne cząstkowe pierwszej funkcji

traktujemy liniowe przybliżenie funkcji jako ...
wzór - mnożenie przez macierz odwrotną zamiast dzielenia
wzór z książek vs wzór do implementacji (użyc solwera dla równań liniowych)
rozwiązanie dla wektora różnic

zbieżna lokalnie kwadratowo

wada - konieczność liczenia jakobianu w każdym kroku

### Dyskretna metoda Newtona
jak wyżej tylko pochodne cząstkowe szacowane numerycznie

e - wersor układu współrzędnych

dla prostych funkcji można obliczać symbolicznie pochodne (sa do tego narzędzia w matlabie)

Metody quasi-newtonowskie - ten sam sposób działania tylko różne sposoby na szacowanie jakobianu (żeby go nie obliczać bezpośrednio) (np. metoda Broydena)

## Metoda iteracji prostej
Metoda punktu stałego (fixed point method)
W wielu zastosowaniach spotykamy równanie lub układ w postaci

$$x - f(x)=0$$
$$x_{k+1} = f(x_k)$$
Metody jacobiego i gaussa-seidla to przykłady iteracji prostej

ciąg przybliżeń jest lokalnie zbieżny do rozwiązania $\alpha$ (punktu stałego)
wttw $sr(f'(\alpha)) < 1$
promień spektralny jakobianu mniejszy od 1 (największy moduł wartości własnej)

szybkość zbieżności można poprawić stosując metodę z relaksacją

$$
x_{k+1} = x_k + s(f(x_k) - x_k)
$$
$s \in (0,1]$

zbieżny jeśli ... (wzór)

## Wyznaczanie zer wielomianów
Z podstawowego twierdzenia algebry wielomian n-tego stopnia ma dokładnie n pierwiastków zespolonych

pierwiastki rzeczywiste albo parami zespolone, mogą być wielokrotne

### Metoda Mullera (idea)
w każdej iteralcji przybliżamy wielomianem kwadratowym, znajdując jego zero (uogólnienie metody siecznych)

### Metoda Mullera MM1
Każda iteracja bazuje na 3 ostatnich punktach, pierwiastek leży między skrajnymi
przez te 3 prowadzimy parabolę
jako przybliżenie bierzemy jedno z miejsc zerowych

zmienna przyrostowa z (upraszcza zapis)
dzięki zamianie zmiennych redukuje się wyznaczanie paraboli do 2 równań (zamiast 3)
$c=f(x_2)$

interesuje nas ten pierwiastek, który leży najbliżej $x_2$ (najmniejsze z)
bierzemy pierwiastek o najmniejszej wartości

$x_3 = x_2 + z_{min}$

jeśli delta wychodzi ujemna - będzie pierwiastek zespolony
metodę implemetuje się w arytmetyce liczb zespolonych

przed przejściem do następnej iteracji odrzucamy spośró x_0, x_1, x_2 ten który jest najbardziej oddalony od x_3

### Metoda Mullera MM2
Iteracja bazuje na jednym (ostatnim) punkcie x_k, wykorzystuje pochodną

wywliczamy współczynniki paraboli z pochodnych
dalej analogicznie - wybieramy pierwiastek o mniejszym module

wzór ...

### Metoa Laguerre'a
dla n=2 to samo co MM2
uogólniony dla większej liczby równań
ogólnie nieco szybsza od MM2
globalnie zbieżna jeśli same zera rzeczywiste (rzadki przypadek)

podobna zbiezność dla laguerr'a i newtona przy rzeczywistych pierwiastkach (zależy bardziej od punktu startowego)

### Deflacja czynnikiem liniowym
Po wyznaczeniu jednego pierwiastka wykonujemy dzielenie wielomianu przez czynnik liniowy - deflacja

Schemat prosty Hornera
n liniowych operacji
błędy arytmetyczne się kumulują

Odwrotny schemat Hornera

Sklejany schemat Hornera
połowę współczynników wyznaczamy prostym schematem, a drugą połowę odwrotnym prostym schematem

### Metoda Bairstowa
W arytmetyce liczb rzeczywistych

iloczyn dwóch liczb sprzężonych daje rzeczywistą funkcję kwadratową

wyznaczane pierwiastki parami stosując deflację czynnikiem kwadratowym

po dzieleniu wielomianu zostaje reszta, dobieramy p i r tak żeby reszta wynosiła 0

korzysta z metody newtona

pochodne po p i r muszą być równe 0

...

### Root polishing
znajudjemy pierwszy pierwiastek
kolejne wyznaczamy przez dzielenie
błędy numeryczne się kumulują
chcemy wszystkie zera z maksymlaną dokładnością

na oryginalnym wielomianie startujemy w przybliżonych zerach wyznaczonych przez dzielenie
zazwyczaj jedna iteracja metody Newtona (mało iteracji)

## Kolokwium
bez dzisiejszego materiału
do wartości własnych włącznie
zadania na slajdach, na końcach rozdziałów z podręcznika