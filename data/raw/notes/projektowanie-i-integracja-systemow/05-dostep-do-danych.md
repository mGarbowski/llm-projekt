# Warstwa dostępu do danych

## OLTP vs OLAP
* OLTP
	* duża liczba transakcji
	* raczej proste transakcje
	* z reguły spójność ma znaczenie
* OLAP
	* mniejsza liczba skomplikowanych zapytań
	* stosowane do analityki
* Big Data
	* variety
	* velocity
	* volume

## Architektura dostępu do danych
* Model domenowy
	* książka, autor
* Model logiczny
	* obiekt, mapa, encja
* Model fizyczny
	* tabela relacyjna

Logika aplikacji powinna być osadzona w modelu domenowym

### Model logiczny a fizyczny
* Mogą być tymi samymi modelami
* Jeśli są różne to wymagają odwzorowania
	* np. ORM
	* narzut na konwersję może być bardzo duży
	* dobór technologii i modelu fizycznego - na frontendzie i w bazie są JSONy - nie ma narzutu na samą konwersję
	* marshallling

## Modele nierelacyjne
* Nie wszystko daje się sensownie wtłoczyć w tabelę
* Często brak transakcji ACID

### Klucz-wartość / kolumnowe
* Przechowują dane jako klucz-wartość lub klucz-wiele wartości
* Cassandra
* Hbase

### Dokumentowe
* Cechy
	* przechowują dokumenty wraz z cechami
	* dostosowane do przechowywania i indeksowania dużych plików
* MongoDB
	* własny system plików GridFS
	* indeksowanie pełnotekstowe
	* rekordy w formacie JSON
	* zapytania w javascript

### Grafowe
* Przykłady
	* neo4j
	* GraphDB

## Polyglot persistence
* Jedna aplikacja korzysta z wielu różnych baz danych
* Z jednej strony więcej baz do obsłużenia
* Z drugiej strony każda z baz ma interfejs bardziej dostosowany do zastosowania do którego została dobrana
* Problem z zamodelowaniem transakcji przechodzącej przez wiele baz
* Redukuje złożoność problemu po stronie aplikacji
* Zwiększa złożoność problemu po stronie infrastruktury

## Wyszukiwanie pełnotekstowe
* Apache Solr
* ElasticSearch
* Większość oparta o Apache Lucene
* Model danych (w dużym przybliżeniu)
	* w kluczu słowo
	* w wartości - id dokumentów w których występuje
* Dokument to może być pdf
* Wierz w tabeli to może być dokument
	* można zaindeksować relacyjną bazę danych w bazie pełnotekstowej

## Command Query Responsibility Segregation
* Osobny model do odczytu
	* np. denormalizacja dla przyspieszenia odczytu, cache'owanie
* Osobny model do zapisu/modyfikacji/usuwania
	* zapewnia walidację reguł biznesowych
* Zapis i odczyt mogą operować na oddzielnej infrastrukturze lub oddzielnych bazach danych
* Potencjalne problemy ze spójnością danych między dwoma modelami
* Ma na celu zwiększenie wydajności i skalowalności

## Event Sourcing
* Każda zmiana stanu aplikacji jest zachowywana jako zdarzenie
* Zdarzenia są przechowywane w logu zdarzeń
* Stan aplikacji można odtworzyć na podstawie loga
	* lub na podstawie migawki wcześniejszego stanu i fragmentu loga od tamtego momentu
* Możliwość formułowania zapytań o konkretną chwilę w czasie
	* zdarzenia mają dołączone znaczniki czasowe
* Odtworzenie zdarzeń
	* np. jeśli któreś zdarzenie w przeszłości było niepoprawne
	* można wyjść od jakiejś migawki stanu aplikacji i odtworzyć ciąg zdarzeń żeby dostać nowy stan aplikacji
* Podobna idea jak systemy kontroli wersji (git)
* Ponieważ stan aplikacji da się wyliczać z loga zdarzeń można stosować różne podejścia do cache'owania
* Można implementować odwracanie zdarzeń


## Schemat w bazach danych
* Ciężko jest z góry zaprojektować schemat
* Trzeba pisać skrypty migrujące jeśli zmieni się model
* Schema - full
	* optymalizacja dostępu wg danego typu (indeksy)
	* łatwe do zrozumienia
	* uwzględnia związki
* Schema - less
	* elastyczność w dodawaniu typów
	* schemat powstaje iteracyjne
	* bez narzutu na utrzymanie więzów integralności po stronie bazy
	* szybszy deveopment
	* potencjalnie bałagan

## Zarządzanie zmianą w schemacie
* Liquibase
	* do baz SQL
	* schemat bazy danych też jest artefaktem

## Transakcje
* Nie zawsze są potrzebne
* Pytanie o ACID na egzmainach dyplomowych
* JTA
	* Java Transaction API
	* transakcja na wielu bazach jednocześnie
	* bardziej ogólne niż tylko bazy danych
	* two-phase commit
	* bardzo obciążająca wydajnościowo


## Replikacja i transakcje
* Twierdzenie CAP
* BASE
* W bazach relacyjnych klastry zazwyczaj polegają na master-slave

## JPA
* Generowanie tabelek na podstawie kodu Javy - wygodne
* Kod Javy na podstawie istniejącego schematu bazy - syfiasty kod
* Problem z powiązaniami
	* proste pola są wyciągane od razu
	* obiekty podrzędne są dociągane leniwie - ryzyko że zapytanie wyciągnie całą bazę
	* wzorzec Proxy

### Zapytania natywne
* Ograniczona przenośność
* Można wykorzystać pełne możliwości bazy

## CriteriaAPI
* Tworzenie zapytań przez wywołania metod w Javie
* Zabezpieczenie przed wstrzyknięciem

## JOQQ
* Generuje kod na podstawie bazy

## JCR
* Java Content Repository
* Kombajn all in one

## Wydajność
* Relacyjne bazy źle się klastrują
* Stosowane rozwiązania
	* optymalizacje
	* cache 2 poziomu
	* sharding pionowy i poziomy
	* separacja bazy transakcyjnej i analitycznej
	* separacja baz do edycji i do odczytu

### Cache
* Aplikacja
* EntityManager - poziom 1
* EntityManagerFactory - poziom 2
* Driver JDBC (niskopoziomowy)

Standard JCache
EntityManager będzie np cache'ować zapisy żeby emitować jeden UPDATE zamiast wielu następujących po sobie

Cache poziomu 2