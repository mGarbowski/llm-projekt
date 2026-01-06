# (2024-03-18)
Sprzęg procesowy - zmiana sygnałów logicznych na odpowiednie dla sterowanego układu

Optoizolacja - zamiast przekaźników (dioda emitująca światło i fototranzystor)
* fizycznie izoluje 2 układy

Wejścia analogowe - konwertery analogowo cyfrowe
* mierzą poziom napięcia na jednym z wejść
* start/stop
* może być sterowany przez zapis/odczyt do odpowiednich rejestrów

Wyjście analogowe
* Przetwornik cyfrowo-analogowy
* Zamienia wartość bitową na odpowiednie napięcie
* Rzadko stosowane, częściej PWM
    * Moc uzyskiwana przez uśrednienie zmiennego sygnału cyfrowego (poziom wypełnienia)

Architektury
* intel x86
* arm
* ...

Watchdog - monitorowanie stanu programu
* może wymusić reset systemu


## Szeregowanie kooperatywne
## Rozplanowanie czasowe
* Czas procesora dzielony na takty
* W każdym takcie wykonuje się te zadania które trzeba ze względu na ich ograniczenia i te które jeszcze da się wcisnąć w ten takt

## Przerwania
* Np komunikację z zewnętrznymi urządzeniami można obsłużyć od razu, w bardzo krótkim czasie

## Szeregowanie stałe
* Dokładnie wiemy jakie są ograniczenia
* stałe (pre-run) - zahardkodowana kolejność
* Szeregowanie niewywłaszczające
* Ograniczone wywłaszczanie jeśli wykorzystywane przerwania

Procedura obsługi przerwania na początku kasuje przerwanie, które je wywołało (wyzerowanie odpowiedniego rejestru)


WEJŚCIÓWKA SKPS LAB2 
1. Wymieć 3 cechy OpenWRT 
	1. wbudowany menedżer pakietów
	2. nie ma konieczności rekompilacji przy każdej zmianie
	3. można pobrać gotowy skompilowany
2. Co potrafi dd? Podaj przykład użycia 
	1. manipulowanie plikami
	2. nagrać iso na nośnik
3. podaj różnice między gpio a QEMU 
4. Podaj różnice między openWRT a buildroot
	1. buildroot trzeba rekompilować żeby dodać pakiet, na openwrt jest manager pakietów
	2. openwrt bardziej elastyczny ale mniej zoptymalizowany
	3. openwrt pozwala instalować pakiety podczas działania systemu
5. Obsługa gpio przez sysfs
	1. `echo 27 > /sys/class/gpio/export`
	2. `echo out > /sys/class/gpio/gpio27/direction`
	3. `echo 1 > /sys/class/gpio/gpio27/value`
	4. `cat /sys/class/gpio/gpio27/value`