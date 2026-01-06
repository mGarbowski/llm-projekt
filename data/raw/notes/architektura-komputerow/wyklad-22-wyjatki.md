# Wyjątki (2023-05-15)
Zdarzenie w systemie komputerowym wymagające przerwania wykonania bieżącego strumienia instrukcji i przekazania sterowania do systemu operacyjnego (procedury, którąwybiera system)

* asynchroniczne - niewynikające z wykonywanych instrukcji lub niemożliwe do powiązania z konkretną instrukcją
  * przerwania (interrupt) - obsługa może być odsunięta w czasie
  * błędy krytyczne - obsługiwane natychmiast
* synchroniczne - wynikające z wykonania instrukcji i dokładnie powiązane z instrukcją
  * pułapki (traps)
  * błędy (errors)
    * naprawialne (faults)
    * nienaprawialne (aborts) - w niektórych architekturach są asynchroniczne

## Przerwania
* poza procesorem
  * urządzenia IO
  * timer systemowy


## Pułapki
Wyjątki generowane przez wykonanie instrukcji - zaplanowane

* wywołanie systemu operacyjnego (SYSCALL, ECALL)
* błędy wykonywanych instrukcji (nadmiar dzielenia)
* pułapki śledzenia
  * generowane przez dowolną instrukcje jeśli ustwi się w procesroze tryb śledzenia
  * służy do debuggowania

## Błędy
* generowane przez procesor (na ogół)
* np próba wykonania instrukcji o nieznanym kodzie operacyjnym
* np błąd wyrównania
* np niewystarczający poziom uprzywilejowania

## Obsługa wyjątków
* Każdy musi zostać obsłużony
  * błędy i pułapki - od razu po wystąpieniu
  * przerwania - kiedy OS jest gotowy
* Obsługa na poziomie sprzęu - do momentu wykonania pierwszej instrukcji procedury systemowej (kończy się obsługa przez procesor, zaczyna się obsługa przez OS)
* Obsługa programowa - procedura systemowa


### Fazy
* wykrycie wyjątku
* identyfikacja źródła wyjątku
* przerwanie wykonania strumienia instrukcji i zapamiętanie bieżącego kontekstu procesora (tak żeby można było go przywrócic)
* załadowanie nowego kontekstu procesora i rozpoczęcie wykonywania nowego strumienia instrukcji - procedury systemowej obsługującej wyjątek

## Priorytet procesora
(co innego niż poziom uprzywilejowania!)

* wszystkie zadania systemowe działają na najniższym prorytecie procesora
* przerwanie jest obsługiwane kiedy priorytet przerwania jest wyższy niż priorytet procesora
* wielopoziomowy system przerwań
  * można określić mniej i bardziej pilne przerwania
* Układ arbitrażu przerwań (sterownik przerwań)
  * odpowiada procesorowmi id przerwania o najwyższym priorytecie

## Zapamiętanie kontekstu
* Cel
  * Powrót po obsłudze
  * Komunikat diagnostyczny
* Treść - informacje o stanie procesora - wszystko to co procesor będzie musiał sprzętowo zmienić
  * PC
  * rejestr stanu
  * priorytet procesora
  * informacje o odwołaniu do pamięci
  * rejestry z modelu programowego mogą zostać zapamiętane przez oprogramowanie 
* Zapamiętywany w miejscu naturalnym dla architektury
  * na stosie w CISC
  * w rejestrach systemowych w CISC
* Licznik instrukcji
  * jeśli wyjątek nie ma związnku z instrukcją albo jest normalnym zakończeniem (syscall) to ma sens zachowanie nextPC
  * currentPC - ma sens dla pułapek sygnalizujących błąd wykonania i dla błędów (trzeba wiedzieć która insturkcja powoduje błąd)

## Zmiany kontekstu systemowego w czasie obsługi sprzętowej wyjątku
* Na poziomie uprzywilejowania systemu (na ogół)
* Wyłącza tryb śledzenia
* Przyjmuje priorytet obsługiwanego przerwania
* Każdy poziom uprzywilejowana musi mieć własny, oddzielny stos, system nie może polegać na poprwanym działaniu programu użytkowego


## Sekwencja czynności
* tradycyjna
  * wykrycie i arbitraż
  * identyfikacja
  * składowanie kontekstu
  * ładowanie nowego kontekstu
* współczesne (ARM Cortex)
  * wykrycie
  * składowanie kontekstu
  * arbitraź i identyfikacja
  * załadowanie nowego kontekstu
  * opóźnienie arbitrażu umożliwia szybszą obsługę wyjątków o wyższych priorytetach któe występująod razu po niższych (rozwiązuje problem inwersji priorytetów)


## Przełączanie stosów
* każdy poziom uprzywilejowania ma swój oddzielny stos
* procesor decyduje o wyborze rejestru wskaźnika stosu
* dany poziom ma dostęp do wskaźnika stosu poziomu mniej uprzywilejowanaego
* oprogramowanie systemowe powinno mieć możliwośćoperowania na pamięci z poziomu uprzywilejowania aplikacji

## Priorytety przerwań
* Obsługa przerwania może być przerwana tylko przez przerwanie o wyższym priorytecie
* Niektóre procedury jądra wymagają zablokowania przerwań (sekcje krytyczne, np. przełączanie zadań, komunikacja między zadaniami)

## Ładowanie nowego kontekstu
Są różne często stosowane rozwiązania

* wspólny punkt wejścia
* wiele ustalonych adresó początkowych procedur
* tablica adresów procedur obsługi (wektorowy system obsługi wyjątków)


## Wyjątki w x86
* 256 możliwych do zdefiniowania, 32 dla procesoraw
* 8-bitowy identyfikator używany jako indeks tablicy bram wyjątków
* Klasyfikacja wyjątków
  * przerwania
  * pułapki
  * błędy
  * błędy nienaprawialne

Każdy wątek ma własny, oddzielny stos aplikacyjny i stos systemowy

Zatrzymanie wątku wiąże się z wywołaniem schedulera - procesor zostanie przełączony na inny wątek który wcześniej został wstrzymany (przełącza się stos systemowy)

Instrukcja powrotu z procedury obsługi wyjątku nie tylko przeładowuje PC ale też rejestr stanu (instrukcja tylko systemowa)


Po powrocie z obsługi błędu może nastąpić
* restart instrukcji która spowodowała błąd - używane we współczesnych superskalarach bo już jest zaimplementowane anulowanie instrukcji
* kontynuacja instrukcji od czynności mikrokodu, która spowodowała błąd

Procesor może wykorzystywać mechanizm wyjątków np do realizacji mechanizmu zarządzania zasobami (np. leniwa alokacja)


## Asynchroniczne przerwanie programowe
* przydatne do budowania systemów zdarzeniowych


## Błąd podwójny
* błąd w trakcie obsługi błedu
* odwołanie do pamięci może spowodować błąd
* procesor nie ma ważnej wartości licznika instrukcji
* zdarza się tylko przy błędach w systemie operacyjnym - sygnalizuje awarię systemu

## Inicjowanie działania procesora - Reset
Zrealizowane jak wyjątek bez składowania stanu

* ...

## Priorytety typów wyjątków
Dla mikrokodu procesora błąd -> pułapka -> przerwanie

Pilność dla systemu operacyjnego przerwania -> pułapki -> błędy (przerwania są najbardziej krytyczne czasowo)

## Wymagania czasowe
* obsługa przerwań jest krytyczna czasowo (zwłaszcza w systemach czasu rzeczywistego)
* parametry czasowe
  * czas programowej reakcji
  * czas sprzętowej reakcji
  * determinizm czasu odpowiedzi
* może być tylko jedno przerwanie o gwarantowanym maksymalnym czasie wykonania (o najwyższym priorytecie)
* mogą istnieć pojedyncze bardzo wolne instrukcje które opóxniają obsługę przerwań
* instrukcje iteracyjne są przerywalne

## Późne nadejście (late arrival)
rozwiązane w ARM Cortex

## Łańczuchowanie przerwań (chaining)
Jeśli po zakończeniu obsługi przerwania procesor musi wrócić do obsługi kolejnego przerwanie to nie odtwarza stanu


## Determinizm czasu odpowiedzi
* W niektórych zastosowaniach (sterowanie urządzeniami elektrycznymi) ważne jest żeby czas był stały
* W procesorze umieszcza się timer sprzętowy odliczający większy czas niż maksymalny gwarantowany i odczekuje po obsłudze przerwania żeby kolejna instrukcja wykonała się w deterministycznym czasie


## Pamięć wirtualna
* wymaga podziału przestrzeni adresowe jprocesu na wiele obszarów
* aktualnie używane obszary zaalokowane są w pamięci operacyjnej - pamięć operacyjna jest buforem pamięci wirtualnej
* ...

### Implementacja
* strony przydzielone programowi ale których nie ma w pamięci mają nieważne deskryptory
* odwołanie po nieważnym deskryptorze generuje błąd
* 2 bity deskryptora
  * accessed - nastąpił odczyt
  * modified/dirty - do strony nastąpił zapis
  * system operacyjny zawsze zeruje te bity
  * jednostka stronicowania ustawia bit accessed jeśli z niego skorzystała (nastąpił odczyt)
* system co jakiś czas (1s) przegląda wszystkie deskryptory i gromadzi historie użycia każdej strony i ustawia bit accessed na 0
* przy wyznaczaniu ofiary, w pierwszej kolejności są wyrzucane storny które najdawniej nie były używane
* Jeśli do strony nastąpił zapis to przed wyrzuceniem z pamięci trzeba najpierw zapisać ją na dysk

Moduły 14 i 15 do zrobienia samemu


Obsługa wejścia/wyjścia - wady zalety