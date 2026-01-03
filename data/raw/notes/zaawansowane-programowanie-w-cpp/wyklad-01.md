# # ZPR- W02 -2020 10 13

## Dopuszczalne użycie preprocesora
* `#include`
* Zabezpieczenie przed wielokrotnym dołączeniem nagłówka
* Warunkowa kompilacja
	* tylko w wyjątkowych sytuacjach
	* należy pisać kod który jest przenośny i jej nie wymaga

### Błędne użycie `#define`
* Nie rozumie języka
* Nie wiadomo w jakiej kolejności będą kompilowane pliki
* Należy stosować normalne stałe
	* `const int MAX = 10;`
	* stałe statyczne w klasie
* Należy stosować szablony funkcji
	* rozumieją składnię języka

Stałe globalne nie są wąskim gardłem dla programu bo można je tylko odczytywać

## Stałość
* Informacja dla programisty
* Uproszczenie kodu (unikanie magicznych liczb)
* Pozwala kompilatorowi na optymalizacje
* `const int* p` - stała wartość wskazywana
* `int* const q` - stały wskaźnik
* `const int* const r` - stały wskaźnik i stała wartość wskazywana
* Czytanie od prawej do lewej
* Stałość jest częścią sygnatury metody
	* dwie wersje metody o tej samej nazwie
	* dla stałego obiektu nie można wywołać metody nie-const
* Przekazanie argumentu przez const-referencję pozwala zwiększyć wydajność
	* unika kopiowania dużych obiektów

### Stałość logiczna vs fizyczna
* Stałość logiczna - nie zmieniamy stanu obiektu
* Stałość fizyczna - brak zmiany składowych
* Kompilator bada stałość fizyczną
* Nie zawsze są tożsame
	* np. metoda const zwracająca wskaźnik
	* nie są zmienione składowe ale można zmienić stan jakiegoś obiektu przez wskaźnik
* Rozwiązanie
	* zwracanie stałego wskaźnika
	* użycie `mutable` składowych
* Oznaczenie składowych jako `mutable` oznacza że nie są stanem obiektu
	* można je modyfikować w const metodach

## Konwersja typów
* Nie używać rzutowania w stylu C
* Nie używa się `void*`
* Tylko `explicit` konstruktory
* Operatory rzutowania (unikać, tylko w ostateczności)

### `static_cast`
* Konwersja między spokrewnionymi typami

```cpp
double d = 3.2
int i - static_cast<int>(d);
```
Obcięcie części ułamkowej

### `dynamic_cast`
* Rzutowanie w dół hierarchii klas
* Kosztowny
	* wymaga przejrzenie tablicy typeid

### `const_cast`
* Zniesienie kwalifikatora `const`
* Przydatne jeśli chcemy użyć identycznej implementacji dla metod stałych i niestałych
* Przy serializacji obiektów (np. przesłanie przez sieć, składowe trzeba odtworzyć)

### `reinterpret_cast`
* Dowolna konwersja (tak jak w C)

## Tworzenie nowych klas
* Agregacja jest preferowana do dziedziczenia
* Agregacja - budowa całości z mniejszych kawałków
* Kompozycja - agregacja, gdy obiekt składowy nie może istnieć samodzielnie
* Agregacja jest wygodna bo nie wiąże interfejsów klas
* Dziedziczenie wprowadza powiązanie pomiędzy typami
	* relacja *może być traktowany jako*
	* `Kierownik` może być traktowany jako `Pracownik`

## Wycinanie
Dotyczy konstruktora kopiującego lub operatora przypisania

```cpp
class Pracownik { ... };
class Kierownik : public Pracownik { ... };

Kierownik k(...);
Pracownik p = k;
```

* Skopiowana zostanie tylko część klasy
* Źródło błędów
* Rozwiązanie
	* przekazywać wskaźniki lulb referencje

## Typy klas

### Klasa wartość (klasa autonomiczna)
* Brak metod wirtualnych
* Konstruktor, konstruktor kopiujący, operator przypisania, destruktor
* Najczęściej obiekt automatyczny lub składowa klasy
* Może być przekazywana przez wartość
* Obiekt traktowany jako jedna całość (np. data)

### Klasa bazowa dla hierarchii klas
* Używa metod wirtualnych
* Powinna mieć wirtualny destruktor
* Najlepiej jeśli jest abstrakcyjna albo ma prywatny konstruktor kopiujący i operator przypisania
	* zapobiega wycinaniu
* Najczęściej obiekt na stercie
* Przekazywana przez wskaźnik lub referencję
	* żeby uniknąć wycinania
* Problem z kopiowaniem
	* rozwiązanie przez zastosowanie wzorca Prototyp

## Kopiowanie obiektów

### Płytka kopia (shell copy)
```cpp
Obj* obj = new Obj();
Obj* copy = obj;
```

* Dwa wskaźniki do tego samego obiektu na stercie
* Zmiana obiektu zmienia też kopię

### Głęboka kopia (deep copy)
```cpp
Obj* obj = new Obj();
Obj* copy = new Obj(*obj);
```

* Kopia jest oddzielnym obiektem

### Wzorzec prorotypu
* Kopiowania obiektów w hierarchii klas
* Przeniesienie odpowiedzialności za kopiowanie na obiekty pochodne
* Wirtualna metoda clone

## Wzorzec kompozytu
* Do reprezentacji drzewiastych struktur obiektów
* Traktowanie w ten sam sposób obiektów prostych i złożonych

## Wzorzec proxy
* Kontroluje dostęp do obiektu (podobnie jak wskaźnik)
* Obiekt w innej przestrzeni adresowej - Remote Proxy
	* np. na innym komputerze
* Tworzenie obiektu przy pierwszym użyciu - Virtual Proxy
* Odkłada tworzenie kopii obiektu - Copy-On-Write Proxy
	* leniwe kopiowanie
	* na początku tworzona kopia płytka
	* utworzy kopię dopiero przy pierwszym wywołaniu nie-const metody
	* implementacja `std::string`
	* narzut pamięciowy na licznik odniesień
* Kontroluje prawa dostępu - Protection Proxy
* Synchronizuje dostęp do obiektu - Synchronization Proxy
* Niszczy obiekt na stercie - Smart Pointer
* Wada - metody rzeczywistego obiektu są wołane pośrednio (1 skok więcej)

## Wzorzec fasady
* Uproszczenie koszystania ze złożonego systemu
* Zapewnienie wymienności podsystemu
* Tylko jeśli korzystamy z systemu w sposób uproszczony