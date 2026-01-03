# Sieci bezprzewodowe

## Standardy
* Standard IEEE 802.11 - pierwszy standard WiFi
  * 2.4 GHz, 5GHz
  * krótkodystansowe - rzędu kilkudziesięciu metrów
* Standard IEEE 802.16 - WiMax
  * sieć dostępowa dla obszarów podmiejskich - rzadka zabudowa, nie opłaca się ciągnąć kabli
  * długie dystanse rzędu kilometrów

Przy konfigurowania acces pointu WiFi należy przeskanować które pasma są zajęte i wybrać takie, żeby unikać kolizji

## Zasięg
Maksymalna szybkość transmisji maleje wraz z odległością
W pomieszczeniach ze względu na odbicia zasięg jest mniejszy niż na otwartej przestrzeni

## Tryby pracy

### Ad-hoc
Przeznaczone do Personal Area Network (połączenie z komputerem aparatu, drukarki itp.) bez acces point'u

### Infrastructure mode
Wyróżnione centralne urządzenie - acces point. Wszystkie transmisje odbywają się za jego pośrednictwem

## Problem ukrytego węzła
(hidden node)

Każde z urządzeń widzi access point ale urządzenia nie widzą się nawzajem, mogą zaczynać jednocześnie transmisje i zakłócać się nawzajem

## Physical Layer Convergence Protocol
* Początek ramki transmitowany z najniższą prędkością żeby mógł zostać odebrany przez wszystkie urządzenia


## Ramka MAC
* Adres jest powielony na wypadek zakłóceń

## Unikanie kolizji
* Nadawca wysyła Request To Send
* Jeśli nie ma kolizji to access point odsyła Clear To Send
* Nadawca zaczyna transmisję danych
* Rozwiązuje problem ukrytego węzła

## Podział pasma
### 2.4 GHz
* 14 kanałów
* w różnych regionach różne dozwolone

### 5 GHz
Kanały o różnych szerokościach


## Metody modulacji
* Binary Phase Shift Keying
  * 1 - sinusoida
  * 0 - sinusoida przesunięta o 180 stopni
* Quadrature Phase Shift Keying
  * Wiele wartości przesunięć fazowych kodujących wiele bitów naraz

## Zabezpieczenia
* SSID - Service Set Identifier
  * musi pojawiać się w każdej ramce przesyłanej w sieci
  * sieci otwarte rozgłaszają swój SSID prez beacon frames
  * dla sieci zamkniętych trzeba go wpisać ręcznie
  * może zostać podsłuchany
* Uwierzytelnianie adresem MAC
  * whitelist adresów upoważnionych urządzeń
  * adresy mogą być podsłuchane
* Szyfrowanie i uwierzytelnianie WEP (Wireless Enhanced Privacy)
  * wspólny klucz, niemożliwy do podsłuchania
  * złamane, za słaby szyfr
* WiFi Protected Access (WPA)
* IPsec
  * najmocniejsze szyfrowanie
  * dla urządzeń mobilnych mocniejsze szyfrowanie bardziej obciąża baterię