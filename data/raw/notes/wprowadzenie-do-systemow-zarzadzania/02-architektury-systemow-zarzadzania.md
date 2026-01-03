# Architektury informatycznych systemów zarządzania

## Architektura systemu
Architektura systemu to model koncepcyjny, który określa strukturę, zachowanie i pożądane widoki systemu.

Opis architektury to formalny opis i reprezentacja systemu, zorganizowana w sposób, który wspiera rozumowanie dotyczące struktur i zachowań systemu.

Architektura może dotyczyć przedsiębiorstwa, oprogramowania, sprzętu

## Modelowanie architektury ArchiMate
* Warstwa motywacyjna
    * domena analityków biznesowych
* Warstwa strategiczna
	* określenie celów strategiczynch (np. skrócić czas realizacji zamówień przez wdrożenie systemu MRP)
* Warstwa architektury biznesowej
    * opis procesów biznesowych
* Aplikacja
    * mapowanie aplikacji i usług na procesy biznesowe
* Technologie
* Implementacja / migracje


## Wymagania biznesowe
* Enterprise Architect - komercyjny program do modelowania
* Można modelować bardziej skompikowane zależności między wymaganiami
* Proces biznesowy
    * diagram przedstawia relacje między aktywnościami
    * np. wystawienie faktury jest powiązane z określoną aplikacją
    * modeluje powiązanie między aktywnościami a funkcjonalnościami serwisów (mikroserwisów)
    * obszar biznesowy i obszar aplikacyjny (oprogramowanie, które wspomaga obszar biznesowy)


## Widok aplikacji i usług
* HLD - high level design
    * np. będzie wykorzystywana baza danych
    * określa jakie informacje będą przechowywane
* LLD - low level design
    * np. będzie wykorzystywana baza Postgres
    * określone tabele


## Infrastruktura
* Duży problem przy realizowaniu przedsięwzięcia
    * Ile serwerów potrzeba dla rozwiązania on-premise
    * Jakie parametry
    * Jaki software
    * Monolit czy mikroserwisy
* Skomplikowana konfiguracja przy rozwiązaniach chmurowych
    * load balancing
    * bezpieczeństwo
    * logi

## Architektura systemów zarządzania
* Rządzą się tymi samymi prawami co inne systemy informatyczne
* Firmy raczej preferują systemy oparte na sprawdzonych rozwiązaniach, często wykorzystuje się dużo gotowych modułów
* Jest dużo pracy przy konfiguracji gotowców

### Architektury warstwowe
* 3-wastwowa
    * klient
    * serwer
    * baza danych
* 1-warstwowe i 2-wastwowe odchodzą z użycia

### Architektury oparte o chmury obliczeniowe
* Nie wszystkie dane można trzymać w chmurach
* Firmy budują prywatne chmury
* Zalety chmury
    * Początkowe koszty (dyskusyjne)
    * Niezawodność
    * Gotowce
    * Skalowanie
    * Koszty administracji przerzucone na dostawcę chmury

## Odoo
* System ERP
* Open source
* Oparty na PostgreSQL
* Modułowy, łatwy do rozbudowy
* Moduły pisane w Pythonie
* Gotowe moduły i predefiniowane tabele do księgowości, sprzedaży itd.
* Ok dla małych firm

Comarch - komercyjne rozwiązanie na polski rynek


## SAP
* Duże koszty
* Bardzo rozbudowane moduły
* Dostosowane do międzynarodowych firm
    * Wspiera rozliczenia w różnych systemach finansowych itp.
* Bardziej specyficznie przystosowane moduły
    * np. specjalne dla przemysłu chemicznego
* Język ABAP ale są też interfejsy do Javy
* Predefiniowane procesy
* Ustandaryzowana struktura organizacja
    * podział na działy sprzedaży, marketingu itd.


## Architektury mikroserwisowe
* Mikroserwisy są trudniejsze do analizy
