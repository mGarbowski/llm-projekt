# 2025-03-06

## Monitoring c.d.
* Potrzebny jest monitoring na każdym poziomie technicznym
* Monitoring biznesowy
	* np. jeśli nagle spada liczba zakupów w sklepie to może coś się technicznie wysypało
* Logi
	* zbyt dużo logów to też problem
	* co jak zawierają tajne dane i ktoś się do nich dobierze

## Testowanie
* Co do zasady jest częścią rozwoju ale pojawia się też na styku z utrzymaniem
	* np. przy wdrożeniu nowej wersji
* Testy jednostkowe
* Testy integracyjne
* Testy akceptacyjne
* W odpowiedzialności utrzymującego jest upewnienie się, że testy przechodzą

## Dokumentacja
* Jest niezbędna w utrzymaniu
* Tworzenie dokumentacji wymaga dużego nakładu pracy
	* często się ją pomija, lepiej robić feature'y, poprawiać bugi
* Ma pokazywać czym jest system, jak działa, jaką ma architekturę, jakie ma kluczowe cechy
* Architektura w różnych widokach
	* procesy biznesowe
	* komponenty aplikacyjne
	* komponenty logiczne i ich relacje
	* komponenty fizyczne i ich relacje
* Procedury utrzymaniowe
	* wdrożenia
	* czynności serwisowe (np. czyszczenie logów, danych historycznych)
* Metryki i punkty pomiaru
* Procedury eskalacji

## Bezpieczeństwo
* Każda, nawet najbardziej banalna aplikacja jest warta zaatakowania dla kogoś na świecie
* OWASP - zalecenia bezpieczeństwa dla aplikacji webowych

## DevOps
* Zaciera się podział na rozwój i utrzymanie
* DevOps to kultura organizacyjna, która opiera się na założeniu że development jest nierozerwalnie związany z operations
* Kultura DevOps może być w różny sposób interpretowana i implementowana

## Procesy zarządzania systemami IT
* Jak zarządzać usługami IT
* ITIL
* COBIT
* DevOps

## Zarządzanie konfiguracją
* Zbiór danych opisujący całą infrastrukturę
* ...

## Pozostałe zagadnienia
* Dług techniczny a utrzymanie
* Wpływ transformacji cyfrowej na utrzymanie
* Zarządzanie licencjami
* Utrzymanie urządzeń końcowych użytkowników (laptopy, smartfony firmowe, itd.)

# Infrastruktura, automatyzacja infrastruktury produkcyjnej

## Bare metal
* Oprogramowanie działające bezpośrednio na fizycznych serwerach
* Węzeł fizyczny = węzeł logiczny
* Dodawanie nowych węzłów wymaga instalacji nowego sprzętu
* Najbardziej efektywne wykorzystanie zasobów
	* bez warstw pośredniczących
* Komponenty oprogramowania zainstalowane bezpośrednio na systemie operacyjnym
* Mała elastyczność
* Serwerownia może być dedykowanym pomieszczeniem (w piwnicy?)
	* odpowiednio duża, może być dedykowanym budynkiem (data center)
	* alternatywne sposoby zasilania
	* agregat prądotwórczy do zasilania awaryjnego, akumulatory na czas rozruchu agregatu
	* komora z podwójnymi ścianami wypełnionymi piaskiem - wytrzyma kilka godzin podczas pożaru

### Architektura aplikacji bare metal
* Sprzęt fizyczny
* System operacyjny
* Zbiór aplikacji

## Powtórka z systemów operacyjnych
* User space
	* aplikacje
	* manager okienek
	* biblioteki
* Linux kernel
	* interfejs (wywołania systemowe)
	* zarządzanie procesami
	* IPC
	* wirtualny system plików
	* zarządzanie pamięcią
	* sieć
	* SELinux/AppArmor
	* sterowniki i moduły dynamiczne
	* kod zależny od architektury fizycznej
* Hardware
	* architektura procesora
* Przy eksploatacji aplikacji mamy niedużo do czynienia z samym systemem operacyjnym

## Maszyna wirtualna
* Wiele systemów operacyjnych na jednym węźle fizycznym
* Zasoby sprzętowe są udostępniane systemom gościom przez hypervisora
* Systemy goście nie są świadome że działają na maszynie wirtualnej
	* można się tego dowiedzieć (np. flagi w `lscpu`)
* Współczesne procesory mają wsparcie dla wirtualizacji
	* dzięki temu wirtualizacja powoduje nieduży narzut wydajnościowy
* Dodatkowe warstwy pośrednie między aplikacją a sprzętem
	* hypervisor i system gość
* Zapewnia separację między aplikacjami
* Maszyny wirtualne mają przypisane zasoby przez hypervisora
	* nienaruszalne
* Maszyny wirtualne są widoczne jako oddzielne hosty w sieci
* Powołanie nowego wirtualnego serwera jest bardzo proste i szybkie
	* musimy mieć wcześniej przygotowany sprzęt

### Hypervisor typu 1 i 2
* Typ 2
	* hypervisor uruchomiony na systemie operacyjnym hosta
	* np. VirtualBox
* Typ 1
	* nie ma systemu operacyjnego pod spodem
	* sam hypervisor jest szczątkowym systemem operacyjnym
	* obsługuje podział zasobów
	* w usługach chmurowych

## JVM
* Środowisko wykonawcze dla aplikacji javowych
* To co innego niż maszyna wirtualna
* Program w javie jest kompilowany do bajtkodu
* Bajtkod jest interpretowany przez JVM
* Kolejna warstwa pośrednicząca między aplikacją, a systemem operacyjnym
* Ciekawe zjawiska związane np. z buforowaniem

### Budowa
* Class loader
	* ładuje skompilowany kod do pamięci
* Pamięć środowiska
	* wygląda jak przestrzeń pamięci procesu w systemie operacyjnym
	* stos
	* stos metod natywnych - np. otwórz plik (API systemu operacyjnego)
	* ...
* Execution engine
	* udaje procesor
	* JIT compiler
* Native Method Interface (JNI)
* Native Method Library

Laboratorium w przyszłym tygodniu - organizacyjne