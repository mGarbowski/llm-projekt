# 2025-03-27

## Automatyzacja konfiguracji - Infrastructure as a Code
* Stare podejście - źródłem prawdy o infrastrukturze jest sama infrastruktura
	* serwer i to co na nim chodzi
* Podejście infrastructure as a code
	* źródłem prawdy jest opis deklaratywny
	* mówi jak infrastruktura powinna wyglądać
	* jeśli coś się nie zgadza z oczekiwanym stanem, to automatyczne narzędzie może to poprawić
* Z konfiguracją pracuje się tak jak z kodem źródłowym
	* repozytorium
	* modularność, reużywalne fragmenty
* Konfiguracja aplikowana przez
	* centralny węzeł konfiguracyjny - konfiguracja bezagentowa
	* agenty uruchomione na konfigurowanych elementach - konfiguracja agentowa
* Można konfigurować
	* sieć, interfejsy, routing, firewalle
	* oprogramowanie systemowe
## Przykładowe narzędzia
* Puppet (agentowy)
* Chef (agentowy)
* Ansible (bezagentowy)
* Terraform (agentowy)

## Ansible
### Architektura Ansible
* Węzeł centralny
	* inventory - lista węzłów
* Łączy się z węzłami przez SSH
* Wymaga połączenia sieciowego do węzłów
* Inventory
	* plik yaml
	* struktura drzewiasta
	* można definiować zmienne

### Ansible playbook
* Wbudowane moduły (ok, 1000)
	* ping
	* command/shell - wykonanie polecenia shella
	* apt/npm/pip/pkg - managery pakietów
	* git - operacje na repozytorium
	* mysql_db/postgres_db - zarządzanie bazą danych
	* cron - sterowanie zadaniami crona
	* moduły do zarządzanie interfejsami sieciowymi, firewallem, routingiem
	* azure/gcp/aws - operacja na infrastrukturze chmury publicznej
* `become` - polecenia są wykonywane jako root
* Zadania
	* nazwa
	* komenda i parametry
* `reset_connection`
	* można w ten sposób załadować informację o zmianie grupy
	* można nadpisać `become`
* Domyślne działanie
	* zadania wykonują się po kolei, dopiero jak poprzednie się skończy (można wykonywać równolegle)
	* playbook jest wykonywany równolegle na wszystkich węzłach

## Terraform
* Narzędzie IaC
* Do konfigurowania infrastruktury usług chmurowych
* Agentowy, za faktycznych agentów odpowiadają dostawcy chmury
	* udostępniają biblioteki rozszerzające `providers`

### Architektura
* Proces terraform
* Dostarczamy plik konfiguracyjny opisujący porządany stan
* Proces zachowuje lokalnie stan infrastruktury
	* plik .tfstate
* AWS, Azure itp dostarczają providerów, z którymi komunikuje się proces Terraform

### Proces zarządzania infrastrukturą
* Administrator przygotowuje pliki
* Plan
	* powstanie planu - szeregu poleceń potrzebnego do dostosowania infrastruktury do opisu
	* plan też jest plikiem
* Aplikacja planu
* Rozdzielenie planowania od aplikowania
	* odpowiedzialności mogą być rozdzielone

### Pliki
* `providers.tf`
	* plik konfiguracji biblioteki rozszerzającej do Azure
* `variables.tf`
	* zmienne konfiguracyjne
* `output.tf`
	* zmienne wyjściowe
	* niektóre wartości są zwrócone w kroku apply
	* np. adres IP utworzonej maszyny wirtualnej
* `main.tf`
	* zasadniczy plik konfiguracyjny
	* można w ramach tego pliku nazywać zasoby i odwoływać się do ich atrybutów
* `*.tfstate`
	* plik modyfikowany automatycznie przez terraform
	* stan infrastruktury po zaaplikowaniu
	* zawiera poufne dane - plik musi być chroniony
	* nie dodawać do gita
* `*.tfplan`
	* plan wykonania
	* można go udostępniać, wielokrotnie wykonywać

Za tydzień jeszcze Ratkowski, a potem Zalewski

# Dostępność, wydajność, bezpieczeństwo i monitoring

## Jakość oprogramowania zgodnie z ISO/IEC 25010
* Oprogramowanie dobrze działa jeśli spełnia normy jakości
* Jakość - poziom z jakim system może być użyty przez określonych użytkowników, aby spełnić ich potrzeby w osiągnięciu okreśłonych celów w określonym kontekście użycia

### Kategorie jakości
* Stosowność funkcjonalna
	* na ile system spełnia wymagania funkcjonalne
	* kompletne
	* poprawne
	* właściwe
* Efektywność wydajnościowa
	* czasowa charakterystyka
	* wykorzystanie zasobów
	* pojemności
* Kompatybilność
	* umiejętność współpracy z innymi systemami
	* kompatybilność ze standardami
* Użytkowalność, ergonomia
	* możliwość uczenia się przez użytkownika
	* ochrona przez błędami czynionymi przez użytkowników
	* dostępność
* Niezawodność
	* dojrzałość - przetestowanie na różne sytuacje
	* dostępność
	* odporność na błędy
	* odtwarzalność (po krytycznych błędach)
* Bezpieczeństwo
	* poufność
	* integralnośc danych
	* możliwość audytowania
* Utrzymywalność
	* modularność
	* reużywalność
	* analizowalność
	* modyfikowalność
	* testowalność
* Przenośność
	* możliwość instalowania w różnych środowiskach, systemach operacyjnych, frameworkach

Niektóre są bardziej w sferze projektowania
W sferze utrzymania najbardziej na niezawodność, wydajność i bezpieczeństwo

### Miary niezawodności
* Procent czasu działania (rocznie/miesięcznie/dziennie)
	* 99%
	* 99.99% - 52 minuty w skali roku, w ciągu dnia - lipa
	* może być zliczany przez próbkowanie
	* negocjacja między tym kto to zapewnia, a tym kto za to płaci
	* może wynikać z awarii
	* może wynikać z nieuniknionych czynności utrzymaniowych
	* gwarancja polega na tym, że dostawca płaci jeśli przekroczy ten procent
* Liczba zgłoszonych awarii
	* odczuwalna przez użytkownika
* Liczba wykrytych defektów w określonym czasie
	* nie musi być odczuwalna przez użytkownika
	* może doprowadzić do awarii ale nie musi
* Czas odtworzenia po krytycznej awarii

### Miary wydajności
* Średni czas odpowiedzi
	* co to dokładnie znaczy
* maksymalny czas odpowiedzi dla określonego percentyla
	* np. nie więcej niż 5s dla percentyla 95%
	* centralne twierdzenie graniczne - zmienna losowa, która jest sumą wielu zmiennych losowych to rozkład dąży do rozkładu normalnego
	* rozkład log-normalny
	* nie jest normalny bo jest ograniczony od 0
	* długi ogon - trzeba uważać, 95% będzie sporo większy od średniej, średnia będzie mniejsza od mediany
* Maksymalna przepustowość
	* liczba obsługiwanych klientów, zdarzeń itp.
	* krzywa średniego czasu odpowiedzi od ruchu - rośnie aż do momentu załamania
	* średni czas odpowiedzi określa się przy określonym ruchu
* Zasoby obliczeniowe potrzebne do obsłużenia określonego ruchu
	* liczba CPU
	* pamięć
	* zasoby z publicznej chmury
	* wydatki na publiczną chmurę