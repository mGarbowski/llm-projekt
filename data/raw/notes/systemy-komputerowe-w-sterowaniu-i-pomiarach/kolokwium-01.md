# Kolokwium 1

## Różnice między systemami wbudowanymi, a zwykłymi systemami komputerowymi
System wbudowany jest systemem komputerowym, który wypełnia określoną rolę w większym systemie (elektronicznym, mechanicznym). Typowo systemy wbudowane muszą pracować przy ograniczonych zasobach sprzętowych (pamięć, dysk, pobór mocy) i ograniczeniach czasu rzeczywistego.

## Różne podejścia do tworzenia oprogramowania dla systemów wbudowanych
### Bez OS (bare metal)
* Zalety
	* pełna kontrola nad zasobami sprzętowymi
	* możliwość ustawiania priorytetów obsługi przerwań
	* możliwość optymalizacji pod kątem konkretnego zastosowania
	* możliwość minimalizacji poboru mocy
* Wady
	* konieczność dogłębnego poznania platformy sprzętowej
	* uzależnienie od konkretnych podzespołów (nieprzenośność)
	* odkrywanie koła na nowo bez standardowych funkcji OS

### Z systemem operacyjnym
* Można użyć specjalnego, prostego systemu operacyjnego lub okrojonwego Linuxa
* Dostarcza warstwę abstrakcji sprzętu, uniezależnia się do konkretnych podzespołów
* Zarządza zasobami
	* pamięć
	* czas procesora (wielozadaniowosć)
	* obsługa przerwań
	* system plików
	* synchronizacja dostępu do urządzeń
	* komunikacja międzyprocesowa
	* ochrona
	* obsługa mechanizmów komunikacyjnych (internet)

## Przykłady platform sprzętowych nadających się do realizacji systemów wbudowanych, pracujących pod kontrolą systemu Linux
* Raspberry Pi
* Orange Pi
* Banana Pi
* Nano Pi

## Powody, dla których w przemysłowych systemach wbudowanych chętnie stosujemy specjalizowane wersje systemu Linux (a nie zwykłe dystrybucje)
* Ograniczona pamięć i przestrzeń dyskowa
* Pamięć FLASH nie nadaje się do realizacji pamięci wirtualnej (plik / partycja wymiany)
* Możliwy brak dostępu do interfejsu graficznego
* Ograniczenia czasu rzeczywistego
	* w normalnych dostrybucjach jest za dużo procesów konkurujących o czas procesora
	* przerwania o długim czasie obsługi
	* problemy rozwiązuje przygotowanie minimalistycznej wersji Linuxa


## Środowiska pozwalające na stworzenie obrazu systemu Linux dedykowanego dla systemu wbudowanego
Zapewniają kompilatory skrośne, biblioteki i szerokie możliwości konfiguracji

* OpenEmbedded
* Yocto project
* Buildroot
* OpenWRT

## Środowisko Buildroot - podstawy użytkowania, wybór konfiguracji, składników systemu, wybór konfiguracji jądra
* Środowisko do kompilacji Linuxa dla systemów wbudowanych
* Po skompilowaniu nie ma możliwości instalowania pakietów
* Modyfikacja wymaga rekompilacji systemu
* Trzeba wybrać system plików
* Wykorzystuje GNU Make
	* `make menuconfig` - menu konfiguracyjne
	* `make nazwa_defconfig` - wybór gotowej konfiguracji dla platformy sprzętowej
	* `make clean all` - pełna rekompilacja
	* `make` - kompilacja tylko potrzebnych pakietów (według make)
	* `make linux-menuconfig` - konfiguracja jądra

## Możliwe sposoby rekompilacji Linuxa w systemie Buildroot, ich wady i zalety, wybór właściwego sposobu rekompilacji w różnych warunkach
* `make` - prosta i najszybsza rekompilacja
	* uproszczone badanie zależności między pakietami
	* może dać niepoprawny wynik
	* konfiguracja jednego pakietu może wpływać na sposób kompilacji innego
* `make nazwa1-dirclean all` - wymuszenie rekompilacji konkretnego pakietu
	* ręcznie wymuszamy rekompilacje, tam gdzie `make` nie wykrywa że jest ona potrzebna
* `make clean all` - pełna rekompilacja
	* najwolniejsze - rekompilacja wszystkiego
	* najpewniejsze

## Emulator QEMU - właściwości i możliwości wykorzystania do uruchamiania i testowania Linuxa dla systemów wbudowanych
* Emulowanie systemu wbudowanego
* Badanie zachowania systemu przy ograniczeniach sprzętowych (pamięć, dysk)
* Testowanie z rzeczywistymi urządzeniami
* Testowanie z wirtualnymi urządzeniami, definiowanymi przez użytkownika
* Emulacja karty sieciowej
* Emulacja karty dźwiękowej
* Mapowanie plików z maszyny gospodarza prez 9P


## Wybór systemu plików dla Linuxa używanego w systemie wbudowanym. Różnice między pracą z rzeczywistym systemem plików, a "ramdyskiem startowym" (initramfs)
* Zwykły system plików (np. ext4)
	* kernel ładowany do pamięci z nośnika przy starcie systemu
	* system plików na nośniku (karta SD) jest zamontowany przez cały czas pracy systemu
	* zmiany zapisywane na nośniku
* Initramfs
	* przy starcie systemu ładowany do pamięci kernel i system plików
	* zapisy w pamięci, nie modyfikują nośnika
	* po starcie systemu, nośnik może być dowolnie modyfikowany
	* dobre kiedy na systemie może jeszcze nie działać obsługa pamięci masowej
	* możliwość aktualizacji obrazu systemu w trakcie jego pracy
	* zmiany w systemie plików nie zachowują się po restarcie systemu

## Zagrożenia związane z wgraniem błędnego (np. błędnie skonfigurowanego lub błędnie zbudowanego) systemu operacyjnego do systemu wbudowanego. Sposoby zapobiegania ryzyku nieodwracalnego, lub trudno odwracalnego zablokowania systemu. Sposoby realizacji i uruchamiania "systemów ratunkowych"
* Zagrożenia
	* możemy stracić komunikację z systemem (np. przy złej konfiguracji sieci)
	* system może w ogóle się nie uruchomić
	* system może działać nieprawidłowo
* Żeby zapobiec zablokowaniu systemu wbudowanego przez wadliwy system operacyjny możemy wgrać dodatkowy system ratunkowy
	* wybór uruchamianego systemu z poziomu bootloadera
	* wybór uruchamianego systemu przez fizyczny przełącznik (jeśli wspiera to firmware)

## Typowe interfejsy do podłączania urządzeń peryferyjnych do systemów wbudowanych. Możliwości ich obsługi "z przestrzeni użytkownika" (czyli bez tworzenia dedykowanych sterowników działających w przestrzeni jądra)
Obsługa urządzenia peryferyjnego z przestrzeni użytkownika polega na podłączeniu go przez określony interfejs (np. GPIO, SPI, I2C) i wykorzystanie istniejących sterowników do tych generycznych interfejsów w programie obsługującym urządzenie peryferyjne

### GPIO
* General Purpose Input Output
* obsługa przez zapis i odczyt z odpowiednich plików (sysfs) lub użycie przenośnych bibliotek
### SPI 
* Serial Peripheral Interface
* Jedno urządzenie master i wiele urządzeń slave
* Linie sygnałowe
	* SCLK - zegar
	* MOSI - master output slave input
	* MISO - master input slave output
	* SSX - slave select (X to numer urządzenia slave), po 1 na urządzenie slave
* dostęp przez sterownik `spidev`
* pliki specjalne `/dev/spidevX.Y`, `X` - numer magistrali, `Y`- numer urządzenia
* żeby wykonać operację jednoczesnego zapisu i odczytu trzeba wypełnić odpowiednią strukturę parametrami i użyć funkcji `ioctl`
* nie można użyć `read` i `write`, bo interfejs wymaga jednoczesnego odczytu i zapisu
* można obsłużyć interfejs SPI przez piny GPIO (używając odpowiedniego sterownika)
### I2C
* Jedna magistrala obsługuje wiele urządzeń
* Linie
	* SDA - dane
	* SCL - zegar
	* zasilanie
* Sterownik i2c-dev
* Pliki specjalne `/dev/i2c-N`, `N` to numer kontrolera
* Proste transfery przez `read` i `write`, bardziej skomplikowane przez `ioctl`
* Może być obsłużony przez piny GPIO używając odpowiedniego sterownika

## Możliwości obsługi interfejsu GPIO - dedykowane dla RPi i przenośne między różnymi systemami wbudowanymi. Cechy "starego" systemu opartego na sysfs i "nowego", wykorzystującego libgpiod

### Obsługa przez sysf
* `echo number > /sys/class/gpio/export` - przejęcie pinu GPIO
* `echo number > /sys/class/gpio/unexport` - zwolnienie pinu GPIO
* `echo in > /sys/class/gpio/gpioNN/direction` - ustawienie pinu jako wejście
* `echo 1 > /sys/class/gpio/gpioNN/value` - ustawienie stanu wysokiego na pinie
* `cat /sys/class/gpio/gpioNN/value` - odczyt wartości na pinie
* Jeśli trzyma się otwarty plik, to przed kolejnym odczytem trzeba go przewinąć na początek
* Jest deprecated ale nadal używany
* Łatwy w obsłudze, do wykorzystania w skryptach

### Obsługa przez libgpiod
* GPIO traktowane jako urządzenie znakowe
* Zarządzene przez proces który otworzył to urządzenie
* Szybszy dostęp
* Bardziej ograniczone możliwości użycia w skryptach
* Możliwe definiowanie bardziej złożonych zachowań wyprowadzeń

## Środowisko OpenWRT - cechy szczególne, różnice w stosunku do Buildroota
* Buildroot jest bardziej zoptymalizowany do potrzeb zadania, OpenWRT mniej zoptymalizowany
* OpenWRT pozwala doinstalowywać i odinstalowywać pakiety podczas pracy systemu, Buildroot może wymagać pełnej rekompilacji
* Dla OpenWRT można pobrać gotowe, prekompilowane wersje
* OpenWRT ma manager pakietów `opkg`
* OpenWRT jest mniej oszczędny względem zasobów ale bardziej elastyczny

## Obsługa instalowalnych pakietów w OpenWRT - podstawowe operacje
* Manager pakietów `opkg`
* Obsługuje pakiety typu `.ipk`
* Dostępne też przez interfejs webowy LuCI
* `opkg install`
* `opkg remove`
* `opkg files` - lista plików zawartych w pakiecie
* `opkg update` - pobranie listy dostępnych pakietów
* `opkg list` - lista pakietów
* `opkg list-installed` - lista zainstalowanch pakietów

## Różnice między pakietami w Buildroocie i w OpenWRT
* W Buildroocie pakiety można dodać na etapie kompilacji systemu
* Na OpenWRT można instalować i usuwać pakiety w trakcie działania systemu
* Do tworzenia pakietów wykorzystuje się SDK z odpowiednim dla platformy docelowej kompilatorem skrośnym
* Pakiety opierają się na Makefiles w odpowienim formacie i plikach konfiguracyjnych

## Sposoby modyfikacji konfiguracji OpenWRT
* `make menuconfig` - konfiguracja systemu do kompilacji
* `make kernel_menuconfig` - konfiguracja jądra do kompilacji
* `scripts/feeds` - przygotowywanie pakietów do kompilacji
* LuCI, UCI - konfiguracja działającego systemu (np. ustawienia sieciowe)
	* LuCI - graficzny interfejs webowy
	* UCI - interfejs konsolowy
* `opkg` - zarządzanie instalowalnymi pakietami

## Różnice między dostępnymi trybami rekompilacji w Buildroocie i w OpenWRT
* OpenWRT
	* `make clean` - czyści tylko wyniki kompilacji
	* `make dirclean` - czyści również toolchain, logi i staging_dir
	* `make distclean` - czyści wszystko łącznie z konfiguracjami
* Buildroot
	* `make clean` - czyści wszystkie moduły, niszczy konfigurację jądra
	* `make nazwa-dirclean` - czyści konkretny moduł
## Metody przenoszenia programów (skryptów i skompilowanych aplikacji) między stacją roboczą a uruchamianym systemem wbudowanym
* Wykorzystanie nakładki na system plików
	* wymaga rekompilacji
* Przesłanie pliku przez sieć
	* przez `scp` jeśli system jest zbudowany z klientem SSH
	* pobranie z serwera HTTP, np. przez `wget`
* Przygotowanie pakietu
	* w dedykowanym formacie np. dla Buildroota, OpenWRT
	* dodanie pakietu i rekompilacja Buildroota
	* zainstalowanie pakietu OpenWRT przez manager pakietów `opkg`
* Przesłanie pliku przez konsolę szeregową (niewydajne)

## Praca z SDK w środowisku OpenWRT
* OpenWRT umożliwia zbudowanie SDK, które umożliwia tworzenie i kompilowanie własnych pakietów
* SDK pozwala kompilować pojedyncze pakiety bez rekompilacji całego systemu
* Wykorzystuje się Makefiles i skrypt `feeds` do określenia plików źródłowych, zależności (bibliotek) itd
* `make package/nazwa/compile` tworzy pakiet w formacie `.ipk`
* Pakiet `.ipk` można pobrać na system wbudowany i zainstalować używając `opkg` 

## Czy w typowym systemie wbudowanym pracującym pod kontrolą systemu Linux możemy użyć partycji lub pliku wymiany aby wirtualnie zwiększyć pojemność pamięci RAM? Proszę uzasadnić odpowiedź. Ewentualnie proszę uwzględnić możliwe warianty
Pamięć FLASH (np. karty SD), ze względu na ograniczoną liczbę operacji kasowania nie nadają się do realizacji pamięci wirtualnej (bardzo szybko się zużywa). Można by skorzystać z takiego mechanizmu do powiększenia dostępnej pamięci, gdyby użyć innego nośnika pamięci nieulotnej, który jest pozbawiony tego problemu.

## Jakie jest zastosowanie "systemu ratunkowego" w systemie wbudowanym działającym pod kontrolą systemu Linux? Jak możemy taki system zaimplementować? Proszę opisać przykładową implementację na wybranej przez siebie platformie sprzętowej
System ratunkowy pozwala uruchomić system w przypadku, gdy dedykowany system operacyjny zawiera błędy i np. zastąpić go poprawionym systemem operacyjnym. Można wtedy bez fizycznego wyjmowania nośnika z płytki uruchomić stabilny system ratunkowy, pobrać nową wersję systemu przez sieć i wgrać go na odpowiednią partycję.

Można oba systemu umieścić na oddzielnych partycjach karty SD i wykorzystać firmware platformy Raspberry Pi, żeby podczas uruchamiania wybrać, który system zostanie uruchomiony na podstawie sygnału na pinie GPIO (np. podłączonym do przycisku).

Można wykorzystać odpowiedni bootloader i wybierać, który system ma wystartować przez interfejs szeregowy

## Czy możemy stworzyć instalowalny pakiet z naszą aplikacją dla OpenWRT bez pobierania i rekompilacji pełnych źródeł OpenWRT? Jeśli tak, to jak możemy to zrobić? Proszę opisać podstawowe etapy przygotowania środowiska pracy i budowania takiego pakietu
Nie trzeba kompilować pełnych źródeł, można pobrać prekompilowane SDK dla odpowiedniej platformy.

Pakiet można przygotować przez utworzenie `Makefile` w odpowiednim formacie (specyfikuje pliki źródłowe, sposób ich kompilacji, linkowania, biblioteki) i wykorzystaniu skryptu `feeds`. Kompilację pakietu do postaci `.ipk` wykonuje się przez `make package/nazwa/compile`.

## Opracowujemy w Buildroocie oprogramowanie dla systemu wbudowanego, korzystającego z nieulotnej pamięci masowej, dla której nie jest dostępny (jeszcze?) sterownik dla systemu Linux. System jest wyposażony w firmowy bootloader (o zamkniętym kodzie źródłowym), będący w stanie załadować i uruchomić jądro Linuxa. Proszę opisać (uzasadniając), jak powinniśmy skonfigurować BR w takim przypadku
W takiej sytuacji można skonfigurować buildroot, żeby korzystał z ramdysku startowego (initramfs). Wtedy przy starcie systemu, system plików jest ładowany do pamięci i nie korzysta później z dysku.

## Oprogramowanie dla systemu wbudowanego, tworzone za pomocą środowiska Buildroot, jest testowane za pomocą emulatora QEMU. Zależy nam na tym żeby kolejne wersje naszej aplikacji, napisanej w języku C przetestować bez restartowania emulowanej maszyny. Jak możemy to zrealizować? Proszę podać trzy różne scenariusze przekazania nowej wersji aplikacji do emulowanego systemu. W jakim przypadku nie da się przetestować kolejnej wersji bez restartu tego systemu?
* Zamontowanie w emulowanej maszynie katalogu z systemu plików gospodarza korzystając z Plan 9
* Uruchomienie emulowanej maszyny z komunikacją sieciową z maszyną gospodarza i 
	* kopiowanie pliku programem `scp` (emulowana maszyna ma klienta SSH)
	* uruchomienie serwera HTTP na maszynie gospodarza i pobranie pliku przez `wget`
* Nie da się przetestować programu bez restartu systemu, jeśli kolejna wersja wprowadza nowe zależności, które nie są spełnione, trzeba zrekompilować Buildroot z tymi bibliotekami 

## Pakiet aplikacji w Buildroot używa publicznego repozytorium git do przechowywania kodu źródłowego. Chcemy wprowadzić modyfikacje, dostosowujące tę aplikację do naszych potrzeb. Jak możemy to przeprowadzić?
* Dodać pull request ze zmianami do repozytorium i poczekać aż zostanie zaakceptowany
* Wykorzystać mechanizm patchowania
* Dodać zmiany na oddzielnej gałęzi, podać w konfiguracji pakietu BR hash commita
* Zforkować repozytorium, tam wprowadzić zmiany i stworzyć własny pakiet Buildroota

## Proszę wymienić cztery wybrane powody, dla których standardowa dystrybucja Linuksa nie nadaje się do wykorzystania w przemysłowym systemie wbudowanym
* Standardowe dystrybucje są zależne od GUI, w systemie wbudowanym może nie być do niego dostępu
* Standardowe dystrybucje mogą mieć większe wymagania do pamięci i przestrzeni dyskowej niż są dostępne w systemie wbudowanym
* W standardowych dystrybucjach jest wiele procesów, które konkurują o czas procesora, uniemożliwiają spełnianie ograniczeń czasu rzeczywistego w systemie wbudowanym
* Mechanizm pamięci wirtualnej (plik lub partycja wymiany) jest zabójczy dla pamięci FLASH używanej w roli dysku w systemach wbudowanych

## Do zbudowanego w środowisku BR Linuksa działającego na przemysłowym systemie wbudowanym chcemy dodać naszą nową aplikację napisaną w języku C. Czym będzie się to różnić od uruchomienia tej aplikacji na naszym PC?
* Systemy wbudowane typowo korzystają z procesorów o innych architekturach zestawu instrukcji i PC
* Żeby uruchomić aplikację na innej platformie trzeba użyć odpowiedniego dla platformy kompilatora skrośnego (skorzystać z odpowiedniego SDK)
* Dodatkowo mogą pojawić się problemy jeśli program wykorzystuje zewnętrzne biblioteki
	* muszą być dostępne w systemie na etapie kompilacji
* Trzeba przenieść skompilowany program na system (np. przez sieć) albo dodać go na etapie kompilacji systemu

## Jakiej funkcji niedostępnej z poziomu powłoki systemu wymaga pełna obsługa urządzeń podłączonych do interfejsów I2C i SPI? Proszę wymienić przynajmniej trzy działania (łącznie dla I2C i SPI) do których konieczne jest użycie tej funkcji
* Do pełnej obsługi potrzebna jest operacja jednoczesnego odczytu i zapisu, realizowana przez funkcję `ioctl`
	* ustalenie adresu urządzenia slave w I2C
	* zlecenie złożonej sekwencji zapisów i odczytów w I2C
	* wymiana komunikatu miedzy urządzeniami slave i master w SPI

## Dlaczego projekt OpenWRT może udostępniać prekompilowane obrazy Linuksa dla typowych platform sprzętowych, a w przypadku środowiska Buildroot nie jest to stosowane?
Ponieważ na OpenWRT można instalować dodatkowe pakiety w trakcie działania systemu, a w Buildroot nie jest to możliwe. Nie byłoby praktyczne przygotowywać środowiska Buildroot dla każdej permutacji platformy i zestawu pakietów. Na OpenWRT można skorzystać z prekompilowanego obrazu i doinstalować potrzebne pakiety. 

## Proszę podać cztery wybrane powody, dla których może być przydatne testowanie w emulatorze QEMU systemu Linux, przygotowywanego dla systemu wbudowanego
* Uruchomienie maszyny wirtualnej jest szybsze niż każdorazowe nagrywanie obrazu systemu na nośnik i uruchamianie go na właściwej płytce
* Można wykorzystać własne emulowane urządzenia peryferyjne
* Nie wymaga fizycznego dostępu do płytki
* Można przetestować zachowanie systemu przy różnych ograniczeniach na zasoby sprzętowe (np. pamięć) bez fizycznego ingerowania w sprzęt

## Po zbudowaniu w środowisku Buildroot Linuksa dla naszego systemu wbudowanego, okazało się, że nie jest w nim dostępny sterownik dla używanej w nim kamery USB (mimo że jest dostępny w źródłach jądra). Proszę opisać szczegółowo w punktach jak rozwiążecie ten problem (uwzględniając dodatkowe problemy związane ze specyfiką BR)
* Upewnić się, że odpowiednia opcja jest wybrana w konfiguracji `make menuconfig` lub `make linux-menuconfig`
	* skorzystać z wyszukiwania `/`, ponieważ przy niespełnionych zależnościach opcja może nie być widoczna w menu
* Wykonać pełną rekompilację systemu przez `make clean all`
	* mamy pewność, że zależności między pakietami zostaną uwzględnione na etapie kompilacji

## Stworzyliśmy specjalizowaną aplikację do przetwarzania danych, napisaną w języku C, którą pomyślnie przetestowaliśmy w systemie Linux na komputerze PC (z procesorem Intel lub AMD). Co musimy zrobić, aby móc jej używać w systemie Linux zbudowanym przy pomocy środowiska Buildroot pracującym na systemie wbudowanym z procesorem ARM?
* Skorzystać z kompilatora skrośnego dla używanej platformy wbudowanej (z SDK Buildroota)
* Zapewnić, że w Buildroot są spełnione zależności naszej aplikacji
* Przetestować działanie aplikacji zbudowanej przez SDK np. korzystając z emulatora QEMU
* Wgrać program na system wbudowany (np. przez sieć)

## Oprogramowanie dla systemów wbudowanych czasami realizujemy bez stosowania systemu operacyjnego (podejście "bare metal"), a czasami z wykorzystaniem takiego systemu (na przykład Linuxa). Wybór właściwego rozwiązania zależy od wymagań realizowanego projektu. Proszę podać dwa przykłady wymagań preferujących podejście "bare metal" i dwa przykłady wymagań skłaniających do wykorzystania systemu operacyjnego
* Przesłanki za *bare metal*
	* bardzo restrykcyjne ograniczenia na pamięć, dysk, pobór mocy wybranje platformy sprzętowej
	* prostota systemu - nie wymaga użycia systemu operacyjnego do zrealizowania wymagań
* Przesłanki za systemem operacyjnym
	* wykorzystanie złożonych mechanizmów komunikacji, które są standardowo zaimplementowane w systemie operacyjnym
	* konieczność zrealizowania logiki, która została już zaimplementowana w dostępnych bibliotekach
	* wykorzystane podzespoły mogą ulec zmianie i chcemy się od nich uniezależnić

## Proszę wyjaśnić znaczenie skrótów GPIO, SPI, I2C i PWM oraz proszę krótko opisać funkcję związanych z nimi elementów systemu wbudowanego
* GPIO - General Purpose Input Output
	* generyczna obsługa pinów wejścia / wyjścia
* SPI - Serial Peripheral Interface
	* komunikacja z wieloma urządzeniami wejścia/wyjścia przez magistralę
* I2C - Inter-Integrated Circuit
	* komunikacja z wieloma urządzeniami wejścia/wyjścia przez magistralę
* PWM - Pulse Width Modulation
	* emulowanie sygnału analogowego przez sygnał cyfrowy
	* tańsza alternatywa dla stosowania przetwornika cyfrowo-analogowego

## Jaka jest relacja między systemem wbudowanym a systemem czasu rzeczywistego?
System czasu rzeczywistego - system, w którym obliczenia prowadzone równolegle z przebiegiem zewnętrznego procesu mają na celu nadzorowanie, sterowanie lub terminowe reagowanie na zachodzące w tym procesie zdarzenia.

System wbudowany - system komputerowy będący częścią większego systemu i wykonujący istotną część jego funkcji (np. komputer pokładowy samolotu, system sterujący koleją miejską)

## Co to jest i jaką rolę pełni sprzęg procesowy
Część sprzętu w systemie wbudowanym, odpowiedzialna za zamianę sygnałów logicznych na odpowiednie dla sterowanego układu, np. kiedy mikrokontroler steruje urządzeniem, które pracuje przy większym prądzie i napięciu.

## Proszę omówić sposób realizacji odczytów z przetworników AC
* Procesor przez zapis odpowiedniego bitu do rejestru zaczyna próbkowanie przez przetwornik AC
* Po wykonaniu pomiaru, przetwornik zapisuje wartość po kwantyzacji do rejestru wynikowego
* Przetwornik sygnalizuje gotowość przez zapis odpowiedniego bitu w rejestrze

## Dlaczego w środowsiku Buildroot do rekompilacji poprawnego obrazu systemu czasami wystarczy wydać polecenie make, a czasami konieczne jest posłużenie się kombinacją poleceń "make clean; make" (lub, co równoważne, poleceniem "make clean all"). Proszę podać przykład sytuacji , w której na pewno wystarczy samo "make" oraz takiej, w której potrzebne będzie "make clean all"
Program `make` określa, które moduły należy skompilować na podstawie znaczników czasowych, kompiluje tylko potrzebne moduły. W środowisku Buildroot zmiana konfiguracji jednego modułu może wpłynąć na sposób kompilacji innego modułu, jednak nie zostaje to uwzględnione przez `make`. W takiej sytuacji należy wykonać `make clean all` czyli usunąć wyniki wcześniejszej kompilacji i skompilować wszystko od nowa.

Samo `make` wystarczy np. przy dodaniu nowego modułu, od którego nie zależy żaden inny.

`make clean all` jest potrzebne jeśli zmiana konfiguracji modułu A wymaga ponownej kompilacji modułu B (który został skompilowany wcześniej).

## Do naszego systemu wbudowanego chcemy podłączyć urządzenie zewnętrzne z interfejsem I2C. Program je obsługujący ma działać w przestrzeni użytkownika. Jak powinniśmy skonfigurować nasz system, aby było to możliwe? Jakie funkcje musimy wykorzystać w naszym programie, aby zapewnić komunikację z naszym urządzeniem?
System powinien mieć sterownik dla interfejsu I2C (lub do GPIO, który umożliwi obsługę I2C). Wtedy program przestrzeni użytkownika obsługuje urządzenie korzystając z generycznego sterownika. Do pełnej obsługi interfejsu potrzebna jest funkcja `ioctl` umożliwiająca jeddnoczesny odczyt i zapis.

## Jakie właściwości ma interfejs GPIO w systemie wbudowanym? Proszę wymienić dwa typowe sposoby obsługi tego interfejsu. Proszę szczegółowo opisać jeden z tych sposobów.
* Pin GPIO można skonfigurować jako wejście albo wyjście ogólnego przeznaczenia
* Można je obsłużyć przez sysfs lub bibliotekę libgpiod
* Obsługa przez sysfs
	* `echo 25 > /sys/class/gpio/export` - przejęcie pinu GPIO 25
	* `echo 25 > /sys/class/gpio/unexport` - zwolnienie pinu GPIO 25
	* `echo in > /sys/class/gpio/gpio25/direction` - ustawienie pinu 25 jako wejście
	* `echo 1 > /sys/class/gpio/gpio25/value` - ustawienie stanu wysokiego na pinie wyjściowym 25
	* `cat /sys/class/gpio/gpio25/value` - odczyt wartości na pinie wejściowym 25

## Scharakteryzuj systemy czasu rzeczywistego. Opisz czym różni się od pozostałych systemów
System czasu rzeczywistego różni się od zwykłych systemów komputerowych tym, że musi reagować na sygnały z otoczenia w ściśle określonym, gwarantowanym czasie, co jest kluczowe dla zapewnienia prawidłowego działania w krytycznych aplikacjach. Charakteryzuje się:

- dotkliwymi konsekwencjami awarii
- integralnym połączeniem z instalacją
- terminowością działania - musi działać na czas 
- bezobsługowością
- wymaganiami sprzętowymi np. wysoka wydajność

## Opisz krótko realizację sprzętową systemów wbudowanych
* Realizacja przekaźnikowa
	* wykorzystuje przekaźniki - elektromagnes zwiera / rozwiera połączenia
	* zapewnia izolację galwaniczną i odpornośc na zakłócenia
	* duży rozmiar, koszt, zyżycie energii
	* ograniczone funkcje
	* trudne do modyfikacji
	* mała szybkość i trwałość
	* stosowane w elementach wykonawczych i układach zabezpieczeń
* Realizacja układowa
	* układ cyfrowy FPGA / ASIC realizujący logikę systemu (bramki, przerzutniki)
	* sprzęg procesowy zapewnia odpowiednią konwersję sygnałów logicznych (napięć itd)
	* duża szybkość, trwałość
	* mały pobór energii, rozmiar, koszt produkcjji
	* drogie do opracowania
	* trudna modyfikacja
	* stosowane w sterownikach urządzeń
* Realizacja programowa
	* logikę systemu realizuje mikrokontroler
	* sprzęg procesowy zapewnia odpowiednią konwersję sygnałów logicznych
	* elastyczna i modyfikowalna
	* duża trwałość
	* mały pobór energii, rozmiar, koszt produkcji
	* umiarkowana szybkość
	* stosowane w dużych i rozproszonych systemach, w unikalnych rozwiązaniach
* System jednoukładowy
	* procesor, pamięć, IO i specjalizowane układy na jednej płytce
	* wielka niezawodność
	* prosty montaż
	* mały pobór energii, rozmiar, koszt produkcji
	* wysoki koszt opracowania
	* stosowane w sterownikach dużej wydajności i produkcji wielkoseryjnej

## Po co w systemach wbudowanych stosuje się przerwania i jak one zachodzą
Stosuje się do asynchronicznej obsługi zdarzeń, które wymagają natychmiastowej reakcji procesora poza pętlą sterowania (np. obsługa wejścia/wyjścia)

Programowa obsługa przerwania wymaga zarejestrowania procedury obsługi przerwania w kontrolerze przerwań. Kiedy zostanie zgłoszone przerwanie, wykonywane zadanie zostaje zatrzymane, sterowanie jest przekazane do procedury obsługi przerwania, po zakończeniu procedury zadanie jest kontynuowane.

## Co to jest initramfs, jakie ma funkcjonalności i jak można go wykorzystać w systemach wbudowanych
* System plików w pamięci, ładowany przy starcie systemu
* Pozwala korzystać z systemu plików niezależnie od pamięci masowej
* Nie zachowuje zmian po restarcie systemu
* Można np. załadować go z karty SD a następnie dowolnie modyfikować jej zawartość


## Do pinu 23 GPIO podpięta jest dioda Led, do pinu 21 GPIO podpięty jest przycisk. W jaki sposób używając sysfs można przetestować połączenia
```
echo 23 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio23/direction
echo 1 > /sys/class/gpio/gpio23/value # Sprawdzenie czy zapala się dioda LED
echo 0 > /sys/class/gpio/gpio23/value # Sprawdzenie czy gaśnie dioda LED
echo 23 > /sys/class/gpio/unexport

echo 21 > /sys/class/gpio/export
echo in > /sys/class/gpio/gpio21/direction
cat /sys/class/gpio/gpio21/value # Przy nacisnietym przycisku
cat /sys/class/gpio/gpio21/value # Przy zwolnionym przycisku
echo 21 > /sys/class/gpio/unexport
```


## Opisz wady i zalety korzystania z pakietów instalowalnych. Podaj jeden przykład środowiska do konfiguracji linuxa dla systemów wbudowanych obsługujących takie pakiety i jeden który nie obsługuje
* OpenWRT obsługuje takie pakiety
* Buildroot ich nie obsługuje
* Zalety
	* można zainstalować je podczas pracy systemu
	* nie wymagają rekompilowania całego systemu
	* wygoda, elastyczność
* Wady
	* zajmują więcej przestrzeni dyskowej
	* nie mogą być aż tak zoptymalizowane jak w przypadku pakietów wkompilowanych w obraz systemu

## Linux jako system operacyjny dla systemu wbudowanego
* Jest w dużym stopniu zgodny ze standardem POSIX
* Może być dostosowywany do konkretnych potrzeb ze względu na otwarty kod źródłowy

## Organizacja oprogramowania systemów wbudowanych
* Dla twardych ograniczeń czasu rzeczywistego bierze się pod uwagę najdłuższy czas wykonywania zadań
* Cykliczne odpytywanie urządzeń nie gwarantuje realizacji dowolnego systemu
* Uwzględnia się cykl wykonywania zadań

## Ograniczenia czsowe w systemach czasu rzeczywistego
* Ostre (hard real-time)
    * każde przekroczenie ograniczeń może prowadzić do katastrofalnego błędu systemu
    * projektowanie na najgorszy przypadek
* Łagodne (soft real-time)
    * przekroczenie ograniczeń stopniowo degraduje jakość systemu ale nie niszczy zupełnie
    * projektowanie na wartości przeciętne
    * np. sterowanie grzejnikiem w pomieszczeniu
* Sztywne (firm real-time)
    * pojedyncze przekroczenia ograniczeń mogą być tolerowane
    * liczne przekroczenia pogarszają jakość systemu
    * np. przesyłanie dźwięku, obrazu