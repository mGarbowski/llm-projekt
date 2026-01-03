# RISC-V (2023-03-20)

* Otwarta architektura, nie chroniona patentem
* 32/64 bity, rozszerzalna do 128
* Zmodernizowana wersja MIPS

## Pojęcia
* ISA - Instruction Set Architecture
* ABI - Application Binary Interface
* hart - hardware thread - procesor logiczny
* EEI - Execution Environment Interface - model programowy komputera
  * ISA
  * pamięć
  * IO
  * parametry sprzętu


## Zestaw rejestrów
* stałe 0 - x0
* 31 rejestrów uniwersalnych (x1..x31)
* brak operacji stosowych
* x2 przewidziany jako wskaźnik stosu
* x1 przewidziany jako rejestr śladu
* opcjonalna jednostka zmiennopozycyjna - 32 rejestr f0..f31
* PC - program counter
* bezznacznikowy
* Przypisuje się alternatywne nazwy zgodne ze znaczeniem wg konwencji wołania

## Specyfikacje ISA
### Wersje specyfikacji podstawowej
* RV32I - podstawowa 32-bitowa, 31 rejestrów
* RV32E - uproszczona 32-bitowa, 15 rejestrów
* RV64I - 64-bitowa, 32 rejestry

### Rozszerzenia
* RVM - mnożenie i dzielenie stałopozycyjne
* RVA - prymitywy synchronizacyjne
* RVF - jednostka zmiennopozycyjna 32-bitowa
* RVD - jednostka zmiennopozycyjna 64-bitowa
* RVC - alternatywny zapis binarny instrukcji (skompresowane, 2 możliwe długości)

### Nowe rzeczy
* Hart - wątek sprzętowy
* rejestr bazy statycznej wątku
* Position-Independent Code
  * możliwość nieużywania adresów absolutnych
  * wszystkie adresy skoku są względne
  * możliwość relokacji kodu

PIC umożliwia ładowanie plików wykonywalnych od razu do pamięci bez modyfikacji


## Dane
* 8-bitowe - byte
* 16-bitowe - halfword
* 32-bitowe - word
* 64-bitowe - doubleword
* 128-bitowe - quadword

Dane mogą być interpretowane jako
* wartość boolowska
* liczba całkowita bez znaku
* liczba całkowita ze znakiem
* liczba zmiennopozycjyna

Dane są wyrównane naturalnie w pamięci, przy rozszerzeniu RVC wyrównanie jest do 16 bitów

Konkretne bity w instrukcji mają zazwyczaj to samo znaczenie - ułatwienie realizacji sprzętowej

Różne formaty instrukcji różnie rozmieszczają stałe


## Formaty instrukcji
* R (register) - 2 rejestry źródłowe i docelowy
* I (immediate) - rejestr źródłowy, docelowy i stała
* S (store) - rejestr bazowy, przemieszczenie, źródło
* B (branch) - skoki warunkowe, inne rozmieszczenie stałych względem S
  * bit 0 nie jest zapisywany, bo wszystkie adresy są parzyste ze względu na wyrównanie
* U (upper immediate) - kawałek stałej 32-bitowej do ładowania długich wartości natychmiastowych
* J (jump) - dla skoków z długim zasięgiem


## RV32I
* 40 instrukcji
* niektóre instrukcje używają aktualnego PC a niektóre zinkrementowanego

### Grupy instrukcji
* wymiana z pamięcią
* arytmetyczne i logiczne
* przesunięcia bitowe
  * SLL logiczne w lewo (to samo co arytmetyczne) - mnożenie przez 2^n
  * SRL logiczne w prawo - dzielenie NKB przez 2^n
  * SRA arytmetyczne w prawo - dzielenie U2 przez 2^n
* przekazywanie sterowania
  * `jal` - skok ze śladem
  * `jalr` - skok ze śladem, adres docelowy w rejestrze
  * `beq`
  * `bne`
  * `blt`
  * `bltu`
  * `bge`
  * `bgeu`
* interakcja z systemem operacyjnym
  * `ecall` - wywołanie systemu
  * `ebreak` - pułapka debuggowania
* RVM
  * mnożenie, mniej znacząca połowa wyniku
  * mnożenie, bardziej znacząca połowa wyniku
  * dzielenie
  * reszta z dzielenia

Assembler RISC-V udostępnia rozszerzony zestaw mnemoników - pseudoinstrukcje, przyjaźniejsze dla szłowieka

Deklaracje danych przez dyrektywy assemblera

`.data` - otwarcie sekcji danych
`.text` - otwarcie sekcji instrukcji
`.space` - alokacja pamięci bez inicjalizowania


## Wołanie usług systemowych
wpis do odpowiednich rejestrów

zawsze trzeba wywołać `Exit`

100 bajtowy bufor mieści realnie 98 znakow (`LF` i `NUL`)


## Praca domowa
* Przejrzeć dodatek A do starego wydania Patterson-Hennessy
* Dokument wprowadzenie do zajęć laboratoryjnych - przykładowe zadania


## Zapis kodu assemblerowego
* wierszowy, graficznie podzielony na kolumny
* etykieta
  * instrukcja
    * argumenty
      * komentarze

Etykieta to symboliczna nazwa odpowiadająca adresowi (danej lub instrukcji).

Etykieta jset widoczna w całym pliku źródłowym

Niektóre asemblery wspierają etykiety lokalne