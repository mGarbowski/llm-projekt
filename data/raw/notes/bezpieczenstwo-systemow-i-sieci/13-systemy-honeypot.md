# Systemy HoneyPot
* Systemy HoneyPot są technologią pozwalającą zdobywać informacje dotyczące sposobu działania, stosowanych techniki i motywacji atakujących
	* to nie jest określone rozwiązanie, tylko sposób działania
* "A honeypot is an information system resource whose value lies in unauthorized or illicit use of that resource"
* Systemem HoneyPot może być
	* program symulujący jakąś usługę
	* działający system komputerowy z lukami
	* sieć działających systemów komputerowych
	* rekord w bazie danych

## Zalety
* Zbierają relatywnie mało danych o dużej wartości
	* w porównaniu do logów systemów IDS/IPS
* Redukują liczbę false positives
* Pozwalają analizować ataki wykorzystujące szyfrowane protokoły sieciowe
* Są bardzo elastyczne
* Wymagają minimalnych zasobów
* Atakujący może marnować czas na atakowanie honeypot zamiast systemów produkcyjnych

## Wady
* Mają ograniczone pole widzenia
* Mogą wprowadzać dodatkowe ryzyko do sieci w której są uruchomione
	* administrator jest odpowiedzialny za maszynę którą podłącza do sieci

## Podział systemów HoneyPot
* Low interaction
	* tylko symulują pewne usługi
* High interaction
	* pełne działające systemy z działającym oprogramowaniem
	* poddane odpowiedniej kontroli

## Systemy low interaction
* Spectre
* HoneyD
	* symuluje określony system operacyjnych, tak żeby oszukać fingerprinting programem `nmap`
	* możliwość tworzenia routerów, tuneli i konfigurowania routingu
	* symuluje całą podsieć
* Nepenthes
	* modułowa budowa
	* łatwa rozbudowa o nowe moduły
	* dedykowany zbieraniu informacji o automatycznym kodzie (robaki, wirusy)
	* do łapania robaków
	* symuluje podatne robaki wykorzystywane przez inne robaki
* Dionaea
	* w pythonie
	* analizuje też ataki na telefonię internetową

## Systemy high interaction

### Systemy HoneyNets
* Odpowiedź na wady systemów HoneyPot
	* ograniczone pole widzenia - uruchamia się wiele systemów HoneyPot
	* wprowadzają dodatkowe ryzyko - dokładna kontrola ruchu
* Architektura
	* honeywall gateway - obsługuje cały ruch między honeypot i internetem
	* systemy honeypot w oddzielnej podsieci
	* systemy produkcyjne w oddzielnej podsieci
* Zadania
	* zbieranie danych (logi)
	* blokowanie ataków
* System nie powinien blokować całego ruchu atakującego
	* zorientuje się że to podpucha
	* nie można pozwolić na np. spamowanie mailami
* Pierwsza generacja
	* urządzenie działające w warstwie 3 (router)
	* niezależne systemy służące podsłuchiwaniu ruchu i systemu IDS
* Druga generacja
	* urządzenia warstwy 2 (switch)
	* zbiera wszystkie logi na jednej maszynie
	* zamiana systemu IDS na inline IPS
* Zalety drugiej generacji
	* trudniejszy do wykrycia i zaatakowania
	* może wybiórczo usuwać / przepuszczać ruch (działanie IPS)
	* możliwość zmiany zawartości pakietu zamiast kasowania
* Oprogramowanie wspierające budowę systemów HoneyNet
	* Sebek
	* HoneyWall

### Sebek
* Działa w jądrze systemu operacyjnego
* Przychwytuje wywołania systemowe `read`,  `write` i ruch sieciowy
* Pozwala logować dowolną aktywność na systemie HoneyPot
	* ściągane pliki
	* naciskane klawisze

### HoneyWall CD-Rom
* Bootowalna płyta systemu Linux zawierająca wszystkie potrzebne programy do budowy systmeu HoneyPot gateway z GUI
* Zaliczany do 3. generacji

## Klienckie systemy HoneyPot
* Zamiast pasywnego oczekiwania na atak, system kliencki sam szuka zagrożeń
* Na monitorowanej maszynie uruchamia się aplikacje klienckie
	* przeglądarka
	* klient pocztowy
	* komunikatory
* Przeglądarki otweirają potencjalnie niebezpieczne linki
* Klienty otweirają potencjalnie niebezpieczną pocztę
* Problemy
	* znalezienie niebezpiecznych zasobów (strony, pliki)
	* wiarygodne sprawdzenie czy maszyna została zainfekowana

### HoneyC
* Low interaction
* Skrypty Ruby
* Pobierają strony, analizują, skanują ruch
* Modułowa budowa
* Działa tylko dla stron statycznych, nie dla wspołczesnych SPA
	* nie uruchamiały skryptów JS

### Capture-HPC
* High interaction
* Klient-serwer
	* jeden zarządca
	* wiele klientów czekających na infekcję
* Możliwość integracji wielu różnych programów
* Wirtualizacja VmWare
* Wykrywanie czy maszyna uległa infekcji
	* zmiany w rejestrze
	* nowe pliki wykonywalne
	* stworzenie nowego procesu

## Zastosowanie systemów HoneyPot
* Badawcze
	* analiza nowych ataków
* Wykrywanie ataków
	* łapie to co przeszło przez firewall i IDS/IPS
* Zapobieganie ataków
	* przestraszenie atakującego
	* wyświetlenie wiadomości
	* marnowanie czasu atakującego
* Odpowiedź na ataki
	* problemy etyczne - ataki przychodzą z przejętych maszyn innych ofiar
	* kontratak też jest nielegalny
