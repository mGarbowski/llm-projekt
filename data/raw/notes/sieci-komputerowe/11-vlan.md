## VLAN
Wirtualna sieć lokalna (nie mylić z VPN)

Używane w dużych budynkach. Budynki są okablowane na etapie konstrukcji (okablowanie strukturalne) - okablowanie poziomie (od punktu zbiorczego do pomieszczeń na piętrze) i okablowanie pionowe (łączy punkty koncentracji)

Chodzi o to żeby dostosować istniejącą infrastrukturę (okablowanie strukturalne) do potrzeb użytkowników (wiele instytucji w jednym budynku)

Na poziomie przełącznika definiuje się partycje (VLANy) i przypisuje do nich konkretne porty, tak żeby odseparować od siebie ruch między partycjami. Przełącznik zachowuje się jak więcej mniejszych przełączników. Łączenie pionowe - oddzielny kabel dla każdej sieci

### 802.1q
Znakowanie - do ramki wstawia się dodatkową informację - numer VLAN, wtedy można użyć jednego kabla dla wielu VLANów

W ramce Ethernet za adresem nadawcy - 4 bajty - stare urządzenia zignorują takie ramki

* Stałe 0x8100
* Tag Control Information
    * priorytet
    * bit zarezerwowany
    * vlan id (12 bitów)

Przełączniki mogą stosować znakowane i nieznakowane ramki zależnie od potrzeb

Na poziomie systemu operacyjnego, znakowane ramki odpowiadające VLANom są widziane jako oddzielne interfejsy (nawet jeśli wszystko idzie przez jeden kabel)


### 802.1ad
Dodatkowa wstawka do ramki o stałym prefixie 0x88ab i TCI. Dodatkowa enkapsulacja do routingu między budynkami, używania niezależnego schematu numerowania VLANów w sieci szkielecie
