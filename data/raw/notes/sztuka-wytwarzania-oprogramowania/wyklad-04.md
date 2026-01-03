# Obiektowe wzorce projektowe (2024-03-11)

## Fasada
* Pojedyncza klasa ukrywa cały złożony podsystem
* Upraszcza korzystanie z podsystemu
* Umożliwia wymienność podsystemu


## Fabryka
* Nie można stworzyć nowej klasy w trakcie działania programu
* Inicjacja wymaga podania konkretnego typu
* Typ musi być znany w momencie kompilacji

### Prosta fabryka obiektów (niepoprawne)
* Duże switch..case w klasie bazowej gdzie wołane są konstruktory klas pochodnych
    * Zależy od wszystkich klas pochodnych
    * Niewydajne
    * Nie ma kontorli kompilatora

### Fabryka skalowalna
* Odwraca zależność
    * Nie jest zależna od wszystkich klas konkrentych
    * Wszystkie klasy konkretne są zależne od fabryki
* Zapewnia kontrolę
* Każda klasa konkretna implementuje funkcję fabryczna (tworzącą obiekt)
* Fabryka utrzymuje kolekcję funkcji fabrycznych (np. mapę)
* Fabryka może rejestrować nowe funkcje fabryczne
* Wymaga poprawnego posługiwania się identyfikatorem
* Rejestracja w czasie działania (np. na początku działania aplikacji)
* Problem z identyfikatorem
    * można użyć RTTI (struktura `type_id`)
    * generowanie identyfikatorów
    * może być enum ale to też rodzi problemy (zależny od wszystkich klas konkretnych)


### Fabryka prototypów
* Trochę jak fabryka skalowalna
* Ale nie trzyma kolekcji funkcji tworzących, tylko obiekty (prototypy), na wywołuje `clone()`
* Zajmuje więcej zasobów - przechowuje cały obiekt


### Fabryka abstrakcyjna
* Do tworzenia obiektów w wielopoziomowej hierarchii klas
* Fabryka abstrakcyjna zwraca uchwyt na klasę wyżej w hierarchii
* Fabryka konkretna zwraca uchwyt na konkretne klasy

## Singleton
* Tylko jeden obiekt danego typu
* Zastępuje obiekty globalne
* Obiekty globalne są błędem, singleton też może być błędem
* Jedna metoda `getInstance`
    * Jeśli już jest stworzony to zwraca zapamietaną instancję
    * Jeśli nie to tworzy i zapamiętuje
* Prywatny konstruktor, usunięte standardowy konstruktor kopiujący itd
* Możliwy do utworzenia tylko przez `getInstance`
* Kolejność inicjacji obiektów globalnych jest losowa - nie mogą się wołać nawzajem
    * niezdefiniowane zahchowanie
    * singleton nie ma tego problemu - to zapewnia dostęp do obiektu przez `getInstance`
* Wolniejsze odwołanie, bo przy każdym dostępie do instancji jest sprawdzany warunek


## Wizytator
* Dodanie nowej klasy do hierarchii jest proste
* Dodanie nowej funkcjonalności - złożone
    * wymaga zmieniania wielu plików w projekcie
    * częściej dodaje się funkcjonalność niż typy
* Kiedy jest ustalona hierarchia klas i wiele metod, które mogą się zmieniać
* Gorsze / niepoprawne rozwiązanie
    * Klasy konkretne muszą mieć nadpisane metody, które wołają metody na oddzielnym obiekcie
    * Cała funkcjonalność w nowej klasie, sprawdzanie typów (dynamic cast)
* Tworzy się dodatkową hierarchię klas wizytatorów
* Hierarchia wizytatorów jest zależna od hierarchii klas elementów wizytowanych
* Każda kolejna funkcjonalność dziedziczy po bazowym wizytorze i logika zawiera się w 1 klasie
* Bazowy Element (wizytowany) ma metodę accept przyjmującą bazowy wizytator
    * nie trzeba w żaden inny sposób jej zmieniać żeby dodać funkcjonalności
    * accept woła metodę wizytatora na `this`
    * typ rozstrzyga się bez żadnego dynamic cast
    * zamiast tego są 2 wywołania metod wirtualnych
* Zależności są tylko lokalne
* accept musi być czysto wirtualny w bazowym elemencie


## Wielometoda
* Kiedy jest zależność od dwóch typów
* Korzystamy z wizytatora
* Złe rozwiązania
    * if, else i dynamic cast na wszystkie kombinacje
    * dwywymiarowa tablica wskaźników na odpowiednie metody
* Jeden wizytator rozsztrzyga o jednym elemencie, a drugi o drugim


## Most
* Separuje abstrakcję od implementacji

### pimpl
* Zdegenerowany most
* Mniej zależności w headerze
* Prywatna klasa implementowana w pliku cpp, jest łatwo wymienialna
* Zawsze pośredni dostęp przez uchwyt
* Pointer do implementacji

### Wstrzykiwanie zależności
* Obiekt, który będzie składową dostarczany przez konstruktor
* Można np. na potrzeby testów dostarczyć inny obiekt (wymienić implementację)
