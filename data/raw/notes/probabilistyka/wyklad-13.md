# Prawa wielkich liczb (2024-01-08)

Załóżmy że wykonujemy $n$ doświadczeń w schemacie Bernouliego z prawdopodobieństwem sukcesu $p$. Doświadczenie można opisać przez ciąg zmiennych losowych $X_1, \ldots, X_n$, gdzie $X_i$ ma wartość $1$ jeśli w $i$-tej próbie był sukces, $0$ w przeciwnym razie

$$
S_n = \sum_{i=0}^n X_i
$$
## Słabe Prawo Wielkich Liczb Bernouliego
Niech $S_n$ będzie liczbą sukcesów w $n$ doświadczeniach w schemacie Bernouliego. Dla każdego $\epsilon > 0$

$$
lim_{n\rightarrow \infty}(|\frac{S_n}{n}-p| \le \epsilon) = 1
$$

## Mocne Prawo Wielkich Liczb Kołomogorwoa
Niech $(X_i)_{i=1}^n$ będzie ciągiem niezależnych zmiennych losowych o tym samym rozkładzie. Wtedy $\frac{1}{n} \sum_{i=1}^nX_i$ dąży z prawdopodobieństwem $1$ do $EX$

### Wnioski
Niech $X_1, \ldots, X_n$ będzie próbą $n$-elementową wylosowaną z rozkładu o wartości oczekiwanej $m$ i warwiancji $\sigma^2$.

Średnia z próby $\bar{X} = \frac{1}{n}\sum_{i=1}^nX_i$ dąży z prawdopodobieństwem $1$ do $EX=m$
Średnia z próby jest dobrym oszacowaniem wartości średniej dla całej populacji

Wariancja z próby $S^2 = \frac{1}{n-1} \sum_{i=1}^n(X_i-\bar{X})^2$ dąży z prawdopodobieństwem $1$ do wariancji populacji $VX$
Wariancja z próby jest dobrym oszacowaniem wariancji dla całej populacji

## Obliczanie całki oznaczeonej metodą Monte-Carlo
Niech $X_1, \ldots, X_n$ będą niezależnymi zmiennymi losowymi o rozkładzie jednostajnym w przedziale $[a,b]$ Niech $f$ będzie taką funkcją, że istnieje $E(f(X_1))$.
Wtedy zmienne losowe $f(X_1), \ldots, f(X_n)$ roœnież są niezależne, wszystkie mają ten sam rozkład i 

$$
E(f(X_q)) = \int_a^b f(x) \cdot \frac{1}{b-a}dx = \frac{1}{b-a} \int_a^bf(x)dx
$$

Z MPWL Kołomogorowa wynika że $\frac{1}{n}\sum_{i=1}^nf(X_i)$ dąży z prawdopodobieństwem $1$ do $E(f(X_1))$

### Algorytm
1. Losujemy niezależne liczby $u_1, \ldots, u_n$ z rozkładu $U([0,1])$
2. Stosujemy przekształcenie $x_i = a + (b-a)u_i$
3. ...

## Centralne twierdzenie graniczne
Niech $X_1, \ldots, X_n$ będzie próbą losową pochodzącą z populacji (niezależne zmienne losowe o tym samym rozkładzie), w której cecha $X$ ma znaną wartość średnią $m$ oraz znane odchylenie standardowe $\sigma$.

$$
E\bar{X} = E(\frac{1}{n}\sum_{i=1}^nX_i) 
= \frac{1}{n} \sum_{i=1}^n EX_i 
= \frac{1}{n} \sum_{i=1}^n m 
= \frac{1}{n} \cdot m \cdot n = m
$$

$$
V\bar{X} = V(\frac{1}{n}\sum_{i=1}^n X_i) 
= \frac{1}{n^2} \sum_{i=1}^n\sigma^2
= \frac{1}{n^2} \cdot n \cdot \sigma^2
= \frac{\sigma^2}{n}
$$

Jeśli próba losowa $X_1, \ldots, X_n$ pochodzi z populacji, gdzie $X \sim N(m,\sigma^2)$ to

$$
\bar{X} \sim N(m, \frac{\sigma^2}{n})
$$

## Centralne Twierdzenie Graniczne Lindenberga-Levy'ego
Niech $X_1, \ldots, X_n$ będą niezależnymi zmiennymi losowymi o tym samym rozkładzie, mającymi wartość oczekiwaną $m$ i wariancię $\sigma^2$. Wtedy zmienna losowa $\bar{X}$ dla dużych $n$ ma w przybliżeniu rozkład

$$
\bar{X} \sim N(m, \frac{\sigma^2}{n})
$$

### Wnioski z CTG
* Dla dużych $n$ zmienna losowa $Y_n = X_1 + \ldots + X_n$ ma w przybliżeniu rozkład $N(nm, n\sigma^2)$
* Dla dużych $n$ zmienna losowa $\frac{Y_n - nm}{\sigma\sqrt{n}}$ ma w przybliżeniu rozkład $N(0,1)$

## Kwantyl
Kwantylem rzędu $\alpha$ zmiennej losowej X o rozkładzie ciągłym nazywamy liczbę $x_\alpha$, dla której

$$
P(X \le x_\alpha) = F_X(x_\alpha) = \alpha
$$

Jeżli $X \sim N(0,1)$ to kwantyl rzędu $\alpha$ ...


### Przykład
Trasa wyścigu kolarskiego liczy 192km. Czas przejazdu 1km jest zmienną losową o rozkładzie $U([1.5min, 1.9min])$. Czasy przejazdu poszczególnych kilometrów są od siebie niezależne.

* Ile procent kolarzy przejeżdża trasę wyścigu w czasie dłuższym niż $322min$?
* Po jakim czasie będzie na mecie $90\%$ zawodników?

$Y_{192} = \sum_{k=1}^{192}X_k$ - czas przejazdu całego wyścigu

$X_k \sim U([1.5,1.9]) \implies m = 1.7, \sigma^2 = \frac{0.4^2}{12}$
$Y_{192}$ ma w przybliżeniu rozkład $N(192 \cdot 1.7, 192 \cdot \frac{0.4^2}{12})$

$$
P(Y > 322) = 1 - P(Y_{192} \le 322)
\simeq 1 - \phi(\frac{322-326.4}{4\cdot0.4})
$$

$$
P(Y_{192} \le t) = 0.9 \implies
\phi(\frac{t-326.4}{1.6}) = 0.9
\implies z_{0.9} = \frac{t-326.4}{1.6}
$$
## Centralne Twierdzenie Graniczne Moivre'a-Laplace'a
Niech $X_1, \ldots, X_n$ będą niezależnymi zmiennymi losowymi o tym samym rozkładzie takim, że
$$
P(X_i=1) = p \in (0,1), P(X_i=0)=1-p
$$

...