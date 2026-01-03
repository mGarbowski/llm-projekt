# Zmienne losowe jednowymiarowe (2023-10-21)

## Przykład 1
Rzucamy 2 razy symetryczną monetą. Niech $X$ oznacza liczbę wyrzuconych reszek. Zapisać $X$ jako funkcję zdarzenia elementarnego.

$$
\Omega = \{ OO, OR, RO, RR \} = \{ \omega_1, \omega_2, \omega_3, \omega_4 \}
$$

X(omega) = {
	0 dla omega_1
	1 dla omega_2, omega_3
	2 dla omega_4
}

Zmienna losowa o rozkładzie dyskretnym

## Przykład 2
Losujemy liczbę z przedziału $[0, 2]$. Niech $Y$ będzie równe podwojonej wylosowanej liczbie. Zapisać $Y$ jako funkcję zdarzenia elementarnego.

$$
\Omega = [0, 2]
$$
$$
Y(\omega) = 2 \omega
$$

Zmienna losowa o rozkładzie ciągłym

## Jednowymiarowa zmienna losowa
Określona na przestrzeni probabilistycznej $(\Omega, \mathcal{F}, P)$. Funkcja $X: \Omega \rightarrow \mathbb{R}$  taką, że dla każdego $t \in \mathbb{R}$

$$
\{ \omega \in \Omega : X(\omega) \le t\} = X^{-1}((-\infty, t]) \in \mathcal{F}
$$

$X^{-1}((-\infty, t]) \in \mathcal{F}$ oznacza, że $X^{-1}((-\infty, t])$ jest zdarzeniem losowym

Rozkład zmiennej losowej określa jej zbiór wartości oraz prawdopodobieństwa, z jakimi te wartości są przyjmowane.

## Dystrybuanta
Funkcja jednowymiarowej zmiennej losowej $X: \Omega \rightarrow \mathbb{R}$,
$F_X: \mathbb{R} \rightarrow [0, 1]$, która dla każdego $t$ jest określona wzorem

$$
F_X(t) = P(\{\omega \in \Omega: X(\omega) \le t\}) = P(X^{-1}((-\infty, t]))
$$

Da się taką funkcję wyznaczyć dla każdej zmiennej losowej.

Dystrybuanta jednoznacznie wyznacza rozkład zmiennej losowej. Taka sama dystrybuanta oznacza taki sam rozkład.

Zawsze niemalejąca. Conajmniej prawostronnie ciągła

## Twierdzenie
Funkcja $F: \mathbb{R} \rightarrow \mathbb{R}$ jest dystrybuantą jednowymiarowej zmiennej losowej wtedy i tylko wtedy gdy

* $lim_{t \rightarrow -\infty} F(t) = 0 \land lim_{t \rightarrow \infty} F(t) = 1$
*  $F$ jest funkcją niemalejącą
* $F$ jest funkcją co najmniej prawostronnie ciągła


* $P(X \le a) = F_X(a)$
* $P(X = a) = F_X(a) - lim_{t \rightarrow a^-}F_X(t)$
* $P(X < a) = lim_{t \rightarrow a^-} F_X(t)$
* $P(X \ge a) = 1 - lim_{t \rightarrow a^-} F_X(t)$
* ...
* każde można wyznaczyć

## Punkt skokowy
Punkt skokowy rozkładu zmiennej losowej $X$ nazywamy każdą liczbę $a \in \mathbb{R}$ taką że $P(X=a) > 0$ (w dystrybuancie musi być nieciągłość, skok w górę)

Liczba $a$ jest punktem skokowym rozkładu zmiennej losowej $X$ wwtedy i tylko wtedy gdy funkcja $F_X$ jest nieciągła w punkcie $a$.

## Rozkład dyskretny
Zmienna losowa X ma rozkład dyskretny (skokowy) jeśli jej zbiór wartości jest przeliczalny (albo szczególnym przypadku skończony).

## Nośnik
Nośnikiem rozkładu zmiennej losowej X typu dyskretnego nazywamy przeliczalny zbiór $S_X$ taki że

* $p_i = P(X=x_i) > 0$ dla każdego $x_i \in S_X$
* $\sum_{x_i\in S_X} p_i = 1$



## Funkcja prawdopodobieństwa
Funkcja $p_X: S_X \rightarrow (0, 1]$ taka że

$$
p_X(x_i) = p_i
$$

Jendoznacznie wyznacza rozkład zmiennej losowej typu dyskretnego

## Twierdzenie
Jeśli $X$ ma rozkład dyskretny, to

$$
F_X(x) = \sum_{x_i \le x} P(X=x_i)
$$


## Rozkład ciągły
Zmienna losowa $X$ o dystrybuancie $F_X$ ma rozkład ciągły, jeżeli istnieje funkcja $f_X$

$$
F_X(t) = \int_{-\infty}^t f_X(x)dx
$$

Funkcję $f_X$ nazywamy gęstością rozkładu zmiennej losowej $X$.

Nośnikiem zmiennej losowej $X$ o rozkładzie ciągłym jest zbiór $S_X$ taki, że 
$$
S_X = \{x \in \mathbb{R} : f_X(x) > 0\}
$$

## Twierdzenie
Funkcja f jest gęstością jednowymiarowe jzmiennej losowej wtedy i tylko wtedy, gdy

* $f(x) \ge 0$ prawie wszędzie 
* $\int_{-\infty}^\infty f(x)dx = 1$

Gęstość jednoznacznie wyznacza rozkład zmiennej losowej typu ciągłego

## Twierdzenie
Jeśli X ma rozkład ciągły to

* F_X jest funkcją ciągła w R
* $F_X' = f$ w każdym punkcie ciągłości f_X
* $P(a < X < b) = \int_a^bf(x)dx = F_X(b) - F_X(a)$
* $P(X=a) = 0$ dla każdego $a \in \mathbb{R}$
