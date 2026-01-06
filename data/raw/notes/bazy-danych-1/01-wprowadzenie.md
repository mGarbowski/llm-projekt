# Wprowadzenie do baz danych

## Pojęcia
* Dane - fakty, reprezentują zdarzenia
* Informacje - dane umieszczone w kontekście nadającym im znaczenie
    * te same dane, w różnych kontekstach mogą oznaczać co innego
* Wiedza - informacje osadzone w szerszym kontekście syntaktycznym, semantycznym i pragmatycznym
* Decyzje - czynności podejmowane w kontekście informacji aby zrealizować cele


## Baza danych zapewnia
* trwałość danych
* oddzielenie definicji danych od danych
    * dostosowanie sposobu przechowywania do danych
* wielość widoków na dane
* różne poziomy abstrakcji
* niezależność danych od aplikacji

## Model danych
Specyfikacja reguł definiujących

* strukturę danych
* dozwolone operacje
* więzy integralności

## Baza danych
Zbiór danych / faktów przechowywanych zgodnie z określonym modelem danych

## System zarządzania bazą danych
Program komputerowy wyspecjalizowany do gromadzenia i przetwarzania danych

## System bazy danych
Cały ekosystem, system zarządzania bazą danych, modelem danych, językiem komunikowania się, modelem obliczeniowym


## Tok modelowania
1. Świat rzeczywisty
2. Model koncepcyjny - projekt związków encji, diagramy ER
    * abstrakcyjny model świata rzeczywistego
    * niezależny od szczegółów implementacyjnych
    * opisuje elementy świata rzeczywistego podlegające odwzorowaniu w bazie
3. Model logiczny - schemat relacyjny
    * Odwzorowuje elementy z modelu koncepcyjnego w struktury odpowiednie dla danego modelu logicznego (np. relacje)
    * Tutaj wybiera się system relacyjny / dokumentowy itp
4. Model fizyczny - system zarządzania bazą danych
    * Efektywnie realizuje wybrany model logiczny

Ważne jest stworzenie spójnego modelu, do tych samych zbiorów danych mogą mieć dostęp różne grupy użytkowników

Model pozwala opisać problem ze świata rzeczywistego w języku zrozumiałym przez różne zainteresowane grupy (programiści, architekci, użytkownicy, osoby nietechniczne).

Zdefiniowanie scenariuszy użycia, na podstawie historyjek można napisać testy.

Opis w nie w pełni formalnym języku nie jest modelem danych.

### Model E/R
Entity Relationship, najpopularniejszy model koncepcyjny, zawiera

* encje
* relacje (związki)
* atrybuty
* więzy integralności


### Logiczne modele danych
* Klasyczne
    * hierarchiczny - drzewa
    * sieciowy
    * relacyjny - tabele
* obiektowy
* dedukcyjny - możliwość wnioskowania na podstawie danych
* post-relacyjny - rozszerzenia modelu relacyjnego
* XML (dokumentowy)
* grafowy


### Fizyczny model danych
Określa takie aspekty jak

* fizyczne struktury danych
    * fizyczna reprezentacja nie musi być taka sama jak logiczna - nie będzie odwzorowania tabel 1-1
    * musi zapewniać jak najlepszą wydajność
* indeksy - przyspieszenie wyszukiwania
* klastry - rozproszone bazy danych
* zapewnianie więzów integralności
* metadane
* zarządzanie wielodostępem - obsługa transakcji, unikanie deadlocku
* zarządzanie wydajnością
    * zachowanie spójności bez blokowania całej bazy
* bezpieczeństwo danych
* użytkownicy i role


## System zarządzania bazą danych (DBMS)
### Podstawowe własności
* przechowywanie danych zgodnych z określonym modelem danych
* operacje CRUD
* definiowanie schematu bazy danych
* definiowanie więzów integralności
* wykonywanie zapytań
* wykonywanie raportów i zestawień

### Oferują
* przechowywanie
* trwałość
* niezawodność
* replikacje
* mirroring
* klastrowanie
* spójność
* transakcje
* backupy
* konfigurowalność
* bezpieczeństwo
* poufność
* odtworzenia


## Użytkownicy bazy danych
* użytkownicy końcowi
* użytkownicy końcowi zaawansowani
* analitycy biznesowi
* analitycy danych
* projektanci, architekci bazy danych
* architekci technologiczni
* programiści baz danych
* testerzy
* administratorzy baz danych