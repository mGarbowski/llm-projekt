# Routing statyczny i dynamiczny

## Tabela routingu
Każdy router przechowuje tablice routingu. Tablice mogą się różnić w implementacji ale niektóe kolumny są obowiązkowe.

* net address - adres sieci
  * 0.0.0.0/0 - domyślna ścieżka umieszczona na końcu tabeli, powinna wskazywać na następny router
* netmask
* interface - interfejs routera, do którego przyłączona jest ścieżka
* next hop
    * adres następnego routera
    * adres własny routera - dla sieci bezpośrednio przyłączonych
    * same 0
* metric - odległość od danej sieci (0 - bezpośrednio dołączaona)

W tabeli wystarczy opisać lokalną sieć i wskazać na jakiś inny router, w routerach brzegowych wystarczy kilka pozycji


## Supernetting
Agregacja wierszy z tablicy routingu. Może być zastosowana kiedy jest wolny adres i maska który dokładnie pokryje zakres adresów obejmowany przez agregowane wiersze.

* Odwrotna procedura do subnettingu
* Router wyższego szczebla nie musi znać podziału na podsieci podrzędnego routera
* Oszczędza miejsce w tabeli routingu


## Routing statyczny
* Tabela routingu konfigurowana ręcznie przez administratora
* Odporny na ataki, raz skonfigurowana sieć będzie działać tak samo
* Nie dostosowuje się do zmian w topologii sieci
* Nie sprawdzi się w sieci dostawcy internetu - każdy router musiałby wiedzieć o każdej sieci, a one ulegają ciągłym zmianom
* Jest potencjalnie niebezpieczny, konsekwencje błędów w konfiguracji

## Routing dynamiczny
* Wymaga wpisania do tabeli informacji o sieciach bezpośrednio przyłączonych
* Routery automatycznie wymieniają się wpisami ze swoich tabel routingu
* Protokoły RIP, OSPF
* Nie trzeba wymieniać danych w tabeli wszystkich routerów sieci dostawcy
