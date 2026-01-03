# Biometria tęczówki

## Budowa oka
* Tęczówka reguluje ilość wpuszczanego światła
* Tęczówki częściowo odpowiada za akomodację (ustawianie ostrości)

## Rozwój tęczówki
* Jest bardzo unikatowa
* Jest mocno niezależna od genotypu
* Formuje się w 8 tygodniu życia zarodka
* Hipoteza 1
	* struktura beleczek mięśniowych jest niezmienna aż do śmierci
	* wystarczy jedna rejestracja na całe życie
	* częściowo podważane przez nowe badania
* Hipoteza 2
	* procesy rzęskowe obecne przy formowaniu tęczówki są niezależne od genotypu

## Struktura tęczówki
* Za kolorową częścią są mięśnie
	* ułożone koliście
	* ułożone radialnie
* Włókna kolagenowe widoczne na zewnątrz
* Kołnierz oddziela strefę włoskowatą od strefą okołoźrenicznej

## Historia
* Bertillonage uwzględniał kolor tęczówki
* Pierwszy sensowny opis wdrożenia w 1987
	* Safir, Flom - okuliści
* Daugman 1992 - współczesna biometria tęczówki
	* pierwszy algorytm kodowania tęczówki oparty o dwuwymiarowy filtr Gabora
	* pierwsze urządzenie

## Pozyskiwanie obrazu

### Światło widzialne
* Zawodne dla ciemnych tęczówek
* Melanina w tęczówce pochłania ultrafiolet i światło widzialne
	* mało światła się odbija
	* krzywa absorpcji

### Bliska podczerwień
* Typowo 750-890nm
* Podczerwień jest w mniejszym stopniu pochłaniana
* Bardziej klarowne zdjęcia
* Nie wali po oczach - siatkówka jest nieczuła na podczerwień
	* nie reaguje źrenica
* Nie ma odbić na powierzchni oka tak jak w świetle widzialnym

### Problemy z pomiarem
* Mała głębia ostrości systemów optycznych
	* mały, ruchliwy, trójwymiarowy obiekt
	* potrzeba dużego otworu przesłony
* Wymagana współpraca osoby z maszyną
* Konieczne modelowanie i pomijanie zakłóceń
	* powieki, odblaski, rzęsy, włosy
	* zmiana wielkości źrenicy
	* marszczenie powierzchni tęczówki (nieliniowe)
	* spontaniczne obroty głowy
	* spojrzenia nie w osi optycznej kamery

### Normy ISO dotyczące pomiaru tęczówki
* Rozpiętość tonalna, kodowanie informacji
	* min 256 poziomów szarości
	* użyteczna informacja kodowana na co najmniej 7 bitach
	* odpowiedni kontrast pomiędzy tęczówką i białkówką
* Rozdzielczość
	* nie bardzo duża
	* w telefonach dopuszczalna niższa (już się tego i tak nie robi)
* Zakłócenia i położenie oka
	* 70% widoczności mięśnia tęczówki
	* średnica źrenicy nie większa niż 7mm
	* zalecane zdjęcie okularów i soczewek z nadrukami
	* wyśrodkowanie tęczówki na obrazie
* Natężenie oświetlenia podczerwonego
	* bezpieczne dla zdrowia

### Interoperacyjność pomiaru
* Wpływ oświetlenia na jakość rozpoznawania
	* obrazy z zakresach długości fal zgodnych z normą ISO dają się ze sobą porównywać dosyć dobrze

### Pomiar bez kooperacji
* Układy wielu kamer o zwiększonej rozdzielczości
	* szerokokątna do lokalizacji twarzy
	* wąskokątna do rejestracji tęczówki
* Deformowane lustra
	* jak w teleskopach astronomicznych

### Pozycja oświetlaczy podczerwieni
* Jak zamontować w otoczeniu kamery
* Umieszczenie za blisko osi optycznej kamery - efekt czerwonych oczu
* Zbyt duże odsunięcie od osi optycznej kamery - odblaski nachodzą na tęczówkę
* Oś optyczna nałożona na oś odbicia - bardzo duży odblask
* Poprawne ułożenia - odblask tylko na źrenicy

## Segmentacja
* Interesuje nas tylko tęczówka
* Założenia - tęczówkę i źrenicę można przybliżyć okręgiem
	* sprawdza się w praktyce
	* nie są koncentryczne (źrenica jest przesunięta w stronę nosa)
* Kształt powiek przybliżany krzywymi parabolicznymi
* Starsze metody słabo się przenosiły między kamerami
	* dużo parametrów do dostrojenia
* Współcześnie - sieci splotowe
	* potrzebny zbiór treningowy, segmentacja wykonana ręcznie
* Elementy do lokalizacji
	* granica wewnętrzna
	* granice zewnętrzna
	* zakłócenia górne i dolne (rzęsy, powieki)

### Lokalizacja zakłóceń
* Dodatkowy etap po lokalizacji
	* metody parametryczne
	* metody nieparametryczne - rozpoznawanie odbiegających tekstur
* Powstaje maska - zaznaczone piksele zawierające tęczówkę niezasłoniętą

### Korekcja kąta spojrzenia
* Odwrócenie w kierunku kamery
* Zastosowanie rozwinięcia Fouriera

## Reprezentacja
* Obraz surowy UNCROPPED / VGA
* Obraz kadrowany i maskowany
* Reprezentacja tęczówki w układzie biegunowym
* Rozwinięcie pierścienia do prostokąta - obraz w układzie biegunowym
	* zawsze taki sam rozmiar - rozciągnięty lub ściśnięty - liniowa deformacja
	* niezależny od rozwarcia źrenicy
	* niezależny od skali
	* niezależny od położenia tęczówki
* Mapa zakłóceń - maska binarna zakłóceń (powieki)
* Poziom jasności w funkcji kąta dla ustalonego promienia
	* dla jednego pierścienia na oryginalnym obrazie / paska na obrazie biegunowym
	* cechy tęczówki do rozpoznawania

### Cechy tęczówki
* Informacje o większych częstotliwościach (większe kształty)
	* mniejsze są bardziej podatne na szum
* Filtracja obrazu
	* Gabor, LoG, DoG, Haar
* Kwantyzacja
* Reprezentacja w postaci funkcji schodkowej - do przekształcenia w kod binarny

### Porównywanie binarnych kodów tęczówki
* Ułamkowa odległość Hamminga
* XOR na kodach tęczówki
* W mianowniku iloczyn masek - część wspólna niewymaskowana
* Korekcja obrotu głowy - można porównać z różnymi przesunięciami i znaleźć minimum
* Próg dopasowania ustalany empirycznie

### Własności statystyczne
* Rozkład normalny
* Dla różnych tożsamości 50% zgodności
* 4096 bitów - jak 4096 rzutów monetą
* Można łatwo oszacować jaki będzie błąd jeśli ma się jeszcze rozkład dla porównań tych samych tożsamości
* Kod Daugmana tęczówek bliźniąt jednojajowych jest różny
	* i dla porównań lewe/prawe oko

# Bezpieczeństwo sensorów tęczówki

## Systematyka fałszerstw
* Obraz statyczny
	* papierowy wydruk
	* obraz na ekranie
* Obraz dynamiczny
	* off-line - wiedza a priori - np. film
	* on-line - wiedza a posteriori - np. generowany na bieżąco deepfake 
* Sztuczne oko
	* żywe oko + tęczówka
* Prawdziwe oko
	* martwa tkanka
	* działanie pod przymusem

## Metody testowania żywotności
* Obiekt statyczny, pomiar pasywny
	* cechy 2D - analiza częstotliwościowa, temperatura
	* cechy 3D - analiza kształtu gałki ocznej, struktury mięśnia tęczówki (cienie)
	* analiza odbić Purkiniego (odbicia od soczewki i źrenicy)
* Obiekt dynamiczny, pomiar pasywny
	* spontaniczne ruchy źrenicy - trzeba nagrać film
	* ruchy hippus ok, 0.5Hz
* Obiekt statyczny, pomiar aktywny
	* trzeba np. poświecić
	* analiza stymulowanych odbić światła
	* analiza charakterystyki absorpcyjnej tkanki przy oświetlaniu światłem o różnej długości fali
* Obiekt dynamiczny, pomiar aktywny
	* świadome działanie - podążanie za punktem, mrugnięcia
	* odruch bezwarunkowy - dynamika zmian wielkości źrenicy pod wpływem zmiany natężenia światła

### Odbicia Purkiniego
* Oko składa się z wielu warstw
* Między warstwami są granice ośrodków - dodatkowe odbicia
* Nie będzie tego na wydruku

### Obrazowanie termiczne
* Drogie sensory

### Analiza częstotliwościowa
* Na obrazie z drukarki są widoczne kropki - raster drukarki
* Widać te częstotliwości przestrzenne w widmie
* Wykorzystuje się już zebrane zdjęcie
* Test żywotności
* dodatkowy składnik oceny jakości zdjęcia
* Np. w kwadratach po bokach od źrenicy
* Okienkowanie widma
* Wskaźnik żywotności (sztuczności)