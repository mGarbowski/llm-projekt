# Hurtownie danych

## Definicje

### Definicja Billa Inmona 
* Zorientowana na problem
	* nie dotyczy szczegółów bieżących operacji
	* dotyczy danego problemu biznesowego
* Zintegrowana
	* dane są zbierane z wielu źródeł
	* połączone w jedną całość
	* nie jest widokiem na jedną bazę danych
* Wersjonowana w czasie
	* często jest potrzeba badania zmienności zjawisk w czasie
	* wszystkie dane są przypisane do odpowiedniego okresu
* Niezmienna
	* najczęściej nie podlegają modyfikacji
	* dotyczą faktów, które nastąpiły
	* rejestruje się zdarzenie modyfikacji, a nie nadpisuje stan w hurtowni
	* usuwanie jest czynnością administracyjną, a nie biznesową (czas retencji danych)

### Definicja Ralpha Kimballa
* Kopia danych transakcyjnych ustrukturalizowania w specyficzny sposób do wykonywania zapytań i analiz
* Specyficzna struktura
	* zorientowana wyłącznie na optymalizację zapytań analitycznych
	* nie obsługuje żadnych zadań operacyjnych
	* transakcje nie są istotne
* Zapytania i analizy
	* zapytania nie są ustandaryzowane jak w aplikacjach operacyjnych
	* w aplikacji wiadomo jakie zapytania będą zadawane (z odpowiednimi parametrami)
	* mogą być zadawane ad-hoc
	* z reguły wykonywane przez narzędzia BI
	* nie wiadomo z góry jakie zapytania będą wykonywane przez analityków

### Inna definicja
* Zawiera dane z wielu źródeł
* Przeznaczone do użycia przez aplikacje wspomagania decyzji
	* ze szczególnym uwzględnieniem przetwarzania analitycznego online
* Dane są z reguły
	* wielowymiarowe
	* historyczne
	* niezmienne

### DSS
* Systemy wspomagania decyzji
	* systemy informatyczne pozwalające osobom odpowiedzialnym (menedżerom) szybko podejmować właściwe decyzje
* Zestaw standardowych sposobów przetwarzania danych, z góry ustalone
* Zbliżone do systemów raportujących

### OLAP
* Online Analytical Processing
* System BI pozwalający na szybkie pozyskiwanie informacji z wielowymiarowych baz danych w celu podejmowania decyzji
* Mają ustandaryzowaną metodę wykonywania analiz na wielowymiarowych bazach danych
* Wykorzystywane przez analityków, pozwala na szybkie wykonywanie pracy
* Wyniki analiz są wykorzystywane do podejmowania decyzji
* Dowolne zapytania w dowolnym momencie

## Architektura
* OLTP
* OLAP
	* odpowiednio ustrukturyzowane i wyczyszczone dane
* Nietransakcyjne
	* zorientowane na aplikację
	* do wymiany informacji
	* np. platformy społecznościowe
* Big Data
	* surowe dane
	* zorientowane na wyciąganie użytecznych informacji (nawet z błędnych danych)

### Odrębność hurtowni i systemu OLTP
* Zawawrtość bazy danych
	* hurtownia może zbierać dane z wielu baz transakcyjnych i zewnętrznych źródeł danych
* Organizacja danych
	* te same informacje są zorganizowane w inny sposób
* Metody dostępu do danych
	* OLTP musi wspierać jak najefektywniej `INSERT`, `UPDATE`, `DELETE`
	* do hurtowni dane są tylko dodawane i odczytywane
	* normalizacja nie jest potrzebna bo dane nie są aktualizowane
* Obciążenie systemu
	* OLTP - obciążenie punktowe, modyfikacje pojedynczych wierszy, dużo małych transakcji
	* OLAP - duże zapytania przetwarzające duże ilości danych
	* wymaga innej konfiguracji do zoptymalizowania tego typu poleceń

### Rodzaje hurtowni danych
* Hurtownia korporacyjna (detaliczna)
	* zawiera szczegółowe informacje o każdym fakcie wynikającym z danych bazy OLTP
	* wszystko co można wyciągnąć z pierwotnych danych
* Składnica tematyczna (Data Mart)
	* zorientowana na konkretny problem/temat
	* szybkie wyciąganie informacji na konkretny temat
	* wstępnie zagregowane dane
* Hurtownia wirtualna
	* nie ma faktycznej hurtowni
	* utrzymuje się niezależne źródła danych
	* mechanizmy do pozyskiwania danych na bieżąco ze źródeł

### Warstwy DSS
* Serwer hurtowni
	* obsługuje bazę danych
* Serwery OLAP
	* może być zintegrowany z serwerem hurtowni
	* obsługuje zapytania analityczne
	* ROLAP
	* MOLAP
	* HOLAP
* Aplikacje i narzędzia
	* raportujące
	* analityczne
	* data mining

### ROLAP
* Relational OLAP
* Implementacja bazy wielowymiarowej jako struktury gwiazdy w bazie relacyjnej
* Te same mechanizmy co do baz transakcyjnych, inne ułożenie danych
* Dowolność w definiowaniu struktur
* SQL
* Standardowe mechanizmy optymalizacji
* Dodatkowe narzędzia/nakładki specyficzne dla OLAP
* Mniej wydajne niż MOLAP
* SQL może być mało wydajny w niektórych zastosowaniach
* Bez ograniczeń na pojemność (mała wrażliwość na wolumen)

### MOLAP
* Multidimensional OLAP
* Wielowymiarowość na poziomie fizycznym
* Wysoka wydajność
* Dedykowane narzędzia
* Ściśle określona struktura danych
* Łatwa integracja z systemami BI
* Wrażliwe na wolumen danych
* Nieefektywne dla rzadkich danych
* Duże narzuty przy ładowaniu danych

### HOLAP
* Hybrid OLAP
* Mieszana reprezentacja danych
	* łączy zalety baz relacyjnych i wielowymiarowych
* Część danych w postaci relacyjnej, część w postaci wielowymiarowej
* Dobór mechanizmów dostępu do potrzeb
	* tylko wybrane pola są w bazie wielowymiarowej
	* tylko świeże dane w bazie wielowymiarowej
* Reprezentacja wertykalna i horyzontalna
* Skomplikowana i droga w utrzymaniu

### Architektura CIF
* Corporate Information Factory
* Dane źródłowe poddawane procesowi ETL
	* trafiają do Enterprise Data Warehouse
* Enterprise Data Warehouse (EDW)
	* hurtownia detaliczna
	* znormalizowana
	* dane w procesie ETL trafiają do Data Marts
	* dane używane bezpośrednio przez narzędzia BI
* Data Mart
	* składnice tematyczne
	* zagregowane dane
	* podział ze względu na organizację
* Narzędzia analityczne
	* dostają się do danych detalicznych w EDW lub zagregowanych w DM

### Architektura EDW Bus
* Enterprise Data Warehouse - hurtownia detaliczna (znormalizowana)
* Dane źródłowe trafiają do EDW w procesie ETL
* Dane z EDW trafiają do Data Marts w procesie ETL
* Data Marts - składnice tematyczne
	* dane zagregowane i detaliczne
	* dane uzgodnione
	* podział ze względu na procesy
* EDW Bus
	* moduł pośredni między narzędziami analitycznymi a Data Marts
	* narzędzia analityczne nie korzystają bezpośrednio z hurtowni detalicznej

### Independent Data Marts
* Wiele niezależnych Data Marts
	* dane zagregowane i detaliczne
	* dane nieuzgodnione
	* podział ze względu na organizację
	* każdy niezależnie uzupełniany danymi ze źródeł w procesie ETL
* Bez hurtowni korporacyjnej
* Łatwe do wdrożenia
* Chaotyczna struktura, może prowadzić do niezgodności danych
* Nie ma centralnego miejsca na obowiązujący zbiór danych
* Raczej jako prototyp
* Dedykowane narzędzia do konkretnych DM
* Brak spójności i integracji

## Procesy i narzędzia

### ETL
* Extraction-Transformation-Loading
* Ekstrakcja danych ze źródeł
	* wykonywanie złożonych zapytań na bazach źródłowych
	* wczytywanie i analiza plików
	* pobieranie danych strumieniowych
	* zapis danych w bazie pośredniej (stage)
* Czyszczenie danych
	* usuwanie błędnych wartości, śmieci
	* wykrywanie anomalii (np. na podstawie spodziewanego rozkładu danych, dane są poprawne ale wymagają dodatkowej analizy)
	* wykrywanie naruszonych więzów integralności
	* wykrywanie braków w danych
	* deduplikacja (ta sama wartość wprowadzona na różne sposoby, np. adres)
	* uspójnianie formatów i wartości
* Transformacja
	* do spójnego formatu np. daty
* Integracja
	* np. ta sama osoba może być różnie identyfikowana w różnych systemach (PESEL, id pracownika)
* Znakowanie czasem
* Ładowanie do hurtowni
	* operacje (transformacja, czyszczenie) są wykonywane na bazie pośredniej
	* wyniki są zapisywane w bazie hurtowni
	* przetwarzanie załadowanych danych w hurtowni (agregaty)
* Obsługa danych szczególnych i metadanych
	* obsługa danych wyliczanych, pochodnych
	* tworzenie struktur OLAP
	* obsługa przestarzałych danych - dane źródłowe pojawią się z opóźnieniem
	* obsługa metadanych
* Hurtownia musi zawierać dane w odpowieniej strukturze

### Projektowanie ETL
* Wymaga zrozumienia potrzeb biznesowych
	* są inne niż wobec bazy OLTP
* Ustalenie KPI - Key Performance Indicators
	* wskaźniki wyliczane na podstawie danych
* Ustalenie i zrozumienie przepisów
	* jakie dane i jak długo wolno przechowywać
* Określenie jakości danych źródłowych i opracowanie technik zapewnienia jakości
* Określenie zakresu dostępu do danych
	* zasady bezpieczeństwa
	* może wpływać na architekturę
* Opracowanie metod integracji danych
	* utożsamienie identyfikatorów
	* uzgadnianie faktów i wymiarów
* Określenie potrzeb czasowych, częstotliwości i trybu zasilania
	* zazwyczaj dane są ładowane cyklicznie
	* różne dane mogą mieć różne potrzeby czasowe
	* uzupełnianie bazy OLAP obciąża bazę OLTP
* Dostosowanie wzajemne ETL i narzędzi BI
	* wykorzystanie odpowiednich struktur

### Moduły ETL
* Ekstrakcja
	* profilowanie danych (jakość, przydatność, pełność)
	* wyszukiwanie zmian od ostatniego ETL (CDC - Change Data Capture)
	* odczyt danych z bazy
* Czyszczenie
	* czyszczenie
	* obsługa błędów
	* deduplikacja
	* uzgadnianie danych
* Dostarczanie
	* zarządzanie zmiennością wymiarów (np. klient jako punkt w wymiarze klientów, mogą dochodzić nowi klienci)
	* generacja kluczy sztucznych - klucze z baz źródłowych nie mają znaczenia, dane ze strumieni mogą nie mieć kluczy
	* zarządzanie hierarchiami (np. podział administracyjny, czas)
	* zarządzanie szczególnymi wymiarami (czas, zbiorcze, mini, skurczone, statyczne, użytkownika)
	* budowa i ładowanie tabel faktów
	* zarządzanie powiązaniami, mapowanie kluczy
	* obsługa danych wielowartościowych
	* obsługa danych spóźnionych
	* udostępnianie uzgodnionych wymiarów
	* udostępnianie uzgodnionych faktów
	* budowa agregatów
	* budowa kostek MOLAP
	* sortowanie
	* zarządzanie powiązaniami (dane źródłowe - dane hurtowni - raporty)
	* propagacja danych, udostępnianie na zewnątrz
* Zarządzanie
	* szeregowanie zadań
	* backup
	* restart i odtwarzanie
	* kontrola wersji
	* migracja (test - produkcja)
	* zarządzanie przepływem zadań biznesowych
	* bezpieczeństwo
	* zarządzanie zgodnością z przepisami
	* zarządzanie metadanymi

## Model danych
Standardowo w hurtowniach stosuje się model wielowymiarowy, struktura jest prosta

### Podstawowe struktury

#### Gwiazda
* 1 tabela faktów - opisuje zdarzenia biznesowe i ich cechy
* 1 tabela na wymiar - opisują kontekst w jakim wystąpił dany fakt
* Hierarchie wymiarów są ukryte (denormalizacja)

#### Płatek śniegu
* 1 tabela faktów
* Możliwe wiele tabel na wymiar
* Wymiary hierarchiczne są znormalizowane (rozgałęzienia)

#### Konstelacja
* Wiele tabel faktów
* Współdzielenie wymiarów

#### Tabele agregatów
* Dla optymalizacji dostępu do danych zagregowanych

### Wymiary
* Model hurtowni - podajemy parametry, dostajemy wyniki
* Działa jak zbiór funkcji ze zmiennymi zależnymi i niezależnymi (x i y)
* Wymiary są tym czego chcemy używać jako parametry analiz
	* używane w `WHERE` i `GROUP BY`
* Opisy, etykiety
* Parametry grupowania
* Parametry analiz
* Wymiar nie musi być zbiorem ciągłym ani uporządkowanym
* Różne rodzaje skali pozwalają na różne operacje
	* narzędzia nie powinny wykonywać na wymiarze operacji niedozwolonych

#### Skale
* Skala nominalna, dychotomiczna
	* np. województwo, płeć
	* istnieje określony zbiór wartości, nie ma określonego porządku
	* zliczanie, frakcja, dominanta
* Skala porządkowa
	* ustalony porządek między elementami
	* jakiś naturalny porządek, nie ustalony arbitralnie (można uporządkować województwa alfabetycznie ale nie o to chodzi)
	* porównywanie, min, max
	* można określić co jest większe ale nie ma sensu pytanie *o ile*
	* np. wykształcenie
* Skala interwałowa
	* np. data-czas, temperatura w stopniach Celsjusza
	* odejmowanie, średnia, wariancja
	* ale dodawanie nie ma sensu
* Skala ilorazowa, absolutna
	* wszystkie operacje
	* np. temperatura w stopniach Kelvina, liczba obiektów, stopa procentowa, interwał czasowy
	* można określić np. że coś jest 2 razy większe

#### Wymiary hierarchiczne
* Wymiary dzielące się na jednostki niższego rzędu
	* okresy - rok, kwartał, miesiąc
	* podział administracyjny - województwo, powiat, gmina
	* struktura organizacji
	* kategorie towarów
* Kluczowe cechy to głębokość podziału i jego zmienność
* Hierarchie stałej głębokości, pozycyjne
	* poziomy jako atrybuty w tabeli wymiarów (zdenormalizowane)
	* poziomy jako powiązane tabele wymiarów w modelu płatka śniegu (znormalizowane)
	* np. województwo-powiat-gmina-miejscowość
* Hierarchie o ograniczenie zmiennej głębokości
	* np. wiadomo że głębokość jest maksymalnie 5
	* poziomy jako atrybuty (tyle ile maksymalna głębokość)
	* ewentualnie dodatkowe atrybuty z opisami poziomów (drugie tyle kolumn)
	* np. podział administracyjny w różnych krajach
	* raczej nie ma sensu stosować oddzielnych tabel w stylu płatka śniegu ze względu na niejasność podziału
* Hierarchie o dowolnie zmiennej głębokości
	* rekursywny klucz obcy
	* tabele łączące
	* ścieżka w postaci sformatowanego stringa (jak ścieżka w systemie plików)

#### Szczególne rodzaje wymiarów
##### Wielowartościowe
* Większa granulacja niż tabela faktów
* Z jednym faktem wiąże się wiele wartości
* Np. kontakty, choroby pacjenta
* Realizacja pozycyjna
	* ograniczenie liczby wartości do zadanej stałej
	* odrębny atrybut dla każdej wartości
	* prosta struktura
	* niewygodne do rozszerzenia - wymaga dodania nowej kolumny
* Tabela łącząca (bridge)
	* struktura znormalizowana
	* pozwala na obsługę dowolnej liczby wartości
	* konieczne stworzenie perspektywy w formie tabeli przestawnej
	* pivot zamieniający wiele weirszy na kolumny
* Realizacja bezpośrednia
	* string - wartości oddzielone separatorem
	* wymaga analizy przy odczycie
	* trudność tworzenia zapytań

##### Wymiary skurczone
* Do budowy zagregowanych tabel faktów
* Podzbiór wierszy i kolumn wymiaru
	* odrzucenie danych z niższych poziomów
* Przy budowaniu tabel agregatów o mniejszej granulacji
	* np czas w dniach, a agregat w miesiącach

##### Wymiary zbiorcze
* Zbierają w jednej tabeli wiele wymiarów o niskiej kardynalności
* Np. checkboxy zaznaczane w jednym formularzu przez użytkownika
* Uwzględniające dopuszczalne kombinacje wartości

##### Wymiary statyczne
* Wymiary nie mające odpowiedników w danych źródłowych
* Tworzone przez kod ETL
* Np. arbitralnie określone zakresy lub opisy
	* czas 

##### Wymiary użytkownika
* Wymiary wynikające z potrzeb raportowych
* Utrzymywane ręczne przez użytkownika hurtowni (dedykowaną aplikację)
* Przykłady
	* zakresy wartości grupowania
	* specyficzne hierarchie
	* mogą być wymagane różne dla różnych raportów

#### Przykłady
* Data
	* w bazie operacyjnej zapisuje się timestamp
	* w hurtowni będzie mieć wszelkie atrybuty jakie mogą być potrzebne do analizy
	* np. kwartał, dzień tygodnia, czy dzień roboczy itd

### Projektowanie tabel wymiarów

#### Zasady projektowania
* Prosty klucz sztuczny
* Klucz trwały
	* jeśli istnieje wiele wersji tego samego obiektu to klucz trwały identyfikuje ten obiekt
	* charakterystyczne dla danych historyzowanych
* Duża liczba kolumn opisowych
	* bez kodów i skrótów
	* wszystko ma być gotowe do odczytu i wyświetlenia przez generyczną aplikację

#### Normalizacja i denormalizacja
* Zdenormalizowane - gwiazda
* Znormalizowane - płatek śniegu
* Znormalizowane z kluczami obcymi pochodnymi do wymiarów głębiej w hierarchii
	* model stonogi

#### Wymiary wolnozmienne (SCD)
0. Zachowywanie oryginału (niezmienne)
1. Aktualizacja (korekta)
	* po poprawieniu błędu w bazie źródłowej
2. Nowy wiersz (historia)
	* zalecany klucz trwały
	* znacnziki czasu aktualności
3. Nowe atrybuty (alternatywna rzeczywistość)
	* np. zmiana podziału administracyjnego
4. Miniwymiary
	* podział wymiaru na podzbiory atrybutów zmieniających się wspólnie
5. Miniwymiary + powiązanie z danymi aktualnymi
	* klucz obcy w jednym wymiarze do aktualnej powiązanej wartości w podwymiarze
6. Atrybtu aktualny w wierszach historycznych typu 2
	* w jednym wierszu i dana historyczna i aktualna
7. Połączenie typu 1 i 2 - klucz sztuczny i klucz trwały
	* widok z wartościami aktualnymi wybieranymi na podstawie flagi aktualności
	* w fakcie jeden klucz obcy do wymiaru z tamtego momentu
	* drugi klucz obcy trwały do widoku wymiaru z aktualnymi wartościami

### Fakty
* Opisują zdarzenia biznesowe
* Zmienne zależne (y)
* Wyniki analiz
* Wyniki zapytań
	* w wyrażeniu `SELECT`

#### Rodzaje tabel faktów
* Transakcyjne
	* np. zakup
	* związane z konkretnymi zdarzeniami biznesowymi
* Akumulacyjne
	* np. krok w procesie
	* wyjątkowo - aktualizowane po każdym kroku
	* przez cały czas trwania jakiegoś procesu, rekord jest aktualizowany
* Periodyczne
	* np. stany rachunków
	* snapshot stanu w danej chwili czasu
* Bezmiarowe
	* np. uczestnictwo w zajęciach
	* żadnych dodatkowych informacji
* Skonsolidowane
	* np. zamówienie-faktura-płatność-wysyłka
	* integruje w sobie kilka powiązanych zdarzeń biznesowych
* Zagregowane
	* według hierarchii wymiaru
	* np. miesięczny obrót

#### Miary
* Wartości liczbowe opisujące fakty
* Z rodzaju wynika jakie operacje będą dopuszczalne
* Addytywne
	* sumowanie według każdego wymiaru
	* np. wartość zakupu, ilość towaru, czas połączenia
* Semi-addytywne
	* sumowanie tylko według niektórych wymiarów
	* np. stan konta - nie ma sensu sumowanie po czasie
* Nieaddytywne
	* nie można sumować
	* np. temperatura, procenty

#### Granulacja faktów
* Odpowieniość wiersza w tabeli faktów do zdarzenia biznesowego
* Dla struktury hierarchicznej
	* fakty na poziomie podrzędnym (alokacja faktów, fakty generyczne)
	* fakty na poziomie nadrzędnym (spłaszczenie)
	* fakty na obu poziomach (odpowieniość 1-1 z bazą operacyjną)

#### Alokacja faktów
* Przypisanie faktów z wyższego poziomu do faktów niższego poziomu
	* np. faktura do pozycji na fakturze
* Brak konieczności budowy tabel faktów na różnych poziomach

#### Fakty generyczne
* Fakty, których znaczenie jest opisane typem
* Powodują zamianę kolumn tabeli faktów na wiersze
* Miara jest interpretowana poprzez wymiar
* Sensowne tylko jeśli nie są wykonywane obliczenia na wielu wartościach faktów generycznych

#### Szczególne rodzaje faktów
* Derywaty
	* fakty wyliczane w procesie ETL
	* ułatwiają analizę, ale komplikują ETL
	* definicja i algorytm wyliczania muszą być precyzyjne i stałe
	* obliczenia muszą być wykonalne w czasie wykonywania procesu ETL
* Dane dodatkowe
	* dane zewnętrzne
	* niepowiązane bezpośrednio z faktami
	* np. kurs waluty w momencie wykonania jakiejś transakcji
	* umieszczane w dodatkowych kolumnach tabeli faktów

#### Projektowanie
* Należy dobrze zdefiniować jednolite znaczenie biznesowe faktów
* Minimalizować liczbę wierszy w tabeli faktów o ile to możliwe
* Ujęcie czasu
	* znacznik czasu zdarzenia
	* początek, koniec, znacznik aktualności

### Inne zagadnienia

#### Wymiar vs miara
* Decyzja zależy od zastosowanie
	* zgodnie z definicją (wynik vs kryterium wyszukiwania)
* Informacja może być w obu miejscach
	* data może być i wymiarem i miarą
* Wartość dokładna jako miara, przedział jako wymiar
* Wartość jako miara, dokładny opis wartości jako wymiar

#### Fakty zgodne
* Conformed facts
* Miara występująca w różnych tabelach faktów mająca to samo znaczenie biznesowe
* Kluczowe dla integracji danych z różnych źródeł
	* wymaga weryfikacji zgodności znaczenia (np. zysk netto/brutto itd.)

#### Wymiary zgodne
* Conformed dimensions
* Wymiary używane w różnych tabelach faktów mające to samo znaczenie biznesowe
* Mają te same nazwy kolumn i ich znaczenie
* Kluczowe dla integracji danych

#### Fakty opóźnione
* Nie wszystkie informacje są dostępne w tym samym czasie
* Dane w tabeli faktów nie odpowiadają aktualnemu stanowi tabeli wymiarów
* Odszukanie właściwych danych przeszłych w historii wymiarów
* Konieczność przeliczania agregatów
	* zmieniono przeszłość
* Tabela wymiaru musi mieć znaczniki okresu obowiązywania
* Ewentualna konieczność dodatkowego uzyskania zgodności z przepisami
	* np. zbyt duże opóźnienie

#### Wymiary opóźnione
* Dane przychodzą szybciej niż kontekst
	* np. z danych strumieniowych
* Tworzenie pustych wierszy w tabeli wymiarów i późniejsze wypełnienie
* Warunki występowania
	* bieżące zasilanie hurtowni
	* proces biznesowy pozwala na późniejsze uzupełnienie danych

### Operacje
* Roll up
	* np. sumowanie danych miesięcznych do rocznych
* Drill down
	* np. przejście od poziomu województwa do powiatu
* Slice & dice
	* wybór zakresów w wymiarach
	* np. wybór województwa, kategorii towaru i zakresu czasowego
* Pivot
	* np. przejście od sumy po towarach na sumę po klientach
* Drill across
	* połączenie danych dotyczących różnych faktów
	* unika się takich operacji bo są bardzo nieefektywne
	* np. zamówienia, płatności i wysyłki w jednym raporcie

### Zasady projektowania
* Zapewniać zgodność wymiarów i faktów
* Unikać miar tekstowych
* Zapewniać właściwe opisy tekstowe wymiarów
	* bez kodów, skrótów itd
	* zrozumiałe
* Unikać normalizacji hierarchii wymiarów
	* model gwiazdy gdzie się da
* Unikać faktów generycznych
	* minimalizacja liczby weirszy w tabeli faktów
* Przewidywać zmiany wymiarów
	* odpowiedni model może się dostosować do zmienności
	* jest wiele metod
* Nie używać kluczy naturalnych
	* tylko sztuczne (i trwałe)
* Zapewniać struktury przyspieszające zapytania
* Zachowywać konsekwencję w granulacji tabel faktów
* Nie normalizować faktów
* Nie wymagać złączeń między tabelami faktów
	* można np. połączyć informacje w jednej tabeli
* Unikać dostosowywania tabel faktów do struktury raportów

## Proces projektowania

### Definicja biznesowa
* Określenie procesów i zdarzeń biznesowych
* Co skutkuje pojawiniem się danych
	* działania użytkowników aplikacji
	* kroki procesów biznesowych
* Zdefiniowanie istotnych wartości oraz metryk zdarzeń procesów

### Dobór granulacji danych
* Co reprezentuje wiersz w tabeli faktów
* Przykładowo
	* skan towaru przy kasie
	* pozycja faktury
	* skan karty pokładowej
	* dokument przyjęty w sprawie
	* stan magazynowy towaru na koniec dnia
	* stan rachunku karty na koniec okresu rozliczeniowego
* Zależy jakie informacje są potrzebne dla biznesu

### Identyfikacja wymiarów
* Jak biznes opisuje dane tworzone przez kroki procesów biznesowych
* W jakim kontekście widzą zdarzenia biznesowe

### Identyfikacja faktów
* Konfrontacja potrzeb biznesowych z realnymi danymi
* Co ma być mierzone
* Jakie są generowane wartości i jaka jest ich dostępność
* Jakie są metryki
* Jaka jest wartość biznesowa, KPI

## Podsumowanie
* Hurtownia danych służy wyłącznie celom biznesowym organizacji
* Projektując hurtownię należy poddać analizie procesy biznesowe
	* nie skupiać się na samych danych źródłowych
* Hurtownia jest optymalizowana wyłącznie dla efektywności zapytań
	* dyski są tanie
* Wielowymiarowy model bazy hurtowni jest stosunkowo prosty
	* kluczowe jest zrozumienie biznesowego znaczenia danych
* Przestrzeganie kilku prostych zasad i stosowanie standardowych technik z reguły wystarcza do stworzenia udanego projektu bazy
* Najwięcej pracy i umiejętności wymaga opracowanie dobrego procesu ETL
