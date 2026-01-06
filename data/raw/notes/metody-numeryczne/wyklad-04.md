# 2024-10-31

Mecierz $Q_{m,n}$ która ma kolumny wzajemnie ortogonalne to $Q^TQ=D_n$
$D_n$ jest macierzą diagonalną o wymiarowości $n$

Jeśli kolumny Q są dodatkowo unormowane (długości 1, ortonormlane) to D jest macierzą jednostkową

## Macierz ortogonalna
macierz kwadratowa Q to macierz ortogonalna jeśli $Q^TQ=I$
ma kolumny które są wektorami ortonormalnymi

$Q^T=Q^{-1}$
$Q^TQ=QQ^T=I$
wiersze też są wzajemnie ortonormalne

## Lemat
macierz prostokątna o kolumnach wzajemnia ortonormalnych
$|Qx|_2 = |x|_2$
nie zmienia długośći wektora w normie 2


## Rozkład QR
twierdzenie

Każdą macierz prostokątną $A_{m,n}$ o liniowo niezależnych kolumnach (pełny rząd równy n) można przestawić w postaci rozkładów ortogonalno trójkątnych


1 rozkład qr wąski (ekonomiczny), nieunormowany
A=QR
Q - kolumny ortogonalne
R - trójkątna górna  z jedynkami na diagonali

2 rozkład QR wąski (ekonomiczny)
A = QR
Q - kolumny ortonormalne
R - trójkątna górna z dodatnimi elementami

3 rozkład QR
A = QR'
Q - kwadratowa, maierz ortogonalna
R' - kwadratowa R dopełniona zerami

Dowód przez konstrukcję (podanie algorytmów)
A ortogonalizujemy (np. algorytmem Grama-Schmidta)
GS dla 2 wektorów
	wybieramy jeden
	od drugiego odejmujemy wektor zrzutowany na pierwszy
	 dla kolejnego wektora odejmuje się rzuty na wszystkie poprzednie wektory

kolumny q tworzą bazę w której można wyrazić oryginalne kolumny a

wzory dają taką samą postać jak przy mnożeniu macierzy
zapis w postaci mnożenia macierzy kolumn q z macierzą współczynników r daje rozkład ekonomiczny nieunormowany

po znormowaniu kolumn macierzy Q i pomnożeniu macierzy R przez macierz diagonalną z oryginalnymi normami q wychodzi rozkład QR wąski

jeśli macierz prostokątną Q uzupełni się do kwadratowej przez dodanie dowolnych ortonormalnych kolumn
i macierz R uzupełni się zerami do wymiaru m x n
otrzymujemy rozkład QR (pełny)

rozkład QR istnieje dla każdej macierzy prostokątnej mx n, m >= n (też o rzędzie mniejszym od n)


## Numeryczne wyznaczanie rozkładu QR
dla macierzy o pełnym rzędzie - ortogonalizacja Grama-Schmidta

QR pełny przez rozszerzenie macierzy A na początku kolumnami liniowo niezależnymi
mogą być dowolne, bo zostaną przemnożone w iloczynie przez 0 z macierzy R

Z reguły stosuje się zmodyfikowany algorytm GS o lepszych własnościach numerycznych (inna kolejność ortogonalizacji)

dla macierzy o niepełnym (dowolnym rzędzie) można rozszerzyć algorytm GS
ale zalecane jest stosowanie jednej z
	metoda odbić Householdera
	metoda obrotów Givensa - zalecana dla macierzy rzadkich

## Algorytmy Grama-Schmidta
CGS i MGS

CGS - i-ta kolumna ortogonalizowana względem i-1 poprzednich - kumuluje się błąd

MGS - ortogonalizuje wszystkie następne wobec ostatniej zortogonalizowanej, błędy lepiej się rozkładają, nie rozważamy dokładnie czemu


uwaga
iloczyn skalarny dla wektorów liczb rzeczywistych - nie ma znaczneia kolejność mnożenia
dla liczb zespolonych - kolejność ma znaczenie


## Wartości własne
$Av = \lambda v$
po przemnożeniu, wektor nie zmienia kierunku
madier zo wymiarze n, ma dokładnie n wartości własnych
dla macierzy symetrzycznej wartości są rzeczywiste
właściwie to nie wektory, a kierunki własne (bo dla przeskalowanego też działa), tradycyjnie normujemy je do długości 1
kierunki normalne są ortogonalne, tworzą bazę
każdy wektor x można wyrazić jako kombinację liniową wektorów własnych

$x = \alpha_1 v_1 + \alpha_2 v_2$
$Ax = \alpha_1 \lambda_1 v_1 + \alpha_2 \lambda_2 v_2$

Stąd wyprowadza się wzór na normę 2 macierzy
największe wydłużenie - w kierunku wartości własnej o największym module
pierwiastek z maksymalnej wartości własnej macierzy $A^TA$

Kolejne mnożenia wektora przez macierz A - zbieżne jeśli $|\lambda_{max}| < 1$ 

$(A - \lambda I) v = 0$ - układ równań
warunek konieczny istnienia rozwiązania - osobliwość macierzy
$\det(A - \lambda I) = 0$
równanie charakterystyczne macierzy
zbiór wszystkich wartości własnych $sr(A)$

własność o przesunięciu wartości własnych o $\alpha$


Macierze A i B są podobne jeśli istnieje macierz kwadratowa, nieosobliwa że $S^{-1}AS=B$
macierze podobne mają takie same wartości własne


jeśli wszystkie wektory własne macierzy A są ortogonalne to można tę macierz sprowadzić do macierzy diagonalnej z wartościami własnymi przez podobieństwo

### Zespolone wartości własne
Typowo macierz niesymetryczna ma zepsolone wartości własne

macierz kwadratowa
hermitowska - odpowiednik symetrii dla liczb rzeczywistych
unitarna - odpowiednik ortogonalności dla liczb rzeczywistych
macierz normalna $A^*A=AA^*$ 


### twierdzenie Schura
Każda macierz jest podobna do macierzy trójkątnej górnej przez podobieństwo do macierzy unitarnej

## Metody wyznaczania wartości własnych
Metady wyznacznikowe - znajdowanie zer wielomianu charakterystycznego
Metody bisekcji wykorzystująca ciągi Sturma
Metoda Hymana
Metoda Jacobiego - efektywna do wymiaru ok n=10

Metoda QR - najbardziej ogólna, wydajna

zbieżność do iloczynu $V^{-1}AV = diag\{\lambda\}$

kolokwium 28 XI