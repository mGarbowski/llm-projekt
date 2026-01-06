## Session Initiation Protocol
Używany w telefonii internetowej do nawiązywania połączeń


## Metody kolejkowania
Dostęp do współdzielonego medium, wiele strumieni wejściowych i jeden wyjściowy

* FIFO - standardowa, po kolei
* Fair queueing
* Priority queueing
* Round Robin - na przemian

## Metody dostępu do medium
Współdzielenie medium transmisyjnego (kable, spektrum radiowe)

* polling
    * centralny kontroler przepytuje kolejno urządzenia
    * używany w sieciach pomiarowych
* dostęp z przekazywaniem znacznika (token passing)
    * urządzenia muszą być ustawione w pierścień (wirtualnie, nie musi być fizycznie)
    * określa się pakiet znacznikowy
    * urządzenie posiadające token jest uprawnione do przesyłania danych po czym przekazuje token do kolejnego urządzenia
* dostęp jednoczesny z wykrywaniem kolizji (CSMA/CD)
    * w sieci Ethernet
    * wszystkie urządzenia mogą wykrywać kiedy inne urządzenie nadaje i nie przerywają trwającej transmisji
    * każde urządzenie ma równe prawo do zaczęcia transmisji podczas "ciszy"
    * urządzenia mogą wykryć kiedy następuje kolizja (wielu nadawców zaczyna transmisję w tym samym czasie) i zatrzymują transmisję
    * urządzenia uczestnicząca w kolizji odczekują czas proporcjonalny do wylosowanej liczby
* dostęp jednoczesny z unikaniem kolizji (CSMA/CA)
    * WiFi
    * przed transmisją wysyła się krótki pakiet request to send
    * kolizja może wystąpić tylko w ramach pakietu request to send
    * wydobywanie się z kolizji jest tanie
    * jeśli request to send udało się przesłać to zaczyna się transmisję


## Nagłówki ramki sieci Ethernet
Różne w kolejnych standardach

* preambuła
* adres nadawcy
* ades odbiorcy
* typ - protokół następnej warstwy (IP)
* długość danych
* DSAP - Destination Service Access Port - numer stosu protokołów, uzgadniany na początku transmisji
* SSAP - Source Service Access Port
* control
* SNAP ID - zachowuje kompatybilność wsteczną
* dane
* suma kontrolna