# Wykład 01 (2023-02-20)

## Literatura

* Patterson, Hennessy - Computer Organization and Design - do ściągnięcia legalnie
* The RISC-V Instruction Set Manual, [riscv.org](https://riscv.org) - dokumentacja
* [Dokumentacja Intel 64](https://developer.intel.com)
* [Dokumentacja AMD](https://amd.com)
* Dodatek A do 5 edycji Patterson-Hennessy
* System V Application Binary Interface Intel386, rozdziały 2.1-2.3, na gitlabie
* System V Application Binary Interface AMD64

## Oprogramowanie

* RARS
* NASM
* GCC

## Zakazane książki

* W Stallings
* Cheatsheets list instrukcji x86

## Treść wykładów

* Moodle
* [github.com/gbm-ii](https://github.com/gbm-ii)

## Laboratoria

* Za 3 albo 2 tygodnie
* Ważne zajęcia wprowadzające, nie trzeba się przygotować
* Ćwiczenia do pełnego wykonania w ciągu 2h labów, warto się przygotować
* Projekty do domu i z konsultacjami na laboratoriach
* Przykładowe ćwiczenia na Moodle
* Harmonogram będzie na Moodle
* Prośby o zmiane grupy kiedy pojawi się harmonogram

## Regulamin

* 2 kolokwia po 20pkt
* laboratoria 3, 3, 6, 6, 2
* min 11pkt z laboratorium, min 16pkt z kolokwiów

## Kolokwia

* Kolokwia online w terminach laboratoriów
* Można poprawić jedno kolokwium, końcowa ocena jest uśredniona
* Zgłosić się do prowadzącego w przypadkach losowych

## Wstęp do architektury komputerów

### Logiczna budowa komputera

* Procesor
* Pamięć
* Wejście / wyjście

### Jednostki miary

* normy IEEE 1541 i IEC 80000-13
* bit (b)
* oktet (o) - 8 bitów
* bajt (B) - najmneijsza jednostka adresowalna, zazwyczaj 8 bitów

### Krotności binarne

|      |    |      |
|------|----|------|
| 2^10 | Ki | kibi |
| 2^20 | Mi | mibi |
| 2^30 | Gi | gibi |
| 2^40 | Ti | tebi |
| 2^50 | Pi | pebi |
| 2^60 | Ei | exbi |

### Taksonomie

Podział architektur na kategorie

### Taksonomia Flynna

* nie ma zastosowania praktycznego
* przetwarzanie strumieni danych na podstawie strumieni instrukcji
* klasyfikuje komputery na podstawie liczby strumieni instrukcji i danych (jeden lub wiele)

SISD SIMD
MISD MIMD

* SISD
    * najprostszy komputer
    * najbardziej rozprzestrzeniony typ
    * uniprocesor von Neumanna
* SIMD
    * operacje wektorowe
    * jeden strumień instrukcji pracujący na wielu kompletach danych
    * procesor wektorowy / macierzowy
* MISD
    * nie istnieje
* MIMD
    * zestawione wiele SIMD

#### Architektura data flow

* NISD
* NIMD

Koncepcja data-flow stanowiła podstawę do projektowania sprzętu, dzisiaaj wykorzystuje się do projektowania systemów

urządzenia bez strumieni instrukcji mogą przetwarzać dane
coś co nie ma strumienia danych nie jest komputerem wg naszej definicji

Przetwarza porcje danych (tokeny). Token składa się z opisu - metki i danych przetwarzanych - payload. W Wyniku
przetwarzania uzyskuje się nowy token z opisem i payload'em.

### Taksonomia Skillicorna

Schemat blokowy (koncepcyjny) komputera opisujący jego ideę działania, model koncepcyjny. Nie odpowiada temu jak
faktycznie zbudowany jest komputer.

Struktura złożona z mniejszych składników połączonych w określony sposób.

#### Składniki architektury

* procesory instrukcji (IP)
* procesory danych (DP)
* *hierarchie* pamięci instrukcji (IM)
* *hierarchie* pamięci danych (DM)

Procesor nie zawiera elementów pamiętających (w teoretycznym modelu).

Każdy procesor ma odpowiadającą hierarchię pamięci

#### Połączenia

* procesor z hierarchią pamięci
* procesor instrukcji z procesorami danych
* procesory jednego rodzaju między sobą

#### Rodzaje połączeń

* 1-1
* 1-N
* N-N (każdy z jednym odpowiadającym)
* N x N (każdy z każdym)

Dwukierunkowy przepływ danych między proesorem danych a hierarchią pamięci danych - jedyne miejsce w którym przepływ
jest dwukierunkowy.

### Modele w taksonomii z sensownym zastosowaniem
* uniprocesor dataflow
* ...

Jeśli jest więcej niż jeden procesor to połączenia z innymi procesorami mogą być
* ma sens tylko dla procesorów danych
* słbe - przez kanał komiunikacji między procesorami danych
* silnie - przez uwspólnienie hierarchii pamięci między procesorami

### Hierarchia pamięci
Nie da się zbudować pamięci o jednocześnie dowolnie dużej pojemności i dowolnie krótkim czasie dostępu - tradeoff.

Czas dostępu rośnie z pojemnością, pojemność wpływa na fizyczny wymiar a wymiar na drogę dostępu, wydłużająca czas
dostępu.

Struktura hierarchiczna-wartwowa
* umożliwia zróżnicowanie parametrów (pojemności i czasu dostępu)
* kolejne warstwy mają coraz większe pojemności i czasy dostępu

Warstwy
* Rejestry procesora
* Kieszenie (cache), 3 poziomy
* Pamięć operacyjna
* Pamięć wirtualna (pamięć masowa, rozszerzenie pamięci operacyjnej)
* Lokalny system plików (pamięć masowa)
* Zasoby zdalne

Wydajność procesora jest ograniczona przez wydajność pamięci (z przyczyn technologicznych, pamięć jest wolniejsza).
Współczesny procesor mógłby wykonać 100 instrukcji w czasie który pamięć potrzebuje na odczyt 1 instrukcji. Cache
kompensuje różnicę w wydajności między procesorem a pamięcią.

Pamięć wirtualna rozwiązuje ograniczenie w rozmiarze pamięci operacyjnej.

Lokalny system plików przechowuje dane w sposób trwały.

### Sterowanie hierarchią pamięci
Żeby zachować względną szybkość i pojemność, trzeba przemieszczać dane po hierarchii.

Obiekty potrzebne procesorowi w danym momencie powinny znaleźć się w warstwie jak najbliższej do procesora. Obiekty
chwilowo niepotrzebne powinny być spychane do dalszych warstw, żeby zwalniać miejsce w bliższych warstwach.

| styk                               | zarządzany przez                         |
|------------------------------------|------------------------------------------|
| rejestry-reszta                    | kompilator lub programista w assemblerze |
| cache-pamięć operacyjna            | sprzęt                                   |
| pamięć operacyjna-pamięć wirtualna | system operacyjny                        |
| pamięć wirtualna-system plików     | użytkownik lub program użytkowy          |
| lokalny-zdalny                     | użytkownik lub program użytkowy          |

Styki mają różną charakterystykę czasową i granularność

Pamięć wirtualna i lokalny system plików fizycznie znajdują się na dysku (HDD/SSD)

### Maszyna von Neumanna
Ogólny pomysł na budowę komputera, uniwersytet Princeton, lata 40'.

Instrukcje tworzące program są przechowywane w tej samej pamięci co dane, na których operuje program. Paamięć składa się
z ponumerowanych komórek. Procesor odwołuje się do komórki pamięci przez jej numer nazywany **adresem**.

Kolejne instrukcje zazwyczaj znajdują się w kolejnych komórkach. Adres obecnie wykonywanej instrukcji jest przechowywany
w specjalnym rejestrze (Program Counter).