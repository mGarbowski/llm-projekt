# Perceptron

## Model neuronu
* Perceptron
* Warstwy
* Neuron
	* obliczenie ważonego pobudzenia (suma ważona wejść)
	* o 1 więcej wag niż wejść
	* $\sum_{i=1}^n x_i \theta_i + \theta_{n+1}$
	* płaszczyzna, przechodzi przez 0 jeśli $\theta_{n+1}=0$
	* jak mamy 2 wejścia to proporcja $\theta_1/\theta_2$ określa kąt nachylenia
* Funkcja aktywacji $\psi$
	* przyjmuje wartość skalarną i wytwarza wartość skalarną
	* nieliniowa
	* np. $\tanh$ - asymptoty poziome w - i + $\infty$, w $0$ wartość $0$
* Neuron przekształca wektor liczb rzeczywistych na skalar (liczbę rzeczywistą)

## Perceptron dwuwarstwowy
* Przypadek z 2 warstwami
* pierwsza ma funkcje aktywacji tanh, druga f(x)=x
* tanh ma asymptoty, po oddaleniu od 0 funkcja jest prawie stała
* wyjście neuronu jako funkcja wejść sieci
* perceptron dwuwarstwowy modeluje dowolne ciągłe odwzorowanie z $\mathbb{R}^m$ do $\mathbb{R}^n$ (m wejść, n wyjść)
	* twierdzenie o uniwersalnych własnościach aproksymacyjnych
	* nie wiadomo ile neuronów ukrytych potrzeba ale istnieje taka skończona liczba która da błąd nie większy niż zadany
	* twierdzenie jest niekonstruktywne, wiadomo że się da ale nie wiadomo jak dobrać liczbę neuronów warstwy ukrytej


## Uczenie perceptronu dwuwarstwowego
* Uczenie to minimalizacja funkcji, nie wiadomo jak mierzyć jakość sieci
* Nie znamy funkcyjnej postaci funkcji aproksymowanej, funkcja jest zdefiniowana na zbiorze o mocy continuum

$$\min_\theta \int_X \| f(x,\theta) - f(x)\|g(x) dx$$

* g(x) to funkcja gęstości prawdopodobieństwa próbek - zakładamy że źródło danych ma jakieś własności probabilistyczne
* minimalizujemy wartość oczekiwaną odległości między funkcjami
* błąd aproksymacji ma być możliwie jak najmniejszy, uwzględnia prawdopodobieństwo występowania wejść
* Mamy zbiory trenujący, walidacyjny i testowy, są zbiorami próbek S z rozkładem g(x)

$$\min_\theta \sum_{x \in S} \|f(x, \theta) - f(x)\|$$
* realistyczny wzór (S już jest wybrane z danym rozkładem prawdopodobieństwa)
* funkcja straty (kwadratowa) może mieć znacznie więcej niż jedno minimum lokalne
* mimo tego, w uczeniu stosuje się metody gradientowe (optymalizacja lokalna)
	* znane metody optymalizacji globalnej mają istotne ograniczenia - słaba zbieżność, są powolne
	* dlatego mimo znanych wad stosuje się metodę stochastycznego gradientu

## Wsteczna propagacja błędu
* Metoda obliczenia gradientu funkcji stray przy założeniu jakiegoś zbioru uczącego
* q - wartość funkcji straty dla konkretnej pary trenującej
* h - ważone pobudzenie (punkt pracy)
* $\frac{dq}{d\theta_{ij}^k}$ - pochodna cząstkowa straty po wadze połączenia ...
* $q = (y_i - f(x))^2$
* $dq/dy_i = 2(y_i - f(x))$
* sumowanie we wzorze na neuron ukryty - jakby było więcej neuronów (ścieżek od końca)
* część $\delta$ się pokrywa z tym co było poprzednio wyliczone

$$
\delta_l^{k-1} = \sum_i \delta_i^k \theta_{il} \psi'(h_l^{k-1})
$$

* Jak obliczamy wyjście sieci na podstawie wejścia to liczymy najpierw pierwszą warstwę neuronów, potem kolejną, ...
* Obliczanie gradientu - najpierw obliczamy $\delta$ ostatniej warstwy, potem przedostatniej, ...
* Wygodnie liczy się pochodną $\tanh'(z) = 1-\tanh^2(x)$
* Obliczenie gradientu funkcji straty jest tego samego rzędu co obliczenie wyjścia sieci

## Metoda stochastycznego najszybszego spadku
$$x_{t+1} \leftarrow x_t - \beta_tg_t$$
$$\mathbb{E}[g_t] = \nabla J(x_t)$$

Możemy brać tylko niektóre przykłady ze zbioru trenującego do obliczania (oszacowania) wartości gradientu (koszt liczenia jest liniowy z liczbą próbek)

## Inicjacja parametrów sieci
* Wagi neuronów ukrytych losuje się z rozkładu jednostajnego
	* heurystyczny wzór
	* $U(-1/\sqrt{dim(we)}, 1/\sqrt{dim(wy)})$
	* wg. symulacji takie wartości są dobre
	* unika się wylosowania parametrów które dają nasycenie neuronu
	* dla innych funkcji aktywacji są inne dobre rozkłady do inicjacji
* Skalowanie wejść i wyjść tak żeby std każdego było zbliżone do 1
* Wagi neuronów wyjściowych 0
	* sensowne tylko dla liniowego wyjścia

## Przeuczenie
* Znacznie większy błąd na zbiorze testowym niż treningowym
* Wczesne zatrzymanie uczenia
	* uczymy dopóki strata na zbiorze walidacyjnym (a nie treningowym) spada
* Regularyzacja
	* redukujemy wartości bezwzględne wag
	* działa jak funkcja kary za duże wartości wag
	* pochodne w punkcie pracy nie powinny być zerowe - utrzymujemy się w tym regionie funkcji aktywacji gdzie nie ma nasycenia
* Odrzucanie
	* redukcja architektury przy uczeniu (mniej bogaty kształt modelu)
	* zmniejszamy liczbę parametrów do uczenia - z jednej strony trudniej, a z drugiej strony większa generalizacja

## Perceptron dwuwarstwowy jako klasyfikator
* Dla 2 klas może być próg wartości w 1 neuronie wyjściowym
* Dla n klas może być n wyjściowych
* Można bardziej egzotyczne - ponumerować klasy i kod Gray'a na wyjściu
