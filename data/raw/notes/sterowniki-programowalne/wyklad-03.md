# Wprowadzenie do lab 1 (2025-03-13)
* Wejścia cyfrowe `X` i wyjścia cyfrowe `Y`
* Program operatorski wizualizuje stany wejść/wyjść

`Y10 := X10 AND X11;`
`Y11 := X12 OR X13;`

Wejście `X14` ustawi wyjście `Y12` - stan musi być podtrzymany (bez użycia `SET/RST`)
`Y12 := X14 OR Y12`

Wejście `X15` zresetuje wyjście `Y12`(bez użycia `SET/RST`)
`Y12 := (X14 OR Y12) AND NOT X15;`

## Wyjście Y13 ma mrugać zgodnie z bitem systemowym SM412 (zegar 1Hz, tylko do odczytu)
`Y13 = SM412`

Bity pamięciowe M mogą być podtrzymywane po restarcie sterownika (da się skonfigurować)

Przestrzeń D - od `D0` do `D8000` - rejestry 16-bitowe
Można przypisywać do nich etykiety (nazwy zmiennych)

## Bit pamięci `D600.5` ma zostać ustawiony na zbocze narastające wejścia `X16`
W języku ladder - strzałka do góry w wejściu
S w cewce - realizacja funkcji SET na tym adresie pamięci - bit zostanie podtrzymany (analogiczne działanie do zapętlenia z logicznym OR)

LDP - load pulse - zbocze narastające
`D600.5 := LDP(TRUE, X16);` - ustawia na jeden cykl
`D600.5 := LDP(TRUE, X16) OR D600.5;` - podtrzymanie
`SET(LDP(TRUE, X16), D600.5);` - podtrzymanie przez instrukcję SET

```
IF LDP(TRUE, X16) THEN
	D600.5 = TRUE;
END_IF;
```

IF i SET nie są równoważne z cewką w języku ladder

## ... zbocze opadające
instrukcja LDF (falling)

## Rejestr `D601` ma zwiększać się o 1 na każde włączenie wejścia `X16` 
ladder - `---[ INC D600.1 ]`

`--| X16 |---[INC D600.1]` - złe bo inkrementuje co każdy cykl sterownika, trzeba na zbocze narastające

`INC(LDP(TRUE, X16), D601)`

```
IF LDP(TRUE, X16) THEN
	D601 := D601 + 1;
END_IF
```

domyślnie wszystkie rejestry są zerami, konfiguruje się, jakim typem danych ma być rejestr

## Przycisk Alternate P1 powinien sterować lampką L1
Przyciski są na panelu operatorskim

alternate - kliknięcie przełącza stan przycisku (bistabilny)
momentary - 1 kiedy trzymamy naciśnięty (monostabilny)

w sterowniku są zdefiniowane etykiety do przycisków, lampek, rejestrów

na panelu jest przełącznik to wybierania programu (ladder i st)

## Przykład programu w ladder
GOEND - skok na koniec programu

Na 1 lab przeczytać rozdział 2, 6.1, 7.1, 8.1

tryb monitoringu w IDE - podgląd zmiennych na żywo w kodzie

online program change - szybsze wgranie zmiany