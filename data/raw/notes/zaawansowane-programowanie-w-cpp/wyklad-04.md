# ZPR- W05 -2020 11 03 Obsługa wyjątków i sprytne wskaźniki

## Mechanizm wyjątków
* Mechanizm niesekwencyjnego przekazania sterowania
* Autor biblioteki może wykryć błąd, ale nie wie co z nim zrobić
* Użytkownik wie co zrobić z błędem, nie potrafi go wykryć
* Warstwa systemowa i warstwa aplikacji
* Błędy zewnętrzne i błędy wewnętrzne
	* zewnętrzne - np. brak pamięci
	* wewnętrzne nieprawidłowy stan aplikacji, np. dzielenie przez 0
* Nieprawidłowe mechanizmy
	* ignorowanie błędów
	* kończenie działania programu
	* komunikaty dla użytkownika
* Kłopotliwe mechanizmy
	* kod powrotu - wymieszanie logiki z obsługą błędów
	* zmienna globalna - problem ze współbieżnością
	* specjalny stan obiektu - np. NaN w standardzie dla liczb rzeczywistych, nie dla każdego typu daje się zdefiniować (dla liczb całkowitych)
	* ANSI: longjmp - struktura pamięta stan rejestrów procesora, można załadować ją do procesora, nie używa zmiennej globalnej, błąd opisuje liczba całkowita, nie zwalnia zasobów
* Mechanizm wyjątków nie ma wad wszystkich wymienionych wcześniej
* Wyjątek jest obiektem dowolnego typu
	* zwyczajowo powinny dziedziczyć po `std::exception`
	* moga mieć składowe
* Środowisko zapewnia zwalnianie obiektów automatycznych
	* będą wywołane destruktory
* Nie ma zarezerwowanej wartości zwracanej
* Bez obiektów globalnych
* Oddziela kod obsługi błędu od innego kodu
* Użytkownik nie może zignorować zgłoszonego błędu
* Wymaga wsparcia przez język
	* można wyłączyć w kompilatorze
	* łańcuch skoków po końcach bloków
* Jest znacznie wolniejszy niż zwykły powrót z funkcji
	* zwijanie stosu
	* tak samo wolny jak `dynamic_cast`
* Klasa wyjątku to inny typ niż klasa-wartość i klasa w hierarchii
	* powinny dziedziczyć po `std::exception`
	* konstruktor nie może zgłaszać wyjątków
	* tworzone w specjalnym miejscu podczas zgłaszania wyjątków
	* często implementują wzorzec wizytatora
	* mogą tworzyć głębokie hierarchie
* Można opisać listę zgłaszanych wyjątków przez funkcję
	* nie używa się tego
* Ok. 100 razy wolniejszy
	* zakładamy że sytuacje błędne nie zdarzają się aż tak często
	* zależy nam na poprawności

### Zasady stosowania
* Hierarchie klas
	* pozwalają grupować podobne błędy
* Nie należy rzucać wyjątków z destruktorach
* Należy rzucać wyjątek przez wartość `throw Exception`
	* nie zajmujemy miejsca na stercie
* Wyjątek przechwytywać przez referencję
	* `catch(Exception& e)`
	* nie tworzymy lokalnej kopii
* Należy reagować na wszystkie wyjątki
	* w przeciwnym wypadku aplikacja się kończy
	* należy przynajmniej wypisać komunikat jeśli nie da się go obsłużyć

## Mechanizm wyjątków a zasoby
```cpp
void f1() {
	int* tmp = new int;
	// Kod może rzucić wyjątek
	delete tmp;
}
```

* Rzucenie wyjątku spowoduje wyciek pamięci
* Łapanie wyjątku żeby zwolnić zasoby - niewydajne
* Poprawne zabezpieczenie - użycie sprytnego wskaźnika

## `boost::scoped_ptr`
* usunięty konstruktor kopiujący i operator przypisania
* Wielkość normalnego wskaźnika
* Poprawnie obsłuży zwolnienie zasobów przy rzuconym wyjątku
* Jeden obiekt jest właścicielem obiektu na stercie

## `std::auto_ptr`
* Jeden obiekt jest właścicielem obiektu na stercie
* Wielkość normalnego wskaźnika
* Niezalecane
* Dozwolone kopiowanie - przenosi uprawnienia
	* modyfikuje prawą stronę operatora `=`
* Niebezpieczny do przekazywania jako argumentu
	* przekazanie przez wartość modyfikuje oryginalny obiekt
* Niebezpieczny do przechowywania w kolekcji
	* na nic nie wskazują
	* po pobraniu wartości niczego w nim nie ma

## r-value
* Od C++11
* Pozwala odróżnić obiekty tymczasowe
* Konstruktor przenoszący i przenoszący operator przypisania
	* `Foo(Foo&& f)` - obiekt `f` będzie pusty

## `std::unique_ptr`
* Wielkość zwykłego wskaźnika
* Zastępuje `std::auto_ptr`
* Mogą być przechowywane w kontenerach standardowych
* Automatycznie usuwają obiekt w destruktorze
* Jedyny właściciel obiektu na stercie
* Funkcja `std::move` przenosi własność ze wskaźnika
* Kopiowanie jest zabronione
* Należy używać zawsze do zarządzania zasobami, tam gdzie mogą wystąpić wyjątki
* Warto tak implementować składowe klas
	* rozwiązuje problem z częścią zainicjowanych składowych, kiedy wystąpi wyjątek w konstruktorze

## Rule of three, rule of five
* Dla klasy z niebanalnymi składowymi należy dostarczyć
	* destruktor
	* konstruktor kopiujący
	* operator przypisania
	* konstruktor przenoszący
	* przenoszący operator przypisania

## `std::shared_ptr`
* Do współdzielonych obiektów
* Płytkie kopie
* Poza obiektem przechowuje licznik
* Dozwolone kopiowanie i przypisanie
	* zwiększa licznik o 1
* Destruktor zmniejsza licznik
	* jeśli spadnie do 0 to usuwa obiekt
* Działa poprawnie w aplikacjach współbieżnych
* Trudno znaleźć powód żeby nie używać sprytnych wskaźników
	* chyba że kto inny zarządza czasem życia obiektu
* Problem z cyklicznymi zależnościami między obiektami
	* obiekt wskazuje sam na siebie

### Jawne przerywanie zależności cyklicznej
* Destruktor listy cyklicznej wywołuje `reset()`

### `std::weak_ptr`
* Uzupełnienie `std::shared_ptr`
* Nie zwiększa licznika odniesień
* Rozwiązuje problem z cykliczną zależnością
* Może pokazywać na zniszczony obiekt
	* metoda `expired` - trzeba sprawdzić czy dalej istnieje
* Można zamienić na `shared_ptr` wołają metodę `lock()`
* Obiekt może wskazywać sam na siebie przez słaby wskaźnik
	* używa semantyki sprytnych wskaźników

## Błędne użycia sprytnego wskaźnika
* Nie należy inicjować wielu sprytnych wskaźników tym samym zwykłym wskaźnikiem

## Funkcja fabryczna `make_shared` i `allocate_shared`
* Unikamy wołania operatora `new`
	* symetryczny zapis
* Od razu alokuje pamięć na licznik
	* problem alokacji małych obiektów
* `allocate_shared` - używa dostarczonego alokatora

## `boost::intrusive_ptr`
* Programista implementuje licznik przechowywany w obiekcie

## Tworzenie sprytnego wskaźnika na podstawie `this`
* Wzorzec RTCP
	* typ dziedziczy po szablonie którego parametrem jest on sam
* `boost::shared_from_this'
	* zamiast trzymania składowej `me`

## Rule of zero
* Zarządzanie zasobami tylko przez sprytne wskaźniki
* Domyślne konstruktor kopiujący i operator przypisania zachowują się poprawnie
	* zachowanie określa wykorzystany typ sprytnego wskaźnika