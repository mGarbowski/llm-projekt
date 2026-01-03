# Przykładowe kolokwium 01


## System binarny, endianness, kodowanie
### 8 bitów
* oktet
* najczęściej bajt ale niekoniecznie
* bajt jeśli jest to najmniejsza adresowalna porcja informacji w danej architekturze


### 4 bity
* tetrada
* nibble


### Jeśli 2745 jest liczbą w pewnym systemie pozycyjno-wagowym, to może to być system
* dziewiątkowy
* heksadecymalny
* ~~siódemlowy~~

Podstawa systemu musi być większa conajmniej o 1 od największej cyfry


### 500 bajtów to
* zazwyczaj 8*500 bitówa (nie zawsze!)
* 0.5kB (k -> 1000)
* ~~0.5KiB~~ (Ki -> 1024)


### Zakładając, że 0x7D4ABACC to 32 bitowa liczba w kodzie U2 i jest ona przechowywana pod adresem 0x100A

Big endian - najbardziej znaczący bajt pod najmniejszym adresem

|       | 1      | 2      | 3      | 4      |
| ----- | ------ | ------ | ------ | ------ |
| bajt  | 7D     | 4A     | BA     | CC     |
| adres | 0x100A | 0x100B | 0x100C | 0x100D |


Little Endian - najmniej znaczący bajt pod najmniejszym adresem

|       | 1      | 2      | 3      | 4      |
| ----- | ------ | ------ | ------ | ------ |
| bajt  | CC     | BA     | 4A     | 7D     |
| adres | 0x100A | 0x100B | 0x100C | 0x100D |


### Liczba -121 w kodowaniu U2
|                       |            |
| --------------------- | ---------- |
| 121 w NKB             | 0111 1001  |
| Negacja bitów         | 1000 0110  |
| -121 w U2 (dodanie 1) | 1000 0111  |
| binanie               | 0b10000111 |
| oktalnie              | 0o207      |
| heksadecymalnie       | 0x87       |

Przy zapisie oktalnym nie rozszerza się pierwszej jedynki (0o207 a nie 0o607) mimo że liczba jest ujemna, chodiz tylko o zakodowanie bitów


### Zamiana oktetu na postać heksadecymalną
* Należy potraktować cyfry jak liczbę w kodzie NKB niezależnie od tego jaką informację i w jakim kodowaniu przedstawiają oktety.
* Niezależnie zamienić każdy nibble na cyfrę heksadecymalną.
* Wykorzystujemy niezależnie kodowanie górnej i dolnej tetrady oktetu


## Architektura, ALU, klasyfikacja Flynna
### Flaga przepełnienia w rejestrze stanu
Sygnalizuje, że wynik ostatniej operacji wykonanej prez ALU nie mieści się w natywnym słowie procesora

### Instrukcja MMX
Realizuje operacje arytmetyczne jednocześnie na całym wektorze liczb.

Jest przykładem architektury SIMD


### ALU
* wykonuje takie operacje jak
  * dodawanie
  * negacje
  * przesunięcie logiczne
  * przesunięcie arytmetyczne
  * rotacja (przesunięcie cykliczne?)
* Arithmetic Logic Unit
* Układ kombinacyjny asynchroniczny realizujący funkcje logiczne


## Pamięć, rejestry
### Pamięć ulotna
Traci przechowywane informacji po utracie zasilania

Na przykład
* DRAM
* SRAM


### Uporządkowane malejąco wg. typowych pojemności
* pamięć stała - dysk HDD
* pamięć stała - dysk SSD
* pamięć operacyjna RAM
* pamięć cache L2
* pamięć cache L1
* rejestry procesora

### Uporządkowane malejąco wg typowego czasu dostępu
* pamięć stała - dysk HDD
* pamięć stała - dysk SSD
* pamięć operacyjna RAM
* pamięć cache L2
* pamięć cache L1
* rejestry procesora


### Połączenie wyjścia przerzutnika z wejściem kolejnego
* Rejestr z dostępem szeregowym
* Działanie zgodnez koncepcją FIFO (first in - first out, kolejka)
* Dane można odczytać wysuwając po 1 bicie w kolejnych taktach zegara
* układ synchroniczny

### Rejestr z dostępem równoległym
* Wymaga tylu linii do przesyłu danych ile bitów przechowuje
* Umożliwia jednoczesny dostęp do wszystkich bitów przechowywanych w rejestrze jednocześnie
* Umożliwia zapis nowej zawartości całego rejestru w pojedynczym takcie zegara
* jest układem synchronicznym


## Tranzystory, Open collector

### Tranzystor
* Umożliwia budowanie układów realizujących dwuwartościową logikę boolowską. Jego działanie można zamodelować jako klucz włączone/wyłączone
* Tryb nasycenia pozwala na wymuszenie stanu niskiego na lniach sygnałowych
* Jest wykorzystywany we współczesnych komputerach
* Jest wykorzystywany w DRAM

### Ustalenie praw dostępu do wspólnej magistrali
* Wykorzystuje koncepcję otwartego kolektora
* Wykorzystuje własność tranzystora do wymuszenia stanu niskiego na współdzielonej linii sygnałowej
* Wykorzystuje własności tranzystora w trybie nasycenia

### Układ wspólnego emitera
* nasycenie tranzystora npn pozwala na wymuszenie stanu niskiego na współdzielonej linii sygnałowej
* zatkanie tranzystore npn pozwala na wymuszenie stanu niskiego na współdzielonej linii sygnałowej przez inne układy