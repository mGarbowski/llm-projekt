# Połączenia modemowe (2023-05-16)

## Komunikacja przez port szeregowy
* Null modem - kabel szeregowy ze skrzyżowanymi przewodami (żeby łączyć nadajnik z odbiornikiem)
* Emulator terminala - umożliwia pracsę zdalną 
* Prymitywna komunikacja - przesyłanie znaków z klawiatury do drugiego komputera

## Sieć telefoniczna
* Wyjorzystano istniejącą sieć telefoniczną do transmisji cyfrowych
* przystosowana do przesyłania ludzkiej mowy
* Częstotliwości dla pojedynczego pasma
  * od 200Hz - eliminuje zakłócenia od sieci energetycznej (50Hz)
  * do 4kHz - maksymalne potrzebne do odwzorowania ludzkiej mowy dla większości ludzi
* Multipleksacja częstotliwościowa
  * jednym kablem można przesyłać na raz kilka transmisji jako sygnały z różnych przedziałów częstotliwości
  * moduluje się sygnał tak, żeby przesunąć go w dziedzinie częstotliwości
  * żeby zmieścić jak najwięcej transmisji na jednym kablu trzeba maksymalnie zawęzić pasmo dla pojedynczej transmisji
* Do transmisji cyfrowych trzeba stosować modulację
  * w jednym paśmie wyróżnia się 4 częstotliwości
  * po 2 (logiczne 0 i logiczne 1) dla transmisji w obie strony
  * osiągano w ten sposób transmisję cyfrową o szybkości rzędu 1kbps
  * praktyczne maskimum dla połączeń analogowych 33,6kbps
* Modem - modulator-demodulator
* DTE
* DCE - digital circuit termination equipment

### Homologacja
Certyfikat wystawiony urządzeniu przez odpowiedni urząd dla terytorium, który poświadcza że urządzenie nie będzie zakłócało transmijsi (korzystało z niedozwolonych częstotliwości)


### Sprzężenie akustyczne
Kładzie się słuchawkę telefonu na mikrofonie i głośniku - hack do obejścia regulacji telekomów

## Przejście sieci telefonicznej na transmisje cyfrową
* Połączenia między centralami zmieniono na cyfrowe
* Na stykach central z aparatami telefonicznymi trzeba było stosować przetworniki analogowo cyfrowe
* Odcinki analogowe sieci telekomunikacyjnej skróciły się tylko do połączenia telefon-centrala
* Dzięki temu da się osiągnąć szybkość transmisji cyfrowej 56kbps przez modemy
* Transmisja między centralami jest z szybkością 64kbps


## ISDN
* Połączenie cyfrowe do centarli (telefonu albo modemu)
* Pełne 64 kbps

## ADSL
Asymmetric Digital Subscriber Line

* Neostrada
* Przesyłanie danych przez linie abonenckie
* Pasma częstotliwości
  * transmisje akustyczne - 33.6kbps
  * upload - 1Mbps
  * download - 8Mbps


## Transmisja asynchroniczna po porcie szeregowym
* bit startu
* 7-8 bitów danych
* 0-1 bit parzystości
* 1-2 bity stopu
* Sekwencja +++ zrywa połączenie modemowe, system operacyjny wstawia odstępy czasowe kiedy sekwencja pojawia się w przesyłanych danych

## PPP
Point-to-Point Protocol

* Umożliwia enkapsulację np. protokołu IP dla transmisji po linii modemowej
* Połączenia modemowe są bardziej zawodne, lepiej stosować mniejsze MTU - mniejsze prawdopodobieństwo uszkodzenia ramki

## Generacje telefonii mobilnej
* 1G
* 2G
* 3G
* 4G
* 5G

## Światłowody
* obecnie stosowane, najszybsze
* Stosowane od lat 80 na kolei i w energetyce do przesyłania sygnałów sterujących