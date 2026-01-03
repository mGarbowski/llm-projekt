# Architektura komputera

## Tranzystor
możliwe 4 stany
* aktywny - wzmocnienie prądu bazy
* nasycenia - logiczne 1
* zatkania - logiczne 0
* inwersyjny


Dla układów logicznych interesujące są stany nasycenia i zatkania (1 i 0)

Otwarty kolektor - przy wielu urządzeniach podpiętych do jednej linii umożliwia przerwanie i zapewnia ekskluzywny dostęp oparty o priorytet, szyna I2C.

Kiedy wiele urządzeń jest podłączonych kolektorem tranzystora do szyny to jeśli dowolny z nich przejdzie w stan nasycenia (1), wtedy na szynie wymusza stan niski, nawet jeśli pozostałe urządzenia są w stanie zatkania (0).

Tryb nasycenia pozwala na wymuszenie stanu niskiego na liniach sygnałowych

## Claude Shanon
Powiązał algebrę Boole'a z układami elektrycznymi.
Minimalizację wyrażenia logicznego można wykorzystać do optymalizacji układu, układy mogą rozwiązywać problemy logiczne itd.
Algebra Boole'a i system binarny rządzą się tymi samymi zasadami.


## System binarny i arytmetyka
Dodawanie dwóch liczb binarnych można wyrazić tabelą prawdy (a, b, suma, przeniesienie)


## Przerzutniki
Przerzutniki umożliwiają zapamiętywanie sygnału - asynchronicznie.
Można dodać sygnał zegara - flip-flop typu D, zapamiętany jest sygnał z chwili zatrzaśnięcia.

Zegar nie musi być sygnałem o stałym okresie ale np. reagować na zdarzenia.


## Słowo
Dwa znaczenia w kontekście architektury komputerów
* natywna wielkość jednostki danych używanej przez CPU (liczba bitów)
* ze względów historycznych, przyjmuje się określenia
  * word - 16b
  * dword - 32b
  * qword - 64b


## Rejestr
* Adresowalny zestaw bitów - bajt (najczęściej 8 bitów ale niekoniecznie!)
* Zapamiętuje zestaw wartości binarnych
* Ma ograniczoną pojemność - może nastąpić przepełnienie
* Wspiera natywnie słowa o określonej długości
* Są naturalne ograniczenia na maksymalną wartość

### Z dostępem równoległym
* Umożliwia jednoczesny dostęp do wszystkich bitów przechowywanych w rejestrze jednocześnie
* Wymaga tylu linii do przesyłu danych ile bitów przechowuje
* Umożliwia zapis nowej wartości całego rejestru w jednym takcie zegara
* synchroniczny

### Rejestr przesuwny (dostęp szeregowy)
* Odczyt/zapis pojedynczego bitu w jednym takcie zegara
* potrzebuje tylko jednej linii do przesyłu danych
* Synchroniczny
  
Mając wiele rejestrów, linie wyjściowe łączą się w szynę danych (magistralę), którą można odczytywać po adresie. 

Na szynie mogą powstać konflikty jeśli dwa rejestry wystawiają na danej linii różne wartości. (open collector)

Szyna sterująca służy do wysyłania rejestrom poleceń wystawienia/zapamiętania zawartości

### Polecenia
* READ - rejestr podaje swoją wartość na szynę danych
* WRITE - rejestr zatrzaskuje z szyny danych nową wartość
* CLEAR - wyzerowanie zawartości rejestru

## ALU Arithmetic Logic Unit
![ALU](https://upload.wikimedia.org/wikipedia/commons/0/0f/ALU_block.gif)
Wymyślony przez von Neumanna w 1945

Układ kombinacyjny wykonujący podstawowe operacje logiczne i arytmetyczne, złożony z rejestrów, szyn itd.

Na wejściu: A, B, kod operacji

Na wyjściu: wynik operacji, sygnał stanu (np. przepełnienie)

### Flagi
* N - negative
* O - overflow
* Z - zero
* C - carry

## Prymitywny procesor
* Rejestry
* ALU
* Szyna danych
* Jednostka sterująca

## Paradygmaty programowania
* strukturalne
* obiektowe

oddalamy się od niskiego poziomu assemblera

## Assembler
dodawanie dwóch liczb
```
mov R0, A
add R1
mov A, R2
```

Operacje i adresy rejestrów są odpowiednio kodowane i dekodowane przez jednostke sterującą.

Nie wszystkie operacje wymagają 2 argumentów.

| instrukcja | kod operacji | kod źródła | kod celu | kod instrukcji |
| ---------- | ------------ | ---------- | -------- | -------------- |
| mov R0, A  | 00           | 00         | 11       | 000011         |
| add R1     | 01           | 01         |          | 0101           |
| mov A, R2  | 00           | 11         | 10       | 001110         |

Instrukcje nie muszą być jednakowej długości, zależy od architektury


## Tryby adresowania
Dana przechowywana w pamięci może być adresem jakeiejś innej danej.

* adresowanie bezwględne -> czytaj/zapisz pod adresem 0xXXXXXXXX
* adresowanie względne -> czytaj/zapisz pod adresem 0xXXXXXXXX + offset
  * adres bazowy i przesunięcie


## Program dodający dwie liczby
```
move [0x20], R0
move R0, A
move [0x22], R1
add R1
move A, R2
move R2, [0x24]
```

1. Wczytaj liczbę pod adresem 0x20 do rejestru R0
2. Przenieś zawartość rejestru R0 do akumulatora
3. Wczytaj liczbę pod adresem 0x22 do rejestru R1
4. Dodaj do akumulatora zawartość rejestru R1
5. Przenieś zawartość akumulatora do rejeestru R2
6. Zapisz zawartość rejestru R2 pod adresem 0x24 w pamięci


## Kodowanie instrukcji maszynowych
| Cel / Źródło   | Kod  |
| -------------- | ---- |
| R0             | 0000 |
| R1             | 0001 |
| R2             | 0010 |
| Akumulator (A) | 0011 |
| Ram            | 0100 |
| immediate      | 1111 |

Immediate - sięgnięcie do zawartości komórki pamięci o podanym adresie. Druga połowa bajtu kodu źródła



| Instrukcja     | Kod operacji | Kod źródła | Adres | Kod celu | Adres | Kod instrukcji |
| -------------- | ------------ | ---------- | ----- | -------- | ----- | -------------- |
| mov [0x20], R0 | 0x00         | 0x4F       | 0x20  | 0x00     |       | 0x 00 4F 20 00 |
| mov R0, A      | 0x00         | 0x00       |       | 0x30     |       | 0x 00 00 30    |
| mov [0x22], R1 | 0x00         | 0x4F       | 0x22  | 0x10     |       | 0x 00 4F 22 10 |
| add R1         | 0x01         | 0x10       |       |          |       | 0x 01 10       |
| mov A, R2      | 0x00         | 0x30       |       | 0x20     |       | 0x 00 30 20    |
| mov R2, [0x24] | 0x00         | 0x20       |       | 0x4F     | 0x24  | 0x 00 20 4F 24 |


## Pamięc operacyjna
Zbiór rejestrów, każdy z unikalnym numerem (adresem), połączonych szynami
* szyna adresowa - który rejestr wybrać
* szyna sterująca - jaką operację wykonać (READ/WRITE/CLEAR)
* szyna danych - przesyłanie zawartości z/do rejestru

Pamięć nie musi składać się z rejestrów - może być cokolwiek ułożonego w tabelę, zdolne do zapamiętywania bitów.

## DRAM
Dynamic Random Access Memory

![DRAM](./obrazy/https://upload.wikimedia.org/wikipedia/commons/8/80/Square_array_of_mosfet_cells_write.png) 

* Jedna komórka składa się z tranzystora i kondensatora, który przechowuje bit (może być naładowany lub nie).

* Kondensatory rozładowują się z czasem więc konieczne jest odświeżanie

* Obecnie używany - DDR SDRAM - Double Data Rate Synchronous Dynamic  Random-Access Memory

* Pamięć ulotna - wymaga stałego zasilania

## SRAM
Static Random Access Memory
![SRAM](./obrazy/https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/SRAM_Cell_%286_Transistors%29.svg/1280px-SRAM_Cell_%286_Transistors%29.svg.png)

  * nie wymaga odświeżania
  * mniej kompaktowa - 6 tranzystorów na 1 bit
  * szybsza niż DRAM
  * używana w cache'ach
  * pamięć ulotna - wymaga stałego zasilania


## Prawo Moore'a
Liczba tranzystorów będzie się podwajać w danym okresie (rosnąć wykładniczo)

## Budowa komputera
![Schemat](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Frh6stzxdcl1wf9gj1fkj14uc-wpengine.netdna-ssl.com%2Fwp-content%2Fuploads%2F2016%2F12%2F640px-Computer_system_bus.svg_.png&f=1&nofb=1&ipt=4b228cb9566bab5f9b217535a4024d5bb6595aca303eaea7da45c323558ab4da&ipo=images)

### Procesor
* PC - program counter
  * adres obecnie wykonywanej instrukcji
  * wystawiany na szynę adresową do pobrania instrukcji
* Rejestry
* Jednostka sterująca
* ALU z rejestrem akumulatora

### Pamięć
* poza procesorem
* przechowuje instrukcje

### Szyny
* Szyna danych
  * przesyłanie informacji między pamięcią i rejestrami
* Szyna adresowa
  * podawanie pamięci adresu do odczytu/zapisu
* Linie sterujące
  * wybór operacji oddczytu/zapisu
* Wewnętrzna szyna danych procesora


## Co robi komputer

### Operacje
* Odczyt i zapis z pamięci
* Arytmetyczne
* Logiczne
* Porównania
* Rotacje i przesunięcia bitów
* Skoki warunkowe i bezwarunkowe do kolejnych instrukcji

### Wykonuje instrukcje
* Sekwencyjnie (inkrementacja PC)
* Skokowo (zmiana PC inna niż zwykła inkrementacja, względna lub bezwzględna)

## Cykl pracy procesora
* Fetch
  * Pobranie instrukcji odpowiadającej wartości PC z pamięci do rejestru
  * Inkrementacja PC
* Decode
  * Zdekodowanie instrukcji przez jednostkę sterującą procesora
* Execute
  * Wykonanie zdekodowanej instrukcji przez wysyłanie sygnałów sterujących do odpowiednich komponentów (np. ALU)
  * Wtedy procesor wykonuja właściwą pracę z perspektywy użytkownika


## Zestaw instrukcji procesora
* CISC
  * Compound Instruction Set Computer
  * Zestaw "bogatych" instrukcji
  * Jedna instrukcja - skomplikowana operacja
  * Skomplikowane tryby adresowania
* RISC
  * Reduced Instruction Set Computer
  * Zestaw "prostych" instrukcji
  * Proste i ograniczone tryby adresowania

Złożone instrukcje są znacznie trudniejsze do zaprojektowania. Przejście do mniej skomplikowanych instrukcji (RISC) sprawiło, że procesory stały się wydajniejsze.


## Zmienna
Zmienna to pojęcie ze świata wysokopoziomowego - coś co przechowuje wartość, do której można się odwołać przez nazwę.

Zmienna jest adresem początkowej komórki, gdzie jest przechowywana jej wartość. Trzeba wiedzieć jak zinterpretować zawartość binarną pamięci
  * może to być liczba w U2
  * może być ciąg znaków/obiektów/struktur
  * może być adresem pod którym jest wartość innej zmiennej
  * może być adresem kodu instrukcji


## Architektura von Neumanna (Princeton)
![Schemat](./obrazy/https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/Von_Neumann_Architecture.svg/1920px-Von_Neumann_Architecture.svg.png)

* Program i dane są przechowywane w tej samej pamięci
* Nie można jednocześnie pobierać danych i instrukcji - von Neumann bottleneck
* Model obliczeń zgodny z maszyną Turinga
* Pamięć składa się z ponumerowanych komórek
* Dostęp do komórki pamięci przez podanie jej adresu
* Adres komórki z instrukcją programu jest przechowywany i inkrementowany w rejestrze PC (Program Counter)
* Możliwość modyfikacji programu (operowanie na komórkach pamięci z instrukcjami)
* Obiekt zapisany jako dana może być pobrany jako instrukcja
* Komputery uniwersalne


## Architektura typu Harvard
![Schemat](./obrazy/https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Harvard_architecture.svg/1920px-Harvard_architecture.svg.png)

* Oddzielna pamięć dla programu i oddzielna dla danych
  * osobne przestrzenie adresowe
  * niezgodna z koncpecją von Neumanna
* Szybsza od architektury von Neumanna
  * można jednocześnie pobierać dane i instrukcje
* Program wbity na stałe, bez możliwości zmiany
  * nie ma możliwości zapisu do pamięci instrukcji
* Procesory sygnałowe, mikrokomputery jednoukładowe


## Arhitektura Harvard-Princeton
![Schemat](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fbrasil.cel.agh.edu.pl%2F~08pdiakow%2Fgrafika%2Fhp.png&f=1&nofb=1&ipt=367c933fbb6e37aaf4aefa665c37f42f28629eab6269780a43dbf4d85d0a8909&ipo=images)

* Oddzielne górne warstwy pamięci (cache) - jak w architekturze Harvard
* Wspólna dolna warstwa pamięci - jak w architekturze von Neumanna
* Szybkie działanie dzięki równoległemu dostępowi do instrukcji i danych w górnej pamięci (jeśli są w cache'u, a nie trzeba ich pobierać z głównej pamięci)
* Programowalny - przez zapis do wspólnej pamięci
* Typowe dla współczesnych PC

Pamięć cache jest mniejsza ale szybsza. Nie ma pewności czy zapis wartości do pamięci cache spowoduje też zapis do pamięci głównej.

Pojawia się problem kiedy jest więcej niż 1 procesor, który chce odczytać wspólne dane.


## Klasyfikacja Flynna
Podział architektur komputerowych ze względu na liczbę jednoczesnych strumieni instrukcji i danych

| Single Instruction                                                                              | Multiple Instruction                                                                           |
| ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| ![SISD](./obrazy/https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/SISD.svg/1024px-SISD.svg.png) | ![MISD](./obrazy/https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/MISD.svg/800px-MISD.svg.png) |
| ![SIMD](./obrazy/https://upload.wikimedia.org/wikipedia/commons/thumb/2/21/SIMD.svg/800px-SIMD.svg.png)  | ![MIMD](./obrazy/https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/MIMD.svg/800px-MIMD.svg.png) |

## SISD vs SIMD
Przemnożenie 4 różnych ośmiobitowych liczb przez 3.

| SISD                                                                                                                             | SIMD                                                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| ![SISD](./obrazy/https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Non-SIMD_cpu_diagram1.svg/800px-Non-SIMD_cpu_diagram1.svg.png) | ![SIMD](./obrazy/https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/SIMD_cpu_diagram1.svg/800px-SIMD_cpu_diagram1.svg.png) |

### SISD
* Wczytuje liczbę z pamięci do rejestru R1
* Mnoży zawartość R1 przez zawartość R2
* Zapisuje wynik mnożenia do R3
* Zapisuje wynik z R3 do pamięci
* Powtarza po kolei dla każdej z 4 liczb
* 4 wczytania z pamięci, 4 mnożenia, 4 zapisy do pamięci

### SIMD
* Wykorzystuje 32-bitowy rejestr jako 4 rejestry 8-bitowe
* Jednocześnie wczytuje 4 liczby do R1
* Wykonuje 1 mnożenie SIMD 
* Jednocześnie zapisuje 4 wyniki do pamięci
* 1 wczytanie z pamięci, 1 mnożenie, 1 zapis do pamięci
* 4-krotne przyspieszenie przy takim podziale rejestru


## Przetwarzanie potokowe i superskalarne
Instrukcje wykonywane są etapami

* IF - instruction fetch
* ID - instruction decode
* EX - execute
* MEM - memory access
* WB - write back

Classic RISC Pipeline

![Pipeline](./obrazy/https://upload.wikimedia.org/wikipedia/commons/2/21/Fivestagespipeline.png)

Może wystąpić hazard jeśli późniejszy program w swojej fazie Execute, będzie korzystać z tych samych danych co wcześniejszy program ale zanim wcześniejszy zdąży je zapisać z powrotem do rejestru w fazie Write Back.

Zrównoleglenie przyspiesza wykonywanie ale trzeba zabezpieczyć wspólne dane.

Atomowa instrukcja - nie da się rozdzielić (zarezerwować dostęp do zasobu na czas wykonywania instrukcji, inny program nie może zmodyfikować jego danych)


## Jednostki pamięci
b - bit

o - oktet (8 bitów)

B - bajt (byte) - najmneijsza jednostka informacji adresowana przez procesor zazwyczaj 8b

| jednostka | zapis | wartość   | jednostka | zapis | wartość   |
| --------- | ----- | --------- | --------- | ----- | --------- |
| kilobyte  | kB    | $1000$b   | kibibyte  | KiB   | $1024$b   |
| megabyte  | MB    | $1000^2$b | mebibyte  | MiB   | $1024^2$b |
| kilobyte  | GB    | $1000^3$b | gibibyte  | GiB   | $1024^3$b |


## Opóźnienie
| Medium                       | Wielkość | Czas    |
| ---------------------------- | -------- | ------- |
| ALU / flip-flops             | KB       | <1ns    |
| Rejestry                     | KB       | <1ns    |
| Cache L1                     | KB       | <1ns    |
| Cache L2, L3                 | MB       | 3-10ns  |
| RAM                          | GB       | 10-30ns |
| Dyski lokalne, pamięć masowa | TB       | 1-30ms  |
| Zasoby zdalne, chmura        | PB       | 100ms   |