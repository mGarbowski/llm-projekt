# VPN
Virtual Private Network

## Protokoły
* Generic Routing Encapsulation
	* konfigurowany ręczne na obu końcach
* Point-to-point Tunneling Protocol
	* złamany algorytm generowania kluczy
* IPSec

## IPSec
* Framework umożliwiający wybór dostępnych mechanizmów aby zabezpieczyć komunikację użytkowników
* Protokoły
	* Authentication Header (AH)
	* Encapsulated Security Payload (ESP)
	* IKE/ISAKMP - zestawienie połączenia

### Protokół AH
* Protokół IP numer 51
	* warstwy transportowej (jak TCP, UDP)
* Zapenia integralność pakietów i autentyczność źródła
* Zabezpiecza dane i nagłówek
* Problemy jeśli na trasie jest stosowany NAT lub są modyfikowane nagłówki

### Protokół ESP
* Protokół IP numer 50
* Zapewnia poufność
	* chroni jedynie zawartość pakietu, bez nagłówków

### Asocjacja bezpieczeństwa
* Security Association (SA)
* Struktura w pamięci
* Przechowuje istotne informacje dotyczące zabezpieczonego połączenia
	* wynegocjowane algorytmy
	* wektory inicjalizacyjne
	* klucze sesyjne
	* numery sekwencyjne
	* identyfikację ruchu do zabezpieczenia
* SA przechowywane w SADB i identyfikowane przez numer SPI (Security Parameter Index)
	* SPI umieszczany w nagłówkach AH i ESP
* Jedno SA dotyczy jednego protokołu (AH / ESP) i jednego kierunku połączenia
	* dla komunikacji dwustronnej z oboma protokołami będą 4 asocjacje bezpieczeństwa (2 kierunki, 2 protokoły)

### Protokół IKE/ISAKMP
* Internet Key Exchange wykorzystuje Internet Security Association and Key Management Protocol
* Port 500 UDP
* Służy do zestawienia tunelu IPSec, wynegocjowania parametrów i wypełnienia danymi struktur SA
* Negocjuje najmocniejsze mechanizmy wspierane przez obie storny

### Topologie
* Site-to-site
	* do łączenia wielu użytkowników
	* komunikacja między dwoma urzędzeniami dostępowymi
	* tunelowy tryb pracy - cały pakiet IP i nagłówek IPSec jest umieszczony w nowym pakiecie IP
* Remote access
	* podłączenie pojedynczego użytkownika
	* najczęściej realizowane w dodatkowym oprogramowaniu
	* tryb pracy transportowy
	* nagłówek IPSec między nagłówkiem IP a danymi

### Uwierzytelnienie
* Wspołdzielony sekret
* Certyfikaty
	* zazwyczaj do remote access
	* wykorzystuje PKI

### Działanie
* Ruch interesujący - pakiety, które mają być zabezpieczone
* Sprawdzenie czy jest aktywny tunel IPSec
* Jeśli tunel IPSec nie jest aktywny rozpoczyna się proces negocjacji protokołem IKE
	* tworzy własny zabezpieczony tunel zarządzania (w tym SA)
	* w tunelu następuje negocjacja parametrów włąsciwego tunelu IPSec
* Po zestawieniu tunelu IPSec jest wykorzystywany do przesyłania ruchu użytkownika
