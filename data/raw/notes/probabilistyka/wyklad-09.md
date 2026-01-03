## Niezależność zmiennych losowych
Dla wszystkich zbiorów $B_1, B_2 \subset \mathbb{R}$ zachodzi

$$
P(X \in B_1, Y \in B_2) = P(X \in B_1) \cdot P(Y \in B_2)
$$

Zmienne losowe są zależne kiedy nie są niezależne

### Twierdzenie
Zmienne X i Y są niezależne $\iff$ dla wszystkich $x, y \in \mathbb{R}$
$$F_{XY}(x, y) = F_X(x) \cdot F_Y(y)$$

### Twierdzenie
Zmienne losowe X i Y o rozkładach dyskretnych są niezależne wtedy i tylko wtedy gdy
* $S_{XY} = S_X \times S_Y$
* Dla każdego $(x,y) \in S_{XY}$ $P(X=x, Y=y) = P(X=x) \cdot P(Y=y)$


## Niezalezność zmiennych losowych o łącznym rozkładzie ciągłym
$$
f_{XY}(x,y) = f_X(x) \cdot f_Y(y)
$$

### Przykład 4
$D$ - Trójkąt ze slajdów

$f_{XY}(x,y) = \frac{1}{4} \cdot \mathbb{1}_D(x,y)$ 

$f_X(x) = \int_{-\infty}^\infty f_{XY}(x,y) dy$

$D = \{ (x,y): -2 \le x \le 2, 0 \le y \le 2 - |x| \}$
$D = \{ (x,y): 0 \le y \le 2, y-2 \le x \le 2-y \}$

$$
f_X(x) = \int_0^{2-|x|} 1/4 dy \cdot \mathbb{1}_{[-2,2]}(x) 
= \frac{1}{4} \cdot (2-|x|) \cdot \mathbb{1}_{[-2,2]}(x)
$$

$$
f_Y(y) = \int_{y-2}^{2-y} \frac{1}{4}dx \cdot \mathbb{1}_{[0,2]}(y)
= \frac{1}{4} \cdot (2-y - (y-2)) \cdot \mathbb{1}_{[0,2]}(y)
= \frac{1}{2} \cdot (2-y) \cdot \mathbb{1}_{[0,2]}(y)
$$

$$
f_X(x) \cdot f_Y(y) = \frac{1}{4}(2-|x|) \cdot \frac{1}{2}(2-y) \cdot \mathbb{1}_D(x,y)
$$

$$f_X \cdot f_Y \ne f_{XY}$$
Widać że nie są równe bo nośnik $S_{XY}$ jest trójkątem a nośnik $S_X \times S_Y$ jest prostokątem

### Twierdzenie
Jeśli $X$ i $Y$ są niezależne to $g_1(X)$ i $g_2(Y)$ też są niezależne

## Dwuwymiarowy rozkład jednostajny
Zmienna losowa $(X,Y)$ ma rozkład jednostajny w obszarze $D \subset \mathbb{R}^2$ takim, że $|D| \le \infty$, $|D| \ne 0$, jeśli dla każdego punktu

$$
f_{XY} = \frac{1}{|D|} \cdot \mathbb{1}_D
$$

### Twierdzenie
Jeśli $(X,Y)$ ma rozkład jednostajny w obszarze D to dla dowolnego $A \subset \mathbb{R}^2$

$$
P((X,Y) \in A) = \frac{|A \cap D|}{|D|}
$$

### Przykład 5
Wektor $(X,Y)$ ma rozkład jednostajny w zbiorze $D = [-1,1] \times [0,1]$. Wyznaczyć gęstości brzegowe i sprawdzić, czy zmienne losowe $X$ i $Y$ są niezależne.

$$f_{XY}(x,y) = \frac{1}{2} \cdot \mathbb{1}_D(x,y)$$

$$
f_X(x) = \int_0^1\frac{1}{2}dy \cdot \mathbb{1}_{[-1,1]}(x) 
= \frac{1}{2} \cdot \mathbb{1}_{[-1,1]}(x)
\implies X \sim U([-1,1])
$$

$$
f_Y(y) = \int_{-1}^1\frac{1}{2}dx \cdot \mathbb{1}_{[0,1]}(y)
= \mathbb{1}_{[0,1]}(y)
\implies Y \sim U([0,1])
$$

$$
f_X(x)f_Y(y) = \frac{1}{2} \cdot \mathbb{1}_{[-1,1]}(x) \cdot \mathbb{1}_{[0,1]}(y)
= \frac{1}{2} \cdot \mathbb{1}_D(x, y)
= f_{XY}(x,y)
$$

Zmienne $X$ i $Y$ są niezależne

### Twierdzenie
Wektor $(X,Y)$ ma rozkład jednostajny w prostokącie $[a,b] \times [c,d]$ wtedy i tylko wtedy gdy
* $X$ i $Y$ są niezależne
* $X$ ma rozkład jednostajny w przedziale $[a,b]$, a $Y$ ma rozkład jednostajny w $[c,d]$


## Dwuwymiarowy rozkład normalny
Zmienna losowa $(X,Y)$ ma rozkład normalny z parametrami $m \in \mathbb{R}^2$ i $C$ jest symetryczną macierzą kwadratową stopnia $2$, dodatnio określoną, jeśli dla każdego $(x,y) \in \mathbb{R}^2$

$$
f_{XY}(x,y) = \ldots
$$

Kowariancja

$$c_{12} = c_{21} = \rho\sigma_1\sigma_2$$ gdzie $\rho$ to współczynnik korelacji

* $m_1 = EX$
* $m_2 = EY$
* $c_{11} = VX$
* $c_{22} = VY$


### Twierdzenie
Jeżeli $(X,Y) \sim N(m, C)$ to

* $X$ i $Y$ są niezależne $\iff \rho = 0$
* $X \sim N(m_1, \sigma_1^2)$ i $Y \sim N(m_2, \sigma_2^2$)