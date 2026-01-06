# Dynamic Host Configuration Protocol (DHCP)
Służy do automatycznego przydzielania hostom w sieci adresów IP na określony czas i dodatkowych parametrów (maska, brama domyślna, serwery DNS, nazwa domeny)

## Automatyczne konfigurowanie interfejsów
Przyznawanie adresów IP dla hostów w sieci

* RARP - Reverse Address Resolution Protocol
    * podobnie do ARP - jest znany adres sprzętowy i nieznany adres IP
    * adres przyznawany na zawsze (statyczne powiązanie z adresem sprzętowym)
* BOOTP - Bootstrap Protocol
    * przydział adresu IP, i dodatkowe niezbędne informacje (adres routera, DNS, maska)
    * adres przyznawany na zawsze (statyczne powiązanie z adresem sprzętowym)
* DHCP - Dynamic Host Configuration Protocol
    * mechanizm dzierżawienia adresu IP
    * adres przyznawany na określony przedział czasu
    * rozszerzony protokół BOOTP


## Działanie DHCP
DHCP do odkrywania używa broadcast w wersji 4 i multicast w wersji 6.

### Podłączenie do sieci
1. Host wysyła przez broadcast zapytanie DHCPDISCOVER
2. Serwery DHCP odpowiadają DHCPOFFER zawierające adres IP jaki może zostać przydzielony
3. Host wysyła przez broadcast DHCPREQUEST z adresem z oferty, którą wybiera (informuje pozostałe serwery o odrzuceniu ich oferty)
4. Serwer wybrany przez klienta odpowiada DHCPACK

### Przedłużenie dzierżawy
Po upływie czasu dzierżawy (lease time), host prosi o przedłużenie czasu.

1. Host wysyła przez broadcast DHCPREQUEST
2. Serwer, oferujący ten adres odpowiada DHCPACK

Host może zwolnić adres wysyłając do serwera DHCPRELESE, serwery nie mogą na tym polegać z przyczyn praktycznych

Po upływie czasu dzierżawy, serwer może przedłużyć czas po otrzymaniu odpowiedzi na echo request

## Pakiet DHCP
Pytający umieszcza w polu options kody porządanych informacji, odpowiadający zamieszcza odpowiedzi.

Typy pakietów
* DHCPDISCOVER - wysyłany przez klienta broadcastem, prośba o przydział adresu IP
* DHCPOFFER - wysyłany przez serwer, oferta dzierżawy adresu IP w odpowiedzi na DHCPDISCOVER
* DHCPREQUEST - wysyłany przez klienta broadcastem, prośba o przydzielenie zaoferowanego adresu IP
* DHCPDECLINE - wysyłany przez klienta, kiedy wykryje innego hosta posługującego się tym adresem (przez ARP)
* DHCPACK - przyjęty request
* DHCPNAK - odrzucony request (?)
* DHCPRELEASE - zwolnienie przydzielonego wcześniej adresu


## Pliki konfiguracyjne
* `/etc/networks/interfaces`
* `/etc/netplan/01-netcfg.yaml` - w nowszych Linuxach

## Network manager
Program zarządzający interfejsami sieciowymi

Dobre dla PC, nie nadaje się do serwerów.
