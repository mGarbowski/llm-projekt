# Powtórzenie do kolokwium 2

## Inżynieria oprogramowania

### Stos i ramki wywołania funkcji
Stos realizuje koncepcję LIFO (Last In - First Out)

Na stosie można odkładać tymczasowo dane w celu zwolnienia rejestrów na potrzeby obliczeń.

Sposób przekazywania argumentów do funkcji jest określony na poziomie kompilacji.

Wynik funkcji może być zwracany przez stos lub przez rejestry procesora.

Przechowywanie w ramce stosu jednocześnie danych, adresu bazowego i adresu instrukcji powoduje, że program może zakłócić swoje działanie przez modyfikację danych na stosie.

Attak buffer overflow polega na nadpisaniu danymi kopiowanymi do zmiennych lokalnych na ramce stosu adresu powrotnego wywołania funkcji na wartość podaną przez atakującego.

Zmienne pozostają na stosie po powrocie z wywołania tak długo jak nie zostaną nadpisane (zmienia się tylko wartość wskaźnika stosu) - do wykorzystania przy buffer overflow.


### Skoki warunkowe
Procesor wykorzystuje ALU do porównywania wartości przez odjęcie i określenie flag - wynik ujemny, wynik równy 0. Operacja skoku warunkowego wykorzystuje flagi ALU ustawione po poprzedniej operacji.

Skoki są związane np. z instrukcjami warunkowymi - wtedy nie ma potrzeby zapisywania stanu przetwarzania na stosie.

### Przekazywanie argumentów
Przekazanie mutowalnego obiektu przez referencję do funkcji/metody spowoduje, że modyfikacje pozostaną w tym obiekcie i będą dalej widoczne po powrocie do funkcji wywołującej.


### Niemutowalność w Pythonie
Po przekazaniu przez referencję niemutowalnego obiektu jako argument funkcji/metody

* Dokonane na nim zmiany nie będą widoczne z poziomu funkcji wywołującej (po powrocie)
* Na zewnątrz będą widoczne zmiany na zagnieżdżonych obiektach mutowalnych
* Przy próbie modyfikacji automatycznie wykona się płytka kopia


### Obsługa wyjątków
Wyjątki służą do kontroli sterowania przepływem w sytuacjach wyjątkowych w trakcie wykonywania programu.

Ułatwiają organizowanie obsługi w określonych punktach przetwarzania.

Umożliwiają budowanie hierarchicznego systemu obsługi sytuacji wyjątkowych i obsługiwanie ich na odpowiednim (z punktu widzenia programisty) poziomie zagnieżdżenia.


### Debugger
Debugger pozwala:
* analizwoać zagnieżdżenia wywołań funkcji i metod na stosie
* sprawdzać wartości zmiennych w kolejnych powtórzeniach pętli


### Statyczne typowanie zmiennych
Umożliwia kontrolę poprawności semantycznej na poziomie kompilacji.

Ogranicza możliwość pojawianie się błędów semantycznych w trakcie wykonywania programu.


### Kopia płytka
Wykonanie kopii płytkiej na obiekcie z wewnętrzną kolekcją innych obiektów spowoduje, że obiekt wewnętrznej kolekcji zostanie sklonowany, ale jej elementy nie. Obiekty przechowywane w kolekcji kopii obiektu to te same co w kolekcji oryginalnego obiektu.


## Algorytmy i struktury danych

### Struktury danych
Słownik, tablica hashująca są dobre do danych, do których odwołuje się po ich konkretnym atrybucie (np. ID, numer PESEL).


### Złożoność obliczeniowa O()
Od najlepszej

* O(1)
* O(log(n))
* O(n)
* O(nlog(n))
* O(n^2)
* O(2^n)
* O(n!)

Do O(nlog(n)) uznaje się za efektywne.

Złożoność co do zasobów i co do czasu to 2 oddzielne rzeczy.

Złożoność O(n^2) nie oznacza, że zawsze dla zbioru bardziej licznego zajmie więcej czasu - może zależeć np. od szczególnych wartości danych.


### Algorytmy
Kiedy ograniczenia zasobów (czasu, sprzętu) nie pozwalają na uzyskanie dokładnego/najlepszego wyniku można wykorzystać

* Algorytmy heurystyczne
* Algorytmy ewolucyjne
* Algorytmy probabilistyczne
* Algorytmy zachłanne
* Algorytmy rekurencyjne


## Automaty

### Automat zupełny
Każdy ze stanów ma zdefiniowane przejścia dla każdego symbolu alfabetu.

Dodanie stanów tak, żeby automat był zupełny, nawet jeśli nie są ściśle konieczne, żeby rozpoznać daną sekwencje, umożliwia rozbudowaną diagnostykę błędnych sekwencji (oceniając po końcowym stanie automatu).

Stan może się zapętlać - przejście na ten sam stan.


### Automat deterministyczny
W automacie deterministycznym nie mogą występować przejścia spontaniczne - dla danego stanu, każdemu symbolowi alfabetu może być przypisane conajwyżej 1 przejście.

Do stanu może dochodzić wiele przejść o tym samym symbolu (z różnych stanów).

Nie musi mieć określonych wszystkich przejść


### Automat niedeterministyczny
Może mieć przejścia spontaniczne - z jednego stanu kilka dl atego smaego symbolu alfabetu.


## Lingwistyka

### Maszyna Turinga
[Symulator](https://turingmachine.io)

Maszyna rozpoznaje słowo z języka $L(\{a^nb^nc^n: n>= 1\})$ i wpisiuje 1 za ostatnim 'c' w słowie. W trakcie sprawdzania podmienia 'a' na 'A' itd.

```
input: 'aaabbbccc'
blank: ' '
start state: qA
table:
  qA:
    'a': {write: A, R: qB}
    'B': {R: scan}
  qB:
    ['a', 'B']: R
    'b': {write: B, R: qC}
  qC:
    ['b', 'C']: R
    'c': {write: 'C', L: back}
  back:
    ['a', 'B', 'b', 'C']: L
    'A': {R: qA}
  scan:
    ['B', 'C']: R
    ' ': {write: '1', R: accept}
  accept:
```

Maszyna sprawdzająca podzielność liczby dziesiętnej przez 3 (ze sprytnym wykorzystaniem przystawania modulo 3)
```
input: '1524'
blank: ' '
start state: q0
table:
  q0:
    [0,3,6,9]: R
    [1,4,7]: {R: q1}
    [2,5,8]: {R: q2}
    ' ': {R: accept}
  q1:
    [0,3,6,9]: R
    [1,4,7]: {R: q2}
    [2,5,8]: {R: q0}
  q2:
    [0,3,6,9]: R
    [1,4,7]: {R: q0}
    [2,5,8]: {R: q1}
  accept:
```

### Hierarchia języków
![Hierarchia Chomsky'ego](./obrazy/https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Chomsky-hierarchy.svg/1024px-Chomsky-hierarchy.svg.png)

| Typ języka                 | Automat                     |
| -------------------------- | --------------------------- |
| Rekurencyjnie przeliczalny | Maszyna Turinga             |
| Kontekstowy                | Automat liniowo ograniczony |
| Bezkontekstowy             | Automat ze stosem           |
| Regularny                  | Automat skończony           |

Języki regularne dają się wyrazić przez wyrażenia regularne - równoważnie z automatami skończonymi.

Automat nie musi być zupełny, żeby rozpoznawać język regularny.

Języki regularne są podzbiorem jezyków bezkontekstowych itd. to oznacza, że też dają się rozpoznać np. przez maszynę Turinga.


### Wyrażenia regularne
Sekwencje rozpoznane przez wyrażenie `[a-c]?.*d`

(0 lub 1 z liter {a,b,c}, dowolna liczba dowolnych znaków, d)

* cbbad
* adddad
* dbbd


### Określenie łączności i priorytetów
```ebnf
hash_statement = ("a", "#", hash_statement) | "a";
at_statement = hash_statement, {"@", hash_statement};
```

przykładowy ciąg `a@a@a#a#`


```
     @                   @
    / \                 / \
   @   #               a   @
  / \ / \                 / \
 a  a a  #               a   #
        / \                 / \
       a   a               a   #
                              / \
                             a   a
```

* `#` ma wyższy priorytet od `@`
  * jest wyprowadzony z `at_statement`
  * na drzewie wyprowadzenia jest zagnieżdżony
  * bardziej zagnieżdżona operacja musi zostać wykonana przed podstawieniem
* Łączność `#` jest prawostronna
  * na drzewie wyprowadzenia kolejne zagnieżdżenia są zawsze w prawej gałęzi
  * odwołanie rekurencyjne po prawej stronie operatora w definicji
* Łączności `@` nie da się określić
  * iteracyjna definicja `at_statement` (z powtórzeniem w `{...}`)
  * można zbudować różne drzewa wyprowadzeń dla tego ciągu
  * przy konstrukcji drzewa dla przykładowego ciągu równie dobrze w korzeniu może być lewy co prawy `@`


### Określanie wyrażenia regularnego na podstawie grafu
* Rozgałęzienie - alternatywa `|`, otwarcie nawiasu
* Zapętlenie - dowolna liczba powtórzń `*`
* Złączenie rozgałęzienie - koniec alternatywy, domknięcie nawiasu
* Trzeba określić priorytety za pomocą nawiasów, na podstawie hierarchii zagnieżdżeń
