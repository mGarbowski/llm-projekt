## Cykl instrukcyjny procesora
* Fetch
* Decode
* Read
* Execute
* Write

W procesorze jednocyklowym etapy są odwzorowane w różnych fragmentach sprzętu

Nie zawsze fizyczna budowa procesora musi odzwierciedlać dokładnie ten schemat

## Realizacja wielocyklowa
* Przestarzała
* Wygląda tak jak wygląda ze względów historycznych, stan techniki w latach 60
* minimalizuje liczbe wykorzystanych bloków funkcjonalnych
* Wykonanie instrukcji dzieli się na kilka cyklów maszynowych
  * jednostka sterująca najczęściej implementowana jako automat mikroprogramowany - skomplikowana
  * reużywanie bloków funkcjonalnyhc w różne sposoby w zależności od cyklu
  * więcej multiplekserów
  * rejestr instrukcji - zapamiętuje aktualnie wykonywaną instrukcję między cyklami - trzeba też czytać dane z pamięci
  * rejestr danych pamięci
  * rejestry robocze z pośrednimi wynikami ALU
  * rejestry są niewidoczne z punktu widzenia modelu programowego
  * nie narzuca sekwencji czynności w obrębie instrukcji - można mieć dowolnie skomplikowane instrukcje, wielofazowe
* Odwzorowanie między etapem cyklu instrukcyjnego w czasie (ten sam sprzęt, różne chwile w czasie)


## Połączenie procesora z pamięcią
* Szyna
* Bus interface - w procesorze, układ obsługujący szynę
* wewnętrzna szyna procesora
  * jednostka sterująca
  * rejestry
  * alu z rejestrami na wejściu

### Cykl maszynowy pobrania instrukcji
Nie da się odczytać danej z pamięci z jednym cyklu.

Cykl maszynowy składa się w różnej liczbie taktów zegara

## Wydajność
Komputer jednocyklowy zrealizowany w tej samej technologii wcale nie musi być szybszy

### Komputer jednocyklowy
Ograniczona przez czas propagacji po najdłuższej ścieżce kombinacyjnej - okres zegara musi być dłuższy

### Komputer wielocyklowy
Więcej cykli zegara ale mogą być dużo krótsze, bo nie muszą propagować przez cały układ

Jedna ścieżka dla danych - potzreba wielu cykli żeby wykonać np operację trójargumentową, można dołożyć rejestr wynikowy ALU i zawinąć na wejście (akumulator) - wtedy nie potrzeba aż tylu instrukcji, jest druga, krótsza ściezka danych w obrębie ALU

Więcej niezależnych szyn = mniej cykli maszynowych = szybszy procesor (?)

Nie każda instrukcja odwołuje się do pamięci, niektóre obszary procesora nic nie robią w ciągu całej instrukcji

Można jednocześnie wykonywać instrukcję bez odwołania do pamięci i zacząć pobierać następną instrukcję

## Prefetch
Pobieranie instrukcji na zapas

* prefetch register - bufor interfejsu szyny (albo kolejka FIFO, bo insturkcje w CISC mają zmienną długość)
* rejestr scanPC z lokalną kopią licznika instrukcji używany przez interfejs szyny
  * (PC zawiera adres następnej instrukcji - nextPC jest widoczne programowo, currentPC jest fizycznie istniejącym rejestrem)
  * jednostka sterująca wysyła do interfejscu szyny nextPC
  * interfejs szyny zapamiętuje zinkrementowaną wartość nextPC
  * interfejs rozpoczyna pobieranie z pamięci i zapisuje to do prefetch register jeśli nie dostaje innych instrukcji od jednostki sterującej
  * jednostka sterująca wysyła nextPC do interfejsu szyny
  * jeśli nextPC == scanPC to nie trzeba czytać instrukcji z pamięci i jednostka sterująca czyta prosto z rejestru prefetch (nie potrzeba 3 taktów zegara tylko 1)
* Jeśli procesor skończy wykonywać instrukcje zanim interfejs skończy prefetch to traci się czas
* Jeśli zadziała to skraca cykl instrukcyjny o etap pobierania instrukcji - ogromne przyspieszenie
* Działanie mechanizmu prefetch jest warunkowe - nie działa jeśli aktualna instrukcja jest skokiem (bo pobiera następną instrukcję)
* Statystycznie opłaca się robić prefetch mimo tego, że spowalnia niektóre instrukcje (co 10 instrukcja jest skokiem wydłużonym ok 2 razy)

## Branch penalty
Opóźnienie skoku - skoki spowalniają procesor o kilka procent

Dokładnie to różnica między wykonaniem instrukcji skoku (a właściwie czas tracony przez instrukcję skoku) i instrukcji niebędącej skokiem

## Redukcja opóźnień przy skokach
* Opóźnienie wynika z potrzeby przeładowania kolejki instrukcji
* Należy używać jak najmniej instrukcji skoku w kodzie assemblerowym
* Instrukcje iterowane - pozwalają zrealizować pętlę bez skoku
* Bufor pętli
  * procesor wykrywa krótkie pętle
  * krótka pętla mieści się w buforze
  * procesor nie pobiera instrukcji tlyko wykonuje cyklicznie instrukcje z kolejki
* Przykład z if-then-else ...


Struktura szynowa - jedna wiązka przewodów do której są przyłączone komponenty - procesor, sterowniki IO

* szyna adresowa
* szyna danych
* szyna sygnałów sterujących

Dekodowanie adresu - rozpoznaje jakie urządzenie ma obsłużyć operację - tylko jedno w każdym momencie powinno używać szyny