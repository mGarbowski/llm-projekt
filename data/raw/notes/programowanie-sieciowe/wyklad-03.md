# 2024-10-24
Za tydzień może będą prowadzący labów
Dobrać się w zespoły projektowe
Zespoły zgłaszają się do prowadzących

## Gniazda BSD
* API programowania usług sieciowych (Network API)
	* protokoły sieciowe
	* system operacyjny
	* język programowania
* W różnych systemach i językach są w zasadzie warianty gniazd BSD
* Interfejs BSD sockets jest bardziej uniwersalny
	* protokoły internetowe w warstwie transportowej
	* raw sockets - warstwa sieciowa
	* protokół bluetooth
	* gniazda lokalne (AF_UNIX, AF_NETLINK)

### Komunikacja UDP
* Utworzenie gniazda - `socket()`
	* zwraca deskryptor, podobnie jak `open()`
* `bind()`
* `recvfrom()`, `sendto()`

### Komunikacja TCP
* Trzeba utworzyć połączenie
* Serwer - `socket()`, `bind()`
* Klient - `socket()`
* Serwer nasłuchuje na porcie `listen()`
* Przyjmowanie połączeń `accept()`
	* najczęściej w pętli
* Klient wywołuje `connect()`
	* niejawne wywołanie `bind()`
* Komunikacja przez `read()` i `write()`
	* jak dopisywanie do końca sekwencyjnego pliku

### API C vs API Python
* C
	* skomplikowana i żmudna obsługa typów adresowych
* Python
	* można niejawnie używać resolvera
	* wygodniejsze w użyciu
	* nie rozwiązuje typowych problemów samych protokołów sieciowych (np. ograniczona wielkość paczki danych)
* Istotne różnice przy bardziej zaawansowanych funkcjach
	* np. `select()`

### Klient TCP w Pythonie
...

### Serwer TCP w Pythonie
...

listen nie blokuje
accept zwraca parę (gniazdo, adres klienta)
to inne gniazdo niż to nasłuchujące
accept zwraca gniazdo w pełni zasocjowane
system tworzy nowe gniazdo, gniazdo nasłuchujące nie ulega zmianie

binary_stream - przydatne do serializowania bardziej skomplikowanych danych

recv blokuje

### Python `socket()`
* Rodzina protokołów
	* `AF_INET`
* Typ
	* `SOCK_STREAM`
	* `SOCK_DGRAM`
	* `SOCK_RAW`
* Protokół - wyznaczony przez rodzinę i typ
* Deskryptor pliku

### `bind`
* Przywiązuje lokalny adres do gniazda
* Nie generuje komunikacji sieciowej
* Typowo używane przez serwer do przywiązania numeru portu

### `connect`
* Powoduje nawiązanie połączenia z serwerem
* Używany dla TCP, może być użyty dla UDP
* Nie wymaga `bind`
* Funkcja powolna, może być przerwana za pomocą sygnału
	* ctrl+c jeśli program działa z konsoli
	* `send`, `recv`, `read`, `write`
	* użytkownik może zauważyć spowolnienie

### `accept`
* Produkuje zasocjowane (połączone z klientem) gniazdo
* Gniazdo źródłowe nie jest modyfikowane

### Inne funkcje
* socket.listen
	* backlog - liczba kolejkowanych klientów
* send - wysyła dane przez gniazdo
	* może się zablokować
	* może przekazać sterowanie do niższych warstw stosu sieciowego
	* może wysłać tylko część danych
* sendall - wysyła dane przez gniazdo do skutku
	* do wystąpienia błędu lub wysłania wszystkich danych
* recv
* shutdown - zamknięcie gniazda
* settimeout - timeout dla operacji blokujących
	* 0 - tryb nieblokujący

## Dane binarne w Pythonie
* bytearray
* moduł struct

## API C

### Nagłówki
* Niezwiązane z gniazdami ale zazwyczaj potrzebne
	* stdlib.h
	* stdio.h
	* string.h
	* unistd.h
* Unix - gniazda
	* sys/types.h
	* sys/socket.h
	* netinet/in.h
	* arpa/inet.h
	* netdb.h
* Windows
	* ...
* API gniazd do Windowsa różni się tylko minimalnie

### Adresowanie
* adres generyczny - sockaddr - stosowany we wszystkich wywołaniahc systemowych
	* przekazywany przez wskaźnik
	* przekazuje się rozmiar struktury (adresy moga mieć różne długości)
* sockaddr_in
	* adresowanie internetowe
	* rodzina
	* port
	* adres - struktura in_addr

### Budowanie adresów
```c
sock_addr.sin_family = AF_INET;
sock_addr.sin_addr.s_addr = inet_addr("192.168.1.1");
sock_addr.sin_port = htons(8000);
```

* htons 
* htonl
* ntohs
* ntohl
host to network / network to host - konwersja z konwencji hosta na big-endian
short (16b) / long (32b)
dla maszyny big-endian nic nie robi
kod powinien być uniwersalny


Protokół jest obojętny na dane, to programista zapewnia przenośność

### `socket()`
* rodzina, typ, protokół - jak w pythonie
* `SOCK_RAW`
	* IP
	* ICMP
	* wymaga podania protokołu
* zwraca deskryptor, taki sam jak deskryptor plikowy
	* jak ten zwracany przez `open()`
	* taki sam kod do czytania z gniazd, plików, potoków
	* zwraca -1 jeśli błąd

### `bind()`
* `int bind(int sockfd, const struct sockaddr *saddr, socklen_t addrlen);`
* Przypisuje loklany adres do gniazda
* Trzeba zachować zgodność adresowania
* Do rejestracji serwera lub klienta UDP
* Sukces - 0
* Błąd - 1

### connect
* Zestawia połączenie TCP
* Funkcja blokująca
* three way handhsake
* nie wymaga wywołania bind
	* sam przydziela adres i port efemeryczny
* errno w wypadku wystąpienia błędu
	* ETIMEDOUT - timeout
	* ECONNREFUSED - druga strona odmówiła połączenia (np. nie ma otwartego portu)
	* ENETNOTREACH - otrzymaliśmy komunikat ICMP, że nie da się rutować pakietu na poziomie sieciowym
	* EISCONN - już jest połączony
* ma też sens dla UDP
	* zapamiętuje adres serwerwa
	* przydatne jeśli ma być wysłane wiele datagramów (send, zamiast sendto)
* Jeśli wystąpi błąd przy sendto to nie wiadomo co z nim zrobić
	* system nie wie gdzie ten błąd dostarczyć
* Jeśli połączymy się z gniazdem przez connect to system zapamiętuje adres odbiorcy
	* błąd po send (nie sendto) - system rozpoznaje
	* przy kolejnym wywołaniu send będzie zwrócony komunikat o błędzie dotyczący poprzednio wysyłanych danych

### listen
* wywoływana tylko przez serwer TCP
* nie jest blokująca
* zamienia socket niepołączony w socket pasywny (nasłuchujący)
* Pomiędzy wywołaniami accept w pętli
	* pojawiają się klienci
	* mogą być połączeni na poziomie sieciowym i czekają na accept
	* mogą być w trakcie nawiązywania połączenia
	* są 2 kolejki
	* backlog określa długość kolejki zestawionych połączeń
	* długość kolejki niezestawionych połączeń określa parametr kernela
* backlog
	* gniazdo serwerowe jest dużo cięższe
	* nie ma co przesadzać, doczytać dokumentację kernela

### accept
* Po powrocie może ponownie nasłuchiwać na oryginalnym gnieździe
* Pamiętać o zamykaniu gniazd
* Można nie startować nowego procesu tylko wykorzystać pulę, albo przekazać sterowanie do wątku
* Można wywoływać accept w wielu wątkach jednocześnie
	* stosowane np. w nginx
* Wiele funkcji accept na odrębnych gniazdach w odrębnych wątkach/procesach
	* dla serwerów o bardzo wysokim obciążeniu
* Nalaboratorium .... (ten prostszy wariant)

#### Serwer współbieżny
* fork
* proces potomny zwalnia gniazdo nasłuchujące i obsługuje socket nowego połączenia
	* jeśli deskryptor jest nam niepotrzebny to należy go zamknąć
	* inny proces nie zobaczy że skończyły się dane(?)
* proces rodzic zamyka nowe gniazdo

### close
* Zamyka deskryptor
* Jeśli to jedyny deskryptor to zamyka połączenie
* Jeśli jest więcej deskryptorów to zamknie deskryptor bez zamykania gniazda
* TCP najpierw spróbuje dostarczyć niewysłane dane, a następnie wynegocjować zamknięcie połączenia

### shutdown
* parametr określa jak chcemy zamknąć gniazdo
	* czy do zapisu / odczytu / obu
* zamyka gniazdo, robi inne rzeczy niż close

w unixie jest czas (typowo 30-60s) kiedy gniazdo już zostało zamknięte ale nie można go ponownie otworzyć - po restarcie serwera może wylecieć błąd
jest szansa że do strony zamykającej dotrą zduplikowane fragmenty danych - TCP sobie z tym poradzi

Python concurrent.futures.ThreadPoolExecutor