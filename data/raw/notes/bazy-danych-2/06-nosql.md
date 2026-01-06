# Podstawy NoSQL
* NoSQL - not only SQL
* Idea, nie określona technologia
	* jest wiele sposobów myślenia o bazach nierelacyjnych
* Rezygnacja z relacyjnego modelu tam, gdzie się nie sprawdza

## Problemy baz relacyjnych
* Nie nadają się do wszystkiego
	* mit z czasów klasycznych systemów OLTP
	* statyczność, niezmienność modelu
	* kontorla danych
	* obligatoryjność mechanizmów RDBMS - nie można ich obejść
	* mit o bezproblemowym i transparentnym rozpraszaniu danych
	* niedostosowane do obliczania w chmurze
* Wysoka złożoność i komplikacja nie zawsze potrzebnych zasobów
	* struktury dyskowe - wszystkie dane i indeksy
	* dostęp do danych zależny od optymalizatora
	* transakcyjność
	* synchronizacja oparta na blokadach
	* trwałość danych oparta na dziennikach
	* wieloprocesowość
	* wielowątkowość
* Architektura
	* wywodzi się z czasów mainframe
	* komunikacja przez pamięć współdzieloną
	* wymóg dużej mocy obliczeniowej serwera
	* skomplilkowana i niewydajna architektura baz rozproszonych
	* tylko skanowanie pionowe
* Dostęp
	* obiektowe języki nie pasują do bazy relacyjnej
	* ORM - komplikuje i dodaje narzut
	* różnica koncepcyjna metod dostępu
	* zamkniętość mechanizmów RDBMS

## Motywacja
### ACID
* Atomicity - wystarczająca na poziomie poleceń
* Consistency - często nadmiarowa na poziomie bazy
* Isolation - często zbędna (brak konfliktów)
* Durability - możliwa do zrealizowana w inny sposób (np. przez redundancję na wielu serwerach)

### Trwałośc i integralność
* Zastąpienie rozwiązań w założeniu pewnych, rozwiązaniami opartymi na prawdopodobieństwie
* Ale są też prawdopodobieństwa awarii
* Trwałość zapewniona przez redundancję na wielu instancjach
* Izolacja przez małe prawdopodobieństwo równoczesności

### Wydajność
* Orientacja na wydajność operacji zamiast na poprawność danych
* Proste mechanizmy dostępu do danych zamiast skomplikowanych funkcji interpretacji SQL
* Wykorzystanie znajomości struktury i mechanizmów dostępu
	* zamiast niezależności fizycznej i optymalizacji zapytań
* Jendowątkowość prostych i szybkich operacji, brak potrzeby synchronizacji

### Skalowalność pozioma
* Akceptacja braku możliwości zapewnienia sprzętu z góry wyskalowanego na system docelowy
* Użycie dużej liczby tanich elementów dostosowanych w miarę potrzeb
* Rozproszenie geograficzne
* Skalowalność jako podstawowe założenie, a nie dodatkowa cecha

### Niezgodność z paradygmatem programowania
* Ułatwienie programowania, prostsze środowisko
	* jednolity model
	* brak potrzeby ORM
	* brak konieczności wbudowywania zapytań SQL w kod
* Zysk wydajnościowy
* Łatwość obsługi niestandardowych typów danych

## Cechy baz NoSQL
* Elastyczne skalowanie poziome
* Elastyczny model danych (lub brak modelu)
* Specyficzny język danych
* Big Data
* Uproszczona administracja
* Uproszczone mechanizmy, wydajność
* Ekonomia, tani sprzęt

## Rodzaje baz NoSQL

### Klucz-wartość
* Baza bez schematu
* Zastosowanie
	* szybkie przetwarzanie prostych danych
	* zarządzanie zawartością
* Przykłady
	* Redis
	* Cassandra
	* Amazon Dynamo
	* Oracle NoSQL
* Często bazy pamięciowe, bo i tak jest mały narzut
* Zalety
	* szybki dostęp do danych
	* wysoka dostępność

### Bazy dokumentowe
* Baza zorientowana na przechowywanie dokumentów
* Zastosowanie
	* zarządzanie dokumentami
	* aplikacje www
* Przykłady
	* MongoDB
	* CouchDB
	* DocumentDB
* Zalety
	* łatwe operowanie na dokumentach
	* dynamiczny model danych (XML)

### Bazy kolumnowe / tablicowe
* Baza o kolumnowej reprezentacji danych
* Zastosowanie
	* zbieranie i przetwarzanie dużej ilości prostych danych
* Przykłady
	* Apache Cassandra
	* Google Bigtable
	* HBase
	* SAP HANA
* Zalety
	* szybki zapis danych
	* wysoka dostępność
	* bardzo duża sklaowalność

### Bazy obiektowe
* Baza z obiektowym modelem danych
* Zastosowanie
	* aplikacje ze złożonym modelem danych
* Przykłady
	* Versant OD
	* Objectivity
	* ObjectStore
* Zalety
	* efektywne przetwarzanie danych
	* łatwe powiązanie baza-aplikacja

### Grafowe
* Baza dedykowana do reprezentacji danych grafowych
* Zastosowanie
	* przetwarzanie powiązanych danych
	* sieci społecznościowe i inne (transport, telekom)
* Większość danych w związkach
* Przykłady
	* ArangoDB
	* InfiniteGraph
	* Neo4J
	* Apache Giraph
	* OrientDB
* Zalety
	* efektywne wykonywanie algorytmów grafowych

### Wielomodelowe
* Różnorodne bazy pozwalające na mieszanie modeli danych
* Zastosowanie
	* przetwarzanie różnorodnych danych
	* dane strukturalne i niestrukturalne
* Przykłady
	* ArangoDB
	* Couchbase
	* MarkLogic
	* OrientDB
* Zalety
	* możliwość przechowywania i przetwrzania różnorodnych danych
	* wiele mechanizmów w jednym systemie

## Paradygmaty NoSQL

### BASE
* Basically Available
* Soft-state
	* może zmieniać swój stan, nawet jeśli nie są wykonywane operacje
	* np. propagacja danych w bazie rozproszonej
* Eventually consistent
	* w odróżnieniu od spójności transakcyjnej
	* następuje po jakimś czasie
	* nie musi być spójna w danym momencie

### CAP
* Consistency
	* baza bez consistency - BASE
* Availability
* Partition-tolerance
	* niewrażliwość na rozspójnienie bazy rozproszonej
	* baza bez partition tolerance - ACID
* Można mieć 2 z 3

## Podstawowe mechanizmy

### Sharding
* Partycjonowanie rozproszone na wiele węzłów
* Replikacja małyhc struktur pomiędzy węzły
* Zalety
	* możliwość wykorzystania słabszego sprzętu przy bardzo dużej ilości danych
	* wzrost wydajności - przetwarzanie równoległe
	* wzrost dostępności (części danych - BASE)
	* ułatwienie administrowania - mniejsze wolumeny
* Wady
	* wzrost złożoności i komplikacji (systemu i aplikacji)
	* trudność realizacji pewnej klasy zapytań
	* dodatkowy narzut na replikację i utrzymanie spójności
	* wrażliwość na parametry łączności pomiędzy serwerami
	* obniżenie dostępności (pełnych danych - ACID)
	* utrudnienie administrowania - złożona struktura

### Hinted Handoff
* Mechanizm obsługi sytuacji awaryjnej
* Zapis danych do działającego węzła zamiast do węzła uszkodzonego aby zchować kworum
* Dane są zapisywane z podpowiedzią, aby przepisać je do węzła docelowego gdy tylko będzie to możliwe

### Read-repair
* Mechanizm obsługi niespójności
* Podczas odczytu - zapis danych aktualnych do węzła, który zwrócił dane o niaktualnej wersji
* Odczyt spowolniony, ale poprawia spójność danych
* Stosowany w bazach, w których optymalizowana jest szybkość zapisu

### Anti-entropy repair
* Mechanizm obsługi niespójności
* Mechanizm uzgadniania replik na podstawie analizy drzew hashujących (Merkle'a)
* Szybkie porównanie wartości funkcji w drzewie - wykrycie różnic pomiędzy replikami
* Synchronizacja wykrytych różnic na podstawie wersji

### Consistent Hashing
* Mechanizm funkcji mieszającej
* Przypisuje wartości do poszczególnych węzłów bazy w sposób pozwalający łatwo usuwać i dodawać węzły

### Vector Clock
* Mechanizm oznaczania danych znacznikami zdarzeń (nie czasu)
* Pozwala określić relację częściowego porządku w zbiorze danych w systemie rozproszonym
* Dzięki temu wiadomo, czy dane są od siebie zależne czy niezależne
* Pozwala wykryć sytuacje, w których
	* mamy do czynienia z kolejnymi wersjami danych
	* dane pochodzą z dwóch różnych źródeł i może być konieczne rozwiązanie konfliktu
* Na początku wszystkie zegary mają wartość 0
* Węzeł inkrementuje swój zegar przy każdym zdarzeniu (modyfikacji danych)
* Z każdym komunikatem rozsyłany jest cały wektor zegarów
* Przy odbiorze komunikatu węzeł inkrementuje swój zegar i aktualizuje pozostałe na wartości maksymalne (własna / otrzymana)

### Gossip
* Protokół komunikacji pomiędzy węzłami bazy rozproszonej działający w tle
* Cykliczna wymiana małych komunikatów pomiędzy losowymi węzłami
* Niska częstotliwość - pomijalny narzut
* Aktualizacja stanu agentów
* Brak gwarancji niezawodności komunikacji
* Zastosowania
	* wymiana informacji o stanie klastrów i węzłów
	* wykrywanie awarii
	* uzgadnianie niespójnych danych (anti-entropy)
	* wyliczanie i agregacja informacji

## Apache Cassandra
* Baza postrelacyjna
* Połączenie 2 rozwiązań
	* Amazon Dynamo - architektura rozproszona
	* Google BigTable - model kolumnowy
* Architektura węzłów równorzędnych
	* możliwość rekonfiguracji online
	* wysoka skalowalność
* Konfigurowalna replikacja
	* wysoka dostępność
	* odporność na awarie
* Dwie opcje spójności
	* BASE (AP)
	* ACID (CP)
* Wsparcie dla przetwarzanie rozproszonego

### Model danych
* Oparty na strukturze kolumnowej
* Podobny do relacyjnego, ale bardziej elastyczny
* Column family z możliwością dynamicznego dodawania kolumn
* Brak odpowiednika kluczy obcych - konieczność denormalizacji
* Pełne możliwości indeksowania - kluczy i innych kolumn

### Operacje na danych
* Język bazy danych CQL - wzorowany na SQL
	* większość poleceń z SQL
	* brak operacji `JOIN`
	* brak możliwości wyszukiwania części klucza
* Wyszukiwanie pełnotekstowe dzięki integracji z narzędziami
	* Apache Solr/Lucene
	* DataStax Enterprise Search
* API dla wielu języków programowania

### Wsparcie MapReduce
* Integracja z Hadoop
* Apache Pig - platforma programowania MapReduce z językiem Pig Latin
* Apache Hive - platforma BI oparta na Hadoop

## MarkLogic
* Baza XML o mechanizmach transakcyjnych
* Architektura dwuwarstwowa
	* D-nodes
	* E-nodes
	* możliwość rekonfiguracji online
	* wysoka skalowalnosć
* Konfigurowalna replikacja
	* wysoka dostępność
	* odporność na awarie
* Transakcje ACID
* Wielowersyjna kontrola współbieżności (MVCC)
* Wsparcie dla przetwarzania rozproszonego

### Model danych
* Model oparty na strukturze XML
* Model dynamiczny oparty na schematach XSD i metadanych
* Pełne możliwości indeksowania
	* zawartość i metadane
	* indeksy zwykłe, XML, skalarne, odwrócone, pełnotekstowe, przestrzenne
* Wielowersyjna baza danych
	* aktualizacja - nowa wersja

### Operacje na danych
* Języki danych
	* XQuery
	* XSLT
	* JSON
* Wyszukiwanie atrybutów, wartości
* Wyszukiwanie zakresowe
* Wyszukiwanie pełnotekstowe
* Wyszukiwanie przestrzenne
* Jest implementacja operacji złączenia
* Zapytania odwrócone
	* jakie zapytanie odnosi się do określonych danych
* Dostęp przez XDBC
* Wymiana danych przez WebDAV

### Wsparcie MapReduce
* Integracja z Hadoop
	* jako źródło danych przez konektor
	* jako warstwa dostępu do danych nad HDFS
