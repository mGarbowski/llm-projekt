# Wprowadzenie do zagrożeń sieciowych

## Podstawowe pojęcia
* Zagrożenie (threat)
	* możliwa do wykonania akcja prowazdąca do niechcianych efektów
	* wykorzystuje podatność
    * np. możliwość poznania poufnych danych
* Podatność (vulnerability)
	* błąd w oprogramowaniu lub konfiguracji pozwalający na uzyskanie nieautoryzowanego dostępu do pewnych zasobów
    * SQL injection
    * nieszyfrowana transmisja
    * błąd w logice programu
* Atak (exploitation)
	* wykorzystanie dostępu do podatności i doprowadzenie do sytuacji niezamierzonej przez programistę
	* powodujące odmowę wykonania usługi
	* poznanie poufnych danych
	* uzyskanie zdalnego dostępu do maszyny
* Jeśli w oprogramowaniu istnieje błąd to jeszcze niekoniecznie da się go wykorzystać
* Ryzyko
	* jakie jest prawdopodobieństwo ataku i jak groźne są jego skutki

## Podatności
* Podatności są katalogowane przez wiel firm i organizacji
* Lista CVE - Common Vulnerabilities and Exposures
	* jednoznaczne identyfikowanie podatności
* Listy producentów oprogramowania (Microsoft, Cisco)
* Listy producentów oprogramowania antywirusowego 
* Ogólnie przyjęto że posługuje się numerami CVE
* Z podatnością są związane
	* aspekty techniczne umożliwiające lub uniemożliwiające jej wykorzystanie
	* możliwe efekty wykorzystania
	* prawdopodobieństwo wykorzystania
	* opisuje się poziom ważności (krytyczna, groźna, niewielka)

## Ryzyko
* Systemy są tak skomplikowane, że nie da się stworzyć w 100% bezpiecznego systemu
* Trzeba szacować ryzyko związane z działaniem aplikacji
* Wykorzystuje się model zagrożeń
* Bezpieczeństwo jest na ten moment
	* po audycie może wyjść na jaw nowa podatność

## Exploit
* Specjalnie spreparowana porcja danych umożliwiająca wykorzystanie błędu w oprogramowaniu przez atakującego
* Exploitem może być
    * odpowiednio spreparowany plik
    * odpowiednie zapytanie / dane wprowadzane przez użytkownika
    * żądanie do serwera / sesja komunikacyjna
* W efekcie aplikacja wykonuje niezamierzone przez autora, a zamierzone przez atakującego akcje

## Remote code execution
* Podatność umożliwiająca zdalne wykonanie kodu na zaatakowanej maszynie
* W efekcie atakujący może wykonać dowolny program i przejąć kontrolę nad dalszym wykonywaniem programu

## Shellcode
* Nazwa historyczna
	* pierwsze exploity dawały dostęp do powłoki Unixa
* Kod wykonywalny (instrukcje dla procesora)
	* instrukcje asemblerowe w postaci binarnej

## Atak odmowy usługi
* Atak uniemożliwiający użytkownikowi wykonanie jego zadań
* Można to zrobić na wiele sposobów
    * wykonanie instrukcji wyłączającej zaatakowaną aplikację
    * wykorzystanie zasobów atakowanej maszyny

## Spoofing
* Fałszowanie adresu nadawcy (podszycie się)
* W wielu systemach do dostarczenia wykorzystuje się tylko adres docelowy (sieć IP)
* Bez dodatkowych zabezpieczeń, jako adres źródłowy można ustawić dowolną wartość
* Wtedy na ten fałszywy adres może przyjść odpowiedź

## Sniffing
* Podsłuch transmisji w celu uzyskania wartościowych informacji
* Wiele informacji powinno być, a nie jest szyfrowanych
* Kartę sieciową można przestawić w tryb *promiscuous*
	* odbiera wszystkie ramki
	* nie tylko te zaadresowane do niej
* Segmentacja sieci utrudnia bezpośrednie wykorzystanie podsłuchu

## Przykładowe ataki

### Rekonesans
* Zdobycie jak największej liczby informacji o atakowanym
	* usługa, system, organizacja
* Przykładowe techniki i narzędzia
    * nmap
    * skanery podatności
    * pasywna analiza
    * whois, nslookup
    * Shodan
    * google

#### nmap
* Skaner sieciowy
* Pozwala skanowac otwarte porty na danej maszynie
* Pozwala zidentyfikować system operacyjny
* Nowsze wersje umożliwia rozpoznanie działającej usługi
* Wykorzystuje normalne zachowanie stosu TCP/IP
* nmap nie nawiązuje pełnego połączania, zamyka półotwarte połączenie
    * SYN, SYN/ACK, RST - to dzieje się w jądrze systemu operacyjnego
    * nic nie dzieje się na poziomie aplikacji, nie ma jak trafić do logów bez dodatkowych narzędzi (np. sprzętowych)


#### Skanery podatności
* Automatycznie sprawdza potencjalne podatności na wskazanej maszynie
    * znane podatności w wykrytym oprogramowaniu
    * standardowe hasła
    * znane błędy w konfiguracji
* Narzędzia
    * SATAN, SAINT (historyczne)
    * Nessus

#### p0f
* Program umożliwia identyfikację systemu operacyjnego zdalnej maszyny
	* z którą się łączymy
	* która łączy się do nas
	* której ruch obserwujemy
* Specyfikacja RFC stosu TCP/IP pozostawia elastyczność w implementacji
	* obserwując zawartość pakietów można z dużym prawdopodobieństwem określić na jakim systemie operacyjnym działa

#### whois, nslookup
* Baza danych dotycząca właścicieli osób rejestrujących i firm obsługujących wpisy w systemie DNS
* Bezpośrednio z systemu DNS można często uzyskać dużo informacji na temat sieci

#### Google hack
* Wyszukiwanie podatnych usług za pomocą wyszukiwarki internetowej
* Niektóre aplikacje udostępniają dane, które da się wyszukać przez google

#### Shodan
* Dedykowana wyszukiwarka maszyn podłączonych do sieci

### Ataki man in the middle
Atakujący umieszcza się między dwiema komunikującymi się ofiarami, żeby przechwycić komunikację (podsłuchać, modyfikować)

#### Atak na wartswie drugiej
* Sieci wykorzystując przełączniki (switch)
* Mozna wymusić na przełączniku, wysyłając fałszywy adres MAC, żeby przekierowywał komunikację do złej maszyny
* Można przepełnić tablicę CAM przełącznika zalewając go sfałszowanymi adresami MAC
    * przełącznik zaczyna działać jak koncentrator - rozsyła na wszystkie porty

#### Atak na warstwie trzeciej z DHCP
* Komputer atakującego uruchamia serwer DHCP
* Komputery podłączające się do sieci dostają od niego adresy IP
* Komunikacja przechodzi przez wrogi serwer
* Są mechanizmy, które pozwalają się przed tym obronić

#### Atak na warstwie trzeciej z IPv6
* Komputer atakującego zgłasza się jako router w IPv6
* Atakujący uruchamia własny DNS
* Urządzenia dual stack mogą szukać w pierwszej kolejności routera IPv6

### Ataki DoS
* Prymitywny flooding / wykorzystanie sieci botów (botnetu)
    * już nieefektywne, odcinane przez automatyczne systemy
* DDoS
    * Rozproszony atak, z wielu przejętych maszyn

#### Flooding
* Zalanie serwera zapytaniami
* Prymitywny
* Wersja rozproszona wykonywana przez sieć botów

#### SYN-flooding
* Wykorzystuje połączenia półotwarte TCP
* Wysyła pakiety z flagą SYN z fałszywym adresem źródłowym, ofiara odpowiada i czeka
* System operacyjny utrzymuje ograniczoną kolejkę połączeń półotwartych (embryonic)
* Po zapchaniu kolejki, kolejne zgłoszenia są ignorowane
* SYN/ACK trafia do "czarnej dziury" - nigdy nie wyjdzie odpowiedź ACK
* Można to rozwiązać przez odpowiednie dobieranie numerów sekwencyjnych w ramkach TCP i kryptograficzne weryfikowanie
    * nie potrzeba nawet kolejki
* Już nie działa (raczej)

#### Zwielokrotnienie ruchu - atak smurf
* Pakiety ICMP na adres broadcastowy
* Jeden pakiet wysyłany, wiele pakietów odpowiedzi
* Atakujący wysyła ICMP z adresem źródłowym ofiery, na adres broadcastowy
* Już nie działa
    * administratorzy blokują ICMP w firewallu

#### Zwielokrotnienie ruchu - DNS
* Wykorzystuje otwarte resolvery DNS
* Atakujący wysyła zapytanie DNS typu ANY z adresem źródłowym ofiary
* Odpowiedź jest dużo większa niż zapytanie, w TCP można uzyskać np. 200-krotne zwielokrotnienie
* Nie konfiguruje się już serwerów DNS jako open resolver

#### Slowloris
* Na serwery webowe
* Poprzednie ataki polegały na generowanie dużej ilości danych
* Atak polego na utrzymywanie jak najwięcej jak najwolniejszych sesji
* Wysyła 1 bajt i czeka
* Dopiero po ponagleniu od serwera (keep-alive) wysyła kolejny itd
* Zajmuje zasoby serwera, a atakującego to niewiele kosztuje

### Ataki wykorzystujące błędy w oprogramowaniu
* Command Injection
* Błąd w programie
	* średnio wykrycie błędu zajmuje 200 dni
	* możliwość pominięcia procesu uwierzytelniania
* Remote Code Execution
