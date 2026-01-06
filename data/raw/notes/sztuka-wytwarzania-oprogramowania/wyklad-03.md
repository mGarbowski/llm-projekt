# Obiektowe wzorce projektowe (2024-03-04)
* Wzorce to poprawne, standardowe rozwiązania typowych problemów

## Agregacja i dziedziczenie
* Agregacja - kolekcja obiektów jako składowa
* Kompozycja - obiekt jako składowa
* Dziedziczenie - klasa pochodna i klasa bazowa

## Problem wycinania
```cpp
Kierownik k(...);
Pracownik p = k;
```

* Zostanie wywołany konstruktor kopiujący
* Jest błędem logicznym, powoduje niespodzianki
* Należy przekazywać wskaźniki lub referencje do obiektów
* Mozna zabronić tworzyć obiektów klasy bazowej (klasa abstrakcyjna / prywatny konstruktor)

## Płytka kopia
```cpp
Obj *obj = new Obj();
Obj *copy = obj;
```

* Przy adresowaniu pośrednim (przez wskaźnik)
* Można skopiować sam wskaźnik
    * Szybkie, bo wskaźnik to jedna zmienna
    * Wskaźnik wskazuje na ten sam obiekt
    * Poprawne jeśli używamy obiektu do odczytu

## Kopia głęboka
```cpp
Obj *obj = new Obj();
Obj *copy = new Obj(*obj);
```

## Kopia z hierarchią dziedziczenia
Można przeciążyć metody w klasach pochodnych.
Wołając metodę kopiująca na wskaźniku klasy bazowej zostanie wywołana odpowiednia implementacja w klasie pochodnej.
Wzorzec prototypu.


Importy, dołączanie przestrzeni nazw powinno być maksymalnie lokalne

## Prototyp
* Odpowiedzialność przeniesiona na obiekty pochodne

## Kompozyt
* Reprezentacja drzewiastych struktur obiektów
* Traktowanie w ten sam sposób obiektów prostych i złożonych
* Łatwo dodawać nowe klasy do hierarchii
* Przykład plików i katalogów w systemie plików
* dyskusyjne jak powinny działać add i remove i czy powinny być w bazowym interfejsie


## Adapter
* Wrapper
* Rozwiązuje problem, gdzie klasa ma odpowiednie dane ale ma nieodpowiedni interfejs
* Nie zawsze można zmienić interfejs klasy która nie pasuje
* Adapter obiektów wykorzystuje agregację (preferowany)
    * obiekt adaptowany jest składową adaptera
    * jego metody są wołane przez adapter
* Adapter klas wtykorzystuje dziedziczenie prywatne
    * Adapter dziedziczy publicznie po interfejsie i prywatnie po adaptowanym
    * Można nadpisywać metody wirtualne adaptowanego

## Proxy
* Pośrednik
* Proxy to uchwyt (wskaźnik) do obiektu
* Sprytny wskaźnik to przykład proxy
* Proxy agreguje jeden obiekt rzeczywisty (trzyma wskaźnik)
* Proxy ma ten sam interfejs co obiekt rzeczywisty
* Przykłady
    * Virtual Proxy
    * Copy-On-Write Proxy - odkłada tworzenie głębokiej kopii obiektu
    * Smart Pointer - zarządza czasem życia obiektu na stercie
    * Remote Proxy - obiekt w innej przestrzeni adresowej
    * Protection Proxy - kontroluje prawa dostępu do obiektu
    * Synchronization Proxy - synchronizuje dostęp do obiektu

### Virtual Proxy
* Tworzy obiekt przy pierwszym użyciu, odracza tworzenie obiektu
* Utworzenie obiektu jeszcze nie oznacza zajęcia zasobów
* Większy koszt - dwa skoki
* Np. drzewo gry - można reprezentować strukturę niemieszczącą się w pamięci

### Copy-On-Write Proxy
* Leniwe kopiowanie
* Przy odczycie kopia płytka
* Przy zapisie kopia głęboka
* Przechowuje licznik referencji
    * Jeśli jeden to można modyfikować
    * Jeśli więcej to można czytać albo trzeba utworzyć głęboką kopię

## Obserwator
* Rozwiązuje problem, gdzie zmiana stanu jednego obiektu wymaga zmiany innych
* Naiwna implementacja prowadzi do cyklicznych zależności
* Aktywne oczekiwanie jest błędne (błąd projektowy), są niepotrzebne wywołania
* Obserwator nie ma ani cyklicznych zależności ani aktywnego oczekiwania
* Obiekt posiadający stan agreguje obserwatory
* Konkretne obserwatory mają metodę wirtualną `update`
* Wysłanie powiadomienia przez temat obserwacji woła `update` na każdym z zarejestrowanych obserwatorów
* Obserwator zależy od tematu, ale temat nie zależy od obserwatora
* Przykłady
    * MVC - model to temat, widok to obserwator
    * Qt - sygnał to temat, slot ot obserwator

## Komenda
* Wzorzec opóźnionego wołania
* Obiekt przechowuje akcję i parametry
* Pozwala zdefiniować komendę w jednym miejscu i wykonać w innym
* W C++ używa się do tego operatora wołania funkcyjnego `operator()(...)`
* Jest semantycznie wartością
    * Można kopiować
    * Można przechować w kolekcji
    * Można zwracać jako wynik
    * Można przekazać jako argument
* Można dostarczyć możliwość wycofywania komendy
    * funkcja odwrotna
    * zapamiętanie stanu i przywracanie
* Mozna wykorzystać do przetwarzania równoległego
* Zawiera wszystkie informacje potzrebne do wykonania akcji

```cpp
window.resize(0, 0, 200, 300);
```

```cpp
Command *cmd = new ResizeCommand(window, &Window::resize, 0, 0, 200, 300);
/* ... */
cmd->run();
```

## Dekorator
* Zmiana funkcjonalności dla obiektów w czasie działania
* Alternatywa dla dziedziczenia (inna funkcjonalność w czasie kompilacji)
* Powstaje łańcuch obiektów
* Jak odczyt z plików z buforowaniem w Java
