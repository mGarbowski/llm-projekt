# (2023-10-26)

## Rozkład ciągły c.d.

Gęstość prawdopodobieństwa nie jest prawdopodobieństwem, nie musi być ograniczona do $[0,1]$

Gęstość pozwala łatwo odczytać nośnik

Nośnik - $\{ x \in \mathbb{R}: f_X(x) > 0\}$ 

## Przykład
$$
F_X(t) = \int_{-\infty}^t(x)dx
$$

$$
0 \le t < 1: \int_{-\infty}^0 0dx + \int_0^t xdx = \frac{1}{2}t^2
$$

# Wartość oczekiwana
## Przykład 1
Rzucamy 1 raz kostką sześcienną. Jaka będzie średnia liczba oczek?

$X$ - liczba oczek
$S_X = \{1, 2, 3, 4, 5, 6 \}$
$\forall_{k \in S_X} P(X=k) = \frac{1}{6}$

$$
EX = \sum_{k \in S_X} k \cdot P(X=k)
$$

## Definicja
Niech X będzie jednowymiarową zmienną losową o rozkładzie dyskretnym. Jeśli szereg 
$$
\sum_{x_i \in S_X} |x_i| \cdot P(X=x_i)
$$
jest zbieżny, to wartością oczekiwaną zmiennej losowej X nazywamy liczbę
$$
EX = \sum_{x_i \in S_X} x_i \cdot P(X=x_i)
$$
Jeśli szereg $\sum_{x_i \in S_X} |x_i| \cdot P(X=x_i)$ nie jest zbieżny to mówimy, że $EX$ nie istnieje.

Jeśli w zadaniu nie jest powiedziane że trzeba sprawdzić to zakładamy że szereg jest zbieżny

## Przykład 2
$$S_X = \{-60, 10, 50 \}$$
$$
EX = -60 \cdot \frac{1}{2} + 10 \cdot \frac{1}{3} + 50 \cdot \frac{1}{6} = -\frac{55}{3}
$$

Gra jest niekorzystna (dla gracza)

## Definicja dla rozkładu ciągłego
$$
EX = \int_{-\infty}^{+\infty}x \cdot f(x)dx
$$

## Przykład 3
Niech $T$ oznacza czas oczekiwania na autobus mający przyjechać w ciągu godziny. Ile średnio czasu będziemy czekać?

$$ \Omega = [0, 1] $$
$$ T(\omega) = \omega $$
$$
T^{-1}((-\infty, t]) = 
$$
$$
=\varnothing, t < 0
$$
$$=[0, t], 0\le t < 1$$
$$=[0,1] = \Omega, t \ge 1$$

Prawdopodobieństwo geometryczne

$$
f_T(t) = \frac{d}{dt} F_T(t)
$$

$$
ET = \int_{-\infty}^{+\infty} t \cdot f_T(t) dt 
= \int_{0}^{1} t \cdot f_T(t) dt
= \int_{0}^{1} t \cdot 1 dt
= \frac{1}{2}
$$

## Uwaga
Przypuśćmy, że $X$ oznacza pewną cechę populacji. Z tej populacji losujemy próbę n-elementową otrzymując wyniki $x_1 \ldots x_n$, gdzie $x_i$ oznacza wartość cechy $X$ dla i-tego elementu. Wtedy wartość średnią dla wylosowanej próby oznaczamy symbolem $\bar{x}$

$$\bar{x} = \frac{1}{n} \cdot \sum_{i=1}^n x_i$$

Tak wyznaczona średnia jest dobrym oszacowaniem wartości oczekiwanej dla całej populacji.

$EX$ jest wartością średnią dla populacji, $\bar{x}$ dla próby.

## Własności
* $E(b) = b$
* $E(a \cdot X) = a \cdot EX$
* $E(X + Y) = EX + EY$
* Jeśli $X \ge 0$, to $EX \ge 0$

Niech g będzię funkcją taką że g(X) jest zmienną losową jednowymiarową

$$
E(g(x)) = \sum_{x_i \in S_X} g(x_i) \cdot P(X=x_i)
$$
$$
E(g(X)) = \int_{-\infty}^{+\infty} g(x) \cdot f_X(x)dx
$$

## Przykład 4
$$
Y = g(X) = max(1, X)
$$

X ma rozkład ciągły więc 
$$
EY = E(g(x)) = \int_0^1 1 \cdot \frac{1}{2}dx + \int_1^2 x \cdot \frac{1}{2}dx
= \frac{1}{2} + \frac{1}{4} \cdot 3
= \frac{5}{4}
$$

Średnie odchylenie nie ma dobrych własności analitycznych, zamiast średniego analizuje się zwykle odchylenie standardowe

## Wariancja i odchylenie standardowe
### Wariancja
$$
VX = E[(X-EX)^2]
$$
### Odchylenie standardowe
$$
\sigma_X = \sqrt{VX}
$$

Zazwyczaj odchylenie standardowe przyjmuje zbliżone wartości do odchylenia średniego $E|X-EX|$
