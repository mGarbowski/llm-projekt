## Zbiór zdarzeń elementarnych
Zbiór wszystkich możliwych wyników doświadczenia losowego

## Zdarzenie losowe
Dowolny podzbiór zbioru zdarzeń elementarnych

Niech $F$ będzie rodziną wszystkich zdarzeń losowych
* $\Omega \in F$ - zdarzenie pewne
* $\varnothing \in F$ - zdarzenie niemożliwe
* $A' = \Omega - A$ - zdarzenie przeciwne do $A$
* Jeśli $A, B \in F$ to $A \cup B \in F$, $A \cap B \in F$, $A- B \in F$

## Aksjomaty Kołmogorowa
Prawdopodobieństwo - funkcja $P: F \rightarrow [0; \inf)$
* $P(\Omega)=1$
* Dla każdego przeliczalnego ciągu rozłącznych zdarzeń $P(\bigcup_{i=1}^{\infty}A_i) = \sum^{\infty}_{i=1} P(A_i)$


## Własności prawdopodobieństwa
* Jeśli zdarzenie jest niemożliwe to jego prawdopodobieństwo wynosi $0$ (implikacja tylko w jedną stronę)
* $P(\varnothing) = 0$
* $P(A\cup B) = P(A) + P(B) - P(A \cap B)$
* Wzór włączeń i wyłączeń $$
P(A_1 \cup A_2 \cup ... \cup A_n) = \sum^n_{i=1}P(A_i) - \sum_{1 \le i \le j \le n}P(A_i \cap A_j) + ... + (-1)^{n+1} P(A_1 \cap ... \cap A_n)
$$
* $$
P(A') = 1 - P(A)
$$
* $$
P(A - B) = P(A) - P(A \cap B)
$$
* $$
A \subset B \implies P(A) \le P(B) 
$$
* Dla każdego zdarzenia losowego $A$: $0 \le P(A) \le 1$

## Przestrzeń probabilistyczna
Trójka $(\mathcal{F}, \Omega, P)$

## Klasyczna definicja prawdopodobieństwa
Pierre Simon de Laplace

Założenia
* $\Omega = {w_1, w_2, w_N}$ - zbiór skończony złożony z N elementów
* wszystkie zdarzenia są jednakowo prawdopodobne $P(\{w_k\}) = 1/N$ dla każdego $k = 1, 2, ... N$

Dla każdego zdarzenia losowego $A$ 
$$
P(A) = \frac{|A|}{|\Omega|}
$$

## Przykład
Rzucamy 10 razy symetryczną monetą. Ile wynosi prawdopodobieństwo, że dokładnie 3 razy wypadnie orzeł?

$$
\Omega = \{(x_1, x_2, ..., x_{10}): x_i \in \{O, R\}\}
$$
$$
|\Omega| = 2^{10} = 1024
$$
$$
A = \{(OOORRRRRRR), ...\}
$$
$$
|A| = \frac{\binom{10}{3}}{2^{10}}
$$


## Prawdopodobieństwo dla przeliczalnego zbioru zdarzeń elementarnych
$$
P(A) = \sum_{i, w_i \in A} P(\{w_i\})
$$

## Przykład
Rzucamy niesymetryczną monetą, dla której prawdopodobieństwo wyrzucenia orła wynosi $\frac{1}{3}$ do momentu wypadnięcia pierwszego orła. Obliczyć prawdopodobieństwo, że liczba rzutów będzie nieparzysta.

Zbiór zdarzeń elementarnych jest przeliczalny, nie obowiązuje klasyczna definicja gdzie każdy element $\Omega$ musi być jednakowo prawdopodobny.

$$
\Omega = \{O, RO, RRO, \ldots \}
$$
$$
A = \{w_1, w_3, w_5, \ldots \}
$$
$$
P(A) = P(\{w_1\}) + P(\{w_3\}) + \ldots = 
\frac{1}{3} + (\frac{2}{3})^2 \frac{1}{3} + (\frac{2}{3})^4 \frac{1}{3} + \ldots =
\sum^{\infty}_{k=0} (\frac{2}{3})^{2k}\frac{1}{3} = 0.6
$$

## Geometryczna definicja prawdopodobieństwa
Niech $A \subset \mathbb{R}^n$
Niech $|A|$ (miara Lebsgue'a) będzie określone jako
* długość dla $n=1$
* pole dla $n=2$
* objętość dla $n=3$

$$
P(A) = \frac{|A|}{|\Omega|}
$$


## Przykład
Dwie osoby X i Y...

$\Omega = \{(x, y): 0 < x < 1 \wedge 0 < y < 1\}$  - kwadrat
$|\Omega| = 1$ - pole kwadratu
$A = \{(x,y) \in \Omega: |x-y| < \frac{1}{3}$\}
$y < x + \frac{1}{3} \wedge y > x - \frac{1}{3}$

(rysunek)

$|A| = 1 - (\frac{2}{3})^2 = \frac{5}{9}$ - pole wycinka kwadratu
$P(A) = \frac{\frac{5}{9}}{1}$

Zdarzenie prawie niemożliwe $P(0)$
