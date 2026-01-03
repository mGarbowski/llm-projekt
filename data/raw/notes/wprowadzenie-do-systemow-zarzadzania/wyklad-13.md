# Systemy Business Intelligence, Big Data (2024-06-03)

Będzie jedno pytanie z ostatnich 2 wykładów na kolosie

## Business Intelligence
* Zbiór technik i narzędzi przekształcających dane operacyjne w użyteczną wiedzę biznesową
	* wykorzystanie w procesach podejmowania decyzji
	* wspieranie działalności operacyjnej 
* Analiza danych historycznych i aktualnych
* Dostarcza informacje o charakterze prognostycznym

## Techniki BI
* Raportowanie
* Online Analytical Processing (OLAP)
* Analytics
* Data mining, text mining
	* analiza komentarzy
* Complex Event Processing (CEP)
	* przetwarzanie i analityka w czasie rzeczywistym

## Przechowywanie danych
* Bazy danych
* Hurtownie danych
	* zbieranie danych z wielu źródeł
	* inne silniki
	* inny sposób modelowania
* Bazy wielowymiarowe
* Specjalizowane rozwiązania typu Big Data
	* Volume Velocity Variety (3V)
	* duża ilość danych
	* duża zmienność
	* duża różnorodność

## Hadoop Distributed File System
* HDFS
* Do przetwarzania danych strumieniowych
* Zrównoleglenie, bardzo dużo węzłów
* Węzeł nadrzędny i wiele datanodes
* Blok danych replikowany między węzłami
* Pozwala na rozproszenie geograficzne
* Redundancja danych, zabezpiecza przed awarią
* Dobrze skalowalne, można dodawać węzły

## OLAP
* Narzędzie informatyczne przeznaczone do wielowymiarowych i hierarchicznych analiz danych
	* wymiary i miary
* Rzutowania, agregacja
* Hierarchia
	* np. wymiar czasu - rok, miesiąc, dzień
* Kokpit zarządzania
	* predefiniowane i własne widoki dla użytkownika
	* możne definiować na bieżąco

## Architektura systemu analitycznego
* Wiele baz danych (operacyjnych)
* Hurtowania danych
	* operational data store - odseparowane
	* zbiera dane z wielu baz danych
* OLAP server
	* struktury wielowymiarowe
* Aplikacje
	* graficzna prezentacja

## Przegląd rozwiązań BI
* Dla małej ilości danych
	* Excel z tabelami przestawnymi
* Z łatwo konfigurowalnymi analizami
	* Power BI
	* QlikView
	* Tableau
* Analityka z wykorzystaniem chmury
	* Qubole
* Analityka z wykorzystaniem BigData
	* Apache Kylin
* Rozwiązania z zaawansowaną analityką
	* SAS
	* IBM
	* SAP

### Excel
* Zalety
	* szybkie analizy
	* znane narzędzie
* Wady
	* słabo skalowalne

### Power BI
* Microsoft - też inne narzędzia
	* Hadoop
	* SQL Server
	* SharePoint
	* warstwa integracyjna
	* warstwa dostępu do danych (Excel)
* Architektura (oparta na chmurze)
	* Power BI na samym końcu jako warstwa prezentacji danych
	* ładowanie danych strumieniowych
* Zalety
	* duże możliwości
	* zintegrowane rozwiązania
* Wady
	* vendor lock-in, wszystko trzyma Microsoft
	* wersja on-premise jest bardzo ograniczona
	* koszty
* Wspiera skrypty Pythonowe

### QlikView
* Wiele rozwiązań in-memory
* Architektura
	* wiele źródeł danych
	* serwer przechowujący dane
	* wiele aplikacji klienckich / wyjść

### Tableau
* Prosty interfejs użytkownika


## Rozwiązania chmurowe
* Infrastructure as a Service
	* wynajmuje się tylko infrastrukturę (serwery)
* Platform as a Service
	* aplikacja na dostarczonej platformie analitycznej
* Software as a Service
	* całe oprogramowanie dostarczone jako usługa chmurowa
* Przykłady rozwiązań analitycznych
	* Sisense
	* Microsoft Power BI Pro
	* ...

### Qubole
* Rozproszone
* Integruje dane z różnych chmur obliczeniowych

### Apache Kylin
* Open Source
* Wejście
	* Apache Kafka - dane strumieniowe
* Widoki - Power BI, aplikacje webowe
* Silnik do bardzo szybkiego przetwarzania danych
	* struktury kostkowe

### SAS Intelligence Platform
* Źródła danych
	* płatne usługi dla różnych źródeł
* Serwery SAS
	* metadane
	* workspace - wykonywanie obliczeń
	* OLAP - ze strukturami kostkowymi
	* process server - przetwarzanie dla aplikacji typu Excel
* Warstwa pośrednia
* Aplikacje klienckie
	* Enterprise Guide
	* Enterprise Miner - data mining
	* Data Integration Studio - integracja danych na poziomie korporacji

### IBM
* Dedykowane rozwiązania dla
	* business intelligence
	* analiza predykcyjna
	* zarządzanie wydajnością
	* analiza ryzyka
* Dedykowane dla dużych firm

### SAP HANA
* Wizualizacje
* Dane rozproszone
* Dla dużych firm


## Open Source OLAP
* Pentaho from Hitachi Vantara
	* tylko część funkcjonalności
* JasperReports Library
* Mondrian
* Cubes
* Apache Kylin

## Analiza dostępnych narzędzi
* Microsoft ma największą bazę użytkowników

## Multidimensional Expressions
* MDX
* Odpowiednik SQL dla danych wielowymiarowych
* Do skonfigurowania środowiska przez informatyka

## Big Data Analytics
* Volume - duża ilość danych
* Variety - duża różnorodność danych\
* ...

### Hadoop i SAS
* Rozproszone przetwarzanie pozwala drastycznie przyspiedszyć obliczenia (np. regresji)

## Data mesh
* Dzielenie danych i wyników między zespołami
## Event Stream Processing
* Praca bezpośrednio na strumeiniu danych
* Np. dane z czujników