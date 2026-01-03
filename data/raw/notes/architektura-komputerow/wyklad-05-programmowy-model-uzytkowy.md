# Wykład 05 (2023-03-06)


## Języki wysokieg opoziomu
Komputer który sprawnie wykonuje programy w C, spokojnie wykona program w każdym współczesnym językiu

Języki obiektowe od strony implementacji są bardzo podobne do języków proceduralnych. Różni się sposobem myślenia programisty o programie a nie sposobem wykonania prograwmu przez komputer


## Wymagania języka wysokiego poziomu
* Klasy pamięci (sekcje)
* Operacje na danych
  * arytmetyczne
  * logiczne
* Dostęp do danych
  * indeksownie tablic
  * wskaźniki
  * referencje
* Przekazywanie sterowania
  * wywołanie procedury i powrót
  * przekazywanie parametrów
  * zmienne lokalne procedur


## Pojęcia
* Program - statyczny zapis algorytmu, coś co jest napisane np w pliku / w pamięci
* Zadanie / proces - instancja programu w systemie wielozadaniowym
  * Proces ma własną, prywatną pamięć z kodem i danymi
  * Wiele instancji tego samego programu będzie mieć oddzielną pamięć
  * Zadania są od siebie odizolowane, inne zadania nie mają dostępu do nieswojej pamięci
* Wątek - dynamiczna instancja wykonania w obrębie procesu
  * wątki procesu mają wspólną pamięć
  * w małych systemach czasu rzeczywistego są wątki ale nie ma oddzielnych procesów

Współczesne systemy są wielozadaniowe i wielowątkowe. Działa na raz wiele procesów, a w ramach każdego z nich może działać wiele wątków.


## Klasy pamięci
* Kod
* Dane statyczne
  * stałe
  * zmienne zainicjowane
  * zmienne niezainicjowane (BSS)
  * są w pamięci przed rozpoczęciem wykonywania programu
* Dane dynamiczne automatyczne (oddzielne dla każdego wątku)
  * czas życia kontrolowany przez kompilator
* Dane dynamiczne kontrolowane
  * czas życia kontrolowany przez programistę
  * `malloc`, `free`, `new`, `delete`

Dodatkowo we współczesnych systemach
* zmienne statyczne wątu
* kod współdzielony - sekcje kodu wspólne dla wielu zadań (`.dll`)
* dane współdzielone

### Kod (sekcja TEXT)
* Statyczny, obecny w pamięci przez cały czas życiaa programu
* Stały rozmiar
* Tylko do odczytu
* Zawiera
  * instrukcje programu
  * stałe dane wygenerowane przez kompilator (tablice adresów `switch`, literały), logicznie należą do kodu
* Adresy w sekcji kodu są określane przed uruchomieneim programu
  * podczas konsolidacji albo najpóźniej podczs ładowania do pamięci

Statyczna - nie zmienia się, nie znika przez cały czas życia programu


### Dane statyczne
* Czas życia równy czasowi życia programu
* Stały rozmiar
* Obszary
  * RODATA - stałe, tylko do odczytu, zdefiniowane jako `const`
  * DATA - Zmienne zainicjowane niezerową wartością (`int a = 5;`)
    * deklarowane na poziomie zewnętrznym (poza procedurą)
    * wewnątrz procedur zdefiniowane ze słowem `static`
  * BSS - zmienne niezainicjowane (`int a;`)
    * block started by symbol
    * pozwala oszczędzić pamięć
    * współcześnie są zerowane przed rozpoczęciem programu
    * niezainicjowane jawnie albo jawnie zainicjowane na wartość `0` (`int x;`, `int y = 0;`)
* Tworzone przy użyciu dyrektywy assemblera
* Adresy są określane przed uruchomieniem programu
  * Najpóźniej w trakcjie ładowania do pamięci, podczas konsolidacji


### Dane dynamiczne automatyczne
* Argumenty i zmienne lokalne procedur
* Pojawiają się i znikają wtedy kiedy powinny, automatycznie
* Usuwane w odwrotnej kolejności co tworzenie
* Zmienne i argumenty są niszczone po powrocie z procedury
* Tworzą stos
* Określone dynamicznie do konkretnego wywołania procedury (wspiera rekurencję)
* Alokowane i dealokowane przez instrukcje programu (`push`, `pop`), w czasie wykonywania programu
* Każdy wątek ma własny stos, oddzielnie woła procedury
* Położenie stosu może zostać określone bezpośrednio przed uruchomieniem wwątku
* Adresy stają się znane w momencie stworzenia


### Dane dynamiczne kontrolowane
* Tworzone i usuwane jawnie przez programistę (`malloc`, `free`)
* Tworzą stertę (heap), nieuporządkowana struktura
* Czas życia nie jest związany z czasem życia i zagłębianiem procedur
* Adres poznaje się w momencie utworzenia danej


## Pamięć w wątku w procesie wielowątkowym
* współdzielą kod, dane statyczne i stertę
* własny stos
* własne dane statyczne (opcjonalnie)
  * TDATA - zainicjowane
  * TBSS - niezainicjowane
* sekcje są tworzone w chwili tworzenia wątku, podczas działania programu
* adresy są znane w momencie utworzenia wątku


## Struktura przestrzenia użytkowej procesu
Główne obszary - kod, dane statyczne, stos, sterta

Sterta rośnie w górę (większe adresy), a stos w dół (mniejsze adresy)

Adresy bliskie zera nie są używane.

Pusta sekcji przestrzeni adresowej przy adresie 0 - odwołania po wskaźniku o wartości null rzuca błąd.

Przestrzeń adresowa to nie to samo co pamięć fizyczna. Pozostawia się przedziały adresów jako puste (nielegalne, program nie może się do nich odwołać). Adresom nie odpowiadją fizyczne komórki pamięci


## Symboliczny zapis instrukcji procesora
W pamięci komputera instrukcje procesora są zapisane w postaci słów binarnych

Język symboliczny - assemblerowy odpowiada bezpośrednio insturkcjom procesora

Assembler jest inny dla różnych procesorów.

`nazwa-instrukcji argument1, argument2,...`


## Instrukcje potrzebne do implementacji języka wysokiego poziomu
* kopiowanie
  * rozszerzanie długości słów przy konwertowaniu typów
* operacje arytmetyczne i logiczne
* rozejścia warunkowe i pętle
* przekazywanie sterowania pomiędzy procedurami


## Licznik instrukcji
PC - Program Counter

* Adres kolejnej instrukcji, która ma być pobrania
* Inkrementowana w trakcie pobrania instrukcji
* W trakcie wykonywania instrukcji wskazuje już na następną
* Przy wykonaniu skoku jest ładowanym adresem docelowym skoku
* Adres jeset zawsze w obrębie sekcji kodu


## Wywołanie i powrót z procedur
Procedura - fragment wołany z więcej niż jednego miejsca programu

Instrukcja skoku ze śladem `call x` - zapamiętuje aktualną wartość PC razem z argumentami i zmiennymi lokalnymi na stosie, ładuje podaną wartość do PC

Instrukcja powrotu `ret` - ładuje do PC ostatnio zapamiętaną wartość