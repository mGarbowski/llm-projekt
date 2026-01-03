# Wprowadzenie cd (2024-02-26)

## Możliwości QEMU
* Dobre narzędzie to testowania
* Open source
* Emuluje systemy wbudowane
* Mozna badać zachowania systemu przy różnych ograniczeniach (pamięć, dysk)
* Można testować z rzeczywistymi urządzeniami (forwarding)
* Można testować z wirtualnymi urządzeniami (tworzone przez użytkownika)
* Można emolować kartę sieciową
* Można emulować kartę dźwiękową

Zawartość ramdysku startowego resetuje się po uruchomieniu bo jest wkompilowana w kernel
więc po załadowaniu systemu znajduje się tylko w pamięci.

Wyłączenie QEMU przez CTRL+A X może mieć niespodziewane rezultaty (emuluje odcięcie zasilania).
Zawartości cache mogą nie zostać utrwalone

Normalne wyłączenie komendą `poweroff`

tmux i screen pozwalają uruchomić wiele programów w jednej konsoli nie tracąc dostępu do ich
standardowych wejść i wyjść

w buildroot menuconfig jest wyszukiwarka pod `/` (wybiera się po wyświetlonym obok numerze)

Po zmianach w buildroot trzeba rekompilować
Jak zmienia się zależności bibliotek to może nie wystarczyć kompilowanie przez `make`

Można ręcznie zrekompilować daną bibliotekę `make ncurses-dirclean all`

`make clean all` robi pełną kompilację na czysto (dłuuuugie)


Można skonfigurować QEMU tak, żeby VM miała dostęp do katalogu z systemu plików gospodarza
przez system plików 9P

Konfiguracja kernela jest czyszczona przez `make clean`, `make linux-update-defconfig` zmienia domyślną
konfigurację kernela i to rozwiązuje

konfigurację można skopiować poza buildroota i wybrać ścieżkę pliku z konfiguracją z menu

Żeby odtworzyć buildroota trzeba zachować konfigurację kernela i .config

`make linux-dirclean all` - rekompilacja samego kernela


## Dodanie pliku na system tworzony przez BR
nieelegancko można dodać coś do output/target i jeszcze raz wywołać `make` 
ale wtedy zostanie wyczyszczony przez `make clean`

do tego służą zewnętrzne katalogi z nakładkami
system configuration > root file system overlay directories
zawartość katalogu jest nakładana na system plików
nakładka nadpisuje oryginalną zawartość (można nadpisać konfiguracje)

dobra dla skryptu w pythonie (ale nie dla programu w C)

## Zachowanie stanu BR
bezpieczniej kopiować archiwa bo zachowają linki symboliczne i metadane plików


# Raspberry PI 
* ma moc solidnego komputera ale używany go jako systemu wbudowanego
* będziemy wgrywać linuxa zbudowanego przez buildroot
* komunikacja prez UART albo przez sieć


## BHP na laboratorium
* można usmażyć płytkę źle podłączonymi kablami
* podłączanie kabli przy odłączonym zasilaczu

Połączenie RX i TX na krzyż (odbiornik do nadajnika, nadajnik do odbiornika)

## budowanie Linuxa przez buildroot
* Predefiniowana konfiguracja dla raspberry pi
* Wynik w output/images
    * Image - jądro systemu
    * .dtb - drzewo urządzeń - opis zasobów sprzętowych komputera
    * rootfs - obraz głównego systemu plików
    * sdcard.img - obraz binarny zawartości karty SD

Obraz karty sd można wgrać na raspberry przez `dd`
`dd` należy używać **ostrożnie**

Build jest zoptymalizzowany, można powiększyć partycję i rozszerzyć system plików
`resize2fs`

Na labach nie wyjmujemy karty SD żeby oszczędzać gniazda

W systemach przemysłowych ładuje się bootloader przed właściwym systemem i jest
jakaś możliwość wybrania co będzie ładowane


## Obsługa GPIO
* sysfs
    * pisanie wartości do plików
    * korzystając z nich w programie, przed odczytem trzeba przewijać plik do początku
    * przez poll można uśpić proces do pojawienia się przerwania
    * jest uważany za przestarzały ale dalej szeroko wykorzystywany
* nowa metoda
    * biblioteka periphery


## Obsługa SPI
* jest link na prezentacji
* nie można przez read ani wrtie bo odpowiedź od urządzenia slave przychodzi od razu po odebraniu danych


PWM też można obsłużyć przez sysfs albo bibliotekę periphery
