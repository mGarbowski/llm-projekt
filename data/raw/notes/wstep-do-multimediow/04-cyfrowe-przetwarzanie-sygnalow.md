# Elementy cyfrowego przetwarzania sygnałów

## Przekształcenie DTFT
* Widmo też można wyrazić jako zespolony szereg fouriera
	* jak wszystko co jest okresowe
* Współczynniki szeregu to próbki $x(nT_S)$
* Podstawienie $\Omega = \omega T_S$ - pulsacja unormowana
	* po znormalizowaniu widmo jest okresowe o okresie $2\pi$
* Częstotliwość unormowana $F$ 
	* $\Omega = 2\pi F$
* Widmo rozważa się w ograniczonym przedziale bo jest okresowe

## N-punktowe dyskretne przekształcenie Fouriera
* Dyskretyzacja dziedziny częstotliwości
	* N próbek w jednym okresie
* Krok dyskretyzacji $\Delta f = \frac{f_S}{N}$ - rozdzielczość częstotliwościowa DFT
* Zastąpienie zmiennej $f$ przez $k \Delta f$

$$
X_N(k) = \sum_{n=0}^{N-1} x(n) \exp(-j2\pi kn/N) = \sum_{n=0}^{N-1} x(n)W_N^{kn}
$$

$$
x(n) = \frac{1}{N} \sum_{k=0}^{N-1} X_N(k) \exp(j2\pi kn/N) 
= \frac{1}{N} \sum_{k=0}^{N-1} X_N(k)W_N^{-kn}
$$
$$x(n) \leftrightarrow X_N(k)$$

* To samo $N$ - liczba próbek w dziedzinie czasu i częstotliwości
* N-punktowa DFT to funkcja o okresie N, widmo sygnału $x(n)$

### Przesunięcie cykliczne w czasie
* Jak dodawanie modulo N
* Jest różnica między splotem zwykłym a cyklicznym

## Przeciek widma
* Kiedy w widmie sygnału zdyskretyzowanego pojawiają się składowe nie występujące w widmie sygnału analogowego
* Mozna je redukować przez okienkowanie sygnału w dziedzinie czasu
* Np. widmo sinusa może miec więcej niż 2 prążki
	* ale o takiej samej sumarycznej mocy

$$
X_w(k) = \sum_{n=0}^{N-1} w(n) x(n) \exp(-j 2\pi kn / N)
$$

## Fast Fourier Transform
* Algorytm numerycznie obliczający N-punktową DFT
* Wymaga żeby N było potęgą 2
* Złożoność $O(N \log N)$
