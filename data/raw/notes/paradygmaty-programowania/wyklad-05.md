# 2023-10-31

wiele funkcji można wyrazić jako `foldr`

Funkcje anonimowe (lambda abstraction)
`(\ x y -> x + y) 1 2`

Przydają się kiedy nie chcemy nazywać argumentu do filter itd albo kiedy chcemy zwrócić funkcję z funkcji

`.` - operator łączenia funkcji
```haskell
(not.even.sum) [1..5]
```

każdą funkcję wieloargumentową można wyrazić jako kolejne aplikowanie funkcji jednoargumentowych
(aplikowanie częściowe)
Każda funkcja w Haskellu jest conajwyżej jednoargumentowa
`:type add 5`

`map (1/) [1..4]`

`$` operator aplikacji funkcji - można używać mniej nawiasów

`sqrt (recip (1 + 3) )`
`sqrt $ recip $ 1+3`


# Algebraiczne typy danych
Deklarowanie synonimu
`type String = [Char]`

Można utworzyć nowy typ danych podając wartości tzw konstruktorów
`data Bool = False | True`

Nazwa typu musi zaczynać się od wielkiej litery

```haskell
type Pos = (Int, Int)
data Move = North | South | East | West

move :: Move -> Pos -> Pos
move North (x, y) = (x, y+1)
...
```

`data Shape = Circle Float | Rect Float Float`
```haskell
area (Circle r) = pi * r^2
area (Rect a b) = a * b 
```



