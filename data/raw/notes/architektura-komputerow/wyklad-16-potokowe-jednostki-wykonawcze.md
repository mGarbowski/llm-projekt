# Potokowe jednostki wykonawcze

Krótszy okres zegara, bo wygnał musi przepropagować tylko do najbliższego rejestru pośredniego

W każdym takcie zegara rozpoczyna się kolejna instrukcja

Jeżeli wprowadzi się gdzieś zrównoleglenie danych lub buforowanie to pojawiają się problemy z synchronizacją - zawsze!!!

```asm
add x4, x3, x2
add x6, x5, x4
```

Jeśli wykonają się jedna po drugiej to druga instrukcja wczyta starą wartość x4. Jeśli wykonywanie zostanie przerwane przez system operacyjny to wynik będzie poprawne

Pojawia się hazard typu read-after-write - wynik jest niedeterministyczny

Hazard musi być bezwzględnie usunięty, działanie systemu cyfrowego musi być deterministyczne

## Rozwiązanie hazardu typu Read-After-Write (RAW)
* zakaz stwarzania sytuacji powodujących hazard (metoda administracyjna)
  * każdy programista zignoruje
  * trzeba wstawiać puste instrukcje
* Wstrzymanie potoku po wykryciu hazardu
  * układ kombinacyjny porównujący numery rejestru docelowego i źródłowego w odpowiednich instrukcjach
  * trzeba patrzeć 2 kroki do tyłu (w konkretnej realizacji, MIPS(?))
  * jeśli układ wykrył hazard to zatrzywane są kroki IF i RD
  * efekt jak wstrzyknięcie pustej instrukcji do stopnia ALU
  * procesor nadal marnuje cykle zegara
* Poprwoadzić dodatkową szynę do stopnia RD ze stopni ALU i MEM (obejścia)
  * Właściwie to wynik jest wyliczony w stopniu ALU a nie WB, a stopień ALU jest bliżej stopnia RD
  * Przy stopniu RD jest układ komparatorów i multiplekserów
  * czyta wartość ALU albo wartość MEM albo zawartość rejestru (w tej kolejności)

Analiza problemów synchronizacyjnych - producent, konsument, przebieg czasowy, dystans

## Load-Use Penalty
```asm
lw x4
add x6, x5, x4
```

* Nie da się rozwiązać hazardu bez wprowadzania opóźnienia - odczyt w stopniu MEM
* Load-use penalty - występuje we wszystkich współczesnych architekturach
* Poślizg potoku - procesor automatycznie wprowadza opóźnienie


## Instrukcje skoku w potoku
* Trzeba podjąć decyzję czy skakać czy nie skakać
* Przeładowanie PC może zajść dopiero kiedy adres wynikowy pojawi się w ALU
* Program może skoczyć a instrukcje już zostały wczytane i zaczęły się wykonywać
* Nie da się odzyskać czasu straconego na pobranie instrukcji po instrukcji skoku
* Każdy skok z przeładowaniem PC powoduje stratę jednego cyklu zegara
* Branch penalty - inny powód niż w procesorach wielocyklowych ale też wprowadza opóźnienie

### Delayed branch
* Wykonuje następną instrukcję po instrukcji skoku i doopiero wtedy jest wykonywany skok
* "It's a feature"
  * Program pisze się normalnie
  * Jeśli przed instrukcją skoku jest instrukcja, która nie wpływa na warunek to umieszcza się ją po opóxnionym skoku
  * (slot opóźnienia)
  * W praktyce w 90% przypadków slot wypełnia się użyteczną instrukcją a w 10% NOP
* Współcześnie nie jest wykorzystywany, nie rozwiązauje problemów współczesnych architektur


## Wydajność potoku
W idealnym przypadku byłaby jedna instrukcja na cykl zegara

### Opóźnienia powodują
* wewnątrz potoku
  * hazardy usuwane inaczej niż obejściami
  * ładowanie danych z pamięci
  * skoki
* na zewnątrz potoku
  * dostęp do hierarchii pamięci dłuższa niż 1 cykl

Praktyczna wydajność osiągana przez procesory potokowe to ok. 1.2 cyklu na instrukcję


## Przyspieszanie potoku
* Wydajność ogranicza czas propagacji
* Czas propagacji jest ograniczony przez aktualną technologię półprzewodnikową
* Można podzielić potok na większą liczbę faz, z których każda jest krótsza więc wykona się szybciej
* Superpotok - dłuższy niż 6 stopni
  * różnica względem procesorów potokowych jest tylko ilościowa
  * występują takiego samego typu problemy synchronizacyjne tylko większe
  * wymaga większych multiplekserów, więcej szyn
  * 3 razy większe load-use penalty

### Rozwiązanie w MIPS R4000
* Rozbito stopień dostępu do pamięci na 3 stopnie
* Wymiana z cache instrukcji i cache pamięci odbywa się potokowo - w każdym takcie zegara zaczyna się w jednej i kończy w drugiej instrukcji

## Budowa pamięci (każdej)
* Ma strukturę matrycową - komórki ułożone w prostokąt
* Dekoder wiersza
* Multiplekser kolumn
* Rozbicie dekodowania wiersza i odczytu kolumny można wykorzysta do potokowych odwołań w 2 fazach


Architektura potokowa jest używana tylko w procesorach riscowych, architektura load-store
Argumenty skalarne i zmienne lokalne skalarne są w rejestrach
Odwołania do pamięci występują głównie w epilogu i prologu procedury, wiele na raz
Można zmienić kolejność ładowania danych tak, żeby odpowiendio dużo użytecznych instrukcji rozdzielało ładowanie od używania danej


## Wydajność superpotoków
* Gorsze CPI, rzędu 1.5
* 2x krótszy okres zegara
* Wychodzi 50% lepsza wydajność(?)

Wyższa częstotliwość pracy - większy pobór mocy

Zależnie od potrzeb - może być potrzebna dłuższa praca na baterii w laptopach, kieyd i tak są wystarczająco szybkie


## Realizacja potokowa procesora CISC
CISC nie nadaje się wprost do realizacji potokowej

Procesor z transkodowaniem instrukcji - wszystkie współczesne

* kawałek procesroa odpowiada za pobieranie instrukcji CISC
* instrukcja CISC jest transkodowana na jedną lub więcej nistrukcji RISC
* instrukcje wymagające długiego ciągu instrukcji są odczytywane z pamięci ROM
* potokowa jednostka wykonawcza typu RISC


# Procesory wielopotokowe (superskalarne)
Kiedy procesory potokowe są zbyt wolne

Można wykonywać więcej niż jedną instrukcję jednocześnie w każdym takcie zegara

* wiele potoków wykonawczych
* wymaga porządkowania instrukcji

## Pseudosuperskalar
* intel 860
* jeden potok do obliczeń stałopozycyjnych i jeden do obliczeń zmiennopozycyjnych
* instrukcje sprawdzane parami
* specjalne instrukcje assemblerowe, które mogą być zrównoleglane
* jeśli któryś potok musi się zatrzymać to zatrzymują się razem

## Superskalar z kolejnym wykonaniem instrukcji
* mogą być różne potoki dla różnych klas instrukcji, mogą by identyczne
* musi być wolny potok do wykonania instrukcji
* instrukcje mogą być zrównoleglowe tylko jeśli nie są od siebie zależne
* wchodzi pewna liczba instrukcja do stopnia szeregującego
* w każdym takcie układ szeregujący wypycha tyle kolejnych instrukcji ile może
* nie zmiena się logika programu
* potoki pracują synchroniczne - wszystkie zatrzymują się równolegle

## Superskalar z kolejnym rozpoczynaniem i niekolejnym kończeniem
* zatrzymuje się tylko ten potok, który musi się zatrzymać
* wzrasta wydajność
* zmiana kolejności powoduje problemy synchronizacyjne, jeszcze gorsze

## Superskalar z niekolejnym wykonaniem instrukcji
* najbardziej wydajne i skomplikowane
* zdekodowane instrukcje gromadzone w stopniu szeregującym
* przekazywanie do wykonania nie są przekazywane do wykonania według kolejności w programie tylko według teego, której argumenty są już gotowe
* może być duży bufor instrukcji - złożone
* może być dekoder przydzielające instrukcje do danej klasy, do mniejszego buforu na początku potoku - prostsze
  * algorytm Tomasulo, stacje rezerwacyjne
* można zrobić jedno i drugie (AMD)

## Superskalarny z niekolejnym wykonaniem instrukcji
* Procesor musi mieć ważną wartość PC a wykonuje wiele naraz
* PC pokazuje pierwszą niewykonaną instrukcję
* Ostatnie 2 stopnie potoków są wspólne, odpowiadają za porządkowanie instrukcji

## Synchronizacja przy superskalarze ze zmianą kolejności
```asm
add t4, t3, t2
add t2, t5, t6
```

Hazard WAR - zapis po odczycie

```asm
addu t4, t3, t2
addu t4, t6, t7
addu t2, t5, t4
```

Hazard WAW - zapis po zapisie

Hazard wystąpi nawet jeśli instrukcje nie występują jedna po drugiej
Nie wynikają z zależności instrukcji - coś jest nie tak mimo tego że są niezależne - antyzależność / zależność wsteczna

Antyzależności się nie wykrywa, nie usuwa się ich tylko zapobiega


## Register renaming
Przemianowywanie rejestrów

* Dodaje się dużo więcej rejestrów niż jest widoczne w modelu programowym
* Procesor przy dekodowaniu zastępuje numery rejestrów z instrukcji fizyczne rejestry których jest więcej (dłuższe numery)
* Używane przez wszystkie procesory out-of-order
* Stopnie przywracające kolejność instrukcji odpowiadają za zwalnianie rejestrów

## Półka
* Zapis sekwencyjny
* Dostęp swobodny przez pozycję

### Antypółka
Używane przy przywracaniu kolejności instrukcji

* Dostęp sekwencyjny (tylko z początku)
* Zapis swobodny

* Jak pojawi się instrukcja na pozycji pierwszej to może zostać przekazana do stopnia zapisu
* Jeśli brakuje pierwszej instrukcji to żadna nie może zostać zdjęta

Instrukcje w wewnętrznej reprezentacji są trójargumentowy - np. `add eax, ebx` - docelowy jest nowy eax a źródłowe stary eax i ebx

## Liczba rejestrów fizycznych
p - liczba rejestrów modelu programowego
s - liczba instrukcji przebywających w sekcji out-of-order (od bufora instrukcji do stopnia przywracania kolejności włącznie)
r - liczba rejestrów fizycznych

r = p + s - 1

Wystarczy żeby nigdy nie musieć czekać na zwolnienie rejestru

Instrukcja decrement and branch w motoroli - zatrzymuje system prefetch po tej instrukcji bo raczej będzie skakać, tylko przy ostatnim obrocie pętli będzie niepotrzebny prefetch z początku pętli
