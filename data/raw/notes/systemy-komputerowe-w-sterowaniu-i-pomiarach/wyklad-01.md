# Wstęp
## Systemy wbudowane

### Możliwe realizacje systemów
* Mikrokontrolery lub mikrokomputery
* Rozwiązania bez systemu operacyjnego (bare metal), z prostym systemem, z pełnym systemem operacyjnym

* UART - Universal Asynchronous Receiver Transmitter (port szeregowy)
* GPIO - General Purpose Input/Output

### Systemy wbudowane bez OS
* Zalety
	* pełna kontrola nad zasobami sprzętowymi
	* możliwość mocnej optymalizacji
	* minimalizacja poboru mocy (np. sterowanie częstotliwością zegarów)
* Wady
	* konieczność dogłębnej znajomości platformy
	* uzależnienie od konkretnych podzespołów
	* potrzeba implementowania podstawowych funkcji, które normalnie realizuje OS (odkrywanie koła na nowo)

### Systemy Wbudowane pracujące pod kontrolą OS
* System operacyjny oferuje warstwę abstrakcji sprzętu (HAL), pozwalającą znacznie uniezależnić się od konkretnej platformy sprzetowej
* System operacyjny oferuje zarządzanie zasobami systemu wbudowanego
	* pamięć
	* czas procesora (wielozadaniowość)
	* obsługa przerwań
	* system plików
	* synchronizacja dostępu do urządzeń IO
	* komunikacja między procesami
	* mechanizmy ochrony - nie zawsze
	* obsługa standardów komunikacyjnych (Internet, Bluetooth, itp.)

## Platformy

### Dobre platformy do eksperymentów
* Platformy dobrze współpracujące z otwartym oprogramowaniem
	* STM32
	* ESP32
* Możliwość korzystania z systemów operacyjnych
* Język MicroPython - dobry do szybkiego prototypowania ale ograniczona możliwość pracy w czasie rzeczywistym
* Na bardziej złożonych systemach pójdzie Linux

### Linux
* Używany na serwerach, PC i systemach wbudowanych
* Otwarty kod źródłowy
* Dużo otwartego oprogramowania
* elixir.bootlin.com - źródła wygodne do przeglądania
* zgodny ze standardem POSIX (w miarę)

Dalej produkuje się i dobrze się sprzedają platformy o "słabych" parametrach ze względu na oszczędność energii (szybki procesor i duża pamięć kosztują)

### Ograniczenia typowych dystrybucji
* Duże wymagania co do pamięci i dysku (pamięci nieulotnej)
* Wykorzystanie pliku wymiany do wirtualnego powiększenia pamięci (zabójcze dla pamięci FLASH)
* Uzależnienie od GUI
* Ograniczona możliwość pracy w czasie rzeczywistym
	* w systemie wielozadaniowym procesy konkurują o czas procesroa
	* w systemie czasu rzeczywistego należałoby ograniczyć liczbę zadań do minimum
	* może być konieczne ograniczenie korzystania z urządzeń generujących przerwania o długim czasie obsługi
	* rozwiązaniem jest ograniczenie Linuxa do minimalistycznej wersji


### Środowiska do kompilacji Linuxa dla systemów wbudowanych
Środowiska automatycznie dbają o zapewnienie właściwego kompilatora skrośnego, bibliotek i spójny dobór opcji

* OpenEmbedded
* Yocto
* Buildroot
* OpenWRT

## Buildroot
* do małych i średnich systemów wbudowanych
* raz kompiluje się obraz i oddaje klientowi, który nie będzie wprowadzał zmian
* wygodna instrukcja w jednej stronie html
* dobre szkolenie od bootlin

### Zwykły system plików vs ramdysk startowy
* ramdysk
	* karta pamięci potrzebna tylko przy starcie systemu
	* z karty będzie załadowane jądro i system plików
	* kartę można potem sformatować itp.