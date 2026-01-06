# Zarządzanie zasobami komputera
Współczesne systemy są wieloużytkowe, wieloprocesowe i wielowątkowe

Procesy nie mogą wzajemnie wpływać na swoje wykonywanie, dane są izolowane, zakłócenie jesdnego nie zakłóca działania innego procesu ani systemu operacyjnego

## Ochrona zasobów

### Procesor
* proces nie może zmonopolizować czasu procesora (np. przy nieskończonej pętli)
* inne procesy muszą mieć możliwość wykonywania się
* cdn...

### Pamięć
* Proces ma dostęp tylko do przydzielonej mu pamięci (i ewentualnie do danych współdzielonych po uzgodnieniu z innym procesem)
* Proces nie może odwołać się do własnej pamięci w niewłaściwy sposób
  * zapis do stałych
  * zapis do kodu
  * wykonywanie danych jako kodu

## IO
* Urządzenia IO nie mogą sobie przeszkadzać nawzajem
* W praktyce całkowicie uniemożliwia się bezpośrednie odwołania do urządzeń - wszystkiemu pośredniczy system operacyjny

## Użytkownik i system
* Żeby zrealizować mechanizmy ochrony trzeba zróżnicować uprawnienia programów na poziomie sprzętu (conajmniej 2 poziomy)
* Proces użytkowy pracuje na poziomie użytkownika
* System operacyjny pracuje na poziomie systemowym
* Założenie - system operacyjny jest poprawny - nie zawiera błędów, nie wpadnie w nieskończoną pętle itp.
* Założenie - aplikacje nie są zaufane, mogą zawierać błędy a system operacyjny ma przed tym chronić

## Poziomy uprzywilejowania
Często wprowadza się trzec

* jądra systemu
* usług systemu
* użytkownika

Aktualny poziom uprzywilejowana jest przechowywany w procesorze w systemowym rejestrze stanu


## Egzekwowanie zasad ochrony
Naruszenie zasad ochrony jest wykrywane (sprzętowo), blokowane i zgłaszany jest wyjątek

Sprzętowo przełącza się wykonywanie z wadliwej aplikacji na procedury systemowe

## Ochrona czasu procesora
Wątki wykonują się naprzemiennie, wątek musi być możliwy do przerwania wbrew jego woli.

Timer systemowy zgłasza wyjątek co stały okres - system operacyjny przejmuje sterowanie

W szczególnych sytuacjach system może zezwolić na wyłączny dostęp pojedynczego procesu do urządzenia (np. DirectX)

## Ochrona pamięci
Poprawność musi być zapewniana przez mechanizmy sprzętowe - program wykonuje się cały czas


## Maszyny wirtualne
Jednoczesna praca kilku systemów operacyjynch na jednym komputerze

Wprowadza się kolejny poziom ochrony - hypervisor

dwa systemy operacyjne muszą być kontrolowane jak aplikacja i system

## Strefa zaufana
Zabezpieczenie przed instalacją podrobionego systemu operacyjnego - np. aktualizacje do urządzeń IoT

### Przestrzeń uprawnień
* użytkownik-system
* system-hypervisor
* strefa zaufana - strefa niezaufana

Przestrzeń uprwanień może być zrealizowana jednowymiarowo aplikacja, system, hypervisor, monitor strefy zaufanej

Może być trójwymiarowa - hypervisor/gość, aplikacja/system, zaufany/niezaufany

# Funkcje systemu zarządzani pamięcią
Wykuć na pamięć!!!!!

1. Sprzętowa relokacja - translacja adresów - ten sam adres w dwóch procesach wykonujących ten sam program z tymi samymi zahardkodowanymi zadaniami oznaczają inne fizyczne komórki pamięci i jest to zapewniane sprzętowo w sposób przezroczysty dla programu
2. Ochrona
3. Dynamiczna alokacja i dealokacja - powiększenie zmniejszenie rozmiaru przestrzeni adresowej w trakcie pracy
4. Wirtualizacja - uniezaleznienie rozmiaru pamięci dostępnej dla zadania od fizycznej konfiguracji komputera i aktualnego stopnia wykorzystania pamięci

## Realizacja zarządzania pamięcią
...

## Jednostka zarządzania pamięcią
MMU - Memory Management Unit

Układ pośredniczący między procesorem a pamięcią

* Adres logiczny (adres wirtualny) z procesora trafia na wejście MMU, MMU produkuje na wyjściu adres fizyczny komórki w pamięci
* Typ odwołania - odczyt instrukcjim odczyt danej, zapis danej, poziom uprzywilejowania
* Błąd

Schemat połączenia ...


## Algorytmy zarządzania pamięcią

### Prosta relokacja
* Przestrzeń adresowa jest jednym ciągłym blokiem
* System operacyjny operuje na adresach fizycznych

## Prosta relokacja
* rejestr datum
* rejestr limit
* generacja błędu przy przekroczeniu wartości limit
* Oddziela zadania od siebie
* Nie chroni zadania samego prze sobą
* Dynamiczna alokacja
  * jeśli dalej w pamięci jest pusto to wystarczy zwiększyć limit
  * jeśli obszar dalej jest zajęty trzeba przenieść segment pamięci tam gdzie jest wolne miejsce i zmodyfikować datum i limit
  * po dealokacji zostaje puste miejsce - po zakończeniu wiellu zadań pamięć ma wiele dziur, nie ma dużego wolnego fragmentu - fragmentacja pamięci
  * defragmentacja - przepisanie bloków zadań po kolei (zsunięcie) przez system operacyjny - na końcu pamięci zostaje duży ciągły obszar wolnej pamięci

## Segmentacja
* Uogólnienie prostej relokacji
* Sekcje kodu, static, sterta i stos są oddzielnie zarządzanymi segmentami
* Można zrobić więcej segmentów niż 4
  * rozdzielenie stałych
  * pocięcie sekcji TEXT
  * podział sterty na kawałki
  * stos musi być jednym segmentem!
* W każdym segmencie adresy są liczone od 0 - adres jest parą (identyfikator segmentu, adres wewnątrzsegmentowy)
  * na wyjściu jednostki segmentacji - adres liniowy
* Deskryptor segmentu
  * znacznik ważności (1 bit)
  * prawa dostępu do segmentu (poziom uprzywilejowania)
  * rozmiar segmentu
  * liniowy adres bazowy segmentu
  * trzymany w jednostce segmentacji albo w pamięci
  * informacje dla jednostki segmentacji
* Jednostka segmentacji wybiera deskryptor na podstawie identyfikatora segmentu
  * sprawdza ważność
  * sprawdza uprawnienia
  * sprawdza czy adres mieści się w zakresie
  * jeśli nie było błędu to adres wyjściowy = adres bazowy + adres wewnątrzsegmentowy
* Pojawiają się problemy z fragmentacją - rozszerzenie często wymaga relokacji
* Żeby efektywnie realizować wirtualizację musi być dużo segmentów
  * defragmentacja pamięci jest szybka
  * defragmentacja dysku jest bardzo wolna
* Generalnie źle działa ale jest używana w x86


## Stronicowanie
* Metoda wymyślona na potrzeby realizacji wirtualizacji
* Bloki o stałej długości 2^n (typowo 4KiB) wyrównane naturalnie - strony
* Strony fizyczne / ramki strony - przestrzeń fizyczna
* Strony / strony logiczne / strony wirtualne - przestrzeń logiczna
* Pamięć dla programu zawsze alokuje się w stronach
* Marnowanie pamięci na końcu ostatniej strony (fragmentacja wewnętrzna) - mały problem

### Jednostka stronicowania
* Przyporządkowuje strony logiczne do fizycznych
* Mniej znaczące bity adresu to adres wewnątrz strony
  * nie wymaga translacji bo jest wyrównanie naturalne
  * bardziej znaczące bity adresu są adresem strony logicznej
* Sprawdza prawa dostępu, ważność i ewentualnie zwraca błąd
* Jeśli nie ma błędu to zwraca adres fizyczny strony (bez operacji arytmetycznych!)

### Bufor translacji
* Różne nazwy
  * TLB (translation lookaside buffer)
  * TB (translation buffer)
  * ATC (address translation cache)
* Zrealizowany jako kieszeń pełnoasocjacyjna (albo o wysokiej asocjacyjności)
* Każdy element przechowuje
  * Virtual Page Number
  * deskryptor strony
    * znacznik wazności (1 bit)
    * znacznik praw dostępu do strony
    * fizyczny numer strony
    * dodatkowe bity atrybutów wykorzystywane przez OS


### Chybienie bufora translacji
* System operacyjny trzyma informacje w pamięci (sprzętowo) - podejście CISC
* Chybienie powoduje wyjątek, system musi załadować deskryptory do bufora - podejście RISC, mniej wydajne bo programowe
* Nie ładuje się nieważnych deskryptorów do bufora

## Pamięć wirtualna z użyciem stronicowania
* Współpraca dwóch warstw hierarchii pamięci
* Takie same rozwiązania jak dla kieszeni L1, L2, L3 można zastosować do styku pamięci operacyjnej z wirtualną
* Zbiór roboczy - zbiór stron
  * część w pamięci operacyjnej
  * część w pamięci masowej
* Algorytm wyznaczania ofiar - stron zrzucanych do pamięci wirtualnej
* Przerzucanie stron w obie strony
* Nie ma problemu fragmentacji przez stały rozmiar stron

## Problem ze stronicowaniem
* Typowo w systemach 32-bitowach przestrzeń adresowa była podzielona na przestrzeń dla użytkownika i dla systemu (po 2 GiB)
* Jednostka musi być gotowa z odpowiedzią na każdy dozwolony adres
* Przestrzeń adresowa jest wykorzystana w bardzo małym stopniu (dziura między stertą i stosem)
* Problem rzadkich (sparse) struktur danych
* Przechowywanie deskryptora dla każdej strony przestrzeni adresowej zajmuje 4MiB na każde zadanie - przesada
* Stosuje się rozwiązanie tablicowo-drzewiaste (tree of tables)
  * Dla 32-bitowego procesora 2 poziomy
  * wirtualny adres storny dzieli się na 2 indeksy
  * pierwszy indeksuje w tablicy głównej tablice podrzędną gdzie jest deskryptor albo jest pustym wskaźnikiem - błąd
  * każda tablica zajmuje jedną stronę

## Problem z dwupoziomowymi tablicami stron
* połowa przestrzeni adresowej każdego zadania jest przeznaczona na część systemową
* ta część - połowa tablic pierwszego rzędu w każdym zadaniu jest taka sam adla każdego zadania
* doalokowanie pamięci przez system przekraczające granicę 4KiB wymaga kolejnej strony i w każdym zadaniu trzeba odzwiercieglić te zmiany


## Trójpoziomowe tablice deskryptorów - tryb PAE
* tablica główna umożliwia oddzielenie poddrzewa systemowego od poddrzewa użytkownika
* 8-bajtowy deskryptor (x86 w trybie PAE)
* Wprowadzono rozróżnienie na odczyt danych i odczyt instrukcji (odporność na ataki buffer overflow) - flaga no-execute
* vpi dzielony na 3 pola - 2b, 9b, 9b
  * tablica 3. poziomu - 4 elementy
  * tablica 2 - poziomu - maksymalnie 4, 2 dla użytkownika, 2 dla systemu
    * dla systemu są tworzone tylko raz, sa modyfikowane ale nie zmieniają położenia, nie są tworzone/usuwane

## Stronicowanie w procesorze 64-bitowym
* Procesor 32-bitowy może wykorzystać mniej niż 4GiB pamięci - fizyczne zasoby komputera muszą być widoczne dla systemu w pamięci
* Zaczęto konstruować 64-bitowe procesory po to żeby wkładać więcej pamięci
* "nikt nigdy nie będzie potrzebował więcej niż 2^64" - może być uzasadnione (liczba avogadro i masa takiej pamięci)
* Realnie adresy są krótsze (np. 48b)
* w x86-64 program operuje na adresach od 0 do 2^47 i od (2^64-2^47) do 2^64
* Adres musi mieć na początku albo 17 zer albo 17 jedynek - adresy kanoniczne
* Deskryptory stron wykorzystują tylko 48b adresu
* Stosuje się 4-poziomowe tablice

## Chybienie bufora translacji
* Jednostka translacji przeszukuje tablice w poszukiwaniu deskryptora strony
* Traci się czas 4 pełnych dostępów do pamięci
* 1 chybienie to koszt rzędu czasu 400 instrukcji
* Chybienia zdarzają się bardzo rzadko ale powodują bardzo duże spowolnienie
* Chybienia można podizelić na 3 rodzaje
  * chybienia inicjalne - przed pierwszym wypełnieniem bufora - przy każdym przełączeniu zadania
    * przy przałączaniu zadania wystarczy wymienić deskryptory z dolnej połowy przestrzeni adresowej (użytkownika)
    * bit G (global) deskryptora - deskryptor nie jest wyrzucany z bufora translacji
    * deskryptorów użytkownika jest na ogół mniej
  * chybienia rozmiarowe - wynikające z zapełnienia bufora(konieczności wyrzucenia elementu)
    * jeśli nie potrzeba wirtualizacji
    * nie trzeba dzielić pamięci na małe strony
    * nie potrzeba tak wielu deskryptorów
    * mniejszy bufor translacji pomieści deskryptory
    * obszary które nie wymagają wymiany można przechowywać w dużych megastronach
    * wirtualizacji nie podlega jądro systemu, i niektóre inne kawałki systemu
    * zasoby fizyczne nie wymagają wirtualizacji - zajmują dużą część przestrzeni adresowej
    * w x64 tablica 2 lub 3 poziomu może bezpośredni opisywać obszar o rozmiarze 2MiB albo 1GiB
  * chybienia strukturalne - ...

## 5-poziomowe tablice deskryptorów