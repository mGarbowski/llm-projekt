# Rozkłady funkcji jednowymiarowych zmiennych losowych

## Twierdzenie
Jeśli $X \sim U([c,d])$ i $Y = aX + b$, gdzie $a \ne 0$, to

1. $a>0 \implies Y \sim U([c\cdot a + b, d \cdot a + b])$
2. $a<0 \implies Y \sim U([d \cdot a + b, c\cdot a + b])$

## Przykład 3.
Niech $T_f \sim U([95, 104])$ będzie temperaturą podaną w stopniach Fahrenheita. Wtedy $T_c = \frac{5}{9} \cdot (T_f - 32)$ jest temperaturą w stopniach Celsjusza, Wyznaczyć rozkład zmiennej losowej $T_c$

$$
T_c = \frac{5}{9}T_f - \frac{5}{9} \cdot 32
$$

$$
T_c \sim U([\frac{5}{9}\cdot 95 - \frac{5}{9} \cdot 32, \frac{5}{9}\cdot 104 - \frac{5}{9}\cdot 32])
$$

$$
T_c \sim U([35, 40])
$$

## Twierdzenie
Jeśli $X \sim N(m, \sigma^2)$ i $Y = aX+b$, gdzie $a \ne 0$, to
$$
Y \sim N(am+b, a^2\sigma^2)
$$
$$
EY = E(aX+b) = a\cdot EX + b = a\cdot m + b
$$
$$
VY = V(aX+b) = a^2 \cdot VX = a^2\sigma^2
$$

W szczególności, jeśli $Y = \frac{X-m}{\sigma}$

$$
Y \sim N(0, 1)
$$

## Przykład 4.
$$
X \sim N(-1, 9) \implies m=-1, \sigma = 9
$$
$$
Z = 3X -1
$$
$$
Z \sim N(3\cdot (-1) -1, 3^2 \cdot 9) = N(-4, 81)
$$

## Twierdzenie
Jeśli $X$ ma rozkład ciągły i $Y = g(X)$, to

$$
F_Y(y) ...
$$

## Przykład 5.
Niech $X \sim U([-1, 2])$. Wyznaczyć rozkład zmiennej losowej $Y=X^2$

$$
F_Y(y) = P(X^2 \le y)
$$
* dla $y < 0: 0$
* dla $0 \le y \le 1: P(-\sqrt{y} \le X \le \sqrt{y}) = \frac{2\sqrt{y}}{3}$
* dla $1 \le y \lt 4: P(-1 \le X \le \sqrt{y}) = \frac{\sqrt{y}+1}{3}$
* dla $y \ge 4: 1$

Zmienna losowa $Y$ ma rozkład ciągły o gęstości ...

## Generowanie liczb pseudolosowych o zadanym rozkładzie
Jeśli liczby $x_i$ zostały wylosowane zgodnie z rozkładem jednostajnym z przedziału $[0,1]$, to liczby $F^{-1}(x_i)$ można traktować jako liczby wylosowane zgodnie z rozkładem o dystrybuancie $F$.


Niech $F^{-1}(X)$ gdzie $F$ jesy jakąś dystrybuantą (funkcją rosnącą)

$$
F_Y(y) = P(Y \le y) = P(F^{-1}(X) \le y) = P(X \le F(y)) = F_X(F(y)) = F(y)
$$
# Zmienne losowe dwuwymiarowe

## Zmienna losowa dwuwymiarowa
Niech $X$ i $Y$ będą jendowymiarowymi zmiennymi losowymi. Parę $(X, Y)$ nazywamy **zmienną losową dwuwymiarową** (dwuwymiarowym wektorem losowym)

* Rozkład wektora $(X, Y)$ - **rozkład łączny**
* Rozkłady $X$ i $Y$ jako osobnych zmiennych losowych - **rozkłady brzegowe**

## Punkt skokowy
**Punktem skokowym** rozkładu wektora $X,Y)$ nazywamy każdą parę $(a,b) \in \mathbb{R}$, taką że ...

## Rozkład dyskretny
Zbiór wartości jest przeliczalny lub skończony.

## Nośnik
$S_{XY} \subset \mathbb{R}^2$ 

1. $P(X=x, Y=y) > 0$ dla każdego punktu w nośniku
2. prawdopodobieństwa sumują się do 1

## Funkcja prawdopodobieństwa
$$
p_{XY}(x,y) = P(X=x, Y=y)
$$

## Przykład 1.
Dwa rzuty niesymetryczną monetą $P(O)=1/3$
* X - liczba orłów w pierwszym rzucie
* Y - liczba orłów we wszystkich rzutach

$$
S_{XY} = \{ (0, 0), (0,1), (1,1), (1,2) \}
$$

$$p_{XY}(0,0) = P(R)^2 = (\frac{2}{3})^2$$
$$p_{XY}(0,1) = P(R)P(O) = \frac{2}{3} \cdot \frac{1}{3}$$
$$p_{XY}(1,1) = P(O)P(R) = \frac{2}{3} \cdot \frac{1}{3}$$
$$p_{XY}(1,2) = P(O)^2 = (\frac{1}{3})^2$$

Zazwyczaj przedstawia się rozkład w postaci tabeli

| X\Y | 0 | 1 | 2 |
|----|---|---|---|
|0|4/9|2/9|0|
|1|0|2/9|1/9|

## Twierdzenie
Zmienna losowa (X,Y) ma rozkład dyskretny wtedy i tylko wtedy gdy rozkłady brzegowe zmiennych X i Y też są dyskretne

1.  $S_{XY} \subseteq S_X \times S_Y$ 
2.  Dla każdego $x \in S_X$ $P(X=x) = \sum_yP(X=x, Y=y)$
3. Dla każdego $y\in S_Y$ $P(Y=y) = \sum_x P(X=x, Y=y)$

Sumuje się wiersze / kolumny tabeli