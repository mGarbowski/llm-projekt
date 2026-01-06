# Powtórzenie do kolokwium 02

## VLAN
Wydzielone fragmenty sieci fizycznej zachowujące się jak zwykła podsieć

### Standard 801.Q
Definiuje sposób znakowania ramek umożliwiający przekazanie informacji o numerze wirtualnej sieci lokalnej (vlan id), w której została wysłana ramka


## Urządzenia do łączenia sieci
### Bridge / Switch
* Podejmuje decyzję o dalszym losie pakietu na podstawie docelowego adresu MAC
* Buduje tablicę sterującą na podstawie adresu MAC nadawcy

### Router
* Podejmuje decyzję którędy kierować pakiet na podstawie adresu IP odbiorcy

### Które wymagają konfiguracji
* Router
* Bridge - do VLANów
* Switch - to zależy

### Łączenie sieci Token Ring i Ethernet
Bridge


## Porty uprzywilejowane
* Numery do 1024
* Może być przydzielony tylko programowi działającemu z uprawnieniami administratora
* Well known services

## DNS
### Reverse DNS
* Odpowiada na pytanie jaką nazwą domenową posługuje się host o danym adresie IP
* Dla IPv4 
  * 1.2.3.4 -> 4.3.2.1.in-addr.arpa
* Dla IPv6
  * 1080::8:800:200C:417A -> A.7.1.4.C.0.0.2.0.0.8.0.8.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.8.0.1.IP6.ARPA
  * Pierwsze dwa człony odpowiadają dwu ostatnim cyfrom heksadecymalnym adresu IPv6

### Resolver
Biblioteka procedur służących do komunikacji z serwerem DNS


### Klasy rekordów
* SOA
* NS
* A
* AAAA
* PTR
* CNAME
* MX
* TXT
* SRV
* DNSKEY
* RRSIG
* HINFO
* WKS

### Typy serwerów
* Root - szczyt hierarchii
* Primary (master)
* Secondary (slave)
* Caching-only
* Forawrding

### Budowa rekordu
* nazwa
* czas życia
* klasa
* typ
* wartość

### Odpowiedź autorytatywna
Odpowiedź od serwera obsługującego daną domenę (primary albo secondary)

### Rekord SOA
* Serial - numer sekwencyjny
* Refresh - co ile sekund należy sprawdzać aktualność danych
* Retry - co ile sekund ponawiać nieudaną próbę
* Expire - po ilu sekundach uznać dane za nieaktualne
* Minimum - minimalny czas przechowywania
* MNAME - nazwa domenowa głównego serwera DNS
* RNAME - email administratora
* TTL (własne)


## Metody dostępu do medium
### Przekazywanie znacznika
* Token ring
* Arcnet
* FDDI
* CDDI
* IEEE 802.5

### CSMA/CD
* Ethernet
* IEEE 802.3

### CSMA/CA
* AppleTalk
* WiFi

## Model ISO/OSI
* Buforowanie i potwierdzanie transmisji TCP - wartwa transportowa (4)
* Kierowanie ruchem pakietów - warstwa sieciowa (3)
* Urządzenia typu switch - warstwa łącza (2)

## Szybkości transmisji
### Ethernet
* 10 Mb/s
* 100 Mb/s
* 1 Gb/s
* 10 Gb/s
* 25 Gb/s
* 40 Gb/s
* 100 Gb/s


## UDP
### Nagłówek
* port nadawcy
* port odbiorcy
* długość
* suma kontrolna

## TCP
### SEQ (sequence)
Numer pierwszego bajtu w pakiecie


## IPv6
### Autokonfiguracja bezstanowa
* Utworzenie adresu lokalnego (link-local)
* Sprawdzenie unikalności adresu lokalnego

### Fragmentacja
* Podział pakiet na mniejsze części
* Informacje w oddzielnym nagłówku

### Nagłówek
* numer wersji (6)
* priorytet
* flow label
  * parametry jakościowe (spełnia funkcję 'type of service')
  * parametry bezpieczeństwa
* payload length
  * maksymalnie 4GB
  * długość danych
  * całkowita długość pakietu może się zmieniać w trakcie transmisji
* next header - typ następnego nagłówka (TCP / UDP / opcjonalny IPv6)
* hop limit - odpowiednik TTL
* (128b) source address
* (128b) destination address
* opcjonalne nagłówki pomocnicze
  * określony przez pole next header wcześniej
  * routing
  * fragmentacja
  * bezpieczeństwo (IPsec)

### Budowa adresu Aggregatable Global Unicast Address
* prefiks
* TLA - top level aggregation
* pole zarezerwowane
* NLA - next level aggregation
* SLA - site level aggregation - numer podsieci
* Interface ID

## VPN
Służy do tworzenia bezpiecznych (szyfrowanych) kanałów komunikacyjnych w sieciach publicznych

### L2TP
* Layer 2 Tunneling Protocol
* Może być przesyłany w
  * ramkach Frame Relay
  * pakietach UDP
  * ramkach ATM


### PPP
* Nie nadaje się do połączeń SSH
  * enkapsulacja TCP w TCP
  * z punktu widzenia zagnieżdżonego nagłówka wszystkie pakiety przechodzą i ustawia duże okno
  * problemy przy zatorze w sieci

### PPTP
* Połączenie protokołów
  * PPP
  * CHAP
  * RC4
  * GRE