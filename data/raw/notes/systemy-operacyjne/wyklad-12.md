# (2024-01-09)

## Komunikaty
W środowisku rozproszonym wszystkie wymienione wcześniej metody są bezużyteczne bo nie ma dzielonej pamięci. Jedyny dostępny mechanizm to przekazywanie komunikatów.

Komunikaty można wykorzystać na potrzeby synchronizacji

Oparte na dwóch wywołaniach systemowych `send(destination, &message)` i `receive(source, &message)`. Nadaje się do komunikacji sieciowej bez wspólnej pamięci. Tworzy się analogiczny bufor ze zbioru komunikatów.

`send` jest nieblokujące, a `receive` jest blokuące (proces zawiesza się dopóki nie dojdzie komunikat)

* Konsument wysyła producentowi wiele pustych komunikatów
* Producent najpierw odbiera (zawiesza się w oczekiwaniu) a potem odsyła zapełnioną wiadomość
* Konsument odbiera (zawiesza się w oczekiwaniu) pełną wiadomość i odsyła pustą

Kontrola przepływu - wydajność jest ograniczona do szybkości wolniejszego z dwóch procesów, producent prześle treść dopiero jak dostanie pusty komunikat - gwarancja że nie będzie przepełnienia. Szybszy producent nie zaleje wolnego konsumenta komunikatami


## Problem ucztujących filozofów
Jeśli proces wszedł do sekcji krytycznej, opuścił jakiś semafor i poszedł spać to ten semafor będzie opuszczony - może nastąpić blokada, jeśli inny proces czeka na semafor, a ten który opuścił nie zostanie obudzony i go nie podniesie

N filozofów przy stole i N widelców pomiędzy nimi, filozof musi wziąć 2 widelce, żeby móc jeść, filozof może jeść lub myśleć

Wzajemne wykluczanie w dostępie do stołu (mutex) - nie będzie blokady ale to nieefektywne

Semafor zainicjowany wartością N-1 - nie będzie blokady bo nie mogą wszyscy złapać za prawy widelec (rozwiązanie z kelnerem)

Trzeba przeformułować zadanie - wewnątrz sekcji krytycznej tylko operacja up i sprawdzanie wyjątków, bezwarunkowe opuszczenie semafora na końcu sekcji krytycznej (pytanie czy nie zatrzymywać procesu zamiast pytania czy zatrzymać proces) Semafor podnosi się z wyprzedzeniem

Pośredni stan stan hungry między thinking i eating
mutex do organizacji sekcji krytycznej i tablica semaforów (po 1 dla każdego filozofa), inicjowane wartością 0
W sekcji krytycznej ustawia stan na hungry i sprawdza czy może być nie zatrzymany (jeśli może to z wyprzedzeniem podnosi semafor)
Wykonuje down na swoich semaforze (jeśli już może jeść to zaczyna a jeśli nie to się zawiesza)
Odłożenie widelców sprawdza czy sąsiedzi mogą zacząć jeść i podnosi ich semafory jeśli tak

Warunkowe podniesienie semafora z wyprzedzniem i bezwarunkowe opuszczenie poza sekcją krytyczną - wzorzec synchronizacyjny, dobry do wielu problemów

Istotą jest unkikanie wywołania down w sekcji krytycznej

Na egzamin
* synchronizacja w problemie 5 filozofów
* jak poradzić sobie z sytuacją kiedy potencjalnie musimy usypiać proces po sprawdzeniu warunku w sekcji krytycznej

## Problem czytelników i pisarzy
Problem dostępu do rekordu bazy danych

Można rozwiązać przez sekcję krytyczną ale to nie będzie wydajne
Chcemy wzajemnego wykluczania tylko w przypadku konfliktów
Wiele odczytów tego samego rekordu nie powinno się nawzajem blokować

mutex chroni dostęp do licznika czytelników
może wejść wielu czytelników na raz
pisarz może wejść tylko jeśli nie ma czytelników
Jest problem bo odczyty mogą zablokować aktualizację (ale nie będzie blokady)

Można użyć analogicznego mechanizmu żeby blokować nowych czytelników kieyd przychodzi nowy pisarz
semafor r blokuje nowo przychodzących czytelników
tylko 1 czytelnik może zatrzymać się na r (od tego jest semafor m) - statystycznie lepsza szansa że to pisarz zostanie wznowiony
conajwyżej 1 czytelnik może rywalizować z pisarzami