# Potok graficzny

## Po co GPU
* Istotne kwestie
	* ilość danych przetwarzanych w tym samym czasie
	* szybkość przetwarzania każdego elementu
	* ilość danych transferowanych w jednostce czasu (przepustowość pamięci)
	* czas przesyłania danych
* Wg. taksonomii Flynna - SIMD
	* single instruction, multiple data
* Wątki, grupy wątków i grupy grup
* Każde wywołanie shadera dla fragmentu ma swój wątek, rejestry i niedużo pamięci
* Grupa wątków wykonująca ten sam program - Warp
* Grupy wątków są harmonogramowane do rdzeni cieniowania
* Warp-swapping
	* maskowanie opóźnień
	* np. pobieranie informacji z tekstury
* Dynamic branching
	* w przypadku gdy wszystkie wątki wykonują tę samą gałąź, druga nie ma znaczenia
	* odrzucanie gałęzi kodu, których wyniki są niepotrzebne
	* jeśli którykolwiek wątek wchodzi w inną gałąź to trzeba wykonać obie i odrzucić niepotrzebne wyniki

### Synchronizacja wątków
* Stosuje się bariery, żeby zapewnić, że wszystkie wątki zakończyły obliczenia
* Szybciej będzie przekopiować macierz do pamięci dzielonej grupy wątków i zastosować barierę niż wykonywać obliczenia na pamięci globalnej (która jest wolniejsza)

## Potok graficzny
* Potok renderujący - generacja / rendering obrazów 2D
	* kamery
	* obiekty
	* źródła światła
	* materiały
	* tekstury
* Położenie i kształt obiektów
	* geometria
	* środowisko
	* kamera
* Wygląd obiektów
	* materiały
	* źródła światła
	* tekstury
	* modele cieniowania
* Potok
	* najwolniejszy element potoku spowalnia cały potok
	* część elementów może być przetwarzana równolegle
* Architektura - 4 części
	* aplikacja
	* przetwarzanie geometrii
	* rasteryzacja
	* przetwarzanie pikseli
### Aplikacja
* Pełna kontrola nad przebiegiem przetwarzania
* Wykorzystuje CPU
* Możliwość wykorzystania compute shader GPU
* Ustawienia lub algorytmy
	* np. redukcja siatki trójkątów
* Jeśli się da to przetwarzanie równoległe
* Algorytmy, których nie da się / ciężko zaimplementować w kolejnych krokach
	* np. detekcja kolizji
* Główne zadanie - przesłanie prymitywów do renderingu do etapu przetwarzania geometrii
	* linie
	* punkty
	* trójkąty
* Obsługa wejścia od użytkownika

### Przetwarzanie geometrii
* Etap odpowiedzialny za wszystkie operacje na trójkątach i wierzchołkach
* Etapy
	* cieniowanie wierzchołków
	* projekcja
	* obcinanie
	* mapowanie na ekran

#### Cieniowanie wierzchołków
* Zadania
	* obliczenie położenia wierzchołka
	* obliczenie dodatkowych danych dla wierzchołka (normalne, uv, itd.)
* Dawniej też w tym kroku liczono cieniowanie, teraz raczej obliczane per piksel
* Teraz raczej przetwarzane są tutaj dane związane z wierzchołkiem
	* np. obliczanie wag dla animacji szkieletowej
* Wyjściem jest obowiązkowo pozycja wierzchołka
* Seria przekształceń
	* przestrzeń modelu -> przestrzeń świata
	* przestrzeń świata -> przestrzeń widoku
* Każdy model istnieje w swoim układzie współrzędnych
* Model może mieć swoje przekształcenie - transformacja modelu
* Wiele przekształceń może być skojarzonych z tym samym modelem
	* ta sama geometria
	* wiele instancji w różnych miejscach, różnej wielkości
* Po aplikacji transformacji model znajdzie się w przestrzeni świata

#### Przestrzeń kamery / widoku
* Interesują nas tylko obiekty, które są widoczne w kamerze
* Zadanie - przekształcenie widoku
	* umieszczenie kamery w środku układu współrzędnych
	* typowo wzdłuż osi z, orientacja zależnie od biblioteki
* Kamera ma wartości near i far
	* odległości odcięcia

#### Projekcja
* Przekształcenie bryły widoku na kostkę
	* ekstrema $(-1,-1,-1)$ i $(1,1,1)$
* Może być określona macierzowo
* Ortogonalne lub perspektywiczne
* Ortogonalna
	* ułatwia modelowanie obiektów
	* nie ma zniekształceń
	* linie równoległe zostają równoległe
	* zachowuje relatywne odległości
	* definiowana przez 6 krawędzie prostopadłościanu widzenia
* Perspektywiczna
	* obiekty które są daleko są mniejsze
	* nie zachowuje odległości ani kątów
	* linie równoległe przestają być równoległe
	* dodatkowo wartość field of view
		* szerokość stożka
		* do skalowania wartości z płaszczyzny projekcji na koordynaty $[-1,1]$ w płaszczyźnie widoku


#### Obcinanie
* Odrzucenie prymitywów poza widokiem (sześcianem jednostkowym)
* Przycinanie do kostki jednostkowej
* Sprowadzenie do współrzędnych znormalizowanych
	* między $(-1,-1,-1)$ i $(1,1,1)$
* Przy przycinaniu mogą powstać nowe wierzchołki
	* jeśli nachodzi na krawędź

#### Mapowanie do przestrzeni ekranu
* Przejście z trójwymiarowych współrzędnych na dwuwymiarowe
	* mapowanie na współrzędne ekranu
	* mapowanie wartości głębi do przedziału $[z_1,z_2]$ (domyślnie $[0,1]$)
* Współrzędne okna z remapowaną wartością przekazane do rasteryzacji

### Rasteryzacja
* Znalezienie wszystkich pikseli które należą do prymitywów które są renderowane
* Tego nie można oprogramować
* Etapy
	* ustawianie trójkątów
	* przejście przez trójkąty
* Ustawienie trójkątów
	* obliczanie równań dla każdego prymitywu
	* może być wykorzystane do interpolacji cieniowania
	* wykonywane przez sprzęt
* Przechodzenie trójkątów
	* generacja fragmentów - dla każdego piksela którego środek jest pokryty przez trójkąt
	* każdy fragment posiada informacje o głębi i inne pochodzące z przetwarzania geometrii
	* właściwości fragmentu - generowane z wykorzystaniem interpolowanych danych z trójkąta

### Przetwarzanie pikseli
* Dokonywanie obliczeń dla piksela/próbki, która jest wewnątrz prymitywu
* Etapy
	* cieniowanie pikseli
	* łączenie

#### Cieniowanie pikseli
* Obliczenia cieniowania dla każdego piksela
	* wykorzystanie interpolowanych informacji z poprzednich etapów
* Całkowicie programowalne
* Różne operacje do wykonania
	* np. nakładanie tekstury
* Rezultat - ostateczny kolor dla każdego fragmentu

#### Łączenie
* Potok operacji rastrowych (Raster Operations Pipeline - ROP)
* Brak możliwości programowania, dużo możliwości konfiguracji
* Zadanie
	* połączenie koloru z etapu cieniowania z tym, który już jest w buforze
	* stwierdzenie widoczności

##### Potok operacji rastrowych
* Bufory
	* koloru
	* głębi
	* kanał alfa
	* szablonowy (stencil buffer)
	* ramki (frame buffer) - zawiera wszystkie pozostałe bufory

##### Bufor szablonowy
* Zapamiętuje lokalizacje renderowanych prymitywów
* Rendering do bufora może być wykonany z wykorzystaniem różnych funkcji
	* np. porównania - piksel wyświetlany jeśli relacja jest prawdziwa
* Można generować różne efekty - np. przezroczystość

### Rezultaty
* Po przejściu przez cały potok prymitywy, które przeszły wszystkie testy są wyświetlane na ekranie
* Podwójne buforowanie
	* renderujemy piksel po pikselu
	* nie chcemy żeby użytkownik to widział
	* renderowanie robi się w tle - zapis do back buffer
	* po zakończeniu renderowania podmieniamy back buffer z front buffer
