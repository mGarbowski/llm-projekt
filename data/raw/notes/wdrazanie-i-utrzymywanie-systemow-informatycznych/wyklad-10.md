# DevOps (2025-04-24)

## Klasyczne podejście
Development i Operations

Klasycznie - oddzielne procesy
aplikacja powstaje w procesie kaskadowym, ma ustalony zakres, budżet i koniec
operacje - czynności ciągłe, utrzymywanie cały czas przy działaniu, w aplikacji nic się nie zmienia

problemy kulturowe, przy przekazaniu aplikacji z projektu do operacji zaczynają się konflikty, pojawiają się bugi

to jest dobrze znany proces z inżynierii, np. budowlanej

przekazanie do eksploatacji tradycyjnie było bolesne, zespół projektowy musi udowodnić, że dostarczyli to co mieli dostarczyć (protokoły testów, procedury wdrożeniowe, utrzymaniowe, certyfikacje)

rozliczenia związane z odpowiedzialnością
zespół deweloperski ma sprzeczne interesy z zespołem utrzymaniowym

monolityczne aplikacje
kod jest odizolowany od infrastruktury

### Konsekwencje
* Czas produkcji i wdrażania wydłuża się przez procedury przekazania na styku dev i ops
* Nieelastyczne podejście do infrastruktury
* Biurokracja
* Bariery komunikacyjne

### Wyzwania wobec klasycznego podejścia
* Upowszechnienie metodyk zwinnych
	* częste wdrożenia
* Fragmentacja architektury
	* podział na mniejsze aplikacje
	* mikroserwisy
* Popularyzacja chmury
	* wzrost zaufania do chmur publicznych
* Infrastruktura jako kod
* Potrzeby biznesu
	* częste i szybkie zmiany
* Komunikacja zwrotna i ciągłe usprawnianie procesów

## DevOps
* Zmiana paradygmatu
* Nie znikają czynności czysto deweloperskie i czysto utrzymaniowe
* Strefa przejściowa integrująca rozwój z utrzymaniem
	* chcemy żeby była jak najszersza

### Pryncypia DevOps
* Zasady przepływu
	* jeżeli coś zrobimy - deweloper wrzuca kod do repozytorium
	* jak najszybciej efekt pracy powinien być widoczny na produkcji
	* informacja ma płynąć
* Zasady sprzężenia zwrotnego
	* jak coś zrobiłem, powinienem się jak najszybciej dowiedzieć jakie są efekty działania
	* np. feedback od testera
	* np. feedback od klienta - nie musi być wprost, klient korzysta, a ja to widzę (np. przez logi)
	* np. product owner ma wgląd w analitykę i widzi czy jego pomysł się sprawdza
* Zasady ciągłego uczenia i eksperymentowania
	* eksperyment nie zawsze musi się powieść
	* trudna zmiana kulturowo, akceptowanie błędów, przyznawanie się do błędów

Konwersja - zamiana potencjalnego klienta w kupującego (procent)

### Wpływ na efektywność
* W tradycyjnym ujęciu ekonomicznym to stosunek zysku do nakładu
* W IT ważniejszą miarą jest czas reakcji (cycle time)
	* cycle time - ile czasu mija od wyrażenia wymagań do wdrożenia na produkcji
	* można mierzyć i maksymalizować liczbę wdrożeń dziennie
	* im częściej wdrażamy tym krótszy cycle time jesteśmy w stanie osiągnąć
* Jeśli wielkość zespołu rośnie to czas pracy jednego pracownika rośnie
	* więcej komunikacji, więcej wdrażania nowych ludzi itp.
	* przy małej efektywności liczba wdrożeń maleje ze wzrostem liczby pracowników
	* przy średniej efektywności liczba wdrożeń zostaje z grubsza stała przy wzroście liczby pracowników
	* przy skutecznym wdrożeniu procedur DevOps - dużej efektywności liczba wdrożeń rośnie ze wzrostem liczby pracowników

### Struktury w organizacjach

grafika...


#### Nie działające
* Dodatkowy zespół - silos
	* 2 styki zamiast jednego
* Dev nie potrzebuje ops
	* członek zespołu dev
	* w końcu aplikacja i tak trafia do operacji
* DevOps jako narzędzia
	* wdrożenie CI/CD, IaC
* DevOps jako stanowiska zespołu operacji

#### Działające
* Współpraca zespołu deweloperskiego i operacyjnego
	* część ludzi jest w obu sferach
* Ops jako IaaS
	* część infrastruktury jest w naszych rękach, a część w publicznej chmurze
	* devops zajmuje się częścią chmurową i jest częścią zespołu dev
* Tymczasowy zespół DevOps

### Zapewnienie jakości a DevOps
* V-model testów
* Zstępujące
	* wymagania biznesowe
	* architektura (integracja)
	* kod źródłowy
* Wstępujące
	* testy jednostkowe
	* testy integracyjne i systemowe
	* testy akceptacyjne (raczej manualne)
* Jeśli nie przejdziemy testów jednostkowych to nie robimy integracyjnych itp
	* testy jednostkowe są tańsze niż systemowe

## Środowiska wykonawcze
* Deweloperskie
* Testowe / QA
* Preprodukcja
* Produkcja

## CI/CD
* Zapewnia przepływ
* Zapewnia szybki feedback

## Narzędzia
* Przekazywanie wiedzy
	* Confluence
	* GitLab wiki
	* Trello
* Zarządzanie kodem źródłowym
	* Git
* Proces budowania
	* Maven
	* Gradle
	* JUnit
	* Sonar
* CI
	* GitLab CI
	* Jenkins
	* Travis
	* Nexus
* Automatyzacja wdrożenia
	* Terraform
	* Ansible
* Monitoring i logi
	* Nagios
	* Zabbix
	* Prometheus
	* Logstash (ELK)
	* Graylog