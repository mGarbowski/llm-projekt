# 2025-03-13

## Regiony i availability zone

W Europie regiony to przykładowo
West Europe - w Amsterdamie
North Europe - w Dublinie
Central Europe - w Warszawie

W USA przykładowo
East US
West US

Odległości między najbliższymi regionami rzędu kilkuset kilometrów

Wybór lokalizacji zależy od lokalizacji klientów
round trip pakietu USA-Europa to kilkadziesiąt ms

W ramach jednego regionu (np. West Europe) są availability zones - 3 centra danych (DC) odległe od siebie o mniej niż 10 mil - niedużo
Zapis idzie synchronicznie na wszystkie 3 DC

Osiągnięcie tego samego między regionami - wprowadzałoby bardzo duże opóźnienia

Ryzyko jest dopiero, kiedy cały region ulegnie awarii - trzeba zapewnić redundancję między regionami - to wymaga innych mechanizmów niż synchroniczne zapisy

## Wirtualizacja c.d.
Narzuty na wirtualizację są małe i coraz mniejsze - stosuje się ją powszechnie

## Konteneryzacja
* Sposób pakowania i dystrybucji oprogramowania
* Aplikacja zapakowana w ustandaryzowany pojemnik
* Uruchamiają się na czymś - nie jest jak maszyna wirtualna
* Analogia do kontenerów w transporcie

### Wsparcie OS Linux dla kontenerów
* cgroups
	* część jądra
	* umożliwia przydzielanie i kontrolowanie zasobów
	* pamięć, CPU, priorytety
	* samodzielnie odpalony proces może zużywać całe zasoby
	* cgroups sztywno ogranicza proces
* Linux namespaces
	* zakres po którym proces może się poruszać
	* funkcjonalność jądra
	* z punktu widzenia aplikacje otwarcie pliku to wywołanie systemowe
	* namespace dokłada do wywołania dodatkowy parametr - namespace
	* żaden inny proces nie ma dostępu do pliku otwartego w tym namespace - gwarantuje system operacyjny
	* sieć, ipc, użytkownicy, zegary, pid, system plików

## Docker
### Architektura
* Klient
	* komunikuje się z demonem przez socket unixowy - wywołanie endpointu restowego
	* komendy typu `docker run`, `docker build`
	* nie ma autoryzacji, tylko uprawnienia do socketa na tej maszynie
* Obraz
	* plik binarny, który zawiera wszystko co pakujemy do aplikacji
	* biblioteki, JVM, jar
	* musi być dostępny lokalnie na maszynie, która go uruchamia
	* można zbudować
	* można pobrać z repozytorium
	* można pobrać z repozytorium i coś dodać
* Rejestr
	* usługa sieciowa
	* może być lokalne
* Kontener
	* na podstawie obrazu
	* ma swoje dane

### Warstwy abstrakcji
* Klient
* containerd
	* dawniej docker daemon
	* to co pobiera obrazy, zarządza sieciami itd.
* runc
	* uruchamia kontenery
	* wykorzystuje natywne funkcje systemu Linux (cgroups, namespace)

## Po co konteneryzować
* Obraz można publikować, uruchamiać
* Powtarzalne środowisko, konfiguracja
	* robimy to tylko raz i potem działa

## Przykład
* Obrazy są podzielone na warstwy
	* można nimi oddzielnie zarządzać
* Można przemapować porty bez modyfikowania aplikacji i konfiguracji
	* flaga `-p` przy uruchamianiu kontenera
* Docker daje kontrolę nad uruchomionymi kontenerami
	* można podejrzeć statystyki - zużycie CPU, pamięć, IO dyskowe, IO sieciowe
* Konteneryzacja też daje narzut
* Optymalizacja aplikacji javowej
	* do JVM podaje się rozmiar heap początkowy i maksymalny
	* docker domyślnie pozyskiwał pamięć gdzieś pomiędzy tymi 2 wartościami
	* jak zaczynało brakować heap'u w JVM - JVM próbował rozszerzyć, a docker nie dawał
	* brakuje pamięci i częściej odpala się garbage collector - wydajność spada

## Najważniejsze pojęcia
* Image (obraz)
	* plik źródłowy zawierający binaria i biblioteki do uruchomienia
	* obraz jest niezmienny (immutable)
* Container
	* uruchomiony w kontenerze proces na podstawie określonego obrazu
* Registry
	* katalog obrazów

## Docker - storage
* Do danych trwałych, które mają przetrwać wyłączenie kontenera
* Volume
	* ścieżka, która zawiera dane dla kontenera
	* w odpowiednim katalogu gospodarza
	* pliki, które są wirtualnymi systemami plików
* Bind mount
* tmpfs
	* system plików w pamięci
	* ale przetrwa restart

## Cykl życia kontenera
* ...diagram stanów...

## Docker daemon API
* RESTowe API
* Zawiera też endpointy do orkiestracji - swarm
	* zamiast tego raczej używa się Kubernetes

`docker top` - tak jak systemowy `top`


## Docker - sieci
* Tryb `bridge` (domyślny)
	* host ma dodatkowy interfejs sieciowy o ip `172.17.0.1` - kontener widzi hosta pod tym adresem, niewidoczny na zewnątrz (z puli prywatnej)
	* każdy uruchomiony kontener dostaje adres z puli `172.17.0.0/24`
	* kontenery widzą się nawzajem
	* kontenery nie są widoczne bezpośredni z zewnątrz hosta
* Tryb `overlay`
	* na hoście jest tworzona nowa sieć, do której mogą się podłączać kontenery i przez którą mogą być widoczne na zewnątrz
	* może być routing z zewnątrz do kontenerów
* Tryb `host`
	* kontener korzysta z interfejsu sieciowego gospodarza