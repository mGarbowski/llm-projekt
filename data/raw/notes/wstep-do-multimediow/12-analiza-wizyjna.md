# Analiza wizyjna

## Wizyjna analiza semantyczna
* Ma na celu wydobycie informacji wyższego poziomu z surowych danych
	* próbek wizyjnych / dźwiękowych

## Przykłady w analizie obrazu
* Lokalizacja, śledzenie i rozpoznawanie obiektów
	* twarzy, samochodów, pisma
* Detekcja sytuacji nietypowych
* Analiza oka, pozy twarzy
* Śledzenie sztywnych obiektów w 6-wymiarach
	* 3 położenia, 3 obrotu
* Śledzenie, modelowanie twarzy
* Monitorowanie ruchu ulicznego
	* detekcja poruszających się obiektów
	* obiekty stojące traktowane jako tło
* Analiza dłoni do zastosowania w wirtualnej rzeczywistości
* Wykrywanie kierunku patrzenia
* Modelowanie sceny 3-wymiarowej i rozpoznawanie obiektów 3-wymiarowych
	* informacja o głębi z kamery głębi lub estymacji dysparycji stereowizyjnej
	* obroty sceny odsłaniają miejsca o których brak informacji wizyjnej
* Detekcja replik obrazów
* Rozpoznawanie liter (OCR)
* Odciski palców
* Rozpoznawanie tęczówki
* Analiza emocji

## Mapy głębi
* Uzyskiwane z kamer wykorzystujących promień laserowy
* Najpopularniejsza kamera to Kinect
* Problemy z przesłonięciami, oświetleniem, odbiciami i większymi odległościami

## Estymacja dysparycji stereowizyjnej
* Rejestruje się obraz z dwóch kamer
* Mozna wyznaczyć mapę głębi znając geometrię kamer porównując oba obrazy
	* można dostać 2 mapy (lewa względem prawej i na odwrót)
* Problemy z przesłonięciami, małymi obiektami, powierzchniami płaskimi, powtarzanymi wzorcami
* Przed estymacją konieczna jest rektyfikacja
	* algorytmy zakładają, że linia sobie odpowiadają w obu obrazach
	* obraz z kamery może być zniekształcony
	* obrazy wymagają przekształcenia

## Zbiory danych
* Kluczowy element przy
	* uczeniu algorytmów
	* weryfikacji skuteczności
	* porównywaniu różnych algorytmów
* Istnieje wiele gotowych baz obrazów, filmów, audio
* Wyniki analizy w dużym stopniu zależą od zbioru danych, na którym algorytm był trenowany i weryfikowany
* Znane zbiory
	* ImageNet
	* MNIST - pismo odręczne
	* Wider Face - zdjęcia twarzy
	* MsCeleb - zdjęcia celebrytów
	* COCO - detekcja i segmentacja

## Schemat analizy
* Przetwarzanie wstępne
* Normalizacja
* Ekstrakcja cech
	* wektory liczb rzeczywistych
	* porównywalne z cechami innych obrazów np. przez odległość euklidesową
* Klasyfikacja
	* klasyfikator bayesowski
	* svm
	* analiza dyskryminacyjna LDA
	* sieci neuronowe, uczenie głębokie
* Przetwarzanie końcowe

Ekstrakcja cech i klasyfikacja mogą być wykonywane przez jedną sieć neuronową

## Przetwarzanie wstępne
* Filtracja szumów
	* madianowa
	* gaussowska
* Operacje na histogramie
	* rozciąganie
	* wyrównanie histogramu
* Logarytmowanie obrazu
* Usuwanie określonych częstotliwości
* Uwypuklenie / wyostrzenie krawędzi
* Korekcja zniekształceń geometrycznych
* Normalizacja geometryczna
* Detekcja obiektów
* Przetwarzanie ma poprawić skuteczność systemu, a nie jakość obrazu dla człowieka

### Algorytm Chena normalizacji jasności
* Cienie są częstym problemem
* Algorytm
	* zlogarytmuj obraz
	* wykonaj DCT
	* usuń niskie częstotliwości
	* wykonaj odwrotne DCT
* Bez odwrotnego logarytmowania

### Korekcja zniekształceń geometrycznych
* W większości kamer i aparatów występuje zniekształcenia geometryczne
	* ramka nie jest płaska
	* piksele nie są rozmieszczone regularnie
	* soczewki wprowadzają zniekształcenia geometryczne
* Rodzaje zniekształceń
	* "beczka"
	* "poduszka"
	* tangensoidalne

### Modelowanie tła
* Dobrze jest wydzielić tło, żeby móc odróżnić je od interesującego obiektu
* Podejścia
	* w najprostszym przypadku - tło modelowane na podstawie klatki referencyjnej (odejmowana od obrazu w skali szarości)
	* w przypadku wielokanałowym (RGB) można stosować analizę zmian wektora (change vector analysis)
	* image ratioing - stosunek sygnałów zamiast różnicy
* Zapamiętanie obrazu pod warunkiem braku obiektów w scenie
	* częso nierealizowalne (np. ulica)
	* brak adaptacyjności - zmiany oświetlenia i warunków atmosferycznych
	* brak uwzględnienia ruchomych obiektów tła
* Modelowanie piksela wartością średnią
	* w każdej klatce aktualizowana wartość
	* $\mu_{t+1} = w\mu_t + O((1-w)i)$
	* waga z przedziału $[0,1]$
	* jeśli odchylenie od średniej przekracza próg, to obraz nie należy do tła
	* można modelować piksel rozkładem gaussowskim (oddzielnym dla każdego piksela)
* Modelowanie tła serią rozkładów gaussowskich
	* dobre dla wieloelementowego tła (poruszające się liście, zmienne warunki atmosferyczne)
	* każdemu pikselowi przypisane jest kilka rozkładów
	* część rozkładów odpowiada tłu, a część aktualnie widzianemu obiektowi
	* każdy rozkład ma przypisaną wagę
	* większa waga - rozkład występuje częściej
	* daje się rozszerzyć na 3 wymiary
	* efekt ducha po krótkim zatrzymaniu obiektu
* Algorytm
	* ustalenie liczby rozkładów na piksel
	* jeśli piksel pasuje do rozkładu to zwiększa się wagę i aktualizuje wariancję i średnią
	* jeśli nie pasuje to usuwa się rozkład o najmniejszej wadze i dodaje nowy
	* zakładamy że tło jest modelowane rozkładem o dużej wadze i małej wariancji
	* tło to średnia ze średnich rozkładów o największej wadze z każdego piksela

### Wyznaczanie obiektów zainteresowania
* Detekcja twarzy na podstawie punktów zainteresowania i ich orientacji
* Detekcja tablic rejestracyjnych
* Detekcja dłoni
* Detekcja zestawu klas obiektów (samochody, ludzie, ...)

## Normalizacja
* Najczęściej obejmuje
	* normalizację zakresu wartości do $[-1, 1]$
	* normalizację średniej
	* normalizację odchylenia standardowego / wariancji
* Normalizacja geometryczna
	* normalizacja obrotu (np. względem pozycji oczu)
	* wycięcie obszaru obiektu
	* normalizacja wielkości obrazu (skalowanie do określonego rozmiaru)

## Ekstrakcja cech

### Analiza składowych głównych
* Principal Components Analysis (PCA)
* Celem jest wyznaczenie kierunków głównych zbioru
	* kierunek o największej wariancji i prostopadłe o mniejszej wariancji
* Chodzi o taki kierunek, dla kturego wariancja rzutu punktów jest maksymalna
* Maksymalizacja funkcji wariancji względem wektora jednostkowego
* Rozwiązanie przez wyznaczenie wartości własnych i wektorów własnych macierzy kowariancji
* Zalety
	* prosta interpretacja
	* liniowe przekształcenia (operacje macierzowe)
	* pozwala na redukcję wymiaru danych bez utraty znaczących informacji
* Wady
	* nie uwzględnia klas przypisanych elementom
	* może powodować utratę ważnych informacji zawartych w danych

#### PCA wielowymiarowe dla rozpoznawania twarzy
* Każdy piksel jest traktowany jako oddzielny wymiar
* Każdy obraz to jeden punkt w tej przestrzeni
* Wektory własne PCA odpowiadające najwyższym wartościom własnym formują "twarze własne"
* Ekstrakcja cech polega na przemnożeniu wektora obrazu przez macierz twarzy własnych
	* wynikiem jest wektor wag
* Rekonstrukcja twarzy polega na stworzeniu kombinacji liniowej twarzy średniej i twarzy własnych

## Klasyfikacja
### Dla rozpoznawania twarzy
* Tworzy się bazę twarzy
* Każda twarz jest opisywana przez deskryptor (wektor liczb)
* Porównuje się klasyfikowany obraz z każdym i wybiera się ten o najmniejszej odległości euklidesowej
* Może powodować utratę ważnych informacji zawartych w danych

### k najbliższych sąsiadów
* Jako wybraną kategorię wyznaczamy tę do której należy najwięcej najbliższych k sąsiadów badanego elementu
* Przy badaniu bliskości zazwyczaj stosowana miara euklidesowa lub Mahalanobisa
* Skuteczny dla nietypowych rozkładów prawdopodobieństwa

### Liniowa analiza dyskryminacyjna
* Służy do znalezienia liniowej kombinacji cech, które najlepiej rozróżniają klasy obiektów
* LDA - linear discriminant analysis
* LDA i PCA redukują wymiarowość przestrzeni
* PCA znajduje kierunki główne
* LDA bierze pod uwagę przynależność punktów do klas
* Bierze pod uwagę wariancję międzyklasową $var_B(X)$ i wewnątrzklasową $var_W(X)$ (odległość przykładów klas od środka ciężkości klasy)
* Maksymalizowany jest stosunek wariancji międzyklasowej do wewnątrzklasowej $\frac{var_B(X)}{var_W(X)}$
* Szukamy kierunku dla którego rzutowanie (mnożenie przez wektor) da klasy jak najbardziej od siebie oddalone
* Szukamy kiernku dla którego rzutowanie da klasy jak najbardziej zwarte
* W ogólnym podejściu zastępuje się wariancje odpowienimi macierzami kowariancji $S_W$ i $S_B$
* Równanie w postaci $S_W^{-1}(X)S_B(X)W' = W' \Lambda$
	* rozwiązywane przez wyznaczenie wektorów własnych odpowiadających największym wartościom własnym iloczynu macierzy rozproszenia
	* można rozwiązać przez wyznaczenie wektorów osobliwych odpowiadających największym wartościom osobliwym

### Analiza dyskryminacyjna w podklasach
* SDA - subclass discriminant analysis
* Klasy nie są spójne - dobrze je podzielić na podklasy (np. oczy zamknięte i otwarte)
* Podział można realizować przez algorytm k-średnich
* Jeśli uda się uzyskać spójne klasy, klasyfikacja będzie skuteczniejsza
* Wynikowa liczba klas będzie większa niż pierwotna

### Sieci neuronowe
* Kiedy wagi neuronów odpowiadają wektorowi rzutowania z analizy PCA to neuron wykonuje analizę PCA
* Kiedy wagi neuronów są kierunkami maksymalizującymi separację i minimalizującymi separację klas to mamy LDA
* Kiedy wagi neuronów transformują do podprzestrzeni rozdzielającej klasy hiperpłaszczyzną to mamy SVM
* Nieliniowość pełni rolę klasyfikacyjną
* Więcej warstw daje większą zdolność klasyfikacyjną

### Sieci splotowe
* CNN - convolutional neural networks
* Rodzaj filtrów z maską lokalną
	* podobne działanie jak filtracja na obrazach
* Wagi filtrów dobierane na etapie uczenia
	* algorytm propagacji wstecznej
* Wykorzystywane w
	* klasyfikacji obrazów
	* poprawianiu jakości
	* steganografii
	* kompresji
	* modelowaniu głębii
	* automatycznym podpisywaniu
* Na przemian 2 warstwy (zazwyczaj)
	* splot z wytrenowanym filtrem
	* max-pooling - wybór maksimum w otoczeniu i podpróbkowanie
* Końcowe warstwy są gęste (fully connected) - klasyfikacja
* Sposoby rozszerzenia sieci na większą liczbę osób
	* żeby rozpoznawała nie tylko tych, na których została wytrenowana
	* bottleneck - odcięcie ostatniej warstwy sieci (etykiety)
	* założenie, że w ostatniej wartswie będziemy mieli sensowną reprezentację wszystkich twarzy
	* ostatnia warstwa służy jako wektor cech do rozpoznawania dowolnych twarzy
	* nie wiadomo czy ostatnia warstwa jest faktycznie dobrą reprezentacją innych twarzy

### Śledzenie ruchu
* Musi być poprzedzone detekcją obiektów
* Redukuje złożoność obliczeniową w relacji do detekcji
* Śledzenie punktu
	* metody deterministyczne
	* metody statystyczne (Kalman, filtry cząsteczkowe, roje cząstek)
* Śledzenie kształtu
	* oparte na wzorcach
	* oparte na wielowidokowych modelach wyglądu
* Śledzenie sylwetki
	* dopasowywanie kształtu
	* ewolucja konturów
* Mean shift, CAMSHIFT

### Filtr Kalmana
* Predykcja i pomiar są zaszumione
* Szum powinien być gaussowaski i zmienny w czasie
* Wzmocnienie Kalmana decyduje czy bardziej zdać się na predykcję czy pomiar
	* zależy od szumu (kowariancji) w obu przypadkach
* Model predykcji $\hat{x_k} = Ax_{k-1} + Bu_{k-1} + w_{k-1}$
	* aktualny stan $x_i$
	* macierz dynamiki $A$ (położenie, prędkość, przyspieszenie)
	* macierz kontroli modelu $B$
	* wektor kontroli $u_i$ - zwykle zerowy
	* szum predykcji $w_i$
* Aktualizacja pomiarem $x_k = \hat{x}_k + K_n(z_k - H \hat{x}_k)$
	* Wzmocnienie Kalmana $K_n$
* Model pomiaru $z_k = Hx_k + v$
	* pomiar $z_k$
	* model obserwacji $H$
	* aktualny stan $x_k$
	* szum pomiaru $v$
* Polega na ważeniu między predykcją a pomiarem

### Przepływ optyczny
* Siatka wektorów określających przmieszczanie się punktów w kolejnych klatkach
* Metody na określenie przemieszczenia
	* metody najmniejszej różnicy
	* metoda gradientowa

### Mean shift
* Pozwala na znalezienie lokalnych maksimów rozkładu gęstości punktów charakterystycznych (np. kącików oka)
* Otrzymuje się początkowe estymacje (pozycje) i funkcję jądra $K(x)$
* W kolejnych iteracjach oblicza się środek ciężkości

### CAMSHIFT
* Continuously Adaptive Mean Shift
* Rozszerzenie algorytmu mean shift
* Prawdopodobieństwo z histogramu koloru zamiast funkcji jądra
	* przestrzeń HSV
* Iteracyjne obliczanie środka ciężkości ważone kolorami
* Zmienne okno analizy
	* regulowane powierzchnią lub wariancją
* Służy do śledzenia przemieszczającego się obiektu na podstawie położenia punktów charakterystycznych
	* wyznacza się histogram kolorów
	* na podstawie histogramu wylicza się prawdopodobieńśtwo należenia piksela do obiektu
* Mean Shift z adaptacją rozmiaru okna
