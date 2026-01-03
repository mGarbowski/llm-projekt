# UML (2024-03-25)

UML jest językiem specyfikacji, projektowania i dokumentowania systemów IT.
UML nie jest metodyką, narzędziem modelowania, językiem programowania.
Nie trzeba znać całości UMLa, wystarczy mały podzbiór. Nie należy modelować wszystkiego, a tylko istotne fragmenty systemu
Im bardziej szczegółowy diagram tym krócej powinien żyć

Narzędzia takie jak draw.io robią tylko rysunki, nie ma żadnej weryfikacji semantyki

Enterprise Architect
Papyrus - open source

## Diagramy UML
* Opis struktury
	* klas
	* pakietów
	* struktury złożonej
	* komponentów
	* wdrożenia
* Opis zachowania
	* przypadki użycia
	* maszyna stanowa
	* czynności
	* sekwencji
	* komunikacji
	* przeglądu interakcji
	* czasowy

# Cykl wytwarzania oprogramowania
* Zebranie wymagań
* Analiza i projektowanie
	* wybór technologii
* Implementacja
	* może się okazać, że projekt trzeba zmienić
* Wdrożenie
	* w trakcie można odkryć bugi, trzeba wrócić do implementacji
* Utrzymanie
	* zajmuje najwięcej czasu
	* w trakcie mogą pojawić się nowe wymagania
* Koniec życia / wycofanie
	* może się zdarzyć
	* raczej żyją dłużej niż pierwotnie się zakładało

## Wymagania
* Sformułowana potrzeba cechy produktu / usługi (lub sposobu działania)
* Skąd
	* wewnętrzne - analiza arynku, poprzednich wersji, strategia
	* zewnętrzne - dostarczone w całości przez klienta (przetargi)
	* mieszane - ogólna potrzeba klienta jest uszczegóławiana w ramach usługi
* Klasyczny podział
	* wymagania funkcjonalne - co ma robić
	* wymagania niefunkcjonalne - jak ma robić (wszystko inne - wydajność, niezawodność, jakość)

### Wymagania do wymagań
* Bez dobrych wymagań nie da się zrealizować projektu
* Problem - programiści często nie znają dziedziny, dla której system tworzą
* Poświęcenie czasu na dokładne zebranie wymagań może być kosztowne
	* wg. metodyki agile należy prototypować i zbierać szybki feedback
* Inżynier musi umieć ocenić i wymagać dobrych wymagań

### Dobre wymaganie
* Jasne - bez lania wody
	* sformalizowany / uproszczony język
	* ustandaryzowane konstrukcje gramatyczne
* Kompletne - wszystkie infromacje potrzebne do zrozumienia i sprawdzenia wymagania są w nim zawarte
	* złe - system ma być szybki
	* lepsze - system ma obsłużyć do 1000 zapytań HTTP na sekundę
* Zgodne - nie może być sprzeczne z innymi
	* zawsze trzeba to wyjaśnić, rozwiązać
	* nie może być sprzeczności z dokumentami zewnętrznymi (przepisami)
* Spójne - w opisie systemu nie powinno być braków
	* nie powinno być też nachodzących na siebie wymagań
	* nie ma pola do interpretacji
	* jedno wymaganie odnosi się do jednej i tylko jednej sprawy
* Atomowe - niepodzielne
	* ciężko zweryfikować coś co ma w sobie "i" / "lub"
	* złe - system będzie wspierał formatty JSON, XML
	* lepiej - system pozwoli na zapis danych w formacie JSON, system pozwoli na zapis danych w formacie XML
	* może prowadzić do eksplozji wykładniczej
* Jednoznaczne - wszsystkie pojęcia powinny być zrozumiałe dla każdego odbiorcy
	* skróty i żargon ograniczone, najlepiej do ustalonego słownika pojęć
* Weryfikowalne - zrealizowanie wymagania powinno dać się jednoznacznie i możliwie obiektywnie ocenić
	* najlepiej jeśli wymaganie jest testowalne
	* testy akceptacyjne - uzgodnione z klientem - idealna sytuacja
	* metoda weryfikacji powinna być zdefiniowana razem z wymaganiem (test, analiza dokumentacji, niezależna inspekcja)
* Może mieć priorytet - w jakiej kolejności / czy musi być zrealizowane
	* must / should / could
	* dla klienta to jest zawsze must
* Może mieć uzasadnienie - przydatne jeśli my je tworzymy
* Może mieć możliwość śledzenia - posiada powiązanie z wymaganiami wyższego rzędu / standardami
	* np. wymagania o obsługiwanej liczbie zapytań na sekundę bieże się ze spodziewanej liczby użytkowników

### Zbieranie wymagań / analiza wymagań
* Nie należy traktować pobieżnie
* Kluczowa faza dla ustalenia celu projektu i zdefiniowania co zadowoli klienta
* Dobra analiza może wymagać zestawienia sprawnego kanału komunikacji od klienta do technicznych
* Zebranie wymagań to pierwszy krok

## Model wodospadowy (waterfall)
* Etapy następują po kolei
* Mogą na siebie nachodzić
* Etapy
	* analiza wymagań -> specyfikacja
	* projektowanie -> dokumentacja
	* implementacja -> oprogramowanie
	* weryfikacja
	* utrzymanie
* Dzieli proces na łatwe do zrozumienia i rozdzielenia etapy
* Nie działa - otwarta pętla sterowania, nie ma sprzężenia zwrotnego
* Jest domyślnym sposobem postępowania przy kontraktach o ustalonej cenie
	* wszystkie zamówienia publiczne tak działają
	* może działać przy dużym doświadczeniu wytwórcy
* Często występuje w formach zmodyfikowanych

## Metodyki zwinne (Agile)
* Krótkie cykle od wymagań do wdrożenia
	* cykle liczone w dniach
* Interakcja z klientem na każdym etapie
* Oprogramowanie jest non-stop gotowe do wdrożenia
	* powiązane z CI/CD
* Hipotetycznie - zwinna reakcja na zmiany / elastyczność
* Wymaga elastyczności od klienta, też w kosztach

## SCRUM
* Krótkie cykle - sprint (2-4 tygodnie)
* Klient / reprezentant interesów klienta - Product Owner
* Opiekun i kapitan zespołu - Scrum Master
	* dba żeby zespół nie był przeciążony
* Codzienna obserwacja procesu
* Przebieg
	* sprint planning - zaangażowany product owner
	* daily scrum - spotkanie, co się robiło wczoraj, co się będzie robiło dzisiaj, jakie są problemy
	* work
	* sprint retrospective
	* sprint review - zaangażowany product owner
* Wycenianie zadań na abstrakcyjne jednostki zamiast za godziny
	* dyskusyjne
	* może się sprawdzić jeśli jest jeden projekt i stabilne zatrudnienie


Należy dostosowywać proces do potrzeb, a nie potrzeby do procesu