# 2024-10-31

## Zapis na laboratoria
Laboratoria/projekt
3-osobowe zespoły
Prowadzący:
Grzegorz Blinowski - mail, najlepiej każdy od lidera zespołu
Tomasz Główka
Konrad Kamiński
Paweł Radziszewski
z każdym kontakt przez teams

zgłaszamy zespoły przez maila

pilnować używania odpowiednich adresów na laboratorium
przypis do prowadzacych z usosa jest nieistotny

## Wysyłanie i odbieranie danych
* Funkcje standardowe read, write
* Funkcje z API gniazd
	* send, recv, sendto, recvfrom
* Funkcja zachowują się inaczej niż odpowiedniki dla plików
	* odbiór/wysłanie mniejszej liczby danych niż zamierzaliśmy jest typowy
* Przypadki dla TCP read, recv
	* nigdy nie zwróci więcej bajtów niż żądamy, niezależnie od tego ile danych jest w buforze
	* zwróci maks. tyle bajtów ile aktualnie zostało zbuforowanych
	* jeśli nie ma żadnych zbuforowanych danych to blokada
* Przypadki TCP write, send
	* może wysłać mniej danych niż żądamy, trzeba sprawdzać co zwraca funkcja
	* blokuje jeśli odbiorca nie nadąża
* UDP write, send
	* wysyła datagram atomowo
	* 1 wywołanie to wysłanie jednego datagramu (dla tcp tak nie jest)
* Czasy blokowania są dużo dłuższe niż dla operacji dyskowych


## send, sendto
* Argumenty
	* deskryptor
	* bufor
	* wielkość bufora
	* flagi
* sendto tylko dla udp
* zwraca liczbę wysłanych bajtów
* zwraca -1 w przypadku błędu
* flagi

## recv, recvfrom
* zadaniem stosu jest pozbycie się zbuforowanych danyhc maksymalnie szybko
* MSG_WAITALL - czeka na skompletowanie danych
* SO_RCVBUF - rozmiar bufora
* MSG_PEEK - odczyt bufora bez usuwania z niego danych
	* dobre np. w aplikacjach wielowątkowych gdzie dyspozytor rozdziela ruch

## Korzystanie z resolvera
* W pythonie jest używany niejawnie, można podawać normalnie jako napisy
* netdb.h

### Stary interfejs
* struct hostnent *gethostbyname(char *name)
	* standardowe zapytanie
* struct hostent *gethostbyaddr(char *addr, int len, int type)
	* rekordy PTR, odwrotny DNS

### Nowy interfejs
* int getaddrinfo(...)
* Wyogdne, używa tych samych struktur so sockety

### Konwersja adresów
* inet_ntoa
* inet_aton
* inet_addr
* inet_ntop
	* uniwersalne, też dla IPv6
* inet_pton

## Przykłady
* kod na studia3
* serwer
	* jako adres można ustawić INADDR_ANY - nasłuchuje na wszystkich adresach
	* serwer może mieć wiele adresów
	* port = 0 - system przydzieli port efemeryczny

## getservbyname
* Kiedy posługujemy się standardowymi protokołami
* Nie hardkoduje się dobrze znanych portów (np. 80)
* Funkcja odpytuje systemową bazę znnaych adresów po nazwie
	* `/etc/services`

## Gniazda w domenie Unix
* Gniazda do komunikacji między procesami
* Datagramowe lub strumieniowe
	* ale to nie jest TCP/UDP przez interfejs loopback
* Rolę adresu pełnią ścieżka systemu plików
	* bez numeru portu
* Adres jest zmiennej długości

## Gniazda w innych domenach
* Wygodnie posługiwać się socket API
* ....

## Gniazda z IPv6
* Są bardziej uniwersalne funkcje do obsługi resolwera i konwersji adresów które wspierają obie wersje IPv4 i IPv6

## Multipleksowanie gniazd
* Blokujące są
	* connect, accpet, read, write
* Możemy mieć kilka gniazd, dylemat na której powinniśmy się zawiesić
	* nie wiadomo które odwiesi się jako pierwsze
	* można mieć każde gniazdo w osobnym wątku / procesie - nie zawsze dobre
	* deskryptory nieblokujące + aktywne oczekiwanie - marnowanie CPU
	* timeout + przerwania - nieefektywne czasowo
* select
	* działa na zbiorze deskryptorów
	* zbiory obsługiwane przez makra
	* liczba deskryptorów - indeksy od 0 do nfds-1
	* timeout
	* funkcja powolna - może być przerwana przez sygnał
* asynchroniczny connect
* Można też użyć select do obsługi gniazd połączeń (TCP)
	* bez wielu wątków

### poll
* lepszy select
* przekazuje się tablicę struktur z deskryptorami
* bardziej precyzyjna obsługa


## Nieblokujące wejście / wyjście
* Operacja która by blokowała, nie blokuje
	* np. read write, accept, select
* Zamiast blokowania zwraca błąd


## Rozgłaszanie (broadcast)
* Działa w takim zakresie jak umożliwia sieć lokalna
	* w podsieci ethernet
* Tylko dla UDP
* Co innego niż multicast (rozsiewanie)
	* grupa hostów, może być rozproszona
	* wymaga protokołu, który zrobi tunelowanie i lokalne rozgłoszenie
* Adres IP z adresem sieci i samymi 1 w miejscu adresu hosta
	* można użyć adresu złożonego z samych 1 - nie wyjdzie poza sieć lokalną (wycinane przez router)
	* adres INADDR_BROADCAST
* setsockopt(..., SO_BROADCAST, ...)
* Poprawnie należałoby sprawdzić jakie mamy interfejsy sieciowe i które z nich obsługują broadcastowanie

## Transmisja danych
* Przydatne przy projekcie
* Protokoły L3 i L4 nie interpretują i nie modyfikują danych użytkownika
	* TCP zapewnia poprawność przesłania
	* UDP nie zapewnia, warto używać sum kontrolnych w protokole
* Struktura przesyłanych danych (int, float) zależy od architektury, języka programowania i użytych bibliotek
* Format tekstowy (XML, JSON)
	* dobre, zapewniają przenośność, ale ma bardzo duży narzut
	* pola w strukturze C są wyrównane, pomiędzy nimi mogą być śmieci
* Warto zobaczyć jak realizowane są istniejące protokoły
* Protokół powinien być deterministyczny
	* daje się opisać przez maszynę stanów
	* definiujemy wszystkie przejścia
* Może protokół powinien być czytelny dla człowieka
* Przy przesyłaniu liczb zawsze należy stosować network order
* Polecenia powinne być spójne (np. wszystko wielkimi literami, po angielsku)
* Dobrze żeby protokół zostawiał miejsce na rozbudowę
	* mniej istotne na projekt
* Protokół powinien być udokumentowany
* Protokół powinien być solidny (robust)
	* konserwatywny w tym co wysyła
	* liberalny w tym co akceptuje - nie ufa ślepo, że są zgodne ze specyfikacją