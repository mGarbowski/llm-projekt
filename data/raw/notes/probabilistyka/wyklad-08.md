# Wykład 8 (2023-11-20)

## Dystrybuanta dwuwymiarowa zmiennej $(X,Y)$ 
$$
F_{XY}: \mathbb{R}^2 \rightarrow [0,1]
$$

$$F_{XY}(x,y) = P(X \le x, Y \le y)$$

Warunek $(X\le x, Y \le y)$ wyznacza ćwiartkę płaszczyzny

1. Dystrybuanta jednoznacznie wyznacza rozkład
2. $(x,y) \in S_{XY} \implies F_{XY}$ jest nieciągła w punkcie $(x,y)$
3. Nie każdy punkt nieciągłości jest punktem skokowym (nie zachodzi implikacja w drugą stronę)

Dla dyskretnego rozkładu łącznego - sumujemy prawdopodobieństwa punktów należących do ćwiartki

### Twierdzenie
Dla dowolnych $x_1 < x_2, y_1 < y_2$ zachodzi równość:

$$
P(x_1 \lt X \le x_2, y_1 \lt Y \le y_2) 
= F(x_2, y_2) - F(x_1, y_2) - F(x_2, y_1) + F(x_1, y_1)
\ge 0
$$

(łatwo wyprowadzić z rysunku)

### Twierdzenie
$F: \mathbb{R}^2 \rightarrow [0,1]$ jest dystrybuantą dwuwymiarową $\iff$ 
* $F$ jest prawostronnie ciągła po współrzędnych
* $\forall_{x_1 \lt x_2, y_1 \lt y_2} F(x_2, y_2) - F(x_1, y_2) - F(x_2, y_1) + F(x_1, y_1)\ge 0$ 
* $\forall_{x \in \mathbb{R}} lim_{y \rightarrow -\infty} F(x,y) = 0$
* $\forall_{y \in \mathbb{R}} lim_{x \rightarrow -\infty} F(x,y) = 0$
* $lim_{x,y \rightarrow +\infty} F(x,y) = 1$

### Uwaga
$$P(X \lt x, Y \le y) = F(x^-, y) = lim_{t \rightarrow x^-}F(t,y)$$
$$P(X \le x, Y \lt y) = F(x, y^-)$$
$$P(X \lt x, Y \lt y) = F(x^-, y^-) = lim_{(s,t) \rightarrow (x,y)^-} F(s,t)$$
$$P(X=a, Y=b) = F(a,b) - F(a^-,b) - F(a,b^-) + F(a^-,b^-)$$

### Dowód
$$
\{X=a, Y=b\}
=\{ X \le a, Y\le b \} - (\{ X \le a, Y \lt b\} \cup \{ X \lt a, Y \le b\})
$$

$$
P(X=a, Y=b) = F(a,b) - P(\{X \le a, Y \lt b\} \cup \{ X \lt a, Y \le b \})
= F(a,b) - F(a^-,b) - F(a,b^-) + F(a^-,b^-)
$$

## Przejście z rozkładu łącznego do brzegowego
Niech $(X,Y)$ będzie dwuwymiarową zmienną losową o dystrybuancie $F_{XY}$, wówczas

$$F_X(x) = lim_{y \rightarrow +\infty}F(x,y)$$
$$F_Y(y) = lim_{x \rightarrow +\infty}F(x,y)$$

## Dwuwymiarowy rozkład ciągły
Dwuwymiarowa zmienna losowa $(X,Y)$ ma rozkład ciągły, jeśli istnieje funkcja $f_{XY}: \mathbb{R}^2 \rightarrow \mathbb{R}$ zwana gęstością zmiennej $(X,Y)$ taka, że 

$$
\forall_{x,y} F_{XY}(x,y) = \int_{-\infty}^x [\int_{-\infty}^yf_{XY}(t,s) ds] dt
$$
Wtedy nośnikiem wektora $(X,Y)$ jest zbiór $S_{XY} = \{ (x,y): f_{XY} \gt 0\}$

### Twierdzenie
Funkcja $f: \mathbb{R}^2 \rightarrow \mathbb{R}$ jest gęstością dwuwymiarowej zmiennej losowej $(X,Y) \iff$
* $f(x,y) \ge 0$ prawie wszędzie (poza zbiorem o zerowej mierze)
* $\int_{-\infty}^\infty \int_{-\infty}^\infty f(x,y)dxdy = 1$

### Twierdzenie
Jeżeli $f: \mathbb{R}^2 \rightarrow \mathbb{R}$ jest gęstością zmiennej $(X,Y)$ to

$$\frac{\partial^2 F(x,y)}{\partial x \partial y} = f(x,y)$$
$$
P((x,y) \in A) = \int \int_A f(x,y)dxdy
$$
Prawdopodobieństwo to objętość bryły o podstawie $A$, ograniczonej z góry wykresem $f$

### Twierdzenie
Jeżeli zmienna $(X,Y)$ ma rozkład ciągły o gęstości $f_{XY}$ to rozkłady brzegowe $X$, $Y$ to gęstości rozkładów brzegowych też są ciągłe i

$$f_X(x) = \int_{-\infty}^\infty f_{XY}(x,y)dy$$
$$f_Y(y) = \int_{-\infty}^\infty f_{XY}(x,y)dx$$

(ale nie w drugą stronę)

## Przykład
$(X,Y) \sim f(x,y) = a \cdot \mathbb{1}_D(x,y)$ 
$D$ - trójkąt o wierzchokach $(-2,0), (0,2), (2,0)$
Wyznaczyć stałą $a$, rozkłady brzegowe i policzyć prawdopodobieństwo $P(Y>X)$

$a \ge 0$
$\int_{-\infty}^\infty \int_{-\infty}^\infty f(x,y)dxdy = a \cdot \int \int_D dxdy = a \cdot |D| = 4a = 1$
$a = 1/4$

$S_{XY} = D$
$S_X = [-2,2]$
$S_Y = [0,2]$

$$
f_X(x) = \mathbb{1}_{[-2,2]} \cdot \int_0^{2-|x|} \frac{1}{4}dy
$$

$$
f_Y(y) = \mathbb{1}_{[0,2]} \cdot \int_{y-2}^{2-y} \frac{1}{4}dx
$$
$$
P(Y>X) = \int \int_{Y>X} f(x,y)dxdy = \frac{3}{4}
$$
