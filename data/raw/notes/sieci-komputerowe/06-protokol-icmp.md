# Internet Control Message Protocol (ICMP)
Służy do diagnostyki sieci, sprawdzania poprawności konfiguracji. Protokół pomocniczy do IP z odpowiednikiem ICMPv6 do IPv6.

## Nagłówek
* type - podprotokół
    * ECHO (program `ping`)
    * Router Advertisement / Solicitation
        * konfiguracja routera u hostów
    * Timestamp Request/Reply - informacja o aktualnym czasie (z małą precyzją), wyparty przez NTP o dużej precyzji
* code - komunikat towaryszący zapytaniu / odpowiedzi
    * Destination unreachable - niedostęny host, nieobsługiwany protokół itp.
    * Source quench - pakiet odrzucony z przyczyn wydajności
    * Redirect - pakiet wysłany nieoptymalną ścieżką, obecnie ignorowane przez luki w bezpieczeństwie
    * Time exceeded - przekroczony limit TTL
    * Parameter problem - błąd w nagłówku
* checksum
* identifier
* sequence number
* nagłówek IP i dane


## Traceroute
* Wykorzystuje pole TTL i zwrotne informacje o błędzie ICMP od routerów żeby określić jaką ścieżką są przesyłane pakiety.
    * Wysyła pakiet z TTL=1 i sprawdza od kogo dostaje odpowiedź, inkrementuje TTL i powtarza
    * Po kolei dowiaduje się informacji o kolejnych routerach
* Nie każdy router odsyła odpowiedzi ICMP
* Można określić na którym etapie pojawiają się opóźnienia (opóźnienie rzędu 200ms wprowadzają satelity)

Na podobnej zasadzie można zbadać MTU ścieżki wysyłając pakiety z flagą Don't Fragment ale nie wszystkie pakiety muszą dojść tą samą trasą