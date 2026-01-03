# Interpolacja (2024-12-12)

## Zadanie interpolacji

Zbiór n punktów
Funkcja interpolowana, której wartość jest znana tylko w tych n punktach
szukamy funkcji interpolującej - pokrywa się z tą oryginalną w danych punktach

Ważne klasy funkcji interpolujących
wielomiany algebraiczne
funkcje sklejane
funkcje trygonometryczne
funkcje wymierne

## Interpolacja wielomianami algebraicznymi

Twierdzenie o jednoznaczności
istnieje dokładnie jeden wielomian interpolacyjny sopnia co najwyżej n, który przychodzi przez n+1 punktów

Błąd interpolacji - z rozwinięcia w skończony szereg Taylora
wzór ...

oznaczenie $\omega_n(x)$ wielomian stopnia n+1 z jedynką przy czynniku o najwyższej potędze

### Wielomian interpolacyjny Lagrange'a

Cząstkowy wielomian
$$ L_j(x) = \prod_{i=0, i \neq j}^n \frac{x-x_i}{x_j-x_i} $$

W węźle ma wartość 0 dla $k \neq j$, i wartość $1$ dla $k=j$

Wielomian interpolacyjny Lagrange'a

$$ W_n(x) = \sum_{j=0}^n y_jL_j(x) $$

dla każdego węzła tylko jeden wielomian cząstkowy da wartość 1 i zostanie przemnożony przez $y_j$ czyli da poszukiwaną wartość w węźle

## Ilorazy różnicowe

Pierwszego rzędu

$$ f[x_i, x_{i+1}] = \frac{f(x_{i+1})-f(x_i)}{...} $$

Kolejne tworzone rekurencyjnie

Można rozpisać jako sumę - takie mianowniki jak w cząstkowych wielomianach lagrange'a

Efektywne obliczanie ilorazów różnicowych - schemat tabeli trójkątnej
wygodne przy przesuwającym się oknie punktów (dochodzi jeden, wypada jeden)
dochodzi do tabeli wiersz na dole, odpada wiersz na górze, wykorzystuje się wcześniejsze obliczenia

## Wzór interpolacyjny Newtona

Wielomian $W_k$ i $W_{k-1}$ przyjmują równe wartości w pierwszych k węzłach (do $x_{k-1}$)

Przy wyprowadzaniu wzoru niczego nie zakładaliśmy o kolejności punktów (x nie muszą być uporządkowane rosnąco)

Można uprościć wzór biorąc różnice zamiast ilorazów różnicowych

Wielomian Newtona jest wygodniejszy jeśli chcemy dołożyć 1 węzeł do już wyliczonego wielomianu

### Schemat hornera dla wzoru Newtona
...

### Zbieżność
Zwiększając stopień wielomianu nie zawsze dojdziemy do dokładnej funkcji
Tylko jeśli interpolowana funkcja ma wszystkie pochodne we wszystkich punktach przedziału

Jak nie wiemy co interpolujemy (chcemy znać w miare dokladny przebieg pomiedzy punktami) to dla wyższych stopni nie dostaniemy dobrych wyników 

## Interpolacja funkcjami sklejanymi

Na przedziale wyznaczamy punkty w rosnącym porządku

Funkcja sklejana

stopień funkcji sklejanej (zazwyczaj do sopnia 3)

funkcja sklejana jest wielomianem stopnia <= m na każdym z podprzedziałów
funkcja jest klasy ... - na całym przedziale ma pochodzne do m-1 rzędu włączne i jest ciągła

Funkcja sklejana interpolująca

### Jendoznaczność określenia funkcji sklejanej
Na każdym z przedziałów ma być wielomian stopnia co najwyżej m

jest n(m+1) współczynników do wyznaczenia - wielomiany na wszystkich podprzedziałach

warunki
n+1 warunków w węzłach interpolacji
ciągłość pochodnych rzędu od 0 do m-1 w punktach sklejenia
w sumie m(n-1) warunków

łącznie jest $n(m+1) -m + 1$ warunków

dla m=1 jest jednoznacznie

m-1 stopni swobody

dodatkowe warunki - np. wartość pochodnej na krańcach przedziału

dla stopnia trzeciego
not-a-knob condition (knob - węzeł) - ciągłość trzeciej pochodnej
węzeł przestaje być węzłem, bo po obu stronach jest ten sam wielomian
dla punktów $x_1$ i $x_{n-1}$

warunki na współczynniki tworzą układ równań liniowych

efektywne wyliczanie interpolacji - nie na kolosa

funkcje sklejane są używane nie tylko do interpolacji
zastępuje dowolną funkcję ciągłą, funkcją ciągłą o skończonej liczbie współczynników
redukujemy funkcję nieskończenie wymiarową do funkcji skończenie wymiarowej
przy wyznaczaniu przebiegów dynamicznych w efektywny sposób - redukuje się problem do wyznaczania skończonej liczby współczynników - rozwiązania układu równań
(teoria optymalizacja, sterowanie)