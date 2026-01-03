# Cieniowanie
* Określa wygląd obiektu
	* fotorealizm
	* stylizacja - np. ograniczenie kolorów, przejścia między kolorami
* Zależne od różnych czynników
	* orientacja powierzchni
	* kierunek patrzenia
	* oświetlenie
	* właściwości powierzchni (chropowatość itp.)
* W większości przypadków, minimalna ilość informacji to
	* $\vec{V}$ wektor w kierunku patrzenia
	* $\vec{N}$ wektor normalny dla powierzchni w danym punkcie
	* $\vec{L}$ wektor w kierunku światła
* Dodatkowe informacje na temat światła i samego obiektu

## Typowe operacje wykorzystywane w cieniowaniu
* Zaimplementowane w językach programowania shader'ów
* Clamping - ściskanie wartości do zadanego zakresu
	* `clamp`
* Iloczyn skalarny
	* `dot`
* Interpolacja liniowa
	* `Mix` / `lerp`
* Odbijanie
	* odbicie $\vec{L}$ względem $\vec{N}$
	* $Reflected = 2(\vec{N} \cdot \vec{L})\vec{N} - \vec{L}$
	* `reflect`

## Światło
* Oświetlenie w prawdziwym świecie jest dosyć złożone
	* rozmiar
	* kształt
	* kolor
	* intensywność
* Przy tworzeniu modelu cieniowania należy wziąć pod uwagę
	* obecność światła
	* zachowanie modelu w przypadku braku oświetlenia
	* odległość od światła

## Padanie światła
* Wpływ światła - grupa promieni
	* gęstość promieni zderzająca się z powierzchnią zależna od intensywności światła
* Opisujemy jedną zależnością w najprostszym przypadku
* Odstępy między promieniami świetlnymi odwrotnie porporcjonalne do cosinusa kąta między $\vec{L}$ a $\vec{N}$

### Wzór

$$c_{shaded} = f_{unlit}(\vec{N}, \vec{V}) + \sum_i (\vec{L_i} \cdot \vec{N})^+ c_{light_i} f_{lit}(\vec{L}, \vec{N}, \vec{V})$$

* $c_{shaded}$ - Kolor wynikowy
* $f_{unlit}$ - wygląd gdy nie dociera światło
* $(\vec{L_i} \cdot \vec{N})^+$ - clampowany iloczyn skalarny
	* wartości ujemne do $0$
* Suma składowych od każdego światła w scenie
* $c_{light_i}$ - kolor $i$-tego światła
* $f_{lit}$ - funkcja oddziaływania światła na powierzchnię
	* jeśli funkcja stała = kolor powierzchni - model Lambertowski
* Bardziej skomplikowane modele - uwzględniają np. chropowatość powierzchni

## Światło punktowe
* Położenie
* Intensywność
* Emisja światła w każdym kierunku w ten sam sposób
* Daje uproszczoną możliwość generacji cienia
	* ostra granica cienia

## Światło reflektorowe
* Wariacja światła punktowego
* Ograniczone do stożka
	* punkty w zasięgu pierwszego stożka są całkowicie oświetlone
	* od końca pierwszego stożka do całej szerokości następuje spadek oświetlenia od pełnego do $0$
* Dodatkowe parametry
	* początek spadku
	* całkowita szerokość

## Obszarowe źródło światła 
* Efekt półcienia - gładkie granice cienia
* Traktowanie jako wiele punktowych źródeł światła
	* problem z próbkowaniem punktów - wpływa na ostateczny wynik
* Wyliczanie osi przecięcia i granic półcienia

## Aliasing
* Pożądany efekt - gładkie przejście między wartościami pikseli
* Aliasing - próbkowanie sygnału ze zbyt małą częstotliwością
	* problem pojawia się przede wszystkim na krawędziach

## Materiały
* Czym jest materiał
	* opis wyglądu obiektu w scenie
	* służą do symulacji interakcji światła z otoczeniem
* Różne materiały odbijają światło w różnych kierunkach i absorbują różną jego ilość

## Odbicia
* Lustrzane
	* idealne odbicie
	* funkcja reflect
* Połyskliwe
	* promienie odbite - idealne odbicie + odchylenia
* Rozproszone
	* promień odbity może odbić się w dowolnym kierunku w półkuli otaczającej punkt


## Model oświetlenia Phonga
* Suma składowych
	* otoczenia
	* rozproszenia
	* odbicia
* Poza modelem oświetlenia jest model cieniowania

### Otoczenie
* $I=k_aI_a$
* $k_a$ - współczynnik otoczenia
* $I_a$ - intensywność otoczenia sceny / źródła światła
	* element globalnego oświetlenia

### Rozproszenie
* $I = k_d(\vec{L} \cdot \vec{N})I_d$
* $k_d$ - współczynnik rozproszenia
* $\vec{L}$ - wektor w kierunku źródła światła
* $\vec{N}$ - wektor normalny
* $I_d$ - intensywność światła dla rozproszenia

### Odbicie
* ang. specular
* Rozbłysk na powierzchni
* $I = k_s(\vec{V}, \cdot \vec{R})^n I_s$
* $k_d$ - współczynnik odbicia
* Zależne od obserwatora
	* $\vec{V}$ - wektor w kierunku obserwatora
	* odbicie zmienia wartość ze zmianą położenia obserwatora
* $\vec{R}$ - wektor światła odbitego
* $n$ - współczynnik połyskliwości
* $I_S$ - intensywność światła dla odbicia


## Modele cieniowanie
### Cieniowanie płaskie
* Kolor dla każdego wielokąta liczony raz
	* każdy piksel w jednym wielokącie
* Obliczenia dla punktu leżącego w środku wielokąta
* Wykorzystujemy wektory normalne do wierzchołków

### Cieniowanie Gourauda
* Barwa wyznaczana jest w każdym wierzchołku
* Piksele z wnętrza wielokąta są interpolowane z wierzchołków
* Działa dobrze do pewnego momentu
	* dobre dla powierzchni matowych
	* dla połyskliwych pojawiają się artefakty ze względu na interpolację po wierzchołkach
	* charakterystyczne krzyże
* Obliczenia w vertex shaderze
	* obliczone wartości przekazywane do pixel shadera
	* pixel shader bierze interpolowaną wartość z vertex shadera i przekazuje na wyjście

### Cieniowanie Phonga
* Obliczenia barwy dla każdego piksela ekranu
* Interpolowane są wektory normalne i pozycje
* Vertex shader zapisuje wektory normalne i pozycje
* Pixel shader odczytuje interpolowane wartości i wykorzystuje do obliczeń
* Pozbawione błędów poprzedników
