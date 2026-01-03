# Wykład 05 (2023-11-08)

## Stream API
* Unikamy zwracania null, lepiej pusty strumień
* Wszystkie kolekcje mają metodę stream
* Nie można przetworzyć strumienia 2 razy (tracimy dostęp do strumienia źródłowego)
* Operacje pośrednie są wykonywane leniwie - nie wykonają się jeśli wynik nie jest potrzebny

`reduce` na kolokwium


## Obiektowosć
W Javie domyślnie wszystkie metody są wirtualne

Anotacja `@Override` jest opcjonalna

Typowe pytanie na egzamin dyplomowy

* dziedziczenie
* nadpisywanie
* polimorfizm
* abstrakcja


W pliku może być wiele klas ale tylko jeden publiczny byt

W Javie jest jednokrotne dziedziczenie

metoda `final` nie może być nadpisana

Konstruktor klasy widzi pola statyczne, wywoływany leniwie w momencie ładowania klasy
```java
static {
    // kod konstruktora
}
```


## Klasy abstrakcyjne
* Może mieć metody abstrakcyjne (bez ciała)
* Nie można utworzyć obiektu tej klasy - trzeba stworzyć klasę dziedziczącą, która zaimplementuje metody
