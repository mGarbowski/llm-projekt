# (2024-10-17)
## Zaburzenie elementów macierzy A i wektora b

Wzór na błąd względny wyniku...

## Układ równań z macierzą trójkątną
Elementy pod diagonalą są zerowe
Rozwiązujemy iteracyjnie idąc od dołu rozwiązując n skalarnych równań - najprostsza i najlepsza metoda

rozwiązanie numeryczne jest równoważne rozwiązaniu dokładnemu układu z zaburzoną macierzą
algorytm jest numerycznie stabilny i poprawny (metoda pozornych równoważnych zaburzeń)

błąd względny $\le O(1/2 n^2) eps$
Liczba operacji arytmetycznych $D=O(1/2 n^2), M=O(1/2 n^2)$

## Eliminacja Gaussa
1. eliminacja zmiennych - przekształcenie do równoważnego układu równań z macierzą trójkątną górną
2. postępowanie odwrotne (back-substitution) - algorytm opisany wcześniej

Krok 1
wyzerowanie kolumny pierwszej oprócz elementu w wierszu 1
mnożymy wiersz 1 przez współczynnik i odejmujemy od wiersza i-tego (nie modyfikujemy pierwszego wiersza)

Krok 2
zerowanie kolumny drugiej poza elementami w wierszach 1 i 2

...

Każdy krok jest operacją liniową - jest równoważny pomnożeniu układu prezz macierz L

L - macierz jednostkowa ze współczynnikami w pierwszej k-tej kolumnie
macierz odwrotna - współczynnik bez minusów

Całe przekształcenie to mnożenie prawostronnie przez kolejne macierze $L^{(k)}$

Ogólna zalezność
$(ABC)^{-1} = C^{-1}B^{-1}A^{-1}$

L - lower triangular
U - upper triangular

A = LU
rozkład A na LU - faktoryzacja LU macierzy A


$LUx=b \iff Ly=b, Ux=y$
$y=b^{(n)}$

nakład na rozkład LU macierzy $O(1/3n^3)$

Co jeśli element centralny przez który dzielimy jest zerowy - eliminacja Gaussa z przestawieniami wierszy - zawsze da się to zrobić dla układu równań z macierzą nieosobliwą (1 rozwiązanie)

## Eliminacja Gaussa z częściowym (kolumnowym) wyborem elementu głównego
Wybieramy ten element główny, który ma maksymalny moduł - nawet nie sprawdzamy czy element jest bliski 0, tylko zawsze bierzemy ten o maksymalnym module - minimalizujemy przez to błędy numeryczne - najmniejsze moduly wspolczynnikow l - najmniejsze modyfikacje wierszy

zamieniamy wiersze i stosujemy dalej standardowy algorytm

### Pełny wybór elementu głównego
przestawianie też kolumn w podmacierzy
w praktyce - mała poprawa kosztem dużo większego nakładu na obliczenia


### Przestawianie elementów
Przestawienie elementów jest równoważne pomnożeniu przez macierz przestawień - macierz jednostkowa z przesuniętymi jedynkami

Postać macierzowa algorytmu z przestawieniami ...


Ze względu na zamiany wierszy, rozkład nie dotyczy oryginalnej macierzy A, tylko PA
$LU = PA$
$P = P^{(n-1)} \ldots P^{(1)}$
ale nie wiemy z góry jak będziemy przestawiać

macierzy przestawień nie warto trzymać pamięci, lepiej zapamiętać wektor mapujący elementy do pierwotnych indeksów

### Błędy numeryczne
Można pokazać że wynik numerycznej faktoryzacji jest równa dokładnej faktoryzacji zaburzonej o macierz E

górne oszacowanie jest bardzo wysokie ($2^n$) ale w praktyce jest bardzo pesymistyczne

algorytm jest numerycznie stabilny