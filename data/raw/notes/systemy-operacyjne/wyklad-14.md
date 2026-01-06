# Wykład 14 (2024-01-23)

Warstwy
* procesy użytkownika
* oprogramowanie niezależne od urządzenia
* sterowniki urządzeń
* procedury obsługi przerwań
* sprzęt

Jest urządzenie od producenta z dokumentacją (pod jakie porty się mapuje, jaki protokół komunikacji)
Trzeba to zaimplementować w jądrze
Jest wywoływane przez wywołania systemowe
Muszą być jakieś identyfikatory wskazujące na konkretne urządzenie
w unixie to para liczb major i minor
Major to numer sterownika
Minor to numer danego urządzenia w ramach jego sterownika
Np dyski mają wspólny major i każdy ma własny minor

### Używanie sterowników
w unixie mknod tworzy pozycję katalogową dla pliku specjalnego, przyjmuje nazwę, typ (block/character) i parę major, minor
Nazwa jest dla człowieka, istotne są typ, major i minor

np można zmienić pozycję /dev/null tak żeby logować wszystko co miało być ukryte

Zazwyczaj w katalogu /dev - urządzenia zarejestrowane w systemie plików
wtedy można wykorzystać mechanizm otwierania plików żeby dostać się do urządzenia
open, close, seek, read, write - te same wywołania co dla zwykłych plików - to znaczy unifikacja
seek ustawia bieżącą pozycję (adres) w obrębie urządzenia

zawartość funkcji read, write dla konkretnego urządzenia to "górne połówki"

major to indeks sterownika w tablicy sterowników (np. sterownik do obsługi dysków)
sterownik to struktura danych zgodna z dokumentacją danego systemu operacyjnego, zawiera procedury obsługi open, read, write, seek, close (te które mają sens dla urządzenia, nie czyta się z drukarki znakowej)
taką strukturę rejestruje się w jądrze jako sterownik

w linuxie jest koncepcja modułów ładowanych dynamicznie, można ładować sterownik niezależnie od reszty jądra 
przygotowuje się sterownik zgodnie z konwencją, kompiluje się i ładuje nowy moduł

tak się też dostarcza sterowniki o zamkniętych źródłach

Na egzamin
pytanie typu na czym polega tworzenia sterownika
* obsługa wywyołań
* major minor
* pozycja katalogowa

Kurz szkodzi elektronice bo blokuje odprowadzanie ciepła

## RAID
* redundancja
* większa niezawodność dysków
* kody detekcyjno-korekcyjne

Poziomy RAID są od 0 do 6 (10 to 1+0, marketing)

### RAID 0
* bez powielenia danych
* wiele dysków tworzy jeden logiczny dysk
* adresy mogą iść albo wzdłuż albo w poprzek (konkatenacja albo striping)
* striping
	* jest bardziej skomplikowany do zarządzania
	* można robić równoległe odczyty i przyspieszyć dostęp
	* ma sens dla dysków o jednakowej pojemności
* nie ma redundancji
	* jak padnie jeden dysk to pada wszystko

### RAID 1
* Jak RAID 0 ale z lustrzaną kopią
	* może być więcej niż 1 kopia
* Najlepsza niezawodność
* Drogie, bo trzeba mieć przynajmniej drugie tyle dysków
* Ze względu na koszt ogranicza się użycie do krytycznych obszarów
	* bootowanie
* Lepsze są małe mirrory, duże concaty

Żeby zrobić backup można 
* dynamicznie dołączyć 3 kopię
* uaktualnić 3. element
* powstaje spójna kopia
* można odłączyć i przenieść na inny nośnik

### RAID 2
* już się nie stosuje
* kody detekcyjno-korekcyjne (Hamminga)
	* tylko ograniczoną liczbę można naprawić
* piekielnie niewydajne i drogie

### RAID 3
* oddzielny dysk na bity parzystości
* analogiczny do RAID 2
* mała przepustowość zapytań
* bardziej wydajne niż RAID 2
* nie stosuje się już

### RAID 4
* Niezależny dostęp do poszczególnych dysków
* Zwielokrotnienie na poziomie sektorów

### RAID 5
* Wykorzystywany współcześnie
* redundancja kosztuje jeden dysk
* parzystość rozsiana między wieloma dyskami
* pasek można odtwrozyć na podstawie nadmiarowego bloku
* ekonomiczne
* dla kilku dysków, nie dla kilkudziesięciu
* nieelastyczny
	* ciężko rozszerzyć macierz o jeden dysk ze względu na paskowanie
	* ale łatwo podmienić dysk

## Praktyka
* dysk do bootowania w RAID 1
* macierz dyskowa podłączona sieciowo (sieć typu SAN)
	* z RAID 5
	* kilka dysków poza RAID 5 w trybie standby
	* nadmiarowe dyski zostaną automatycznie podmienione w razie awarii jednego z dysków macierzy

Parzystość - trzeba rozumieć
* operacja XOR
* przemienna
* pozwala odtworzyć zawartość zepsutego dysku


### RAID 6
* Parzystość jest wyliczana 2 razy , trzymana w 2 miejscach
* Nie jest odporne na awarię 2 dysków na raz
* Po awarii jednego dysku działa jak RAID 5 dopóki nie zostanie naprawiony
	* jak dysk padnie w piątek wieczorem to macierz dalej będzie działać
	* "last hope of administrator"


Na linuxie można założyć partycję typu RAID - to bardziej udawanie że się zabezpiecza dane

RAID z kontrolerem sprzętowym jest niewidoczne dla systemu operacyjnego (konfiguruje się macierz dyskową przez BIOS/UEFI)

W centrum danych to typowo
* RAID 1 dla krytycznych danych (system operacyjny)
* RAID 5 dla dużych danych produkcyjnych
	* z nadmiarowymi dyskami standby
	* gwarantowane że można w trakcie działania macierzy wyciągnąć dysk i podpiąć nowy
	* obsługa centrum danych to przede wszystkim wymienianie twardych dysków, często, w dużej liczbie


## Egzamin
* taka forma jak kolokwium, wyświetlane pytania
* 40 pkt
* będzie podany zakres
* każdy ma obowiązek przyjść na egzamin
* do 80 minut
* chyba będzie zwalniał ale nie można wykluczyć że nie zwolni