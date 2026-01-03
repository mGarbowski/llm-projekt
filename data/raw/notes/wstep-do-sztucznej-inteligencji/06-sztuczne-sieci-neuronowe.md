# Sztuczne sieci neuronowe
Modelowane na podstawie biologicznego mózgu

Nie do wszystkiego warto stosować sieci, trzeba przygotować zbiór uczący i często trenować model na mocnym sprzęcie, jeśli prostsze rozwiązanie wystarcza to lepiej użyć prostszego!

## Model neuronu
* Neuron ma skończoną liczbę wejść (wektor n-elementowy)
* Każdy element wektora ma przypisaną wagę (weight)
* Neuron ma przypisane obciążenie (bias) - liczbę rzeczywistą
* Każdy z elementów wejściowych jest mnożony przez wagę i iloczyny są sumowane (iloczyn skalarny)
* Do sumy dodaje się obciążenie
* Wynik przepuszcza się przez funkcję aktywacji

Perceptrom dwuwarstwowy - dwie warstwy neuronów
n klas w problemie klasyfikacji -> n neuronów w ostatniej warstwie


## Funkcja aktywacji
* Neuron liniowy
	* $\psi(s) = s$
* Neuron sigmoidalny - funkcja ciągła, różniczkowalna, rosnąca
	* $\psi(s) = tanh(s)$
	* $\psi(s) = \frac{exp(s)}{1+exp(s)}$
* Neuron ReLU
	* $\psi(s) = max(0, s)$
	* $\psi(s) = min(max(0, s), M)$

## Perceptron dwuwastwowy
* Warstwa ukryta
	* neurony sigmoidalne
* Wastwa wyjściowa
	* neurony liniowe

### Własność uniwersalnej aproksymacji
Dla ograniczonego i domkniętego zbioru $\mathbb{X}$, dla każdego $\epsilon$ istnieją takie $n$ i $\theta$, że
$$max_{x \in \mathbb{X}} ||f(x) - \bar{f}(x, \theta)|| \le \epsilon$$

Perceptron dwuwarstwowy ma własność uniwersalnej aproksymacji - można tak dobrać parametry żeby na zadanym zbiorze aproksymować funkcję z zadaną precyzją (im większy zbiór tym bardziej rozbudowany model)

### Jako klasyfikator
* Tyle neuronów wyjściowych ile klas
* Idealne działanie to wyjście sieci w postaci 1 z $n$
* Wybiera się tą klasę, której neuron ma największą aktywację

## Uczenie sieci
* Definiuje się funkcję straty (typowo MSE)
* W procesie uczenia potrzebujemy wyliczyć wektor pochodnych funkcji straty po wagach i obciążeniach sieci - gradient
	* gradient mówi o tym jak zmienić odpowiednie parametry sieci
	* stosuje się do metody optymalizacji gradientowej
* Minimalizujemy stratę - różnicę między prawdziwą wartością i aproksymowaną

### Wsteczna propagacja gradientu
* Służy do wydajnego obliczania gradientu funkcji straty po wagach i obciążeniach
* Wylicza pochodne iterując od ostatniej warstwy do warstwy wejściowej
* Unika nadmiarowych operacji obliczania wyników pośrednich
* Zamiast stosowania reguły łańcuchowej

### Metoda gradientu prostego
* Parametr kroku (ciąg parametrów)
* Wartość aktualizowana o $-\nabla$ przeskalowany przez parametr kroku

### Metoda stochastycznego najszybszego spadku
* Jest bardziej wydajny od gradientu prostego, nie operuje na całym zbiorze uczącym
* Wykorzystuje estymaty gradientu zamiast dokładnej wartości
* Zbiór uczący dzieli się na mini-pakiety
* Wartość aktualizuje się na podstawie estymaty gradientu
* Są dodatkowe warunki na zbieżność

### Uczenie off-line
* Wykonuje się w epokach
* Jedna epoka to
	* przetasowanie zbioru uczącego
	* podział na mini-pakiety
	* zaktualizowanie wag na podstawie każdego mini-pakietu

### Inicjalizacja parametrów
* Najlepiej jak wartości wejściowe i wyjściowe są z przedziału $[-1, 1]$
	* pojęcie nasycenia neuronu
	* na tym przedziale funkcja sigmoid jest stroma, poza nim się wypłaszcza
	* stosuje się skalowanie tak żeby odchylenie standardowe $\simeq 1$
* Wagi neuronów wyjściowych inicjuje się zerami
* Wagi neuronów warst ukrytych inicjuje się wartościami $\mathcal{U}([-1/\sqrt{n}, 1/\sqrt{n}])$ 
	* $n$ to wymiar wejścia neuronu


## Zapobieganie przeuczeniu
* Wczesne zatrzymanie uczenia
	* przerywa się uczenie kiedy strata na zbiorze walidacyjnym przestaje spadać
* Regularyzacja
	* $\bar{q_t}(\theta) = q_t(\bar{f}(x_t, \theta) + \lambda ||\theta ||^2$
	* dodatkowa kara za duże wartości wag i obciążeń
* Odrzucanie (drop-out)
	* $p$ jest parametrem warstwy
	* podczas uczenia każde wejście warstwy może być ignorowane z prawdopodobieństwem $p$
	* podczas testowania używane są wszystkie wejścia ale wagi mnoży się przez $(1-p)$ żeby skompensować
	* ma oduczać sieć bazowania na przypadkowych zależnościach między neuronami
* Dostrojenie hiperparametrów
* Zebranie większego zbioru danych
* Stosowanie komitetów
	* zespół modeli i agregowanie wyniku
	* jak las losowy

## Perceptron wielowarstwowy
* Uogólnienie percpetronu dwuwarstwowego
* Wiele warstw ukrytych
	* neurony sigmoidalne
* Warstwa wyjściowa z neuronami liniowymi
* Ma takie same możliwości aproksymacji jak perceptron dwuwarstwowy
	* jeśli jest wystarczająco dużo neuronów
* Lepiej reprezentuje niektóre wysokopoziomowe zależności

## Inne modele
* Sieci głębokie i bardzo głębokie
	* głębokie to $\ge 3$ warstw
	* bardzo głebokie to $\ge 10$ warstw
* Sieci konwolucyjne (splotowe)
* Sieci rekurencyjne
	* cykliczne połączenie z opóźnieniami
* Sieci impulsowe