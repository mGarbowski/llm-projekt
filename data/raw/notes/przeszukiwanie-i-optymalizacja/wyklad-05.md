# 2024-11-06

## Mutacyjny algorytm ewolucyjny

Losowanie ze zwracaniem - nie ma gwarancji do zachowania punktu

zdolności eksploracyjne przejawiają się tym, że czasami pojawia się przejście doliny
pojawia się w populacji punkt po drugiej stronie doliny
może pojawić się więcej niż jedna kopia tego punktu
po losowym przeskoku zaczyna się samonapędzający proces namnażania punktów po lepszej stronie doliny
stan gdzie populacja jest rozdzielona jest nietrwała

charakterystyczne układanie się punktów w chmurki


## Inne rodzaje mutacji
* Mutacja rozkładem jednostajnym w kostce z centrum w punkcie mutowanym
	* dalej w śladzie algorytmu pojawiają się *chmury* - wynikają bardziej z selekcji
* Mutacja bitowa
	* jednakowe prawdopodobieństwo dla każdego bitu (raczej mniejszą niż 1/2)
	* zamienienie bitu na wartość przeciwną
	* xor z wektorem maski
	* $p_m$ - prawdopodobieństwo mutacji pojedynczego bitu osobnika
	* prawdopodobieństwo że osobnik zmutuje $1 - (1-p_m)^n$ ($n$ - lizcba bitów osobnika)
	* prawdopodobieństwo że dokładnie k bitów zostanie zmutowanych $\binom{n}{k}p_m^k(1-p_m)^{n-k}$
	* analogia do mutacji Gaussa
* Inna mutacja bitowa
	* zamiana jednego bitu wybranego z rozkładem jednostajnym
* Mutacja permutacji
	* w przestrzeni permutacji
	* zamiana przyległych pozycji
	* promień mutacji - uogólnienie z liczbą losowanych punktów(?)

Rozkład $\chi^2$

$$
Y = \sum_{i=1}^nx_i^2 \quad X \sim N(0,1)
$$

Dla 1 stopnia swobody gęstość przyjmuje maksimum z 0
Dla więcej niż 1 stopni swobody maksimum jest w pewnej charakterystycznej odległości od 0
mało prawdopodobne że populacja nie będzie się ruszać

Kształt chmury nie jest wynikiem mutacji
zbiór realizacji zmiennej losowej, której wartością oczekiwaną jest położenie punktu optymalnego
populacja jest realizacją zmiennej losowej

średnie położenie punktów w populacji jest estymatorem punktu optymalnego

punkt środkowy populacji (nie musi być zawarty w populacji) na ogół będzie lepszy niż dowolny punkt w populacji


## Weryfikacja jakości algorytmów
Przez rozważania teoretycznie można dowieść, że jak czas dąży do nieskończoności do dokładne rozwiązanie jest znajdywane z prawdopodobieństwem dążącym do 1 - mało praktyczne

Nie wiedząc z góry jakie zadanie optymalizacji przyjdzie nam rozwiązać, nie możemy dobrać efektywnej metody dla niego (no free lunch theorem)

Testowanie - z założeniem że algorytm jest prawidłowo zaimplementowany

Metoda optymalizacji - generator punktów z przestrzeni przeszukiwań
Ewaluator (funkcja celu) - zwrotna informacja o jakości punktu

Optymalizacja typu black box
Krzywe *zbieżności* (nie ściśle rozumiana matematycznie zbieżność tylko zmiana znajdowanego rozwiązania)
czas jest mierzony liczbą wyliczeń funkcji celu

Ten sam algorytm uruchomiony wielokrotnie (np. z różnym punktem startowym, zależy czy algorytm jest deterministyczny) może mieć różne krzywe zbieżności

Nie wystarczy jednokrotne uruchomienie algorytmu do jego oceny


Porównując dwa algorytmy mamy dwa pęki krzywych zbieżności
Jaki jest w ogóle najlepszy znaleziony wynik
Jaka jest szansa szybkiego uzyskania niezłego wyniku niezależnie od punktu startowego

Krzywa ECDF - empirical cumulative distribution function
ustalony zakres wartości na osi pionowej (termometr rtęciowy, kwantyzacja)
ile poziomów z zakresu wartości zostało przebitych przez algorytm / liczba poziomów
ważne jak ustawi się skalę

najpierw przerabia się krzywe zbieżności na ECDF, a potem uśrednia

skąd wziąć minimum i maksimum do ECDF
możemy znać z definicji problemu (objawienie?)
można przyjąć min i max ze wszystkich uruchomień algorytmu - niedoskonałe

wygodniejszy sposób prezentacji bo nie zależy od tego czy mnimalizujemy czy maksymalizujemy, niezależnie od samych wartości
można je uśredniać dla różnych problemów i tego samego algorytmu

na projekt - porównywać krzywe ECDF

wygodniejsza może być skala logarytmiczna przy ustalaniu barier do pokonania

### Porównywanie metod losowych
Dystrybuanta empiryczna rozwiązań uzyskanych po załozonym czasie dla dwóch algorytmów (a nie w czasie jak ECDF)

Żeby wiarygodnie wnioskować analizuje się rozkłady częstości wyników

wyniki posortowane od najgorszego do najlepszego
idąc od -inf do +inf patrzymy jak często uzyskujemy wartości nie większe niż liczba

jeśli jedna krzywa leży nad drugą to algorytm radzi sobie lepiej dla danego zadania
zależy jak duża jest różnica między krzywymi

### Hipotezy statystyczne
* Testy parametryczne i nieparametryczny
* Stawiamy hipotezę zerową (null hypothesis)
* oblicza się prawdopodobieństwo że hipoteza zerowa jest prawdziwa - p-wartość
* wykazanie niewprost
* są implementacje w każdym pakiecie naukowym
* nieparametryczny test Wilcoxona
* parametryczny test t-Studenta

Mając wiele algorytmów i wiele zadań
dla każdego zadanie robi się tabelę przewag (wg. statystycznie istotnej różnicy) (-1, 0, 1)
Sumuje się wartości żeby dostać bilans, a z porównania bilansów ranga
uśrednia się wartości rang po zadaniach



Benchmarki CEC i BBOB