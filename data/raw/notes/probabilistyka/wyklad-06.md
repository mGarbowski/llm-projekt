# Rozkłady c.d.
Np. czas między kolejnymi wydarzeniami występującymi zgodnie z rozkładem Poissona.

$\lambda > 0, (X \sim exp(\lambda))$

$$
f_X(x) = \lambda \cdot e^{-\lambda x} \cdot 1_{[0, +\infty)}(x)
$$

$$
F_X(x) = (1-e^{-\lambda x} \cdot 1_{[0, +\infty)}(x)
$$

$$
EX = \frac{1}{\lambda}, VX = \frac{1}{\lambda^2}
$$

Rozkład wykładniczy jest ciągłym odpowiednikiem rozkładu geometrycznego

### Własność braku pamięci
Podobnie jak dla rozkładu geometrycznego

$$
P(X > t + s | X > t) = e^{-\lambda s} = P(X > s)
$$

## Związek z rozkładem Poissona
Jeśli zdarzenia określonego typu pojawiają się w przedziale czasowym $[0, t]$ zgodnie z rozkładem $P(\lambda_1)$, to czas między tymi zdarzeniami ma rozkład $exp(\lambda_2)$, gdzie $\lambda_1 = \lambda_2 \cdot t$

### Przykład 3.
Czas między zgłoszeniami do sieci wynosi $\lambda_2 = 1/2$ (średni czas między zgłoszeniami wynosi 2h). Obliczyć prawdopodobieństwo, że w ciągu 8 godzin będzie pracowało co najmniej 3 użytkowników

T - czas pomiędzy zgłoszeniami $T \sim exp(1/2) \implies ET = 2h$
X - liczba zgłoszeń w ciągu 8h $\lambda_1 = t \cdot \lambda_2 = 1/2 \cdot 8 = 4 \implies X \sim P(4)$

$$
S_X = \{1, 2, 3, \ldots \}
$$
$$
\forall_{k \in S_X} P(X=k) = \ldots
$$
$$
P(X \ge 3) = 1 - P(X < 3) = 1 - P(X = 0) - P(X = 1) - P(X = 2)
= 1 - e^{-4} - 4e^{-4} - 8e^{-4}
= 1 - 13e^{-4}
$$


## Rozkład normalny (Gaussa)
$\sigma > 0, X \sim N(m, \sigma^2)$ - trzeba zwrócić uwagę czy drugi parametr to std czy wariancja

$$
\frac{1}{\sqrt{2\pi} \cdot \sigma}\cdot exp(-\frac{(x-m)^2}{})
$$

Wykres jest symetryczny $P(X < m) = 1/2$
Im większe $\sigma$ tym bardziej spłaszczony wykres

### Standardowy rozkład normalny 
$$X \sim N(0, 1)$$
Dystrybuanta tego rozkładu pozwala policzyć prawdopodobieństwo dla każdego innego rozkładu normalnego

Dystrybuantę rozkaładu normalnego standardowego oznacza się $\Phi$

$$
\Phi(x) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^x exp(-\frac{1}{2}t^2)dt
$$
#### Własności
* $\Phi(0) = 1/2$
* $\Phi(-x) = 1 - \Phi(x)$

Dla $X \sim N(m, \sigma^2)$ i dowolnego $a \in \mathbb{R}$
$$F_X(a) = \Phi(\frac{a-m}{\sigma})$$

### Twierdzenie o trzech sigmach
Dla $X \sim N(m, \sigma^2)$

$$P(X \notin [m-3\sigma, m+3\sigma]) = 0.0026$$

Prawie wszystkie wartości $X$ są nie dalej niż $3\sigma$ od średniej

Dowód

$$
P(m - 3\sigma \le X \le m + 3\sigma) 
= F_X(m+3\sigma) - F_X(m-3\sigma)
= \Phi(\frac{m + 3\sigma  - m}{\sigma}) - \Phi(\frac{m-3\sigma -m}{\sigma})
= \Phi(3) - \Phi(-3) 
= \Phi(3) - 1 + \Phi(3) 
= 2 \Phi(3) - 1
\simeq 2 \cdot 0.9987 - 1
$$

## Rozkład jednostajny

$$X \sim U[a, b]$$
$$
f_X(x) = \frac{1}{b-a} \cdot 1_{[a, b]}(x)
$$


$$F_X(s) = \ldots$$

$$EX = \frac{a+b}{2}, VX=\frac{(b-a)^2}{12}$$

Gęstość nie jest ciągła, a dystrybuanta jest

### Twierdzenie
$$
P(X \in [c,d]) = \frac{|[a,b] \cap [c,d]|}{b-a}
$$

# Rozkłady funkcji jendowymiarowych zmiennych losowych

## Twierdzenie
Jeśli $X$ jest zmienną losową o rozkładzie dyskretnym, to zmienna losowa $Y=g(X)$ ma rozkład dyskretny oraz

$$
S_Y = g(S_X), P(Y=y)= \sum_{x\in S_X: g(x)=y} P(\ldots)
$$

## Przykład 1.
Niech $X$ będzie zmienną losową o rozkładzie dyskretnym $S_X=\{-4, -3, \ldots, 3, 4\}$
oraz P(X=x) = 1/9
Wyznaczyć rozkłład zmiennej losowej $Y = |X|$

$$S_Y = \{0, 1, 2, 3, 4\}$$
$$P(Y=0) = P(|X| = 0) = P(X=0) = \frac{1}{9}$$

$$
\forall_{k \in \{1, 2, 3, 4\}} P(Y=k) 
= P(|X| = k) 
= P(X=k) + P(X=-k)
= \frac{2}{9}
$$

Jeśli $X$ ma rozkład ciągły, to zmienna losowa $g(X)$ wcale nie musi mieć rozkładu ciągłego

## Przykład 2.
...