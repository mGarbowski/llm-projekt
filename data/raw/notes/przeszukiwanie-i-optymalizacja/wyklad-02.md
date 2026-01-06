# (2024-10-16)

## A*
Kolejka priorytetowa

Przeszukiwanie najpierw-najlepszy, gdzie priorytet to liczba krawędzi od węzła początkowego - BFS

rysunek poziomicowy (poglądowy)
funkcja heurystyczna sprawia, że poziomice są przesunięte w stronę węzła docelowego
idealna funkcja heurystyczna - poziomica obejmuje wszystkie węzły na ścieżce do węzła docelowego

## Funkcja celu
Funkcja celu zależy od rozwiązywanego zadania

Funkcja zysku razem z funkcją heurystyczną stanowią priorytet - mówią w jakiej odległości od korzenia jest dany węzeł drzewa przeszukiwania

Sposoby organizacji przestrzeni
* relacja sąsiedztwa - węzły w drzewie 

Chcemy drugiej informacji, która jest lokalnie dostępna, a prowadzi do globalnie porządanego celu

Funkcja heurystyczna - nadmiernie optymistyczna i monotoniczna
i poza tym mniej kosztowna obliczeniowo niż samo rozwiązanie problemu!!

## Przykład - łamigłówka 15
### Reprezentacja - stan łamigłówki
Sąsiedztwo - łlamigłówka po przesunięciu jednego elementu
Przestrzeń przeszukiwań nie będzie drzewem - będą cykle
A* służy tylko do przeszukiwania przestrzeni zorganizowanej w drzewo
Żeby przekształcić taką przestrzeń w drzewo - trzeba by zapamiętać wszystkie węzły żeby wykrywać cykle

### Reprezentacji - sekwencja ruchów
Ciąg decyzji
Wykonanego ruchu nie można już odjąć - nie zmienia się historia
Jest wiele sekwencji, które doprowadzą do rozwiązania
Szukamy możliwie najkrótszej ścieżki
Decyzje układają się w drzewo - możemy użyć A*
Potrzeba funkcji kosztu i funkcji heurystycznej
Funkcja kosztu - liczba wykonanych decyzji (wysokość węzła)
Funkcja heurystyczna

liczba elementów nie na swoim miejscu - jest nadmiernie optymistyczna
lepsze oszacowanie - suma odległości elementów od docelowych miejsc

Czy funckja jest monotoniczna?

## Kiedy można mówić o funkcji heurystycznej
* Zadanie jest złożeniem składników
* Da się ocenić rozwiązanie cząstkowe
* Przestrzeń przeszukiwań obejmuje rozwiązania cząstkowe
* Algorytmy wszerz, w głąb, najpierw najlepszy są stosowalne w przestrzeniach rozwiązań cząstkowych
* Porządana jest drzewiasta struktura przestrzeni
* A* jest odmianą najpierw najlepszy, która korzysta z sumy funkcji kosztu i funkcji heurystycznej

Trzeba znaleźć tą rzecz w zadaniu, która sprawia że problem jest trudny (przedmiotów w plecaku nie da się podzielić, klocki w 15 sobie przeszkadzają)
Jeśli relaksacja założenia sprawia, że problem staje się bardzo prosty
Przestrzeń z ograniczeniem jest podzbiorem przestrzeni ze zdjętym ograniczeniem
Szukamy sensownego nadzbioru, który zawiera wszystkie dopuszczalne rozwiązania i jest możliwie najmniejszy (ma najmniej niedopuszczalnych rozwiązań)

# Przeszukiwanie niedrzewiastych przestrzeni

## Algorytm wspinaczkowy
```
initialize(x)
log.append(x)
while !stop
	Y = neighbourhood(x)
	y = selectBest(Y)
	if q(y) > q(x)
		x = y
	log.append(Y)
```


Algorytmy gradientowe - algorytmy najszybszego spadku/wzrostu

Dane przy trenowaniu sieci nauronowej to próbki
Szukamy przybliżenia jakiejś funkcji (klasyfikacji lub regresji)

Standardowa metoda gradientowa też ma w sobie zaszytą losowość - wybór danych do trenowania
Tym łatwiej się pogodzić ze stochastycznym gradientem - jest mniej kosztowny obliczeniowo i dodatkowo wystartowany z tego samego punktu nie zawsze dojdzie do tego samego punktu

### Stochastyczny algorytm wspinaczkowy
```
initialize(x)
log.append(x)
while !stop:
	y = selectRandom(neighbourhood(x))
	if q(y) > q(x):
		x = y
	log.append(y)
```

Nie ma gwarancji że znajdzie minimum lokalne (losowanie ze zwracaniem wybiera ten sam punkt)

## Błądzenie przypadkowe
Algorytm wspinaczkowy bez elementu decyzyjnego

```
initialize(x)
log.append(x)
while !stop:
	x = selectRandom(neighbourhood(x))
	log.append(x)
```

Nie ma tendencji do utykania w otoczeniu optimów lokalnych
Jaka mamy nieskończenie wiele czasu to znajdzie optimum globalne

## Symulowane wyżarzanie
```
initialize(x)
log.append(x)
while !stop:
	y = selectRandom(neighbourhood(x))
	if q(y) > q(x):
		x = y
	else if uniform(0,1) < p_a:
		x = y
	log.append(y)

p_a = exp(-|q(y) - q(x)| / T)
```

T - temperatura
analogia to procesu krystalizacji
parametryzuje to jaką odległość uznaje się za dużą

Jest szansa że algorytm zaakceptuje gorszy punkt
Pomieszanie algorytmu wspinaczkowego z błądzeniem przypadkowym

dla p_a == 1 - błądzenie przypadkowe
dla p_a == 0 - stochastyczny algorytm wspinaczkowy

Zbieżność lokalna i zbieżność globalna

wartość p_a określa balans między eksploracją a eksploatacją

Przy symlowanym wyżarzaniu zaczyna się od arbitralnie wybranej wysokiej temperatury i obniża się z kolejnymi iteracjami
np. wg reguły $T(t+1) = \alpha T(t), 0 < \alpha < 1$
