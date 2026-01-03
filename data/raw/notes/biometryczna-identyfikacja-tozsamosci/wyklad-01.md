# Biometria odcisku palca
* Historia - nie na egzamin
* Sir Francis Galton
	* 1888
	* klasyfikacja punktów osobliwych
	* definicje minucje - detale Galtona
	* dzieło *Fingerprints*
	* podstawa współczesnej biometrii odcisków palca
* Alphonse Bertillon
	* system Bertillonage
	* metoda nieautomatyczna - pomiary długości kości, koloru tęczówki
	* w końcu znaleziono 2 osoby a identycznych parametrach
	* pytanie na egzamin - czemu ta metoda jest zła?
* Sir Edward Richard Henry
* Edmond Locard
	* zasada wymiany

## Paradygmaty biometrii odcisku
* Cechy muszą być unikatowe w populacji
* Zmienność w populacji jest na tyle systematyczna, że pozwala grupować podobne odciski
	* klasyfikacja
	* ułatwienie przeszukiwania

## Przedmioty obserwacji
* Elementy podstawowe
	* grzbiety - kolor ciemny
	* doliny - kolor biały
	* kolory na skanach ustandaryzowane przez ISO
	* grzbiety mogą się kończyć albo rozwidlać
* Poziom globalny
	* rdzeń i punkty osobliwe
	* punkty osobliwe - 3 układy
		* wir
		* pętla
		* delta
	* punkty osobliwe to podstawa do klasyfikacji
	* rdzeń
		* najbardziej na północ wysuniętym punktem osobliwym typu wir lub pętla
		* do wyrównania obrazów przed porównaniem
* Poziom lokalny
	* minucje
* Poziom szczegółów
	* pory
	* brodawki
	* zmarszczki
	* blizny
	* linie zdegenerowane

### Lokalizacja punktów osobliwych
* Wektor dla każdego puntu osobliwego
	* rotacje
	* dzisiaj zamiast tego używa się sieci neuronowych

### Klasyfikacja Henry'ego
* 8 klas

### Minucje
* Detale Galtona
* Minucje podstawowe
	* zakończenie
	* rozwidlenie
* Minucje złożone
	* np. oczko - 2 rozwidlenia
	* nie uczyć się na pamięć

### Poziom szczegółów
* Linie wcale nie muszą być równe
* Pory
	* pozwalają na stworzenie testów żywotności
	* trudno podrobić pory

### Biometria vs AFIS
* Kryminalistyka
	* Automatic Fingerprint Identification System
	* FBI - 200 mln kart daktyloskopijnych
	* różna jakość danych - zbierane np. z miejsc przestępstw
	* czas identyfikacji rzędu minut
* Biometria
	* sensory z kontrolą jakości
	* czas identyfikacji rzędu ułamków sekund

## Pozyskiwanie obrazu

### Metody
* Metody off-line
	* digitalizacja odcisków z kart
	* digitalizacja odcisków utajonych (zbierane z miejsca zbrodni) - pędzel, proszek, lampa UV
* Metody on-line

#### Technika pojemnościowa
* Matryca kondensatorów
* Sensor oddzielony od ekranu (np. w laptopach)
* Typowo rozdzielczość 300 dpi
* Ładunek zamieniany w przetworniku AC
* Nie działa z mokrym palcem

#### Technika optyczna
* Jak aparat fotograficzny
* Pryzmat albo matryca pryzmatów
* Światło IR
* Rejestracja światła na matrycy CCD
* Rozdzielczość 400-600 dpi


#### Technika naciskowa
* Matryca sensorów nacisku
	* sensory piezoelektryczne
* Nie spopularyzowała się

#### Technika termiczna
* W starych laptopów
* Pasek po których przesuwa się palec
	* oszczędność miejsca i kosztu sensorów
* Rekonstrukcja obrazu z kilku skanów w trakcie przesuwania palca

#### Technika ultradźwiękowa
* Sensory podekranowe

#### Technika bezdotykowa
* Droga
* Wyparta przez biometrię twarzy

## Zakłócenia
* Odcisk palca to obraz trójwymiarowej powierzchni
	* duża zmienność wewnątrzklasowa
* Deformacje liniowe i afiniczne
	* przesunięcia i obroty palca - mniejszy problem
* Deformacje nieliniowe
	* zniekształcenia elastyczne
	* różna siła docisku palca do sensora
* Różne obszary pomiarowe
	* inny fragment palca na małym sensorze
* Własność skóry
	* sucha, spocona, chora, zraniona
	* grzbiety nie kontaktują się z powierzchnią sensora
	* nieciągłość linii
	* sklejenia linii

## Przetwarzanie wstępne
* Uwypuklane grzbietów i dolin
* Wyrównanie jasności i ostrości obrazu

### Filtry Gabora
* Bank filtrów w różnej skali
* Sinusoida spleciona z Gaussem

### Segmentacja
* Pozbycie się tła
* Wynikiem jest obraz z nałożoną maską
	* maska to obraz binarny
	* mnożenie wartości piksela przez 0 lub 1
* Analiza histogramu poziomów jasności
	* średnie poziomy jasności - raczej tło
* Średnia wariancja w obszarach

## Klasyfikacja metod rozpoznawania
* Porównywanie na poziomie globalnym
	* level 1 fingerprint matching
	* traktowanie obrazu jako tekstury
* Porównywanie na poziomie lokalnym
	* level 2
	* mapy minucji
	* położenie i orientacja mnucji
	* podejście wywodzące się z daktyloskopii
	* poszukiwanej maskymalnej liczby par pasujących minucji
* Porównywanie na poziomie szczegółów
	* level 3
	* własności szczegółów
	* kształt, położenie, orientacja
	* raczej testowanie żywotności niż samo rozpoznawanie

### Potrzeba metod nieminucyjnych
* Kiedy minucji jest za mało

### Rodzaje obrazów
* Potok
	* obraz w skali szarości - bmp z sensora
	* obraz binarny - po progowaniu obrazu szarości
	* obraz szkieletowy - stała grubość linii - 1px

## Estymacja minucji
* Na obrazie szkieletowym to trzy IF-y na liczbę sąsiadów
	* bo linie mają grubość 1 piksela
* Zakłócenia powodują zwielokrotnienie minucji
* Końce linii na krawędziach obrazu nie są minucjami
* Filtracja minucji
	* reguły heurystyczne
	* np. za blisko siebie, za krótka przerwa

## Mapa minucji
* Norma ISO
* Minucja oznaczona przez $(x, y, \theta)$
* Problem deformacji odcisków

## Kroki dopasowania map minucji
* Przyjmujemy tolerancję - obszar dopuszczalnego błędu
	* blisko
	* pasująca orientacja
* Wskaźnik dopasowania
	* popularny - liczba pasujących / średnia liczba w obu obrazach
* Zmodyfikowane wskaźniki
	* ważenie minucji jakością - lepsza jakość ma większy wpływ na wynik
	* mianownik - liczba minucji w części wspólnej obrazów (po segmentacji)

## Przykładowe pytania na egzamin
Dla każdej z poniższych propozycji orzec czy jest to minucja podstawowa

Poprawne: zakończenie i rozwidlenie