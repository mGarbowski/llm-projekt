# Sieci przemysłowe (2024-05-20)

## Sieć urządzeń
### Węzły
* Rozproszone IO
* Inteligentne czujniki
* ...

...

## Sieć sterująca

### Węzły
* Sterowniki lokalne i PLC
* Sterownik nadrzędny

### Warunki pracy
* Krótkie komunikaty (rzędu 10B)
* ...

## Protokoły dostępu do kabla

### Ethernet
* Algorytm CSMA/CD
* Obserwacja stanu -> nadawanie gdy wolny
* Przerwanie nadawania jeśli kolizja
* Ponowne nadanie po odczekaniu losowego czasu
* Nie nadaje się do systemu czasu rzeczywistego
* Niedeterministyczny czas przekazu
* Długosć komunikatu ograniczona od dołu
* Bardzo duża szybkość transmisji


### Odpytywanie
* Węzeł master odpytuje węzły slave
* Węzły slave odpowiadają na zapytania
* Węzły slave sa identyfikowane unikalnym numerem
* Tylko węzeł master może inicjować komunikację
* Istotny jest czas odpowiedzi węzła slave
	* wolny węzeł spowolni całą sieć
	* slave ma bufory odczytu i zapisu
	* odpowiada danymi z bufora
* Czas przekazu określa master
* Awaria węzła master zatrzymuje całą sieć
* Brak kolizji - możliwe krótkie komunikaty
* Stosowany np. w I2C

### Przekazywanie znacznika
* Równoważne węzły
* Tylko węzeł posiadający znacznik może nadawać
* Znacznik może być przesyłany innym kanałem niż główna magistrala
* Deterministyczny czas przekazu
* Problem w sytuacjach nietypowych
	* dołączenie nowego węzła
	* rozmnożenie znacznika
	* utrata znacznika

## I2C
* Do łączenia niezbyt szybkich urządzeń
* Linia zegarowa SCL
* Linia danych SDA
* Maksymalnie kilka metrów
* Podłączenie do linii przez otwarty kolektor
* Start i stop - SDA zmienia stan przy wysokim stanie zegara
	* pozostałe zmiany przy stanie niskim zegara
* ACK od urządzenia slave
* Prez otwarty kolektor
	* jeśli w jednym momencie nadaje wielu masterów
	* priorytet ma zawsze stan niski
	* master porównuje stan magistrali z nadawanymi danymi
* Będzie na lab 5 i 6
* Priorytet ma slave o niższym adresie (wspólny kolektor)

### Obsługa w Linuxie
* Wysokopoziomowy driver
* `int i2c_master_send(...)`
* `int i2c_master_recv(...)`
* `int i2c_transfer(...)`

## CAN bus
* Rozgłaszanie
* Bez adresowania węzłów
* Odpytywanie danych po id danej
* Arbitraż kolizji
	* otwarty kolektor - dominuje stan niski
* Suma kontrolna


## Profibus
* Definiuje warstwę fizyczną i aplikacyjną
* Klient - master
* Serwer - master lub slave
* Słownik obiektów


## Ethernet przemysłowy
1. Warstwa fizyczna - standard Ethernet
2. Warstwa liniowa 
	1. MAC - zmodyfikowana
	2. LLC - standard Ethernet
3. Warstwa sieciowa - IP lub brak
4. Warstwa transportowa - UDP lub TCP lub własny lub brak
5. Warstwa sesji - brak
6. Warstwa prezentacji - brak
7. Warstwa aplikacyjna - jedna z tradycyjnych

* Standardowe narzędzia
* Łatwość integracji
* Szybkość

### Protokoły
* EtherCAT - popularny w przemyśle
* Powerlink