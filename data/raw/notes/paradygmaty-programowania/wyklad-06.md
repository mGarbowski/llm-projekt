# Wykład 06 (2023-11-07)
Oddajemy zadania na LeOnie, tylko jedna osoba z zespołu odsyła, najlepiej zipa (źródła)

## Deklarowanie przynależności typu do klasy typów
```haskell
data Move = North | South | West | East

instance Eq Move where
    North == North = True
    ...
    _ == _         = False
```

## Klauzula `deriving`
```haskell
data Move = North | South | West | East deriving Eq
```

Komilator wygeneruje domyślną implementację dla operacji z podanej klasy
Może być użyta dla klas Eq, Ord, Show, Read, Enum

## Programy interaktywne, moduły, leniwe wartościowanie

## Funkcja czysta
Przyjmuje wszystkie dane wejściowe explicite jako argumenty i zwraca wszystkie dane wyjściowe explicite jako wynik.

Pozyskanie / zwrócenie przez funkcję innych danych wejściowych / wyjściowych jest jej efektem ubocznym (side effect)
(Wyświetlenie wiadomości na ekranie, zapis do pliku, wysłanie zapytania po sieci)

* Łatwo ją analizować, to samo wejście zawsze da to samo wyjście
* Nie ma znaczenia w jakiej kolejności będą wykonywane czyste funkcje (dopóki wynik jednej nie jest wejściem drugiej)
    * Mogą być obliczane równolegle
    * Obliczanie może być odroczone w czasie

## Jak myśleć o programie interaktywnym jako o funkcji czystej
Program jest funkcją, który przyjmuje stan świata (pliki, czas, itd) i zwraca kolejny, zmieniony stan świata

Akcja to wyrażenie typu `IO`

Złożoną akcję można utworzyć przy użyciu notacji `do`

`IO` jest typem monadycznym


## Strategie wartościowania
Każdy ciąg rozwinięć wyrażenia funkcji da ostatecznie taki sam wynik (o ile się skończą)

* innermost reduction - od najbardziej wewnętrznego wyrażenia
* outermost reduction

Jeśli dla danego wyrażenia istnieje kończąca się sekwenja redukcji to outermost redction również się kończy z tym samym wynikiem
Chociaż outermost reduciton może prowadzić do większej liczby operacji

### Leniwe wartościowanie
* outermost reduction + współdzielenie wyników wartościowania argumentów
* Nigdy nie wymaga więcej kroków niż innermost reduction
* Domyślnie stosowane przez Haskella

