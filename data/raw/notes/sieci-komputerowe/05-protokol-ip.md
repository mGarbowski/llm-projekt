# Internet Protocol (IP)

## IPv4

### Nagłówek
* numer wersji (4)
* internal header length - potrzebny bo na końcu jest pole options o zmiennej długości
* type of service - dostosowanie algorytmów routingu stosownie do usługi
    * usługa może wymagać 100% poprawności danych - lepiej maksymalnie buforować pakiety
    * usługa może wymagać małych i stałych opóźnień - lepiej zgubić pakiet
    * informuje router jak najlepiej dopasować zachowanie do potrzeb usługi
* total length - długość danych + nagłówka
* TTL - time to live
    * przez ile routerów może jeszcze być przekazany
    * unika zaśmiecania sieci pakietami, których nie da się dostarczyć (np. w cyklu)
    * dekrementowany przy każdym przekazaniu
    * pakiet jest odrzucany kiedy osiągnie 0
    * typowo rzędu 32
* protocol - następny nagłówek (TCP / UDP)
* header checksum
    * pominięty w wersji 6
    * nie zapewnia w znaczący sposób bezpieczeństwa
    * dubluje niższe warstwy
    * sieci są na tyle niezawodne, że nie jest potrzebny
    * IPsec zapewnia bezpieczeństwo transmisji
* source address
* destination address
* options

### Klasy adresów IPv4
Przestarzały sposób podziału przestrzeni adresowej, wyparty przez routing bezklasowy i subnetting

| Klasa | początkowe bity | najmniejszy adres | największy adres | funkcja                                                       |
|-------|-----------------|-------------------|------------------|---------------------------------------------------------------|
| A     | 0               | 0.0.0.0           | 127.255.255.255  | adresowanie interfejsów                                       |
| B     | 10              | 128.0.0.0         | 192.255.255.255  | adresowanie interfejsów                                       |
| C     | 110             | 192.0.0.0         | 223.255.255.255  | adresowanie interfejsów                                       |
| D     | 1110            | 224.0.0.0         | 239.255.255.255  | multicast, indentyfikuje grupy, a nie poszczególne interfejsy |
| E     | 1111            | 240.0.0.0         | 255.255.255.255  | eksperymentalna, nie powinny trafiać do sieci globalnej       |


| klasa | numer sieci | numer hosta |
|-------|-------------|-------------|
| A     | 1 bajt      | 3 bajty     |
| B     | 2 bajty     | 2 bajty     |
| C     | 3 bajty     | 1 bajt      |

Jeśli numer sieci szukanego komputera jest taki sam to zapytanie ARP jest wysyłane do komputera, jeśli nie to do routera.

Taki sposób adresowania sieci prowadzi do marnowania przestrzeni adresowej. Subnetting zapobiega wyczerpywaniu przestrzenia adresowej.


### Subnetting
Adres IP jest dzielony za pomocą maski sieci na adres sieci i adres hosta, każdy komputer poza adresem IP ma też przypisaną maskę sieci.

### Maska podsieci
* zaczyna się od samych jedynek.
* notacja kropkowo-dziesiętna - 255.255.255.0
* podawana w skrócie, razem z adrsem IP po znaku '/' (liczba jedynek w masce) - 148.81.31.191/24

* Numer hosta - najmniej znaczące bity adresu IP (tyle ile jest zer w masce) - otrzymany przez bitwise AND adresu IP z zanegowaną maską
* Adres sieci - same 0 w miejsu numeru hosta - uzyskiwany przez operację bitwise AND adresu IP z maską
* Adres broadcastowy - same 1 w miejsu numeru hosta


### Podział puli adresowej
Pulę adresów można podzielić na podsieci w taki sposób, żeby zakresy odpowiadające maskom były rozłączne

Najmniejsza użyteczna grupa adresów to 4 (dla maski 255.255.255.252), bo 2 są zarezerwowane na numer sieci i adres broadcastowy, Grupa 4 nadaje się na połączenia punkt-punkt.

Standard RFC 1122 zabrania użwania adresów podsieci 0 i -1. Proponowany standard RFC 1812 zezwala na te numery podsieci. Praktycznie można ich używać na współczesnym sprzęcie (po 1995).


### Adresy zastrzeżone
* `0.0.0.0` - nie znam swojego adresu IP, używany przez urządzenia przy podłączaniu do sieci
* `255.255.255.255` - broadcast, do wszystkich w sieci lokalnej
* `127.0.0.1` - loopback, adres pseudo-interfejsu sieciowego, do zapytań w sieciowych w obrębie jednej maszyny

### Sieci prywatne (RFC 1918)
Grupy adresów zarezerwowane przez IANA, nigdy nie będą przydzielone żadnej instytucji. Można je bezpiecznie przydzielać w sieci prywatnej, bo żaden serwer na świecie nie może ich używać.

* `10.0.0.0` - `10.255.255.255`
* `172.16.0.0` - `172.31.255.255`
* `192.168.0.0` - `192.168.255.255`


## IPv6
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

Nie są fragmentowane przez routery - host musi dowiedzieć się jakie jest MTU (maximum transfer unit) i się dostosować


### Skrócony zapis adresu IPv6
* zapis heksadecymalny
* pomija się wiodące zera
* conajwyżej jedną grupę samych zer można zastąpić przez `::`

### Adresy specjalne
* Loopback `::1`
* Nieokreślony `::`
* IPv4 compatible - `::129.144.52.38`
* IPv4 only
    * `0:0:0:0:0:FFFF:129.144.52.38`
    * dla sieci w której komputery obsługują tylko IPv4


### Prefiks sieciowy
Odpowiednik maski w IPv4

### Rodzaje adresów
* większość przestrzeni pozostaje nieprzydzielona
* adresy kompatybilnościowe
* Aggregatable Global Unicast Addresses - przyznawane adresy publiczne
* Link-Local Unicast Addresses - prywatne w ramach segmentu sieci
* Site-Local Unicast Addresses - prywatne w ramach wewnętrznej sieci jednej instytucji, nadają się do routingu
* Multicast Addresses

### Budow aadresów unicastowych
64 bity adresu sieci, 64 bity adresu hsota

* EUI-64
    * stałe `FFFE` wstawione w środek 64-bitowego ID interfejsu
    * ID interfejsu zawiera adres MAC
    * można zrobić inaczej przy innej stałej (np. nadane statycznie dla serwera a nie dla karty sieciowej)
* Link-Local - 64 bitowy stały prefiks
* Site-Local - 48 bitów stałych i 16 bitów numeru podsieci przyznawanych przez router 
 
 
Adresy publiczne (Aggregatable Global Unicast Addresses)
* prefiks
* TLA - top level aggregation
    * identyfikator operatora sieci (ISP)
    * wykorzystywany w routingu przez routery szkieletowe
* pole zarezerwowane - na przyszłość, w zależności od tego które identyfikatory szybciej się wyczerpią (TLA/NLA)
* NLA - next level aggregation
    * identyfikator sieci instytucji w sieci operator
    * routery operatora wykonują routing na podstawie NLA
* SLA - site level aggregation - numer podsieci
    * nie potrzeba masek
    * jeśli prefiks zgadza się z adresem sieci routera to routing odbywa się wewnętrznie na podstawie numeru podsieci

Ten format znacznie ułatwia routing

## Fragmentacja pakietów IP
W sieci obowiązuje maksymalna długość ramki (MTU - maximum transfer unit). Pakiety większe niż MTU są dzielone na mniejsze fragmenty i mogą dojść do odbiorcy w innej kolejności. Odbiorca musi mieć możliwość odtworzenia każdego pakietu w całości. Fragmentcaja może być wykonywana kilkukrotnie.

* umożliwia grupowanie
* umożliwia odtworzenie kolejności
* jest odporne na wielokrotną fragmentację

* identification - nadaje różne wartości różnym pakietom, służy do grupowania fragmentów
* fragment offset - 0 w pierwszym fragmencie (i oryginalnym pakiecie), określa pozycję w buforze w jakiej trzeba umieścić dane (odstęp od początku danych w pierwszym fragmencie)
* more fragments - 1 dla nieostatniego fragmentu i 0 dla ostatniego

W ten sposób można ponownie zfragmentować pakiety przeliczając odpowiednio offsety. Odtwarzanie pakietu jest obowiązkiem końcowego odbiorcy (routery po drodze niczego nie odtwarzają, nie wszystkie pakiety musiały przejść tą samą trasą)

W IPv6 informacje o fragmentacji są w opcjonalnym nagłówku
