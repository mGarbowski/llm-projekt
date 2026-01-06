# Logika biznesowa

## Definicje
* Reguły biznesowe definiują pojęcia i polityki niezbędne dla działania biznesu
* Proces biznesowy to seria powtarzalnych kroków wykonywanych prezz organizację w celu uzyskania pożądanego efektu (celu biznesowego)
* Logika biznesowa to część aplikacji odpowiedzialna za realizację przyjętych reguł biznesowych

### Poprawna implementacja logiki biznesowej
* Czysty kod i czysta architektura
* Niskie sprzężenie (low coupling)
	* minimalne zależności między modułami
* Wysoka spójność (high cohesion)
	* zasada pojedynczej odpowiedzialności

### Interfejs / API
* Abstrakcja definiująca kontrakt między współpracującymi elementami
	* obiekty, komponenty, moduły, usługi, mikroserwisy
* Określa możliwe sposoby interakcji
* Ukrywa szczegóły implementacyjne

### Wzorzec projektowy
* Szablon najlepszego rozwiązania
	* odkrywany na drodze doświadczenia

### Inwersja kontroli (IoC)
* Odwrócenie sterowania wykonania programu
* Przeniesienie na zewnątrz odpowiedzialności za kontrolę wykonania
* Programista dostarcza kod, który będzie wykonany przez framework

### Wstrzykiwanie zależności
* Tworzenie, konfigurowanie i podawanie zależności *z zewnątrz*
* Zmniejsza sprzężenie między elementami aplikacji
	* swoboda wymiany implementacji
	* łatwiejsze testowanie
* Przykładowa realizacja
	* ręczne podawanie zależności przez argumenty konstruktora
	* wzorce projektowe, np. factory method
	* kontener zarządzający cyklem życia komponentów (Spring)

### Programowanie aspektowe
* Uzupełnia paradygmat programowania obiektowego
* Umożliwia oddzielenie logiki biznesowej od dodatkowych zadań pobocznych
	* transakcje, logowanie, bezpieczeństwo
* Często wykorzystuje się wzorzec Proxy

### Programowanie przez zdarzenia
* Umożliwia rozluźnienie powiązań
	* komponenty komunikują się, chociaż niewiele o sobie wiedzą
* Oparte o wzorzec Observer

## Architektura
* Definiuje najważniejsze komponenty, zakres odpowiedzialności, wzajemne relacje
* Stanowi szablon rozwiązania
* Może być definiowana na różnym poziomie
	* aplikacja
	* system

### Monolit
* Aplikacja rozwijana, testowana i wdrażana jako całość
	* jeden artefakt
* Zalety (do pewnego rozmiaru projektu)
	* łatwa nowych funkcjonalności biznesowych i pobocznych
	* mała złożoność infrastruktury
* Wyzwania (od pewnego rozmiaru projektu)
	* trudność utrzymania i rozwoju ze względu na rosnącą złożoność, zakres funkcjonalności i rozmiar aplikacji
	* ograniczona skalowalność
	* przywiązanie do określonych rozwiązań i technologii

### Modularny monolit
* Aplikacja rozwijana, testowana i wdrażana jako zbiór modułów
	* niezależne od siebei
	* dobrze zdefiniowane odpowiedzialności
	* publiczny interfejs (kontrakt)
	* mogą być reużywane w innych aplikacjach

### Architektura zorientowana na usługi (SOA)
* Rozwiązanie w postaci rozproszonych usług / komponentów
	* dobrze zdefiniowana odpowiedzialność
	* publiczny interfejs (kontrakt)
	* mogą współdzielić dane
	* integrowane z wykorzystaniem szyny (ESB) i standardowych protokołów

### Mikroserwisy
* Rozwiązanie w postaci rozproszonych mikro usług (mini aplikacji)
	* niezależne od siebie
	* dobrze zdefiniowana odpowiedzialność
	* publiczny interfejs (kontrakt)
	* nie współdzielą danych
	* komunikują się wyłącznie przez publiczne API

### Czysta architektura
* Centralnym elementem aplikacji jest logika biznesowa zaimplementowana w sposób niezależny od bibliotek, frameworków i użytej infrastruktury
* Wokół logiki biznesowej tworzone są kolejne, bardziej wysokopoziomowe warstwy
	* adaptery umożliwiające komunikację ze światem zewnętrznym

### Command Query Separation
* Każda metoda powinna być zaklasyfikowana do jednej z grup
	* command - zmienia stan aplikacji, nic nie zwraca
	* query - coś zwraca, nie zmienia stanu aplikacji

### Command Query Responsibility Segregation
* Idea CQS przeniesiona na poziom klas / komponentów / całego systemu
* Command
	* obiekt reprezentujący intencję użytkownika systemu
	* `UpdateItemQuantityCommand`
* Command Bus
	* kolejka dla przychodzących komend
	* router przekazująca zadania do odpowiedniego handlera
* Command Handler
	* waliduje otrzymane komendy
	* tworzy lub zmienia stan obiektu domenowego
	* utrwala zmiany za pomocą repozytorium (write database)
	* opcjonalnie przekazuje zdarzenia na Event Bus
* Domain objects, Aggregates
	* model domenowy i logika biznesowa
	* zmiany na obiektach tego typu generują zdarzenia
* Event
	* obiekt reprezentujący zmiany, które zaszły w domenie
	* `ItemQuantityUpdatedEvent`
* Event Bus
	* kolejka dla generowanych zdarzeń
	* router przekazujący zdarzenia do odpowiedniego handlera
* Event Handler
	* utrwala zmiany stanu w bazie danych do odczytu (read database)
* Read Database Abstraction
	* abstrakcja umożliwiająca odczyt danych (stanu domeny)

### Event Sourcing
* W CQRS zdarzenia są używane jako mechanizm synchronizacji dwóch baz danych
	* odczytu i zapisu
* Event Sourcing pozwala na odtworzenie aktualnego stanu aplikacji (obiektów domenowych) na podstawie zdarzeń składowanych w magazynie danych (Event Store)

### Wzorzec Saga i orkiestracja logiki
* Orkiestruje wykonanie transakcji przez jedne serwis, który wchodzi w interakcję z innymi serwisami
* Orkiestrator jako maszyna stanów
* Odpowiedzialny za rollback
* Komunikuje się z innymi serwisami za pośrednictwem kanałów brokera komunikatów

## Logika zdalna
* Logika dostępna przez sieć, realizowana w formie rozproszonego systmu
* Komunikacja może odbywać się n aróżne sposoby i z użyciem różnych protokołów
	* tekstowe i binarne
	* synchroniczne i asynchroniczne
	* oparta o zdarzenia, rpc, transferowanie stanu

### Usługi sieciowe (web services)
* Funkcjonalność dostępna przez sieć
* Zbiór standardów umożliwiających wyszukiwanie i wykorzystanie usług zdalnych
* Założenia
	* komunikacja w niejednorodnym środowisku
	* niezależność od platformy sprzętowej, programowej, transportowej
	* duża modularność i reużywalność
* Warstwa transportowa
	* HTTP/HTTPS
	* FTP
	* JMS
	* email
	* ...
* Warstwa komunikacji
	* protokół SOAP
	* dialekt XML
	* definiuje sposób wymiany informacji między konsumentem i producentem usługi
* Kontrakt / dokumentacja
	* dokument WSDL
	* dialekt XML
	* opisuje usługę, dostępne operacje i sposób ich użycia
	* nie ujawnia szczegółów implementacji
* Scenariusz użycia
	* dostawca publikuje dokument WSDL w ustalonym katalogu
	* konsument pobiera WSDL
	* konsument wysyła żądanie do serwera protokołem SOAP
	* producent przetwarza żądanie i odsyła odpowiedź protokołem SOAP
* Dokument WSDL
	* kontrakt
	* opis usług i informacje niezbędne do ich użycia
	* parametry wejściowe, zwracane wyniki, wyjątki, sposób dostępu
	* dokument XML
* Obsługa danych binarnych
	* obrazy, audio, video
	* zakodowanie do postaci tekstowej (base64) w ciele wiadomości
	* załącznik do wiadomości SOAP

#### Kodowanie base64
* Narzut na objętość danych
* Narzut na kodowanie i dekodowanie
* Rozsądne tylko dla stosunkowo małych załączników