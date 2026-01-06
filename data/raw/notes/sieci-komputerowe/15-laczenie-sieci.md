# Łączenie sieci

Maksymalna odległość jest ważnym parametrem technologii seiciowej, wynika z tego że sygnał ulega tłumieniu i z opóźnień

Sieć energetyczna powoduje zakłócenia o takiej częstotliwości (50Hz w Europie)
Silniki elektryczne
Świetlówki, zwłaszcza przy włączaniu

## Urządzenia wykorzystywane do łączenia ze sobą sieci
* Repeater
* Bridge
* Router
* Gateway

## Repeater
* Co maksymalną długość umieszcza się repeater (wzmacniacz sygnału)
* Repeater regeneruje sygnał, rozpoznaje oryginalny sygnał ze zniekształconej wersji i nadaje go dalej w wersji idealnej
* Musi rozpoznawać i odtwarzać kolizje
* Działa na poziomie warstwy fizycznej modelu ISO, rozpoznaje sygnał bit po bicie, nie ma rozróżnienia na ramki itp
* Może mieć wiele portów, port na który dochodzi sygnał zostaje portem wejściowym, a pozostałe wyjściowymi
* Nie można zamknąć pętli - sprzężenie

Żeby do sieci ethernet w standardzie kabli koncentrycznych przyłączyć jak najwięcej komputerów stosuje się sieć szkieletową (backbone)

### Repeater UTP
Stosuje się topologię gwiazdy z dwoma piętrami repeaterów, prawdziwym ograniczeniem jest tak naprawdę czas opóźnienia w danej technologii


## Bridge
* Pracuje w warstwie 2 (łącza)
* Rozpoznaje nagłówki ramek i adresy fizyczne
* Prowadzi filtrację ruchu
* Przesyła ramki tylko we właściwym kierunku - mniejsze natężenie ruchu w sieci
* Decyzje o kierunku przesyłania są podejmowanie na podstawie tabel FDB

### Forwarding Database (FDB)
* Kojarzy adresy fizyczne z portami bridge'a
* Tablice są utrzymywane automatycznie przez bridge, są rozsyłane pomiędzy bridge'ami
* Rozmiary tabel w każdym bridge'u są proporcjonalne do liczby wszystkich komputerów we wszystkich segmentach
* To rozwiązanie nie jest skalowalne

### End Bridge
* Wpisuje do tabeli FDB tylko informacje na temat komputerów przyłączonych bezpośrednio do tego bridge'a
* Drastycznie zmniejsza rozmiar tabel FDB
* Zapewnia gorszą filtrację - przesyła nadmiarowe ramki

### Spanning Tree Protocol (STP)
* Bridge'e rozpoznają się nawzajem, rozpoznają topologię sieci i znajdują drzewo rozpinające (graf acykliczny) - nie transmitują przez odpowiednie interfejsy
* Podłączenie bridge'ów w pętle nie stworzy problemów
* W razie awarii drzewo rozpinające zostanie przebudowane i mogą być wykorzystane wcześniej nieaktywne interfejsy

### Podwójny szkielet, podwójna gwiazda
Podwójna szyna łącząca wszystkie bridge'e, protokół STP zapewnia rozwiązanie problemów wynikających z pętli i zapewnia redundancję na wypadek awarii łącza

Podwójna gwiazda jest analogicznym rozwiązaniem dla szkieletu UTP o topologii gwiazdy

Administrator musi wiedzieć kiedy dochodzi do przełączenia spanning tree


## Router
* Na poziomie warstwy sieciowej

## Gateway
* Działa na poziomie od warstwy 4 (transportowej) w górę

## Hub
Marketingowe określenie - repeater, bridge, router...?

## Switch
To samo co bridge zaimplementowany w jednym układzie scalonym, marketingowe określenie

* FDB
* STP
* zaimplementowany sprzętowo (w przeciwieństwie do klasycznego bridge'a)
* store and forward - pobranie całej ramki z bufora i wysłanie ramki z bufora
* cut through
  * odbiera nagłówek
  * od razu po odebraniu nagłówka już zaczyna transmitować dalej ramkę
  * nie sprawdza się do architektur klient-serwer gdzie ruch skupia się na jednym porcie


## Domena kolizyjna
* Zbiór urządzeń, których transmisje mogą ze sobą kolidować
* Repeater nie rozwiązuje problemu
* Bridge (działając w trybie store and forward) rozdziela domeny kolizyjne
* Tak samo router rozdziela domeny kolizyjne - oddzielne interfejsy

## Domena rozgłoszeniowa
* Zbiór urządzeń, do których dotrą pakiet broadcastowe
* Repeater niczego nie ogranicza
* Bridge'e na ogół nie ograniczają broadcastu, pakiety są rozsyłane na wszystkie porty
* Router rozdziela domeny rozgłoszeniowe - każdy interfejs to oddzielna domena


## Multi-Protocol Label Switching (MPLS)
* Routing wykonuje siętylko na wejściu do sieci operatora
* Każdy router w sieci operatora może współdzielić informacje
* Pierwszy router wstawia do pakietu etykietę
* Liczba wszystkich etykiet to liczba sieci klienckich
* Każdy kolejny router wykonuje już tylko przełączanie na podstawie etykiety, bez routingu
* Z etykietą poza ścieżką można związać parametry jakościowe
* Pole flow label w nagłówku IPv6 zastępuje MPLS

## Generalized MPLS
* Rozszerzenie MPLS o więcej typów etykiet
  * Etykiety MPLS
  * Długość fali
  * Numer szczeliny czasowej
  * Port przełącznika optycznego


## Software defined networking
* Definiowanie na poziomie software'u reguł przesyłania danych na podstawie różnych parametrów (adresy IP, MAC, porty, ...)
* Może pełnić funkcję routera, bridge'a, ...
* Stosowane w chmurach, więcej elastyczności niż klasyczne urządzenia sieciowe