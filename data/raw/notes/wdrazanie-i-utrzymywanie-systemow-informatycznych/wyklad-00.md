# 2025-02-28

## Organizacja
* Informacje na kanale Teams
	* slajdy
	* kalendarz
* Laboratoria do de facto projekt
	* nie trzeba być obecnym na miejscu na każdym terminie
	* 3 zadania, na każde 4-5 tygodni
	* na 1 wprowadzającym muszą być wszyscy
	* potem indywidualnie się dogadujemy na oddanie
* Przenosimy wykład na termin w czwartek 18-20
	* wtedy laby w terminie środowym
* 2 kolokwia
	* 11 VI
	* 6 VI
	* termin rezerwowy 13 VI
	* po 30 pkt
* Laby
	* zespoły 4-osobowe
	* 40 pkt w sumie
	* 3 projekty
* Standardowa skala ocen
* Pierwszy lab w ciągu 2 tygodni
	* będzie info na teams

## System Development Life Cycle
* SDLC
* Każdy system podlega cyklowi rozwoju i utrzymania aż do wygaszenia
	* wygaszanie może być równie złożone co cała reszta - zapewnienie obsługi klientów, usług
* Etapy
	* planowanie
	* analiza
	* projektowanie
	* implementacja
	* testowanie i integracja
	* utrzymanie

### Wdrażanie
* Konfiguracja
* Aktywacja mechanizmów bezpieczeństwa
* Testy funkcjonalności
* Przegląd oprogramowania
* Instalacja
* Formalna autoryzacja do eksploatacji
	* związane z przeniesieniem odpowiedzialności na właściciela biznesowego
	* może być bardzo sformalizowana, pisemne dokumenty itp.
	* bardziej miękkie formy (mail z akceptacją)
	* np. na podstawie testów
	* mogą być wymagania żeby zespół testerski jest oddzielony od zespołu deweloperskiego
* Odnosi się zarówno do całego nowego systemu i do każdej poważnej modyfikacji funkcjonalnej działającego systemu
* Rezultaty testów i przeglądów powinny być dokumentowane
	* w praktyce...
* Odpowiedzialność za eksploatację przejmuje właściciel biznesowy
	* jeśli przez działanie systemu dojdzie do naruszenia prawa to on odpowiada

### Utrzymanie
* System jest zainstalowany we właściwej lokalizacji
* Używany operacyjnie
* Ulepszenia i modyfikacje są rozwijanie i testowane
* Elementy sprzętowe i oprogramowania są dodawane lub usuwane
* Organizacja powinna w sposób ciągły monitorować działanie systemu i zapewnić spójność z wymaganiami bezpieczeństwa
	* trzeba reagować na awarie, zapełnienie dysków
	* lepiej monitorować proaktywnie niż tylko reagować po fakcie
	* zarządzanie uprawnieniami administracyjnymi

## System informacyjny
* Oprogramowanie + infrastruktura
	* sprzęt
	* sieci
	* oprogramowanie systemowe
	* maszyny wirtualne
	* kontenery
	* etc.
* Każdy z tych elementów musimy mieć pod kontrolą

## Zadania wdrożeniowe
* Instalacja oprogramowania na infrastrukturze produkcyjnej
	* system operacyjny
	* bazy danych
* Pierwotna konfiguracja infrastruktury
	* systemów operacyjnych (użytkownicy, uprawnienia)
	* sieci (firewall)
	* oprogramowania systemowego (bazy danych, serwery aplikacyjne)
* Zapewnienie aktualnych i odpowiednich licencji na oprogramowanie
	* jak open source to luz ale trzeba wiedzieć jakie to są licencje

## Utrzymanie
* Co to znaczy, że system działa
	* są różne moduły z których korzystają różne grupy użytkowników
* Jak dobrze działa system
	* jakie mamy oczekiwania co do czasów odpowiedzi, liczby obsługiwanych klientów
* Czy system działa zgodnie z oczekiwaniami
	* mamy ustalone wymagania
* Definiuje się ścieżki krytyczne
	* najważniejsze operacje dla których użytkownicy korzystają z systemu
	* jak to działa to można binarnie powiedzieć, że system działa
	* awaria musi być naprawiona tak szybko jak to możliwe

## Zadania utrzymaniowe
* Monitoring stanu aplikacji i infrastruktury
	* z jednej strony powinniśmy gromadzić jak najwięcej faktów i wyciągać z nich wnioski
	* z drugiej strony danych może być za dużo (logi)
	* ważny jest odpowiedni dobór danych i sposobów agregacji
	* na końcu chcemy mieć kilka wskaźników, które mówią czy działa czy nie działa (i czemu?)
* Zapobieganie awariom i wczesne reagowanie na awarie
	* przyczyna nie musi leżeć w tym komponencie, który się wysypał
	* monitoring ma pomóc dotrzeć jak najszybciej do źródła awarii
	* możemy dostrzec niepokojące symptomy zanim się przerodzą w awarię
	* np. kończy się miejsce na dysku
* Instalacja aktualizacja oprogramowania systemowego, dbanie o aktualność
	* możemy przetestować wcześniej na środowisku pre-produkcyjnym (testy regresji)
* Instalacji poprawek do utrzymywanego oprogramowania
	* w ramach utrzymania wdrażamy małe poprawki, a w ramach wdrożenia duże
	* płynna granica
	* bugfix to mała poprawka, nowy feature to duża
* Utrzymywanie aktualnych licencji
* Zapewnienie bezpieczeństwa utrzymywanych systemów
* Administracja kontami systemowymi
* Optymalizacja kosztów finansowych eksploatacji systemów
	* ten sam system, przy takich samych parametrach jakościowych można utrzymać na tańszej infrastrukturze
	* warto benchmarkować

## Architektura z perspektywy wdrażania i utrzymania
* Komponenty oprogramowania
	* moduły
	* mikroserwisy
* Infrastruktura
	* węzły logiczne
	* węzły fizyczne
* Komponenty oprogramowania komunikują się ze sobą
	* między węzłami musi być możliwa ta komunikacja
* Komponenty oprogramowania mapują się na węzły logiczne
* Węzły logiczne mapują się na węzły fizyczne
* Monitoring możemy robić na poziomie oprogramowania, węzłów logicznych, węzłów fizycznych
	* monitorowanie samego oprogramowania może nie wystarczyć

## Typy infrastruktury
* Bare metal
* Maszyna wirtualna
* Kontener
* Serverless computing

### Podział odpowiedzialności
* Enterprise IT / legacy IT
	* wszystkim zarządza klient
	* przepisy mogą tego wymagać
	* przy dużej skali powinno być najtańsze (nie jest oczywiste)
* IaaS
	* klient zarządza stosem od poziomu systemu operacyjnego
* PaaS
	* klient zarządza tylko aplikacją
* SaaS
	* wszystko dostarczone jako usługa
	* klient konfiguruje gotową usługę

## Inne spojrzenie
* W aplikacji jest błąd, gdzie jest przyczyna
	* błąd w kodzie aplikacji
	* runtime (JVM)
	* kontener
	* system operacyjny
	* maszyny wirtualne
	* fizyczne maszyny
* Utrzymanie może wymagać zejścia w niskie poziomy abstrakcji

## Automatyzacja czynności utrzymaniowych
* Automatyzacja wdrożeń i integracji CI/CD
	* styk z rozwojem
* Automatyzacja czynności powtarzalnych
	* backupy
	* rotacja logów
	* czyszczenie dysków
* Automatyczny monitoring i alerty
* Nie wszystko da się zautomatyzować
	* nie wszystko warto automatyzować

## Infrastructure as a code
* Konfigurację infrastruktury zapisujemy w postaci deklaratywnej jako plik
* Zarządzamy podobnie jak kodem źródłowym
* Zapewnia powtarzalność
* Te same praktyki co przy kodzie źródłowym
	* wersjonowanie, code reviews, etc.
* Narzędzia
	* ansible
	* terraform
	* puppet

## Monitoring
* Na różnych poziomach
	* biznesowy aplikacji
	* techniczny aplikacji
	* platformy na której działa aplikacja
	* infrastruktury logicznej i fizycznej
	* sieci

