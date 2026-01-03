# Kompresja sekwencji obrazów

## Kodowanie wideo
* Podobna do kompresji obrazów
* Sekwencje obrazów charakteryzuje duża redundancja czasowa danych
	* kolejne klatki są do siebie bardzo podobne
* Żeby uzskać najlepszą kompresję nie można traktować każdej ramki oddzielnie
* Dodanie dodatkowego modelu ruchu przed koderem obrazów minimalizuje redundancję czasową
	* kodowane są różnice między przewidywaniem/predykcją a danymi oryginalnymi

## Koder wideo
* Kompensacja ruchu
* Estymacja ruchu
	* wektory ruchu są używane przez moduł kompensacji i rekonstrukcji
* Rekonstrukcja
* Analogiczne kroki jak do kompresji obrazu
	* DCT / IDCT
	* Kwantyzacja / odwrotna kwantyzacja
	* Wybieranie zigzag
	* RLE
	* VLC
* Korki w hybrydowym koderze wideo
	* predykcja
	* transformata
	* kwantyzacja
	* kodowanie entropijne
	* rekonstrukcja

### Prosta predykcja międzyobrazowa
* Najłatwiej ograniczyć ilość danych do zakodowania przez odjęcie od kodowanej ramki poprzedniej ramki
	* jeśli nie ma ruchu kamery to tło raczej się nie zmienia
* To nie wykorzystuje informacji o ruchu w sekwencji

### Estymacja ruchu
* Przetwarzanie bloków obrazów (luminancji)
	* typowo makrobloki 16x16 px
	* porównanie z sąsiadującymi obszarami w ramce referencyjnej
	* znalezienie najbardziej podobnego
	* predykcja pobrana z obszaru referencyjnego dla najlepszego podobieństwa
* Szuka się obszaru najbardziej podobnego
	* podobieństwo wg. kryterium SAD, MSE
	* pełne kodowanie oznaczałoby wykonanie wszystkich kroków (DCT, kwantyzacja, ...)
* Wektor ruchu - przesunięcie między aktualnie kodowanym makroblokiem a jego predykcją z obszaru referencyjnego
	* zakodowanie wektora też zajmuje bity w strumieniu
	* nie zawsze opłaca się znajdować najlepsze dopasowanie, jeśli niedokładna wartość pozwala zaoszczędzić bity na kodowaniu wektora

### Wektory ruchu
* Wynikiem estymacji ruchu jest zbiór wektorów ruchu
* Oddzielne wektory dla każdej partycji inter
* Predykcyjne kodowanie wektorów
* Zwykle odzwierciedlają ruch obiektów
* Gdy wektor ruchu jest taki sam jak jego predykcja (z sąsiednich bloków) można to sygnalizować flagą
	* częste dla zerowych wektorów

### Złożoność estymacji ruchu
*  Bardzo złożona obliczeniowo
	* cztery zagnieżdżone pętle przy pełnym przeszukiwaniu
* Miary dopasowania
	* SAD - Sum of Absolute Differences (najczęściej)
	* SSD - Sum of Squared Differences
	* SADT - Sum of Absolute Differences Transformed
	* RD - Rate-Distortion (stosunek zniekształceń do stopnia kompresji)

### Szybkie wyznaczanie wektorów ruchu
* Nie przeszukuje się wszystkich możliwych przesunięć superbloku
* Estymacja ruchu jest nabardziej złożonym modułem kodowania, potrzeba przyspieszenia
* Przeszukiwanie w przestrzeni wektorów zaczyna się od $(0,0)$
* Porównuje się środek z 8 kandydatami różniącymi się we współrzędnych o -4, 0 lub 4
* Wybiera się najlepszy i zostaje nowym środkiem
* Porównuje się środek z 8 kandydatami różniącymi się we współrzędnych o -2, 0 lub 2
* itd.
* Wartości nie muszą być całkowite, można połowić zasięg przeszukiwania poniżej $1$
* Zakłada przesunięcie bloku o ułamkowe piksele
	* trzeba by wyznaczyć wartości pikseli ułamkowych (interpolacja)

### Podpikselowa estymacja ruchu
* Wektory ruchu mogą mieć wartości niecałkowite
	* typowo 1/4, 1/2, 3/4 dla luminancji
	* ułamki n/8 dla chrominancji 4:2:0 (o 1 rząd mniejsze niż luma, bo jest podpróbkowana)
* Interpolację wykonuje się przez dwuwymiarowe filtry o skończonej odpowiedzi impulsowej (SOI)
	* np. najpierw poziomy, potem pionowy

### Kompensacja ruchu
* Odjęcie obszarów referencyjnych od kodowanych makrobloków
	* powstają makrobloki różnicowe
	* z nich można złożyć obraz różnicowy z kompensacją ruchu
* Po kompensacji następuje zakodowanie obrazu różnicowego koderem obrazów
* Efektywna estymacja ruchu
	* mały poziom wartości w makroblokach różnicowych
	* bardziej efektywna kompresja
	* koszt wektora ma znaczenie (ważna nie tylko SAD)
* Wykorzystuje się bufor ramek referencyjnych
* Polega na odjęciu od ramki obrazu referencyjnego
	* obraz różnicowy mówi o ruchu między ramkami
	* niesie mniej informacji - kompresja

## Grupa obrazów
* GOP - group of pictures
* Ramki typu I (Intra)
	* nie ma estymacja ruchu
	* kodowana jak obraz albo analogicznie do obrazu
* Ramki typu P
	* jednokierunkowa estymacja ruchu
	* odwołują się do poprzedniej ramki P lub I
* Ramki typu B
	* dwukierunkowa estymacja ruchu
	* wstawiane między ramki P, a ramki I
* Należy dobrać liczbę ramek typu B
* Grupa obrazów to wszystkie obrazy od ramki I do następnej ramki I (nie licząc jej)
* Grupa otwarta - referencje mogą wychodzić poza GOP (np. odwołać się do poprzedniej grupy)
* Grupa zamknięta - referencje tylko w obrębie GOP
* Można stosować hierarchiczne ramki B
	* albo odwołują się tylko do ramek I, P
	* albo też do innych ramek B (hierarchia warstwowa)
* Predykcja wewnątrzobrazowa (Intra)
	* kompresja wideo
	* na podstawie ramki I dokonuje się predykcji dla kolejnych ramek
	* zamiast całych ramek koduje się korekcję błędu predykcji

## Plastry (slices)
* Kodowanie w porządku rastrowym
* Ciąg pewnej liczby makrobloków
* Dla każdego plastra powstaje spójny strumień, który tworzy jednostkę dostępu
* Można określić np. według liczby bitów jaka ma przypadać na jeden plaster
* Błąd występujący w jednym plastrze nie przenosi się na inny

## Dekoder wideo
* Odwrotne kroki do kodera
	* Bufor danych
	* VLD
	* RLD
	* Odwrotny zigzag
	* odwrotna kwantyzacja
	* IDCT
	* Rekonstrukcja
* Odwrotna kolejność przetwarzania
* Znacznie mniejsza złożoność obliczeniowa
	* nie ma potrzeby znalezienia najlepszego trybu
	* informacji o trybach dekodowana ze strumienia

## Standardy kompresji
* W ramach organizacji ISO/IEC - standardy MPEG
* W ramach organizacji ITU-T - standardy H.261, H.262, ...
* Standardy są ze sobą połączone, powstają we współpracy
* Firmy tworzą własne standardy żeby uniezależnić się od patentów
* Kolejne standardy dają większą przepływność bitową, większe PSNR
	* kosztem większej złożoności obliczeniowej, zwłaszcza w koderach

### MPEG-1
* Pierwszy standard
* Przepływnośc do 1.5Mbit/s
* Próbkowanie 4:2:0
* Kompresja wideo dla internetu i płyt CD
* Parametry
	* szerokość max 768px
	* wysokość max 576
	* max 396 makrobloków
	* framerate max 30Hz
	* zakres wartości wektorów ruchu [-64, 63.5] px

### MPEG-2
* Rozszerzenie i modyfikacja MPEG-1
* Kompresja wideo dla telewizji cyfrowej standardowej i wysokiej rozdzielczości DVD
* Różne poziomy i profile określające parametry strumienia
* Możliwość kodowania z przeplotem albo bez przeplotu
* Próbkowanie 4:2:0, 4:2:2, 4:4:4
* Wektory ruchów z dokładnością do 1/2 piksela
* Różnicowe kodowanie wektorów ruchu

### MPEG-4
* Kompresja wideo ogólnego przeznaczenia
* Reprezentacja sceny jako złożenia obiektów (media objects)
	* wizyjnych, dźwiękowych, ogólnego typu
	* naturalnych lub sztucznych
* Możliwość łączenia obiektów w obiekty złożone
* W praktyce podejście obiektowe się nie sprawdziło
* Multipleksowanie i synchronizacja danych związanych z każdym obiektem
* Elastyczność i reużywanie tej samej treści
* Kodowanie kształtu i tekstury
* Transofmracja dopasowana do kształtów obiektów
* Interkatywność
	* zmiana położenia obserwatora na scenie
	* nawigacja po scenie
	* przesuwanie obiektów wewnątrz sceny
	* wybór wersji językowej
* Różne kodery dla różnych typów danych
* Zabezpieczenie praw autorskich
* Profile simple / advanced - kodowanie prostokątnych ramek obrazu

### H.261
* Przepływność $p * 64kbit/s$
	* $p=1..30$
* Kompresja dla wideokonferencji
* Próbkowanie 4:2:0
* Tylko ramki I i P
* Wektory ruchu z dokładnością do piksela w zakresie 15px
* Różnicowe kodowanie wektorów ruchu
* Pomijanie ramek w celu dostosowania strumienia do pojemności kanału

### H.263
* Rozszerzenie H.261
* Rozdzielczości
* Kompensacja z dokładnością do 1/2 piksela
* Ulepszone predykcyjne kodowanie wektorów ruchu

### H.263+
* Możliwość wyboru ramki referencyjnej spośród wcześniej nadanych
* Dowolna rozdzielczość
* Ramki typu B

### H.264 / MPEG-4
* Predykcja w trybie intra
* Różne kształty bloków do estymacji/kompensacji
* Wektory ruchu wyznaczane z dokładnością do 1/4 piksela
	* ekstrapolacja
	* mogą wykraczać poza granice obszaru referencyjnego
* Możliwość stosowania wielu ramek referencyjnych
	* hierarchiczne ramki B
* Tryb kodowania ramkowy (bez przeplotu) lub polowy (z przeplotem)
	* wybór na poziomie obrazu lub makrobloku
* Transformata całkowitoliczbowa wymaga arytmetyki 16-bitowej
* Zmniejszenie bloku kodowego do 4x4 próbek
* Adaptacyjne kodowanie entropijne
* Próbkowanie 4:2:0, 4:2:2, 4:4:4
* Plastry typu I, P, B (hierarchiczne uogólnione ramki B), SI, SP
* Filtr zmniejszający efekt blokowy
	* adaptacyjny, nieliniowy, wygładzający

#### Profile
* Main
* Extended
* Baseline
* High
* High 10
* High 422
* High 444

## Predykcja Intra 16x16
* Ekstrapolacja zrekonstruowanych pikseli
	* powielenie pionowe
	* powielenie poziomie
	* powielenie średniej
	* hiperpłaszczyzna
* Dla kolejnych standardów i innych rozmiarów bloków jest więcej trybów

## Predykcja Inter
* Podział bloku na mniejsze bloki
	* bok dzielony przez 2
	* może nie być kwadratem
* Pozwala lepiej odzwierciedlić obiekt poruszający się na jakimś tle

## Transformacje
* Operajce macierzowe przybliżające DCT
* W kolejnych standradach rozmiary macierzy są coraz większe

## Kwantyzacja
* Mnożenie i przesunięcie bitowe w dół zamiast dzielenia przez krok kwantyzacji
* Parametr kwantyzacji QP
	* liczby załkowite $\in [0,52]$
	* określa krok kwantyzacji w skali logarytmicznej
	* po sześć dyskretnych wartości QP na oktawę wartości kroku kwantyzacji
	* oktawa to $6dB$

## Kodowanie entropijne
* Elementy Składni
	* współczynniki
	* wektory ruchu
	* predykcje
* Binaryzacja - kodowanie tylko kodami przedrostkowymi
* CAVLC - kontekstowo adaptacyjny koder zmiennej długości
	* dostępny tylko w H.264
* CABAC - kontekstowy adaptacyjny binarny koder arytmetyczny
* Serializacja
	* np. zigzag
	* uszeregowanie danych w strumieniu kodowym (wyjściowym)

### Modelowanie kontekstu
* Na początku mamy zbinaryzowany element składni
* wyznacza się dla niego offset - oddzielne zakresy dla poszczególnych typów
	* oddzielne modele prawdopodobieńśtw dla oddzielnych typów elementu składni
* Określenie przyrostu na podstawie sąsiednich elementów
	* i pozycji w zbinaryzowanym ciągu
* Połączenie offsetu i przyrostu daje etykietę kontekstu
* Etykieta kontekstu to adres wybierający model probabilistyczny lub tablicę kodową

### Strumień kodowy
* Sequence Parameter Set
* Picture Parameter Set
* IDR - ramka intra
	* zaczyna kodowanie
* Slice'y (plastry)
	* nagłówek
	* dane - sekwencja makrobloków
* Makroblok
	* typ
	* typ predykcji (intra / inter)
	* coded block pattern - flaga czy bloki lumy i chromy są zerowy czy nie
	* parametr kwantyzacji
	* dane (y, cb, cr)

## Regulacja stopnia kompresji
* Pożądana jest kompresja uzyskująca zakładany budżet bitowy i stabilność długości strumieni kodowych dla kolejnych ramek
* Regulowanie przez zmianę parametru kwantyzacji
	* im większy tym silniejsza kwantyzacja, tym większy krok
* Efekt zależy od złożoności treści wizyjnej
	* ilość szczegółów
	* aktywność ruchu
* Cel
	* maksymalizacja jakości (PSNR)
	* wykorzystanie przypisanego budżetu bitów
	* stabilność przepływności
