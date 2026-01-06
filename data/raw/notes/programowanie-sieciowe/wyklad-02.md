# Rodzina protokołów TCP/IP

## Własności
* Otwartość
	* nie zależą od producenta sprzętu lub oprogramowania
* Dostępna dla praktycznie każdej platformy
	* smartfony
	* komputery wbudowane
* Mogą być stosowane zarówno w sieciach LAN i WAN

## Protokół IP
* Protokół warstwy 3 (sieciowej)
* Odpowiada za dostarczenie danych od hosta do hosta
* Cechy
	* datagramowy
	* nie gwarantuje sekwencyjności
	* nie gwarantuje poprawności
	* może nastąpić uszkodzenie, gubienie i zwielokrotnienie pakietów
* Ruting
	* wyłącznie na podstawie adresu docelowego
* Przygotowany do przenoszenia protokołów warstwy 4
* Przygotowany do przenoszenia pakietów przez sieci o różnym MTU
* Dupleksowy

### Adresowanie IPv4
* Adres
	* liczba 32-bitowa
	* konwencja big-endian (network order)
	* zwyczajowo zapisywana jako 4 bajty (oktety)
* W celu uproszczenia rutingu adres dzieli się na starszą część określającą **sieć** i młodszą określającą **hosta**
* Classless Inter-Domain Routing (CIDR)
	* obecnie nie przyznaje się organizacjom adresów z zakresu pełnych klas
	* typowo (niewielka) organizacja otrzymuje pod-klasę składającą się z 4 adresów
* Mechanizm subnettingu pozwala na dalsze dzielenie części hosta na pod-sieć i hosta (wielokrotnie)
* Adresy prywatne
	* `10.0.0.0 - 10.255.255.255` - 1 klasa A
	* `172.16.0.0 - 172.31.255.255` - 16 klas B
	* `192.168.0.0 - 192.168.255.255` - 256 klas C
* Numer hosta `0..0` - sieć
* Numer hosta `1..1` - broadcast
* Klasy A, B, C, D, E
	* przestarzały sposób podziału adresów
	* wyparte przez CIDR i subnetting

### Konwencje little- i big-endian
* Little-endian
	* najmniej znaczący bajt pod najmniejszym adresem
	* architektura x86 i pochodne
* Big-endian
	* najbardziej znaczący bajt pod najmniejszym adresem
	* historyczne architektury, IBM360 itp.
* Bi-endian
	* sprzęt może pracować w obu trybach
	* Arm, Power, SPARC
* Wszystkie standardy sieciowe wykorzystują big-endian
	* trzeba stosować konwersję
	* protokoły wyymagają przestrzegania konwencji w nagłówkach, ale nie w danych użytkownika
	* trzeba ustalić konwencję między komunikującymi się stronami

### Nagłówek protokołu IP
* Adres źródłowy
* Adres docelowy
* Suma kontrolna nagłówka
* Pola związane z fragmentacją
* Długość (16b)
* Numer identyfikacyjny
	* nie umożliwia kontroli sekwencji
	* do identyfikacji fragmentów poddanych podziałowi

W protokołach sieciowych mówi się o *oktetach*, a nie o bajtach
### IPv6
* Za mała przestrzeń adresów IPv4
* Ogólne założenia jak dla IPv4
	* warstwa 3
	* datagramowy
	* niezależny routing pakietów
* 128 bitów adresu
* Integracja IPsec w standardzie
* IPv6 funkcjonuje równolegle do sieci IPv4
	* mogą istnieć równocześnie
	* dopuszczone jest tunelowanie w obie strony
* Prostsza struktura nagłówka (pozornie)
	* wiele funkcji przeniesionych do opcji
* Brak fragmentacji (zazwyczaj)
	* ograniczona fragmentacja
* Jumbogramy
	* do $2^{32} -1$ oktetów
* Typy transmisji
	* unicast
	* anycast - 1 do sąsiednich
	* multicast - 1 do wielu
* W praktyce
	* jest zaimplementowany w większości używanych systemów operacyjnych
	* wiele urządzeń domowych ich nie obsługuje, np routery operatorskie
	* nie wszędzie jest skonfigurowana infrastruktura transmisyjna

### Adresowanie IPv6
* Nie ma koncepcji klas
* Adres loopback
	* :1/128
* Adresy nierutowalne (prywatne)
	* link-local
	* prefix fc00::/7
* Adres używany w dokumentacji
	* 2001:db8::/32
	* nie należy go używać w rzeczywistym kodzie
* Routowalny adres
	* 64 bity adresu sieci CIDR
	* 64 bity adresu hosta, typowo zawierają 48-bitowy adres MAC

### Nagłówek IPv6
* Numer wersji - 4b
* Długość pakietu
* Adresy
* Opcje

### Fragmentacja IP
* W teorii maksymalny rozmiar datagramu to 64kB
	* w praktyce warstwa fizyczna nie przenosi tak dużych datagramów
* Datagramy zostają podzielone
	* przez nadającego, musi mieć wiedzę o maksymalnym rozmiarze w praktyce
	* w sieciach lokalnych MTU może być inne niż na zewnątrz
	* lub podział przez ruter
	* podział może się powtarzać
* Fragment jest w pełni poprawnym datagramem IP
	* ma zapisaną informację o tym że jest fragmentem
* Fragmenty są przesyłane oddzielnie
	* mogą docierać do odbiorcy różnymi drogami
* Fragmenty są łączone przez odbiorcę
	* jeśli fragment zostaje zgubiony to jakby cały datagram został zgubiony
	* im więcej fragmentów tym większa szansa, że któryś zaginie
* Uwaga na rozmiar datagramu
	* dla sieci LAN 1500 jest bezpieczne
* Dla TCP nie przejmujemy się tym ze względu na mechanizm MTU discovery
* Działanie
	* identyfikator
	* offset (w 8B)
	* flaga czy jest fragmentem, w ostatnim 0
* Większe ryzyko zgubienia datagramu
* Większy narzut - każdy fragment ma nagłówek IP
* Bezpieczny rozmiar pakietu
* IPv4
	* teoretycznie 65507
	* minimum reassembly buffer size - standard RFC, nie uwzględnia nagłówków
	* najczęściej przyjmuje się bezpieczną wartość za 512
* IPv6
	* 1500B

## Warstwa transportowa
* Dostarczanie danych między programami działającymi na różnych hostach (od procesu do procesu)
* Dwa protokoły warstwy 4
	* UDP - User Datagram Protocol
	* TCP - Transmission Control Protocol
* Zastosowania UDP
	* DNS, RPC, SNMP, strumieniowanie multimediów
* Zastosowanie TCP
	* większość zastosowań, HTTP, ...

### UDP
* Port źródłowy (16b)
* Port docelowy (16b)
* Długość w bajtach (16b)
* Suma kontrolna (16b)
	* nagłówek UDP, adres IP, długość
	* nie uwzględnia danych
* Port identyfukuje zdalną i lokalną aplikację
* Nadawca i odbiorca są identyfikowanie jednoznacznie

### Porty
* Numery portów UDP i TCP są ortogonalne
* 16 bitów
* Zakres
	* 0 - nielegalny
	* 1-1023 - zarezerwowane well-known ports
	* >=1024 - porty efemeryczne i serwery testowe, ale
		* zależne od implementacji
		* 1024-49151 - registered ports, znane, opcjonalnie dostępne usługi
		* 49152-... - dynamic ports, efemeryczne

### Asocjacje
* Asocjacja jednoznacznie określa dwa komunikujące się procesy
	* protokół
	* adres lokalny
	* port lokalny
	* adres zdalny
	* port zdalny
* Asocjacja jest unikalna w skali internetu
	* z dokładnością do adresów nierutowalnych
* Półasocjacja
	* gniazdo
	* protokół, adres, port
	* punkt końcowy komunikacji

### TCP
* Protokół sekwencyjny, niezawodny, dupleksowy
	* użytkownik nie ma dostępu do abstrakcji *pakietu*
* Z punktu widzenia użytkownika, strumień danych jest jak plik do którego można dopisywać do końca
* Nawiązanie połączenia jest asymetryczne
	* sama transmisja danych odbywa się symetrycznie, nie ma strony wyróżnionej
* Numer portu - 16b
* Zapewnia sterowanie przepływem
	* dopasowanie szybkości transmisji źródła i odbiorcy danych
	* kiedy źródło transmituje szybciej niż odbiorca jest w stanie odebrać
	* w pewnym momencie pakiety będą odrzucane po stronie odbiorcy
	* funkcja write jest zawieszana do momentu wyczyszczenia buforów
	* odbiorca powiadamia nadawcę
* Transmisja OOB
	* out of bound
	* pomija standardowe mechanizmy buforowania
	* dla danych o wysokim priorytecie
* Protokół z przesuwnym oknem
	* doczytać o co chodzi
* Nagłówek
	* Sequence number
	* Acknowledgement number
	* Na poziomie numerowanych bajtów
* Wykrywanie i kontrola błędów
	* nie zawsze potrzebnie
* MSS - maximum segment size
* MTU
* Congestion control
	* dostosowanie szybkości nadawcy i odbiorcy
	* slow-start - początkowa transmisja jest wolna, jak działa dobrze to potem przyspiesza
* Zapewnia sekwencyjność danych

### Model klient-serwer
* Serwer
	* otwarcie pasywne gniazda
	* oczekiwanie na połączenie
* Klient
	* otwarcie aktywne
	* połączenie z serwerem
* Obsługa wielu klientów przez serwer
	* unikalność asocjacji (połączonego gniazda)
	* porty efemeryczne klienta przyznawane automatycznie w czasie nawiązywania połączenia
	* serwery współbieżne i iteracyjne

### Typy serwerów
* Iteracyjny
	* UDP - typowe (np. DNS)
	* TCP - rzadkie (protokoły testowe)
* Współbieżny
	* UDP - rzadkie (np. TFTP, dla prostych klientów, mogą nie mieć zaimplementowanego TCP)
	* TCP - typowe (np. HTTP, SMTP, ssh)

### Inne protokoły transportowe
* DCTP
	* datagram congestion control protocol
	* zapewnia kontrolę przepływu
	* nie zapewnia niezawodności
	* zastosowania w VoIP, streamingu, grach
* SCTP
	* stream congestion transmission protocol
	* datagramowy
	* zapewnia kontrolę przepływu, niezawodność
	* obsługa wielu strumieni na raz
	* multihoming - więcej niż 1 adres IP jako źródło/cel
* QUIC
	* Dostosowany do obsługi HTTP/3
	* Nazywany TCP/2
	* zoptymalizowany do transmisji wielu równoległych strumieni danych w HTTP
	* eliminuje wady wydajnościowe TCP
	* więcej przy okazji HTTP

## DNS
* Protokół aplikacyjny (L7) ale ma szczególne znaczenie dla innych protokołów
* Odpowiada za tłumaczenie adresów symbolicznych na adresy IP
* Hierarchia serwerów DNS odpowiada hierarchi organizacyjnej internetu
* Rozproszona baza danych
	* nigdzie nie jest przechowywana pełna informacja
* Serwer odpowiada za strefę, a strefa niekoniecznie pokrywa się z domeną
* Resolver
	* programista korzysta z DNS za pośrednictwem reesolvera
	* biblioteka
	* kernelowy stos protokołów używa tylko adresów IP, nie symbolicznych

### Dane rekordów
* Nazwa domenowa - FQDN
	* fully qualified domain name
	* case insensitive
* Składnik może mieć 63 znaki
* Pełna nazwa domenowa do 255 znaków
* Dozwolone znaki
	* a-z
	* A-Z
	* 0-9
	* -
	* inne są niedozwolone
* Ograniczenia wynikają z maksymalnego bezpiecznego rozmiaru datagramów UDP

### Działanie
* Serwer nie musi obsługiwać wszystkich rekordów w danym poddrzewie
	* np. serwer edu.pl posiada rekord o pw.edu.pl, ale nie o elka.pw.edu.pl
* Serwer deleguje obsługę wybranych pod-domen do innych serwerów DNS
* Delegowany serwer posiada upoważnienie ...

### Rekordy
* A - mapuje nazwę na adres IP
* PTR - mapuje adres IP na nazwę
* CNAME - nazwy kanoniczne (aliasy)
* MX - adres serwera SMTP dla domeny
* SOA - source of authority - atrybuty strefy, jak długy cache'ować
* NS - serwer nazw
* SPF - sender policy framework
	* do mechanizmów antyspamowych
	* kto jest upoważniony do wysyłania nam poczty