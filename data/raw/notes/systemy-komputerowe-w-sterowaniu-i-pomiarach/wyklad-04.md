# Buildroot cd (2024-03-11)

## Rozszerzenie Buildroota o skrypty
* Można dodać na etapie kompilacji przez mechanizm nakładek na system plików
* Przez SSH jeśli buildroot ma klienta SSH
* Można postawić serwer HTTP na stacji roboczej i pobrać na maszynie przez wget
    * wget domyślnie usuwa atrybut wykonywalności
* Można przez konsolę szeregową jeśli nie ma komunikacji sieciowej, ale będzie wolno i niewygodnie

### Uruchomienie skryptu przy starcie systemu
* Zależy jaki jest używany mechanizm uruchamiania systemu
    * dla systemV i busybox jest katalog `/etc/init.d`
    * może być problem jak skrpyt ma rozszerzenie .sh i zawiera błąd
    * skrpyt musi się zakończyć, oddać sterowanie
    * puszczenie procesu w tle przez `&` ma tragiczne konsekwencje
    * do włączania usług służy makro `start-stop-daemon`

## Kompilowanie programu w języku C
* Buildroot kompiluje programy na maszynę docelową - może mieć inną architekturę
* Trzeba użyć odpowiedniego kompilatora skrośnego
    * np. w Makefile można ustawić jako zmienną
    * to jest ok dla małych programów
    * nie są poustawiane flagi z buildroota itp(?)
* `make sdk` tworzy przenośną wersję własnego toolchainu
* Do bardziej złożonych programów tworzy się własne pakiety (nie omawiamy, są linki na slajdach i przykład)
    * Trzeba jeszcze dodać wpis w nadrzędnym `Config.in`
* Można źródła własnych pakietów przechowywać poza katalogiem buildroot 
    * `BR2_EXTERNAL`

## Hot plug
* Podłączanie urządzeń w czasie działania systemu wymaga doinstalowania `eudev`
    * reguły udev - do doczytania

## Debuggowanie
* Można przez gdb podłączyć podłączyć się do systemu z buildrootem
* Musiał być zbudowany na tej stacji roboczej na której odpalamy gdb (z obrazem, symbolami debuggera itd)


## OpenWRT
* Buildroot kompiluje się szybko ale często może wymagać pełnej rekompilacji
* OpenWRT pozwala instalować i odinstalowywać pakiety bez reinstalacji systemu i jest prekompilowana wersja do pobrania
* Używa zapisywalnego systemu plików
    * squashfs - mocno skompresowany, read-only - fabryczna wersja
    * jffs2 - nakładka na ten podstawowy system plików - własne modyfikacje
* System `opkg` - package manager
* Żeby uruchomić prekompilowany system trzeba dołożyć odpowiednie moduły jądra
    * np. sterowniki urządzeń `kmod-*`


## Jak zacząć pracę z OpenWRT
* Pobranie najnowszej stabilnej wersji dla naszej platformy (qemu arm-virt, raspberry pi)
    * obraz, system plików
    * można opcjonalnie pobrać sdk
* Domyślnie przyznaje sobie adres `192.168.1.1` - niedobrze
* LuCI, UCI - do konfiguracji tekstowy i graficzny
    * uwaga na UCI bo może kasować komentarze
* Trzeba coś ręcznie zmienić żeby mieć łączność sieciową
    * `/etc/config/network` static -> dhcp
* Można skompilować własną wersję OpenWRT ze źródeł
* `make menuconfig`
* `make kernel_menuconfig`
* `make clean` nie niszczy kongiuracji
* Można kompilować wielowątkowo!
* Czyszczenie
    * clean tylko bin i build_dir
    * dirclean czyści powyższe, staging_dir, toolchain, logs
    * distclean najgłębsze czyszczenie
* Dodawanie własnych pakietów w oparciu o Makefile
* Można określać zależności między pakietami

## Tworzenie własnego pakietu

