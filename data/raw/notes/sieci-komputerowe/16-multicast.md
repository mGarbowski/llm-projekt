# Multicast IP
* Transmisja od jednego nadawcy do wielu odbiorców jednocześnie
* Wymaga innych protokołów routingu, więcej niż jedna decyzja dla każdego adresu
* Jest szeroko zaimplementowany ale w praktyce w niewielu routerach jest skonfigurowany
* W praktyce ze względu na mały stopień rozpowszechnienia jest praktycznie nieużywany
* Jest integralną częścią IPv6


## Adresy 
* Klasa D - przeznaczona na transmisje multicast
* Przydziela się adresy na potrzebę konkretnej transmisji
* zakres `224.0.0.0`-`239.255.255.255`

## Multicast w sieci lokalnej
* Adres MAC budowany na podstawie adresu IP multicast
* Ramka odbierana przez wszystkie zainteresowane hosty
* Broadcast jest odbierany zawsze (przez system operacyjny) a multicast tylko na życzenie systemu operacyjnego
* multicast jest filtrowany przez kartę sieciową, nie przerywają pracy systemu operacyjnego

## Internet Group Management Protocol
* 2 typy pakietów
  * report
  * query
* Host chcący odbierać pakiety multicast wpisuje odpowiedni adres do rejestrów karty sieciowej i wysyła pakiet report do routera
* Router przechowuje listę adresów odbierających multicast i zgłasza zmianę do routera nadrzędnego
* Router okresowo rozsyła pakiety query to hostów, którzy mają odesłać pakiet report żeby nie zostać usuniętym z listy - zapewnia czyszczenie listy
* Zaprojektowany dla sieci hierarchicznej, nie nadaje się do sieci szkieletowej internetu (topologia kraty), nadaje się tylko do sieci lokalnych

## Adres multicastowy IPv6
* stałe 0xff
* scope - 4 bity - jak szeroko mają być rozsyłane pakiety
  * node-local
  * link-local
  * site-local
  * organization-local
  * global - nie wszędzie dotrze, routery mają ograniczenia i nie przepuszczą pakietów
* flag - 4 bity
  * well known address
  * transient address - tymczasowy adres przeznaczony na konkretną transmisję
* group ID - 112 bitów

## Multicast Listener Discovery
* Współczesny odpowiednik IGMP
* Przeznaczony do pracy w sieci lokalnej

## Protocol Independent Multicast

### Sparse mode
* router zaczyna przekazywać pakiety do odbiorcy
* w międzyczasie może zostać znaleziona lepsza ścieżka z pominięciem routera kontaktowego
* Router odbiorcy nawiązuje bezpośrednie połączenie z nadawcą i zrywa połączenie z routerem kontaktowym

### Dense mode
* Rozsyłanie do wszystkich routerów - flooding
* Routery zgłaszają chęć odłączenia się od transmisji


## Application Layer Multicast
* Wybiera się klientów, którzy będą działać jako przekaźniki
* Tylko jeden klient ma kontakt z centralnym serwerem, reszta klientów kontaktuje się z nim


## Reliable Multicast
* Dla sytuacji kiedy wszystkie pakiety muszą na pewno dotrzeć do każdego klienta
* sender initiated - oparty na potwierdzeniach, jeśli nie dotrą to serwer retransmituje
* receiver initiated - oparty na negatywnych potwierdzeniach od klientów, powodują retransmisję
* tree based
* ring based