# DNS

Hierarchiczna, rozproszona baza danych. Ma drzewiastą strukturę, poddrzewa są obsługiwane przez oddzielne serwery

Serwer Bind - oficjalna referencyjna implementacja serwera DNS

## TLD
Top level domain - domeny najwyższego szczebla

gTLD - ogólne gov, com, edu

ccTLD - country code, państwowe pl, fr, de, uk

Konkretne kraje w różne sposoby przypisują niższe szczeble (często na wzór gTLD edu.pl, com.pl)


## Odwrócony DNS
Odpowiedź na pytanie "Jaką domeną posługuje się ten adres IP?" wymagało przeszukania całego drzewa DNS (ze względu na hierarchiczną budowę)

Do tego został stworzony reverse DNS w poddomenie in-addr.arpa

## Rekursywny serwer
Po stronie klienta resolver to dynamicznie linkowana biblioteka

Tak naprawdę to nie ma tam rekurencji tylko iteracyjne odpytywanie kolejnych serwerów

Master files

Odpowiedzi są cache'owane - to odciąża serwery wyższych szczebli

* Jeśli żadnej domeny nie ma w cache'u to pierwsze zapytanie jest wysyłane do jednego z serwerów root (podany w master file)
* Serwer root przekierowuje do serwera DNS niższego szczebla np `pl`
* Serwer rekursywny cache'uje odpowiedź i odpytuje kolejny serwer
* Serwer `pl` przeszukuje swój cache i przekierowuje do serwera niższego szczebla
* Serwer rekursywny cache'uje odpowiedź i odpytuje kolejny serwer
* ...
* Ostatni serwer zwraca odpowiedź autorytatywną


## Odpowiedź autorytatywna
* Kończy poszukiwanie w DNS
* Może być pozytywna lub negatywna

## Zapobieganie atakom DoS
Można postawić firewall - zostawić dostęp tylko dla użytkowników w sieci lokalnej

Przy ataku z wnętrza sieci można odciąć zainfekowanego hosta (odpiąć kabel)

Te metody są nieskuteczne dla publicznych serwerów DNS gdzie nie ma jak rozróżnić dobrych i złych zapytań. Wtedy wyłącza się obsługę rekursywnych zapytań, serwer odpowiada tylko na podstawie własnego cache'a.


## Budowa rekordu
* nazwa
  * litery Unicode, cyfry, '.', '-'
  * może być wiele rekordów o tej samej nazwie (np. jeśli komputer ma wiele interfejsów)
  * jeśli danej nazwie odpowiada wiele rekordów to są zwracane wszystkie adresy (przetasowywane przy kolejnych zapytaniach)
* czas życia (TTL)
  * w sekundach
  * maksymalny czas przechowywania w serwerach buforujących (rekursywnych)
  * określany przez autora rekordu
  * po jego przekroczeniu serwery powinny usunąć ten rekord z cache i ponownie odpytać serwer autorytatywny
  * rzędu tygodnia
* klasa
  * IN - Internet (jedyna faktycznie używana)
* typ
  * jak należy interpretować zawartość
  * SOA - początek opisu domeny, jeden egzemplarz w każdej domenie
  * NS - serwer obsługujący domenę, conajmniej 2 w każdej domenie (master/primary, slave/secondary)
  * A - adres IPv4
  * AAAA - adres IPv6
  * PTR - odsyła do innego rekordu (w pełni kwalifikowana nazwa)
  * CNAME - nazwa alternatywna (aliasy), wartość to nazwa kanoniczna, najczęściej wskazuje usługi
  * MX - serwer pocztowy, priorytet i nazwa serwera
  * TXT - dowolny tekst
  * SRV - serwer usługi, związany z service discovery
  * DNSKEY - klucz serwera
  * RRSIG - podpis rekordu
* wartość
  * wartość zależna od typu

### SOA
Informacje dla serwerów typu slave. Slave porównuje numer sekwencyjny i aktualizuje swoje dane jeśli numery się nie zgadzają

Master może wymusić aktualizację serwera slave szybciej niż to wynika z parametru refresh (pakiet UDP)

* Serial - numer sekwencyjny, musi rosnąć po aktualizacji, zalecany YYYYMMDDnn
* Refresh - Co ile sekund należy sprawdzać aktualność danych
* Retry - Co ile sekund ponawiać nieudaną próbę
* Expire - Po ilu sekundach uznać za nieaktualne
* Minimuim - minimalny czas przechowywania (domyślny TTL)


## Widoki
* Ograniczenie dostępu dla użytkowników z zewnątrz sieci
* W zależności od adresu pytającego, serwer zwraca różne odpowiedzi
* Dyrektywa `match-clients {...}`
* Najczęściej definiuje się oddzielny widok publiczny i prywatny

## Dynamic DNS (DDNS)
* Potrzeba odzwierciedlenia w DNSie dynamicznego przydziału adresów IP
* Czas życia rekordu DNS musi być krótki - ogranicza możliwość cache'owania
* Powinno się stosować oddzielne serwery do dynamicznego DNS

* Serwer DHCP przydzielający adres zgłasza to do serwera DNS
* Serwer DHCP przydziela adres, host zgłasza to do serwera DNS
  * częściej stosowane
  * mniej bezpieczne, konflikty nazw, możliwość podszywania się

## Service discovery
* Rekordy typu SRV
* `_service._protocol.domain.name ttl class SRV priority weight port target`
* `_service._protocol.domain.name ttl class TEXT parameters`


## DNSsec
* Uniemożliwienie podrabiania zawartości DNS
* Zabezpieczenie przed podszywaniem się pod serwer DNS
* Dla każdej grupy rekordów identyfikokwanej przez nazwę i typ rekordu jest generowany podpis na podstawie klucza prywatnego
* Rekordy DNSKEY też trafiają do cache'a, weryfikowanie podpisu nie jest kosztowne
* 12% użytkowników weryfikuje podpisy

### Łańcuch zaufania
* Najwyżej w łańcuchu jest IIANA, publikuje swoje klucze publiczne
* Każdy kolejny poziom jest podpisany kluczem poziomu wyżej(???)


## Konfiguracja resolvera na komputerze
* plik /etc/resolv.conf
* `search` - końcówki doklejany do nazwy krótkiej
* `nameserver` - adresy serwerów, odpytywane w kolejności takiej jak w pliku
* `nameserver 127.0.0.1` - na localhoscie, powienien być pierwszy jeśli faktycznie działa taki serwer ale spowalnia system jeśli go nie ma


## Konfiguracja serwera bind
`named-checkzone`

### /etc/boot.conf
* directory - ścieżka do katalogu z resztą plików
* cache - nazwa pliku ładowanego do cache'a przy starcie, przynajmniej serwery domeny głównej
* primary - serwer master, domena i domena odwrotna nie muszą być obsługiwane przez ten sam serwer
* secondary - serwer slave


### /etc/named.conf



