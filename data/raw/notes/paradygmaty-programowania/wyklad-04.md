# Wykład 04 (2023-10-24)

`++` jest prawostronnie łączny

## Typ funkcyjny
`Typ1 -> Typ` - funkcja 1-argumentowa
`Typ1 -> Typ2 -> Typ` - funkcja 2-argumentowa

na końcu jest typ zwracany a wcześcniej są typy argumentów

Można jawnie deklarować typy wartości i funkcji używając `::`
W przeciwnym wypadku typy są dedukowane

Najwyższy priorytet ma aplikowanie funkcji


## Polimorifzm i funkcje wyższego rzędedu
`fst :: (a, b) -> a` - nie ma konkretnych typów, są zmienne typów (type variable)

Funkcja polimorficzna - działa na argumentach więcej niż jednego typu

Typ polimorficzny może podlegać ograniczeniom
`(Num a, Ord a) => a -> Bool` - postać implikacji
`a` nie jest dowolnym typem, musi należeć do wymienionych klas

W klasach można określać domyślne definicje operatorów

Oddzielne operacje dzielenia całkowitoliczbowego i ułamkowego

Klasa `Enum`
pozwala tworzyć ciągi arytmetyczne `[1..10]`, `['a', 'c'..'z']`

Read i Show - klasy typów które można zamienić na stringa i wczytać ze stringa

polimorfizm wywodzi się z programowania funkcyjnego

`map reverse ["Ala", "ma", "kota"]`

funkcja wyższego rzędu przyjmuje inną funkcję jako argument
leniwa ewaluacja pozwala używać nieskończonych list `zip "Ala ma kota" [1..]`
