# Konsultacje 2025-01-24

Można notatki
3 do 4 zadań
Raczej będą wydrukowane rysunki i coś na nich pozaznaczać i napisać krótkie uzasadnienie

## Materiał
To co omawiane po kolosie 1
Termin poprawkowy w 1 tygodniu sesji (pn/wt/śr)

* Algorytm ewolucyjny z krzyżowaniem
* Ewolucja różnicowa
* EDA
* Rój cząstek
* Ograniczenia
* Hybrydyzacja z metodami optymalizacji lokalnej
* Wyprowadzenie funkcji gęstości rozkładu próbkowania algorytmu ewolucyjnego

Być może ograniczenia w innym kontekście (symulowanego wyżarzania)

## Zadanief
Algorytm ewolucyjny z krzyżowaniem, naprawa

![[Pasted image 20250124180803.png]]

nie wiemy jaka jest funkcja celu

a - kolejna populacja skupiona wokół tych skupisk punktów co widać
głównie kropki położone nie dalej niż 1

b - wszytkie są rezultatem krzyżowania i mutacji
krzyżowanie w parach albo z tego samego skupiska albo z różnych skupisk
waga 1/2 - punkt krzyżowany będzie na środku pomiędzy skupiskami
3 chmury punktów
gdzie będzie więcej punktów - zależałoby od funkcji celu ale nie znamy

c - krzyżowanie równomierne
chmury punktów mogą być na wierzchołkach prostokąta rozpiętego przez 2 chmury punktów
gęstość chmur zależy od wartości funkcji celu

d- nie ma krzyżowania, ograniczenia kostkowe -3,3, uwzględnienie ograniczeń przez rzutowanie widoczne dla algorytmu (lamarcowskie)
będą punkty leżące dokładnie na granicach, nie będzie żadnego punktu za granicą

jak jest reinicjacja i ograniczenia kostkowe to reinicjuje się z rozkładem jednostajnym w kostce

## Zadanie
Ewolucja różnicowa

![[Pasted image 20250124182233.png]]
a - krzyżowanie nie zachodzi (CR=1)

skupiska te co są - wektor różnicowy z jednego skupiska
2 cienie - na linii pomiędzy skupiskami w 0.2 i 0.8 odległości
2 cienie na zewnątrz - na linii łączącej skupiska, 0.8 odległości pomiędzy skupiskami ale na zewnątrz

prawdopodobienstwo 1/2 że punkt zostanie w chmurce (2 skupiska)
prawdopodobieństwo 1/2 że punkt wyrzucony do jednego z 4 cieni (4 skupiska) - 2 razy mniej gęste 

b CR=0.5
mutant krzyżowany z punktem poddawanym mutacji

takie skupiska jak ostatnio + dodatkowe wyznaczone przez "krzyżykowanie" ale pamiętać że krzyżowany jest mutant z punktem przed mutacją

w sumie grup
2 oryginalne skupiska
![[Pasted image 20250124183551.png]]

c CR=1 (wyłączone krzyżowanie) i uwzględnienie ograniczeń kostkowych przez odbijanie

jak w punkcie a ale te cienie ktore wychodzą poza kostkę odbite do środka

w DE naprawa po krzyżowaniu

## Zadanie
![[Pasted image 20250124184408.png]]![[Pasted image 20250124184457.png]]

Krzyżowanie może doprowadzić do Xa - CR powinien być 0<CR<1, najlepiej 1/2
F ok 1 pozwoli od razu wstrzelić się do Xa, inaczej punkt po krzyżowaniu może zostać odrzucony bo bedzie mial niższą jakość

wylądowanie na zboczu może nic nie dać bo punkt po krzyżowaniu musiałby być lepszy od tego przed mutacją

może być bardzo duże F - wektor między punktami z jednego skupiska akurat tak się ułoży że przeskoczy do X - mniej prawdopodobne ale możliwe

## Zadanie
![[Pasted image 20250124190503.png]]

Tabela

q wyliczamy - tu są liczby z dupy żeby zademonstrować co dalej

$p_s$ - ze wzoru na selekcję turniejową

| i   | $x_i$ | $q_i$ | $p_s$ |
| --- | ----- | ----- | ----- |
| 1   | 2     | 5     | 7/25  |
| 2   | 3     | 6     | 9/25  |
| 3   | 6     | 4     | 5/25  |
| 4   | 6     | 4     | 3/25  |
| 5   | 7     | 2     | 1/25  |
|     |       |       |       |
|     |       |       |       |

dla punktów w położeniu na osi liczbowej (redukujemy i=3 z i=4)

| $x_i$ | $p_s$ |
| ----- | ----- |
| 2     | 7/25  |
| 3     | 9/25  |
| 6     | 8/25  |
| 7     | 1/25  |

z mutacji z rozkładem jednostajnym wychodzą prostokąty z wysokością przeskalowaną przez $p_s$
prostokąt nad każdym punktem z populacji bazowej

sumujemy prostokąty ze sobą

Pamietac wzory (numeracja od 1)

![[Pasted image 20250124192401.png]]


## Zadanie
![[Pasted image 20250124193133.png]]
w chmurze prawdopodobnie są 2 optima lokalne

b - odbijanie
c - wariant z funkcją kary, reszta jest lamarcowska
d to rzutowanie bo jest ramka
e to zawijanie - są dodatkowe 2 zagęszczenia punktów tam gdzie wcześniej ich nie było


## Zadanie

![[Pasted image 20250124193535.png]]
Trzeba by zamienić na wykres schodkowy i porównać dystrybuanty empiryczne

jeśli jedna krzywa jest cała nad drugą to wiadomo ktora lepsza a jak sie przecinaja to nie wiadomo

![[Pasted image 20250128161738.png]]

## Zadanie
![[Pasted image 20250124193800.png]]zacznie q w przedziale -36, -25 a dojdzie do poziomu troche mniejszego niż 0 bo mowimy o średniej a punkty będą rozproszone

b) dla pc=0
na końcu będzie jeszcze niżej niż dla pc=1/2
algorytm może robić większe kroki bo populacja nie jest ściskana
na początku lepiej, na końcu gorzej

c) std mutacji 0.1 (10 razy mniejsze)
wolniej idzie do 0 ale dochodzi bardzo blisko 0

e) turniej z 5 elementami w szrankach
bardziej zachłanne działanie - idzie szybciej
dojdzie troche wyżej niż bazowy

d) selekcja elitarna
szybszy wzrost
średnia troche bliżej 0 niż bazowo
podobny przebieg do e)

f) populacja zawiera 10 elementów
bardziej poszarpana krzywa
wolniej idzie w góre względem numeru iteracji
dochodzi niżej

## Jeszcze
Co by było gdyby w roju cząstek wszystkie punkty miały taką samą wartość początkową
Co jak się sprzęgnie z metodą optymalizajci lokalnej (lamarcowskie/darwinowskie)

![[Pasted image 20250128225002.png]]
![[Pasted image 20250128225028.png]]![[Pasted image 20250128225136.png]]