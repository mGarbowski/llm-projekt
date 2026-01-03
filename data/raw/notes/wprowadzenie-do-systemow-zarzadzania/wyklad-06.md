# Programowanie liniowe (2024-04-08)
Projekt będzie wymagał zamodelowania i rozwiązania problemu decyzyjnego

Nazwa jest zaszłością historyczną, bardziej poprawnie modele liniowe

## Zadanie programowania liniowego
Polega na znalezieniu optymalnych wartości zmiennych decyzyjnych $x = \langle x_1, x_2, \ldots, x_n \rangle$ ze zbioru **liczb rzeczywistych** maksymalizujących funkcję celu $\max_x x_0 = \sum_{j=1}^n c_jx_j = cx$, przy spełnieniu ograniczeń $\sum_{j=1}^n a_{ij}x_j = b_i$ ($Ax=b$), $x_j \ge 0$. Współczynniki $a, b, c$ są znane (są danymi wejściowymi modelu). Ograniczeń jest mniej niż zmiennych decyzyjnych (inaczej nie może być wielu rozwiązań).

### Inne postaci zadania PL
* Znak $\le$ lub $\ge$ w ograniczeniach
	* nie może być $<, >$ - źle zdefiniowane zadanie 
* $\min$ zamiast $\max$
* $x$ nieograniczone lub ograniczone z jednej / obu stron

### Przekształcanie modelu
Z każdej postaci można przejść w każdą inną

* przez zmianę znaku przy min/max
* wprowadzenie zmiennych decyzyjnych dopełniających
* ograniczenie równościowe zamienić na dwa nierównościowe
* zamianę zmiennych niograniczonych na nieujemne

Model liniowy możemy zastosować tylko jeśli wszystkie zalezności rosną proporcjonalnie - nie zawsze nadaje się do modelowania rzeczywistego problemu.

Rozwiązanie spełniające ograniczenia - dopuszczalne (feasible)

## Interpretacja graficzna
* Ograniczenia wyznaczają wielokąt (w przypadku 2-wymiarowym) - część wspólna półpłaszczyzn
* Punkt optymalny będzie na brzegu
* Może być więcej niż jedno rozwiązanie optymalne jeśli funkcja celu i jedno z ograniczeń są liniowo zależne
* Ograniczenia mogą być sprzeczne - część wspólna będzie zbiorem pustym

## Kiedy nie ma optymalnego rozwiązania
* Dzieli się ograniczenia na twarde i miękkie
* Miękkie ograniczenia można całkowicie pominąć
* Przekroczenie miękkich ograniczeń można minimalizować w funkcji celu
* Zbiór może być nieograniczony
	* najprawdopodobniej wynika z błędu modelowania
* Trzeba dokładnie czytać komunikat końcowy solvera

## Algorytm simplex
* Wyznacz początkowy punkt wierzchołkowy
* Czy rozwiązanie jest gorsze od sąsiednich
	* jeśli nie to znaleziono rozwiązanie optymalne
* Przejdź do sąsiedniego punktu wierzchołkowego dającego lepszą wartość funkcji celu
* Powtarzaj od kroku 2
* W najgorszym wypadku ma wykładniczą złożoność
* Stosuje się heurystyki dla wyboru sąsiada
* Sam problem programowania liniowego daje się rozwiązać algorytmem wielomianowym (ale jest wolniejszy w praktyce)
* Powszechnie stosowany
* Wydajny w typowych przypadkach

## Modelowanie funkcji celu typu minmax
Sztuczka, może być przydatna do projektu
Wyznaczanie $\max (\min (x_1, x_2, x_3))$, z ograniczeniami liniowymi z góry

Można zapisać w postaci programowania liniowego
$z \le x_1, z \le x_2, z \le x_3$
$\max z$
??

## Założenia modelu
* Liniowość
* Pełna podzielność
* Brak niepewności 
* Jedno kryterium oceny




