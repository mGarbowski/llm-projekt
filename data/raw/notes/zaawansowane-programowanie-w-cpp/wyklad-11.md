# Kontenery z boost (ZPR- W12 -2020 12 22)
* Naturalne rozszerzenie STL
* Większosć wymienionych jest już elementem standardu

## `std::pair`
* W implementacji tablic asocjacyjnych (klucz-wartość)
* Grupuje dwie składowe
* `std::make_pair`

## `std::tuple`
* `std::make_tuple`
* `auto element = tuple.get<0>()`
* `auto element = get<0>(tuple)`
* Operatory porównania
* `tie` - tworzy krotkę zawierającą referencje (kopiowanie płytkie)

## `std::function`
* Pozwala przechowywać funkcje i funktory
* Klasa-wartość
	* można przechowywać w kolekcjach
* Można inicjować na podstawie
	* funkcji
	* metody
	* funktora
	* lambdy
	* wyniku bind
* Operator wołania funkcyjnego
* Te same zastosowania co wzorzec komendy
	* separacja tworzenia akcji od wołania
	* kolekcjonowanie poleceń

## `std::variant`
* Unia z wyróżnikiem bieżącego typu
* Typy nie muszą dziedziczyć po wspólnej klasie bazowej
* Normalne `union` mogą przechowywać tylko typy wbudowane i POD
	* nie wymagające wołania konstruktora
* Dowolna liczba parametrów
* PObranie obiektu danego typu przez `get<typ>(variant)`
* Konstruktor bezparametrowy - obiekt pierwszego typu
* Konstruktor z jednym argumentem lub przypisanie - przechowuje argument podanego typu
* Poprawny dostęp przez wzorzec wizytatora
	* wykrywa brak typu na etapie kompilacji
	* `boost:static_visitor` - klasa bazowa
	* `apply_visitor`

## `std::optional`
* Przechowuje wartość lub jest pusty
* Zamiast używania specjalnej wartości / pary / wariantu
	* `string::npos`
	* `nullptr`
* Zamiast rzucaniu wyjątku
* Wygodne do użycia w instrukcjach warunkowych
	* operator rzutowania na `bool`
* Konstruktor bezparametrowy - pusty
* `value_or(default)`
* Zamiast `optional<bool>` wrato używać `boost::tribool`
	* ma przeciążone operatory logiczne zgodne z logiką trójwartościową

## `std::any`
* Kontener na wartość dowolnego typu
* Wartość przechowywana na stercie
* Zamiast `void*`
* Metody
	* `empty`
	* `type` zwraca `typeid`
* Dostęp do wartości przez `any_cast<T>(any)`
	* rzuca wyjątek jeśli niezgodne typy
	* albo zwraca `nullptr` jeśli pointer

## `boost::multi_array`
* Tablice wielowymiarowe
* Właściwie kontener jednowymiarowy z przeciążonym operatorem dostępu
* Kształt jako parametr konstruktora
* Nie wyróżnia żadnego z wymiarów przy dostępie

## Boost Graph Library
* Generyczna reprezentacja grafów
* Bardzo wydajna pamięciowo
* Kilkadziesiąt wydajnych implementacji algorytmów grafowych
* Reprezentacje
	* lista sąsiedztwa
	* macierz sąsiedztwa
	* graf skompresowany - bez możliwości zmiany topologii

### Lista sąsiedztwa
* `adjacency_list`
* Parametry szablonu
	* kolekcja na wierzchołki
	* kolekcja na krawędzie wychodzące
	* czy graf skierowany
	* typ użytkownika związany z wierzchołkiem
	* typ użytkownika związany z krawędzią
	* typ użytkownika związany z grafem

### Macierz sąsiedztwa
* Dwuwymiarowa tablica
* Krawędzie w komórkach macierzy
* Parametry szablonu
	* czy skierowany
	* typy użytkownika dla wierzchołków, krawędzi, grafu

### Parametry szablonów
* Kontener przechowujący wierzchołki
	* vecS
	* listS
	* setS
	* multisetS
* Kontener przechowujący krawędzie
* Typ grafu
	* directedS - dostęp do krawędzi wychodzących
	* bidirectionalS - przechowuje krawędzie wychodzące i wchodzące
	* unidirectedS

### Przeglądanie grafu
* Dostęp do wierzchołków
	* `vertices(g)` - para iteratorów - do pierwszego i ostatniego
	* `num_vertixes(g)`
* Dostęp do krawędzi
	* `edges(g)` - para iteratorów
	* `num_edges(g)`
* Krawędzie dla danego wierzchołka
	* `out_edges(v, g)`
* Wierzchołki dla danej krawędzi
	* `source(e,g)`
	* `target(e,g)`
* Iterator może się unieważnić jeśli używany jest wektor

### Związanie własnych danych
* Można związać własne dane z wierzchołkiem i z krawędzią
	* wewnątrz struktur - dodatkowe parametry szablonu

### Modyfikacja grafu
* Niedostępne dla grafu skompresowanego
* `add_vertex(g)`
* `clear_vertex(v, g)` - usuwa krawędzie związane z wierzchołkiem
* `remove_vertex(v,g)` - usuwa, może zostawić wiszące krawędzie
* `add_edge(u,v,g)` - zwraca false jeśli krawędź już istnieje i graf nie pozwala na wiele krawędzi między tymi samymi wierzchołkami
* `remove_edge(u,v,g)`
* `remove_edge(e,g)`

### Algorytmy grafowe
* Kopia
* Transpozycja
* BFS
* DFS
* A*
* Topologiczne sortowanie
* Dijkstra
* Bellman Ford
* Kruskal
* Badanie maksymalnych przepływów
* wiele więcej

### Użycie algorytmów
* Dostarcza się klasy wizytatora, dziedzicząc po bazowym wizytatorze dla danego algorytmu
	* np. `default_bfs_visitor`
	* nadpisuje się metody
* Metody wizytatora przy przeglądaniu grafu
	* `initialize_vertex(v,g)`
	* `discover_vertex(v,g)`
	* `examine_vertex(v,g)`
	* `examine_edge(e,g)`
	* `finish_vertex(v,g)`

### Podsumowanie
* Reprezentacja grafów skierowanych i nieskierowanych
* Jest port do Pythona
* Przeglądanie i modyfikacja grafów
* Można związać własne dane z krawędziami, wierzchołkami lub całym grafem
* Wiele algorytmów

## Trwałość danych
* Możliwość zapisu i odtwarzania stanu obiektów
	* system plików
	* system zarządzania bazą danych
* Niezgodność interfesów wymaga tworzenia pośredniej warstwy
	* biblioteki do serializacji
	* biblioteki upraszczające ręczne tworzenie warstwy pośredniej (embedded SQL)
	* biblioteki mapowania relacyjno-obiektowego (ORM)

### Embedded SQL
* Przykład - biblioteka SOCI
* Mechanizm kursora

### Serializacja
* Dane binarne
	* zależne od architektury
	* problem z big-endian, little-endian
	* mniejsze narzuty
* Napis
* JSON
* XML
* Biblioteka Boost.Serialization
	* poprawna obsługa wskaźników, kolekcji standardowych
* Google protocol buffers
