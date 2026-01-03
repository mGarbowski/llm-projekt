# Wstęp do inżynierii oprogramowania

## Metody projektowania programu
* Metoda wstępująca (bottom-up) - od szczegółu do ogółu
* Metoda zstępująca (top-down) - od ogółu do szczegółu


## Paradygmaty programowania
Paradygmat - wzorzec / przykład

Klasyfikacja pod względem sposobu patrzenia programisty na przepływ sterowania programu. Język może wspierać różne paradygmaty programowania.


### Imperatywne
* programista instruuje komputer jak zmieniać stan
* programista skupia się na tym jak coś wykonać
* program jest sekwencją instrukcji do wykonania - control flow

### Deklaratywne
* programista deklaruje jaki rezultat chce dostać, a nie jak go uzyskać
* programista skupia się na tym co wykonać
* program jest zdefiniowaną logiką, a nie konkrenym przebiegiem sterowania
* np. SQL


## Paradygmaty imperatywne

### Proceduralne
Rozwinięcie koncepcji programowania strukturalnego o modularyzację.

* Bloki instrukcji, instrukcje warunkowe, pętle, modularność
* Są zmienne lokalne
* Instrukcje są grupowane w procedury
* Dekompozycja na procedury
* Program ma swoją strukturę
* Nie powinno być niestrukturalnych instrukcji (`goto`, `break`, `continue`)

Warunek pętli powinien być jedynym punktem określającym czy ma się kontynuować lub przerwać


### Obiektowe
Instrukcje są grupowane ze stanem (danymi), na którym operują. Program to zbiór porozumiewających się ze sobą obiektów.

* Obiekt - jednostka zawierająca dane i operująca na nich
* Odzwierciedla współpracę obiektów w świecie rzeczywistym
* Dziedziczenie - definiowanie bardziej złożonych obiektów na bazie istniejących
* Klasy (typy) i obiekty (instancje)
* Metody - procedury, które operują na wewnętrznych atrybutach klasy
* Programista określa kto co może zrobić
  * Można np. nie pozwolić na podanie niepoprawnych danych


## Paradygmaty deklaratywne

### Funkcyjne
Rezultat jest deklarowany przez serię aplikowanych funkcji (złożenie funkcji jak funkcji matematycznych)

* Nie ma zmiennych, jest rekursja
* Cały program jest złożoną funkcją, której wartość oblicza się z danych wejściowych
* wywołanie funkcji na samym końcu
* Funkcje wyższego rzędu - użycie funkcji jako argumentów / wyników
* Leniwe obliczanie (lazy evaluation)
* np. Haskell, Scala, F#

### Logiczne
Rezultat deklarowany jako odpowiedź na pytanie oparte o system faktów i reguł

np. Prolog

### Programowanie sterowane danymi (data flow)
Program to graf operacji między którymi przepływają dane

* Moment wykonania operacji nie zależy od kolejności instrukcji, tylko od dostępności danych
* Analogicznie do arkusza kalkulacyjnego
* AHDL - definiuje strukturę układu, a nie kiedy co się stanie
  * W układzie wszystko dzieje się równolegle
* np. LabVIEW, Verilog, VHDL, AHDL, TensorFlow


## Inne paradygmaty

### Programowanie zdarzeniowe (event-driven)
Program jest zbiorem procedur (handler) reagujących na zdarzenia (zewnętrzne i wewnętrzne)

* Sekwencje zdarzeń (Kliknięcie przycisku, ruch myszką, upływ czasu itp.)
* Wymaga dodatkowego zarządcy, sterującego wykonywaniem procedur
  * kolejka zdarzeń
* Handler nie pamięta jaki ciąg zdarzeń doprowadził do obsługi danego zdarzenia
* Sekwencja zdarzeń to język (ma strukturę gramatyczną)
* Stan okna GUI jest stanem automatu popychanego zdarzeniami
* np. obsługa GUI, aplikacje klient-serwer


### Programowanie współbieżne (concurrent)
Program to zbiór współbieżnych elementów (procesów / zadań / wątków) wykonujących się równocześnie

* Wiele procesów - każdy ma oddzielną pamięć, proces może się rozgałęzić i wystartować kolejne
* Wiele wątków - w ramach jednego procesu, na jednym rdzeniu procesora, dzielona pamięć w ramach procesu
* Wersja ze wspólną pamięcią lub z komunikatami
* Nacisk na zależności między elementami (więzy i zakazy)
* Wymaga synchronizacji i zapobiegania hazardom między elementami wykonującymi się równocześnie
* Może być realizowane przez biblioteki do języków, bo systemy operacyjne natywnie wspierają procesy i wątki
* Może być nałożone np. na model imperatywny, obiektowy i inne


### Data-driven programming
Instrukcje opisują wzorce danych, w momencie dopasowania wyzwolą określone przetwarzanie

* Podobne do programowania zdarzeniowego
* Przetwarzanie strumieni danych
* Filtrowanie, agregowanie
* np. AWK, sed, Lua


### Programowanie aspektowe (aspect-oriented)
Paradygmat zwiększający modularność programu przez separację zagadnień. Zamiast modyfikować kod realizujący daną funkcjonalność dodaje się aspekt.

* Punkt przecięcia (pointcut) - np. dotyczy wszystkich metod o określonej nazwie
* Porada (advice) - funkcje wywołane w określonych punktach przecięcia

Może być zrealizowane statycznie lub dynamicznie - podczas kompilacji lub podczas wykonywania

## Podstawowe założenia OOP

### Dziedziczenie
Budowanie hierarchii typów obiektów, z których obiekt dziedziczący posiada wszystkie cechy obiektu bazowego.

### Abstrakcja
Każdy obiekt może ukrywać przed innymi swoje szczegóły implementacyjne.

* Klasy dziedziczące mogą być zaimplementowane inaczej
* Publicznie dostępny interfejs nie powinien pozwolić na stworzenie obiektu z niespójnym stanem


### Hermetyzacja (enkapsulacja)
Tylko sam obiekt może dokonywać zmian na swoim stanie wewnętrznym. 

Na zewnątrz udostępnia swój interfejs, żeby inne obiekty mogły zmieniać jego stan w kontrolowany sposób.


### Polimorfizm
Referencja na obiekt może dotyczyć dowolnego typu obiektu z hierarchii dziedziczenia. 

* Dynamicznie ustala się z której klasy zostanie wywołana metoda (dowiązanie późne)
* Koszt wywołania nie jest "deterministycznie" znany - trzeba za każdym razem znaleźć, gdzie jest implementacja, którą należy wywołać


## Data-oriented design
Optymalizacja danych w celu najefektywniejszego wykorzystania zasobów (np. sprzętu)

* Organizacja bloków danych do przetwarzania wektorowego na karcie graficznej (SIMD)
* Organizacja danych i przetwarzania w celu optymalnego wykorzystania cache'y


## Refleksja
Zdolność programu do badania swojej struktury, własności, typów obiektów w trakcie wykonywania (introspekcja) i zdolność programu do modyfikowania swojej struktury i zachowania.

### Możliwości refleksji
* Odpytanie obiektu o listę atrybutów i metod
* Modyfikacja struktury obiektu
* Wywołanie metody na obiekcie
* Tworzenie bibliotek i framework'ów
  * np. do serializacji / deserializacji danych

```py
obj = gloabals()['Foo']()
getattr(obj, 'hello')()
```

Nie używać `eval`, najlepiej nigdy


## Separacja zagadnień (SoC)
Podział programu na odrębne moduły, które nie pokrywają się funkcjonalnością

* Każdy element powinien mieć swoje unikalne zastosowanie
* Każdy element zachowuje możliwość jak największej adaptacji do zmian

### Zalety
* Uproszczona praca zespołowa
* Łatwiejsza rozbudowa
* Lepsza czytelność
* Większa reużywalność kodu

### Dotyczy
* Architektury systemu
* Architektury aplikacji - podział na warstwy
  * prezentacja
  * logika biznesowa
  * dostęp do danych

### Problem separacji zagadnień
Często poza główną logiką biznesową, program musi realizować też jakąś logikę poboczną (np. logowanie)

* Implementacja zagadnienia może być porozrzucana (scattered) po wielu modułach.
* Implementacja zagadnienia może być splątana (tangled) z kodem realizującym inne zagadnienia
* Splątanie i porozrzucanie utrudniają albo uniemożliwiają testowanie


## Zasady SOLID

### Single Responsibility Principle
Odpowiedzialność to powód do zmiany - kiedy trzeba by zmienić kawałek kodu. Jeśli powodów jest kilka, to funkcjonalności nie powinny być splątane w jednej klasie/funkcji itp.

* Podział programu na elementy o pojedynczych odpowiedzialnościach zwiększy ich reużywalność
* Każdy element będzie łatwiejszy do zaimplementowania i przetestowania

### Open-Closed Principle
Klasy, moduły, funkcje powinny być otwarte na rozszerzenia i zamknięte na modyfikacje. Uzyskanie nowych funkcji powinno być możliwe przez rozszerzenie elementu a nie przez zmianę już istniejącego elementu (który może już być używany i nie można tego zepsuć).

* Zmniejsza ryzyko złamania kompatybilności
* Dodanie funkcjonalności nie powinno wymuszać zmian w istniejących elementach ani w testah jednostkowych
* Można to osiągnąć przez wykorzystanie interfejsów albo dziedziczenia (lepiej interfejsów)

### Liskov Substitution Principle
Funkcje, które używają referencji do klas bazowych muszą być w stanie używać też obiektów klas dziedziczących po tych klasach bazowych bez znajomości ich implementacji.

* Polimorfizm nie może zmieniać semantyki, przeciążone metody powinny się zachowywać tak samo z punktu widzenia użytkownika
* Klasa dziedzicząca nie powinna zmieniać funkcjonalności tylko ją rozszerzać
* Rule of Three - przy drugim kopiuj-wklej należy się już poważnie zastanowić
* Nie każda relacja "is a" musi oznaczać dziedziczenie
  * Gołąb i Pingwin są ptakami - bazowy ptak nie powinien mieć możliwości latania
* Do tego są interfejsy

### Interface Segregation Principle
Interfejsy powinny być odpowiedzialne za jak najmniejszą funkcjonalność.

* Nowa klasa implementuje tylko te interfejsy, których potrzebuje
* Fat / polluted interface - zawiera zbyt wiele metod, które nie będą używane i wymaga ich zaimplementowania
* Łączy się z zasadą Liskov


### Dependency Inversion Principle
Kod z warstw wyższego poziomu nie powinien zależeć od kodu z niższych warstw. 
Obie warstwy powinny zależeć od abstrakcji (nie implementacji). 
Implementacja (szczegóły) powinna zależeć od abstrakcji.

W ten sposób, można łatwo wymienić implementację jednej ze stron bez konieczności wprowadzania zmian w drugiej i nie trzeba testować rzeczy, które nie zostały ruszone.

Wstrzyknięcie zależności - podanie instancji klasy implementującej wymagany interfejs (abstrakcję) jako parametr konstruktora.

Np. warstwa logiki biznesowej aplikacji zależy od abstrakcyjnej warstwy utrwalania - podmieniając implementację umożliwia się współpracę z różnymi bazami danych.

Wyższa / niższa warstwa - która używa (zależy od) której.

Przykład
* Budowa kompilatora
  * obsługa tekstu źródłowego
  * analizator leksykalny
  * analizator składniowy
  * analizator semantyczny
  * optymalizator
  * generator kodu
* Stos protokołów sieciowych
  * pakiety IP można przesyłać gołębiami pocztowymi i reszta protokołów ze stosu dalej działa


## DRY - Don't repeat yourself
Należy unikać powtarzania tych samych części kodu w różnych miejscach.

* Uniknięcie kopiowania
* Uniknięcie błędów, zaoszczędzenie czasu
  * Zmiana jest tylko w 1 miejscu
  * Nie trzeba szukać wszystkich miejsc
* Uniknięcie powtarzania czynności przez programistę
  * Skrypty
  * Generatory kodu

### Realizacja założeń DRY
* Funkcje
* Szablony / makra (języki silnie typowane)
  * Kompilator generuje kod
* Struktury
* Klasy
* Stałe
* Moduły
* Biblioteki


## KISS - Keep It Simple, Stupid
Nie należy komplikować prostych rzeczy.

Nie należy stosować na siłę wzorców projektowych tam gdzie to nie jest potrzebne.
Nie należy szukać lepszego rozwiązania dłużej niż można na tym zaoszczędzić.

Skomplikowane rozwiązania i wzorce projektowe warto stosować kiedy przynoszą jakąś korzyść (zaoszczędzenie czasu).


## Wzorce projektowe
Gotowe, sprawdzone w praktyce szablony rozwiązań na często pojawiające się problemy projektowe. Opisują rozwiązanie a nie są implementacją rozwiązania.

Wzorce pozwalają na lepszą zrozumiałość, wydajność i niezawodność kodu.

### Kategorie wzorców
* Kreacyjne - związane z tworzeniem obiektów
  * Factory
  * Singleton
  * Prototype
* Strukturalne - związane ze strukturą aplikacji
  * Adapter
  * Decorator
  * Proxy
* Behawioralne - związane z wykonywanymi czynnościami
  * State
  * Strategy
  * Observer
  * Iterator

### Materiały
* [Refactoring Guru](https://refactoring.guru/)
* [Source Making](https://sourcemaking.com/design_patterns)
* [Clean Code - Robert C. Martin](https://www.goodreads.com/book/show/3735293-clean-code)


## Wiarygodność systemów
Wiarygodność (dependability) to pewność działania, która pozwala na uzasadnione zaufanie do usług dostarczanych przez system.

### Aspekty wiarygodności
* Dostępność (Availability) - gotowość do użycia
* Niezawodność (Realiability) - ciągłość usług, wykonywanie funkcjonalności w wymaganym czasie
* Bezpieczeństwo (Safety) - unikanie katastrofalnych konsekwencji (np. odblokowanie drzwi windy w razie awarii)
* Zabezpieczenie (Security) - zapobieganie nieupoważnionemu dostępowi do danych i operacji
