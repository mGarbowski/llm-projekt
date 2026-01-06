## Przykład 2.
X_1 i X_2 są niezależnymi zmiennymi losowymi takimi, że $X_1 \sim P(\lambda_1), X_2 \sim P(\lambda_2)$. Wyznaczyć rozkład zmiennej losowej $Z=X_1+X_2$

$$
X_1 \sim P(\lambda_1) \implies 
P(X_1=k) = e^{-\lambda_1} \cdot \frac{\lambda_1^k}{k!}
$$

$$
S_Z = \{0, 1, 2 \ldots\}
$$
$$
P(Z=n) = P(X_1 + X_2 = n) = P(X_1=0, X_2=n) + P(X_1=1, X_2 = n-1) + \ldots P(X_1=n, X_2=0)
$$

$$
P(Z=n) = \sum_{k=0}^n P(X_1=k, X_2 = n-k)
= \sum_{k=0}^n e^{-(\lambda_1 + \lambda_2)} \cdot \frac{\lambda_1^k}{k!} \cdot \frac{\lambda_2^{n-k}}{(n-k)!}
$$

$$
P(Z=n) = e^{-(\lambda_1 + \lambda_2)} \cdot \frac{1}{n!} \cdot \sum_{k=0}^n \binom{n}{k} \cdot \lambda_1^k \cdot \lambda_2^{n-k}
= e^{-(\lambda_1 + \lambda_2)} \cdot \frac{(\lambda_1 + \lambda_2)^n}{n!} \implies Z \sim P(\lambda_1 + \lambda_2)
$$

### Wniosek
Niech $X_1, X_2, \ldots, X_n$ będą niezależnymi zmiennymi losowymi z rozkładu Poissona to zmienna $Z=\sum_{k=0}^n X_k \sim P(\lambda = \sum \lambda_i)$

## Przykład 3.
Wektor $(X,Y)$ ma rozkład $U(D)$, gdzie $D = \{(x,y): |x| + |y| \le 2\}$. Wyznaczyć rozkład zmiennej losowej $Z=g(X,Y)$

$g(x,y) = \ldots$

$P(Z=-1) = P(X<0 \vee Y<0) = \frac{|D_1|}{|D|} = \frac{3}{4}$
$P(Z=1) = P(X > 0 \wedge Y > 0) = \frac{1}{4}$
$P(Z = 0) = P(X=0, Y=0) = 0$

## Twierdzenie
$Z = g(X,Y)$

$$
F_Z(z) = P(Z \le z) = P(g(X,Y) \le z) = \ldots
$$

## Twierdzenie
Jeśli $\mathcal{X} = (X,Y) \sim N(m,C)$, $A$ jest macierzą $k \times 2$, $k=1,2$, $r(A) = k$, $b \in \mathbb{R}^k$ 

k-wymiarowa zmienna losowa $A\mathcal{X}+b$ ma rozkład normalny z parametrami

$$m^* = A\cdot m+b$$
$$C^* = ACA^T$$

to będzie na egzaminie!!

## Przykład 5.
Zmienna losowa $(X,Y)$ ma rozkład normalny taki, że $\ldots$
Wyznaczyć parametry rozkładu zmiennej losowej $Z=2X-3Y$ oraz wektora $(W,T) = (X+Y +1, 2X-3Y)$

# Warunkowe ...

## Rozkład warunkowy dyskretnych zmiennych losowych
Przy ustalonym $y$ wyznaczamy dla każdego $x\in S_X$
$$
P(X=x | Y=y) = \frac{P(X=x, Y=y)}{P(Y=y)}
$$

Otrzymamy funkcję prawdopodobieństw arozkładu warunkowe zmiennej losowej $X$ pod warunkiem zdarzenia $\{Y=y\}$

Przy ustalonym $y\in S_Y$ 
$$
\sum_x P(X=x  \ldots)
$$

