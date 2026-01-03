# NoSQL

## Klucz-wartość
* Tak naprawdę bardziej złożone niż prosta tablica asocjacyjna
* Klucz może być złożony
* Wartość może być bardzo różnego typu (różne struktury danych)
* Schemat danych w budowie klucza, tworzenie przestrzeni nazw
* emulacja tabel po stronie klucza lub po stronie wartości


## Dokumentowe
* dokumenty (json, xml, ...)
* zamiast pośrednich tabel jak w relacjach many-to-many jest zagnieżdżanie dokumentów
* można zagnieżdżać wszystko a można minimalnie trzymać tylko odnośniki
* optymalizacja odczytu vs zapisu
* używane w
  * CMS
  * e-commerce
  * mediach społecznościowych
  * grach
  * logowaniu i analizie
  * biurokracji
  * służbie zdrowia
  * podróżach


## Kolumnowe
* weiele zapytań (o sume, średnią, maksimum) operuje tylko na jednej (małej liczbie) kolumn
* działa wolno kiedy zapytanie operuje na wielu kolumnach (rekord po rekordzie)
* i tak istnieje pojęcie rekordów
* przy pytaniu o rekord trzeba poskładać dane z wszystkich kolumn
* rodziny kolumn
* przestrzeń kluczy - agregaty obszarowe
* zastosowania
  * monitorowanie i analiza danych z maszyn
  * aplikacje finansowe
  * aplikacje geolokalizacyjne
  * iot
  * gry
  * analiza w czasie rzeczywistym


## Grafowe
* Używane tam gdzie rzeczywistość modeluje się grafami
* węzły i krawędzie, ścieżki, pętle
* operacje i pojęcia typowe dla teorii grafów
* zapytania wyrażane jako ścieżki, przepływy itp


## Rozproszone bazy danych
* dane są przechowywane w różnych fizycznych lokacjach
* dane się nie pokrywają

### Twierdzenie CAP
* Consistency - spójność
* Availability - dostępność
* Partition tolerance - odporność na podział

Nie można mieć 3 na raz


## Kolokwium
* to co na pierwszym
* postaci normalne
* harmonogramy tansakcji, szeregowalne, nieszeregowalne
