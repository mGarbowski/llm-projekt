# Komputer jednocyklowy (2023-04-12)

## Komputer jednocyklowy
* Układ synchroniczny wykonujący jedną instrukcję w jednym cyklu
* Automat zmieniający stan na końcu instrukcji
* Instrukcja wykonywana przez układ kombinacyjny
* Model programowy klasy RISC
* Musi mieć architekturę typu Harvard - stała pamięć programu typu ROM
* Adresowane całe słowa, nie indywidualne bajty, wymusza wyrównanie naturalne
* Uproszczony RISC-V
* Słowa 32-bitowe

## Budowa

### Licznik instrukcji
* Zawartość licznika instrukcji trafia na wejście pamięci instrukcji i na wejście układu inkrementującego
* Wyjściem inkrementera jest nextPC - zwiększony o 4 (następna instrukcja)
* Aktualna wartość PC też jest potrzebna

### Jednostka sterująca
* Wejścia
  * Opcode
  * funct3
  * funct7
* Wyjścia
  * Sygnał wyboru oepracji ALU
  * Branch - czy instrukcja jest skokiem
  * Load - czy instrukcja jest ładowaniem z pamięci
  * Store - czy instrukcja jest składowaniem do pamięci
  * Imm - czy drugi argument ALU jest stałą natychmiastową a nie rejestrem
  * RegWrite - czy bieżąca instrukcja ma zapisać daną do rejestru
* Układ kombinacyjny
* Może być zrealizowany jako pamięć ROM
* Sygnały functx zawierają kod operacji dla ALU


### Generator stałej
* Wyciąga stałą natychmiastową z instrukcji
* Przyjmuje sygnał Store z jednostki sterującej na wejście - są 2 sposoby zapisu stałej natychmiastowej
* Rozszerzenie bitem znaku


### Blok rejestrów
* Trzy wejścia adresowe
  * rs1
  * rs2
  * rd
* Model w logisimie używa sztuczek

### ALU
* 10 obsługiwanych instrukcji
* Jednostka Control generuje 4-bitowy kod wybierający operację ALU
* Pierwszy argument - zawsze rs1
* Drugi argument - wybierany na podstawie sygnału Imm z jednostki sterującej
  * rs2
  * stała natychmiastowa


### Ładowanie z pamięci
* Tryb adresowania rejestrowy pośredni z przemieszczeniem
  * suma wartości z rejestru bazowego i stałej natychmiastowej (przemieszczenia)
* Adres wyliczany w ALU


### Skoki warunkowe
* Przemieszczenie dodawane do bierzącej wartości PC
* Sumator generuje adres docelowy skoku
* Czy jest skok -> instrukcja jest skokiem warunkowym oraz jest spełniony warunek
* Jeśli jest skok to do PC jest ładowany adres docelowy skoku zamiast zinkrementowanego nextPC


### Wartości generowane w każdym cyklu
* Wartość PC dla następnej instrukcji
* Wartość, która ma być ładowana do rejestru (jeśli coś ma być ładowane)
* Wartość, która ma być składowana do pamięci (jeśli coś ma być składowane)

### Zegar
* do PC
* do rejestrów - bramkowany sygnałem RegWrite żeby nie nadpisać
* do pamięci

## Działanie instrukcji `jalr rd, rs, imm`
* wywołanie procedury
* powrót z procedury

* rd = nextPC
* PC = rs + imm

* Ścieżka danych
* Ścieżka sterowania




## Podsumowanie
* Implementacja jednocyklowa nie jest i nigdy nie była faktycznie konstruowana. Nie jest w stanie spełnić modelu programowego CISC
* Długi łańcuch układów kombinacyjnych
* W ciągu jednego cyklu stan bramki się zmienia i do końca wykonywania instrukcji się nie zmieni (fala na poziomie bramek, bloków)
* Jeśli blok wykona swoją prace, to do końca instrukcji tylko utrzymuje stały stan (do tego służą rejestry)
* Za każdym dużym blokiem ustawia się rejestr na wyjściu
* Wszystkie tkaie rejestry są taktowane tym samym zegarem o odpowiednio krótszym czasie względem jednocyklowego
* Blok może zacząć wykonywać następną instrukcję
* Architektura potokowa