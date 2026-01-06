# Integracja systemów (2024-12-09)

## Rodzaje integracji

### Integracja danych
* Różne źródła danych
* Różne formaty danych
* Proces ETL
	* extract, transform, load
* Data Flow Diagram (DFD)
* Apache Flink
	* narzędzie z ekosystemu Javy
* Arkusze migracyjne
	* klient przygotowuje dane
	* widoki SQLowe
	* arkusze w excelu

## Strategie integracji

### Integracja przez pliki
* Jeden system eksportuje dane do pliku
* Drugi system importuje dane z pliku
* Najstarsza i najprostsza metoda integracji
* Wymaga uzgodnienia formatu pliku
* Do operacji batchowych, gdzie jest bardzo dużo danych może być całkiem ok
* Nie ma dużego problemu jeśli jeden z systemów leży
	* plik może poczekać w katalogu
* Systemy nie muszą nic o sobie wiedzieć
* Komunikacja jest asynchroniczna
	* nie muszą być jendoczesnie aktywnie
	* nie da się pobierać danych na żywo
	* dane wędrują z opóźnieniem
* Komunikacja jednokierunkowa
* Różne protokoły
	* FTP
	* NFS
	* S3
* Nie ma sensownej obsługi błędów
* Rytm dostarczania plików może generować problemy
* Sensowny dla plików binarnych
* Nie jest sensowny dla metadanych

### API/RPC
* Oba systemy muszą działać jednocześnie
* Może być dwukierunkowy przepływ danych
* Nie jest zależne od szczegółów implementacyjnych (jaka baza itp)
* Może być problem wydajnościowy przy dużych ilościach danych
* Wymaga decyzji kto kogo woła
	* push vs pull
	* problemy projektowe, może wymagać pracy po stronie innego zespołu / podmiotu
	* dodatkowy aspekt wpływający na wydajność - jak inne systemy korzystają z naszego API
* Problem jeśli zmieni się API
* Problem jeśli API nie ma wszystkich potrzebnych metod
* Niemożliwe do zastosowania w starych systemach nie wystawiających API
* Problem jeśli jest wiele systemów
* Łatwe do analizy
* Dobra granulacja bezpieczeństwa
* Dostęp do danych na żywo

#### Protokoły binarne vs tekstowe
* Binarne protokoły bardziej wydajnie pakują dane
* Problemy z serializacją danych przy binarnych protokołach
* Łatwość debugowania tekstowych protokołów

### Integracja przez bazę danych
* Są mechanizmy transakcji
* Asynchroniczny
* Może system nie musi chodzić jeśli system jest na innym serwerze
* Nie ma takiego narzutu jak API
* Przywiązany do szczegółów implementacyjnych
	* kwestia granulacji informacji
	* można użyć widoków albo procedur składowanych jako API
* Można się zintegrować z prawie każdym systemem
* Radzi sobie z dużą ilością danych
* Da się pobrać dane i na żywo i asynchronicznie
* Praktyczne jedyne podejście transakcyjne
* Trudne do analizy
* Słaba granulacja bezpieczeństwa
* Łatwo coś popsuć w drugim systemie
* Duże ryzyko, że jeśli system się zmieni to integracja przestanie działać

### Szyna komunikatów
* Message broker
	* np. JMS
	* obsługuje trasowanie - nie każdy system musi o wszystkim wiedzieć
	* granulacja bezpieczeńśtwa
	* single point of failure
* Asynchroniczna komunikacja
* Tam gdzie istotna jest niezawodność i wiele systemów
	* odciąża systemy z obsługi komunikatów
* Gwarantuje dostarczenie
* Standaryzuje wiele systemów
* Rzadko da się zastosować
	* to decyzja organizacji

#### JMS
* Kolejka - jeden do jeden
* Topic - publish and subscribe
* Poziomy gwarancji dostarczenia
	* at most once
	* at least once - często wystarcza ale wymaga obsługi duplikatów u odbiorcy
	* exactly once - najcięższe wydajnościowo

#### AMQP
* Agnostyczny względem technologii

#### Technologie
* RabbitMQ
* Apache ActiveMQ
* Mule ESB

#### Kafka
* Wymiana komunikatów
	* trochę jak integracja przez bazę danych ...

#### Szyna vs message broker
* Szyna obsługuje wiele różnych protokołów
	* np. adaptery do SOAP i REST
* ESB obsługuje orkiestrację
	* zdarzenie inicjuje zdefiniowany workflow
* Szyna często przywiązuje do konkretnego dostawcy
* Szyna jest mądra i wie gdzie wszystko dostarczyć

#### Outbox pattern
* Uniknięcie problemu rozproszonych transakcji

#### Saga
* Implementacja długotrwałej transakcji
* Rozbicie długotrwałego procesu na krótkie etapy
* Każdy kawałek jest transakcyjny
* Zamiast wycofania jest kompensacja
	* np. nie da się odrezerwować hotelu - trzeba wykonać anulowanie

## Błędy, wersjonowanie
* Wersjonowanie przez ściezki URL
* Wersjonowanie przez nagłówki Accept
* Forwards compatibility
	* co jeśli nowa wersji systemu zwróci więcej danych niż poprzednia wersja (np. dodatkowe pola)
	* problemy przy głupim parsowaniu
	* powinna być przynajmniej sensowna obsługa błędów

### Błędy biznesowe i techniczne
* Techniczne
	* zerwane połączenie, przeciążenie systemu
* Błąd biznesowy
	* błędy walidacji

## Enterprise Integration Patterns
* Stara książka
* EAI
* Wzorce implementowane np. w Springu
* Wzorce bezstanowe
	* filtry
	* translacja
	* wzbogacanie - np. zamiast dużego zdjęcia wprowadzić id jak można się do niego dobrać z innego źródła lepiej zoptymalizowanego pod dane binarne
	* split
	* throttle - krytyczne systmy, których nie wolno zapchać
		* przydatne przy okresowych importach
		* zadania do przetworzenia *o północy*
* Wzorce stanowe
	* claim-check - wykorzystuje zewnętrzne repozytorium, podobne do enricher
	* agregacja - sklejanie wiadomości z różnych systemów
	* scatter-gather - rozproszenie przetwarzania

Nie zawsze dostarczanie dobrego API do systemu jest w interesie dostawcy

