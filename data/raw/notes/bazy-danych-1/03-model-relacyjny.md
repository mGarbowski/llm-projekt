# Relacyjny model danych

## Model relacyjny
* model poziomu logicznego
* Codd, przełom lat 60/70'
* Prosty model teoretyczny i realizacja struktur - podstawowa struktura: realcja/tabela
* Deklaratywne języki zapytań
* Wydajne implementacje
* Normalizacja pozwala uniknąć anomalii


## Postulaty Codda
### Dotyczące struktury danych
* informacyjny - dane są reprezentowane jedynie przez wartości atrybutów w wierszach tabel - nie ma danych domniemanych
* dostępu - każda wartość w bazie jest dostępna przez podanie nazwy tabeli, atrybutu i wartości klucza podstawowego
* fizycznej niezależności danych - niezależne od innych warstw
* logicznej niezależności danych - niezależne od innych warstw
* niezależności lokalizacyjnej (dystrybucyjnej)
* zabezpieczenia przed modyfikacjami przez języki proceduralne - więzy integralnośći utzrymuje SZBD

### Dotyczące przetwarzania danych
* postulat języka danych - ten sam język do definiowania, manipulowania itd.
* modyfikowanie bazy danych przez widoki
* modyfikowanie danych na wysokim poziomie abstrakcji

### Dotyczące integralności danych
* wartości `Null`
* słownika danych
* niezależności ograniczeń
    * klucz podstawowy
    * klucz obcy

Codd matematycznie wykazywał poprawność tego modelu


## Podstawowe elementy
* podstawową strukturą danych jest relacja (tabela)
* operacje to operatory algebry relacyjnej (coś więcej niż operacje na zbiorach)
* więzy integralności są wyrażane przez zależności funkcyjne atrybutów

### Pojęcia
* Dziedziny
* Atrybuty
* Iloczyn kartezjański
* Relacja
* Krotka
* Zależność funkcyjna

### Struktury danych
* Schemat bazy to zbiór schematów relacji
* Schemat relacji to nazwa i zbiór atrybutów (kolumn tabeli)
* Relacja nie ma duplikatów
* Każdy atrybut ma określoną dziedzinę
* Dziedzina jest zbiorem wartości atomowych (bez zbiorów, kolekcji)
* Krotka ma wartość dla każdego atrybutu (może być `Null`, nigdy pusto)
* Klucz - atrybut lub zbiór atrybutów, którego wartość jest unikalna w każdej krotce
* Dla danego schematu relacyjnej bazy danych istnieje zbiór zależności funkcyjnych między atrybutami (wewnątrz relacji i między relacjami)

## Zależności funkcyjne
Atrybut B zależy funkcyjnie od atrybutu A jeżeli wartość A determinuje jednoznacznie wartość atrybutu B, zapisuje się A->B

### Przykłady
* PESEL -> Nazwisko
* PESEL -> Data urodzenia
* IdStudenta, NrPrzedmiotu, Data -> Ocena
* IdStudenta -> Kierunek, Dziekan, Wydział
    * Można to rozbić na 3 różne zależności


## Klucz
* Zestaw atrybutów relacji jednoznacznie identyfikujący każdą krotkę tej relacji
* Każdy atrybut zależy funkcyjnie od klucza
* Relacja może mieć wiele różnych kluczy


### Klucz główny (podstawowy)
* Jednoznacznie identyfikuje rekord
* Wybrany minimalny zestaw atrybutów (nie istnieje inny, który ma mniej atrybutów)
* Relacja może mieć maksymalnie 1 klucz główny
* Unikalny, nie `Null`

### Klucz obcy
* Zbiór atrybutów w danej relacji, który jest jednocześnie kluczem głównym w innej relacji
* Kaskadowe usuwanie
* Określa zależność funkcyjną
* Oznaczenie atrybutu jako klucza obcego jest ważne w praktyce do zachowana apoprawności
* Może być częścią klucza głównego


### Klucz kandydujący
* Jeden z kluczy minimalnych dla danej relacji.
* Jeden z nich to klucz główny
* Potencjalny klucz główny, zależnie od decyzji projektanta
* Może być kilka możliwości np. PESEL i numer indeksu w tabeli studentów

### Klucz pomocniczy
Dowolny klucz wybrany do dalszego wykorzystania w modelu logicznym i fizycznym (przyspieszenia wyszukiwania). Nie musi być unikalny.


### Superklucz
Zbiór atrybutów, których zestaw jest unikalny w całej relacji. Może być redundantny, np. wszystkie atrybuty. Klucz jest minimalnym superkluczem - bez redundantnych atrybutów, żadnego nie można usunąć żeby dalej móc jednoznacznie identyfikować krotki.

### Klucz prosty
Jeden atrybut

### Klucz złożony
Wiele atrybutów


## Normalizacja
* Proces tworzenia schematu, który nie będzie podlegać anomaliom usunięcia, modyfikacji i wstawiania.
* Wyraża zależności funkcyjne przez strukturę bazy.
* Wszystkie zależności powinny być pokryte przez dobór kluczy podstawowych i obcych - nie ma zależności przechodnich



### Postaci normalne
1. Każdy atrybut jest wartością atomową (nie jest kolekcją)
    * w najgorszym wypadku kluczem są wszystkie atrybuty
2. Każdy atrybut niekluczowy jest funkcyjnie zależny od **całego** klucza głównego
3. Każdy atrybut niekluczowy jest **bezpośrednio** zależny funkcyjnie od klucza głównego - nie ma zależności pośrednich

Każda kolejna zakłada spełnienie poprzednich (żeby być w 2NF, relacja musi być w 1NF itd.). Zawsze dąży się do conajmniej 3. postaci normalnej.


## Operowanie danymi
* języki proceduralne (algorytmiczne) - algebra relacji
* języki deklaratywne - rahunek relacyjny 1. rzędu (SQL, QBE)


### Operatory algebry relacji
* Selekcja - wybrór krotek (wierszy)
* Projekcja - wybór atrybutów (kolumn)
* Złączenie
    * iloczyn kartezjański
    * równo-złączenie
    * złączenie naturalne
    * złączenie wewnętrzne
    * złączenie zewnętrzne
* Operatory teorii zbiorów
    * suma
    * przecięcie
    * różnica


Baza relacyjna to operacje na zbiorach