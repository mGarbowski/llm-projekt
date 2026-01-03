## Gęstość rozkładu warunkowego
Gęstość rozkładu warunkowego zmiennej losowej $X$ pod warunkiem zdarzenia $\{Y=y\}$

Dla $f_Y(y) \ne 0$
$$
f(x|y) = \frac{f_{XY}(x,y)}{f_Y(y)}
$$
$0$ w p. p.

### Przykład 2.
Rozkład jednostajny w obszarze $D = \{(x,y): |x| + |y| < 2\}$
Wyznaczyć gęstość Y pod warunkeim $\{X=x\}$

$$
f_{XY}(x,y) = \frac{1}{8} \cdot \mathbb{1}_D(x,y)
$$

$$
f_X(x) 
= \int_{-\infty}^\infty f_{XY}(x,y)dy 
= \int_{|x|-2}^{2-|x|} \frac{1}{8}dy \cdot \mathbb{1}_{[-2,2]}(x) 
= \frac{1}{8}(4-2|x|) \cdot \mathbb{1}_{[-2,2]}(x)
$$

Dla $y \in [|x| -2, 2-|x|]$, gdzie $x \in (-2, 2)$
$$
f(y|x) 
= \frac{\frac{1}{8}}{\frac{1}{8}(4-2|x|)}
= \frac{1}{4-2|x|}
$$
$0$ w p. p.

To jest funkcja jednej zmiennej $y$, $x$ to stała z przedziału $(-2,2)$

## Warunkowa wartość oczekiwana
Zmiennej losowej $X$ pod warunkiem zdarzenia $\{Y=y\}$

Kiedy $(X,Y)$ ma rozkład dyskretny
$$
E(X|Y=y) = \sum_{x \in S_X} x \cdot P(X=x|Y=y)
$$

Kiedy $(X,Y)$ ma rozkład ciągły
$$
E(X|Y=y) = \int_{-\infty}^{\infty} x \cdot f(x|y) dx
$$

Można to rozumieć tak, że $E(X|Y=y)$ jest średnią wartością przyjmowaną kiedy $Y=y$
albo można to rozumieć jako funkcję od $y$

### Przykład
Gęstość z poprzedniego przykładu

$$
E(Y|X=x) 
= \int_{-\infty}^\infty y \cdot f(y|x)dy 
= \int_{|x|-2}^{2-|x|} y \cdot \frac{1}{4-2|x|} dy
= \frac{1}{4-2|x|} \cdot \frac{1}{2}[y^2]|^{2-|x|}_{|x|-2}
= 0
$$

### Przykład 3.
Wektor $(X,Y)$ ma rozkład ciągły o gęstości

$$
f(x,y) = 21x^2y^3 \cdot \mathbb{1}_D(x,y)
$$
$$
D = \{(x,y): 0 < x < y < 1\}
$$
(D jest trójkątem)
Wyznaczyć $h_1(x) = E(Y|X=x)$ i $h_2(y) = E(X|Y=y)$

$$
f_X(x) 
= \int_{-\infty}^{\infty}f_{XY}(x,y)dy 
= \int_x^1 21x^2y^3dy \cdot \mathbb{1}_{(0,1)}(x)
= 21x^2 \cdot \frac{1}{4} \cdot y^4|^1_x \cdot \mathbb{1}_{(0,1)}(x)
= 21x^2\cdot \frac{1}{4} \cdot (1-x^4) \cdot \mathbb{1}_{(0,1)}(x)
$$

Dla $y \in (x,1)$, kiedy $x \in (0,1)$
$$
f(y|x) = \frac{4y^3}{1-x^4}
$$
$$
h_1(x) = E(Y|X=x) = \int_x^1 y \cdot \frac{4y^3}{1-x^4} dy
= \frac{4}{1-x^4} \cdot \frac{1}{5} y^5|_x^1
= \frac{4}{5} \frac{1-x^5}{1-x^4}
$$

$h_2(y) = 3/4y$ jest rozwiązaniem zagadnienia minimalizacji wartości oczekiwanej $E(X-h(Y))^2$

## Wariancja rozkładu warunkowego
zmiennej losowej $X$ pod warunkeim zdarzenia $\{Y=y\}$

$$
V(X|Y=y) = E(X^2|Y=y) - (E(X|Y=y))^2
$$

## Dystrybuanta rozkładu warunkowego
Niech $B$ będzie zdarzeniem takim, że $P(B) > 0$. 
Dystrybuanta rozkładu warunkowego zmiennej losowej $X$ pod warunkiem zdarzenia $B$ to funkcja $F: \mathbb{R} \rightarrow [0,1]$

$$
F(x|B) = P(X \le x | B) = \frac{P((X \le x) \cap B)}{P(B)}
$$

### Przykład 4.
Wektor $(X,Y)$ ma rozkład jednostajny w zbiorze $D=\{(x,y) : -2 \le x \le 2, 0 \le y \le 2-|x|\}$

Wyznaczyć dystrybantę rozkładu warunkowego zmiennej losowej $X$ pod warunkiem zdarzenia $\{Y \le 1\}$.

$D$ to trójkąt


$$
P(Y \le 1) = \int \int_A f_{XY}(x,y)dxdy = \frac{1/2(4+2)\cdot 1}{4} = \frac{3}{4}
$$

$$
F(x|Y \le 1) = P(X \le x | Y \le 1)
= \frac{P(X \le x \wedge  Y \le 1)}{P(Y \le 1)}
= \frac{4}{3} \cdot P(X \le x \wedge  Y \le 1)
$$

$0$ dla $x < -2$
$\frac{4}{3} \cdot \frac{1/2(x+2)^2}{4} = \frac{1}{6}(x+2)^2$ dla $x \in [-2, -1)$
$1/6(2x+3)$ dla $x \in [-1, 1)$
dla $x \in [1, 2)$
1 dla $x \ge 1$
