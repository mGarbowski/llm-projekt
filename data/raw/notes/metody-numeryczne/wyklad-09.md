# Równania różniczkowe zwyczajne (2024-12-19)
Układ m równań różniczkowych zwyczajnych z warunkami początkowymi

y - funkcje rozwiązań
x - zmienna niezależna (zazwyczaj czas)
warunek na początku przedziału $x \in [a,b]$
$y_i(a) = y_{ia}$

$$ dy_i/dx = f_i(x, y_1, \ldots, y_m) $$

## Twierdzenie o jednoznaczności rozwiązania
Jeśli funkcje f_i są ciągłe na zbiorze D = ...
funkcje f_i spełniają warunek Lipschitza względem y
dla każdej wartości zmiennej niezależnej, 2 dowolne różne wartości y odległość funkcji jest mniejsza niż stała razy odległość argumentów y

każda funkcja różniczkowalna spełnia warunek Lipschitza
są funkcje, które nie są różniczkowalne, a spełniają warunek (przedziałami różniczkowalne i punkty ostrzowe)

dla każdych warunków początkowych istnieje dokładnie jedna funkcja rozwiązania y(x) ciągła, różniczkowalna i spełniająca $y'(x) = f(x,y(x)), y(a) = y_a$
też ciągła względem zaburzeń argumentów

## Metody numeryczne różnicowe
Przybliżona wartość rozwiązania obliczana jest w kolejnych punktach przedziału x_n

Krok $h_i=x_{i+1}-x_i$

Metody jednokrokowe
Metody wielokrokowe

Metoda jest zbieżna jeśli dla każdego układu równań mającego jednoznaczne rozwiązanie y(x) zachodzi $\lim_{h \rightarrow 0}y(x_n;h) \rightarrow y(x)$

## Metoda Eulera
Przybliżenie funkcji szeregiem Taylora z czynnikiem liniowym
Najprostsza metoda zbieżna
Niezalecana poza specyficznymi problemami (symulacje)

## Zmodyfikowana metoda Eulera
Metoda punktu środkowego
Jak metoda Eulera tylko że bierzemy punkty na środkach odcinków

$$ y_{n+1} = y_n + hf(x_n + 1/2h; y_n + 1/2hf(x_n,y_n)) $$

O rząd wielkości dokładniejsza a wymaga tylko 2 razy większego nakładu obliczeń
Wartość pochodnej na środku przedziału jest lepszym przybliżeniem średniej na przedziale niż wartość na krańcu przedziału

### Przykład
Model epidemii Kermacka-McKendricka
Trzecie równanie wynika z drugiego

## Metoda Heuna
Średnia arytmetyczna pochodnej na początku i na końcu przedziału

## Metody jednokrokowe
Ogólna postać ...

informacja dotycząca tylko przedziału

Funkcja $\Phi$ - iloraz różnicowy

Dla zerowego kroku równa funkcji - warunek konieczny i dostateczny zbieżności metody jednokrokowej

## Błąd aproksymacji
Można sformułować nieskończenie wiele metod jednokrokowych (różnych funkcji $\Phi_f$)
Do porównywania służy błąd aproksymacji

są 2 błędy
błąd metody - metoda wykorzystuje przybliżenia
błędy numeryczne

Błąd aproksymacji (lokalny) - błąd powstały w jednym kroku
Przy założeniu, że w bieżącym funkcje jest zerowy błąd
$$ r_n(h) = y(x_n+h) - y_{n+1} $$

Nie znamy funkcji błędu bo nie znamy dokładnego rozwiązania
rozwijamy funkcję błędy w szereg Taylora, metoda jest rzędu p jeśli dla dowolnego rozwiązywanego układu
pierwszych p pochodnych błędu jest zerowych
Tym dokładniejsza metoda im wyższy rząd
Część główna błędu aproksymacji - pierwszy niezerwowy wyraz w szeregu Taylora

Metoda Eulera jest rzędu pierwszego - pierwszy niezerowy wyraz w rozwinięciu z drugą pochodną

## Metody Runge-Kutty (RK)
Najpopularniejsza jendokrokowa

Maksymalny możliwy rząd metody równy
m dla m=1,2,3,4
m-1 dla 5,6,7
$\le m-2$ dla m $\ge 8$
W praktyce korzysta się z m do 4

Metoda RK3, RK4

### Przykład
Dla wielu funkcji

...

Chcemy dostać rozwiązanie, które dla wszystkich punktóœ ma jednakową dokładność
jeśli funkcja jest szybciej zmienna to krok powinien być krótszy 
Powinien istnieć mechanizm adaptacji długości kroku, potrzebujemy do tego oszacowania dokładności

## Szacowanie błędu metodą podwójnego kroku
Startujemy 2 razy z punktu x_n

liczymy metodą z krokiem h i 2 razy z krokami h/2
z porównania tych 2 wartości szacujemy błąd

Przy jednym kroku rozwiązanie to wartość + błąd

Przy dwóch krokach połówkowych
Zakładamy że drugi krok połówkowy będzie miał taki sam błąd - mnożenie przez 2 we wzrorze
nie znamy funkcji błędu tylko ją wyliczamy
mamy oszacowanie części głównej błędu

Bierzemy to rozwiązanie które jest bardziej dokładne - wyznaczone z dwóch kroków połówkowych

## Metody Runge-Kutty-Fehlberga (RKF)
Inna metoda szacowania dokładności
Wykonanie po 1 kroku 2 metodami
m-etapowa rzędu p i m+1-etapowa rzędu p+1

Wartości k pokrywają się dla m pierwszych wyrazów

Oszacowanie błędu jako różnica punktów otrzmanych obiema metodami

Współczynniki dla metod podaje się w tablicy Butchera - współczynniki $c_i, a_{ij}, w_i$

## Zmiana długości kroku
Dla każdej metody rzędu p ...

zmiana kroku na $\alpha h$
$\gamma$ się nie zmieni
$\delta_n(\alpha h) = \alpha^{p+1} \cdot \delta_n(h)$

W każdym punkcie chcemy mieć zadaną dokładność $\epsilon$
wzór na współczynnik korekty kroku
dla dowolnej metody z oszacowaniem błedu $\delta_n(h)$

Oszacowanie nie jest dokładne, powinniśmy założyć że oszacowanie jest z niedomiarem (pesymistycznie)
Wprowadza się współczynnik bezpieczeństwa $s$
np. rzędu 0.9 dla metody RKF45

Funkcja może przyjmować bardzo zróżnicowane wartości na badanym przedziale, zadany stały epsilon może być za mały przy maksimum, lepiej zachować proporcję

Parametry dokładności (parametry użytkownika)
dokładność względna
dokładność bezwzględna
$\epsilon = |y_n| \cdot \epsilon_w + \epsilon_b$
np. oba równe $10^{-6}$

będzie działać i przy dużych wartościach i przy przechodzeniu przez 0

Dla układu m równań długość kroku określa równanie z największym błędem
szacujemy błąd dla każdego z równań

## Schemat realizacji
beta - współczynnik płynności działania metody (heurystyczny) - opcjonalne
krok minimalny - to nie jest krytyczne