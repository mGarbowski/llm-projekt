# (2024-10-10)
# c.d.

## Błędy danych

Bezwzględny

$$\Delta d = [\Delta d_1 \ldots \Delta d_n]^T$$

Względny

Błąd bezwzględny wyniku
Błąd względny wyniku

Wskaźnik uwarunkowania (zależy od danych)
supremum, bo interesuje nas największa osiągana

$$
cond_\phi(d) = \lim_{\delta \rightarrow 0} \sup_{||\Delta d|| \le \delta} 
\frac
{||\phi(d+\Delta d) - \phi(d)||}{...}
$$

Względem wszystkich możliwych zaburzeń

Jeśli zadanie jest opisane funkcją różniczkowalną to wzór można wyprowadzić

Przybliżamy różnicę jako pochodna * przyrost danych (iloraz skalarny wektorów) (dla małych przyrostów)

Iloczyn skalarny przyjmuje maksymalną wartość kiedy wektory są współliniowe

$$
cond_\phi(d) = \frac{\| f'(d) \|   \| d \|}{|f(d)|}
$$
Daje maksymalną wartość (może być mniejsza w zależności od kierunku zaburzeń)

## Aproksymacja pochodnej funkcji
Przez iloraz różnicowy wsteczny

Jeśli w algorytmie operację możemy wykonać dokładnie (np. dzielenie tlyko przez potęge 2) to warto to przyjąć

...

Dla zmniejszania kroku $h$ rośnie uwarunkowanie
Im mniejszy kork $h$ tym mniejszy błąd aproksymacji
Przeciwne efekty
Istnieje optymalny krok minimalizujący błąd samej metody i błąd numeryczny

## Pierwiastki funkcji kwadratowej
Uwarunkowanie wzrasta dla $b^2 >> |4ac|$

Aby uniknąć błędu oblicza się pierwiastek który da się obliczyć z mniejszym błędem, a drugi oblicza się z wzoru Viete'a

Przekształcone wzory, kiedy potrzeba tylko jednego pierwiastka o mniejszym module

## Szacowanie
Dla wielu zadań nie ma analitycznych wzorów lub są bardzo skomplikowane
Norma wektoru błędu bezwzględnego danych jest ogranicozna przez $eps$

Z definicji wskaźnika uwarunkowania względny błąd wyniku to iloczyn uwarunkowania i względnego błędu danych

Szacujemy jako najmniejszą możliwą do wyznaczenia wartość dla której zachodzi nierówność

## Algorytm i numeryczne realizacje
* Zadanie obliczeniowe (matematyczne) $w = \phi(d)$
* Algorytm $A(d)$ obliczania wyniku zadania $\phi(d)$
	* sposób wyznaczenia wyniku zgodnie z jednoznacznie określoną kolejnością wkyonywania elementarnych działań arytmetycznych
* Numeryczna realizacja $fl(A(d))$ algorytmu $A(d)$
	* zastąpienie wielkości liczbowych ich reprezentacjami zmiennopozycyjnymi
	* wykonaniu operacji arytmetycznych w arytmetyce zmiennopozycyjnej

### Przykład
Zadanie $\phi(a,b) = a^2 - b^2$
Algorytm $A1(a,b) = a \cdot a - b \cdot b$
Algorytm $A2(a,b) = (a+b)(a-b)$

Przydatne
$|a \pm b| \le |a| + |b|$

Przerobić przykład z błędami danych

## Numeryczna stabilnośc algorytmu
Im dokładniejsza arytmetyka tym dokładniejsze wyniki

Algorytm A(d) relizujący fi(d) nazywamy numerycznie stabilnym, jeśli istnieje taka stała Ks (wskaźnik stabilności), że dla danych d i dostatecznie małego eps (silnej arytmetyki) zachodzi nierówność

Z definicji wynika że dla eps dążącego do 0, błąd dąży do 0

## Całkowity błąd względny
Zależy od

* Uwarunkowania zadania (błędu nieuniknionego) cond
* Stosowanej arytmetyki eps
* Wskaźnika stabilności numerycznej algorytmu (jakość algorytmu) Ks

### Metoda pozornych równoważnych zaburzeń
Stabilność numeryczną można udowodnić wykazując że fl(A(d)) jest zaburzonym dokładnym rozwiązaniem zadania fi o zaburzonych danych

Użyteczna metoda do zadań algebry liniowej



# Normy wektorów i macierzy
Aksjomat normy
Pojęcia V, K

1
2
3


Przestrzeń jest liniowa jeśli operacje liniowe nie wyprowadzają z tej przestrzeni (dodanie wektora, pomnożenie przez stałą)

Normy Holdera wektorów
... definicja

norma pierwsza
norma euklidesowa
norma nieskończoność

Normy są równoważne (dają ciasne ograniczenie z góry i z dołu)

## Normy macierzy
Macierze to operatory liniowe

Normę macierzy nazywamy indukowaną przez normę wektora jeśli zachodzi

$$
\| A \| = \max_{\{x: \|x\|=1\}} \|Ax\|
$$

Zależność $g_1(x) >0$ i $g_2(x) > 0$
to $\max_x [g_1(x) \cdot g_2(x)] \le \max_x g_1(x) \cdot \max_y g_2(y)$

Najważniejsze normy indukowane macierzy
norma pierwsza - maksymalna suma modułów w kolumnie
norma druga - norma spektralna (wartości własne)
norma nieskończoność - maksymalna suma modułów w wierszu 


$A^TA$ to zawsze macierz kwadratowa, dodatnio określona 
$x^T(A^TA)x = (Ax)^T \cdot Ax \ge 0$
wszystkie wartości własne takiej macierzy są nieujemne
$sp$ - zbiór wszystkich wartości własnych

### Norma euklidesowa macierz (norma Frobeniusa)
$$
\|A\|_E = \sqrt{\sum_{i=1}^m \sum_{j=1}^n |a_{ij}^2}
$$
Nie jest indukowana przez żadną normę wektora

dla macierzy jednostkowej norma frobeniusa jest $\sqrt{n}$ a dla wszystkich norm indukowanych jest 1

Jest zgodna z wektorową normą auklidesową

Łatwiej się liczy normę Frobeniusa niż normę spektralną

## Promień spektralny macierzy
$$
sr(A) = \max_{\lambda \in sp(A)} | \lambda |
$$

Dla dowolnej zgodnej normy macierzy A zachodzi $sr(A) \le \| \mathbf{A}\|$

## Układ algebraicznych równań liniowych
Ax = b

Metody rozwiązywania można podzielić na 2 grupy

* skończone
	* wynik otrzymujemy po skończonej, określonej ilości przekształceń, zależnej od wymiarowości zadania
* iteracyjne
	* startują z przybliżenia początkowego (znanego/założonego)
	* w kolejnych iteracjach poprawia się przybliżenie
	* dla wielkich układów, o specjalnej strukturze

### Uwarunkowanie układu równań liniowych
Przy zaburzeniu wektora b (wektora danych)
implikuje zaburzenie wektora wyniku x

inaczej - wskaźnik uwarunkowania macierzy

dla norm Holdera zawsze >= 1

Macierz Hilberta - przykład ogromnego uwarunkowania