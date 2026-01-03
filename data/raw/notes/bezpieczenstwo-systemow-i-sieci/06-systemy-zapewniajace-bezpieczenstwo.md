# Systemy zapewniające bezpieczeństwo w sieciach komputerowych

## Zapora ogniowa
* Służy do odseparowania podsieci o różnych wymaganiach co do poziomu bezpieczeństwa (Internet, LAN)
* Zapora ogniowa umożliwia filtrowanie ruchu
	* przesyłanie/blokowanie ruchu na podstawie jego wybranych cech
* Powinien odcinać ataki ze złego internetu na dobrą sieć lokalną
* Ataki wychodzące też należy odcinać
* Ogólnie firewall to pudło stojące pomiędzy siecią zewnętrzną i wewnętrzną
* W sieci lokalnej może być wiele poziomów firewalla
	* na każdym styku sieci o różnych wymaganiach bezpieczeństwa
### Rozwój zapór ogniowych
* Filtr pakietów
	* patrzy na nagłówki w stosie protokołów
	* sprawdza tylko protokoły
	* nieodporne na spoofing nagłówków
* Proxy
	* maszyna pośrednicząca
	* wolniejsze
	* niedozwolone połączenie nie jest nawiązywane z odbiorcą
* Filtry stanowe
	* śledzi stan - nie można zmanipulować pakietu tak, żeby przeszedł przez filtr
	* dla każdego połączenia kontroluje w pamięci stan
	* dominujące rozwiązanie dzisiaj
* Zapory działające w warstwie 7 (aplikacji)
	* czasami nie wystarczy po prostu zezwolić na ruch HTTP
	* analiza ruchu VoIP - żeby to zaimplementować, trzeba analizować ruch wartswy aplikacji
* Web application firewall
	* dedykowany do HTTP
* Osobista zapora ogniowa
	* oprogramowanie instalowane na komputerze

### Demilitarized zone (DMZ)
* Dla niektórych usług, zwykły podział na sieć zewnętrzną i wewnętrzną nie wystarcza
* Wprowadza się dodatkowe strefy o pośrednim poziomie bezpieczeństwa
* Przykładowo serwery webowe umieszcza się w DMZ
	* z routera oddzielne połączenie do LAN i do serwerów WWW, poczty, FTP
	* wystarczy router z 3 portami
* Architektura
	* zgrubny filtr zewnętrzny
	* router
	* DMZ bez filtra
	* LAN z precyzyjnym filtrem

### Konfiguracja
* Lista warunków Deny/Drop/Reject i Accept/Forward ułożonych w kolejności
* Testowany pakiet/połączenie jest porównywany z warunkami i przy pierwszym dopasowaniu jest podjemowana decyzja
* Odpowiednie listy przypisywane do interfejsów
* Dobrze jest przemyśleć reguły
	* jeśli jedna reguła odsiewa 90% ruchu to lepiej żeby była na początku
* Lepsze jest whitelistowanie niż blacklistowanie
	* to co wiemy że jest dobre puszczamy, resztę blokujemy
	* jak coś jest zablokowane a nie powinno to użytkownik szybko to zgłosi

### Ingress i egress filtering
* Ingress - filtrowanie ruchu wchodzącego
* Egress - filtrowanie ruchu, który nie powinien wyjść z sieci
	* do internetu nie powinny wychodzić pakiety zaadresowane na prywatny adres albo na loopback
	* nie powinien wychodzić pakiet z innym niż własny adresem źródłowym
	* broni przed DoS
* Dokumenty BCP 38 / RFC 2827

## Systemy antywirusowe
Systemy wyszukujące w chronionych zasobach (dyski, maszyny, poczta, ruch sieciowy) znanych zagrożeń związanych z wirusami i szeroko rozumianym złośliwym oprogramowaniem

### Sposoby wykrywania wirusów
* Sygnatury
	* wyszukiwanie znanych ciągów bajtów powiązanych z danym zagrożeniem
	* wykrywa tylko znane, przeanalizowane oprogramowanie
	* drobne modyfikacje mogą uniemożliwić wykrycie
* Heurystyki
	* próba oceny czy dany program wykonuje niebezpieczne operacje
	* możliwe wykrycie wcześniej nieznanych zagrożeń
	* dużo liczba false positives
	* np. niepodpisany, skompilowany mniej niż miesiąc temu

### Przykładowe rodzaje sygnatur ClamAV
* Budowa plików PE - portable executable
	* nagłówek pliku opisujący sekcje (kod, dane, zasoby, itd.)
* Wartość MD5 dla całego pliku
	* nie sprawdza się jeśli wirus jest okresowo modyfikowany
* Wartość MD5 dla wybranej sekcji pliku PE
* Ciągi bajtów z możliwością stosowania wild-card masks
* W tworzeniu malware'u dąży się do tego żeby jeden exe był używany tylko raz
	* zmienany za każdym atakiem

### Chronione zasoby przez współczesne systemy AV
* Pliki znajdujące się na dysku
	* cykliczne skanowanie całego dysku
	* skanowanie każdego nowego i uruchamianego pliku
* Skanowanie ruchu sieciowego
* Skanowanie poczty
	* lokalnie i na serwerze pocztowym

## Systemy IDS/IPS
* IDS - System wykrywania włamań (Intrusion Detecion System)
	* oprogramowanie monitorujące działanie systemu w celu wykrywania zdarzeń sugerujących wystąpienie ataków
* IPS - System przeciwdziałania włamaniom (Intrusion Prevention System)
	* IDS z modułem reagującym na włamanie
	* cały ruch przechodzi przez urządzenie IPS
	* ruch może przepuścić, usunąć, zmodyfikować

### Rodzaje analizowanych danych
* Systemy Hostowe (Host IDS)
	* pobierają dane z systemu operacyjnego
	* częsta analiza różnego typu logów i liczników wydajności
	* wykrywa ataki związane z ruchem szyfrowanym
	* musi być instalowany na każdym chronionym hoście
* Systemy Sieciowe (Network IDS)
	* analizuje ruch sieciowy pod kątem śladów ataku
	* jeden sensor chroni wiele maszyn
	* nie wykryje ataków na szyfrowanych kanałach
	* problem przy dużym wolumenie ruchu
* Systemy Hybrydowe - łączą dane z obu źródeł

### Sposób wykrywania ataków
* Wykrywanie znanych naruszeń - sygnatury
	* każdy atak musi być opisany przez analityka
* Wykrywanie anomalii
	* buduje się model normalnego stanu systemu
	* wykrywa odstępstwa od normalnego stanu
	* statystyki, sieci nauronowe, uczenie maszynowe
	* problem z false positives

### Snort
* Popularny system typu NIDS
* Open source
* Wykrywa zagrożenia na podstawie sygnatur
* Przykładowa sygnatura
	* `alert ip any any -> 10.0.1.23 any (msg:"Zainfekowana maszyna";)`
	* `alert` - wygeneruj alarm
	* `ip any any -> 10.0.1.23 any` - opis protokołu, adresy i porty

### Systemy Sandbox
* System zintegrowany z systemem AV, zaporą, systemem IDS/IPS
* Umożliwia analizę podejrzanego kodu w kontrolowanym środowisku
* Przeniesienie technologii AV do klienta
* Możliwość wykrycia nowych zagrożeń i przygotowanie IoC (Indicator of Compromise)
* IoC mogą być od razu wykorzystywane przez system IDS/IPS

## Mechanizmy obrony warstwy 2

### Port Security
* Możliwość skonfigurowania liczby lub dokładnych adresów mogących być odbieranych na danym porcie
* We współczesnych sieciach jest mikrosegmentacja - jedno gniazdko w switchu do jednego komputera
	* można przypisać konkrenty adres MAC do portu
* W razie wykrycia większej liczby adresów MAC lub niezgodnego adresu, można podjąć akcję
	* zablokowanie portu
	* usunięcie pakietu
	* zalogowanie zdarzenia
* Zapobiega większości ataków na wastwę 2
	* trzeba wygenerować dużo pakietów z fałszywymi adresami MAC na pojedynczym porcie atakującego

### DHCP snooping
* Mechanizm filtrujący i analizujący ruch DHCP na przełączniku
* Switch analizuje ruch DHCP (nieszyfrowany, nieuwierzytelniany)
* Można skonfigurować limit na liczbę wysyłanych komunikatów DHCP na port
* Można oznaczyć porty jako zaufane
* Przeciwdziała próbom ataków man-in-the-middle wykorzystujących DHCP

### Dynamic ARP Inspection
* Inspekcja poprawności informacji zawartych w komunikacji protokołu ARP
* Wymaga włączenie DHCP snooping
	* budowana jest baza mapowania IP-MAC
* Komunikaty niezgodne z mapowaniem są usuwane i logowane

## Systemy HoneyPot
* System, który ma być zaatakowany
	* jego wartość leży w jego niautoryzowanym wykorzystaniu
* Pozwala zdobywać informacje o atakujących
	* sposób działania
	* motywacja
	* stosowane techniki
* Sposoby wykorzystania
	* odstraszanie
	* marnowanie czasu atakującego
	* informacyjne - zdobycie informacji, że organizacja jest celem spersonalizowanego ataku
* Systemem HoneyPot może być
	* program symulujący jakąś usługę
	* działający system komputerowy z celowymi podatnościami
	* sieć działających systemów komputerowych
	* rekord w bazie danych

## Budowanie bezpiecznych sieci

### Low hanging fruit
* Atakujący szuka najsłabiej zabezpieczonych maszyn
* Nawet najprostsze zabezpieczenie może być nie do przejścia (script kiddies)

### Defense in depth
* Podejście z wojskowości
* Wiele linii obrony
* Każda linia obrony może zostać przełamana
* Buduje się kolejne linie obrony
	* zapory ogniowe
	* systemy AV
	* systemy IDS/IPS
	* systemy HoneyPot
	* mechanizmy logowania
	* mechanizmy monitorowania
* Logi dostarczają bardzo użytecznych informacji
	* warto je przeglądać i monitorować

## Systemy SEM, SIM, SIEM
* Security Information and Event Management
* Dedykowane systemy służące do zbierania danych z wielu źródeł i ułatwienia ich analizy
* Agregacja danych z wielu systemów, w wielu formatach (np. logi)
* Korelacja - próba łączenia powiązanych danych
	* np. logi dotyczące jednej maszyny
* Alarmowanie - wysyłanie dodatkowych informacji do administratorów
* Wygodne dashboardy
* Zapewniają retencję i archiwizację danych do przyszłego wykrywania trendów
	* jak długo - zależy od budżetu
	* atak wykrywa się raczej po dłuższym czasie
* Przykłady
	* Open Source Security Information Management
	* AlienVault Unified Security Management - komercyjny
