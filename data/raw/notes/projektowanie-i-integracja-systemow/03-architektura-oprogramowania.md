# Architektura oprogramowania

## Architektura
* Zbiór decyzji projektowych
* Zestaw decyzji na odpowiednim poziomie abstrakcji dotyczących struktury systemu, które mają kluczowy wpływ na jego zachowanie, rozwój i utrzymanie
* Nie ma jednej definicji

## Zbiór decyzji projektowych
* Jak podzielić system na zarządzalne fragmenty, jak duże powinny być
* Czy i gdzie konieczna jest spójność danych
* Jakie protokoły i kanały komunikacji zostaną użyte
* Jakie technologie zostaną użyte
* Jak zapewnić trwałość danych
* Jakie będzie środowisko wdrożeniowe
* Jak zapewnione będzie bezpieczeństwo systemu

## Ogólny widok systemu
* Jak system jest podzielony na części
* Abstrakcyjna reprezentacja systemu, która pozwala zobaczyć jego główne komponenty i sposób ich interakcji bez wnikania w szczegóły implementacyjne
* Różne rodzaje widoków ze względu na perspektywę

## Widok techniczny
* Komponenty i komunikacja między nimi
* Jak system jest wdrożony
* Definiuje wzorce projektowe i technologiczne wykorzystywane do budowy systemu
	* np. styl architektoniczny (monolit, mokroserwisy, SOA)

## Kiedy powstaje architektura
* Każdy system ma jakąś architekturę
	* czasami przypadkową
* Architektura up-front vs architektura zwinna
	* ustalenie wymagań z góry nie jest dobrym pomysłem
	* wymaga poprawek, zmian
	* wymagania zmieniają się w czasie
	* zwinna - zakładamy tylko tyle ile potrzebujemy na danych etapie
* Architektura ewolucyjna
	* minimalne założenia
	* z czasem dokładamy kolejne decyzje

## Poziomy definiowania architektury
* Poziom organizacji
* Poziom systemu (domeny biznesowej)
* Poziom aplikacji

### Architektura organizacji (enterprise)
* Polityka organizacji
* Polityka bezpieczeństwa danych
* Działania na poziomie strategicznym
* Mało technikaliów
* Cel
	* powiązanie procesów biznesowych z technologią
	* definiowanie interfejsów i protokołów komunikacji
	* Zapewnienie skalowalności, niezawodności i dostępności całego systemu
	* Zarządzanie przekrojowymi aspektami - integracja, wydajność, bezpieczeństwo

### Architektura systemu
* Zakres - grupa systemów / podsystemów
* Decyzje i struktura zintegrowanej grupy aplikacji lub usług, które realizują określone funkcje
* Pomost pomiędzy planowaniem na poziomie przedsiębiorstwa, a poszczególnymi aplikacjami
* Cel
	* projektowanie podsystemów, które współpracują ze sobą w celu realizacji celów biznesowych
	* definiowanie interfejsów i protokołów komunikacji
	* zapewnienie skalowalności, niezawodności, kompatybilności i dostępności całego systemu
	* zarządzanie przekrojowymi aspektami - integracja, wydajność, bezpieczeństwo

### Architektura aplikacji
* Zakres - pojedyncza aplikacja
* Zapewnienie zgodności z wymaganiami
* Jakie wzorce projektowe
* Zapewnienie łatwości utrzymania
* Odpowiedzialność programistów
* Na tym poziomie definiuje się wymagania funkcjonalne i częściowo niefunkcjonalne
* Cele
	* definiowanie wewnętrznej struktury (podział na warstwy, komponenty)
	* realizacja wymagań funkcjonalnych i niefunkcjonalnych
	* wybór wzorców i fizycznej struktury aplikacji
	* zarządzanie cyklem rozwoju, wdrożeń, zapewnienie jakości

## Wymagania funkcjonalne
* Jakie funkcje ma udostępniać dany system
* Jakie problemy biznesowe ma rozwiązywać

## Ograniczenia projektowe
* Jakie są ograniczenia środowiska, w którym system będzie działał
* Technologiczne
* Biznesowe
* Prawne (RODO)
* Czasowe
* Czy to ma być dostarczone użytkownikowi, czy budujemy prototyp

## Wymagania niefunkcjonalne/jakościowe
* Cechy architektoniczne
* Dostępność, skalowalność, bezpieczeństwo itd.

## Architektura zawsze jest kompromisem
* Nie ma uniwersalnej architektury
* Optymalizacja jednej cechy może osłabiać inną
* Dopasowujemy architekturę do danego kontekstu
* Przykładowe kompromisy
	* dostępność vs koszt
	* wydajność, elastycnzość vs wymagana spójność danych
	* bezpieczeństwo vs wygoda
	* time to market vs jakość
	* utrzymywalność vs wysoka wydajność

## Popularne architektury
* Monolityczne
	* warstwowe
	* modularne
	* mikrokernel
* Rozproszone
	* mikroserwisy
	* service-based
	* service-oriented
	* event-driven
	* space-based

Mark Richards - youtube, software monday

Architecture styles worksheet - ściąga

### Architektura warstwowa
* Zalezności tylko w dół
	* warstwa wyżej zależy tylko od warstwy niżej
* MVC
* Warstwy
	* prezentacji
	* biznesowa
	* serwisów
	* trwałości
	* bazy danych
* Pominięcie warstwy serwisów - architektura otwarta
* Mało skomplikowana, przejrzysta
* Łatwo testowalna
* Stosunkowo szybka w implementacji
* Pasuje do zespołów wyspecjalizowanych technicznie
	* zespół dzieli się na wyspecjalizowanych w bazach danych, frontendzie, domenie biznesowej
* Gorzej się sprawdza przy skomplikowanych zmianach biznesowych
	* wszystkie reguły biznesowe są w ramach jednej warstwy
* Nie ułatwia izolacji modułów
	* podział poziomy
* Trudna skalowalność

### Mikroserwisy
* Wiele osobnych aplikacji współpracujących ze sobą
	* gęsta sieć zależności
* Każda funkcja biznesowa jest zamknięta jako osobna aplikacja
* Użytkownik nie wie z którym serwisem rozmawia
* Użytkownik komunikuje się z API gateway
* Różne poziomy granulacji
* Bardzo skomplikowane wdrożenie
	* trzeba zapewnić wiele serwerów
	* połączenia sieciowe między komponentami
	* dane nie zawsze dojdą do innego serwisu
	* problem ze spójnością danych
* Niezależne wdrożenia przez niezależne zespoły
	* np. każdy serwis należy do innego zespołu
* Lokalna skalowalność
	* pojedynczy serwis jest częściej używany
	* można przeskalować jeden serwis bez skalowania reszty
* Ograniczone pole rażenia w przypadku awarii
	* padnięcie jednego serwisu nie powinno być odczute przez inne
	* zależności powinny być tak asynchronicznie jak to możliwe
	* zakolejkowanie zdarzenia na później
	* obejście niedziałającego serwisu
* Małe konteksty, łatwość utrzymania i rozwoju
* *Right tool for the job*
	* używamy tej technologii która jest dobra dla danego problemu
	* w praktyce nie stosowane, trudne do utrzymania
* Gigantyczna złożonośc infrastruktury
* Spójnośc danych, komunikacja, problemy systemów rozproszonych
* Testowalność, zapewnienie zgodności usług między sobą
	* nie ma jednej aplikacji którą możemy sobie postawić i przetestować w izolacji
* Serwisy nie powinny współdzielić baz danych

### Architektura zdarzeniowa
* Zdarzenie w systemie jest faktem, system musi na niego zareagować
* Wiele luźno połączonych systemów
	* seriwsy nie komunikują się bezpośrednio
	* wysyłają zdarzenia na medium komunikacji
	* inny system obsłuży zdarzenie kiedy będzie w stanie
* Skalowalność (odbiorców zdarzeń) i elastyczność
* Asynchroniczne przetwarzanie ułatwia budowanie wydajnych systemów
* Asynchroniczne przetwarzanie izoluje ryzyko zmniejszonej dostępności
* Utrudniona testowalność, problemy z rozwojem
	* pośredniczy message broker
	* przebieg zdarzeń jest niedeterministyczny, nie ma modelu request-response
* Nie ma prostego API, bardzo złożona
* Asynchroniczność nie pozwala na model request-response
* Wyzwanie z projektowaniem granulacji zdarzeń

## SOA, ESB - architektury w aplikacjach
* Podobna koncepcja do mikroserwisów
	* z czasów przed możliwościami technologicznymi dla mikroserwisów
* Enterprise service bus
	* szyna danych z którą rozmawiają wszystkie serwisy
	* wiele odpowiedzialności szyny
* Bardzo drogie we wdrożeniu i utrzymaniu
* Charakterystyczne dla dużych korporacji
* Bez izolacji baz danych
* Trudne w utrzymaniu i ewolucji
* Często systemy zastane
* Centraliza zarządznia komunikacją
* Single point of failure - awaria szyny zabija system
* Zmniejszenie powiązań - systemy nie wiedzą o sobie
* Złożone wdrożenie ze względu na generyczność ESB
* Standaryzowana transformacja danych
* Orkiestracja usług
* Vendor lock-in

### Modularny monolit
* Monolit podzielony na dobrze odizolowane fragmenty wewnątrz
	* podział domenowy
* Pojedyncze wdrożenie
* Łączy architekturę monolityczną z mikroserwisami
* Rozdzielenie funkcji biznesowych
* Nieskomplikowana infrastruktura wdrożeniowa
* Komunikacja w ramach jednego procesu na serwerze
* Bez problemów systemów rozproszonych
* Łatwość rozwoju kodu w miarę odkrywania domeny
* Otwarta droga do potencjalnej migracji na osobne usługi
* Problematyczna skalowalność - wszystko albo nic
* Mała izolacja błędów
* Dłuższe wdrożenie
* Konflikt przy pracy dużych zespołów

## Jak wybrać architekturę

### Techniki odkrywania driverów
* Analiza wymagań funkcjonalnych i niefunkcjonalnych
* Metody warsztatowe
	* spotkania z klientami, którzy wiedzą co chcą uzyskać
	* event storming
	* event modelling
	* domain storytelling
* Heurystyki
* Wardley maps - narzędzie do *modelowania strategicznego*
	* ewolucja systemu w kontekście potrzeb biznesowych
* Cokolwiek co się sprawdza

Charakterystykę zespołu też bierze się pod uwagę przy wyborze architektury
Czy istnieją komponenty krytyczne pod kątem dostępności
Gdzie są krytyczne dane

## Dokumentowanie architektury
* Model C4 dokumentacji architektury
	* c4model.com
	* metajęzyk
	* opisywany w kodzie
* Rejestr decyzji architektonicznych - ADR
	* architecture decision record
* Dyskusje dotyczące ważnych aspektów architektury - RFC
* Narzędzia
	* Enterprise Architect
	* diagramy UML

### C4
* Context
	* środowisko w jakim działa system
	* jak ma się system do użytkownika
* Containers
	* aplikacje, komponenty wysokopoziomowe
	* z punktu widzenia logicznego / wdrożenia
	* jednostki wdrożeniowe
* Components
	* komunikacja między częściami serwisu
	* co rozmawia z bazą danych
* Code
	* rzadko używany
	* kod za szybko się zmienia

### ADR
* Bardziej znaczące decyzje dokumentujemy
* Ustalony szablon
* Status - wdrożona / odrzucona
* Kontekst
* Konsekwencje

### Jak pilnować architektury
* ArchUnit do Javy
	* nakłada się reguły na architekturę traktowane jako testy
	* np. zależności między pakietami

## Dwa i pół prawa architektury
* Wszystko w architekturze oprogramowania to kompromis
* ***Dlaczego** jest ważniejsze niż **jak**
* Nie istnieją najlepsze praktyki