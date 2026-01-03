# STL, funkcje anonimowe (ZPR- W11 -2020 12 15)

## STL
* Część standardu C++
* Skład
	* kontenery
	* iteratory
	* algorytmy
	* funktory
	* adaptery
	* alokatory
* Bardzo efektywna, bez narzutów czasu wykonania
* Algorytmy korzystają ze wzorca iteratora
* Bezpieczna w aplikacjach współbieżnych

## Kontenery

### Sekwencyjne
* basic_string - jednowymiarowa dablica
	* może stosować wzorzec copy-on-write
* vector - jednowymiarowa tablica
* list - lista dwukierunkowa
* deque - kolejka o dwu końcach
* Ma sens indeks i arytmetyka adresowa

### Asocjacyjne
* set
* map
* multiset
* multimap

### Haszujące
* Kolejność nieznana programiście
* unordered_set
* unordered_map
* unordered_multiset
* unordered_multimap

### Adaptery
* Szablony ograniczające interfejs
* queue
* priority_queue
* stack
* Wykorzystują inny kontener do implementacji, np. deque

### Bazujące na tablicach
* vector
* basic_string
* deque

### Bazujące na węzłach
* Każdy element przechowywany w oddzielnym bloku
* Więcej informacji sterujących
* Iterator jest ważny dopóki element nie zostanie usunięty
* list
* set
* map
* ...

## Kopiowanie
* Biblioteka STL operuje na kopiach
	* kontener przechowuje kopie elementów
* Obiekt przechowywany w kontenerze 
	* powinien mieć publiczny konstruktor kopiujący
	* powinien mieć publiczny operator przypisania
* Problemy
	* obiekty bazowe dla hierarchii klas (wycinanie)
	* auto_ptr - nietypowe kopiowanie
* Gdy kopiowanie jes kosztowne
	* przechowuje isę w kontenerze wskaźniki na obiekty na stercie
	* kontener sprytnych wskaźników ze zliczaniem (shared_ptr)

## vector
* Dynamiczna tablica
* Przechowuje elementy w spójnym obszarze pamięci
	* mały narzut pamięciowy w porównaniu z tablicą
* size i capacity
	* wstawienie elmentu gdy `size==capacity` jest kozstowne - wymaga kopiowania całości
	* zazwyczaj capacity zwiększane x2
* Metoda `at`
	* jak `operator[]`, ale bada zakres
* `operator==`
	* taka sama liczba elementów i porównanie wszystkich elementów
* `operator<`
	* jak porównywanie napisów
* Specjalizacja dla `vecotr<bool>`
	* upakowuje na pojedynczych bitach

## list
* Lista dwukierunkowa
* Większe narzuty pamięciowe niż w wektorze
	* każdy blok przechowuje wskaźnik na następny i poprzedni element
* Element nie ma indeksu, nie ma operatora `[]`
* Metoda `reverse`
* Scalenie, sortowanie

## deque
* Kolejka o dwóch końcach
* Oparta o tablicę
* Elementy nie muszą być przechowywane w pojedynczym bloku
* Wiele bloków, wielkość zależna od architektury
* Metody jak dla `vector`
* Wygodne wstawianie i usuwanie na początek i koniec

## basic_string
* Jak vector
* Stosuje optymalizację ze wzorcem copy-on-write

## Kontenery asocjacyjne
* Przechowują elementy uporządkowane
* Dostarczają metod wyszukiwania w czasie logarytmicznym
* Drzewo czerwono-czarne
* Inny porządek elementów niż kolejność wstawiania
	* kolejność rosnąca
* Element musi mieć `operator<`
	* ewentualnie funkcja porównująca
* Oparty o węzły
* Iterator typu `bidirectional`

### set
* Zbiór elementów
	* bez powtórzeń
	* nie wymaga operatora `==` (`!(a < b) && !(b < a)`)

### map
* Słownik, tablica asocjacyjna
* Klucz, wartość
	* eliminuje identyczne klucze
* Elementy w porządku klucza

### multiset
* Jak set, ale nie eliminuje elementów równoważnych
* Elementy sortowane w kolejności rosnącej

### multimap
* Analogicznie może być wiele razy ten sam klucz

## Kontenery oparte o funkcję skrótu
* Dostęp w czasie jednostkowym
* Działa wydajnie, gdy jest wypełniony w ok. 25%
	* zużycie pamięci
* W funkcji skrótu mogą występować konflikty

## `std::array`
* Adapter to tablicy z C
* Dostarcza iteratorów
* Metody at, front, back, itp.
* Operatory `==`, `<`

## STL i wielowątkowość
* Bezpieczne czytanie
	* wiele wątków może jednocześnie czytać z kontenera
* Bezpieczne pisanie do różnych kontenerów
	* różne wątki mogą równocześnie pisać do różnych kontenerów
* Przy współdzielonych obiektach programista zapewnia mechanizmy synchronizacji
* Uwaga na `std::string` w bardzo starych kompilatorach
	* problem wynikający z copy-on-write
	* we współczesnych wersjach biblioteki to jest zaimplementowane poprawnie


## Algorytmy
* `for_each`
* Nie modyfikują kolekcji
	* find, find_if, adjacent_find ...
* Modyfikują kolekcję
	* copy, copy_n, sortujące, kopiec
* Poprawne użycie biblioteki standardowej nie wymaga użycia pętli
* Na niektórych platformach mogą wykonywać się równolegle

### Zakres
* Algorytmu jako wejście przyjmują zakres
* Zakres to para iteratorów
* `begin()` - iterator do pierwszego elementu
* `end()` - iterator do pierwszego za ostatnim
* `rbegin()`, `rend()` - w odwrotnej kolejności (reverse_iterator)
* Pusty zakres kiedy iteratory są sobie równe

### Wykorzystanie algorytmów
* Najlepiej stosować najbardziej specjalizowany algorytm bo może zawierać więcej optymalizacji
* for_each zamiast pętli
* Funktory, funkcje anonimowe

### Wyszukiwanie
* Przeszukiwanie liniowe (nieposortowane elementy)
	* count (int) - czy istnieje element, ile kopii
	* find (iterator) - czy istnieje element i gdzie się znajduje
* Przeszukiwanie binarne (posortowane elementy)
	* sensowne tylko dla kontenerów typu random access (vector, deque, string)
	* binary_search (bool) - czy istnieje element
	* lower_bound (iterator) - pierwszy o danej wartości
	* upper_bound (iterator) - pierwszy za ostatnim o danej wartości
	* equal_range (para iteratorów) - zakres
	* zamiast count - policzyć różnicę z iteratorów z equal_range

### Usuwanie (remove)
* Algorytm nie zna wewnętrznej budowy kontenera
* Tak naprawdę nie usuwa, tylko przenosi elementy na koniec i zwraca iterator na pierwszy element *do usunięcia*
* Typowo używa się w połączeniu z `erase`
	* `v.erase(remove(v.begin(), v.end(), 3), v.end())`
* Niebezpieczny dla kontenerów zawierających wskaźniki
	* nie należy przechowywać gołych wskaźników w kontenerach

### Sortowanie
* partition
	* elementy spełniające warunek na początku, reszta na końcu
* nth_element
	* znajduje pozycję wskazanego elementu
	* wcześniej są mniejsze elementy, potem są większe
* partial_sort
	* sortuje od begin to wskazanego elementu
	* w końcowej części są większe elementy ale nieposortowane
* sort
	* standardowe sortowanie
* stable_sort
	* zachowuje porządek dla równoważnych elementów

## Funkcje anonimowe

### `std::bind`
* Od C++03
* Funkcja której chcemy użyć już istnieje ale ma nie taki interfejs
* Wstawia w miejsce argumentów stałe lub zmienia kolejność
* `std::placeholders`
	* `_1`, `_2`
	* do przekazania dalej argumentu 
* Taka sama składnia dla obiektu, wskaźnika i sprytnego wskaźnika
* Przy przekazaniu metody trzeba jawnie związać obiekt użyty jako `this`
* Można zagnieżdżać `bind` (kompozycja funkcji)

### `std::ref`
* Standardowo algorytmy robią kopie elementów
* Do przekazania referencji `std::ref`
* Do const referencji `std::cref`

### lambda
* Od C++11
* Można użyć zamiast `std::bind`, bez różnicy wydajności
* `[]() -> T { }`
	* funkcja anonimowa zwracająca obiekt typu `T`
* Wygodne do użycia z algorytmami
* Lista przechwytywana
	* które nazwy są wspólna dla kodu wewnątrz funkcji anonimowej
	* `[x]` - obiekt o nazwie x tylko do odczytu
	* `[&x]` - obiekt o nazwie x do zapisu i odczytu przekazany przez referencję
	* `[=]` - dowolny obiekt do odczytu
	* `[&]` - dowolny obiekt przekazywany przez referencję (zpais i odczyt)