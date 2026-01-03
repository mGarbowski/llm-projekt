# 2024-11-08

## Modelowanie dziedziny problemu
W pracy nad projektem pojawiają się specyficzne określenia
Ważne żeby pojęcia były zrozumiałe dla wykonawcy i zamawiającego
Określenie pojęć i powiązań między nimi
Później model pojęciowy jest punktem wyjścia dla modelu danych
Naturalnie współgra z modelem obiektowym - jakie obiekty będą występować w systemie
Rzeczowniki, które pojawiają się w opisie - zastanowić się które są istotne z punktu widzenia tworzonego systemu

Na poziomie analitycznym interesują nas głównie atrybuty (nie operacje)
Model klas w UML

Obiekt może istnieć w różnych stanach, to co można z nimi zrobić zależy od stanu (np. książka wypożyczona i niewypożyczona)
Model stanów obiektów - tam gdzie to jest istotne
Diagram stanów UML

## Diagram klas
* Statyczny
* Pokazuje jakie są zbiory obiektów (klasy) i jakie są relacje między nimi
* Relacje
	* asocjacja
	* uogólnienie

## Perspektywy widzenia modelu
* Diagramu klas używa się na różnych etapach obiektu
	* analiza
	* projektowanie
	* udokumentowanie istniejącego kodu
* Diagram klas jako model pojęciowy
	* klasa = pojęcie, nie tożsame z programowaniem obiektowym
	* rozmieszczenie operacji jest już decyzją implementacyjną
	* brak odniesień implementacyjnych
* Model projektowy
	* rozwinięcie modelu pojęciowego
	* pola i metody klas
	* decyzje zależne od użytych narzędzi (np. nie każdy język wspiera wielokrotne dziedziczenie)
	* model projektu i implementacji
* Analityk określa co powinno być klasą, co warto rozróżnić

### Uogólnienie
* Relacja podzbioru
* W modelu pojęciowym - klasyfikacja bytów
* W modelu projektowym - hierarchia dziedziczenia
* Nazwa klasy *kursywą* - klasa abstrakcyjna
	* każdy obiekt, który należy do tej klasy musi jednocześnie należeć do konkrentej podklasy
* Podział klasy na podklasy może być
	* pełny (complete) - podzbiory pokrywają w całości nadrzędny zbiór
	* rozłączny (disjoint) - podzbiory są rozłączne
	* niepełny (incomplete) - podzbiory nie pokrywają całego nadzbioru
	* nakładające się (overlapping) - podzbiory mogą się nakładać
	* domyślne ograniczenie to incomplete i overlapping - inaczej niż w językach obiektowych
* UML definiuje składnie, nie wszystkie diagramy są dozwolone, nie mogą być wewnętrznie sprzeczne

## Asocjacja
* Model pojęciowy - związek klas
* Model projektowy
	* pola powiązań
	* operacje tworzenia / usuwania
* Opis relacji
	* krotność - ile par może tworzyć obiekt z obiektami drugiej klasy
	* nazwa
	* kierunek - z której storny jest trzymana informacja
* Przypadki szczególne
	* agregacja - pusty romb po stronie całości
	* kompozycja - wypełniony romb po stronie całości
* Kompozycja
	* szczególny przypadke agregacja
	* część może być częścią tylko 1 całości
	* krotność 1 albo 0..1
	* np. fizyczne składanie się z czegoś
* Pominięcie rombów w oznaczeniu nie jest błędem ale model jest mniej szczegółowy
	* bo agregacja i kompozycja są szczególnymi przypadkami asocjacji


## Klasy asocjacyjne
* Asocjacja która jest jednocześnie klasą
* np. odjazd pociągu ze stacji
* Asocjację charakteryzują atrybuty
	* atrybuty nie charakteryzują jednej ze stron
* W UML modelowane przez klasę asocjacyjną
	* klasa połączona przerywaną linią z asocjacją
* Warianty modelowania
	* klasa asocjacyjna - nie przekłada się na języki programowania
	* klasa pośrednicząca - relacje nie powiązane ze sobą na diagramie, oznacza się asocjację pochodną przez `/`
* Co innego jest użyteczne w analizie i co innego w projektowaniu

## Diagram stanów
* Elementy
	* stany - zaokrąglone prostokąty
	* przejścia między stanami - łuki etykietowane parą warunek, akcja
* Zdarzenie
	* upłynięcie czasu
	* wywołanie metody
	* spełnienie warunku logicznego
* Model formalny oparty o teorii automatów
* Bardziej rozbudowana notacja
	* akcje wejściowe i wyjściowe
	* akcje wewnętrzne - stan się nie zmienia, a wykonuje się akcja
* Opis przejścia
	* `zdarzenie [dozór] / akcja`
	* przejście jeśli warunek dozoru jest spełniony
* Podstany
* Stan historyczny - ostatni podstan przed wyjściem ze stanu
* Stany równoległe
	* obiekt może być jednocześnie w kilku stanach lub podstanach
* Diagram ma uzupełniać dokumentację, pomagać ją zrozumieć

Modele powstają w sposób iteracyjny

Ograniczenie `{ordered}` - standardowe z UML oznacza że obiekty klasy są uporządkowane