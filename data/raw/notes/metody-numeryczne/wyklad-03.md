# 2024-10-24
Algorytm rozkładu LU jest numerycznie poprawny i numerycznie stabilny
oszacowanie jest w praktyce bardzo konserwatywne

Rozwiązanie numeryczne układu równań Ax=b LU z częściowym wyborem elementu głównego jest dokładne - algorytm jest numerycznie stabilny i poprawny

## Rozkład $LL^T$ - Cholesky'ego-Banachiewicza
Macierz symetryczna A jest dodatnio określona jeśli 

$$
\forall x \ne 0 = x^TAx > 0
$$

Dla każdej symetrycznej, dodatnio określonej macierzy A istnieje dokładnie 1 trójkątna dolna macierz L o dodatnich elementahc diagonalnych, że $A=LL^T$
(rozkład LU nie jest jednoznaczny)

Rozwiązujemy sekwencyjnie układ $(n^2+n)/2$ - tyle ile niezależnych elementów w macierzy A (bo jest symetryczna)

dodatnia określoność gwarantuje że będzie istniał pierwiastek...

idziemy od a_11 w dół, potem kolumnami

nakład obliczeniowy rzędu $O(1/6n^3)$ (dla LU był 2 razy gorszy)
jeśli macierz spełnia warunki dla istnienia rozkładu $LL^T$ to lepiej użyć jego zamiast LU, bo do tego da mniejszy błąd numeryczny

Macierz L w rozkładzie LL^T i LU jest tak samo oznaczana ale to różne macierze!

nie ma co sprawdzać czy macierz spełnia warunki, próbując rozłożyć macierz dojdziemy do niedozwolonej operacji

## Rozkład $LDL^T$
Rozkład macierzy A na macierz trójkątną dolną, diagonalną i transponowaną trójkątną
Dla dowolnej macierzy symetrycznej

Wyznaczany z równania macierzowego $A = L(DL^T)$
Taki sam nakład obliczeniowy jak $LL^T$

wykorzystywany np w optymalizacji równań nieliniowych

Algorytmy o dobrych cechach numerycznych stosują przestawienia wierszy i kolumn $PAP = LDL^T$

## Relacja między $LDL^T$ i $LL^T$
Tylko dla tych macierzy dla których obie macierze istnieją


...rozkład macierzy diagonalnej na dwie diagonalne o elementach będących pierwiastkami
wymnażając zewnętrzne przez środkowe dostajemy $LL^T$

Łatwo przejść z jednego do drugiego


## Relacja między $LU$ i $LDL^T$
$U=DL^T$


## Iteracyjne poprawianie rozwiązania
liczymy resztę (residual) Ax-b - błąd spełnienia układu równań
rozwiązanie numeryczne do rozwiązanie dokładne + błąd

ma sens jeśli obliczamy residua w możliwie największej precyzji
rozwiązujemy równanie na wektor błędu - już mamy sfaktoryzowaną macierz, zmienia się tylko wektor prawej strony
dostajemy nowe przybliżenie przez odjęcia błędu
jeśli nowa reszta jest istotnie mniejsza i nadal zbyt duża to powtarzamy
w praktyce nie będzie wiele powtórzeń, bo już jesteśmy w rejonie błędów numerycznych

może znacznie poprawić rozwiązanie a niewiele kosztuje

## Obliczanie wyznacznika macierzy
Bardzo wrażliwe na zmiany elementów macierzy

Macierz jednego przestawienia - wyznacznik -1, równa odwrotności i transpozycji
Macierz wielu przestawień - wyznacznik (-1)^p


$$
\det A = \det(P^TP) \det A = \ldots = (-1)^p \det L \det U = (-1)^p \det U = 
(-1)^p \Pi_{i=1}^nu_{ii}
$$
## Obliczanie macierzy odwrotnej
Korzystając bezpośrednio z rozkładów
$P^TLU = A$
$(P^TLU)^{-1} = U^{-1}L^{-1}P$


Dla macierzy trójkątnych obliczenie odwrotności Y macierzy trójkątnej jest efektywne - liczymy z równania definicyjnego LY=I

nakład obliczeniowy



Korzystając z rozkładów, rozwiązując układy równań
kiedy interesują 

do obliczenia np. tylko 1 elementu macierzy odwrotnej

n układów równań
reużywa się rozkład LU

## Odwrócenie macierzy a rozwiązanie układu równań
Bez istotnej potrzeby wyznaczenia macierzy odwrotnej (można zastąpić rozwiązaniem układu równań) nie należy tego robić i zastąpić układem równań

Wzór
$$
x^{k+1} = x^k + A_k^{-1}q_k
$$

Dużo bardziej wydajne do obliczeń
$$
A_k(x^{k+1}-x^k) = q_k
$$

## Metody iteracyjne
$$
x^{(i+1)} = Mx^{(i)} + w
$$

Twierdzenie Ostrowskiego

Ciąg jest dla dowolnego punktu x^0 zbieżny do punktu $\hat{x}$ będącego rozwiązaniem równania x=Mx+w wttw $sr(M) < 1$ (największy z modułów wartości własnych macierzy M)

Miary efektywności metod iteracyjnych

* Liczba działań arytmetycznych potrzebnych do wykonania pojedynczej iteracji
* Wielkość zajmowanej pamięci
* Szybkośc zbieżności (malenia błędu)

Generalnie im mniejszy promień spektralny tym metoda jest szybciej zbieżna

## Metoda Jacobiego
A = L + D + U

...

Schemat obliczeń o strukturze równoległej

znalezienie wartości własnych jest kosztowne

są warunki dostateczne zbieżności metody jacobiego
silna diagonalna dominacja wierszowa albo kolumnowa

## Metoda Gaussa-Seidela
Ax=b -> (L+D+U)x=b
(L+D)x=-Ux+b

szeregowy schemat obliczeń - po kolei wierszami

## Testy stopu
nie warto obliczać błędu w każdej iteracji - mnożenie wektora przez macierz - kosztowna, a stosujemy te metody raczej do dużych macierzy

czy różnica między kolejnymi iteracjami jest mała
kiedy mamy podejrzenie że kończy się zbieżność to wtedy wyliczamy błąd