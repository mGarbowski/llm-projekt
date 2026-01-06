# Wykład 03 (2023-10-17)
```haskell
check n = case mod n 2 of
    0 -> "parzysta"
    a -> "nieparzysta"
```

można definiować operatory tak jak funkcje

## Formatowanie
* wszystkie definicje muszą zaczynać się w tej samej kolumnie
* kolejne linie, wcięte w stosunku do początku definicji, są traktowane jako jej kontynuacja

## Typy danych
Haskell jest silnie i statycznie typowany
* na etapie kompilacji, każda wartość ma przypisany typ
* przypisany typ nie zmienia się przez cały czas działania programu

Int jak isize
Integer ma nieograniczoną precyzję


nie ma zmiennych ani pętli
zamiast pętli używa się rekurencji
środowisko uruchomieniowe optymalizuje rekurencje

