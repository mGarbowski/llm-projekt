# Algorytmy uczenia sieci neuronowych
* Uczenie on-line
	* przetwarzanie próbek po kolei
* Uczenie off-line
	* dostępny cały zbiór
	* można policzyć globalne operacje
	* nierealne dla dużych zbiorów danych
* Strata na minipakiecie - nieobciążony estymator kryterium jakości
	* kryterium jakości jest zdefiniowane na całym zbiorze treningowym
* Gradient na minipakiecie - nieobciążony estymator gradientu

## Pętla uczenia
* Epoka - przejście po całych danych treningowych
* Uczenie - zadana liczba epok
* Wynik - zoptymalizowane wagi sieci neuronowej
* W każdej epoce dane ustawiane losowo do tworzenia minipakietów
	* dla każdego minipakietu jest wyznaczany gradient
	* gradient jest użyty do poprawy parametrów

## Stochastyczny spadek wzdłuż gradientu (SGD)

$$\theta = \theta - \beta \hat{g}$$

* Stochastyczny - gradient jest tylko estymowany na jednym minipakiecie
* Hiperparametr - $\beta$ - learning rate / step size
	* parametr kroku
* Warunki zbieżności
	* do optimum lokalnego
* Wrażliwość na $\beta$
	* za mała wartość - wolne uczenie
	* za duża wartość - niestabilność uczenia
* Konieczny jest dobór dobrej wartości $\beta$
* Przez wykorzystanie tylko jednego pakietu występują fluktuacje

## Algorytmy z inercją

$$m = \lambda m - \beta \hat{g}$$
$$ \theta = \theta + m$$

* Czynnik inercyjny akumuluje zmiany
	* akumulujemy gradienty z wielu minipakietów
	* z większą wagą bierzemy nowsze
* Wykrywa trend i wzmacnia ten trend
* Redukuje fluktuacje
* Hiperparametry
	* współczynnik uczenia $\beta$
	* stopień bezwładności $\lambda$
* Wersja CM (Classic Momentum)
	* metoda z inercją 
	* standardowe obliczanie gradientu
	* $\hat{g} = \nabla_\theta \hat{q}(\theta, \xi)$
* Wersja NAG (Nesterov Accelerated Gradient)
	* metoda Nesterova
	* gradient jest liczony w przesuniętym punkcie (względem przesuniętych parametrów)
	* $\hat{g} = \nabla_{\theta + \lambda m} \hat{q}(\theta + \lambda m, \xi)$

## Algorytmy z normalizacją gradientów

### Adagrad

$$ G = G + \hat{g}^2 $$
$$ \theta = \theta - \frac{\beta}{\sqrt{G + \epsilon}} \hat{g} $$

* $\epsilon$ - stała, zapobiega dzieleniu przez 0
* Modyfikacja SGD
* Skaluje parametr kroku
* Wektor parametrów kroku - oddzielny krok dla każdego parametru sieci
	* większy krok dla wag z małymi zmianami
	* mniejszy krok dla wag z dużymi zmianami
* $G$ jest niemalejące
* Akumulacja przez sumowanie - gradient z każdego minipakietu wpływa tak samo (nowy i stary)
* Stabilny proces uczenia
	* zwalnia w miarę uczenia

### RMSprop

$$ E\hat{g} = \gamma E \hat{g} + (1-\gamma) \hat{g}^2 $$
$$ \theta = \theta - \frac{\beta}{\sqrt{E\hat{g} + \epsilon}} \hat{g} $$

* Modyfikacja SGD
* Wygładzanie wykładnicze gradientów
* Hiperparametr - współczynnik wygładzania $\gamma$
* Wygaszanie wpływu starszych gradientów
* Inne podejście do akumulacji kwadratów gradientów - wygładzanie wykładnicze
	* mocniejszy wpływ nowszych gradientów
* Ograniczenie agresywnego zmniejszania jak w Adagrad

### Adadelta

$$ E\hat{g} = \gamma E\hat{g} + (1-\gamma) \hat{g}^2$$
$$ \Delta \theta = -\frac{\sqrt{E\theta + \epsilon}}{\sqrt{E\hat{g} + \epsilon}} \hat{g} $$
$$ E\theta = \gamma E \theta + (1-\gamma) \Delta \theta^2 $$
$$ \theta = \theta + \Delta\theta $$

* Modyfikacja SGD
* Nie ma parametru kroku - szacowany przez samą metodę
	* $\frac{\sqrt{E\theta + \epsilon}}{\sqrt{E\hat{g} + \epsilon}}$
	* różny krok dla każdej wagi
* Jak RMSprop ale zmieniony wzór daje zgodne jednostki z parametrami sieci
* Można dodatkowo dołożyć parametr kroku skalujący $\Delta$
	* w praktyce niepotrzebny
* Autorzy sugerują wartości hiperparametrów
* Nie ma agresywnego zmniejszania kroku jak w Adagrad

### Adam

$$ m = \gamma_1m + (1-\gamma_1)\hat{g} $$
$$ v = \gamma_2v + (1-\gamma_2)\hat{g} $$
$$ \hat{m} = \frac{m}{1-\gamma_1^t} $$
$$ \hat{v} = \frac{v}{1-\gamma_2^t} $$
$$ \theta = \theta - \frac{\beta}{\sqrt{\hat{v} + \epsilon}} \hat{m} $$
* Oznaczenia
	* $\beta$ - learning rate
	* $\gamma_1, \gamma_2$ - współczynniki wygładzania
	* $\epsilon$ - mała stała (zapobiega dzieleniu przez $0$)
	* $t$ - krok czasowy (indeks minipakietu)
	* $m$ - estymator pierwszego momentu gradientów (średniej)
	* $v$ - estymator drugiego momentu gradientów (niewyśrodkowana wariancja)
	* $\hat{m}, \hat{v}$ - korekty estymatorów
* Modyfikacja algorytmu CM
* Najpopularniejszy obecnie
* Wygładzanie wykładnicze estymatora gradientu i kwadratów gradientu
* Wygładzanie działa jak człon inercyjny
* Skalowanie parametru kroku
* $m$ i $v$ się skaluje, żeby przyspieszyć początkowe kroki uczenia
	* są inicjowane zerami
	* z czasem mianownik zbliża się do 1 - wykładnik $t$
	* wartość skorygowana zbliża się do oryginalnej
* Wariacje
	* AdaMax - akumulacja wartości maksymalnych zamiast kwadratów
	* Nadam - oparty na NAG
	* AMSGRAD - autorzy wykazali, że Adam nie zawsze jest zbieżny dla pewnej klasy problemów
	* w praktyce podstawowy Adam często jest lepszy

## Inne podejścia
* Algorytmy drugiego rzędu
	* wykorzystują drugie pochodne (hesjan) funkcji straty względem parametrów
	* szybsza zbieżność
	* kosztowne obliczeniowo i pamięciowo (kwadratowo względem liczby parametrów, zamiast liniowo jak w gradiencie)
	* praktyczne tylko dla bardzo małych sieci
* Algorytmy dostosowujące hiperparametry uczenia
	* modyfikacje konkretnych algorytmów
	* mechanizmy ogólne
	* często bardziej wymagające pamięciowo i obliczeniowo
	* koszty mogą rekompensować czas potrzebny na eksperymenty ze strojeniem hiperparametrów
