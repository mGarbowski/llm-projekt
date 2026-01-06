# Szereg i transformata Fouriera

## Trygonometryczny szereg Fouriera
Syngał okresowy o częstotliwości podstawowej $f_0$ w postaci

$$x(t) = A_0 + \sum_{n=1}^\infty A_n cos(2\pi n f_0t + \phi_n)$$

* $\{ A_0, A_1, A_2, \ldots \}$ - widmo amplitudowe (jednostronne)
* $\{ \phi_1, \phi_2, \ldots\}$ - widmo fazowe (jednostronne)
* Sygnał o symetrii parzystej - wyraża się jako suma cosinusów
* Sygnał o symetrii nieparzystej - wyraża się jako suma sinusów

## Widmo mocy i twierdzenie Parsevala
* $\{ A_0^2, A_1^2/2, A_2^2/2 \}$ - widmo mocy (jednostronne)
* Moc średnia za okres $P_x = A_0^2 + \sum_{n=1}^\infty \frac{A_n^2}{2}$


## Synteza fourierowska
Przybliżamy sygnał $x(t)$ sumą składowej stałej i skończonej liczby $M$ składowych harmonicznych

$$x_M(t) = A_0 + \sum_{n=1}^M A_n \cos(n\omega_0t + \phi_n)$$
Błąd średniokwadratowy aproksymacji równa się sumie mocy pominiętej w syntezie składowych harmonicznych

$$
\sigma_M^2 = \sum_{n=M+1}^\infty A_n^2 / 2
$$

### Efekt Gibbsa
Synteza fourierowska fali prostokątnej - oscylacje o wyższej amplitudzie w otoczeniu punktów nieciągłości

## Równoważna postać trygonometrycznego szeregu Fouriera
$$x(t) = A_0 + \sum_{n=1}^\infty A_n cos(2\pi n f_0t + \phi_n)$$
$$
x(t) = A_0 
+ \sum_{n=1}^\infty A_ncos(\phi_n) cos(2\pi n f_0t) 
+ \sum_{n=1}^\infty -A_n sin(\phi_n) sin(2\pi n f_0t)
$$

$$
x(t) = A_0 
+ \sum_{n=1}^\infty a_n cos(2\pi n f_0t) 
+ \sum_{n=1}^\infty b_n sin(2\pi n f_0t)
$$
$$
a_n = A_n cos(\phi_n) 
\wedge b_n = -A_n sin(\phi_n) 
\iff A_n = \sqrt{a_n^2 + b_n^2}
$$

* Sygnał o symetrii parzystej $b_n = 0$
* Sygnał o symetrii nieparzystej $a_n = 0$
* Sygnał antysymetryczny 
	* $x(t) = -x(t + \frac{T_0}{2})$
	* $A_0=0$
	* szereg zawiera tylko składowe harmoniczne nieparzyste

## Wzory Eulera
Przekształcając sin i cos ze wzorów Eulera
$$\cos(n\omega_0t) = \frac{1}{2}(e^{jn\omega_0t} + e^{-jn\omega_0t})$$
$$\sin(n\omega_0t) = \frac{1}{2j}(e^{jn\omega_0t} - e^{-jn\omega_0t})$$

$$x(t) 
= \sum_{n=-\infty}^\infty c_n e^{jn\omega_0t}
= A_0 + \sum_{n=1}^\infty a_n \cos(n\omega_0t) 
+ \sum_{n=1}^\infty b_n \sin(n\omega_0t)
$$

* $c_0 = A_0$
* $c_{-n} = c_n^*$
* $a_n = 2 \cdot \Re(c_n) = c_n + c_{-n}$ 
* $b_n = -2 \cdot \Im(c_n) = j(c_n - c_{-n})$

### Widma dwustronne
* Widmo amplitudowe $\{|c_n|: n \in \mathbb{Z}\}$ 
	* parzyste
* Widmo fazowe $\{\arg c_n: n \in \mathbb{Z}\}$
	* nieparzyste
* Widmo mocy $\{|c_n|^2: n \in \mathbb{Z}\}$ 
	* parzyste
* $|c_n| = A_n/2$ dla $n \ge 1 \quad A_n \ge 0$
* $|c_n| = |c_{-n}|$
* Twierdzenie Parsevala $P_x = \sum_{n \in \mathbb{Z}} |c_n|^2$

## Podsumowanie
* Każdą funkcję okresową można przedstawić jako szereg Fouriera funkcji trygonometrycznych lub wykładniczych
* Nie może być bezpośrednio stosowany w praktyce do analizy częstotliwościowej wszystkich sygnałów
	* założenie o nieskończonym czasie trwania
	* założenie o okresowości sygnału

## Przekształcenie Fouriera
* Sygnał okresowy ma widmo dyskretne (prążkowe)
* Prążki na wielokrotnościach częstotliwości podstawowej
* W nieskończoności $T \rightarrow \infty$ następuje uciąglenie widma
	* $T \rightarrow \infty$ - sygnał impulsowy
* Przekształcenie fouriera definiuje transformatę Fouriera (widmo) sygnału $x(t)$
  
$$
X(\omega)
= \mathcal{F}\{x(t)\} 
= \int_{-\infty}^\infty x(t)e^{-j\omega t}dt$$

$$
x(t)
= \mathcal{F}^{-1}\{X(\omega)\}
= \frac{1}{2\pi} \int_{-\infty}^\infty X(\omega)e^{j\omega t} d\omega
$$

## Widmo - pojęcia podstawowe
$$
X(\omega) 
= |X(\omega)|e^{j\arg X(\omega)} 
= \Re(X(\omega)) + j \Im(X(\omega))
$$

* Widmo amplitudowe - $|X(\omega)|$
* Widmo fazowe - $\arg X(\omega)$
* Widmo gęstości energii - $|X(\omega)|^2$
* Widmo rzeczywiste - $\Re(X(\omega))$
* Widmo urojone - $\Im(X(\omega))$


## Twierdzenie Parsevala
Jeżeli $x(t)$ jest sygnałem o ograniczonej energii, to jego energia jest równa polu pod wykresem widma gęstości energii

$$
E_x
= \int_{-\infty}^\infty |x(t)|^2 dt
= \frac{1}{2\pi} \int_{-\infty}^\infty |X(\omega)|^2 d\omega
= \int_{-\infty}^\infty |X(f)|^2 df
$$
