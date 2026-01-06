# Podstawy uczenia głębokiego

## LLM jako klasyfikator probabilistyczny

* Model jako parametryzowana funkcja mapująca sekwencję wejściową na rozkład prawdopodobieństwa kolejnego tokenu
* $f_\Theta: \mathbb{N}^k \rightarrow \mathbb{R}^{|D|}$
* Funkcja $softmax$
	* zazwyczaj sieci trenujemy tak, że w ostatniej warstwie zwracają wektor liczb rzeczywistych
	* w żadne sposób nieznormalizowane, zakres $(-\infty, \infty)$ - logity
	* funkcja softmax zamienia wektor liczb rzeczywistych na rozkład prawdopodobieństwa
	* $e^x$ jest dodatnie
	* elementy wektora sumują się do 1

$$softmax(z) = [ \frac{\exp{z_1}}{\sum_i \exp{z_i)}}, \ldots]$$

## Uczenie nadzorowane
* Ryzyko empiryczne
	* średnia strata modelu predykcyjnego na zbiorze treningowym
* Problem optymalizacyjny - znajdź wartości parametrów minimalizujący ryzyko empiryczne
* Wytrenowany model powinien się generalizować
	* powinien zwracać sensowne odpowiedzi dla wejść, których wcześniej nie widział

## Entropia krzyżowa
Zapamiętać na kolokwium

$$l_{CE} -\sum_i p_i \log \hat{p}_i$$


* $p_i$ - prawdziwe prawdopodobieństwo
	* tylko dla jednej wartości jest $1$
	* dla reszty jest $0$
* $-\log(1)=0$
* $-\log(0) \rightarrow +\infty$
* wzór upraszcza się do $-\log \hat{p}_y$
	* $\hat{p}_y$ - przewidziana wartość prawdopodobieństwa odpowiadająca poprawnej klasie
* Wzór dla logitów
	* ...
	* implementacja w torchu przyjmuje logity

## Trening modelu głębokiego
* Liczymy gradient funkcji stray po parametrach modelu $\Theta$
* Gradient to wektor
	* tyle elementów ile parametrów sieci
	* element wektora - jak bardzo wzrośnie strata modelu jak ten parametr się zwiększy

## Metoda stochastycznego spadku wzdłuż gradientu
* Wyznaczamy wartość funkcji straty i jej gradientu na pojedynczym wsadzie treningowym
	* wsad - podzbiór zbioru treningowego
* Gradient wyznaczany metodą propagacji wstecznej
* SGD jest metodą optymalizacji lokalnej
	* dąży do lokalnego minimum, a nie globalnego
	* w praktyce te optima lokalne są wystarczająco dobre

## Autoróżniczkowanie i grafy obliczeń
* plik PyTorch Intro - Autoróżniczkowanie i grafy obliczeń

## Dobór stopy uczenia
* Zbyt mała - brak zbieżności procesu optymalizacji
* Zbyt mała - zbyt wolna zbieżność
* Zazwyczaj powtarzamy eksperymenty z wieloma różnymi wartościami hiperparametrów (w tym stopy uczenia)

## Lepsze metody optymalizacji (gradientowe)
* Momentum
	* wielkość kroku uczenia jest zależna od od historii kroków
* Adam

## Optymalizacja w praktyce
* Pakiet `torch.optim`
* Optymalizator `Adam`, `AdamW`
* Domyślny wybór - `AdamW`
	* bardziej odporny na zbyt wysokie wartości stopy uczenia niż SGD

## Pętla uczenia
* Epoka - jedno przejście przez cały zbiór treningowy

```py
optimizer = torch.optim.SGD(model.parameters(), lr=eta)

for e in range(n_epochs):
	for b in range(0, train_input.size(0), batch_size):
		batch = train_input[b:b+batch_size]
		output = model(batch)  # output - logity
		
		target = train_target[b:b+batch_size]
		loss = criterion(output, target)
		
		optimizer.zero_grad()
		loss.backward()  # wyznaczanie gradientu - wsteczna propagacja przez graf obliczeń
		optimizer.step()

```

## Przeuczenie
* Dobra praktyka
	* logowanie wartości funkcji straty w każdej epoce
* Musimy mieć odłożony na bok zbiór walidacyjny, na którym model się nie trenuje
	* logujemy stratę na zbiorze walidacyjnym w kolejnych epokach

# Elementy składowe sieci neuronowych, trenowanie modelu

## Elementy składowe
* Warstwa - podstawowy element składowy
	* warstwa to jakaś operacja matematyczna
	* operują na tensorach zawierających przetwarzane dane
	* `torch.nn`
	* klasy warstw dziedziczą po `torch.nn.Module`
	* warstwa może mieć swoje parametry
	* parametry też są przechowywane w tensorach
	* w Torchu tensor może mieć ustawioną flagę `requires_grad=True` - będzie akumulować historię obliczeń
* Moduł może składać się z innych modułów
	* budowanie modelu jak z klocków
* Warstwy w sieci tworzę acykliczny graf skierowany (DAG)
	* w szczególnym, prostym przypadku - połączone sekwencyjnie

## Warstwa liniowa

$$y = xW^T + b$$

* $y$ - wektor wyjściowy
* $x$ - wektor wejściowy
* $W$ - macierz wag (parametr warstwy)
* $b$ wektor obciążenia (parametr warstwy)

* `torch.nn.Linear`
* Większość parametrów transformera bierze się z warstw liniowych
* Przekształcenie afiniczne
	* mnożenie przez macierz i dodanie wektora

## Warstwy nieliniowe
* Złożenie wielu warstw liniowych można zastąpić jedną warstwą liniową
	* właściwość przekształceń afinicznych
	* siła wyrazu samej warstwy liniowej jest ograniczona

### Rectified Linear Unit (ReLU)

$$
ReLU(x) = \begin{cases}
	0 & x <0 \\
	x & x \ge 0
\end{cases}
$$

* `torch.nn.ReLU`

### Gaussian Error Linear Unit (GELU)

$$GELU(x) = x \cdot \Phi(x)$$

* $\Phi(x)$ - dystrybuanta rozkładu normalnego
* Dobre własności
	* jest rózniczkowalna w każdym punkcie
	* gradient nigdzie nie jest zerowy (bardzo bliski zera dla małych wartości)

### Sigmoid Linear Unit (SiLU, Swish)

* $SiLU(x) = x \cdot \sigma(x)$
* Podobny kształt i własności do GELU

### Sigmoid

$$\sigma(x) = \frac{1}{1+\exp(-x)}$$
* Zakres wartości $(0,1)$

### Tangens hiperboliczny

$$\tanh(x)=...$$

* Obecnie rzadko stosowany w praktyce

## Warstwy normalizacji

### Normalizacja wsadu (BatchNorm)

$$y = \frac{x - \mathbb{E}[x]}{\sqrt{Var[x] + \epsilon}} \cdot \gamma + \beta$$

* Przekształca wejście
	* średnia zbliżona do $0$
	* Odchylenie zbliżone do $1$
	* dodatkowe uczone parametry odpowiedzialne za skalowanie
* Stabilizuje trening
* Przyspiesza zbieżność
* Zmniejsza szansę na przeuczenie
* Statystyki wyznaczane wzdłuż wymiaru związanego z rozmiarem wsadu
* W fazie treningu
	* zapamiętywana średnia krocząca
* W fazie inferencji
	* wykorzystanie wartości wyznaczonych w fazie treningu

### Normalizacja warstwy (LayerNorm)

* Wzdłuż wymiaru cech
	* dla wielu wymiarów (poza wymiarem wsadu) - po jednym wyznaczonym wymiarze
* Może poprawić generalizację modelu

## Inne warstwy

### Warstwa odrzutu (Dropout)

* Jest metodą regularyzacji, stosowany w celu ograniczenia przeuczenia
* Polepsza generalizację sieci neuronowej
* W fazie treningu
	* losowo zerowane wejścia z prawdopodobieństwem $p$
	* wyjście skalowane przez $\frac{1}{1-p}$ (żeby skompensować te wyzerowane)
* W fazie inferencji
	* przekształcenie identycznościowe

### Warstwa sekwencyjna
* Połączenie sekwencyjne wielu warstw w jeden moduł
* Przykład - perceptron wielowarstwowy

## Pętla treningowa
* Ważne - przełączenie trybu `.train()`/`.eval()`
	* są warstwy które działają inaczej