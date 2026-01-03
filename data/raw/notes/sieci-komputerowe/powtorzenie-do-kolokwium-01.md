# Powtórzenie przed kolokwium 1
DISCLAIMER nie jestem absolutnie pewny co do poprawności poniższych, pozdrawiam

## Stos protokołów TCP/IP
* starszy od modelu ISO/OSI
* 4 warstwy abstrakcji
    * aplikacji
    * transportu
    * internetu
    * łącza
* bazuje na implementacji w Unixie
* wywodzie się z ARPANET

## TCP
### Okno
* Maksymalny rozmiar danych (liczba bajtów) jaki może być przesłany bez otrzymania potwierdzenia odbioru
* Zależy od rozmiaru bufora, w którym będą przechowywane dane
* Zależy od częstości strat pakietów podczas transmisji(?)

### Pole SEQ
Numer pierwszego bajtu zawartego w pakiecie

## UDP
### Nagłówek
* suma kontrolna
* numer portu odbiorcy
* numer portu nadawcy
* długość


## Pojęcia
* Sieć anonimowa (TOR) umożliwia anonimowej wymiany danych
* Intranet - prywatna sieć odseparowana od publicznego internetu ale używająca do komunikacji protokołów internetowych

## Adresowanie w IP
### Adresowanie bezklasowe (CIDR)
* Oparty o użycie masek sieci - muszą być przekazywane razem z adresami IP
* Pozwala na bardziej efektywny przydział adresów
    * liczba hostów w sieci zależy od długości maski
    * 2 adresy zajmują adres sieci i adres broadcastu
    * wolniejsze zużywanie przestrzeni adresowej
* zmiejszenie liczby wpisów w tabeli routingu
    * przez supernetting odpowiednie operacje bitowe pozwalają pokryć wiele podsieci jedną parą adres + maska
    * przyspieszenie routingu (przez zmniejszenie tabel)

### Budowa adresów
* Jeśli fragment adresu odpowiadający numerowi hosta wynosi 0 to oznacza albo bramę domyślną jako adresata albo nieznany adres nadawcy
* Jeśli fragment adresu odpowiadający numerowi hosta składa się z samych jedynek to oznacza adres rozgłoszeniowy (broadcast) w tej podsieci
* Numer hosta o adresie 3.2.1.0/16 wynosi 256

### Wymagane do nawiązania połączenia z hostem w tej samej sieci lokalnej
* adres IP
* maska sieci

### Wymagane do nawiązania połączenia z hostem poza siecią lokalną
* adres IP
* ~~maska~~
* adres routera

### Klasy adresów IP
* A
    * pierwszy bit 0
    * np. 100.20.3.40
* B
    * pierwsze bity 10
* C
    * pierwsze bity 110
    * przykładowo 200.211.252.33

## ICMPv4
Służy do diagnostyki i obsługi błedów w sieciach IP

## Fragmentacja
* Pakiety których rozmiar przekracza MTU są fragmentowane lub gubione jeśli mają ustawioną flagę DF
* Flaga DF - Don't fragment - pakiet nie może być fragmentowany
* Flaga MF - More fragments - pakiet nie jest ostatnim fragmentem oryginalnego pakietu

### IPv6
* Tylko węzły nadawcze dokonują fragmentacji - host musi określić rozmiar MTU w danej sieci albo pakiety będą gubione
* Maksymalny rozmiar pakietu wynikający z budowy nagłówka IPv6 to 4GiB

## Model referencyjny ISO/OSI
* podział na 7 warstw
* zakres funkcjonalności każdej warstwy
* nazewnictwo
* zasady opisu i współpracy protokołów

### Warstwa łącza danych
* detekcja i korekta błędów w transmisji
* synchronizacja ramki - rozpoznawania początku i końca
* sterowanie przepływem - unikanie kolizji w dostępie do współdzielonego medium
* adresowanie interfejsów podłączonych do tego samego medium transmisyjnego (bez przesyłania danych poza własny router)

### Warstwa sesji
* nawiązywanie/zrywanie połączenia
* uwierzytelnianie, autoryzacja
* zarządzanie aktywnościami
* obsługa punktów synchronizujących przesył danych lub zdalne przetwarzanie

### Warstwa prezentacji
* kompresja danych
* szyfrowanie danych
* negocjowanie kontekstu prezentacji - sposób kodowania i akceptowane struktury danych
* translacja między kodowaniem lokalnym a sieciowym

## Rozpowszechnienie internetu
* Wolny dostęp do dokumentacji RFC i implementacji UNIX BSD
* serwery WWW
* przystępny sposób prezentacji - przeglądarki WWW

## NAT
* ogranicza prędkość przesyłu danych - narzut związany z translacją adresów
* wymaga stosowania dodatkowych urządzeń / programów, żeby uwidocznić hostów dla innych sieci

## Routing statyczny
* konfiguracja jest niezależna od błędnej konfiguracji innych reouterów w sieci
* nie wymaga żadnej wymiany danych przez sieć
* nie adaptuje się automatycznie do zmian w topologii sieci
* wymaga ręcznej konfiguracji przez administratora

## Routing dynamiczny
* Nie wymaga ręcznej konfiguracji
* Automatycznie dostosowuje się do zmian w toopologii sieci
* Zwiększa ruch w sieci - wymaga wymiany tabel routingu między routerami
* Może doprowadzić do powstania pętli w routingu

## Adresowanie EUI-48 (MAC)
* identyfikuje interfejs w danej sieci lokalnej
* wspiera adresy unicast (parzyste), multicast (nieparzyste) i broadcast (same 1)
* wskazuje driver obsługujący dany interfejs fizyczny (?)

## Regionalne Rejestry Internetowe (RIR)
* Utrzymują serwer DNS
* przydzielają numery systemom autonomicznym
* przydzielają bloki adresów Lokalnym Rejestrom Internetowym


## Routing typu distance-vector vs link-state
* distance-vector jest prostszy w implementacji (RIP)

## DHCP
* Umożliwia przydzielanie hostom adresów IP na podstawie adresu MAC (EUI-48) w sposób określony przez administratora
* Umożliwia przydzielanie hostom adresów losowych adresów IP z określonej puli
* Umożliwia dostarczenie adresów IP istotnych serwerów usług sieciowych (np. serwerów DNS)
* Umożliwia wskazanie pliku z systemem operacyjnym do pobrania przez hosta

### Sekwencja pakietów
1. DISCOVER
2. OFFER
3. REQUEST
4. ACK


## Technologie dostępu do internetu
* Cyfrowa linia abonencka (DSL)
* DOCSIS
* IEEE 802.11


## Porty uprzywilejowane
* 0-1024
* Mogą być obsługiwane tylko przez programy pracujące z uprawnieniami administratora


## Ethernet
* Stosuje CSMA/CD - dostęp jednoczesny z wykrywaniem kolizji

### VLAN
* wirtualna sieć loklana
* wydzielony fragment fizycznej sieci, który zachowuje się jak zwykła podsieć
* standard IEEE 802.1q
    * sposób znakowania ramek
    * przekazywanie informacji o numerze VLAN, w którym wysyłana jest ramka

### Typowe szybkości transmisji Ethernet
* 100 Gb/s
* 10 Gb/s
* 1Gb/s
* 100 Mb/s
* 10 Mb/s

## Przekazywanie znacznika
Używane przez sieci

* FDDI
* Token Ring
* ARCNET

## Szybkość transmisji w publicznej sieci telefonicznej (analogowej)
* 19200 b/s
* 9600 b/s
* 33.6 kb/s

## Null modem
Kabel szeregowy ze skrzyżowanymi połączeniami stosowany do łączenia dwóch komputerów

## Modulacja
* stosowana przez modemy przy przesyłaniu danych
* w sieci telefonicznej występują zakłócenia wysokoczęstotliwościowe

## Protokół PPP
* przesyłanie pakietów IP przez łącze szeregowe
* przesyłanie pakietów IP przez łącze ATM
