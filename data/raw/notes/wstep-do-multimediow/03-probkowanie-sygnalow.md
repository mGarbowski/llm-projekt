# Próbkowanie sygnałów
* Próbkowanie polega na mnożeniu sygnału analogowego przez sygnał próbkujący $p(t)$
* Próbkowanie idealne $p(t) = \delta_{T_S}(t)$
* Próbkowanie rzeczywiste $p(t)$ - krótkie impulsy prostokątne

### Widmo sygnału spróbkowanego idealnie

$$X_s(\omega) = \frac{1}{T_s} \sum_{n=-\infty}^\infty X(\omega - n\omega_s)$$
$$X_s(f) = f_s \sum_{n=-\infty}^\infty X(f - nf_s)$$

* Widmo iloczynu dwóch sygnałów jest splotem odpowiednich widm
* Sygnał dyskretny ma widmo okresowe
* Widmo sygnału spróbkowanego składa się z kopii widma sygnału analogowego scentrowanych wokół wielokrotności częstotliwości próbkowania
* Najważniejszy parametr to częstotliwość próbkowania

## Twierdzenie o próbkowaniu
Jeżeli $x(t)$ jest sygnałem o ograniczonym paśmie ($X(f)=0$ dla $|f| > f_m$) , to zbiór próbek $x(nT_s)$ tego sygnału pobieranych z częstotliwością $f_s > 2f_m$ jednoznacznie określa sygnał $x(t)$.

* Częstotliwość Nyquista $f_N = 2f_m$
* Warunek Nyquista spełniony $f_s > 2f_m$
* Dla $f_s < 2f_m$ - fragmenty widma nakładają się na siebie
	* aliasing częstotliwościowy

## Eliminacja zjawiska aliasingu
* Dobranie odpowiednio dużej częstotliwości próbkowania
* Zastosowanie filtracji dolnoprzepustowej przed próbkowaniem
	* ogranicza pasmo sygnału analogowego
	* filtracja antyaliasingowa

## Efekt stroboskopowy
Efekt stroboskopowy w dziedzinie czasu można zaobserwować przy próbkowaniu sygnałów okresowych z odpowiednio dobraną częstotliwością $f_s$ dużo mniejszą niż częstotliwość Nyquista $f_N$ i bliską częstotliwości podstawowej $f_0$.

## Próbkowanie rzeczywiste (chwilowe)
* Próbkowanie impulsami prostokątnymi

$$\hat{x}(t) = \sum_{n=-\infty}^{\infty}x(nT_s) \cdot z(t-nT_s)$$
$$z(t) = \Pi(\frac{t-T_s/2}{T_s})$$
$$
\hat{X}(\omega) 
= Sa(\omega T_s/2) \exp(-j\omega T_s/2) 
\sum_{n=-\infty}^{\infty}X(\omega-n\omega_s)
$$
