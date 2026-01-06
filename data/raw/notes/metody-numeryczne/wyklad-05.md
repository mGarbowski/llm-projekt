# 2024-11-07

Znajdowanie wartości własnych metodą QR
powtarzenie - rozkłąd QR, wymnożenie RQ
dąży do macierzy diagonalnej z wartościami własnymi na diagonali
działą bardzo wolno dla zbliżonych do siebie wartości własnych

jeśli wartości własne są różne
element poza diagonalą dąży do zera liniowo z ilorazem ... (moduł ilorazu kolejnych wartości własnych)
jeśli różnica jest niewielka to zbieżność jest wolna, jeśli są równe to iloraz jest 1


algorytm z przesunięciami
w k-tej iteracji przed rozkładem przesuwa się wartości własne o $p_k$ (dodanie macierzy jednostkowej przemnożonej przez stałą)
kolejna macierz to iloczyn $RQ + p_kI$
znowu przekształcenie przez podobieństwo ale przez inną macierz Q
wtedy iloraz zbieżności $|\lambda_{i+1} - p_k|/|\lambda_i-p_k|$
trzeba znaleźć odpowiednie przesunięcie
jako przesunięcie bierze się wartość własną podmacierzy 2x2 prawego dolnego rogu, tą która jest najbliższa wartości elementu w prawym dolynm rogu
powtarzane iteracyjnie dopóki elementy poza diagonalą się nie wyzerują
w praktyce kilka kroków

Struktura algorytmu QR z przesunięciami
wyznaczamy wartość własną prawego dolnego rogu
opuszczamy dolny wiersz i prawą kolumnę
...
aż zostanie macierz 2x2 dla której oblicza się wartości własne analitycznie

też dla liczb zespolonych, może pojawić się liczba zespolona jako wartość własna przy macierzy liczb rzeczywistych

Dla macierzy symetrycznych metoda jest niezawodna
Dla macierzy zespolonych może się zapętlić


algorytm bez przesunięć nie ma mechanizmu znalezienia wartości własnych zespolonych


## Wartości szczególne
Uogólnienie wartości własnych na macierze niekwadratowe (singular values)
Dla macierzy prostokątnej $A_{m \times n}, m \ge n$ 

Pierwiastki wartości własnych macierzy $A^TA$
dla macierzy kwadratowych symetrycznych, dodatnio półokreślonych wartości szczególne to wartości własne

dla macierzy kwadratowych symetrycznych wartości szczególne są modułami wartości własnych

dla pozostałych nie ma bezpośredniej relacji

Wyznaczanie wartości szczególnych z definicji (liczenie wartości własnych $A^TA$) prowadzi do znacznej utraty dokładności numerycznej

stosuje się algorytmy SVD nie prowadzące do utraty dokładności np Goluba-Reinscha

### Twierdzenie o dekompozycji SVD
Szerokie implikacje praktyczne 

Dla dowolnej macierzy prostokątnej istnieją macierze kwadratowe ortogonalne U, V i maciesz $\Sigma$ takie że $A=U\Sigma V^T$$
$\Sigma$ - macierz kwadratowa, w górnej części diagonalna z wartościami szczególnymi na diagonali, dopełniona zerami na dole

liczba niezerowych wartości szczególnych definiuje rząd macierzy
to jedna z metod na liczenie rzędu macierzy

U - kolumny to ortonormalne wektory własne $AA^T$
V - kolumny to ortonormalne wektory własne macierzy $A^TA$

Analogicznie jak to że dla macierzy kwadratowych można faktoryzować $V^TAV = diag\{\lambda_i\}$

matlab liczy wskaźnik uwarunkowania macierzy jako $cond_2(A) = \sigma_{max}/\sigma_{min}$
$\| A \|_2 = \sigma_{max}$
$\| A^{-1} \|_2 = \sigma_{min}$

wartości szczególne macierzy odwrotnej będą odwrotnościami dla macierzy oryginalnej


## Liniowe zadanie najmniejszych kwadratów
Rozwiązanie układu równań z macierzą prostokątną (więcej równań niż zmiennych)
Szuka się takiego wektora, który da najmniejszą wartość $\|b - A \hat{x} \|_2$
odpowiada rzutowaniu prostokątnemu wektora b na podprzestrzeń x

typowa sytuacja np jak robimy wiele (m) pomiarów dla n parametrów

dla ujednoznacznienia definiuje się rozwiązanie jako taki wektor o najmniejszej normie

jest równoważne minimalizacji funkcji kwadratowej
$$
J(x) = (b-Ax)^T(b-Ax)
$$

Jeżeli macierz A jest pełnego rzędu to $A^TA$ jest dodatnio określona, a J jest funkcją wypukłą o jednym minimum

Układ równań normalnych $A^TAx = A^Tb$
Dla słabo uwarunkowanej macierzy A, uwarunkowanie $A^TA$ staje się jeszcze gorsze

Można zamiast tego wykorzystać rozkład QR macierzy A
po przekształceniu wychodzi $Rx = Q^Tb$, a uwarunkowanie jest takie samo jak dla macierzy A - dużo lepsze (pod warunkiem że obliczanie rozkładu jest dokładne)

inna postać dla rozkładu unormowanego i nieunormowanego


dla macierzy niepełnego rzędu k < n
najlepiej stosować algorytmy oparte na SVD

Macierz ortogonalna - pomnożenie wektora nie zmienia jego długości w normie 2

można minimalizować tylko pierwsze k składowych wektora błędu, pozostałe wartości mogą być dowolne (będą mnożone przez 0)

macierz pseudoodwrotna Penrose'a Moore'a - uogólnienie odwrotności macierzy

## Rozkład Householdera
Odbicie zwiercadlane względem płaszczyzny
Przekształcenie zdefiniowane wacierzą

$P = I - 2ww^T$, w - wektor jednostkowy
odjęcie od wektora rzutu na wektor w

np przekształcenie wektora, tak żeby był równoległy do wersora układu współrzędnych
nie należy wyliczać macierzy, tylko wynik mnożenia (przekształcić wzór z definicji)