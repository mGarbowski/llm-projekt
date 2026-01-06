# Dobre praktyki

## Przeuczenie i co z nim zrobić
* Przeuczenie to znacznie większy błąd na zbiorze testowym niż treningowym
* Niedouczenie
	* za prosty model
	* za mało danych
	* za krótkie uczenie

### Wczesne zatrzymanie
* Do wykrycia przeuczenia potrzebujemy zbioru treningowego i walidacyjnego
* Jeśli nie mamy wystarczająco dużo danych, możemy wykorzystać walidację krzyżową
* Leave-one-out - jak mamy bardzo mało próbek
* Zatrzymujemy uczenie w epoce, w której błąd na zbiorze walidacyjnym był najmniejszy
* W praktyce dobrze jest na bieżąco monitorować zmianę funkcji straty
	* nie zawsze warto uczyć do końca przez zadaną liczbę epok
	* zanikający/eksplodujący gradient
* Bootstrap
	* podział na zbiór testowy i treningowy przez losowanie ze zwracaniem
	* jedno losowanie to próba bootstrapowa
	* powtarza się n razy i uśrednia
	* może dawać dokładniejsze oszacowanie rzeczywistego błędu niż walidacja krzyżowa

### Regularyzacja
* Zmiana funkcja straty
	* wprowadzenie kary zależnej od parametrów (wag) modelu
* Regularyzacja L2
	* $+\lambda \|\theta\|_2$
	* tendencja modelu do równomiernego rozkładania wag
	* niewielkie wartości na wszystkich neuronach
	* gładsza funkcja wyjściowa
	* zrównoważone wykorzystanie wszystkich wejść
	* efekt stabilizujący
	* wagi są tak małe jak to możliwe, ale nie zerowe
* Regularyzacja L1
	* $+\lambda \sum |\theta_i|$
	* wagi stają się rzadkie
	* tylko niektóre neurony mają niezerowe wartości
	* część neuronów otrzymuje zerowe wagi
	* działa jak selekcja cech - niektóre zostają odrzucone, zostają najważniejsze
	* zmniejsza wrażliwość sieci na zakłócenia

### Drop-out
* Prawdopodobieństwo $p$ ustalone dla warstwy
* Waga zostaje taka jaka była
* Wyjście jest zerowane (losowo z prawdopodobieństwem $p$)
* Podobny efekt do regularyzacji
* Przy inferencji wchodzą wszystkie neurony
	* żeby skompensować brak neuronów podczas treningu - mnożenie wag przez $(1-p)$

### Augmentacja danych
* Wprowadzenie do zbioru treningowego zmodyfikowanych kopii istniejących danych
* Zwłaszcza przy obrazach
	* rotacja, odbicie, szum
	* powoduje zmianę rozkładu danych
	* jeśli jakaś transformacja nie była obecna w zbiorze treningowym, a pojawi się przy inferencji to może być słaby wynik
* W modelach językowych
	* zmiana szyku
	* zamiana słów na synonimy
	* literówki
	* podwójne tłumaczenia
* Problem augmentacji n+1

## Destylacja
* Szczególny rodzaj uproszczenia modelu
* Wycięcie tylko niektórych warstw z sieci
* Poza tym stosowana do przyspieszenia

## Funkcje aktywacji
* Tożsamość
* Tangens hiperboliczny
	* sigmoid bipolarny
* Funkcja logistyczna
	* sigmoid unipolarny
* ReLU
* LeakyReLU
* Swish
* Nie ma dobrych, ogólnych metod na dobranie funkcji aktywacji do problemu
	* funkcja aktywacji jest jednym z hiperparametrów

### ReLU
* Zalecana do większości zastosowań w sieciach jednokierunkowych
* Jest złożeniem dwóch liniowych funkcji
	* łatwe do optymalizacji
* Złożenie ReLU z transformacją liniową daje transformację nieliniową
* Nie ma żadnej aktualizacji gradientu kiedy wartość wynosi 0
	* to nie zawsze dobrze, bo dla 0 nie aktualizuje się gradient
	* warianty ReLU to zmieniają, dla niektórych zbiorów danych dają lepsze wyniki

### Funkcja sigmoidalna
* Nasycają się w większości swojej domeny
	* w wąskim zakresie przyjmuje wartości mocno odbiegające od asymptot
	* stwarza problemy dla sieci głębokich
	* wrażliwa tylko na dane wejściowe blisko $0$
* Nasycenie utrudnia uczenie oparte na gradiencie
* Raczej odradzane w sieciach jednokierunkowych
* Tangens hiperboliczny raczej jest lepszy niż funkcja logistyczna

### Problem zanikających / eksplodujących gradientów
* Bardzo szybko dostajemy bardzo duże/małe wartości gradientu
	* głębsze warstwy się nie aktualizują
* Przede wszystkim w sieciach rekurencyjnych
* Rozwiązania
	* użycie nienasycających się funkcji aktywacji (ReLU i pochodne)
	* odpowiednia inicjalizacja wag (He, Glorota)
	* normalizacja wsadowa
	* obcinanie gradientu
	* połączenia nie tylko między sąsiednimi warstwami (ResNet)

## Perceptron dwuwarstwowy jako klasyfikator
* Tyle neuronów wyjściowych ile klas
* Oczekujemy wyjścia w postaci kodowania 1 z n
* Z wektora wyjść sieci patrzymy na to, który element jest największy

### Warstwa soft-max

$$ wy_{[i]} = \frac{\exp(we_{[i]})}{\sum_j \exp(we_{[j]})} $$

* Ma na celu normalizację wyjść do takiego zakresu, żeby wszystkie wyjścia sumowały się do 1
* Można traktować jako prawdopodobieństwo przynależności do klasy
	* wyjście w postaci rozkładu prawdopodobieństwa
* Użyteczne np. do detektorów obiektów
	* można odrzucać detekcję dla prawdopodobieństwa poniżej pewnego progu
	* można określić próg na poziomie jednakowej pewności do wszystkich klas (np. 3 po 0.33)

## Funkcja straty
* Błąd średniokwadratowy
	* do regresji
* Entropia krzyżowa
	* do klasyfikacji
	* wzorcowe prawdopodobieństwo i-tej klasy $y_i^d$
	* zwracane prawdopodobieństwo i-tej klasy $y_i$
	* $l(y) = -\sum_i y_i^d \log_2(y_i)$
	* jest sumą entropii i dywergencji Kullbacka-Leiblera


## Inicjalizacja wag
* Rozkład równomierny $U(-b,b)$
* Metoda klasyczna $b = \frac{1}{\sqrt{dim(we)}}$
* Xavier $b=\frac{\sqrt{6}}{\sqrt{dim(we) + dim(wy)}}$
* dim - wymiar danych wejściowych

## Normalizacja pakietowa
* Batch normalization
* Atrybuty mogą mieć różne zakresy wartości
* Wyjścia z kolejnych warstw też są normalizowane
* Te same zmienne w ramach minipakietu
	* obliczamy średnią
	* obliczamy std
	* zmienne przechodzą dalej znormalizowane (odjęcie średniej, dzielenie przez std)
	* można to robić w trakcie treningu
* Problem - co zrobić na nowych danych
	* pojedyncza próbka, a nie cały wektor, nie ma z czego liczyć rozkładu
	* można wziąć średnią i odchylenie z danych treningowych
* Scale and shift
	* po normalizacji przekształcenie funkcją liniową
	* parametry $\gamma$ i $\beta$ inicjowane losowo i potem aktualizowane w procesie uczenia
	* pozwala wprowadzić obciążenie
* Pozwala przyspieszyć uczenie
	* w trakcie uczenia, wagi się dostosowują i zmienia się rozkład wyjścia z warstwy (internal covariate shift)
	* kolejne warstwy muszą się dostosowywać do tego nowego rozkładu
	* jak wyjścia są znormalizowane to zjawisko ma mniejszy wpływ

## Standard ASPICE 4.0
* Dla branży automotive
* Automotive Software Process Improvement and Capability dEtermination
* Określa procesy i dobre praktyki dla uczenia maszynowego
	* jak definiować wymagania
	* jak tworzyć architekturę
	* jak trenować
	* jak testować model po wytrenowaniu
* Warto poczytać, standard jest generyczny

## Wyznaczanie niepewności
* Epistemiczna
	* spowodowana niewystarczającą liczbą danych
	* szacowanie - metoda monte carlo
	* wiele razy robienie inferencji z losowym dropoutem - sprawdzamy czy się zmienia, czy jest spójnie
* Aletoryczna
	* spowodowana naturalną losowością
	* zaszumienie pomiarów
	* nie może być zmniejszona przez dodanie nowych danych

## Wzorce aktywacji neuronów
* Analizując wzorce aktywacji neuronów można wykrywać dane spoza dystrybucji
	* podczas inferencji dana z innego rozkładu niż przy uczeniu
	* widoczne różnica przy porównaniu dystansu Hamminga
