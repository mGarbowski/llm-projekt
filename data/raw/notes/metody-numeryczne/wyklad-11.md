# Różniczkowanie i całkowanie numeryczne
Formuły numerycznej aproksymacji pochodnych są istotne dla wielu algorytmów obliczeniowych
np. wyznaczanie prędkości i przyspieszenia dla znanych funkcji położenia
wyznaczanie pochodnych w algorytmach optymalizacji funkcji
...

## Aproksymacja pochodnych
Iloraz różnicowy wsteczny (znamy przebieg tylko do chwili bieżącej)
iloraz różnicowy progresywny
iloraz różnicowy centralny (lepszy od progresywnego jeśli już znamy przebieg do przodu)

Podstawowym błędem jest błąd metody (niedokładność przybliżenia pochodnej przez wzór), a dopiero potem błędy numeryczne

### Błąd metody aproksymacji pochodnej
Różnicę wsteczną rozwijamy w szereg Taylora do 2. stopnia

Błąd $f^{(2)}(\alpha)h/2!$

Dla różnicy centralnej - rozwinięcie w szereg Taylora do 3 stopnia i z krokiem +h i -h
Odejmowanie równań stronami i przekształcenie pozwala wyznaczyć błąd metody jako

$$
\frac{f^{(3)}(\alpha_+) + f^{(3)}(\alpha_-)}{12}h^2
$$
o rząd dokładniejsze przybliżenie

Bardziej dokładny bo opiera się na trójpunktowym przybliżeniu

### Błędy numeryczne
Istotne przy małych wielkościach kroku, kiedy błąd metody jest mniejszy
przyjmujemy że krok jest potęgą dwójki i nie wprowadza błędu - łatwiejsza analiza

Proporcjonalny do 1/h - im mniejsze h (bardziej dokładna metoda) tym większe błędy numeryczne
istnieje optymalna wartość h minimalizująca łączny błąd

optymalna wartość kroku jest proporcjonalna do $\sqrt{Eps}$ - dokładności obliczania $f(x)$

Inżynierska reguła - optymalny krok rzędu $\sqrt{Eps}$

## Aproksymacja pochodnej drugiego rzędu
Obliczamy korzystając z definicji rekurencyjnej

Aproksymacja oparta na różnicach wstecznych

Aproksymacja oparta na różnicach centralnych
wygodniej wystartować z punktów x+h/2 i x-h/2
po uproszczeniu wzoru 

$$ \frac{f(x+h)-2f(x)+f(x-h)}{h^2} $$
## Aproksymacja pochodnej oparta na 3 punktach
Wykorzystuje się więcej punktów i pochodne wielomianu interpolacyjnego opartego na tych punktach
np. wielomian interpolacyjny lagrange'a po przekształceniu wzorów wychodzi wzór ...


błąd szacujemy przez rozwiniecie w szereg taylora do 3 stopnia
dokładność jak aproksymacja różnicą centralną

bardzo ważne w praktyce, a rzadko sie pojawia w literaturze
ważne do aproksymacji z pomiarów

Ostrożnie przy bieżącym numerycznym wyznaczaniu pochodnych sygnałów mierzonych - aproksymacja pochodnych jest źle uwarunkowana - np. w regulatorach PID włącza się komponent różniczkujący

## Całkowanie numeryczne
Mały problem z błędami, większy problem z efektywnością
policzenie całki na przedziale do dużo większy nakład obliczeń niż pochodnej w jednym punkcie

Obliczanie jako średnia ważona wartości w n+1 punktach przedziału $[a,b]$

kwadratura liniowa, a $x_i$ to węzły kwadratury

Kwadratura jest rzędu p jeśli błąd jest = 0 dla wszystkich wielomianów stopnia < p i istnieje wielomian stopnia p dla ktorego jest różna od 0

Metoda wyznaczania kwadratur
utworzenie funkcji interpolującej wartości f(x_i) w węzłach i ...

### Kwadratura Newtona-Cotesa
Węzły równoodległe, wielomiany interpolacyjne Lagrange'a

Regułą trapezów - liniowa, nie przybliży dokłądnie wielomianu stopnia 2

Reguła Simpsona (reguła parabol) - rzędu 4

Kwadratury Newtona-Cotesa oparte na n węzłah są rzędu n+1 dla nieparzystych n, n+2 dla parzystych n

Tabela współczynników

### Kwadratury złożone
Dla szerokich przedziałów całkowania
Dzielimy przedział na równe podprzedziały
sumujemy wartości z podprzedziałów

liniowa
w każdym punkcie poza krańcami, wartość funkcji jest liczona 2 razy

### Złożona kwadratura Simpsona
Na każdym podwójnym podprzedziale stosujemy wzór simpsona

punkty nieparzyste mają współczynnik 4, punkty parzyste mają współczynnik (1+1) (krańcowe 1)

### Praktyczne obliczanie kwadratur złożonych
Można określić dokładność przez oszacowanie reszty - trzeba wyznaczyć śrendią wartość którejś pochodnej (zależnie od metody)

można rekurencyjnie obliczać ciąg kwadratur dla rosnącej liczby punktów
szczególnie jeśli dla obliczania ciągu o większej liczbie punktów można było wykorzystać wcześniejsze punkty

### Rekurencyjne reguły kwadratur złożonych
W kolejnej iteracji dodajemy punkty pośrednie

dla reguły trapezów - 2 razy zmniejszony krok
poprzednia wartość dzielona przez 2 + nowe punkty pośrednie

Dla kwadratury Simpsona
w przekształceniu - rozbita suma z wagą 4
nowe punkty pośrednie będą wszystkie nieparzyste
wszystkie stare będą parzyste

dla kwadratury simpsona przybliżenie jest znacnzie lepsze, a nakład obliczeń taki sam

### Kwadratury złożone adaptacyjne
Funkcja może mieć różną zmienność na różnych odcinkach
Wykorzystują nierównomiernie rozłożone węzły kwadratury
w trakcie całkowania dzielimy przedział na podprzedziały i sprawdzamy czy już mamy wymaganą dokładność

w matlabie - funkcja `quad`

materiał na kolokwium 2 - interpolacja, aproksymacja, róœnania rozniczkowe i to co dzisiaj

zadania z interpolacji i aproksymacji na koncach rozdzialow
rownan rozniczkowych nie bedzie do liczenia na papierze - to bylo n aprojekcie
moze byc pytanie teoretyczne o rząd i stabilność metody i podobnie z dzisiejszego tematu

za 2 tyg termin poprawkowy

takie notatki jak na pierwsze kolokwium - 1 strona a4