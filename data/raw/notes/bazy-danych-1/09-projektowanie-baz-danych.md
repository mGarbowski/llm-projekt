# Analizowanie, projektowanie i wdrażanie baz danych

## Metodologia wdrażania
* wodospadowe - długie etapy: projektowania, analizy, implementacji, wdrożenia itd. po kolei
* iteracyjne - więcej mniejszych wodospadów
* zwinne

## Metodyka wodospadowa
* Zbieranie wymagań
  * Przypadki użycia - podstawa do tworzenia testów
  * Dokumentacja
* Projektowanie
  * Architektura oprogramowania
  * Mapowanie interesariuszy
* Implementacja
  * Wytwarzanie oprogramowania
  * Składowanie danych
* Weryfikacja
  * Instalacja
  * Testowanie
  * Debuggowanie
* Utrzymywanie
  * Naprawianie błędów
  * Optymalizacja

Jest dobry przy znanej technologii i wymaganiach

### Wady metodyki wodospadowej
* Błędy na początkowych etapach projektu kumulują się i generują duże koszty na późniejszych
* Zmiana wymagań klienta wymaga cofnięcia do początku
* Etapy trwają zbyt długo


## Metodyka iteracyjna
* Wiele wodospadów - 1 wodospad - 1 iteracja
* Etapy są krótsze więc nie ma tragedii kiedy kumulują się błędy

### Wady
* Mnożą się koszty stałe
* Nie można zrobić od razu wszystkiego
* Nie zarządzanie architekturą w całości na raz generuje problemy


## Metodyka Scrum
* Wariant agile
* Retrospektywy
* Product backlog
* Sprint backlog

### Wady
* Różne spojrzenie na architekturę przez różne zespoły
* Problem z zarządzaniem dokumentacją



## Poziom koncepcyjny
* słownik pojęć dziedziny
* model pojęiowy (koncepcyjny)
  * rodzaje encji
  * rodzaje związków
  * rodzaje więzów integralności
* diagramy ER
* cykle życia ancji
* weryfikacje
  * redundancje
  * więzy integralności

## Poziom logiczny
* Transormacja z modelu pojęciowego
* Normalizacja
* Scalenie perspektyw
* Zapewnienie pożądanych cech
  * brak redundancji
  * elastyczność
  * spójność (przestrzeganie więzów integralności)
  * transakcyjność
  * złożone typy danych

## Poziom fizyczny
* Transormacja z modelu fizycznego
* Wykorzystanie możliwości DBMS
* Projektowanie reprezentacji fizycznej
* Optymalizacja wydajności (denormalizacja, indeksy)
* Projektowanie perspektyw użytkowników
* Projektowanie mechanizmów bezpieczeństwa
* Monitorowanie i dostrajanie systemu
