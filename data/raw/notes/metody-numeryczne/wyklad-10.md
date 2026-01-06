# Równania różnicowe zwyczajne c.d. (2025-01-02)

## Metody wielokrokowe
Wykorzystują informację o poprzednio uzyskanych rozwiązaniach (od $y_1$ do $y_{n-1}$)

Stosujemy inne oznaczenia
krok aktualny $y_{n-1}$
następny krok $y_n$

$$ y_n = \sum_{j=1}^k \alpha_jy_{n-j} + h \sum_{j=0}^k \beta_j \cdot f(x_{n-j}, y_{n-j}) $$
Na początku potrzebna jest pewna procedura startowa żeby mieć $k$ punktów do podstawienia
Można w pierwszych $k$ krokach zastosować jakąś z metod jednokrokowych - uwaga na propagację błędu

### Metoda wielokrokowa jawna
$\beta_0 = 0$

### Metoda wielokrokowa niejawna

$$ y_n = \sum_{j=1}^k \alpha_jy_{n-j} + h \sum_{j=1}^k \beta_j \cdot f(x_{n-j}, y_{n-j}) + h \beta_0f(x_n,y_n)$$
$y_n$ pojawia się po obu stronach
równanie nieliniowe względem $y_n$
ma jednoznaczne rozwiązanie dla $h < (L\beta_0)^{-1}$ (dostatecznie mały krok)

## Metody Adamsa
$$ y'(x) = f(x,y(x)) \quad y(a) = y_a \quad x \in [a,b] $$

Równoważne przekształcenie przez całkowanie
Przybliżenie f przez wielomian interpolacyjny

metody niejawne - wielomian dodatkowo oparty na $x_n$

## Błąd aproksymacji
lokalny - błąd powstały w pojedynczym kroku (przy założeniu, że we wszystkich poprzednich krokach mamy dokładne wartości)

rozwinięcie w szereg Taylora - te same wspolczynniki dla funkcji i jej pochodnej

mimo że nie znamy funkcji to można wyliczyć współczynniki c z wzoru na błąd zależne od $\alpha$ i $\beta$ z danej metody

Tak samo definiujemy rząd metody

Dla metod jawnych rząd metody równy k
Dla metdo niejawnych rząd metody od 1 większy od k i dużo lepsze stałe błędu

## Zbieżność i stabilność
Metoda jest stabilna jeśli stabilne jest jej równanie różnicowe z $h=0$

Metoda k-krokowa jest zbieżna wtedy i tylko wtedy gdy jest stabilna i jest co najmniej rzędu pierwszego $c_0=c_1=0$

Warunek stabilności równania - zera wielomianu charakterystycznego mają moduły $\le 1$

W praktyce decydująca jest stabilność metody dla kroku całkowania $> 0$ (stabilność równania różnicowego) - dla różnań nieliniowych nie ma ogólnych metod

Punkt równowagi jest stabilny wttw jeśli liniowee przybliżenie układu równań w tym punkcie jest stabilna

linearyzujemy funkcje prawych stron do $\lambda \cdot y_k$

Metoda wielokrokowa z krokiem $h>0$ jest absolutnie stabilna jeśli równanie jest asymptotycznie stabillne
alfa i beta są dane dla wybranej metoda więc to zależy od iloczynu $h \lambda$ 

Zbiór wartości $h\lambda$ dla których zera wielomianu charakterystycznego mają moduły <1 nazywamy obszarem absolutnej stabilności metody wielokrokowej
Metodę nazywamy absolutnie stabilną w tym obszarze

zbiory a solutnej stabilności leżą w lewej półpłaszczyźnie

Dobrze zdefiniowany kształt obszaru dla metod adamsa, wielkość zależna od q
Trzeba tak dobierać krok, żeby znaleźć się w obszarze

Metoda niejawna 1. rzędu (niejawna Eulera) ma nieskończony obszar 

Dla układu równań - macierz A zamiast lambda
warunek na wartości własne

Dla układu nieliniowego, A reprezentuje przybliżenia liniowe f(x,y)

Warunek konieczny i dostatenczy absolutnej stabilności dla układu równań
$h \lambda_i$ należy do obszaru absolutnej stabilności (wszystkie wartości własne)

## Metody predyktor-korektor
Najpraktyczniejszą metodą wielokrokową byłaby metoda o
możliwie wysokim rzędzie i małej stałej błedu (metody niejawne)
możliwie dużym obszarze absolutnej stabilności (metody niejawne)
możliwie małej ilości obliczeń na iterację (metody jawne)

stosujemy oba rodzaje metod (łącząc dobre cechy każdej z nich)

predykcja (metoda jawna)
ewaluacja
korekcja - iteracja prosta (metoda niejawna)
ewaluacja

Różne warianty - można robić więcej iteracji korektora dla uzyskania dokładniejszego rozwiązania

W praktyce dla dobrze uwarunkowanych równań wystarcza 1 iteracja korektora

### Rząd metod predyktor-korektor
jeśli rząd predyktora nie mniejsza - taki sam rząd jak dla metody niejawnej
wystarczy jedna iteracja korektora żeby poprawić rząd
predyktor daje zysk postaci dobrego punktu startowego

jeśli rząd predyktora mniejszy to trzeba wykonać więcej iteracji korektora dla uzyskania tej samej dokładności

## Oszacowanie błędu aproksymacji
Na podstawie części głównej błedu - pierwszy niezerowy wyraz w rowinięciu w szereg Taylora
pochodną możemy szacować iloczynem różnicowym

## Zmienny krok całkowania
Efektywne implementacje metod wielokrokowych PK stosują zmienną, automatycznie dobieraną długość krok całkowania

W każdym kroku szacujemy błąd aproksymacji
wyznaczamy współczynnik korekty kroku
jeśli ...

punkty nie są równomiernie rozłożone więc trzeba interpolować dla obliczeń

Do sterowania dokładnością obliczeń w metodach PK sotsuje się również zmiany rzędu
stosuje się wersje wzorów z nierównoodległymi punktami
z zastosowaniem samostartu

## Równania źle uwarunkowane
iloraz największej i najmniejszej wartości własnej znacznie większe od 1
Należy stosować metody numeryczne o bardzo dużych obszarach stabilności absolutnej

dla niejawnej metody eulera absolutna stabilność w całej lewej półpłaszczyźnie

Na jej podstawie może skonstruować metody wielokrokowe o większej krokowości  irzeðzie i o dużych obszarach absolutnej stabilności - metody BDF

metody BDF jawne i niejawne, ustalone współczynniki

korektor trzeba iterować do zbieżności (np. algorytmem Newtona)
