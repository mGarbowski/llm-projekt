# Przetwarzanie obrazów cyfrowych
* Operacje punktowe, lokalne, globalne
* Na wejściu wartość pojedynczego piksela, na wyjściu wartość wynikowego piksela
* Wejście to może być wartość kilku składowych (w ogólności kilku obrazów)
* Nie każdy piksel wejścia musi znaleźć odzwierciedlenie w wyjściu (podbróbkowanie)

## Histogram obrazu
* Liczba wystąpień poszczególnych wartości w obrazie
* Dla obrazu monochromatycznego to wartości jasności
* Histogram w formie znormalizowanej - podzielenie przez liczbę pikseli w obrazie
	* de facto funkcja rozkładu prawdopodobieństwa
* Skala znormalizowana - wartości od 0 do 1
	* podzielenie przez wartość maksymalną (np. 255)

## Operacje punktowe
Na pojedynczych pikselach
### Zmiana jasności
* $y[m,n] = x[m,n] + o$
* Możliwe jest wyjście poza zakres - trzeba przycinać wartości
* Histogram przesuwa się w prawo - jasność się zwiększa

### Zmiana kontrastu
* Rozciąganie histogramu
* $y[m,n] = k \cdot x[m,n]$
	* $k > 1$ - ekspancja
	* $k < 1$ - komprymacja
* Dla $k>1$ uwydatnia szum
	* można wcześniej odszumić obraz

### Rozciągnięcie histogramu
* Połączenie zmiany kontrastu i zmiany jasności
* Musimy znać wartości maskymalne i minimalne
* $y[m,n] = k \cdot x[m,n] + o = k \cdot (x[m,n] + o')$
* Charakterystyka dla skali znormalizowanej
	* stała, liniowa, stała
	* nachylenie $1/k$
	* przycinanie zamiast wyjścia poza zakres (w skali znormalizowanej do $[0,1]$)

#### Przykład
* Rozciągnięcie do zakresu $[i_{min}, i_{max}]$
* Znaleźć wartości minimalną $v_{min}$ i maksymalną $v_{max}$ dla rozważanych pikseli
* Rozwiązać układ
	* $i_{max} = k \cdot v_{max} + d$
	* $i_{min} = k \cdot v_{min} + d$
* Wartość pikselu po rozciągnięciu to $i = k \cdot v + d$
	* $i$ nowa wartość
	* $v$ stara wartość

### Wyrównanie histogramu
* Rozciąga histogram ale nierównomiernie
	* większe odstępy dla częstszych wartości jasności
* Funkcja dystrybuanty $cdf$
* $y[m,n] = cdf[x[m,n]]$
	* $cdf[k] = \sum_{l=0}^k pdf[l]$
* Należy przeprowadzać tylko na składowej luminancyjnej (jasności) w YCbCr
	* robienie oddzielnie dla składowych RGB zmienia zupełnie kolory na wyjściu
* Może uwydatnić szum - lepiej wstępnie przefiltrować
* Implementacja przez lookup table - wylicza się $cdf$ raz dla całego obrazu i potem odczytuje dla każdego piksela

### Korekcja gamma
* Naśladuje potęgowe prawo Stevensa
* Przetwarzanie obrazu w skali odpowiadającej wrażliwości na zmiany postrzegania jasności, a nie proporcjonalnie do zmiany energii światła
* Nieliniowa operacja
* $y[m,n] = A \cdot (x[m,n])^\gamma$
	* $A$ - parametr proporcjonalności
	* przy wartościach maksymalnych wejścia powinna dać maksymalną wartość wyjścja
	* krzywe zbiegają się w punktach $(0,0)$ i $(1,1)$
	* dla skali znormalizowanej to $1$

### Progowanie
* Porównanie wartości każdego piksela
* Jeśli wpada do zakresu przypisujemy 1, jeśli nie 0
* W wyniku powstaje obraz binarny
* Progowanie podwójne
	* dwa progi
	* wartości pomiędzy dostają $1$
* Pseudoprogowanie
	* zamiast przypisać $1$, przepuszca się wartość wejściową na wyjście
	* zerowanie pozostałych

## LUT
* Look-up table
* Można przyspieszyć wiele operacji
* Mogą być zależne od statystyk
* Może mieć duży rozmiar
* Można podzielić zakres na odcinki o w przybliżeniu liniowej charakterystyce i interpolować
	* jak wartość jest pomiędzy tymi zapamiętanymi w tablicy stosuje się interpolację liniową

## Operacje lokalne
* Oprócz pojedynczego piksela używa się też pikseli z jego otoczenia w obrazie wejściowym
* Np.  3x3
* Różne rozmiary sąsiedztwa, maski
* Zazwyczaj symetryczne ale niekoniecznie
* $y[m,n] = f(x[m,n], x[m-1,n], \ldots)$

### Filtry liniowe 2D
* Operacja splotu maski filtru z pikselami obrazu
* Problem z traktowaniem brzegów obrazu
	* można dodać padding
	* zera mogą zmienić statystyki
	* można powielić wartości pikseli z brzegu
	* można zrobić odbicie lustrzane
* $y[m,n] = \sum_{k=-K/2}^{K/2} \sum_{l=-L/w}^{L/2} a[k,l] \cdot x[m+k, n+l] = x[m,n] * a[k,l]$

#### Filtr uśredniający
* $a[k,l] = \frac{1}{K \cdot L}$
* Filtr dolnoprzepustowy

#### Filtr Gaussa
* $a[k,l] = \frac{1}{\sqrt{2\pi} \sigma^2} \exp(-\frac{k^2+l^2}{2\sigma^2})$
* Dolnoprzepustowy
* Dwuwymiarowa krzywa Gaussa
* Kernel to macierz próbek z funkcji Gaussa
* Np. maska 3x3
* Można zastosować większą maskę albo taką samą maskę wielokrotnie
* Wygładza obraz
* Parametryzowany wariancją
* Oprócz usuwania szumu rozmywa krawędzie

#### Filtr Prewitta
* Filtr krawędziowy
* 8 wariantów wykrywających krawędzie w różnych kierunkach
	* poziome
	* pionowe
	* skośne
* Suma elementów maski daje zero
* Można zsumować wartości bezwzględne wyników dla różnych filtrów (i poziomych i pionowych)
	* $abs$ przy sumowanie, ale nie przy wyostrzaniu
	* $y_H[m,n] = x[m,n] * a_H[k,l]$
	* $y_V[m,n] = x[m,n] * a_V[k,l]$
	* $y[m,n] = abs(y_H[m,n]) + abs(y_V[m,n])$
* Dostajemy obraz krawędziowy

$$
a_H[k,l] = \begin{bmatrix}
1 & 1 & 1 \\
0 & 0 & 0 \\
-1 & -1 & -1 \\
\end{bmatrix}
$$

#### Filtr Sobela
* Filtr krawędziowy
* Filtr górnoprzepustowy

$$
a_H[k,l] = \begin{bmatrix}
1 & 2 & 1 \\
0 & 0 & 0 \\
-1 & -2 & -1 \\
\end{bmatrix}
$$

#### Filtr Laplace'a
* Filtr górnoprzepustowy
* Wykorzystuje laplasjan funkcji (sumę drugich pochodnych cząstkowych)
	* 8 lub 4 pochodne cząstkowe
* Detekcja krawędzi

$$
a_H[k,l] = 
\begin{bmatrix}
-1 & -1 & -1 \\
-1 & 8 & -1 \\
-1 & -1 & -1 \\
\end{bmatrix}
\quad
a_H[k,l] = 
\begin{bmatrix}
0 & -1 & 0 \\
-1 & 4 & -1 \\
0 & -1 & 0 \\
\end{bmatrix}
$$

#### Wyostraznie obrazu
* Dodanie obrazu krawędziowego przemnożonego przez stałą
* Można od razu wyostrzyć obraz stosując zmienioną maskę
	* zamiast najpierew wyliczać obraz krawędziowy

### Filtry nieliniowe
* Wykorzystuje statystykę pozycyjną (w otoczeniu)
* Redukcja zakłóceń
* Poprawa jakości obrazu

$$
y[m,n] = f(x[m,n], x[m-1,n], \ldots) = \sum_{i=1}^{k \cdot L} a_i x_i
$$

#### Filtr medianowy
* Środkowy indeks w uszeregowanym ciągu wartości pikseli objętych maską
* Dobrze usuwa szum
	* szczególnie szum impulsowy (salt and pepper)
* Dobrze zachowuje krawędzie
* Problem z narożnikami

$$
a_i = \begin{cases} 
	1 & i = \lceil K \cdot L/2 \rceil \\
	0 & i \ne \lceil K \cdot L/2 \rceil \\
\end{cases}
$$

#### Filtry morfologiczne
* Ograniczający (erozja) - $\min$
* Rozszerzający (dylacja) - $\max$
* Otwarcie - $\max(\min(\ldots))$
* Domknięcie - $\min(\max(\ldots))$
* Otwarcie-domknięcie, domknięcie-otwarcie
* Gradient - $\max(\ldots)-\min(\ldots)$

## Dyskretna transformata kosinusowa
* Transformacja bloków obrazu w blok współczynników częstotliwości przestrzennych
* Dekorelacja wartości wejściowych
* Skpienie większości energii w kilku współczynnikach
	* najczęściej niskoczęstotliwościowych
* Większość współczynników jest mało znacząca
	* wartości bliskie 0
* Większość bloków zawiera tylko kilka znaczących współczynników
	* z reguły niskoczęstotliwościowych
* Każdy blok obrazu można przedstawić jako sumę funkcji bazowych tranformaty (wzorców)
	* suma ważona przez współczynniki otrzymane z DCT
	* głównie niskoczęstotliwościowe
	* większość wynosi $0$
* Wyjściem DCT jest zestaw wag dla wzorców (współczynniki DCT)
* Odtworzenie obrazu
	* przemnożenie wzorców przez wagi
	* zsumowanie
* Wzorce to funkcje bazowe 2D $\cos() \cdot \cos()$
* Współczynniki DCT można uzyskać za pomocą DFT/FFT przez odwzorowanie oryginalnego bloku $N$ próbek na blok $2N$ próbek
	* odbicie lustrzane eliminuje składniki urojone $\sin()$ w DFT
	* $N$ pierwszych współczynników DFT jest lustrzanie taka sama jak $N$ kolejnych
	* współczynniki DCT są równoważne pierwszym $N$ współczynnikom przekształcenia DFT dla bloku $2N$ próbek
* Wykorzystanie FFT pozwala szybko obliczyć DCT

## Operacje globalne
* Wartość piksela wyjściowego zależy od wszystkich pikseli obrazu wejściowego
	* albo obrazów wejściowych jak przy RGB
### FFT, IFFT
* Mmożna przepuścic tylko dolne częstotliwości przez wycięcie części transformaty blisko (0,0)
* Przedstawia statystykę, która nie jest stacjonarna
	* różne części obrazu mają różne właściwości
* Energia po przekształceniu powinna być skupiona
* Zamiast dla całego obrazu można stosować transformatę lokalnie
