# Algorytmy ewolucyjne (2024-10-30)

## Rozszerzony algorytm błądzenia przypadkowego
```
x = x_0
log.append(x_0)
while !stop
	x = select(H)
	y = selectRandom(N(x))
	log.append(y)
```

* select ma rozkład prawdopodobieństwa inny niż jednostajny, ale wybór nadal jest losowy

### Prawdopodobieństwo selekcji w algorytmie proto-ewolucyjnym
* coś pośredniego między stochastycznym wzrostem, a błądzeniem przypadkowym
* stochastyczny wzrost - najlepszy wybierany z P=1
* błądzenie przypadkowe - niezależnie od jakości takie same prawdopodobieństwo
* proto-ewolucyjny
	* największe prawdopodobieństwo dla najlepszego
	* dla gorszych coraz niższe

## Algorytm ewolucyjny
* Reprodukcja
* Mutacja
* Selekcja
* historia populacji

## Idea mutacji
* Wybór losowego sąsiada
* Wraz z oddalaniem się od punktu przed mutacją, funkcja gęstości prawdopodobieństwa powinna nierosnąć
	* otoczenia punktów oddalonych bardziej będą osiągane z mniejszym prawdopodobieństwem niż otoczenia punktów bliskich
* Typy mutacji
	* gaussowska (typowa)
	* gaussowska o różnych odchyleniach standardowych w wymiarach
	* gaussowska o niediagonalnej macierzy kowariancji (skrzywiona chmura punktów)

## Typy selekcji
* Proporcjonalna (ruletkowa)
	* prawdopodobieństwo proporcjonalne do wartości funkcji celu
	* dodaje się czynnik stały żeby osiągać wartości z przedziału $[0,1]$ (jeśli funkcja celu osiąga ujemne wartości)
* Progowa
	* wszystkie powyżej progu mają jednakowe prawdopodobieństwo wyboru 
	* wszystkie poniżej progu mają prawdopodobieństwo $0$
	* nieproporcjonalna - ma znaczenie tylko po której stronie progu znajduje się osobnik, nie ważna jest proporcja wartości funkcji celu
* Turniejowa
	* losowanie ze zwracaniem z populacji bazowej $s$ punktów
	* z $s$ punktów selekcję przechodzi najlepszy
	* podobny do progowej bo istotna jest relacja między wartościami
	* podobny to proporcjonalnej bo wraz z wartością rośnie prawdopodobieństwo przejścia
	* daje się się wyrazić wzorem ($i$ - indeks w posortowanej liście punktów)
* Selekcja rangowa
	* arbitralne przypisanie prawdopodobieństwa selekcji na podstawie rangi (ułożenia w posortowanej liście)

## Realizacja losowanie z założonym rozkładem prawdopodobieństwa
* Dystrybuanta zmiennej losowej $F(x) = P(X \le x)$
	* funkcja niemalejąca
* Jeśli realizujemy zmienną losową o danym rozkładzie, to wartości dystrybuanty będą miały rozkład jednostajny $U(0,1)$
	* $x = F^{-1}(y)$
	* $y \sim U(0,1)$
* Można wygenerować dowolny rozkład licząc odwrotność dystrybuanty tego rozkładu na rozkładzie jednostajnym
	* nie zawsze da się wyznaczyć w ramach funkcji elementarnych (np. dla Gaussa)

## Dystrybuanta empiryczna
* Dla zbioru wartości $A$

$$
F_{emp} =  \frac{|\{ y \in A, y \le x \}|}{|A|}
$$

## Mutacyjny algorytm ewolucyjny
* W kolejnych iterajcjach będą pojawiać się zagęszczenia punktów w pobliżu najlepszych punktów i tam gdzie punkty są bliskie sobie


Kolos 13 albo 20
z algorytmów lokalnych, mutacyjnego ewolucyjnego, empirycznej oceny algorytmu
będzie spotkanie dla chętnych na teams z zadaniami

### Typy mutacji
* Mutacja gaussowska
	* typowa
	* dla wektorów liczb rzeczywistych, do każdej współrzędnej dodaje się niezależnie wylosowaną wartość opisaną rozkładem normalnym $\Delta_i \sim \sigma \cdot N(0,1)$
	* $\sigma$ - siła mutacji
	* równomierna chmura punktów - poziomice funkcji gęstości prawdopodobieństwa są okręgami (hipersferami)
	* kiedy nie ma wyróżnionego kierunku
	* czynniki wpływają na wartość funkcji celu niezależnie od siebie
	* (zmienne są jednakowej siły, niezależne)
* Gaussowska o różnych odchyleniach standardowych w wymiarach
	* czynniki wpływają w różnym stopniu na funkcję celu
	* dla każdego wymiaru oddzielna siła mutacji
	* diagonalna macierz kowariancji
* Gaussowska o niediagonalnej macierzy kowariancji
	* kierunki nie są niezależne od siebie
	* kolejna $\Delta_i$ powinna uwzględnić wpływ wartości skorelowanych wartości zrealizowanych wcześniej
	* problematyczne do implementacji
	* dekomponuje się macierz kowariancji na dwa trójkąty $LL^T$ - złożone obliczeniowo
	* generujemy wektor $\Delta$ niezależnych zmiennych losowych rozkładu normalnego standardowego
	* mnożenie $L \Delta$

Macierz kowariancji
kowariancja - miara współzależności zmiennych
stopień odchylenia od wartości oczekiwanej - wartości poza diagonalą
wariancja na diagonali
macierz symetryczna

dla wariantu mutacji z oddzielnymi siłami mutacji ($\sigma_i$), macierz kowariancji będzie macierzą diagonalną z $\sigma_i^2$ na diagonali

macierz kowariancji opisuje jak realizuje się poszukiwanie sąsiada w oryginalnej przestrzeni poszukiwań
równoważnie, mówi o tym jak przetransformować oryginalną przestrzeń przeszukiwań do innej, w której sąsiedzi są generowani rozkładem normalnym standardowym, a funkcja celu ma jednakową dynamikę we wszystkich wymiarach

## Dynamika mutacyjnego AE
* mała siła mutacji - ogon komety (krótki okres wspinaczki) i długa stagnacja bez znaczącej poprawy (gruba chmura punktów w pobliżu optimum lokalnego)
	* najlepiej wyznaczyć optimum lokalne przez średnią położenia punktów w chmurze
* duża siła mutacji
	* nieidealna eksploatacja - większy szum
	* silniejsza eksploracja
	* szybsze podejście pod górę
	* większe zróżnicowanie (wariancja) osiąganych średnich wartości funkcji celu w populacji w kolejnych iteracjach
	* przeskoki między otoczeniami optimów lokalnych (przekroczenie doliny)
	* populacja nie przechodzi w całości, są nietrwałe stany
	* wspinaczka
	* równowaga dynamiczna
	* przekraczanie doliny / siodła
* bardzo duża siła mutacji