# ZPR- W04 -2020 10 27

## Zarządzanie pamięcią
* `Foo* f = new Foo;`
	* przydziela pamięć, woła konstruktor
	* generuje `bad_alloc` jeżeli brak pamięci
* `delete f;`
	* woła destruktor
	* zwalnia pamięć
* `Foo* f = new Foo[N]`
	* przydziela pamięć dla N elementów
	* woła konstruktory
* `delete [] f;`
	* woła destruktory
	* zwalnia pamięć
* `Foo* f = new (std::nothrow) Foo;`
	* zwraca 0 jeżeli brak pamięci
	* nie ma wyjątku `bad_alloc` ale konstruktor może rzucić wyjątek

## Pusty wskaźnik
* Prawidłowe oznaczenie pustego wskaźnika to `nullptr`
	* rzutowany na dowolny wskaźnik
* Niepoprawne ale używane przed dodaniem słowa kluczowego do standardu
	* `#define NULL (void*)0`
	* `0L`

## Obsługa błędu przydziału pamięci
```cpp
#include <new>

void MyNewHandler() { ... }
set_new_handler(MyNewHandler);  // ustawienie funkcji obsługi
set_new_handler(nullptr);       // usunięcie funkcji obsługi
```

## Definicja własnego operatora `new` i `delete`
* Można przeciążyć globalny lub dla klasy (i jej pochodnych)
	* można badać wycieki
* Bardzo trudne do implementacji

### Small object allocator
* Przydział pamięci standardowym alokatorem wiąże się z narzutem
	* w pamięci dynamicznej poza samym obiektem są przechowywane informacje pomocnicze
	* przy dużej liczbie małych obiektów narzut robi się istotny
* Alokator jest parametrem szablonu kolekcji
* Alokator obiektów o ustalonym rozmiarze
	* nie trzeba trzymać rozmiaru przydzielonego bloku
	* wystarczy informacja dla zestawu bloków, (wskaźnik na blok wolny)
	* nie ma fragmentacji pamięci
* Wspierane przez `Boost.Pool`
* W językach obiektowych to częsty problem, obiekty z hierarchii klas są tworzone na stercie

## Podwójna rola wskaźników
* Wskaźnik jest identyifkatorem obiektu
	* rzutowanie w górę hierarchii dziedziczenia
* Wskaźnik jest iteratorem dla tablicy
	* arytmetyka wskaźników
* Nie należy mieszać tych dwóch
	* problem z arytmetyką jeśli obiekt klasy pochodnej jest innego rozmiaru niż obiekt klasy bazowej

## Ukrywanie nazw
* Nazwa lokalna przykrywa globalne
* Podobnie przy dziedziczeniu
	* można wykorzystać nazwę składowej po raz drugi w klasie pochodnej
	* problematyczne zachowanie z przeciążaniem nazw w hierarchii klas

## Dynamiczna informacja o typie (RTTI)
* Mechanizm można wyłączyć w kompilatorze
* Dla każdego typu można pobrać strukturę `type_info`
	* drzewo (dla dziedziczenia wielobazowego) lub lista
* Operator `typeid`
* Można badać przynależność do typu
	* pozwala implementować rzutowanie w dół hierarchii klas
	* rzutowanie skrośne do klasy siostrzanej przy dziedziczeniu wielobazowym 
* `dynamic_cast` bada `type_info`
	* kosztowny ze względu na przeszukiwanie drzewa/listy
	* bezpieczny pod kątem typów - korzysta z informacji przechowywanych przez kompilator
* Koszty
	* wielkość kodu - struktury `type_info` dla wszystkich klas
	* większa tablica funkcji wirtualnych, wskaźnik do `type_info`
* Czas wykonania
	* wołanie `typeid` - czas jednostkowy
	* wołanie `dynamic_cast` - rekurencyjne przeszukanie referencji do `type_info` klas bazowych
	* badanie typu w `catch` jest tak samo wydajne jak `dynamic_cast`

## Wyrażenia stałe
* `constexpr`
* Można używać jako stałe jeśli zależą tylko od stałych argumentów

## Wyliczenia bezpieczne ze względu na typ
* `enum class`
* Nie można ich rzutować na `int` ani na odwrót
* Symbole w przestrzeni nazwy wyliczenia

## Wzorce projektowe

### Komenda
* Odroczone wykonanie operacji
* Przechowuje czynność jako obiekt
	* przechowuje parametry wykonania
* Konwencja w C++ - użycie operatora wołania funkcyjnego
* Rozdzielone definiowanie operacji od wykonania
	* wygodne do bibliotek GUI
	* mniej zależności między częściami
	* można rozdzielić kod definiujący akcje i uruchamiający
* Komenda ma semantykę wartości
	* kopiowanie
	* zwracanie jako wynik
	* dastarczanie jako argument
	* przechowywanie w kolekcjach
* Możliwość wycofania
	* implementacja odwrotnej funkcji
	* zapamiętanie stanu i odtwarzanie
* Można wykorzystać do przetwarzania równoległego

### Obserwator
* Zmiana stanu jednego obiektu wymaga zmiany innych
* Wołanie metod na obiektach wprowadziłoby zależności cykliczne
* Aktywne oczekiwanie - niepoprawne rozwiązanie w przeważającej większości przypadków
	* zaleta - nie ma zależności cyklicznej
	* wiele niepotrzebnych wywołań inicjowanych zegarem
* Klasa bazowa `Observer`
	* metoda wirtualna `update`
* Klasy obserwujące zmiany dziedziczą po `Observer`
	* konkretne obserwatory
	* zależą od tematów obserwacji
* Tematy obserwacji
	* zależą od obserwatora bazowego
	* `add`, `delete`, `notify`, `getState`
	* powiadamia każdy obserwator przechowywany w kolekcji (dla każdego woła `update`)
* Implementując wzorzec można wprowadzić wspólną klasę bazową dla tematów obserwacji
* Nie ma cyklicznych zależności
* Często spotykany w praktyce
	* MVC - Model = Subject, View = Observer
	* Sygnały (Subject) i Sloty (Observer)

### Iterator
* Pozwala jednakowo traktować różne kolecje
	* które są wystarczająco podobne (np. obie jednowymiarowe wektor i lista dwukierunkowa)
* Dostarczone w STL dla standardowych kolekcji
* Forward iterator
	* dereferencja - dostęp do elementu
	* inkrementacji - wskazuje następny element
* Pozwalają na dostarczenie jednego algorytmu dla wielu różnych kolekcji

### Most
* Oddzielenie abstrakcji od implementacji
* Dwie hierarchie klas
* Wzorzec pimpl - zdegenerowany most
	* uchwyt do implementacji
	* minimalizuje zależności
	* ukrywa zależności
	* w nagłówku są tylko zależności interfejsu
	* pośrednie wołanie przez uchwyt
* Wstrzykiwanie zależności
	* Boost.DI
	* wygodne do testowania jednostkowego

### Fabryki
* C++ ma statyczną kontrolę typów
* Polimorfizm nie jest dostępny podczas inicjacji
	* wołanie funkcji wirtualnej tylko na zainicjowanym obiekcie
	* nie ma wirtualnych konstruktorów
* Czasami chcemy stworzyć obiekt na podstawie informacji podanej dynamicznie
* Prosta fabryka
	* switch case zależny od wszystkich klas w hierarchii
	* wiązanie między identyfikatorem a tworzonym typem zapewnia programista
	* problem przy dodawaniu nowych klas
* Fabryka skalowalna
	* nie ma zależności od wszystkich typów
	* typ jest zależny od fabryki
	* dostarcza się funkcji tworzących
	* fabryka przechowuje kolekcję funkcji tworzących
	* typ rejestruje się w fabryce dostarczając funkcję tworzącą
	* jest problem z identyfikatorami (zależność jest ukryta), może być kolizja
	* można generować identyfikator przy rejestracji albo wykorzystać `type_id`, kod może nie być przenośny
* Fabryka prototypów
	* jak fabryka skalowalna ale przechowuje kolekcję obiektów prototypów
	* przy tworzeniu nowego obiektu, prototyp jest klonowany
	* można mieć wiele obiektów tego samego typu
	* zajmuje więcej pamięci
* Fabryka abstrakcyjna
	* do tworzenia grupy powiązanych ze sobą obiektów
	* fabryka konkretna tworzy obiekty konkretne
* Singleton
	* singleton jest fabryką pojedynczego obiektu
* Tworzenie obiektów gdy mamy informację o typie - fabryka
* Tworzenie kopii obiektów - prototyp
* Tworzenie rodzin - fabryka abstrakcyjna