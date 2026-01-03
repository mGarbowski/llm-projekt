# Stosy protokołów

## Model ISO/OSI
* (7) warstwa aplikacji
* (6) warstwa prezentacji
    * wewnętrzna reprezentacja danych
    * konwencje little/big endian
    * kodowanie znaków
* (5) warstwa sesji
    * nawiązywanie/zrywanie połączenia
    * uwierzytelnianie, autoryzacja
* (4) warstwa transportowa
    * adresowanie procesów (numer portu)
    * niezawodność transmisji
* (3) warstwa sieciowa
    * globalne adresowanie
    * routing pakietów
* (2) warstwa łącza
    * poziomy napięcia
    * postać ramki
* (1) warstwa fizyczna
    * specyfikacje kabli, gniazdek
    * właściwości fizyczne


## Model TCP/IP
* warstwa aplikacji (aplikacji, prezentacji, sesji OSI)
* warstwa transportowa
* warstwa internetu (sieciowa OSI)
* warstwa interfejsu (łącza OSI)
* warstwa sprzętowa (fizyczna OSI)

Do danych dołączane są 3 nagłówki MAC, IP i TCP/UDP i końcówka z sumą kontrolną w sieci Ethernet - enkapsulacja

Model ISO/OSI nie pokrywa się z protokołami stosu IP.

Protokoły oddzielają sprzęt od oprogramowania, to umożliwia niezależny rozwój wszystkich warstw (oprogramowania i sprzętu). Każde oprogramowanie poprawnie wspierające protokół będzie działać na każdym sprzęcie wspierającym ten protokół.

Protokoły bardzo rzadko się zmieniają, specyfikacje są stabilne.