# c.d.

## Problemy z optymalizacją
* Występowanie optimów lokalnych czyni zadanie praktycznie nierozwiązywalnym
* W optymalizacji dyskretnej bywa skończony zbiór rozwiązań, w ciągłej - nie
* Liczba sąsiadów w optymalizacji ciągłej jest nieskończona
	* nie można precyzyjnie znaleźć nawet optimum lokalnego
* Bez dodatkowej wiedzy nie można stwierdzić optymalności punktu
	* kiedy zatrzymać metodę optymalizacji
	* stosowane kryteria (np. budżet zasobów) niczego nie gwarantują
* Optymalizacja ciągła - błędy numeryczne
	* nie da się reprezentować liczby rzeczywistej z dowolną dokładnością

Matematycznie precyzyjne rozwiązanie nie zawsze musi być potrzebne biznesowo

Nie zawsze bardziej pożądane jest optimum globalne od lokalnego
Abstrakcyjna reprezentacja problemu może być jego przybliżeniem
Problem może być w rzeczywistości obarczony niedokładnością/niepewnością
Funkcja celu może mieć lepszą charakterystykę wokół optimum lokalnego niż globalnego

## Metody heurystyczne
* Metoda, która często daje dość dobre rozwiązania i wykorzystuje wiedzę dziedzinową

### Metaheurystyki
* Np. algorytmy genetyczne / ewolucyjne
* Techniki inspirowane naturą

## Problem plecakowy
* Drzewo decyzji
	* węzły nieterminalne reprezentują częściowe decyzje
	* liście reprezentują pełne decyzje do wszystkich przemdiotów
* Algorytm najpierw najlepszy
	* jako pierwszy węzeł terminalny znajdzie najlepsze rozwiązanie jeśli etykiety są dokładne (i w ogóle jeśli zachowana jest relacja)
* Funkcja zysku
* Funkcja heurystyczna
	* oszacowanie ile zysku może nam przybyć po dopełnieniu plecaka
	* sortujemy przedmioty po stosunku ceny do wagi i bierzemy od najlepszych tyle ile się zmieści
* Zsumowanie wartości funkcji heurystycznej i częściowej funkcji zysku daje górne oszacowanie dokładnej wartości etykiety
	* niewystarczające żeby zagwarantować znalezienie najlepszego rozwiązania za pierwszym razem
	* na najlepszej ścieżce muszą być największe etykiety
	* oszacowanie urealnia się wraz ze zbliżaniem się do węzła terminalnego
* Lokalna informacja - wiemy ile zysku da częściowa decyzja
	* rozwiązanie komponuje się ze składowych elementów
	* późniejsze decyzje nie zaburzą zysku z już podjętych decyzji
* Dopuszczalność
	* nadmierny optymizm
	* dla maksymalizacji $g(x) + h(x) \ge g(xt)$
* Monotoniczność
	* błąd oszacowania maleje wraz ze zbliżaniem się do rozwiązania
	* dla maksymalizacji $g(x_i) + h(x_i) \ge g(x_{i+1}) + h(x_{i+1})$

### Algorytm A*
```
A := init(s_0)
best := s_0

while !stop
	x := popPriorityQueue(A)
	if g(x) + h(x) >= g(best) + h(best)
		Y := neighbors(x)
		A := A union Y
```

* Jeśli funkcja heurystyczna jest dopuszczalna i monotoniczna to zmniejsza się liczbę rozwijanych węzłów
* Algorytm musi wyczerpać listę A, żeby dać gwarancję uzyskania wyniku optymalnego

## Poszukiwanie najkrótszej drogi z miasta do miasta
* Poszukujemy najtańszej ścieżki w grafie
* Przestrzeń przeszukiwań
	* przestrzeń ścieżek w grafie zaczynających się w mieście startowym
	* rozwiązania dopuszczalne - ścieżki kończące się w mieście docelowym

## Problem komiwojażera
* Poszukiwanie cyklu hamiltona o najniższej sumie wag
* Przestrzeń przeszukiwań to przestrzeń ścieżek (zaczynających się w mieście startowym)
* Funkcja kosztu - suma wag krawędzi w ścieżce
* Funkcja heurystyczna
	* znamy liczbę krawędzi w poszukiwanym cyklu
	* dolne oszacowanie przez wzięcie kosztu najtańszej krawędzi razy liczba niewybranych krawędzi ($k$)
	* dolne oszacowanie przez wzięcie $k$ najtańszych niewybranych krawędzi w grafie