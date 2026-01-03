# # ZPR- W03 -2020 10 20

## Redefining
Brana jest implementacja metody z zadeklarowanego typu (argumentu) a nie rzeczywistego typu obiektu

To co innego niż nadpisanie w klasie pochodnej

## Polimorfizm z wykorzystaniem funkcji wirtualnych
* Dodanie składowej `virtual` do klasy
	* do obiektu będzie dodany wskaźnik do tablicy funkcji wirtualnych
* Wywołanie funkcji wirtualnej jest pośrednie
* Nadpisana metoda wirtualna jest umieszczona w tablicy funkcji wirtualnych
	* jedna tablica na typ
* Pozwala na tworzenie metod polimorficznych
	* różne w zależności od rzeczywistego typu obiektu
* Narzuty pamięciowe
	* wskaźnik w obiekcie `vtbl`
	* tablica wskaźników dla klas dostarczających funkcji wirtualnych
* Narzuty czasowe
	* dodatkowe adresowanie pośredni
	* wołanie metody przez pobranie adresu z tablicy i skok (zamiast samego skoku)

## Rodzaje metod
* Metoda
	* `void m()`
	* kod nie może być zmieniany w klasach pochodnych
* Metoda wirtualna 
	* `virtual void m()`
	* kod może ale nie musi być dostarczony w klasach pochodnych
	* domyślna implementacja w klasie bazowej
* Metoda czysto wirtualna
	* `virtual void m() = 0`
	* kod musi być dostarczony w klasach pochodnych

## NVI idiom
* Nie powinno być publicznych funkcji wirtualnych
	* poza destruktorem
* Publiczna metoda to część interfejsu
* Funkcje wirtualne to implementacja
	* informacja że fragmenty mogą być zmieniane w klasach pochodnych
* Nie powinno się mieszać interfejsu i implementacji
* Prywatną metodę wirtualną można nadpisać w klasie pochodnej

## Wskaźnik do funkcji
* Alternatywa do użycia funkcji wirtualnych
* Narzut na 1 wskaźnik dla każdej funkcji
* Zachowanie może być różne dla obiektów tej samej klasy
* Zachowanie można zmienić w trakcie działania
* Funkcja nie jest metodą, ma dostęp tylko do publicznego interfejsu klasy

## Dziedziczenie wielobazowe
* Multiple inheritance, MI
* Przejście od wskaźnika do klasy pochodnej na wskaźnik do klasy bazowej
	* przy pojedynczym dziedziczeniu to pusta operacja, adres jest ten sam
* Przy wielodziedziczeniu adres może się różnić
	* jest przesunięcie o stałą
	* składowe klas bazowych zaczynają się w różnych miejscach
	* któraś jest wcześniej

### Wielokrotne wystąpienie klasy bazowej
```cpp
class Base {};
class D1 : public Base {};
class D2 : public Base {};
class Multi : public D1, public D2 {};
```

* Obiekt klasy `Multi` zawiera dwa obiekty klasy `Base`
	* wprowadza niejednoznaczność
	* może być nieporządane ze względu na zasoby

### Dziedziczenie wirtualne
```cpp
class Base {};
class D1 : virtual public Base {};
class D2 : virtual public Base {};
class Multi : public D1, public D2 {};
```

* Tylko jedna instancja obiektu klasy bazowej będzie umieszczana w klasie pochodnej
* Obiekt klasy bazowej nie jest agregowany
* Obiekty `D1` i `D2` przechowują uchwyt do obiektu `Base`
* Dodatkowy poziom pośredniości przy wywołaniu
* Może być przydatne np. przy implementowaniu wzorca Dekoratora przez dziedziczenie

## Metody wirtualne a konstruktory
* Jest ustalona kolejność wołania konstruktorów i destruktorów
* Przy wołaniu konstruktora dla klasy pochodnej wołane są w kolejności
	* konstruktory klas dziedziczonych wirtualnie
	* konstruktory klas pochodnych
	* konstruktor klasy tworzonej
* Destruktory są wołane w odwrotnej kolejności
* Funkcje wirtualne nie działają w konstruktorach i destruktorach
	* obiekt nie został jeszcze zainicjowany
	* wołana jest metoda z klasy bazowej

## Dziedziczenie prywatne i chronione

```cpp
class D : public B {}
class D : protected B {}
class D : private B {}
```

| Rodzaj    | Dostęp do konwersji `D*` do `B*` | Dostęp do składowych publicznych `B` | Dostęp do składowych chronionych `B` |
| --------- | -------------------------------- | ------------------------------------ | ------------------------------------ |
| Publiczne | Wszystkie funkcje                | Wszystkie funkcje                    | metody `D` i klas pochodnych `D`     |
| Chronione | metody `D` i klas pochodnych `D` | metody `D` i klas pochodnych `D`     | metody `D` i klas pochodnych `D`     |
| Prywatne  | metody `D`                       | metody `D`                           | metody `D`                           |
## Wzorzec Adapter (wrapper)
* Mamy typ o odpowiedniej funkcjonalności ale złym interfejsie
* Nie zawsze można zmienić implementację
	* kod z biblioteki
	* zależności
* Adapter obiektów (agregacja)
	* preferowany sposób (prostszy)
	* narzut czasu przez pośrednie wywołanie
* Adapter klas (dziedziczenie wielobazowe)
	* pozwala nadpisywać metody
	* mniejszy narzut (bez pośrednich skoków)

## Wzorzec wizytatora
* Problem
	* dodawanie nowych klas do hierarchii jest proste
	* dodanie metod do interfejsu jest złożone
* Stosuje się gdy
	* jest ustalona hierarchia klas
	* wiele metod, metody mogą się zmieniać
* Unika się konieczności modyfikowania wszystkich klas w hierarchii przy dodawaniu nowej funkcjonalności
* Błędne rozwiązanie z wykorzystaniem `dynamic_cast`
* Dwukrotne zastosowanie funkcji wirtualnej
* Wizytator bazowy ma tyle metod ile typów w hierarchii odwiedzanej
* Każda klasa w hierarchii odwiedzanej musi mieć jedną metodę `accept(Visitor &v) { v.visit(*this); }`
	* tylko jedna zmiana
* Wizytator konkretny nadpisuje `visit` dla konkretnych typów
* Dostaje się informacje o typie bez rzutowania dynamicznego
* Problem z cyklicznymi zależnościami - trzeba stosować deklaracje klas
	* klasa bazowa hierarchii odwiedzanej (`Element`) jest zależna od bazowego wizytatora
	* klassa bazowa wizytatora (`Visitor`) jest zależna od wszystkich klas w hierarchii odwiedzanej
	* klasa konkretna z hierarchii odwiedzanej jest zależna od wizytatora bazowego 
	* klasa konkretnego wizytatora jest zależna od wszystkich klas w hierarchii odwiedzanej

### Wizytator acykliczny (Martin)
* Klasa bazowa wszystkich wizytatorów
	* tylko wirtualny destruktor
* Abstrakcyjna klasa bazowa dla wizytatora konkretnego typu z hierarchiii odwiedzanej
	* dziedziczy bo bazowym wizytatorze
* Konkretny wizytator
	* dziedziczy wielobazowo
	* po bazowym wizytatorze
	* po klasie wizytatora każdego typu z hierarchii odwiedzanej
* Użyty pojedynczy `dynamic_cast` w metodzie `accept` klasy odwiedzanej
	* operacja lokalna
* Dodanie nowej klasy do hierarchii odwiedzanej nie wymaga zmiany bazowego wizytatora i wszystkich konkretnych

## Wzorzec wielometody
 * Kod zależny od dwóch typów (a nie jednego jak Wizytator)
 * Np. obliczenie pola powierzchni przecięcia 2 figur
	 * `double intersect(Circle&, Circle&);`
	 * `double intersect(Circle&, Rectangle&);`
	 * `double intersect(Rectangle&, Rectangle&);`
* Są wizytatory dla wszystkich klas kształtów
* Niepoprawna implementacja przez wykładniczo wiele `if` i `dynamic_cast`
* Można zaimplementować niskopoziomowo jako dwuwymiarową tablicę wskaźników do funkcji

```cpp
double intersect(Figure &a, Figure &b) {
	IntersectVisitor visitor(a);
	b.accept(visitor);
	return visitor.value();
}

struct IntersectVisitor : public Visitor {
	IntersectVisitor(Figure &fig): fig_(fig), value_(0.0) {}
	
	virtual void visit(Rectangle &r) {
		RectangleVisitor rectVisitor(r);
		fig_.accept(rectVisitor);
		value_ = rectVisitor.value();	
	}
	
	...
}

struct RectangleVisitor : public Visitor {
	RectangleVisitor(Rectangle &r) : r_(r), value_(0.0) {}

	virtual void visit(Rectangle &r) { value_ = intersect(r_, r); }
	
	virtual void visit(Circle &c) { value_ = intersect(c, r); }

	...
}
```


## Wzorzec dekoratora
* Dodanie nowej funkcjonalności w czasie działania
* Alternatywa dla dziedziczenia
* Do sytuacji w których liczba sytuacji byłaby potęgowa
	* np. strumień binarny/tekstowy szyfrowany/nieszyfrowany kompresowany/niekompresowany