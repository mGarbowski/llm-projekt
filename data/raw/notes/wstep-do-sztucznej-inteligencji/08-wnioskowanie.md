# Inżynieria wiedzy (2024-01-11)

## Rachunek zdań
Wartościowanie - przypisywanie wartości zdaniom
Klasyczny rachunek zdań - każdemu zdaniu można przypisać tylko wartości prawda lub fałsz
Fromuły logiczne buduje się ze zdań prostych używając spójników logicznych (not, and, or, ...)
Za pomocą jednego spójnika nand można wyrazić wszystkie inne

Tautologie - zdania zawsze prawdziwe niezależnie od wartościowania (prawa de Morgana, prawo wyłączonego środka itd.)

## Badanie czy formuła jest tautologią
Można sprawdzić wszystkie możliwe wartości składowych zdań prostych (złożoność wykładnicza)

## Problem spełnialności (SAT)
Czy dla podanej formuły istnieje takie wartościowani, żeby była prawdziwa - jest rozstrzygalny ale ma złożoność $O(2^n)$

## Postać normalna formuły
* Literał - zdanie $p$ lub $\neg p$ , gdzie $p$ to zdanie proste
* Klauzula - alternatywa literałów $p_1 \vee p_2 \vee \ldots \vee p_n$ 
* Koniunkcyjna postać normalna (CNF) - koniunkcja klauzul

### Sprowadzanie formuły do koniunkcyjnej postaci normalnej
* Eliminacja równoważności
* Eliminacja implikacji
* Ograniczenie zakresu negacji do literału (prawa de Morgana)
* Przekształcenie alternatywy do koniunkcji

### Klauzula Horna
Wygodna do wnioskowania

$$
L_0 \vee \neg L_1 \vee \neg L_2 \vee \ldots \vee \neg L_n 
\equiv L_1 \wedge L_2 \wedge \ldots \wedge L_n \implies L_0
$$

## Formuły ze zmiennymi
Rachunek predykatów 1. rzędu.
Formuły są wartościowane, gdy podamy wartości zmiennych
Kwantyfikatory $\forall$ i $\exists$ 

Obiekty (termy)
* stałe
* zmienne
* funkcje (obliczają termy na podstawie listy termów)
	* predykat - funkcja odwzorowująca argumenty na zbiór {prawda, fałsz}

Notacje predykatów
* prefiksowy
* infiksowy
* listowy
* bez nazwy

## Formuła poprawnie zbudowana (FPZ)
Atom to predykat oraz prawda i fałsz.
* Atom jest FPZ
* FPZ połączone spójnikami logicznymi to FPZ
* FPZ z kwantyfikatorami to też FPZ

### Postać normalna formuły
* Atom to $P$, $\neg P$, prawda, fałsz

### Metoda skolemizacji
Usuwanie kwantyfikatorów szczegółowych

### Przenoszenie kwantyfikatorów na początek formuły

### Podstawienie
Podstawienie to przypisanie termu do zmiennej (termy to stałe, zmienne, funkcje).
Unifikator pary formuł to taka para podstawień, które doprowadza obie formuły do wspólnej postaci

Najbardziej ogólny unifikator - przekształca do postaci prawdziwej dla jak najszerszego zbioru obiektów

## Algorytm wnioskowania
Modus ponens $A \wedge (A \implies B) \equiv B$ 

* Zaczynamy od znanych faktów
* Rozszerzamy fakty w oparciu o posiadane reguły
* Powtarzamy krok 2 do skutku

## Rachunek predykatów wyższego rzędu
Zawiera kwantyfikatory, które dotyczą funkcji lub predykatów, a nie tylko pojedynczych zmiennych