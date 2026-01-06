# Aproksymacja (2024-12-05)
* $f$ - funkcja aproksymowana
* $F$ - funkcja aproksymująca
* $X$ - przestrzeń funkcyjna, liniowa, $f \in X$
* $X_n$ ograniczona podprzestrzeń X z bazą ...
* $F$ jest kombinacją liniową funkcji bazowych X_n
* Zadanie polega na znalezieniu współczynników dla F, które minimalizują $\|f-F\|$

### Rodzaje
* Aproksymacja jednostajna
	* kres górny
	* jaka jest maksymalna odchyłka
	* norma Czebyszewa
	* stosowana w akustyce
* Aproksymacja średniokwadratowa ciągła
	* p - funkcja wagowa, może nas interesować większa dokładność na wybranym przedziale
* Aproksymacja średniokwadratowa dyskretna
	* odpowiednik ciągłej
	* zastąpienie całki sumą i próbkowaniem
	* często aproksymacja wielomianami
	* z reguły stopień wielomianu znacznie mniejszy od liczby punktów

### Aproksymacja średniokwadratowa dyskretna

$$ F(x) = \sum_{i=0}^n a_i \phi_i(x) $$

Zadanie aproksymacja - pomijamy pierwiastek bo jest funkcją monotoniczną, a minimalizujemy

Definiujemy macierz wartości wszystkich funkcji bazowych dla wszystkich punktów aproksymacji
w kolumnach kolejne funkcje bazowe
w wierszach kolejne punkty

wektor a - zmienne decyzyjne
wketor y - wartości funkcji aproksymowanej

$H(a) = (\|y-Aa\|_2)^2$ - zadanie najmniejszych kwadratów (LZNK)

funkcja H ma jednoznaczne minimum (jest funkcją kwadratową)
wyznaczamy analitycznie minimum funkcji H
wychodzi n równań normalnych - zerowanie 1. pochodnej

Definiuje się iloczyn skalarny w przestrzeni funkcji - suma po wszystkich punktach
$\langle \phi_i, \phi_k \rangle = \sum_{j=0}^N \phi_i(x_j) \phi_k(x_j)$
spełnia wszystkei aksjomaty iloczynu skalarnego
Macierz Grama - symetryczna bo iloczyn jest przemienny
Wychodzi $A^TAa=A^Ty$
macierz $A^TA$ jest gorzej uwarunkowana niż $A$
stosujemy rozkład QR - uwarunkowanie jak macierzy A

Przykład ...

Wybór funkcji bazowych to kwestia użytkownika - trzeba odpowiednio dobrać do danych
Przy aproksymacji wielomianami - aproksymujemy wielomianem 1 stopnia, jeśli błąd za duży to 2, ... - jeśli stopień nie jest ograniczony z góry to przeuczymy model


### Aproksymacja wielomianem
upraszcza się wzór na iloczyn skalarny funkcji bazowych

Macierze Grama dla kolejnych stopni - kolejna macierz zawiera poprzednią w lewym górnym rogu
wartości maleją w stronę prawego dolnego rogu - niekorzystne dla uwarunkowania
współczynniki jak w macierzy Hilberta
nie zaleca się aproksymacji wielomianami większych stopni


### Aproksymacja funkcjami ortogonalnymi
Najlepiej uwarunkowany jest układ równań z macierzą diagonalną - nie ma żadnych zależności między zmiennymi

ortogonalne - iloczyn skalarny równy 0

Stosujemy algorytm ortogonalizacji grama schmidta dla bazy funkcji
tak samo jak dla wektorów tylko inaczej liczy się iloczyn skalarny
dostajemy  bardzo dobrze uwarunkowany układ równań normalnych - o ile ortogonalizacja jest dokładna
należy dokładnie wykonywać ortogonalizację, stosuje się zmodyfikowany algorytm grama schmidta
sprawdzamy czy iloczyny skalarne funkcji są istotnie różne od zera

funkcje są ortogonalne na zestawie punktów (na zbiorze uczącym)

wychodzi to samo rozwiązanie (w innej bazie) - rozwiązanie LZNK jest jednoznaczne

poprawienie dokładności ortogonalizacji - reortogonalizacja lub zmodyfikowany algorytm Grama-Schmidta

## Aproksymacja Pade
Funkcja aproksymująca jest funkcją wymierną R
W ułamku $b_0 = 1$ dla jednoznaczności

Powszechnie występują w teorii sterowania (równania transmitancji)

Rozwijamy funkcję aproksymowaną w szereg Maclaurina (w punkcie x=0)

Warunek aproksymacji Pade
Jak najwięcej pierwszych współczynników rozwinięcia funkcji R w szereg Maclaurina jest równe współczynnikom rozwinięcia funkcji f

Współczynniki - nieliniowości funkcji (np dla funkcji kwadratowej będą tylko 2)
im bardziej nieliniowa tym więcej niezerowych współczynników

chcemy żeby w pobliżu zera jak najlepiej zachować nieliniowość oryginalnej funkcji

Jest $n+k+1$ współczynników do wyznaczenia (stopni swobody)
Tyle pierwszych wyrazów rozwinięcia można zrównać

w implementacji rozwiązuje się tylko te równania na $b_i$ - na niebiesko na slajdzie, resztę wylicza się wprost

dla przykładu, aproksymacja pade jest znacznie lepsza od samego szeregu Maclaurina (z taką samą liczbą współczynników)

Stosuje się Pade w równaniach algebraicznych gdzie dodatkowo występują funkcje wykładnicze (np. transmitancja)

w zastosowaniach zastępuje się funkcje niewymierne przez aproksymacje pade