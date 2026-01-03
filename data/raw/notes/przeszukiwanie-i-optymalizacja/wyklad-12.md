# 2025-01-22

## Adaptacja mutacji
* Sterowanie zaprogramowane
* Reguła 1/5 liczby sukcesów
* Samoczynna adaptacja
	* Schwefel Rechenberg
* Adaptacja parametrów

### Samoczynna adaptacja
* Przyjmijmy że prowadzimy optymalizacje w przestrzeni $\mathbb{R}^{100}$
	* żeby scharakteryzować 100 rozkładów normlanych potrzeba wektora 100 wartości oczekiwanych i symetryczna macierz kowariancji 100x100
	* można zredukować liczbę wymiarów przyjmując że zawsze używamy rozkładu standardowego i mnożemy go przez siłę mutacji - tylko 1 parametr zamiast 5000
	* można przyjac diagonalna macierz kowariancji - 100 parametrów - lepiej dopasuje się do poziomic funkcji celu
* Rozważamy mutację z diagonalną macierzą kowariancji - jak 100 niezależnych rozkładów standardowych
* Genom stanowią 2 wektory
	* 100-wymiarowy wektor x - zmienne podlegające optymalizacji
	* 100-wymiarowy wektor $\sigma$ - parametrów
* Selekcja jest oparta na wartościach $q(x)$
	* parametry nie wpływają na jakość
* Mutacja
	* dla każdego wymiaru osobno modyfikuje się parametr $\sigma$ - losowo bez związku z funkcją celu
	* x jest mutowany z użyciem nowej wartości parametru $\sigma$
* Selekcja przyczynia się do adaptacji
	* większą szansę na rozmnożenie się mają te punkty które są lepsze
	* lepsze będą punkty, które są mutantami punktów lepszych z dobrymi parametrami

suma pod exp ma wartość oczekiwaną równą 0 (tak dobrane parametry $\tau$)

$$ \sigma_j = \sigma_j \exp(\tau a + \tau' a_j) $$
$$ \tau = \frac{1}{\sqrt{2n}} \quad \tau' = \frac{1}{\sqrt{2\sqrt{n}}} $$
$$ a, a_j \sim N(0,1) $$
$a$ jednakowe dla wszystkich skladowych, $a_j$ losowane per składowa

Metoda jest obciążona w stronę zmniejszania zasięgu mutacji
jak jesteśmy w minimum lokalnym, to największy współczynnik sukcesów da zmniejszanie zasięgu mutacji do 0

jak to naprawić? może reguła 1/5

## Mutacja wariantowa z wyborem zależnym od poprawy
* Jest wiele wariantow np ewolucji różnicowej
	* nie wiemy który jest najlepszy, każdy jest potencjalnie dobry
* Mamy k wariantów mutacji
* Na początku każdy ma prawdopodobieńśtwo wyboru jednakowe
* Prawdopodobieństwo wyboru zależne od tego ile mutantów było lepsze od ich rodziców
* Dla każdego punktu wybieramy losowo schemat mutacji
	* jeśli nowy jest lepszy niż stary to podmiana, jak nie to odrzucenie
	* jeśli punkt był lepszy to schemat mutacji był dobry więc zwiększamy prawdopodobieństwo wyboru

Można by zastosować jakieś podejście oparte o opóźnione nagrody
Algorytm nie powinien szukać poprawy na już tylko w dłuższej perspektywie

Można zmienić regułę korekty prawdopodobieństwa wyboru wariantu o inne kryteria
np. o rozproszenie populacji


na slajdzie mutaja wariantowa z wyborem zależnym od poprawy
$n_s$ - zdyskontowany współczynnik sukcesu
będą wygaszane te schematy które były wybierane ale przestały już przynosić sukcesy
parametry $\alpha$, $\beta$ regulują czy wolniej czy szybciej zapomina

## SADE
* Komitet operatorów
	* rand/1
	* best/1
	* current-to-bet/1
	* best/2
	* rand/2
* Krzyżowanie bin
* Każdy punkt przetwarzany z indywidualnymi wartościami F i CR
	* to nie jest adaptacja, są losowe
* $F \sim N(0.5, 0.09)$ obcięte do $(0,2]$
* $CR \sim N(CRm, 0.01)$ obcięte do $[0,1]$
* $CRm$ podlega adaptacji proporcjonalnie do sukcesów na poziomie populacji
* Ograniczenia kostkowe i reinicjacja
* Jeśli krzyżowanie poprawia jakość to jest sukces, jak nie to porażka
* Okresowe uruchomienie metody quasi-Newtona
	* do optymalizacji lokalnej, zwiększa precyzję
	* "brudny chwyt"
* W benchmarkach działa lepiej niż którykolwiek ze składowych schematów

## Po co to wszystko
* Zagadnienia dla których nie ma dokładnych algorytmów
* Metody optymalizacji są używane w uczeniu sieciach neuronowych
	* w storjeniu modeli maszynowego uczenia
* mamy dane
	* modelujemy je modelem z katalogu
	* dopasować model to zminimalizować funkcję straty
* Dwa nurty
	* np. modele z połączeniami między warstwami daje łatwiejsze w optymalizacji funkcje celu
	* pytanie czy iść w bardziej rozdmuchane modele i prostsze metody optymalizacji
	* czy komplikować metody optymalizacji żeby lepiej sobie radziły z trudnymi funkcjami straty
* nadzieja w przeskalowaniu w górę najefektywniejszych metod (DE, CMAES) optymalizacji - szybko osiągają niezłe rozwiązania
	* czy da się je przeskalować do milionów parametrów
* Maszynowe uczenie to tylko jeden z przykładów zadań
* Projektowanie wspomagane komputerem (CAD)
	* np. chcemy konkretnych wartości fizycznych dla jakiejś konstrukcji
	* optymalizuje się parametry dla najmniejszego kosztu i spełnienia ograniczeń fizycznych
	* optymalizator i symulator
* Zagadnienia odwrotne
	* identyfikacja parametrów na podstawie modelu
	* polega na dopasowaniu do krzywej
	* krzywa zmierzona i krzywe z symulatora
	* nie chodzi o jak najlepsze charakterystyki
	* jakie parametry trzeba dać do symulatora żeby dostać taką krzywą jak zmierzyliśmy
* Sterowanie predykcyjne
	* elektrownia, którą można sterować (nie wiatraki)
	* trzeba bilansować obciążenie sieci energetycznej
	* np. elektrownie wodne, atomowe, węglowe - możemy sterować ile energii wytworzy
	* w kotle elektrowni węglowej
	* jak jest za dużo tlenu to spada sprawność bo chłodzenie
	* jak za mało to niepełne spalanie, powstaje CO
	* optymalizator na bieżąco na podstawie modelu znajduje optymalną ilość powietrza do kotła

Nie omawialiśmy metod optymalizacji których stanem są rozkłady prawdopodobieństwa (CMAES)
Dualizm miedzy reprezentacją z rozkładem prawdopodobieństwa, a reprezentacją ze zbiorem punktów

więcej teorii na przedmiocie algorytmy heurystyczne na studiach magisterskich

Zadania optymalizacji wielokryterialnej