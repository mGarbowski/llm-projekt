# Programowanie generyczne (ZPR- W10 -2020 12 08)

## Kolekcje i algorytmy
* Pojęcia niezależne od typu
	* kolekcje (np. lista)
	* algorytmy (np. znajdowanie największego elementu)
* Mechanizmy eliminujące redundancję kodu
	* wspólna klasa bazowa (polimorfizm czasu wykonania)
	* wykorzystanie szablonów (polimorfizm czasu kompilacji)
* Wady polimorfizmu czasu wykonania
	* narzuty na wołanie funkcji wirtualnych
	* rzutowanie dynamiczne
	* problem typów wbudowanych (nie ma `Object` jak w Javie)
* Szablony
	* mechanizm generowania kodu
	* rozumie składnię języka (w przeciwieństwie do dyrektyw preprocesora)
	* konkretyzacja - dla każdego typu powstaje binarna implementacja np. dla wektora

## Składnia szablonów
* Parametrem może być typ lub liczba całkowita
* Parametr może mieć wartość domyślną

## Szablon jako mechanizm czasu kompilacji
* Jeśli kod nie został użyty to nie jest kompilowany
	* można nie wyłapać błędu
	* pozwala bardzo ograniczyć kod binarny
* Brak narzutów czasowych w czasie wykonania
* W nagłówkach (miejscu użycia) musi znajdować się definicja (a nie sama deklaracja)
	* nagłówki stają się nieczytelne, bo zawierają implementację

## Organizacja modułu
Nagłówek `x.hpp` - czytany przez użytkownika modułu
```cpp
template<typename T> class Foo {
	// Definicja klasy i metod inline
};
#include "x.tpp"
```

Implementacja metod wzorca `x.tpp`
```cpp
template<typename T> T& Foo<T>::get(int index) {
	// kod szablonu
}
```

Implementacja metod niezależnych od parametrów szablonu - plik `x.cpp`

## Listy inicjujące
* Dostarczanie kolekcji stałych
* Jako parametr (np. konstruktora)
	* uproszczenie zapisu

## Szablony funkcji
* Algorytmy niezależne od typu
* Podobne działanie jak do szablonu klas
* Można jawnie skonkretyzować szablon funkcji
	* np. jeśli nie wynika z typów argumentów

## `typename`
* Jawne wskazanie, że identyfikator jest typem
* W szablonie można stosować wymiennie z `class`
* Odróżnienie sięgnięcia do typu (`using`) od sięgnięcia do składowej

## Specjalizacje szablonu
* Dostarczanie różnych wersji dla tego samego szablonu
	* kompilator rozstrzyga której wersji użyć
* Dla określonych typów można dostarczyć pewnych optymalizacji


```cpp
// Szablon klasy
template<typename T> class Foo { /* ... */ };

// Częściowa specjalizacja dla wskaźników
template<typename T> class Foo<T*> { /* ... */ };

// Pełna specjalizacja dla typu int
template<> class Foo<int> { /* ... */ };
```

## Template metaprogramming
* Szablony (konkretyzacja i specjalizacja) są równoważne maszynie Turinga
	* szablony są odrębnym, funkcyjnym językiem programowania
* Można zapisać cały program przy użyciu szablonów
	* używając konkretyzacji i specjalizacji
* Może znacznie zwiększyć wydajność kosztem zwiększenia czasu kompilacji

```cpp
template<unsigned n>
struct Silnia {
	enum { value = n*Silnia<n-1>::value };
};

template<> struct Silnia<0> {
	enum { value = 1; }
};

cout << Silnia<5>::value;
```

## Szablony vs hierarchia klas
* Preferujemy hierarchię klas kiedy chcemy wyrażać jakieś wspólne elementy
* Używamy szablonów gdy
	* nie można utworzyć klasy bazowej
	* ważne są typy wbudowane
	* bardzo ważna jest efektywność
	* akceptowalne jest wydłużenie kompilacji
* Prosta reguła
	* szablony - gdy typ obiekty nie modyfikuje działania algorytmu (np. kolekcja)
	* funkcje wirtualne - gdy typ obiektu modyfikuje działanie klasy

## Problemy przy stosowaniu szablonów
* Generuje kod, który następnie będzie kompilowany
	* typowo najpierw tworzy się testowy kontener/algorytm dla konkretnego typu
	* dostarcza się testy jednostkowe testujące działanie dla konkretnego typu
	* przekształcenie zapisu w szablon i poprawienie testów
	* dodanie testów dla innych typów
	* inne sposoby mogą prowadzić do powstania błędów trudnych do wykrycia
* Język szablonów jest funkcyjny
	* nie ma mechanizmu rozróżniania typów
* Nadmiernie rozrasta się kod binarny
* Nieczytelne komunikaty o błędach
	* nie w tym miejscu gdzie właściwie występuje błąd

## Iterator
* Pozwala dostarczyć tych samych algorytmów niezależnie od typu kolekcji
* Niektóre kolekcje pozwalają na przesuwanie iteratora (wydajnie) o wiele elementów do przodu
* Kategorie iteratora
	* input_iterator - jednokrotny odczyt wskazywanego elementu, inkrementacja
	* output_iterator - jednokrotny zapis elementu, inkrementacja
	* forward_iterator - wielokrotny odczyt/zapis, inkrementacja (lista jednokierunkowa)
	* bidirectional_iterator - j.w. + przesunięcie o jedne element do tyłu (lista dwukierunkowa)
	* random_access_iterator - j.w. + przesuwanie do przodu i do tyłu o n elementów (tablica)
* Ogólny algorytm do przesunięcie iteratora o n kroków do przodu
	* wykorzystuje operator ++
	* działa niewydajnie dla random_access_iterator

## Trejty
* Klasa bez składowych
* Nie służy do tworzenia obiektów
* Tylko do rozróżniania typów
* Definiowane jako `struct`
* Mogą być powiązane relacją dziedziczenia
* Iteratory mają typ składowy iterator_category
* Przeciążenie szablonu z parametrem służącym tylko do rozróżnienia algorytmu na podstawie typu
* Pomocniczy szablon `iterator_traits`
* Nie są tworzone obiekty, nie następuje skok, kod jest inline'owany
	* rozróżnienie jest w czasie kompilacji

### Trejty w bibliotece standardowej
* iterator_traits
* char_traits
* numeric_limits
	* `!(x==x)` - badanie czy jest NaN
* type_traits
	* sprawdzanie właściwości typu
	* czy liczba całkowita, czy funkcja, czy klasa, czy const
	* czy powiązane relacją dziedziczenia
	* czy ma konstruktor

## Nadmierne rozrastanie się kodu binarnego
* Konkretyzacja sprawia, że generuje się oddzielne kody binarne na podstawie tego samego szablonu
* Wzorzec adaptera
	* współdzielenie implementacji dla typów o takiej samej reprezentacji binarnej
	* np. pełna specjalizacja dla `void*`, specjalizacja dla dowolnego wskaźnika dziedziczy po `Kolekcja<void>`

### Eliminacja parametrów szablonu, które nie są typami
* Przechowywanie liczby jako składowa w bazowym szablonie
* Przykład macierzy

## Nieczytelne komunikaty o błędach
* `static_assert` - asercja czasu kompilacji
	* nie było w starszych standardach języka
	* generuje błąd jeśli parametr szablonu jest niepoprawny

## Koncepcje (C++20)
* ...

## CRTP
* Curiously Recurring Template Pattern
* Klasa dziedziczy po szablonie, którego jest parametrem
* W czasie kompilacji rozsztrzyga się jaki kod ma być wołany
* Efekt podobny do funkcji wirtualnych
	* bez VTBL i kosztów późnego wiązania
* Można np. dziedziczyć po szablonie żeby automatycznie wygenerować operatory porównania

```cpp
template<typename T> struct base {
	int calculate() {
		return static_cast<T*>(this)->doCalculate();
	}
};

struct derived : base<derived> {
	int doCalculate() { /*...*/}
}
```

## Szablony jako parametry szablonów