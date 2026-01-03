# Siatki trójkątów

## Modele 3D
* Modele nigdy nie mają oczekiwanej dokładności i formatu
* Ograniczenie
	* oprogramowanie
	* urządzenia do zbierania danych
* Kompromis między
	* wielkością modelu
	* wydajnością renderingu
	* jakością rezultatów
* Modele się upraszcza żeby osiągnąć kompromis

## Zagadnienia
* Triangulacja (ogólnie teselacja)
	* zamiana wielokątów na łatwiejsze do operacji prymitywy (trójkąty)
* Konsolidacja
	* złożenie pojedynczych wielokątów w siatkę
	* tworzenie nowych danych (np. wektory normalne)
* Optymalizacja
	* w celu przyspieszenia renderingu
	* zmiana ustawienia wielokątów
* Upraszczanie
	* usuwanie nieistotnych danych z siatki
* Kompresja
	* minimalizacja miejsca potrzebnego do przechowania siatki

## Teselacja
* Podział powierzchni na zbiór wielokątów z uwzględnieniem pewnych kryteriów
	* podział na regiony wypukłe
	* podział na trójkąty (triangulacja)
	* podział na jednorodne regiony
* Większość algorytmów zakłada, że punkty wielokąta leżą w jednej płaszczyźnie
	* nie ma zawijanych płaszczyzn itp.
* Bazowy algorytm
	* zbadaj każdą linię pomiędzy dowolnymi punktami wielokąta
	* sprawdź czy wybrana linia przecina lub nakłada się na krawędź
		* jeżeli nie, podziel wielokąt na dwa i kontynuuj dla każdego ze stworzonych wielokątów
		* jeżeli tak, wybierz inną parę

### Ear clipping
* Algorytm triangulacji
* Przeglądanie wszystkich trójek $v_i, v_{i+1}, v_{i+2}$
* Sprawdzenie czy $v_i-v_{i+2}$ nie przecina żadnej krawędzi
	* jeśli tak to trójkąt jest odcinany
	* sprawdzenie czy wierzchołki nie tworzą uszu
* Powtarzanie dopóki istnieją uszy
* Ucho - trójkąt którego dwie krawędzie pokrywają się z krawędziami wielokąta, a jedna krawędź leży wewnątrz

### Problemy w triangulacji
* Pękanie krawędzi
	* jak obiekty się stykają - dzielą krawędzie
	* należy zadbać o poprawny podział
	* zwykle dla modeli powierzchniowych
* T-wierzchołki
	* dwa modele dzielą krawędź, ale nie wszystkie wierzchołki
	* powstają artefakty cieniowania
	* 3 punkty współliniowe zostaną potraktowane jako trójkąt - w renderze wyjdzie krawędź
	* trzeba inaczej podzielić (retriangulacja) albo może przesłać wierzchołki w innej kolejności

## Konsolidacja
* Po teselacji mamy reprezentację złożoną z wielokątów (trójkątów)
* Do rozpatrzenia
	* łączenie wielokątów
	* orientacja wielokątów
	* generacja wektora normalnego dla wierzchołka

### Łączenie wielokątów
* Niektóre dane przychodzą w formie zupy wielokątów - rozłączne wielokąty
* Jeśli dwa trójkąty dzielą krawędź to duplikują się dane - wiele razy te same wierzchołki
	* nieefektywne wyświetlanie
	* marnowanie pamięci
* Najprostsza definicja siatki (mesh)
	* lista wierzchołków - współrzędne, normalne, współrzędne tekstur itd.
	* lista wytycznych - lista indeksów całkowitoliczbowych - wskazanie na wierzchołek w liście wierzchołków
* Siatka trójkątów
	* ograniczenie wielokątów do trójkątów

### Hashing
* Inicjalizuj licznik wierzchołków na 0
* Dla każdego wielokąta
	* spróbuj dodać wierzchołek do tablicy haszującej
* Jeśli wierzchołka nie ma w tablicy
	* dodaj i zainicjalizuj licznik wystąpień
	* dodaj do ostatecznej listy wierzchołków
* Jeżeli jest w tablicy
	* weź indeks
	* zapisz wielokąt wraz z indeksami, które wskazują wierzchołki
* Po przetworzeniu wszystkich wierzchołków listy będą kompletne

### Welding
* Mogą trafić się wierzchołki prawie identyczne
* Należy połączyć ze sobą wierzchołki oddalone nie dalej niż epsilon
* Najprostsza metoda
	* sortowanie z funkcją, która uwzględnia pewien epsilon dla pozycji

### Orientacja trójkątów
* Modele mogą przyjść z różną orientacją
	* normalne trójkątów wskazują poprawny kierunek
* Przetwarzanie wierzchołków zwykle w kierunku przeciwnym do wskazówek zegara
* Stosuje się regułę prawej dłoni
* Algorytm
	* Stwórz struktury typu krawędź-face dla wszystkich wielokątów
	* Posortuj albo oblicz hash dla wszystkich krawędzi, w celu znalezienia pasujących krawędzi
	* Znajdź grupy wielokątów, które się stykają
	* Dla każdej grupy obróć na drugą stronę face'y, w celu osiągnięcia spójności

### Struktura krawędź-face
* Zbiór pół-krawędzi - krawędź należy do dwóch wielokątów
	* krawędź wskazująca na wielokąt
* Wierzchołki są przechowywane w kolejności $v_0<v_1$
* Tworzenie wg kolejności sortowania
	* po kolei współrzędne x, y, z

## Szukanie pasujących krawędzie
* Drugi krok algorytmu
* Znaleźć pasujące krawędzie
	* prosta sprawa, bo krawędzie są przechowywany w kolejności $v_0<v_1$
* Nie ma potrzeby permutacji kombinacji
* Można wykorzystać tablicę haszującą

### Dopasowanie krawędzi
* Jeśli dopasujemy krawędzie to znane są wielokąty sąsiadujące
	* Mamy graf przylegania
* Reprezentacja przez listę
	* dla każdego wielokąta lista face'ów sąsiadujących
* Krawędzie graniczne-  nie ma dwóch sąsiadujących wielokątów
* Zbiór wielokątów połączonych krawędziami - grupa ciągła

### Zapewnienie stałości
* Zmiana orientacji, aby wszystkie wielokąty miały taką samą kolejność konturu
* Algorytm
	* Dla każdej grupy wybierz początkowy wielokąt
	* Weź sąsiadów i sprawdź czy orientacja jest taka sama
	* Jeżeli kierunek przejścia przez krawędź jest taki sam dla dwóch wielokątów, odwróć na drugą stronę sąsiadujący wielokąt
	* Sprawdzaj rekursywnie sąsiadów dopóki wszystkie wielokąty nie będą raz sprawdzone
* Sprawdzenie czy normalna jest do wewnątrz czy na zewnątrz

### Poprawność siatki
* Brak dziur
* Każda krawędź jest wspólna tylko dla 2 trójkątów
	* poza krawędzią brzegową
* Każdy wierzchołek ma jeden ciągły zestaw trójkątów wokół siebie
	* bez "klepsydry"

## Reprezentacja zbioru trójkątów
* Lista trójkątów
	* bardzo nadmiarowe
	* nie ma dzielenia danych między trójkątami
* Lepsze
	* wachlarz
	* paski
	* siatka trójkątów

### Wachlarz
* Wierzchołek centralny
	* współdzielony przez wszystkie wierzchołki
* Definicja przez uporządkowaną listę wierzchołków
* Każdy trójkąt składa się z wierzchołków $v_0,v_i,v_{i+1}$
* Średnia przesyłana liczba wierzchołków na trójkąt
	* $1 + \frac{2}{m}$
	* $m$ - długość wachlarza

### Pasek
* Definicja przez uporządkowaną listę wierzchołków
* Dwa poprzednie wierzchołki + nowy
	* $v_i,v_{i+1},v_{i+2}$
* Średnia liczba wierzchołków na trójkąt $1 + \frac{2}{m}$
	* tak samo jak wachlarz
* Zastosowania
	* źdźbła trawy
	* obiekty, których krańcowe obiekty nie są używane przez inne obiekty
* Często wykorzystywane razem z shaderem geometrii

### Siatka trójkątów
* Tabela wierzchołków
	* współrzędne
	* wektor normalny - średnia z wektorów normalnych ścian
	* współrzędne uv
* Tabela indeksów
	* które wierzchołki tworzą trójkąt
* Oszczędność pamięci - wierzchołek jest pamiętany tylko raz


#### Euler-Poincare
* Charakterystyka Eulera
* $X = v - e + f$
	* $v$ - liczba wierzchołków
	* $e$ - liczba krawędzi
	* $f$ - liczba face'ów
* $g$ - liczba dziur
	* $X = 2 - 2g$
	* $v-e+f+2g=2$
* Każda krawędź ma 2 face'y
* Każdy face ma przynajmniej 3 krawędzie
	* $2e=3f$
* Jeżeli siatka nie ma dziur to $f=2v-4$
* Wnioski
	* dla dużych siatek liczba trójkątów = 2 x liczba wierzchołków
	* każdy wierzchołek - średnio 6 trójkątów
	* średnio 0.5 wierzchołka na trójkąt
* Dlatego siatka trójkątów jest tak dobra

## Cache GPU
* Przetwarzanie wierzchołków FIFO
	* cache jest zorganizowany tak samo
* Przetrzymywanie wyników transformacji wierzchołków
* Miara zużycia cache
	* ACMR - average cache miss ratio
	* średnia ilość wierzchołków do przetworzenia per trójkąt
* Aktualnie
	* przetwarzanie wsadowe
	* skalowalność

## Bufory wierzchołków i indeksów
* Przechowywanie modelu jako ciągły obszar pamięci
* Vertex buffer - tablica wierzchołków o określonym formacie
* Format - definiuje jakie dane są w wierzchołku
* Każdy wierzchołek posiada dane w grupie
* Stride - wielkość wierzchołka w bajtach
* W OpenGL trzeba wyzerować pamięć

## Upraszczanie siatek
* Redukcja danych przy jednoczesnej próbie zachowania wyglądu
* Mniej trójkątów - większa liczba komputerów da radę obsłużyć
	* mniej danych, szybszy rendering
* Typy upraszczania
	* statyczne
	* dynamiczne
	* zależne od widoku

### Upraszczanie statyczne
* Tworzenie modeli przed renderingiem
* Tworzenie osobnych modeli o różnym stopniu szczegółowości
	* Level of Detail
* Zastosowania
	* graficzne shadery webowe - nie da się upraszczać siatki w locie

### Upraszczanie dynamiczne
* Tworzenie modeli w locie
	* ciągły LOD
* Rozpad krawędzi (edge collapse)
	* operacja połączenia 2 wierzchołków w 1 - usunięcie jednej krawędzi

#### Edge collapse
* Proces jest odwracalny jeśli zachowamy kolejność operacji
	* z uproszczonego modelu da się odtworzyć bardziej skomplikowany
* Możliwość optymalizacji transmisji danych
* Proces niezależny od widoku
* Zależność operacji od przyjętej strategii
	* można np. wybrać wierzchołek po środku
	* w praktyce - albo punkty skrajne albo środek
* Algorytm nie zawsze działa
	* przy wklęsłości nowa krawędź może przecinać się z powierzchnią
	* sprawdzenie - czy odwraca się wektor normalny

#### QEM
* Funkcja kosztu usuwania dla krawędzi
* Bierze pod uwagę nową pozycję, wektor normalny dla płaszczyzny, odległość od źródła
* $c(v) = \sum_{i=1}^m(n_i\cdot v + d_i)^2$
	* $v$ - nowa pozycja wierzchołka
	* $n_i$ - wektor normalny do płaszczyzny
	* $d_i$ - odległość od źródła

### Upraszczanie zależne od widoku
* Techniki przeznaczone do generacji LOD, kiedy jest zmienne w ramach jednego modelu
* W szczególności - teren

## Kompresja a precyzja
* GPU ma ograniczoną pamięć
* Oszczędność czasu
* Kompresja danych
	* same wierzchołki
	* indeksy
	* nie zawsze potrzeba pełnego zakresu liczb całkowitych

### Dane wierzchołków
* Same dane można ograniczyć
	* jak monitor obsługuje ograniczoną paletę kolorów
* Czasami nie ma potrzeby trzymania danych o kolorze wcale
	* np. temperatura
* Kwantyzacja skalarów
	* skala + przesunięcie
* Specjalne właściwości
	* współrzędne tekstur
	* jeśli normalna, i dwie styczne są wzajemnie prostopadłe to wystarczy przechowywać dwie z nich, a trzecią da się wyznaczyć

## Przechowywanie danych

### Wavefront
* Najprostszy format
* Reprezentacja modelu - `.obj`
	* plik tekstowy
	* komentarze `#`
	* `v` dane o pozycji
	* `vt` współrzędne tekstur
	* `vn` wektory normalne
	* `f` face'y
* Reprezentacja materiału - `.mtl`
	* plik tekstowy
	* `Ka` kolor otoczenia
	* `Kd` kolor rozproszenia
	* `Ks` kolor odbicia
	* `Ke` kolor emisji
	* `Ns` współczynnik odbicia
	* `Nl` współczynnik załamania
	* `d` nieprzezroczystość
	* `Tf` kolor załamania

### Alembic
* Wsparcie dla
	* siatek trójkątów
	* powierzchni NURBS
	* hierarchii przekształceń
	* kamer
	* świateł
* Format HDF5
	* umożliwia szybki odczyt losowego fragmentu animacji
	* dobre do symulacji
* Jest open source
