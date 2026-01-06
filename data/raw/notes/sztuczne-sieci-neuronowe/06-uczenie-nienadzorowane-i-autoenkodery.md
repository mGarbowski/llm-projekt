# Uczenie nienadzorowanie - autoenkodery i inne 

## Dziedziny uczenia maszynowego
* Uczenie nadzorowane
* Uczenie nienadzorowane
	* zbiór danych bez powiązania wejście-wyjście
* Uczenie ze wzmocnieniem

### Uczenie nienadzorowane
* Większość danych jest nieopisanych
* Anotacja jest kosztowna (przekształcenie w problem uczenia nadzorowanego)
* Generalnie, ludzie uczą się w sposób nienadzorowany
* Niektóre problemy mogą być zbyt trudne dla ludzi (tak żeby pokazać rozwiązania)
	* np. odpowiedzi LLM

### Uczenie nadzorowane a reprezentacje
* Pomiędzy warstwami w sieci neuronowej
* Wiedząc który przykład należy do której klasy można stworzyć taką funkcję i model żeby je oddzielać z jakąś dokładnością
* Model tworzy taką reprezentację, która będzie użyteczna do zadania

## Autoenkoder
* Sieć mapuje wejście na przestrzeń ukrytą $z$
* Kolejna sieć odtwarza z przestrzeni ukrytej oryginalne wejście
* Mamy funkcję celu - błąd rekonstrukcji
* Wymuszamy, żeby przestrzeń ukryta była mniejszej wymiarowości niż wejście
	* nie można po prostu zakodować wszystkich pikseli w naiwny sposób
* Pozwala w sposób nienadzorowany uczyć się relacji pomiędzy obiektami
* W przestrzeni ukrytej dane wejściowe są pogrupowane tak żeby zmniejszać błąd rekonstrukcji
* Obiekty semantycznie podobne mają dużą szansę znaleźć się blisko siebie

### Autoenkodery niedopełnione
* Wejście i wyjście są tej samej wymiarowości
* Gdzieś po środku jest warstwa bottleneck - mniejszej wymiarowości

### Autoenkodery przepełnione
* Warstwa ukryta jest większej wymiarowości niż wejście i wyjście
* Regularyzacja na warstwie ukrytej. np. L2

### Rzadkie autoenkodery
* Wiele wymiarów przestrzeni ukrytej
* Każdy obrazek wykorzystuje tylko ograniczoną liczbę neuronów
* Regularyzacja L1 - dąży do tego żeby jak najwięcej wag miało dokładnie 0
* Regularyzacja w oparciu o dywergencję Kullbacka LEiblera

### Autoenkodery odszumiające
* Uczenie odszumiania przykładów
* Najpierw dodajemy szum do obrazka i wtedy wrzucamy do sieci
* Porównujemy wyjście z oryginałem bez szumu
* Pozwala na wykształcenie bardziej ogólnych reprezentacji

### Architektura UNet
* Dekoder ma odwrócone warstwy względem enkodera
	* np zamiast pooling - upsampling i konwolucja
* Skip connections - warstwa jest połączona nie tylko z kolejną ale też z symetryczną w drugiej części
* Wiele wewnętrznych reprezentacji z różnym poziomem szczegółowości
	* w głębokich warstwach są wysokopoziomowe, wysokoczęstotliwościowe cechy
	* w pierwszych warstwach są wysokoczęstotliwościowe cechy (np. tekstura)
* Model w pełni konwolucyjny
	* tylko warstwy splotowe, pooling i up-conv (upsampling i splot)

## Zastosowania autoenkoderów
* Redukcja wymiarowości / kompresja
	* lepsza kompresja obrazów niż JPEG
	* kosztowne obliczeniowo - dlatego jeszcze nie został wyparty
	* redukcja wymiarowości w przetwarzaniu wstępnym
* Detekcja anomalii
	* Kodowanie przykładów do przestrzeni ukrytej
	* Nowy obrazek zupełnie nie pasujący ląduje daleko od innych przykładów w przestrzeni ukrytej
* Wyszukiwanie obrazów
	* wyszukiwanie semantycznie podobnych obrazów na podstawie dystansów w przestrzeni ukrytej

## Samo / słabo nadzorowane uczenie
* Przewidywanie części wejścia na podstawie pozostałej części
	* domalowywanie obrazka
* Uczenie relacji między fragmentami obrazków
	* można pociąć obrazek na 9 części
	* pozwala na naukę relacji między nimi

### Uczenie kontrastywne
* Porównywanie i różnicowanie obiektów w przestrzeni reprezentacji
* Minimalizowanie dystansu między podobnymi obiektami, maksymalizowanie dystansu między różnymi
* Przecięcie tego samego zdjęcia na pół - oba po zakodowaniu w przestrzeni ukrytej powinny być blisko siebie
* Fragmenty innych obrazów powinny być kodowane daleko od siebie
* Przykładowe metody
	* sieci syjamskie - dwie kopie sieci
	* triplet loss - odległość od pozytywnych i negatywnych przykładów
	* SimCLR - uczenie w oparciu o augmentacje

### Modele multimodalne (CLIP)
* Uczenie kontrastywne na parach obraz - opis tekstowy
	* zbliżanie do siebie obrazu i pasującego podpisu
	* oddalanie od siebie obrazów i niepasujących podpisów
* Zastosowania
	* zero-shot klasyfikacja
	* segmentacja
	* porównywanie cech
	* warunkowanie dużych modeli generatywnych

### Modele językowe
* Uczenie wpół nadzorowane
	* np. przewidywanie słów w zdaniu (ukrycie słowa w istniejącym zdaniu)

## Podsumowanie
* Metody nadzorowane posiadają swoje ograniczenia i wymagają kosztownego opisywania danych
* Metody nienadzorowane np. autoenkodery pozwalają na uczenie się niskopoziomowych reprezentacji danych
* Metody samonadzorowane mogą być stosowane jako alternatywa do metod nienadzorowanych przy uczeniu reprezentacji
