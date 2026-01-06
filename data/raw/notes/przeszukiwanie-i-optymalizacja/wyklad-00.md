# Organizacja
* Kolokwia z notatkami drukowanymi
* 2 kolokwia po 25pkt, min 15pkt z obu(?)
* Projekt na 50pkt, min 20pkt
* Standardowa skala ocen
* Slajdy z wykładów na teamsach

## Projekt
* Jedno większe zadanie
* Za miesiąc będą tematy
* Nacisk na testowanie
	* przeprowadzić badanie na algorytmie, czy przynosi korzyść itd
	* statystyczna analiza wyników na długotrwałym eksperymencie
	* będzie trzeba odpalić długotrwałe testy
	* lepiej mieć do świąt gotową implementacje żeby się wyrobić
* Dwuosobowe zespoły
* Będzie można się przenosić między grupami w usosie żeby być z osobą na projekt

## Wstęp

## Słaba sztuczna inteligencja
* Uczenie maszynowe
	* objaśnianie zjawisk
	* analiza przewidywanie zjawisk
	* analiza scenariuszy
* Podejmowanie decyzji
	* tryb doradczy
	* tryb autonomiczny

## Sortowanie bąbelkowe
* Permutacje to węzły w przestrzeni przeszukiwania
* Permutacje o parze sąsiednich elementów zamienionych miejscami są połączone krawędziami
* Operacja elementarna
* Sortowanie z punktu widzenia przestrzeni rozwiązań to znalezienie ścieżki w grafie do węzła z posortowaną tablicą
* Ruch w stronę rozwiązanie przechodzi do węzła, w którym liczba par w niedobrej kolejności maleje
	* zamiana sąsiednich elementów może zwiększyć albo zwiększyć liczbę par w złej kolejności o 1
	* algorytm sortowanie bąbelkowego tylko zmniejsza

## Funkcja celu
* (Objective function)
* W jakim stopniu cel jest spełniony / niespełniony
	* dla sortowania bąbelkowego to liczba par, które nie spełniają relacji porządku

## Przestrzeń przeszukiwań
* Zbiór reprezentacji rozwiązania
* Sposób organizacji przestrzeni
	* relacja sąsiedztwa - zbiór elementów oddalonych nie dalej niż promień sąsiedztwa
	* metryka - odległość między elementami
* Przykład - przestrzeń wektorów binarnych
	* sąsiedztwo - wektory sąsiadują jeśli różnią się 1 bitem (metryka Hamminga)
* Przykład przestrzeń permutacji
	* metryka edycyjna - liczba zamian par dowolnych elementów

## Zadanie optymalizacji
### Przestrzeń przeszukiwań
* Zbiór reprezentacji rozwiązania $X$
* Sposób organizacji przestrzeni
	* relacja sąsiedztwa $N: X \rightarrow 2^X$
	* metryka $\delta: X \times X \rightarrow \mathbb{R}$
	* sąsiedztwo a metryka $N_r(x) = \{ y \in X, \delta(x,y) < r \}$
* Ocena rozwiązań (wariantowo)
	* funkcja celu $q: X \rightarrow \mathbb{R}$
	* relacja porównująca $compare: X \times X \rightarrow \{-1, 0, 1\}$
	* czasami nie jest potrzebna konkretna wartość funkcji celu, tylko wystarczy relacja jej wartości między dwoma elementami (np. sortowanie bąbelkowe)


### Typowe zadanie optymalizacji ciągłej
* Funkcja celu $q: F \rightarrow \mathbb{R}$
* Zbiór dopuszczalny $F \subseteq \mathbb{R}^n$
* Metryka $\delta(x,y) = ||x-y||$
* Norma euklidesowa $||x-y|| = (\sum_{i=1}^n (x_i-y_i)^2)^{1/2}$
* Każdy punkt dopuszczalny spełnia
	* ograniczenia kostkowe (bound constraints) $l_i  \le x_i \le u_i$
	* ograniczenia funkcyjne $g_j(x) \le 0, h_j(x) = 0$

### Minimum lokalne
$$
\forall_{y \in N_r(x)} \quad q(x) < q(y)
$$
### Minimum globalne
$$
\forall_{y\in X} \quad q(x) < q(y)
$$

### Funkcja unimodalna
Ma jedno minimum lokalne i jednocześnie globalne


Uczenie klasyfikatora przez minimalizację funkcji starty
Klasyfikator liniowy charakteryzują 2 parametry $p_1 x_1 + p_2 x_2 + 1 = 0$
Przeszukiwanie przestrzeni $(p_1, p_2)$, np. metodą gradientową


## Zadania łatwe i trudne
* Zadanie optymalizacyjne ma poza wymienionymi wyżej
	* kryterium zatrzymania - dla sortowania proste, dla problemu komiwojażera - problematyczne
	* punkt startowy (np. tablica którą chcemy posortować, losowe parametry klasyfikatora liniowego)
* Problem łatwy (P)
	* każda ścieżka wzdłuż nierosnącej funkcji celu prowadzi do celu (jedno minimum lokalne)
	* długości w/w ścieżki wielomianowo zależy od ilości danych
	* liczność sąsiedztwa punktu wielomianowo zależy od ilości danych

Maszyna Turinga
* Model obliczeń
* Taśma
* Głowica czytająco-pisząca
* Program (graf sterowania)

Losowość rozumiemy jako czynnik zewnętrzny, poza naszą kontrolą, nie rozstrzygając natury samego zjawiska.

Problem NP - rozwiązywany przez niedeterministyczną maszynę Turinga w czasie wielomianowym
Problem NP-zupełny
* nie jest znany algorytm rozwiązujący problem w czasie wielomianowym
* każdy problem np-zupełny jest sprowadzalny w czasie wielomianowym do każdego innego np-zupełnego

Dla zadania sortowania funkcja celu ma dokładnie jedno minimum lokalne (jest unimodalna).
W problemie komiwojażera nierosnące ścieżki mogą się skończyć w 2 różnych rozwiązaniach.

### Kłopoty z optymalizacją
* Występowanie optimów lokalnych czyni zadanie praktycznie nierozwiązywalnym
* W optymalizacji dyskretnej bywa skończony zbiór rozwiązań, w ciągłej - nie
* Liczba sąsiadów w optymalizaci ciągłej jest nieskończona
	* nie można precyzyjnie znaleźć nawet optimum lokalnego
* Bez dodatkowej wiedzy nie można stwierdzić optymalności punktu
	* kiedy zatrzymać optymalizację
* Błędy numeryczne w optymalizacji ciągłej