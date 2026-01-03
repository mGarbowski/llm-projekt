# Wstęp
## Inżynieria wymagań

### Rodzaje wymagań
* Funkcjonalne
	* odnoszoą się do tego co system ma robić
	* jakie powinien mieć funkcje biznesowe
	* mówią CO, a nie JAK
* Niefunkcjonalne (pozafunkcjonalne)
	* odnoszą się do cech systemu
	* wydajność
	* ergonomia
	* bezpieczeństwo
	* kluczowy wpływ na architekturę
	* mogą mieć kluczowe znaczenie dla klienta
	* muszą być precyzyjne i weryfikowalne

### Attribute-driven design
* Wymagania funkcjonalne
* Wymagania jakosciowe
	* skalowalność
	* bezpieczeństwo
	* dostępność (bezawaryjność)
	* dostępność (WCAG / ergonomia)
	* interoperacyjność (komunikacja z innymi systemami)
	* stabilność / niezawodność (uptime)
	* rozszerzalność
	* szybkość wytwarzania (time to market)
	* zgodność z ustawami
* Ograniczenia
	* technologiczne
		* klient ma serwery o maksymalnie 64GB RAM
		* zespół pracuje w Javie
	* biznesowe
		* czas
		* budżet
		* system krytyczny dla działania organizacji

Rozróżnienie między wymaganiami a ograniczeniami nie do przeskoczenia

#### Potencjalne konflikty
* rozszerzalność vs niezawodność
* time to market vs rozszerzalność
* time to market vs wydajność

#### Wydajność
* Systemy low latency
* Systemy high-throughput
* Ważny szybki zapis / ważny szybki odczyt / oba

### Osie złożoności
* Liczba technologii
* Rozmiar projektów
* Rozmiar i zróżnicowanie zespołów
* Infrastruktura i integrowalność
* Złożona domena
* Zmienność wymagań i podążanie za zmianą

## Standardy Java
* jcp.org - Java Community Process
* Ustandaryzowany proces wpływania na rozwój Javy
* Ma nie być uzależniona od jednego dostawcy
* Jedna specyfikacja, wiele implementacji
	* np. JPA jest pustą specyfikacją, dostawcy dostarczają implementacji (np. Hibernate)
	* implementacje można wymienić
* Standard często będzie w tyle za natywnymi rozwiązaniami bibliotek

## ADR
* Architecture Decision Records
* Dokumentuje się decyzje architektoniczne w jakimś szablonie
	* czemu wybrałem tą bazę a nie tą
* Powinny zostawać w firmie na przyszłość
* Przykładowo zawiera
	* tytuł
	* status
	* kryteria ewaluacji
	* kandydaci do rozważenia
	* research i analiza dot. każdego z kandydatów
	* rekomendacja

## Architektura komponentowa
* Ukrycie złożoności warstwy komunikacyjnej przed deweloperem logiki biznesowej
	* programista nie myśli o puli wątków, połączeń z bazą danych itd
* Middleware zarządza takimi aspektami jak
	* transakcje
	* wielowątkowość
	* bezpieczeństwo
	* klastry
	* failover
	* cykl życia obiektów

## Architektura wielowarstwowa
* Warstwa prezentacji
	* klient *thin* (webowy opart o servlety, JSP, JSF)
	* klient *thick* (webowy oparty o Angular, React, komunikujący się z API)
* Warstwa logiki biznesowej
* Warstwa trwałości

## Dependency Injection
* Wzorzec architektoniczny polegający na usunięciu bezpośrednich zależności pomiędzy komponentami systemu
* Odpowiedzialność za tworzenie obiektów przeniesione do zewnętrzenej fabryki obiektów - kontenera
* Kontener na żądanie tworzy obiekt lub zwraca istniejący z puli ustawiając powiązania z innymi obiektami

## Narzędzia
* Na poziomie programisty
	* IDE
	* narzędzia automatyzacji budowania
	* budowa i uruchamianie testów jednostkowych
* Na poziomie zespołu programistycznego
	* repozytorium kod źródłowego
	* narzędzia przegląda kodu
	* repozytorium bibliotek / wydań
	* serwery ciągłej integracji
	* analiza pokrycia kodu testami
	* system przydziału i kontroli realizacji zadań, planowanie wydań
* Na poziomie wdrożenia
	* serwery ciągłego wdrożenia
