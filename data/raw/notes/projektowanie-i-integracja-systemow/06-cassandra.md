# Apache Cassandra
* Open source, licencja Apache2
* Rozproszona
	* zapewnia odporność na awarie
* Możliwość wymieniania komponentów bez wyłączania systemu
	* np. wymiana dysków twardych
* Przystosowana do ogromnych zbiorów (terabajty, petabajty)

## Model danych
* Zbliżony do modelu relacyjnego
* Tabele, kolumny, wiersze
* Statyczny schemat
* Partycjonowane tabele
	* podzielone między fizyczne serwery
	* klucz partycjonujący - wartość decyduje gdzie w klastrze zostanie umieszczony wiersz
* Klucz główny
	* zawiera klucz partycjonujący
	* dodatkowe kolumny, decydują gdzie w ramach jednego serwera będzie przechowywany wiersz
	* dodatkowe kolumny ustalają porządek w obrębie partycji
* Cała partycja jest na jednym serwerze
* Z każdą komórką danych jest związany znacznik czasowy
	* ten sam wiersz może być zapisany równocześnie przez 2 klientów na różnych serwerach
	* serwery są symetryczne, klient nie musi wiedzieć gdzie dokładnie będzie zapisany wiersz
	* późniejsze dane nadpisują wcześniejsze
	* bardzo ważne jest zsynchronizowanie zegarów między serwerami w klastrze - mogą wracać stare dane, mogą znikać
	* z każdą komórką można skojarzyć TTL, po upływie zamienia się na null
* Fizycznie każda komórka tabeli jest zapisywana jako nazwa kolumny i wartość
	* model dostosowany do rzadkich tabel (dużo nulli)

## Typy danych
* Standardowe jak w tabelach relacyjnych
* Typy zdefiniowane przez użytkownika
	* struktury
* Kolekcje
	* zbiór
	* lista
	* słownik
	* wektor - szczególnie do algorytmów ML

## Różnice z bazami relacyjnymi
* Nie ma kluczy obcych
* Nie ma złączeń
	* możne zrobić je ręcznie w aplikacji
* Nie ma operatorów algebry relacyjnej
* Nie ma group by
* Nie ma podzapytań
* Bardziej ograniczony język zapytań
* Nie jest dobra jako baza analityczna
	* można dostawić obok inny system (np. Solr, Elastic Search, Spark)

## Interfejs
* Cassandra Query Language
* Podony do SQL
* Wiele insertów na ten sam klucz główny
	* ważny jest ostatni
* Można zrobić update dla nieistniejącego rekordu
	* utworzy się nowy rekord
	* update i insert są tłumaczone na to samo polecenie
	* każda aktualizacja to dopisanie nowej informacji o komórkach
* Sterowniki do większości języków programowania
* REST
* gRPC

### Joiny
* Brak złączeń rozwiązuje się denormalizacją danych
	* zapisujemy te same dane w różnych postaciach w różnych tabelach
	* projektujemy struktury danych pod zapytania jakie będą wykonywane
* Pola typu kolekcji
* Złączenia byłyby bardzo kosztowne w systemie rozproszonym

### Lekkie transakcje - Insert
* `INSERT INTO ... IF NOT EXISTS`
* `UPDATE ... IF ...`
* Atomowa, niepodzielna operacja
* Algorytmy bez blokad
* Bardzo kosztowne
	* 3-4 razy więcej niż normalnie
* Algorytm Paxos, Raft (nie na kolosa)

## Architektura
* Nie ma single point of failure
* Serwery są całkiem symetryczne
* Zapytania mogą trafiać do dowolnego serwera
* Serwery komunikują się między sobą
* Klucz partycjonujący decyduje gdzie zostaną umieszczone dane
* Funkcja skrótu murmur64
	* każdy węzeł ma przypisany zakres
	* dzieli sie po równo zakresy wartości haszy
	* różne wartości klucza - będzie równomierne obłożenie
* Dowolny węzeł może paść
* Dowolny węzeł może być zastąpiony bez downtime systemu

### Replikacja
* Np. jak są serwery ABCD i z hasza wynika że wiersz ma trafić na serwer A to zostanie zapisany na ABC, jeśli B to BCD itd
* Współczynnik replikacji
	* zalecany 3
	* lepsze są nieparzyste

### CAP
* Cassandra umożliwia wybór między spójnością i dostępnością

### Rodzaje spójności
* Eventual consistency - spójność ale po jakimś czasie
* Immediate consistency - każdy klient odczytuje najbardziej aktualne dane
* Serial consistency - widoczny stan bazy taki jak gdyby wszystkie operacje były sekwencyjne
	* lightweight transactions
* Współczynnik spójności
	* podaje się przy zapytaniu
	* ile replik ma potwierdzić operację
	* any - dowolny (może być koordynator)
	* one - jedna z replik
	* local_one - w tym samym centurm danych
	* two
	* quorum - więcej niż połowa (dlatego lepsze są nieparzyste współczynniki replikacji)
	* zapis z quorum 2z3 i odczyt z quorum 2z3 - na pewno będzie aktualna wartość
	* local_quorum
	* each_quorum
	* serial
	* all
* CL.READ + CL.WRITE > RF gwarantuje natychmiastową spójność
	* replication factor
* Zapis dalej idzie do wszystkich replik

### Write Path
* Zapis trafia do memtable i commit log
	* commit log - dysk, dane dopisywane na koniec
	* memtable - pamięć, dane posortowane wg klucza
* Po awarii serwer może odtworzyć stan na podstawie commit logu
* Kiedy zabraknie miejsca w memtable
	* flush - zapis memtable do jednego pliku na dysku (SSTable)
	* system operacyjny potwierdza że zapis się skończył
	* czyści się commit log - dane już są na dysku
	* można znowu zapisywać
* Kiedy operacja odczytu
	* trzeba sprawdzić wszystkie miejsca - memtable i wszystkie SSTable
	* szybkie bo dane są posortowane
* Z każdym flush rośnie liczba miejsc które trzeba przeszukiwać przy odczycie
	* filtry blooma do SSTable
	* właściwe rozwiązanie - scalanie (compaction)
* Compaction
	* scalanie SSTable jak w mergesort
	* jeśli 2 razy ten sam klucz to rozstrzygnięcie na podstawie znacznika czasowego
	* scalony plik jest na ogół mniejszy niż suma 2 przed scaleniem
	* jeśli trafi na znacznik usunięcia i dane to nie zapisze danych
	* oryginalne SSTable są usuwane
* Usuwanie
	* dopisuje się znacznik usunięcia
	* ze znacznikiem czasowym
	* nie kasuje się danych
	* GC grace period domyślnie ustawiony na tydzień - czas po którym znacznik usunięcia zostanie usunięty o ile dane zostały już scalone
	* serwer w klastrze mógł być wyłączony i nie dostać informacji o usunięciu, a ma stare dane, jeśli jeszcze jakiś serwer ma znacznik usunięcia to system nie zwróci usuniętego rekordu, jeśli nie będzie to system zwróci usunięte dane (resurrection)
	* są różne mechanizmy które przed tym zabezpieczają

SSTable - sorted string table, dane posortowane po kluczu głównym

### Secondary indexes
* Zapytanie po kolumnie bez indeksu rzuca wyjątek
	* domyślnie nie można robić zapytań które wymagają filtrowania
	* opcja allow filtering do zapytania - może być timeout
* Do każdego SSTable dołącza się indeks
* Dane dla poszczególnych kolumn w oddzielnych plikach
* Dane wspólne w jednym pliku per sstable
* Indeksy są oszczędne - tylko numery (wiersze w sstable można ponumerować)
* Przy odczycie z indeksem trzeba przejrzeć wszystkie indeksy
* Zapytanie z wieloma indeksami
	* obliczenie przecięcia na zbiorach posortowanych
