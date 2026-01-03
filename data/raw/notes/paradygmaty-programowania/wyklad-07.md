# Wykład 07 (2023-11-14)

## Kolokwium
* Przesunięty o tydzień? Będzie informacja na teamsach
* 20 pytań testowych
* może 1 linijka kodu do napisania
* "jakiego typu jest to wyrażenie/funkcja" itp
* "jaka jest wartość wyrażenia w haskellu"
* teoretyczne pytania też
* nie trzeba pamiętać definicji funkcji z std


## Leniwe wartościowanie
```haskell
ones = 1 : ones
```

Dzięki leniwemu wartościowaniu możemy używać nieskończonych listy
(np. pobrać głowę listy, zrobić zip ze skończoną listą itd)

Wyrażenie będzie redukowane tylko do takiego stopnia ile potrzeba żeby dostać wynik

## Ścisłe wartościowanie w Haskellu
operator `$!` pozwala wymusić ścisłe (nie leniwe) wartościowanie


# Podstawy Smalltalka
Najstarszy język obiektowy, rok 1980

Program jest zbiorem komunikujących się ze sobą obiektów

## Obiekt
Operacje które może wykonać + dane

Hermetyzacja (enkapsulacja) - wnętrze obiektu nie jest widoczne na zewnątrz
Wszystkie dane są prywatne, dostęp jest możliwy tylko przez operacje

Model pączka z nadzieneim

Wszystko jest obiektem (liczby, komunikaty, klasy)

## Komunikat
Wysłana do obiektu prośba o wykonanie operacji
Operacja zawsze zwraca obiekt (może być pusty)

Składnia

```smalltalk
anAccount withdraw: 50
```
obiekt, komunikat (słowa kluczowe z argumentami)

Operatory arytmetyczne też są komunikatami, wykonywane od lewej do prawej

## Klasa
Fabryka produkująca obiekty

Do wyprodukowania obiektu służy komunikat `new`

## Dziedziczenie
Obiekty klasy dziedziczącej są szczególnym rodzajem klasy bazowej

Analogia do taksonomii - wszystko co wiem o owadach jest prawdą dla motyli

podklasy dziedziczą operacje z nadklasy, mogą mieć ich własne wersje (przeciążenei) lub dodawać nowe


## Terminologia
* Obiekty = instancje
* Zmienne są wskaźnikami na obiekty
* Metody = operacje
* selektor - sama nazwa metody/operacji

## Podstawowe obiekty
* Integer (SmallInteger)
* Float
* Character - `$b`
* Boolean
* String - `'Smalltalk'`
* Symbol - `#Smalltalk`
    * podklasa String
    * niepusty napis
    * tylko 1 o danej wartości (singleton)
* Array - `#(5 'Smalltalk' 7)`
    * indeksowane od 1

## Rodzaje komunikatów
* unarne - `'Hello' reverse`
* binarne - operatory arytmetyczne, itp `'Hello', 'World'`
* słowa kluczowe - `12 between: 7 and: 9`

Dynamicznie typowany

wywołanie nieistniejącej metody zwraca `Nil`, nie ma błędu

self i super wskazują na ten sam obiekt, super zaczyna szukać implementacji metody od nadklasy

## Blok
Fragment kodu bez nazwy (podobne do lambdy)

`[Transcript show: 'Hello']`

```
|myBlock|
myBlock := [Transcript show: 'Hello']
myBlock value
```
Ostatnia linijka wykona blok

## Instrukcje warunkowe i pętle
Nie istnieją, są realizowane jako metody obiektów z metodami przyjmującymi bloki kodu

instrukcja warunkowa
```
12 < 17
    ifTrue: [blok kodu]
    ifFalse: [blok kodu]
```

Pętla while
```
|k count|
k := 0.
count := 6.
[count > 0]
    whileTrue: [k := k + 1.
                count := count -1].
```

## Kaskada komunikatów
```
object msg1.
object msg2.
object msg3.

object msg1; msg2; msg3.
```

Ma wbudowany garbage collector

