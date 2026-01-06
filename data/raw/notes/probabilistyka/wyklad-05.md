## Wariancja
Wygodniejszy wzór

$$
VX = EX^2 - (EX)^2
$$

### Dowód
$$
VX = E((X-EX)^2) = E(X^2 + (EX)^2 - 2 \cdot X \cdot EX)
= EX^2 + E((EX)^2) - E(2\cdot X\cdot EX)
= EX^2 + (EX)^2 - 2 \cdot EX \cdot EX
= EX^2 - (EX)^2
$$

### Własności wariancji
Jeśli $X$ jest zmienną losową dla której istnieje $EX^2$, to
* $VX \ge 0$
* $VX = 0 \iff X$ ma  rozkład jednopunktowy (jest stała)
* $V(aX + b) = a^2 \cdot VX$ dla wszystkich $a, b \in \mathbb{R}$
* W ogólnym przypadku $V(X + Y) \ne VX + VY$

Wariancja dla wylosowanej próby oznaczana jest symbolem $s^2$

$$
s^2 = \frac{1}{n-1} \cdot \sum_{i=1}^n (x_i - \bar{x})^2
$$

Kiedy dzieli się przez $n-1$ to estymata nieobciążona wariancji, wtedy lepiej szacuje wariancję populacji. `np.var` dzieli przez $n$

* $VX$ - wariancja cechy $X$ mierzona dla całej populacji
* $s^2$ - wariancja cechy $X$ mierzona dla próby

## Nierówność Czebyszewa
Dla każdego $\epsilon > 0$ 

$$
P(|X-EX| \ge \epsilon) \le \frac{\sigma_T^2}{\epsilon^2}
$$

$$
P(|X-EX| < k \cdot \sigma_X) \ge 1 - \frac{1}{k^2}
$$

Dla $k=2$ ponad 75% wartości zmiennej X jest nie dalej od średniej niż $2s$
Dla $k=3$ ponad 88% wartości

Przedział wartości typowych - $[\bar{x} - 2s, \bar{x} + 2s]$
Pozostałe to obserwacje odstające

# Wybrane rozkłady jednowymiarowych zmiennych losowych

## Rozkłady dyskretne

### Rozkład jednopunktowy
Zmienna losowa ma tylko jedną wartość.

* $S_X = \{a\}$
* $P(X=a) = 1$
* $EX = a$
* $VX = 0$

### Rozkład dwumianowy (Bernouliego)
Wykonujemy $n$ doświadczeń w schemacie Bernouliego, z prawdopodobieństwem sukcesu w jednej próbie równym $p$ (doświadczenia są niezależne od siebie).

Niech $X$ oznacza livzbę sukcesów. Wtedy zmienna losowa X ma rozkład dwumianowy z parametrami $n$ i $p$.

Oznaczenie $(X \sim B(n, p))$, gdzie $p\in (0,1)$ i $n\in\mathbb{N}$, jeśli

* $S_X = \{0, \ldots, n\}$
* $P(X=k) = \binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}$
* $EX = n \cdot p$
* $VX = n \cdot p \cdot (1-p)$
* Najbardziej prawdopodobna wartość - $k$ takie że $(n+1) \cdot p - 1 \le k \le (n+1) \cdot p$
	* Może być dokładnie jedna lub dokładnie 2 takie liczby

### Rozkład Poissona
Doświadczenie: np. liczba samochodów przejeżdżających przez pewien punkt drogi, liczba klientów w kolejce

Zmienna losowa $X$ ma rozkład Poissona z parametrem $\lambda > 0 (X \sim P(\lambda))$, jeśli $S_X = \mathbb{N} \cup \{0\}$

$$
P(X = k) = e^{-\lambda} \cdot \frac{\lambda^k}{k!}
$$

$$
EX = VX = \lambda
$$

### Przybliżenie Poissona
Dla dużych $n$ i małych $p$

$$
\binom{n}{k} \cdot p^k \cdot (1-p)^{n-k} \simeq e^{-\lambda} \cdot \frac{\lambda^k}{k!}
$$
$$
\lambda = n \cdot p
$$
### Przykład 1
Prawdopodobieństwo wygranej na pewnej loterii wynosi $0.1$. Obliczyć prawdopodobieństwo, że wśród $1000$ osób, które kupiły los wygra co najmniej $10$ osób.

$X$ - liczba osób, które wygrają
$X \sim B(1000, 0.01)$
$$
P(X \ge 10) = 1 - P(X < 10) = 1 - \sum_{k=0}^9 P(X=k)
=1 - \sum_{k=0}^9 \binom{1000}{k} \cdot (0.01)^k \cdot (0.99)^{1000-k}
\simeq 1 - \sum_{k=0}^9 e^{-10} \cdot \frac{10^k}{k!}
$$


### Rozkład geometryczny
Wykonujemy doświadczenia w schemacie Bernouliego do momentu pojawienia się pierwszego sukcesu.

Zmienna losowa $X$ ma rozkład geometryczny z parametrem $p\in(0,1) (X \sim g(p))$, jeśli $S_X = \mathbb{N}$

$$
P(X=k) = (1-p)^{k-1} \cdot p
$$

$$EX = \frac{1}{p}$$
$$VX = \frac{1-p}{p^2}$$
### Własność braku pamięci rozkładu geometrycznego
Jeśli X ,a rozkład geometryczny z parametrem p, to dla dowolnych $n, m \in \mathbb{N}$

$$
P(X > n + m | X > n) = (1-p)^m = P(X > m)
$$

