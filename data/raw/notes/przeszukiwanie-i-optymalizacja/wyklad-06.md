# Algorytm ewolucyjny c.d. (2024-11-20)

Tylko selekcja (w klasycznym algorymtie) wykorzystuje informację o wartościach funkcji celu - tylko ona sprawia że algorytm działa tzn wybiera coraz lepsze punkty

Metafora 2 sprężyn (Galar)
selekcja - populacja ulega ściskaniu - po selekcji pewne punkty będą pominięte (z większym prawdopodobieństwem lepsze zostaną), zubaża populację
mutacja - przywraca różnorodność w populacji, wnosi nową jakość do populacji, ślepe próbkowanie

algorytm działa dzięki skojarzeniu selekcji i mutacji

mutacja co do zasady nie korzysta z wartości funkcji celu (jest ślepa)
są wariacje algorytmu, które to uwzględniają

czemu alagorytm ma szansę odnaleźć optimum globalne
makromutacje - jeśli każdy punkt dziedziny można wygenerować z jednakowym prawdopodobieństwem - dobrze bo można trafić na optimum globalne
prawdopodobieństwo że i-ty punkt populacji będzie w otoczeniu opt globalnego jest ograniczone z dołu (gęstość prawdopodobieństwa większa lub równa epsilon)
schemat bernouliego - większe prawdopodobieństwo trafienia jeśli więcej prób
największe prawdopodobieństwo dla rozkładu jednostajnego - największa wartość epsilona

takie samo rozumowanie dla błądzenia przypadkowego

selekcja może spowolnić dojście do opt globalnego (jeśli prowadzi algorytm do lokalnego optimum)

w praktyce - generowanie rozkładu normalnego - gęstość prawdopodobieństwa w końcu schodzi dokładnie do 0 ze względu na ograniczenia numeryczne
z powyższym argumentem - rozkład normalny ma prawdopodobieństwo 0 trafienia w otoczenie optimum globalnego

trzeba dać luzu algorytmowi żeby nie robił optymalizacji globalnej - niezerowe prawdopodobieństwo selekcji każdego punktu
selekcja turniejowa jest miękka (niezerowe prawdopodobieństwo do każdego)
proporcjonalna może być (jeśli odpowiednie wartości funkcji celu)
progowa jest twarda

jeśli odległość punktu populacji od opt globalnego jest skończona to nawet przy ograniczonym zasięgu mutacji, ze względu że punkt ma zawsze niezerowe prawdopodobieństwo selekcji to może w skończonej liczbie kroków dojść do optimum globalnego

## Krzyżowanie
Z punktu widzenia przestrzeni przeszukiwań to uśrednianie

metafora - wymieszanie materiału genetycznego z rodziców

Prawdopodobieństwo krzyżowania

najpierw krzyżowania, potem mutacja (można bez mutacji jeśli krzyżowanie ale...)
potomek z prawdopodobieństwem $p_c$ będzie wygenerowany przez najpierw krzyżowanie, potem mutację

część punktów w populacji potomnej jest wynikiem mutacji, a część wynikiem krzyżowania i mutacji
ze względu na losowanie ze zwracaniem ten sam punkt może być oboma rodzicami w krzyżowaniu

ine podejście - prawdopodobieństwo określa ile osobników z populacji bazowej podlega krzyżowaniu - różnica jeśli z krzyżowania wychodzi więcej niż 1 osobnik

można implementować algorytm macierzowo - wtedy inne podejście
za jednym zamachem generujemy reprodukowaną populację
trzeba mieć nadmiarową liczbę punktów żeby zrealizowac krzyżowanie lub jego brak
do przetwarzania SIMD dobre

### Jak rozumiemy uśrednianie
Dla R^n można standardowo uśrednić współrzędne ale co z wektorami binarnymi

wypadkowa to taki punkt, który od każdego z rodziców jest oddalony nie więcej niż rodzice między sobą - rysunek z przecinającymi się okręgami

### Krzyżowanie jako operator liniowy
$y = w \cdot x_1 + (1-w) \cdot x_2$
mnożenie element po elemencie (nie iloczyn skalarny)

jednopunktowe `w = [0,0,..0,1,1..,1]`
część od jednego rodzica, część od drugiego, punkt odcięcia
rozkładem równomiernym wybieramy punkt odcięcia zer i jedynek
potomkowie w narożnikach hiperkostki (ale nie 101 i 010)

równomierne `w = [0,1,1,0,0,1,0,1,...]`
jednakowe prawdopodobieństwo zera i jedynki
potomkowie we wszystkich narożnikach hiperkostki (łącznie z samymi rodzicami)


arytmetyczne `w = [0.1, 0.25, 0.9, ...]`
ważone uśrednianie z losowymi współczynnikami
tylko dla liczb rzeczywistych


brak obciążenia ze względu na obrót / translację
bp. środek odcinka dalej będzie na środku odcinka)
$o(t(x_1),t(x_2)) = t(o(x_1, x_2))$
które są, a które nie są obciążone?

w R^n można stosować i wymieniające i uśredniające krzyżowanie

wyłączenie mutacji nie pozwala osiągnąć optimum globalnego jeśli nie znajduje się ono w powłoce wypukłej początkowej populacji

krzyżowanie uśredniające powoduje większe ściśnięcie populacji bazowej ale zachowanie kształtu
(przykład dla wartości 1/2)
macierz kowariancji przeskalowana razy 2

krzyżowanie wymieniające
chmury przed i po krzyżowaniu różnią się kształtem ale nie skalą
z punnktów (a1, a2) i (b1,b2) mogą wyjść punkty (a1,a2) (b1,b2) (a1,b2) (b1,a2) - każdy równie prawdopodobny
takie same wariancje i mniejsze o połowę kowariancje
bardziej równomierne rozłożenie populacji
macierz kowariancji bardziej zbliżona do diagonalnej

przy krzyżowaniu uśredniającym większej liczby osobników będzie jeszcze bardziej ściśnięta chmura (skrzyżowanie wszystkich osobników daje środek geometryczny)
krzyżowanie jest estymatorem środka populacji
estymujemy środek żeby dookoła rozrzucić punkty po mutacji
nie zawsze krzyżowanie jest potrzebne

## Typy sukcesji
* Generacyjna
	* populacja potomna (po mutacji)
* Elitarne
	* k najlepszych z populacji bazowej i populacja potomna
	* po to żeby nie oddalić się od najlepszego punktu - pozostaniemy w jego otoczeniu
	* może bardziej zakotwiczyć populację w otoczeniu optimum lokalnego
* Steady-state
	* generuje sie jeden nowy punkt
	* z populacji bazowej wyrzucamy jeden (np najgorszy)
	* zastępujemy tym nowym