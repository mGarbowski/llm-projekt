# Lingwistyka matematyczna


## Translacja w C
Jednostka translacyjna
* plik źródłowy
* preprocesor - dołącza pliki nagłówkowe
* kompilator
  * dokonuje optymalizacji tylko w obrębie jednostki translacyjnej - zna jej kontekst
  * generuje plik obiektowy (obj)

Konsolidacja (linker)
* dołącza statyczne biblioteki
* generuje pliki wykonywalne (lib, dll, exe)

Dołączanie zewnętrznych bibliotek
* statyczne - przed wygenerowaniem kodu wykonywalnego
* dynamiczne - w trakcie wykonywania kodu, nie są znane w trakcie kompilacji, tylko na podstawie plików nagłówkowych

Kompilator dekomponuje problem tłumaczenia kodu źródłowego na instrukcje maszynowe
* warstwa leksykalna - wydzielenie wyrazów
* warstwa składniowa
  * sprawdzenie czy wyrazy poprawnie łączą się w większe struktury
  * stworzenie drzewa rozbioru składniowego


## Translator
Translator przetwarza kod źródłowy do innej postaci

* Assembler - z kodu assemblerowego do postaci binarnej
* Kompilator - z kodu źródłowego do postaci binarnej
* Kompilator skrośny (cross-compiler) - z kodu źródłowego do postaci binarnej innej platformy
* Transkompilator - z kodu w jednym języku na drugi
* Interpreter:
  * wykonuje bezpośrednio kod źródłowy po przetworzeniu do wewnętrznej reprezentacji
  * maszyna wirtualna wykonująca kod pośredni (JVM)
  * JIT (just-in-time compilation) - kod pośredni tłumaczony przed wykonaniem do instrukcji natywnych danej platformy


## Konsolidator (linker)
Dołącza kod bibliotek i scala kod powstały z wielu plików podczas kompilacji.
* Statycznie - podczas kompilacji
* Dynamicznie - w trakcie wykonywania programu


## Kompilacja vs Interpretacja
Oba podejścia mają swoje wady i zalety, wpływają na:

* Przenośność kodu między platformami
* Sposób zarządzania pamięcią
* Statyczne / dynamiczne typowanie
* Wydajność kodu
* Możliwość dbugowania

Zastosowanie pośredniego kodu (np. Java bytecode) pozwala na wykonanie tego samego kodu na różnych platformach ale kosztem wydajności.


## Gramatyka
$$G=<T, N, P, S>$$

* T - zbiór symboli terminalnych - alfabet, skończony zbiór symboli
* N - zbiór symboli nieterminalnych (pomocniczych) - używane w produkcjach
* P - zbiór produkcji - reguły generowania poprawnych słów / zdań
* S - symbol główny (startowy) $S \in N$

Opisuje jak przy pomocy skończonej liczby reguł wyrazić zasady
* generowania poprawnych (składniowo) sekwencji
* rozpoznawania czy dana sekwencja jest poprawna (składniowo)

Składnia - reguły budowania poprawnych sekwencji, opisuje się formalnie.

Semantyka - reguły określające znaczenie poprawnych sekwencji. Nie ma formalnego sposobu no opis semantyki, pozostaje nieformalny opis w języku naturalnym.

Przetwarzanie (dowolne) - przekształcanie sekwencji symboli w nowe sekwencje symboli, rządzi się regułami lingwistyki matematycznej. Przetwarzanie jest ciągiem kroków, sekwencja zdarzeń jest językiem przetwarzania.

Język - to co się da wyprowadzić w dowolnej liczbie kroków od symbolu startowego - zbiór wszystkich zdań. Język generowany gramatyką $G$ - oznaczenie $L(G)$

Ciąg pusty - ε (oznaczenie)

Generowanie - przejście od symbolu startowego do poprawnego zdania wykorzystując produkcje

Rozbiór (parsing) - sprawdzenie czy zdanie jest poprwane składniowo. Przejście od zdania do symbolu startowego (aksjomatu) - odwrotność generowania


### Gramatyka wyrażeń algebraicznych
G = <{a, +, *, (, )}, {A, B, S}, P, S>

P = {S -> S+A | A, A -> A*B | B, B -> (S) | a}

Wyrazy w danej gramatyce otrzymuje się przez podstawianie zgodnie z produkcjami, zaczynając od symbolu startowego

S -> S+A -> A+A -> B+A -> a+A -> a+A\*B -> a+B\*B -> a+a\*B -> a+a\*a


## Niejednoznaczność gramatyk
Różne ciągi produkcji mogą dać w rezultacie ten sam wyraz ale dają różne drzewa wyprowadzeń. Mogą dawać inne rezultaty.

Np. 1+2\*3 może oznaczać (1+2)\*3 albo 1+(2*3)


## Backus-Naur Form
Notacja BNF - spsoób formalnego opisu produkcji.

```bnf
<Wyrażenie> ::= <Składnik> | <Wyrażenie> + <Składnik> | <Wyrażenie> - <Składnik> ;
<Skladnik> ::= <Czynnik> | <Składnik> * <Czynnik> ;
<Czynnik> ::= ( <Wyrażenie> ) | x | 0 | 1 ;
```

* Oparty na rekursji
* Wprowadza hierarchię
* Nie ma iteracji
* Nie ma możliwości grupowania symboli wewnątrz wyrażenia
* Rozwłekła
* Dużo specjalnych symboli
* Prosta konstrukcja drzewa rozbioru

Rekurencyjna definicja wyrażenia daje nieskończony język 

`<Skladnik> ::= <Czynnik> | <Składnik> * <Czynnik> ;`


## Extended Backus-Naur Form
* Standard ISO/IEC 14977
* Symbole terminalne w cudzosłowie
* Symbole w sekwencji oddzielone przecinkami
* Reguła zakończona średnikiem
* Stosuje się iteracyjne definicje zamiast rekursywnych

| Znaczenie                | Zapis               |
| ------------------------ | ------------------- |
| definicja                | =                   |
| złączenie                | ,                   |
| zakończenie              | ;                   |
| alternatywa              | `\|`                |
| zawartość opcjonalna     | `[...]`             |
| powtórzenie              | `{...}`             |
| tekst dosłowny (literał) | `"..."` lub `'...'` |
| grupowanie               | `(...)`             |
| komentarz                | `(*...*)`           |
| wyrażenie specjalne      | `?...?`             |
| wyjątek                  | `-`                 |
| powtórzenie              | `*`                 |


```ebnf
(* poziom składni *)
expression = term, {"+", expression};
term = factor, {"*", term};
factor = constant | variable | "(", expression, ")";

(* poziom leksyki *)
variable = "x" | "y" | "z";
constant = digit, {digit};
digit = "0" | "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9";
```

### Diagramy składniowe (railroad diagrams)
![Diagram składniowy z json.org](./obrazy/https://www.json.org/img/object.png)


## Wyrażenia regularne
Wyrażenia regularne pozwalają na rozpoznawanie wzorców i analizę leksykalną.

|                                       |          |
| ------------------------------------- | -------- |
| Alfabet                               | `{0, 1}` |
| Łańcuch – skończona sekwencja symboli | `0 0 1`  |
| Długość łańcucha `x`                  | `\|x\|`  |
| Pusty łańcuch                         | `ε`      |
| Konkatenacja `x` i `y`                | `xy`     |
| Łańcuch `x` powtórzony i-krotnie      | `x^i`    |
| Dowolna ilość (Kleene star)           | `*`      |
| Alternatywa                           | `\|`     |
| Grupowanie wyrażeń                    | `(...)`  |

### Priorytety
* `*` powtórzenie - najwyższy
* iloczyn (konkatenacja)
* `|` suma - najniższy

### Aksjomaty
* `r|s` = `s|r` przemienność `|`
* `r|(s|t)` = `(r|s)|t` łączność `|`
* `r(st)` = `(rs)t` iloczyn jest łączny
* `r(s|t)` = `(rs)|(rt)`
* `(s|t)r` = `(sr)|(tr)`
* `εr` = `rε` = `r`


### Metaznaki
* `\` literalne traktowanie metaznaku (escaping)
* `+` jeden lub więcej razy `a+` = `aa*`
* `?` zero lub 1 raz `a?` = `(a|ε)`
* `{n}` n-krotne powtórzenie
* `{n,}` conajmniej n-krotne powtórzenie
* `{,m}` maksymalnie m-krotne powtórzenie
* `{n,m}` powtórzenie między n a m razy
* `.` dowolny znak, pojedynczy literał
* `[]` jeden znak z podanego zbioru
  * `[abcd]`, `[a-d]` - jeden spośród znaków a,b,c,d
* `[^]` jeden znak spoza podanego zbioru
  * `[^abc]` jeden znak inny niż a,b,c
* `^` początek łańcucha (linii, pliku, zależnie od kontekstu)
* `$` koniec łańcucha


Różne standardy, implementacje definiują pomocnicze klasy literałów (znaki alfanumeryczne `\w`, cyfry `\d`, białe znaki `\s`).

Kwantyfikatory domyślnie są zachłanne (greedy), dopasowują najdłuższe możliwe wyrażenie. Dodanie `?` zmienia kwantyfikator na leniwy (lazy, nongreedy).

`<h1>Hello world!</h1>`

* Wyrażenie `<.+>` dopasuje cały napis (greedy)
* Wyrażenie `<.+?>` dopasuje tylko `<h1>` (lazy, nongreedy)

### Sprawdzanie wyrażeń regularnych
* https://regexr.com
* https://regex101.com
* https://emailregex.com/index.html
* https://www.regextester.com


Wyrażenia regularne nie zawsze są dobrym rozwiązaniem, często niepotrzebnie komplikują rozwiązanie, nie da się rozwiązać problemu wyrażeniami regularnymi (poprawna walidacja adresu email) albo da się rozwiązać problem prościej bez wyrażeń regularnych.


## Automaty
* Automat skończony, skończenie stanowy, FSM, Finite State Machine
  * zbiory stanów i alfabetu są skończone
* Automat deterministyczny, DFA, Deterministic Finite Automaton
  * Jest tylko jeden stan początkowy
  * Przejście jest określone jednoznacznie dla każdego wejścia (relacja przejść jest funkcją)
* Automat niedeterministyczny, NFA, Nondeterministic Finite Automaton
* Automat zupełny
  * Ma zdefiniowane przejście dla każdej pary stanu i wejścia
* Automat niezupełny


## Automat Rabina-Scotta
Pozwala na rozpoznawanie wyrażeń regularnych.

* Skończony zbiór stanów (FSM)
* W zbiorze stanów są wyróżnione
  * stany początkowe
  * stany akceptujące
* Przechodzi do następnego stanu na podstawie symbolu z taśmy wejściowej, według określonej funkcji przejść
* Dojście do stanu akceptującego oznacza, że sekwencja spełnia wyrażenie


## Automaty skończone w informatyce
* Akceptory
  * rozpoznaje sekwencję
  * jedna taśma
  * wyjście "tak" lub "nie"
* Klasyfikatory
  * przyporządkowuje sekwencję do kategorii
  * jedna taśma
  * jeden symbol wyjściowy ale więcej niż 2 możliwości
* Transduktor
  * generuje sekwencję wyjściową na podstawie wejściowej
  * dwie taśmy
* Sekwencer / Generator
  * na żądanie generuje sekwencję wyjściową


Automat skończony (FSM) można przedstawić jako etykietowany graf skierowany (Moore'a i Mealy'ego).

Dla każdego automatu Moore'a da się skontruować równoważny (produkujący takie same sekwencje wyjściowe) automat Mealy'ego i na odwrót.


## Diagramy stanów (statecharts)
Koncepcja statecharts pozwala na łatwiejsze modelowanie złożonych automatów i ich podfunkcjonalności.

* Model skończenie stanowy
* Zdarzenia są wejściami automatu
* Reakcje na zdarzenia to stany automatu
* Hierarchiczne zagnieżdżanie - stan może zawierać statechart
* Może modelować równoległe działanie automatów
* Dodatkowe typy stanów początkowych


## UML - Unified Modeling Language
Notacja opisująca diagramy stanów.

Modeluje diagramy:
* Przypadków użycia
* Struktury
  * Klas
  * Implementacji
  * Pakietów
* Zachowania
  * Sekwencji
  * Współpracy
  * Stanów
  * Aktywności


## [Stan jako wzorzec projektowy](https://refactoring.guru/design-patterns/state)
![Diagram wzorca stanu](https://refactoring.guru/images/patterns/diagrams/state/structure-en.png?id=38c5cc3a610a201e5bc26a441c63d327)

* `Context` przechowuje aktualny stan, deleguje do niego operacje, obsługuje zmianę stanu.
* `State` określa operacje wspierane przez stany.
* Konkretne implementacje mogą przechowywać kontekst i inicjalizować przejście do kolejnego stanu.
* Kontekst i konkretne stany mogą zmieniać aktualny stan przez zmianę referencji do aktualnego stanu w kontekście.
* Każdą implementację stanu można przetestować niezależnie.


Implementacja z wykorzystaniem tabeli przejść i wyjść albo jednym wielkim `switch(...) case: ...` jest nieobiektowe, źle się skaluje i jest ciężkie do testowania.


## Związek między gramatyką i automatem
Gramatyki generują (produkują) słowa i zdania. Automaty akceptują słowa i zdania.

### I Twierdzenie Kleene'go
Dla każdego niedeterministycznego automatu $A$ istnieje gramatyka regularna $G$ taka, że $L(A) = L(G)$

### II Twierdzenie Kleene'go
Dla każdej gramatyki regularnej $G$ istnieje skończony automat $A$ taki, że $L(G) = L(A)$

### Konstrukcja Thompsona
Sposób na zbudowanie automatu rozpoznającego wyrażenie regularne. Tworzy automat niedeterministyczny.

Istnieje algorytm budowania automatu deterministycznego z niedeterministycznego albo z wyrażenia regularnego.

Automat rozpoznający wyrażenie nie musi być zupełny ale można tak uzupełnić przejścia i stany, żeby dodatkowo wprowadzić diagnostykę na podstawie tego, w którym stanie nieakceptującym automat wyląduje.


## Hierarchia gramatyk Chomsky'ego
![Hierarchia Chomsky'ego](./obrazy/https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Chomsky-hierarchy.svg/1024px-Chomsky-hierarchy.svg.png)

| Typ języka                 | Automat                     |
| -------------------------- | --------------------------- |
| Rekurencyjnie przeliczalny | Maszyna Turinga             |
| Kontekstowy                | Automat liniowo ograniczony |
| Bezkontekstowy             | Automat ze stosem           |
| Regularny                  | Automat skończony           |

Języki regularne dają się wyrazić przez wyrażenia regularne - równoważnie z automatami skończonymi.

Notacja nawiasowa z nieograniczoną liczbą zagnieżdżeń nie daje się opisać wyrażeniem regularnym ze względu na brak informacji o historii dojścia do danego stanu - potrzebny jest automat stosowy.


## Automat stosowy
Automat rozbudowanay o pamięć stosową

$$A = <Z, K, next, z_0, q_0, H>$$

* $Z$ alfabet stosu
* $K$ zbiór stanów automatu
* $T$ alfabet taśmy wejściowej
* $next$ relacja przejść
* $z_0 \in Z$ symbol początkowy stosu
* $q_0 \in K$ stan początkowy automatu
* $H \subseteq K$ zbiór stanów akceptowalnych


## Maszyna Turinga
* Nieskończona taśma podzielona na komórki
  * załadowana danymi wejściowymi
* Głowinca czytająco-pisząca
  * wykonuje operacje na podstawie grafu sterowania
  * może przesuwać się o jedną komórkę w lewo lub w prawo
  * ma określone położenie początkowe
* Alfabet - symbole znajdujące się na taśmie danych
  * w tym symbol pusty
* Graf sterowania
  * skończenie stanowy
  * ma stan początkowy i stany końcowe

Po dojściu do stanu końcowego na taśmie znajduje się wynik.

Jest teoretycznym modelem dla każdego komputera. Taśma - przestrzeń adresowa. Procesor jest uniwersalną maszyną Turinga (sekwencer - graf sterowania).

Maszyna Turinga ma wszystkie możliwości atuomatu stanowego, więc każdy język formalny akceptowany przez FSM jest też akceptowany przez odpowiednio ograniczoną maszynę Turinga.

### Teza Churcha-Turinga
* Maszyna Turinga jest w stanie rozwiązać każdy efektywnie rozwiązywalny problem algorytmiczny
* Dla każdego efektywnie rozwiązywalnego problemu algorytmicznego da się skonstruować maszynę Turinga, która go rozwiązuje.
* Jeśli nie da się skonstruować maszyna Turinga rozwiązującej dany problem to jest on nierozwiązywalny.

### Symulatory
* [Symulator maszyny Turinga #1](https://turingmachinesimulator.com)
* [Symulator maszyny Turinga #2](https://morphett.info/turing/turing.html)
* [Symulator maszyny Turinga #3](https://turingmachine.io)

```
// http://turingmachinesimulator.com/shared/iwhwburkwb

name: Negate number in two's complement encoding
init: negating
accept: stop

negating,0
negating,1,>

negating,1
negating,0,>

negating,_
goBackToAdd,_,<  // Finished negating, adding one

goBackToAdd,_
addOne,_,<

addOne,0
stop,1,-

addOne,1
addOne,0,<

addOne,_
stop,_,-
```
