# Biometria podpisu odręcznego (2025-11-13)

## Rodzaje biometrii podpisu
* Metody off-line
	* obraz na papierze, zbiór punktów na płaszczyźnie
	* kolejność występowania elementów podpisu nie jest rejestrowana
* Metody on-line
	* rejestracja procesu podpisywania się
	* za pomocą jakiegoś tabletu
	* dodatkowo informacja o zmianie w czasie, nacisku końcówki pióra, kąta orientacji pióra
	* informacje dynamiczne

## Nazewnictwo
* Obraz podpisu
	* pojedyncza realizacja podpisu
* Podpis
	* klasa wszystkich możliwych obrazów podpisu tego samego typu dla danej osoby
	* inne typy (inicjały, tylko nazwisko, imię i nazwisko) są traktowane jako inne podpisy
* Wykresy
	* wykres xy - położenie punktów
	* wykresy dynamiczne (od czasu)

## Rodzaje fałszerstwa podpisów
* Podpisy obce
	* B nie ma żadnych informacji o podpisie A
	* w praktyce podpisy innych osób wykorzystywane są jako próby fałszerstwa
* Fałszerstwa proste
	* B zna elementy podpisu A
* Fałszerstwo zaawansowane
	* B może obserwować jak A się podpisuje
	* B ma dostęp do obrazów podpisu A w celu treningu
	* B ma możliwość obserwacji podpisu A podczas fałszowania
	* B ma możliwość przekalkowania podpisu A
	* dynamika i tak jest bardzo ciężka do naśladowania

## Pozyskiwanie danych
* Metody off-line - skanowanie
	* wrażliwe na rozdzielczość skanowania
	* 600 dpi raczej jest wystarczające
	* przy lepszej rozdzielczości można oszacować siłę nacisku po grubości
* Metody on-line - wykorzystanie tabletów graficznych
* Tablety do zastosowań ogólnych
	* próbkowanie 100-200 Hz jest wystarczające
	* pomiar również po oderwaniu pióra
* specjalizowane tablety do biometrii podpisu
	* mniejsza powierzchnia do pisania
	* dedykowane narzędzia deweloperskie

## Segmentacja
* Wyodrębnienie z tła
	* lokalizacja położenia podpisu
	* usunięcie tła i zakłóceń
	* progowanie
	* utworzenie obrazu szkieletowego
* Podział na segmenty
	* jednorodny - wykorzystanie ustalonej siatki, np. prostokątnej
		* prosty ale wrażliwy na deformacje podpisu
		* wymaga dobrego wyrównania położenia
	* niejednorodny - poszukiwanie spójnych części podpisu w sensie wybranego wskaźnika
		* elementy tworzące spójne figury
		* odrębne pociągnięcia pióra

### Segmentacja w metodach on-line
* Redukcja liczby punktów (resampling)
	* eliminuje szumy
	* jednorodna - odrzucanie co k-tego punktu
	* niejednorodna - odrzucenie punktów w segmentach o niskiej krzywiźnie
* Podział na segmenty
	* wykorzystanie informacji statycznej
		* podniesienia pióra
		* lokalne ekstrema składników (np. nacisku)
	* wykorzystanie informacji dynamicznej
		* ...

## Wyznaczanie cech
* Cechy globalne
	* własności geometryczne obrysu
	* liczba pętli
	* liczba przecięć
	* nachylenia linii
	* grubość linii
	* wartości średnie i odchylenia standardowe elementów podpisu
	* własności obrazów po przekształceniach morfologicznych
* Cechy lokalne
	* wybrane cechy globalne policzone dla segmentów
	* lokalne deskryptory obrazów: LBP, cechy Gabora

### Metody off-line
* Dylatacja / erozja
	* różne jądra filtrów
	* zostawia elementy zgodne z orientacją filtra
	* np. rozpoznawanie nachylenia podpisu, pole powierzchni po filtrowaniu

### Metody on-line
* Momenty statystyczne
* Cechy globalne
	* czas trwania realizacji podpisu - bardzo istotne
	* współczynniki trendów liniowych
	* prędkość i przyspieszenie prowadzenia pióra
	* cechy po wstępnej filtracji (np. falkowej)
	* miejsca przejść przez zero (cechy dla metod zero-crossing)

### Dobór cech
* W praktyce
	* zbieramy tyle cech ile jesteśmy w stanie
	* eliminujemy cechy skorelowane
	* dobór najbardziej rozróżniających cech

## Rozpoznawanie podpisów

### Grupowanie cech globalnych
* Cechy widoczne
	* łatwe do oszacowania przez fałszerza na podstawie wykresu xy
* Cechy ukryte
	* trudne lub niemożliwe do oszacowania na podstawie wykresu xy podpisu
	* przyspieszenia i prędkość pióra, orientacje, siły nacisku
* Niechlujny podpis trudniej sfałszować

### Rozpoznawanie w podprzestrzeni cech ukrytych
* Grupowanie podpisów podocnych w sensie odległości w podprzestrzeni cech widocznych
	* podobne wizualnie
* Klasyfikacja podprzestrzeni cech ukrytych
	* w przestrzeni cech ukrytych podpisy tej samej osoby powinny być blisko, a różnych osób daleko

### Klasyfikacja cech
* Klasyfikatory neuronowe
	* perceptron wielowarstwowy
* SVM
* Warianty klasyfikacji
	* osobny klasyfikator dla każdego podpisu - typowe do weryfikacji - problem z liczbą danych
	* wspólna funkcja klasyfikująca dla wszystkich podpisów - typowe dla identyfikacji
* W praktyce - sieci syjamskie

### Dynamiczne marszczenie czasu
* Dwie realizacje tego samego podpisu nie muszą zajmować tyle samo czasu
* Liniowe przyporządkowanie nie jest idealne
* Przy nieliniowym przekształceniu może być wiele punktów z jednej krzywej mapowanych na jeden z drugiej
* Jak to działa
	* możemy nanieść przebiegi na osie układu współrzędnych
	* zaczynamy od punktu (1,1)
	* znaleźć takie przejście, żeby skończyć w punkcie (n,n)
	* dalej można przejść albo w obu krzywych do kolejnej próbki (na skos na wykresie) albo pójść dalej tylko na jednej krzywej (pionowo lub poziomo na wykresie)
	* wybór przejścia, które daje najmniejszą różnicę
* Jest błąd na wykresie na slajdzie
* W praktyce stosuje się ograniczenia na dynamiczne marszczenie czasu
	* ograniczenie ścieżki na wykresie do paska albo równoległoboku

## Przykładowe pytanie
* Narysować ścieżkę DWT dla pokazanego dopasowania krzywych
* Rodzaje fałszerstw
* Metody online/offline i różnice (cechy dynamika)
* Jakie cechy są wyznaczane