# Estymacja (2024-01-15)
## Próba losowa
Prosta próba losowa - ciąg $n$ niezależnych zmiennych losowych o tym samym rozkładzie (np. dla grupy studentów ciąg $X_i$ może oznaczać ich wzrosty)

## Statystyka
Każda funkcję próby losowej $g(X_1, \ldots, X_n)$ nazywa się statystyką

### Przykłady statystyk
* Średnia z próby $\bar{X} = \frac{1}{n} \sum_{k=1}^n X_k$
* Wariancja z próby $S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i-\bar{X})^2$
* $\ldots$

## Estymacja punktowa
Wiadomo z jakiego rozkładu pochodzi próba ale nie wiadomo jakie są parametry teego rozkładu (np. wiadomo że rozkład normalny ale nie znamy średniej i wariancji).

Parametry $\theta_1, \ldots, \theta_k$ szacuje się na podstawie $n$-elementowej próby

Każdą statystykę $\hat{\theta}(X_1, \ldots, X_n)$ której wartości przyjmuje się jako oszacowanie nieznanego parametru $\theta$ nazywa się estymatorem tego parametru

Wartość $\hat{\theta}(x_1, \ldots, x_n)$ jest punktowym oszacowaniem parametru $\theta$ dla całej populacji

### Przykłady
* Wartość średnia z próby jest dobrym estymatorem wartości oczekiwanej dla całej populacji
* Wariancja z próby jest dobrym estymatorem wariancji dla całej populacji

### Estymator nieobciążony
Estymator nazywa się nieobciążonym jeśli

$$
E(\hat{\theta}(X_1, \ldots, X_n)) = \theta
$$

$\bar{X}$ i $S^2$ są estymatorami nieobciążonymi

## Metoda największej wiarygodności wyznaczania estymatorów

Wprowadzamy funkcję wiarygodności
$L = f(x_1, \theta_1, \ldots, \theta_k) \cdot \ldots \cdot f(x_n, \theta_1, \ldots, \theta_k)$ 

gdzie $f$ to gęstość dla rozkładu ciągłego, funkcja prawdopodobieńśtwa rozkładu dyskretnego
Estymatory parametrów to takie $\hat{\theta_1}, \ldots, \hat{\theta}_k$ dla których $L$ osiąga maksimum (łatwiej znaleźć minimum dla logarytmu z $L$)


### Przykład
Wartości $X: 1, 3, 2, 5 ,3, 3, 7, 1, 2, 3$

$X \sim g(p)$ - założenie, nieznane $p$
$P(X=x) = (1-p)^{x-1} \cdot p = f(x, p)$
$x_i = 1, 2, \ldots$

Metoda największej wiarygodności
Zakładamy, że mamy realizację próby $n$-elementowej $x_1, \ldots, x_n$ 
$$
L = f(x_1, p) \cdot f(x_2,p) \cdot \ldots \cdot f(x_n,p)
=(1-p)^{x_1 +x_2 + \ldots + x_n - n} \cdot p^n
= (1-p)^{n(\bar{x} - 1)} \cdot  p^n
$$
$$
ln(L) = ln((1-p)^{n(\bar{x}-1)}) + ln(p^n)
= n(\bar{x}-1)ln(1-p) + nln(p)
$$
$$
\frac{\partial lnL}{\partial p} = -\frac{n(\bar{x}-1)}{1-p} + \frac{n}{p}
$$
$$
\frac{\partial lnL}{\partial p} = 0 
\iff n - np = n\bar{x}p - np
\iff 1 = \bar{x}p
\iff p = \frac{1}{\bar{x}}
$$

$$
\frac{\partial^2lnL}{\partial p^2} 
= -n(\bar{x}-1)\cdot (-\frac{1}{(1-p)^2}) \cdot (-1) - \frac{n}{p^2}
= -\frac{n(\bar{x}-1)}{(1-p)^2} + \frac{n}{p^2}
< 0
$$

Więc w punkcie $p = 1/\bar{x}$ funkcja L osiąga maksimum $\implies \hat{p} = 1/\bar{X}$

Liczymy wartość estymatora dla wylosowanej próby $p = 1/3$


## Model regresji
$$
Y = f(X) + \epsilon
$$
* $Y$ - zmienna objaśniana (zależna)
* $X$ - zmienna objaśniająca (niezależna)
* $f(X)$ - funkcja regresji - funkcja określają teoretyczne wartości $Y$ odpowiadające wartościom $X$
* $\epsilon$ - błąd regresji - losowy składnk modelu regresji - opisuje łączny wpływ wszystkich innych poza $X$ czynników działających na $Y$
	* zazwyczaj zakłada się, że ma rozkład normalny o średniej $0$
* $\hat{Y} = f(X)$ - prognozowana wartość cechy $Y$ przy danej wartości cechy $X$

Dąży się do tego, żeby błąd był jak najmniejszy
Najczęstszym sposobem wyznaczania funkcji regresji jest metoda najmniejszych kwadratów czyli minimalizacja wyrażenia $E(Y-\hat{Y})^2$ 

Wyrażenie $E(Y-f(X))^2$ osiąga najmniejszą wartość, gdy $f(x) = E(Y|X=x)$ więc $f$ jest najlepszą funkcją regresji $Y$ względem $X$

### Model regresji liniowej
Można go rozważać tlyko w sytuacji, gdy związek między badanymi cechami jest liniowy, można to ocenić po wykresie rozproszenia i wartości współczynnika korelacji

$$
Y = aX + b + \epsilon
$$
Jeśli rozkład wektora $(X,Y)$ jest znany to współczynniki wynoszą

$$a = \frac{cov(X,Y)}{VX}$$

$$b = EY - aEX$$

Jeśli rozkład nie jest znany i dysponujemy próbą to

$$
\hat{a} = \frac{\sum_{i=1}^n(x_i-\bar{x})(y_i-\bar{y})}{\sum_{i=1}^n (x_i-\bar{x})^2}
$$

$$
\hat{b} = \bar{y} - a\bar{x}
$$
