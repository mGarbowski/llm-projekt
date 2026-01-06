Zadanie 1
nie chodzi o rozwiązanie zadania
chodzi o zdefiniowanie problemu i opisanie go
samo rozwiązanie jest wtórne

reprezentacja rozwiązania
funkcja celu / zysku
funkcja heurystyczna
definicja sąsiedztwa (przy symulowanym wyżarzaniu)
operator przekształcający (np. mutacja w algorytmie ewolucyjnym, generowanie losowego sąsiada w stochastycznym wzroście)

algorytmy są wymuszone

reprezentacja rozwiązania - zbiór decyzji, które trzeba podjąć
A* częściowo podjęte decyzje
czyli np wektory zer, jedynek i znaków zapytania

przykład koncentratora
podgraf będzie zawierał wsystkie węzły
analogiczne do problemu komiwojażera

krawędzi musi być o 1 mniej niż węzłów
jak w grafie jest k krawędzi

mamy wektor k elementowy, gdzie element jest 0,1,? (dla każdej krawędzi bierzemy, nie bierzemy albo jeszcze nie wiadomo)

w symulowanym wyżarzaniu w wektorze są tylko 0 i 1, długość k
ma być n-1 wybranych krawędzi, gdzie n jest liczbą węzłów
każda reprezentacja ma szansę być reprezentacją koncentratora ale nie musi

reprezentacje w symulowanym wyżarzaniu to węzły terminalne z drzewa do A*

minimalizujemy sumę wag - funkcja kosztu
sumujemy wagi tam gdzie są jedynki w wektorze
jeśli w wektorze jest więcej niż n-1 jedynek to rozwiązanie niedopuszczalne

funkcja heurystyczna - suma wag tylu niewybranych krawędzi ile brakuje do n-1
to najlepszy możliwy przypadek, monotoniczna i dopuszczalna

zamieniając znak zapytania na jedynke - ...
zamieniając znak zapytania na zero - ...

wzrost kosztu większy lub równy spadkowi funkcji heurystycznej
szukamy w miare ciasnego oszacowania optymistycznego (dla minimalizacji oszacowania z dołu)

w symulowanym wyżarzaniu - losowy sąsiad - zamiana losowego 0 z losową 1
ale nie każdy wektor reprezentuje koncentrator
blokujemy takie zamiany które prowadzą do nie bycia koncentratorem - poprawne ale niedobre
możemy dopuścić, żeby wektor nie reprezentował koncentratora - można wprowadzić karę np. suma wag wszystkich krawędzi w grafie - każdy punkt dopuszczalny będzie lepszy niż niedopuszczalny

możemy wybrać reprezentację, gdzie liczba jedynek jest dowolna i dolicza się karę


### Przykład - bąbelki
Taka sama reprezentacja jak ostatnio do A* - k krawędzi w grafie, wybieramy mniejszą liczbę z nich

dopiero po dostawieniu ostatniej jedynki wiemy czy rozwiązanie jest dopuszczalne (wiemy czy są cykle)

wybieramy tyle krawędzi co wierzchołków w grafie (cykl ma tyle samo krawędzi co wierzchołków)

funkcja kosztu - suma krawędzi wchodzących w skład bąbelków

w symulowanym wyżarzaniu też tak jak poprzednio
ma być n jedynek
najprostsza modyfikacja (sąsiedztwo) to zamiana losowego zera z losową jedynką

nie każdy wybór krawędzi daje bąbelki - dokładamy funkcję kary
minimum globalne będzie tam gdzie optymalne rozwiązanie - minimalna suma wag i zerowa kara

### Przykład VNS

po m_1 iteracji znajdzie się w optimum lokalnym gorszym bo różni się o m_1 bitów
potem zacznie zwiększać promień sąsiedztwa

2 możliwości 
K=3 pozwala przejść do zbioru przyciągania jeśli m_2 <= 3
bo to lepsze optimum lokalne jest otoczone słabymi punktami
da się dojśc do lepszego optimum lokalnego tylko jeśli wygeneruje się je jako sąsiada

podczas podchodzenia do pierwszego optimum lokalnego
w każdej z m_1 iteracji generuje się n zmian bitowych n * m_1 obliczeń funkcji celu
potem jest rozszerzanie do promienia 2 i 3 $m_1 \cdot n \cdot \binom{n}{3}$

jeżeli m_2 > 3 to algorytm zatrzyma się w optimum lokalnym gorszym

jeśli m_2 == 3 będzie generowanie sąsiadów lepszego optimum lokalnego
(algorytm dochodzi do lepszego optimum i potem znowu rozszerza się do promienia 3 kiedy już nie znajdzie lepszego punktu)

### Przykład tabu
jak na wykładzie - algorytm prawie wspinaczkowy z tabu zorganizowanym jako fifo
jeśli wielkość tabu jest równa rozmiarowi większego zbioru przyciągania

startuje w zbiorze przyciągania gorszego optimum
generuje wszystkich sąsiadów, znajduje lepszego i do niego przechodzi
na początku wspina się do optimum lokalnego gorszego
w najgorszym przypadku będzie jak najwolniej schodził z optimum lokalnego
może w najgorszym wypadku sprawdzić wszystkie punkty z gorszego zbioru przyciągania zanim dojdzie do lepszego zbioru przyciągania
cały zbiór przyciągania gorszego zbioru przyciągania wejdzi do tabu
potem będzie sprawne wejście do lepszego optimum - będzie w najgorszym razie m_2 iteracji

będzie v1 + m2 * n obliczeń funkcji celu - górne oszacowanie
mnożymy przez n bo punkt ma n sąsiadów 
w początkowej fazie nie będzie  * n bo wszystkich punktów jest v1 i nie będą sprawdzane jeśli już są w tabu

### Przykład - zadanie 3
dla q_1 - po wstawieniu do wzoru wychodzi inny rozkład prawdopodobieństwa
q_2 - będzie tak samo bo się upraszcza we wzorze

$$
p_a = \exp(-\frac{|q(y) - q(x)|}{T})
$$

$$
p_a = \exp(-a\frac{|q(y) - q(x)|}{T})
$$

### Przykład - algorytm ewolucyjny
Dla selekcji proporcjonalnej
aq(x) - nie zmienia
q(x) + b

Można mieć notatki na kolosie!!!

może być pytanie typu co by było gdyby zmienić algorytm (np. wyłączyć mutację w algorytmie ewolucyjnym)
jak rozszerzyć tabu do R^n

jak rozszerzyć VNS do przestrzeni ciągłej - może dla algorytmu stochastycznego wzrostu
można by sterować odchyleniem modyfikacji gaussowskiej przez promień sąsiedztwa VNS
np. dla algorytmu mutacyjnego jeśli grzęźnie w optimum to zwiększamy standardowe odchylenie

konkretna odpowiedź, 1-2 zdania odpowiedzi