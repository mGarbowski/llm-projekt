# TCP, UDP

## Well known services
Lista usług publikowana przez IANA, przypisująca numery portów do najczęściej używanych usług

## Porty uprzywilejowane
Numery poniżej 1024

Dla zwykłych portów (powyżej 1024), system przydzieli port jeśli nie ma konfliktu

Dla portów uprzywilejowanych (poniżej 1024), system operacyjny przydziela porty uprzywilejowana tylko procesom pracującym z uprawnieniami administracyjnymi (proces musi je mieć tylko w momencie przydziału, potem może pracować z normalnymi uprawnieniami)



## UDP
User Datagram Protocol

Umożliwia korzystanie z sieci przez wiele procesów, numer portu odpowiada procesowi w systemie operacyjnym, przyznawane dynamicznie

Nie zapewnia kontroli duplikatów, kontroli kolejności w jakiej docierają pakiety itp, za to działa szybko, z minimalnym narzutem


### Nagłówek
* (2B) source port
* (2B) destination port
* (2B) length
* (2B) checksum


## TCP
Transmission Control Protocol

Zapewnia niezawodność transmisji, ponowne przesyłanie utraconych pakietów, odczytanie w odpowiedniej kolejności. Z poziomu programu to dwa strumienie bajtów, wejściowy i wyjściowy (program pisze / czyta)

Nadawca czeka na potwierdzenie, że pakiet dotarł (przez pole acknowledgement). Nadawca może usunąć z bufora dane, których odbiór został potwierdzony.

Round-trip time wyznacza tempo w jakim będą przesyłane pakiety. Jeśli potwierdzenie nie przychodzi dłużej niż 2* średni round-trip time, to pakiety są przesyłane ponownie.

Absolutny limit - 20ms - dane mogą przebywać w buforze bez próby wysłania - unika się zakleszczenia

Acknowledgement i sequence number odnoszą się do 2 różnych strumieni

### Nagłówek
* (2B) source port
* (2B) destination port
* (4B) sequence - numer pierwszego bajtu danych w pakiecie
* (4B) acknowledgement - numer pierwszego bajtu danych, którego nie ma u odbiorcy, wszystkie bity aż do n-1 dotarły, czeka na bajt numer n
* (2B) flags
    * data offset - gdzie zaczynają się dane (bo nagłówek jest zmiennej długości)
    * URG
    * ACK - jest coś sensownego w polu acknowledgement
    * PSH - informacja o najwyższym priorytecie pomijając bufor (np do przerwania transmisji)
    * RST - konieczność synchronizacji numerów sekwencji
    * FIN - żądanie zakończenia transmisji
    * SYN - nowa (początkowa) wartość w sequence number, bo początkowa wartość nie jest ustalona z góry, tylko pseudolosowa
* (2B) window - wielkość bufora, ile bajtów można wysłać bez czekania na potwierdzenie odbioru
* (2B) checksum
* (2B) urgent
* (?B) options
    * zmiennej długości


Numer początkowy sekwencji jest pseudolosowy

### Nawiązywanie połączenia
1. Klient w stanie closed wysyła pakiet SYN z pseudolosowym numerem sekwencji A, przechodzi do stanu syn-sent
2. Serwer w stanie listen wysyła pakiet SYN ACK z numerem potwierdzenia A+1 i pseudolosowym numerem sekwencji B, przechodzi do stanu syn-received
3. Klient wysyła pakiet ACK o numerze potwierdzenia B+1 i numerze sekwencyjnym A+1 (nie ma flagi SYN, bo numer sekwencji wynika z poprzedniego pakietu), przechodzi do stanu established
4. Następny pakiet może wysłać klient lub serwer

### Okno
Nie trzeba każdorazowo czekać na potwierdzenie pakietu, bo traci się dużo czasu na czekanie.

Wysyła się tyle pakietów ile określa odbiorca w rozmiarze okna i potem czeka się na potwierdzenie, dla odpowiednio dużego okna transmisja jest płynna i efektywnie wykorzystuje przepustowość łącza
