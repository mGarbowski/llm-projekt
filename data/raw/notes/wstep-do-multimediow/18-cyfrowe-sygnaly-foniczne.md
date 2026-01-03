# Cyfrowe sygnały foniczne
Sygnał foniczny - sygnał elektryczny, niesie informację o dźwięku

## Ogólny schemat przetwarzania
* Mikrofon odbiera sygnał analogowy
* Przetwornik ADC przetwarza sygnał na cyfrowy
* Sygnał cyfrowy jest przetwarzany
* Przetwornik DAC przetwarza na sygnał analogowy
* Głośnik odbiera sygnał analogowy
* Etapy
	* filtracja
	* próbkowanie
	* kwantyzacja
	* kodowanie

## Filtracja
* Powinniśmy zadbać o to, żeby w sygnale wejściowym nie było częstotliwości wyższych niż połowa częstotliwości próbkowania
	* nie będzie aliasingu

## Próbkowanie
* Zamienia sygnał analogowy (ciągły) na sygnał dyskretny w czasie
* Najważniejszy parametr - częstotliwość próbkowania
	* jak często pobierane są próbki z sygnału wejściowego
	* im częściej tym dokładniejsze próbkowanie

### Twierdzenie o próbkowaniu
Aby możliwe było jednoznaczne odtworzenie sygnału na podstawie próbek, próbki muszą być pobierane z częstotliwością co najmniej dwa razy większą od maksymalnej częstotliwości widma sygnału

### Aliasing
* Próbkowanie daje sygnał o innej (niższej) częstotliwości, nie zawartej w sygnale źródłowym
* Antyaliasingowy filtr dolnoprzepustowy

### Pasmo sygnałów fonicznych
* Audio
	* 20Hz-20kHz
	* częstotliwość próbkowania co najmniej 40kHz
* VoIP
	* 20Hz-4kHz
	* częstotliwość próbkowania co najmniej 8kHz

Żaden filtr nie da idealnie stromej granicy filtracji, nie da się w pełni odfiltrować niepożądanych częstotliwości

### Typowe częstotliwości próbkowania dźwięku
* 8-22kHz - VoIP, transmisja internetowa
* 44.1kHz - audio CD
* 48kHz - dźwięk w filmie i aduio wysokiej jakości
* do 192kHz - profesjonalna, studyjna rejestracja dźwięku

### Błędy próbkowania
* Jitter - błąd wynikający z niedokładności czasu zbierania próbek
	* zbieranie próbek nie wypada idealnie co 1 okres, tylko z małym przesunięciem

## Kwantyzacja
Dyskretyzacja wartości amplitudy

### Rozdzielczość bitowa przetwornika
* Od niej zależy liczba poziomów kwantyzacji

### Dynamika
* Dynamika przetwornika - 6dB * liczba bitów
* Dynamika ludzkiego słuchu wynosi ok. 120dB
* Standardowe wartości
	* 16-bitowy - 96dB
	* 18-bitowy - 108dB
	* 24-bitowy - 144dB

### Błąd kwantyzacji
* Mniejszy im większa rozdzielczość bitowa
* Różnica między wartością oryginalną a wartością po kwantyzacji

### Dither
* Metoda zmniejszenia błędu kwantyzacji
* Do sygnału wejściowego dodaje się losowy szum o małej amplitudzie
* Po kwantyzacji, sygnał nie będzie się "zatrzaskiwać" kiedy zmienia się o mniej niż 0.5 LSB
* Szum jest mniej uciążliwy niż płaski sygnał

### Błędy przetwarzania
* Odstępstwo od charakterystyki przetwornika
* Błąd różnicowy (przesunięte schodki)
* Niemonotoniczność
* Brakujące słowa kodowe (schodki)

## Kodowanie
* Liniowe
	* Zniekształcenie sygnałów o małej amplitudzie
	* Dobrze oddaje sygnały o dużej amplitudzie
* Nieliniowe
	* Bardziej gęsto rozłożone wartości przy niższych amplitudach
	* Trochę gorsza precyzja dla sygnałów o dużej amplitudzie
	* Lepsza precyzja dla małych amplitud

## Przetworniki AC

### Z równoległym porównaniem bezpośrednim (FLASH)
* Całe słowo kodowe na wyjściu na raz
* Dla każdego bitu równoległe porównywanie z napięciem referencyjnym
* Mała precyzja
* Szybkie

### Z kompensacją wagową (SAR)
* Successive approximation register
* Napięcie porównane z połową napięcia referencyjnego
* Zmiana najbardziej znaczącego bitu i porównanie z kolejnym napięciem
* Tyle porównań ile bitów rozdzielczości

## Przetwarzanie $\Sigma\Delta$
* Etapy
	* Filtracja
	* Nadpróbkowanie
	* Kwantyzacja
	* Kształtowanie szumu
	* Decymacja
* Powszechnie stosowane
* Koncept działania
	* Sygnał jest próbkowany tak często (nadpróbkowanie), żeby wartość wolno się zmieniała
	* Przez uśrednienie wielu próbek uzyskuje się wartość sygnału na wejściu
	* Zgrubna kwantyzacja
	* Przykład z inżynierem kupującym kawę
	* Sygnał wartości 0.5 ma tyle samo impulsów 0 i 1, mniejszy niż 0.5 będzie miał więcej 0
* Rozdzielczość bitowa w Sigma-Delta określa stopień nadpróbkowania, sygnał ma tylko wartości 0 i 1 (kwantyzacja na 1 bit)
* Zalety
	* dostępność, niski koszt
	* nie wymagają precyzyjnego dobierania elementów układu
	* liniowość
	* monotoniczność
* Wady
	* uważa się, że brzmią gorzej niż konwencjonalne (ale to nie jest oczywiste do porównania)
	* konieczność wysokiego nadpróbkowania dla uzyskania rozdzielczości
	* niewielka liczba bitów, utrata rozdzielczości, kształtowanie szumu
	* konieczność wypychania szumu poza słyszalne pasmo

## Przetwarzanie cyfrowo-analogowe
* Konwencjonalne albo $\Sigma\Delta$
* Bit słowa kodowego dokłada odpowiednią częstotliwość przez dzielnik napięcia
* Przykładowe implementacje
	* drabinka rezystorowa R-2R

### Błędy przetwarzania C/A
* Odstępstwo od charakterystyki
* Błąd czasowy układu sample-and-hold (zatrzaskującego)

### Specyfika przetworników fonicznych
* Szerokie pasmo i duża dynamika
	* musi być duża rozdzielczość bitowa i wysoka częstotliwość próbkowania
* Duże pole do minimalizacji błędów przetwarzania
* Nie każde zniekształcenie przeszkadza w jednakowym stopniu
	* szum losowy przeszkadza mniej niż degradacja samego sygnału
	* przetwornik nie musi maksymalizować obiektywnych parametrów
	* ważna jest przejrzystość

## Słuchowa ocena jakości
* Odtwarzanie sceny dźwiękowej
	* utrata przestrzenności
* Przejrzystość brzemienia
	* czy wszystko jest łatwe do usłyszenia
	* subtelne zmiany w jednym instrumencie
* Powietrzność, przestrzeń
	* poczucie przestrzeni i atmosfera
* Odpowiedź i waga basu
* Atak, transjenty
	* szybka zmiana
	* krawędź postrzeganego dźwięku
* Słodki dźwięk
	* brak kłujących wybrzmień i sibilantów
* Emocje - ogólne odczucie
* Wrażenie analogowości
* Ciało - czy wokale brzmią ludzko
