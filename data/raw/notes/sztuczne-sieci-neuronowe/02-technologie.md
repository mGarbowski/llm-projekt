# Technologie

## Neuron
* Pojedynczy neuron realizuje mnożenie elementów wektora wejść przez wagi i dodanie obciążenia
	* mnożenie wektora wejść (rozszerzonego o 1) przez wektor wag (iloczyn skalarny)
* Warstwa neuronów to mnożenie wektora wejść przez macierz parametrów neuronów warstwy
* Warstwa neuronów z mini-pakietem
	* mnożenie macierzy - wagi warstwy i przykłady z minipakietu
	* często rozmiar mini-pakietu to potęga 2
	* w mnożeniu macierzy nie jest ważna kolejność - dobrze nadaje się do zrównoleglania
* Mówiliśmy o przypadku gdzie wejściem jest wektor
	* obraz w skali szarości jest macierzą
	* obraz barwny ma 3 wymiary
	* wejściem neuronu może być macierz lub tensor wyższego rzędu
	* wtedy wagi też są odpowiednio wyższego rzędu
* Biblioteki zakładają że jeden wymiar wejścia przypada na pozycję w mini-pakiecie

### Liczba wag w perceptronie (przykład)
* mamy 6 warstw ukrytych po 5 neuronów
* 1 neuron wyjściowy
* 10 elementów wejścia
* w pierwszej warstwie ukrytej jest 10 wejść do każdego neuronu
* $10 \cdot 5 + 5$ wag (po 10 wag i 1 obciążenie na neuron)
* między 1 a 2 ukrytą warstwą jest 25 wag i 5 obciążeń
* do ostatniej warstwy jest 5 wag i 1 obciążenie
* w sumie sieć ma $(10 \cdot 5 + 5) + 5 \cdot (5 \cdot 5 + 5) + (5 + 1)$ parametrów

## Tensory
* Macierz n-wymiarowa
* Rząd tensora
	* 1 - wektor
	* 2 - macierz
* Większe rzędy
	* np. obrazy hiperspektralne - więcej różnych długości światła niż standardowe 3

## Obliczenia tensorowe
* Większość operacji jest wykonywana jako operacje tensorowe
* Wagi / aktywacje są rzadziej odczytywane z pamięci

## Obliczenia na GPU
* Zwiększając liczbę rdzeni można efektywnie wykonywać operacje dla sieci neuronowych
* GPU działa asynchronicznie z CPU
	* transfer danych z CPU do GPU
	* zadanie obliczeniowe do kolejki na GPU
	* CPU czeka aż GPU sygnalizuje że skończyło
	* transfer danych z GPU na CPU
* Te same obliczenia na floatach mogą nie być powtarzalne przez przełączanie wątków
* Architektura GPU - SIMD
	* wiele wątków wykonuje ten sam kod
	* wątek ma w zmiennej swój identyfikator

## Technologia CUDA
* Compute Unified Device Architecture
	* produkt Nvidii
* AMD dostosował się do OpenCL
	* Open Computing Language
	* język programowania kart graficznych ogólnego przeznaczenia
* GPU ma kilka multi-procesorów strumieniowych
	* SM (Streaming Multiprocessor)
* Każdy SM ma kilka rdzeni
	* np. 128 wątki wykonywane współbieżnie / synchronicznie na 1 SM
* Pamięć GPU - DDR
	* pamięć dzielona SM w rejestrach
* Mini-pakiet musi mieścić się w pamięci GPU
	* w plikach konfiguracyjnych modeli można sterować rozmiarem mini-pakietów
* Procedura obliczeniowa
	* ten sam kod
	* zbiór bloków wątków
	* jeden blok realizowany na tym samym SM
* Wątek zna
	* indeks swojego bloku
	* swój indeks w bloku
	* liczbę bloków i rozmiar bloku
* Wszystkie wątki mają wspólny dostęp do kolejnych adresów pamięci GPU
* Zadania są tak dekomponowane żeby czytały sąsiednie komórki pamięci GPU
* Szeroka szyna pamięci GPU wpływa na wydajne przetwarzanie

## Biblioteki do obliczeń na sieciach neuronowych
* TensorFlow
* PyTorch
	* obecnie najbardziej popularny w zastosowaniach prototypowych
* JAX
* MXNet
* Theano
* Keras
* Paddle Paddle
	* popularny w Chinach

### Wspólne cechy
* Wsparcie dla obliczeń na GPU
* Radzą sobie z asynchronicznością CPU-GPU
* Wsparcie dla przetwarzania mini-pakietów
* Automatyczne różniczkowanie
* Separacja
	* budowy sieci
	* obliczeń w sieci
	* obliczania gradientu
	* uczenia sieci

### TensorFlow
* Kod programu ustawia graf obliczeniowy
	* ustawia się sesję
	* w ramach sesji podaje się na wejściu dane
	* graf jest wykonywany
	* trudne do debugowania - całe obliczenia jako black-box
* W wersji 2
	* bliżej programowania obiektowego
* Python, C++ i JS
	* JS dobry do odpalania demonstracji wytrenowanego modelu w przeglądarce

### PyTorch
* Kod faktycznie uruchamia obliczenie wyjść sieci w przód operacjami na tensorach i tworzy graf obliczeniowy
* Możliwość debugowania
	* podglądanie grafu obliczeniowego w trakcie wykonania
* Metoda `backward` oblicza gradient
* Metoda `step` wykonuje krok optymalizacji wag sieci

## ONNX
* Open Neural Network Exchange
* Język
* Umożliwia eksport wag i struktury modelu w ustandaryzowany sposób
* Niezależny od frameworka i języka programowania
* Częsty przypadek
	* kod w pytorchu do trenowania
	* eksport do onnx
	* uruchomienie produkcyjne w innym środowisku
* Jest runtime działający w przeglądarce


## Praktyczne kwestie
* Korzystając z pretrenowanych modeli
	* np. sieć głęboka do wykrywania cech w obrazach i klasyfikacji
* Można zamrozić część wag
	* np. warstwy odpowiedzialne za ekstrakcję cech z obrazów
* A samemu dotrenować tylko ostatnie warstwy np. tylko warstwy głęboko połączone do nowego zadania

## Numba
* Do obliczeń macierzowych, nie tylko związane z sieciami neuronowymi
* Kod optymalizowany przez użycie `@jit`
* Obliczenia na CPU i GPU
* Jeśli istnieją funkcje wbudowane w pythonie to raczej one będą szybsze
