# Wprowadzenie do teorii sygnałów
Sygnały i Systemy - Wojciechowski

## Sygnał
Sygnał to wielkość fizyczna zmieniająca się w czasie

### Podział
* Ze względu na naturę zjawiska
	* deterministyczne - opisywane wzorem matematycznym
	* stochastyczne (losowe) - opisywane rachunkiem prawdopodobieństwa
* Ze względu na wymiar
	* jednowymiarowe
	* wielowymiarowe
* Ze względu na dziedzinę
	* czasu ciągłego
	* czasu dyskretnego
* Ze względu na zbiór wartości
	* ciągły / dyskretny
	* rzeczywiste / zespolone
* Ze względu na okresowość
	* okresowe
	* nieokresowe
* Ze względu na czas trwania
	* o skończonym czasie trwania (impulsowe)
	* o nieskończonym czasie trwania
### Przykłady
* Sygnał ciągły czasu dyskretnego - sygnał po próbkowaniu idealnym sygnału analogowego
* Sygnał dyskretny czasu ciągłego - sygnał schodkowy na wyjściu przetwornika analogowo-cyfrowego
* Sygnał dyskretny czasu dyskretnego - sygnał spróbkowany idealnie po kwantyzacji równomiernej

### Sygnał okresowy czasu ciągłego
* $T_0$ - okres podstawowy
	* $\min_{T_0} \exists T_0 > 0: \forall t \in \mathbb{R}: x(t) = x(t + T_0)$
* $f_0 = \frac{1}{T_0}$ - częstotliwość podstawowa
* $\omega_0 = 2 \pi f_0$ - pulsacja podstawowa

### Sygnał okresowy czasu dyskretnego
* $N_0$ - okres podstawowy

## Sygnały o skończonym czasie trwania
### Czasu ciągłego

#### Impuls prostokątny
$$
x(t) = A \cdot \Pi(\frac{t}{\tau})
= \begin{cases}
	A/2 & t=\pm\tau/2 \\
	A & t \in (\tau/2, \tau/2) \\
	0 & w \quad p. p.
\end{cases}
$$

* $A$ - amplituda
* $\tau$ - czas trwania impulsu

#### Impuls trójkątny
 $$
 x(t) = A \cdot \Lambda(\frac{t}{\tau})
 $$
* $A$ - amplituda
* $2\tau$ - czas trwania impulsu

### Czasu dyskretnego
#### Impuls jednostkowy
(Delta Kroneckera)
$$
\delta(n) = \begin{cases}
	1 & n=0 \\
	0 & n \ne 0
\end{cases}
$$
#### Impuls prostokątny 
$$
\Pi_N(n) = \begin{cases}
	1 & n \in [-N,N] \\
	0 & n \notin [-N,N]
\end{cases}
$$

## Sygnały o nieskończonym czasie trwania
#### Sygnał Sa
$$Sa(\omega_0 t) = \frac{sin(\omega_0 t)}{\omega_0 t}$$
* $\omega_0 t$ - obwiednia sygnału

#### Sygnał Gaussa
$$g(t) = \frac{1}{\sigma \sqrt{2\pi}}exp(-\frac{(t-\mu)^2}{2\sigma^2})$$
#### Skok jednostkowy 
$$\mathbb{1}(t) = \begin{cases}
	1 & t > 0 \\
	1/2 & t=0 \\
	0 & t < 0
\end{cases}$$
#### Skok rampowy 
$$r(t) = t \cdot \mathbb{1}(t) = \begin{cases}
	t & t \ge 0 \\
	0 & t < 0
\end{cases}$$
* $\frac{d}{dt}r(t) = \mathbb{1}(t)$
#### Skok jednostkowy (dyskretny)
$$
\mathbb{1}(n) = \begin{cases}
	1 & n \ge 0 \\
	0 & n < 0
\end{cases}
$$

## Operacje na sygnałach

### Przesunięcie w czasie (translacja)
* $t \rightarrow t - t_0$ - przesunięcie w prawo o $t_0$

### Skalowanie osi czasu
* $t \rightarrow a \cdot t$ 
	* $a > 1$ - ściśnięcie
	* $a < 1$ - rozciągnięcie

### Mnożenie sygnałów
* Mnożenie dwóch sygnałów
* Mnożenie przez stałą (wzmocnienie / tłumienie)
* Mnożenie przez skok jednostkowy (sygnał przyczynowy)
* Mnożenie przez okno (okienkowanie)
* Mnożenie przez cos/sin (modulacja)
* Mnożenie przez deltę (delta Diraca albo impuls jednostkowy)
	* $x(t) \cdot \delta(t-t_0) = x(t_0) \cdot \delta(t-t_0)$

## Podstawowe parametry sygnałów
* Wartość średnia
* Energia
* Moc średnia

Dla sygnałów okresowych oblicza się wartości dla jednego okresu


## Sygnały energii i mocy
* Sygnał energii - energia jest ograniczona (liczba rzeczywista)
	* wszystkie o ograniczonym czasie trwania (impulsowe)
	* sygnały o drganiach gasnących (np. Sa)
	* sygnały rzeczywiste spełniające własność
		* $\lim_{\tau \rightarrow \infty} \int_{-\tau}^\tau |x(t)|^2dt < \infty$
		* $\lim_{M\rightarrow+\infty} \sum_{n=-M}^M |x(n)|^2 < \infty$
		* np. sygnał Gaussa
* Sygnał mocy - moc średnia jest ograniczona (liczba rzeczywista)
	* sygnały okresowe
	* sygnały rzeczywiste dążące do stałej w nieskończoności
		* np. sygnał stały, skok jednostkowy, signum
* Klasy są rozłączne
* Energia ograniczona $\implies P_x = 0$
* Moc ograniczona $\implies E_x = \infty$


## Delta Diraca
$$
\delta(t) = \begin{cases}
0 & t \ne 0 \\
\infty & t = 0 \\
\end{cases}
$$

$$\int_{-\infty}^\infty \delta(t)dt = 1$$

Delta diraca nie jest funkcją w zwykłym sensie bo dla $t=0$ nie przyjmuje wartości liczbowej. Jest modelem matematyznym sygnału impulsowego o nieskończenie krótkim czasie trwania i nieskończenie dużej amplitudzie.

### Ciągi aproksymujące deltę Diraca przy $\tau \rightarrow 0$
* $1/\tau \Lambda(t/\tau)$
* $1/\tau \Pi(t/\tau)$


### Własności delty Diraca
* Parzystość $\delta(-t) = \delta(t)$
* Mnożenie przez stałą $\int A \cdot \delta(t) dt = A \int \delta(t)dt = A$
* Związek ze skokiem jednostkowym $\frac{d}{dt}\mathbb{1}(t) = \delta(t)$
* Własność próbkowania $x(t) \delta(t-t_0) = x(t_0) \delta(t-t_0)$
* Własność filtracji $\int x(t) \delta(t-t_0)dt = x(t_0)$
* Zmiana skali $\delta(t/t_0) = |t_0| \delta(t)$
* Splot $x(t) * \delta(t-t_0) = x(t-t_0)$


## Splot
$$x(t) * y(t) = \int_{-\infty}^\infty x(\tau)y(t-\tau)d\tau$$
$y(t-\tau)$ - złożenie inwersji czasowej z przesunięciem o $t$ w dziedzinie $\tau$

## Dystrybucja grzebieniowa
$$\delta_T(t) = \sum_{n=-\infty}^\infty \delta(t-nT)$$

* Jest modelem okresowego sygnału próbkującego do próbkowania równomiernego
* Służy do próbkowania równomiernego
* Próbkowanie polega na przemnożeniu sygnału przez $\delta_T(t)$
	* $T$ - okres próbkowania.

### Próbkowanie
$$x_S(t) 
= x(t) \cdot \delta_{T_s}(t)
= x(t) \sum_{n=-\infty}^{\infty} \delta(t-nT_s)
= \sum_{n=-\infty}^{\infty} x(t) \delta(t-nT_s)
= \sum_{n=-\infty}^{\infty} x(nT_s) \delta(t-nT_s)
$$
$x_S(t)$ - sygnał spróbkowany

### Powielenie okresowe sygnału impulsowego

$$
x(t) 
= z(t) * \delta_{T_0}(t) 
= z(t) * \sum_{n=-\infty}^{\infty}\delta(t-nT_0)
= \sum_{n=-\infty}^{\infty} z(t) * \delta(t-nT_0)
= \sum_{n=-\infty}^\infty z(t-nT_0)
$$
* $x(t)$ to sygnał okresowy składający się z powielonych impulsów $z(t)$
* $z(t)$ jest sygnałem impulsowym o czasie trwania $\tau < T_0$
