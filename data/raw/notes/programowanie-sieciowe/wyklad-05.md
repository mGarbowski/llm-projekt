# 2024-11-07
## Wskazówki do kodu laboratoriów
* read może zwrócić niepełne dane (w TCP)
* Pilnować zamykania gniazd
	* zwłaszcza przy wielu wątkach
* Kontrolować czy procesy/wątki się zakończyły
* Pilnować odzyskiwania pamięci
* W modelu wielowątkowym C
	* wszystko jest wspólne poza stosem
* Będą materiały dot wątków w C
* Rozważyć Google protobuf jeśli serializacja/deserializacja jest niebanalna
* Ważna decyzja projektowa - czy serializacja binarna czy do tekstu
	* binarna - bardziej oszczędna jeśli wykonana dobrze
	* tekstowa - wygodniejsza do debugowania

## Protokoły konwersacyjne

### Telnet
* Teletype over network
* Sesja zdalna, pozwala na zalogowanie do zdalnej maszyny
* Sewer jest bardzo często domyślnie włączony w unixo-podobnych
* Zastosowanie w internecie rzeczy
	* zbyt słaby hardware do obsługi kryptografii
* Wykorzystuje TCP, port 23
* Duża przenośność
* Można go używać do testowania innych protokołów tekstowych
	* połączenie narzędziem telnet do serwera SMTP, HTTP, FTP, ...
* Minimalny poziom bezpieczeństwa
* Bazuje o mechanizmie pseudoterminali z Unixa
	* mechanizm wykorzystywany też przez SSH
	* poza samym przesyłaniem znaków to można skasować znak przez Backspace, przerwać proces przez ctrl+c, ...
* Trzy podstawowe serwisy
	* moduł transmisji - symetryczne traktowanie obu stron połączenia
	* network virtual terminal - obsługa mechanizmów terminalowych
	* mechanizm negocjacji opcji (np. rozmiar okna, identyfikator terminala z Unixa, bardzo wiele różnych)
* Pozwala na negocjowanie bardzo dużej liczby opcji
* Każdy znak podróżuje zazwyczaj w osobnym pakiecie (tinygram), a echo jest zazwyczaj zdalne
	* użytkownik naciska 'a' na klawiaturze
	* wysyła się pakiet na zdalny serwer
	* zdalny serwer odsyła 'a'
	* pakietów jest 2 razy więcej ze względu na echo
	* to nie jest wielki problem przy pisaniu na klawiaturze


#### Pseudoterminal
* Użytkownik przy terminalu prowadzi interakcję ze sterownikiem terminala
	* systemowy sterownik zapewniający obsługę znaków specjalnych, pracy pełnoekranowej, ...
* Klient telnet używa terminala jako urządzenia wejścia/wyjścia
* Klient telnet zestawia sesję TCP z innym serwerem
* Po drugiej stronie sesji stoi serwer telnet
* Serwer telnet rozmawia ze sterownikiem pseudoterminala
	* obsługuje np to że okienko tekstowe ma określoną liczbę wierszy i kolumn
* Ze sterownikiem pseudoterminala rozmawia najpierw login, a potem shell

#### Algorytm Nagle'a i opóźnionego potwierdzania
* Ma optymalizować pracę zdalną - konwersacyjną i niekonwersacyjną
* Chcemy unikać przesyłania małych pakietów
	* mały czyli rozmiar mniejszy od maximum segment size
* Algorytm Nagle'a
	* nie wysyłaj pakietu małego jeśli poprzednie nie zostały potwierdzone
	* lokalny stos buforuje dane i wysyła jak skompletuje duży pakiet
* Algorytm delayed ACK
	* nie wysyłaj potwierdzenia od razu po otrzymaniu danych
	* stos wstrzymuje się, żeby razem z potwierdzeniem odesłać dane
	* dobre dla protokołu konwersacyjnego
	* dla niekonwersacyjnego (bez echa) będą długie oczekiwania przed odesłaniem ACK
* Bez echa działa np. zdalny pulpit - nie działałby dobrze z delayed ACK
* Jeśli wiemy że porotkół będzie przesyłał małe pakiety bez potwierdzeń
	* trzeba wyłączyć algorytm Nagle'a - TCP_NODELAY
	* `setsockopt`
* na kolokwium

#### Przekazywanie danych pilnych
* Pilne - pomijają buforowanie
* Out of Bound, urgent
* Powoduje wysłanie sygnału SIGURG
* np. zdalny serwer odsyła bardzo dużo danych i użytkownik przerywa przez ctrl+c
	* ctrl+c przesyłane jako pilne
* Dane pilne mogą mieć 1 bajt
	* zimplementowane w stosie sieciowym
	* mogą być umieszczone razem ze zwykłymi danymi w buforze odbiorczym (tryb inline)
	* mogą być umieszczone w odrębnym buforze - odczyt przez recv z flagą MSG_OOB
* Odbiorca rejestruje procedurę obsługi sygnału
	* zazwyczaj tylko ustawienie flagi
	* ryzykowne bo są wykonywane asynchronicznie
	* w głównej pętli sprawdzenie flagi
* ioctl - sprawdzenie czy doszliśmy do znacznika
* trzeba wywalić dane z bufora przed znacznikiem
* na kolokwium

### SSH
* Secure Shell
* De facto standard dla terminalowej pracy zdalnej
* Przewidziany jako następca telnet i usług `r` (remote) z BSD
* Port 22
* Umożliwia tunelowanie innych protokołów (port-forward)
* 5 dokumentów RFC
* Zapewnia
	* poufność
	* integralność
	* autoryzację
* Odporny na podsłuchiwanie, spoofing IP/DNS, ataki MITM, przejmowanie połączeń
* Nie jest odporny na
	* łamanie hasła
	* ataki na poziomie IP i TCP
	* statystyczną analizę ruchu
* Wersje SSH-1 i SSH-2
* Tryb konwersacyjny
	* `ssh user@server-name` - uwierzytelnienie na poziomie systemowym
	* `ssh -i keyfile.pem user@server-name` - uwierzytelnienie na poziomie protokołu
* W telnet uwierzytelnianie nie jest wbudowane w protokół
* Wygodny do zdalnego wykonywania poleceń
	* zdalne uruchomineie skryptu
	* zdalne skrypty na wielu maszynach (Ansible)
	* `cmd <lokalne parametry> | ssh user@host command` - dostanie stdout z cmd na stdin command
* Może działać z lub bez pseudoterminala
* Zdalne wykonywanie poleceń
	* `ssh user@host ls -l > local_file.txt`
	* `ssh user@host 'ls > remote_file.txt'`
	* `ssh user@host ls -l > local_file.txt 2> local-error.txt`
	* `ls -l | ssh user@host grep pattern` - mało sensowne, tylko ilustracja
* Warstwowa budowa protokołu
* Transmisja danych
	* dane podlegają kompresji
	* może wystąpić padding
	* dodawane nagłówki
	* szyfrowanie i suma kontrolna (MAC)
* Protokół autoryzacji (rozpoczęcia sesji)
	* uzgodnienie wersji
	* uzgodnienie algorytmów szyfrowania
	* wymiana kluczy
	* ...
* Jest tryb debugowy - flaga `-v`
	* najpierw jest uwierzytelniany serwer, potem użytkownik
	* ochrona przed podmianą serwera
* Osobne klucze szyfrujęce od klienta do serwera i od serwera do klienta
* Osobne klucze podpisujące
* Klucze sesji zmienane co pewien czas
	* np. co przesłany GB
	* utrudnia ataki statystyczne
* Autoryzacja użytkownika
	* publickey
	* password
	* keyboard-interactive
	* Kerberos, NTLM
	* host based - ok do sieci lokalnej

## Kolokwium
* 21 XI
* 8:30 - 10:00
* 2 grupy, podział alfabetyczny
* Test
* Pytania wielokrotnego wyboru
* 20 pkt
* bez notatek
* będą wysłane wymagania na maila

### FTP
* File Transfer Protocol
* Porty 21 i 20
	* polecenia - 21
	* dane - 20
* Protokół interaktywny
	* często stosowany z nakładką (np. przeglądarki internetowe)
* Przesyła dane bez narzutu
* Proste narzędzie do testowania przepustowości łącza
* 3 cyfrowe kody
	* 1xx - ok, i will
	* 2xx - ok, done
	* 3xx - ok, so far
	* 4xx - no, tetmp
	* 5xx - action required
	* x0x - syntax
	* ...
* Polecenia
	* USER
	* PASS
	* LIST
	* RETR
	* STOR
* Kiedy dochodzi do transferu danych
	* klient otwiera port
	* serwer inicjuje do niego połączenie ze swojego portu 20
	* *oddzwonienie*
	* nie da sie stosować w rozległych sieciach z firewallami itp
	* można to wyłączyć w trybie PASV (passive) - tak jest teraz domyślnie
	* serwer podaje port efemeryczny, do którego ma się połączyć klient
* Odpowiedź jednolinijkowa kod + opis dla człowieka
* Odpowiedź wielolinijkowa
* Protokół stanowy
	* opisuje się grafem (maszyna stanów)
	* wszystkie możliwości są dokładnie określone
* Serwer przełącza port, nie używa obu na raz
	* nie mnoży się liczby sesji przez 2, może być wielu klientów
* Przełączenie portu
	* na gnieździe można wyusić przez setsockopt zmianę adresu (SO_REUSEADDR)
	* wywołanie bind zmienia numer portu

FTP ma konwencję dostępu anonimowego
jako nazwe użytkownika podaje się anonymous
jako hasło podaje się email (nie weryfikowane)
repozytorium udostępnia pliki do pobrania

### Protokoły konwersacyjne - podsumowanie
* Cechy protokołów interaktywnych
	* tinygram
	* alg Nagle'a
	* alg opóźnionego potwierdzenia
* Praca terminalowa
	* na czym polega obsługa różnych typów terminali
	* NVT
	* co robi protokół, a co robi system (np telnet - uweierzytelnienie po stronie systemu, ssh - zależy
* Bezpieczeństwo
	* jaki protokół jaki poziom zapewnia, w jakich okolicznościach
	* nie wystawia się publicznie usługi telnet
* Dodatkowe cechy
	* możliwość zdalnego oskryptowania
	* tunelowanie innych protokołów
	* wykorzystanie telnet do testowania protokołów