# Projektowanie i programowanie (2024-03-18)
* Reguły SOLID itd poprawiają utrzymywalność programu ale nie zapewniają jego poprawności
* Poprawność zapewniają tylko testy

## Test-Driven Development
* Jak ktoś powie że test-driven development to technika testowania, przy której najpierw pisze się testy to uwala egzamin dyplomowy
* Używanie testów nie tylko do weryfikacji procesu wytwarzania oprogramowania, ale do sterowania nim
* Kiedy znajdzie się buga to najpierw należy napisać test, który go wykrywa
* Testy prowadzą przez rozwiązanie problemu
* Proces TDD
    * Minimalny nieprzechodzący test
    * Minimalna implementacja, która sprawi, że test przejdzie
    * Refaktoryzacja

### 3 zasady TDD
* Pisać kod produkcyjny tylko po to, żeby naprawić nieprzechodzący test
* Pisać nie więcej testu, niż wystarczy żeby test nie przeszedł
* Pisać nie więcej kodu, niż potrzeba, żeby naprawić ten test


TDD zapewnia pokrycie testami - bo każda linijka musiała być poprzedzona testem

## Projekt
* Projekt to wszystko po drodze do rzeczywistego produktu
* Kod (też) jest projektem aplikacji
* Nie ma tak, że mądry analityk/projektant zaprojektuje, głupi programista wykona i jest gotowy produkt
* Proces inżynieryjny
    * Projekt wykonywany przez analityków i projektantów rozumiejących domenę klienta
    * Projekt szczegółowy wykonywany przez programistów rozumiejących dobrze technologię
    * Produkt przechodzi walidację (przez testerów i klienta)
    * Powstaje produkt

## Projekt i kod
* Kod nie jest idealny do demonstrowania architektury
* Architektura musi być widoczna w kodzie
    * np. struktura katalogów odzwierciedla jakieś diagramy
* Szczegółowe diagramy mają sens tylko jeśli stają się plikami źródłowymi

## Git
* Wersja to migawka wszystkich plików naraz
* Nie ma centralnego serwera, każda stacja robocza ma pełną kopię repozytorium z całą historią zmian
* Większość operacji odbywa się lokalnie, offline
* Obiekty są dodawane do repozytorium ale nie są usuwane (da się ale na ogół się nic nie usuwa)

