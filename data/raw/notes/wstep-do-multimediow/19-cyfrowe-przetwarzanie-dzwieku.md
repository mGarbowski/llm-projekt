# Cyfrowe przetwarzanie dźwięku

## Cyfrowe przetwarzanie sygnałów fonicznych
* Ekstrakcja cech
	* głównie analiza częstotliwościowa
* Filtracja
* Efekty dźwiękowe
* Synteza

## Okno analizy FFT
* Kiedy okno jest wielokrotnością okresu sygnału
	* nie ma nieciągłości
	* pojedynczy prążek w widmie
* Raczej nie da się osiągnąć dokładnej wielokrotności (jest wiele częstotliwości w sygnale)
	* pojawiają się nieciągłości
	* prążki w widmie się rozlewają
* Sygnał przemnaża się przez odpowiednie wagi
	* mnożenie przez 0 wartości, które "przeszkadzają"
	* istotne składowe zostaną w widmie
	* okno Hanninga, okno prostokątne
	* odpowiednie okno ogranicza przeciekanie widma

## Spektrogram
* Ilustruje czas, częstotliwość i natężenie
	* czas - oś pozioma
	* częstotliwość - oś pionowa
	* natężenie - kolor
* Zamienia dźwięk na obraz
	* pozwala użyć wszystkich mechanizmów do przetwarzania obrazów
	* np. uczenie maszynowe, ekstrakcja cech, rozpoznawanie mowy

## Rozmiar okna
* Dłuższe okno
	* większa liczba próbek
	* lepsza rozdzielczość częstotliwości
	* gorsza rozdzielczość czasowa
	* dłuższa obserwacja - różnice czasowe się zamazują
* Krótsze okno
	* mniejsza liczba próbek
	* gorsza rozdzielczość częstotliwości
	* lepsza rozdzielczość czasowa
* Można zrobić dwa razy analizę tego samego sygnału i mieć oba
* Rozmiar okna to tradeoff w rozdzielczości w czasie i częstotliwości

Widmo dla określonego czasu trwania vs widmo w czasie rzeczywistym vs spektrogram

## Ekstrakcja cech dźwięku

### Spectral roll-off
* Parametr *opadania widma*
* Częstotliwość poniżej której znajduje się określony procent całej energii
* Dobrze wskazuje początki i końce słów, nut

$$
v_{SR}(n) = i | \quad \sum_{k=0}^i |X(k,n)| = \kappa
$$

### Spectral flux
* Parametr określający szybkość zmian widma
* Porównanie widma z bieżącego okna do widma z poprzedniego okna
* Wykorzystywany do opisu barwy dźwięku
* Do wykrywania początków słów, nut

$$
v_{SF}(n) = 
\frac
{\sqrt{\sum_{k=0}^{\kappa/2-1}(|X(k,n)| - |X(k,n-1)|)^2}}
{\kappa / 2}
$$

### Spectral centroid
* Środek ciężkości widma
* Określa jasność brzmienia
	* im większa wartość, tym jaśniejsza barwa dźwięku

$$
v_{SC}(n) = \frac
{\sum_{k=0}^{\kappa/2-1} k |X(k,n)|^2}
{\sum_{k=0}^{\kappa/2-1} |X(k,n)|^2}
$$

### Spectral spread
* Opisuje średnie odchylenie od centroidy
* Dla szumów duża wartość
* Dla dźwięków tonalnych niska wartość

$$
v_{SS}(n) = \sqrt{\frac
{\sum_{k=0}^{\kappa/2-1} (k-v_{SC}(n))^2 |X(k,n)|^2}
{\sum_{k=0}^{\kappa/2-1} |X(k,n)|^2}
}
$$

### Spectral decrease
* Opisuje stromość zbocza widma
* Niskie wartości wskazują na koncentrację energii dla niskich częstotliwości

$$
v_{SD}(n) = \frac
{\sum_{k=0}^{\kappa/2-1}\frac{1}{k}(|X(k,n)| - |X(0,n)|)}
{\sum_{k=0}^{\kappa/2-1} |X(k,n)|}
$$

### MFCC - MEL-Frequency Cepstral Coefficients
* Cepstrum sygnału przedstawione w skali melowej
* Wektor parametrów mel-cepstralnych to wektor współczynników cepstrum w odpowiednich pasmach melowych
* Mają za zadanie odzwierciedlać naturalną odpowiedź układu słuchowego na pobudzenie dźwiękami mowy

$$
v_{MFCC}^j(n) = 
\sum_{k'=1}^{\kappa'} 
\log (|X'(k',n)|) 
\cdot 
\cos(j(k-\frac{1}{2})\frac{\pi}{\kappa'})
$$

### Skala melowa
* Skala melowa odpowiada ludzkiemu postrzeganiu częstotliwości
* Oparte o filtrację bankiem filtrów o charakterystyce trójkątnej
* K-ty współczynnik mel-cepstralny odpowiada zawartości k-tego pasma
* Zazwyczaj liczba pasm wynosi od 12 do 20

## Zastosowania

### ASR
* ASR - Automatic Speech Recognition
* STT - Speech-To-Text
* LVCSR - Large Vocabulary Continuous Speech
	* mowa ciągła
	* dyktowanie tekstu

### Rozpoznawanie mówcy
* Speaker recognition
	* speaker identification
	* speaker detection
	* speaker verification

### Rozpoznawanie emocji w głosie
* Daje się dobrze wyznaczyć na podstawie wyliczonych (wcześniej wymienionych) statystyk

## Kompresja dźwięku
* Redukcja ilości danych
* Redukcja przepływności
* Redukcja wielkości pliku
* Kompresja w sensie zawężania dynamiki dźwięku to co innego (nie mylić)
* Umożliwia zwiększenie ilości danych zapisanych na nośniku
* Umożliwia zmniejszenie szerokości pasma w systemie transmisyjnym
* Umożliwia szybszą transmisję w danym paśmie

### Rodzaje kompresji
* Bezstratna
	* wav
	* flac
* Stratna
	* mp3
	* ogg
	* wma

### Kompresja bezstratna
* Bez utraty informacji o sygnale pierwotnym
* Kodowanie ciszy przez czas jej trwania
* Kodowanie mono i różnic między kanałami zamiast stereo
* Przykłady
	* FLAC
	* WMA
	* MLP
	* M4A
	* APE

### Kompresja stratna
* Utrata informacji o sygnale pierwotnym (może być znacząca)
* Usuwanie skrajnie wysokich i niskich częstotliwości
* Usuwanie dźwięków o niskim poziomie
* Wykorzystywanie modeli psychoakustycznych
	* wycina się to co zostanie najmniej zauważone
* Przykłady
	* MP1, MP2, MP3
	* AAC
	* MPC
	* OGG
	* ATRAC
