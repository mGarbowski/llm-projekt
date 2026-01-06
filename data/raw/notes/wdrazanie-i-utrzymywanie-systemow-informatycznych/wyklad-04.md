# 2025-04-03

## Miary bezpieczeństwa
* Najmniej ustandaryzowane, najbardziej nieuchwytne pod względem metryk
* Podatność to coś co istnieje w systemie
	* może zostać użyta do naruszenia bezpieczeństwa

* Liczba podatności bezpieczeństwa
* Czas istnienia podatności od wykrycia do usunięcia
* Pokrycie procentowe testami bezpieczeństwa
	* np. testy penetracyjne
* Procent słabych / mocnych haseł użytkowników
	* jedno słabe hasło to problem użytkownika
	* wiele słabych haseł w systemie to nasz problem
* Powierzchnia ataku
	* na ile różnych sposobów system może zostać zaatakowany
	* np. liczba publicznych interfejsów
* Liczba wykrytych ataków

## Service Level Agreement (SLA)
* Porozumienie między usługodawcą i usługobiorcą określające poziom i warunki świadczonych usług
* Składniki
	* dokładny opis świadczonych usług
	* określenie minimalnego czasu dostępności usługi / systemu
	* czas reakcji
	* czas rozwiązania problemu
	* procedura zgłaszania awarii
	* monitorowanie i raportowanie działań
	* konsekwencje niewypełnienia umowy
* Czas reakcji i rozwiązania ustala się w zależności od stopnia istotności
* Monitorowanie
	* z jaką częstotliwością
	* jakimi narzędziami
* Między dużymi podmiotami to może mieć formę spisanego dokumentu
	* mniej formalna postać jeśli to porozumienie między 2 działami tej samej firmy

### Wielowarstwowe SLA
* Aplikacja w chmurze publicznej
	* klient eksploatujący aplikację
	* zespół dostarczający i utrzymujący aplikację
	* dostawca publicznej chmury
* Nie ma możliwości utrzymywania jeśli będzie awaria samej chmury
* SLA między klientem i dostawcą usługi odwołuje się do SLA dostawcy i dostawcy chmury
* W Azure SLA są zdefiniowane osobno dla różnych usług
	* są dodatkowo płatne wersje premium SLA

## Narzędzia monitorowania bieżącego systemów IT
* Zabbix
* Splunk
* Prometheus/Grafana
* Co robią
	* agregacja logów
	* wyliczanie metryk

### Zbieranie i agregacja logów z działających systemów
* ELK stack
	* Elastic
	* Logstash
	* Kibana
	* Filebeat
* Aplikacja jest wdrożona w postaci wielu mikroserwisów w kontenerach
	* każdy mikroserwis generuje logi i zapisuje je do systemu plików kontenera
	* coś poszło nie tak i chcemy wyjaśnić co się stało
	* trzeba przejrzeć logi każdego kontenera
	* niepraktyczne
* Wszystkie logi powinno się gromadzić w jednym miejscu
* W każdym mikroserwisie gromadzi się logi
	* np. jeden proces który czyta pliki logów
	* jeśli wykryje nową linię logu, wysyła request do Logstash
* Logstash
	* przetwarzanie, czyszczenie
	* dodaje metadane
	* np. przekształcenie daty do jednolitego formatu
	* po przetworzeniu przesyła do bazy danych (Elastic)
* Elasticsearch
	* baza danych noSQL
	* szybkie wyszukiwanie pełnotekstowe
* Kibana
	* wizualizacja zbioru danych z elasticsearch
	* interfejs do wysyłania zapytań do Elasticsearch
* Z logów można wyciągnąć np. czas odpowiedzi systemu
* Alerty
	* zapytanie do bazy z binarną odpowiedzią
	* czy w ciągu ostatniej godziny czas odpowiedzi przekroczył x
	* jeśli tak, to jest wyzwalany alert
	* mail, wiadomość na komunikator, sms - ludzie zaczną je ignorować
	* czułość alertów raczej ustala się metodą prób i błędów
	* alertów powinno być stosunkowo niedużo i nie generować false positive
* Root cause analysis
	* dojście do źródła problemu - gdzie faktycznie zaczęła się awaria
	* pozwala znaleźć kolejny punkt, w którym należy ustalić alert
	* stopniowe usprawnianie systemu

## Obserwowalność
* Miara jak dobrze jesteśmy w stanie poznać wewnętrzny stan systemu na podstawie znajomość zewnętrznych wyjść systemu
	* z teorii sterowania
* Logi - wysokopoziomowa obserwowalność
	* co jak przestaną przychodzić logi
* Każde narzędzie ujawnia jakieś informacje
	* OS, Docker, JVM

### Obserwowalność na poziomie systemu operacyjnego
* `top`, `ps` - stan procesorów i procesów
	* Load average - długość kolejki zadań
	* jak nagle wzrośnie to wiadomo że coś jest nie tak
* `free` - pamięć
* `du` - zajętość dysku
* `ifconfig` - interfejsy sieciowe
* `nload` - stan użycia sieci
* `netstat`

### Logi systemu operacyjnego
* syslog
* authlog
* boot.log
* kern
* dmesg - sterowniki
* logi aplikacji
	* /var/log/mysqld.log

### Obserwowalność w Dockerze
* `docker stats`
* `docker inspect`

### Obserwowalność w JVM
* JMX - Java Management Extension
* Informacje o stanie maszyny wirtualnej
	* ile wątków
	* aktywność garbage collectora

### Obserwowalność na poziomie aplikacji
* Instrumentacja, jakaś biblioteka
* Np. dodatkowy endpoint
* Spring Actuator
* Tutaj można definiować metryki biznesowe
	* np. liczba zamówień

### Inne poziomy
* System działa w szerszym kontekście niż sama aplikacja webowa
* Należy monitorować np. sieć korporacyjną

# CI/CD

## Proces wytwarzania oprogramowania
* Etapy
	* projektowanie / analiza
	* implementacja
	* inspekcja kodu
	* testy jednostkowe
	* kompilacja / budowanie
	* wdrożenie na środowiska wykonawcze
	* testy integracyjne na tych środowiskach
* Dwa pierwsze kroki przynoszą wartość biznesową, a pozostałe to koszt inżynierii oprogramowania
* Zgodnie z tradycyjnym rozumieniem ekonomii trzeba by ograniczać etapy 3-7 wykonując je jak najrzadziej
	* w IT to się nie sprawdza
	* chcemy nie najefektywniej (najwięcej czasu w etapach 1-2 w stosunku do 3-7), a najszybciej (przejście od 1 do 7)
* Długie cykle wdrożeniowe
	* wymagania się zmienią
	* rynek się zmieni
	* klient zamówił co innego niż dostał
	* rośnie złożoność każdej czynności i to nie liniowo

## Proces ciągłej integracji / wdrażania / dostarczania
* Róbmy małe paczki
* Jak najczęściej przechodzimy przez pełny cykl
* Etapy 3-7 są wykonywane często
	* nie można ich robić ręcznie
	* trzeba je zautomatyzować
* CI - Continuous Integration
	* ciągła integracja nowego kodu z istniejącym kodem
* CD - Continuous Delivery
	* ciągle dostarczane gotowe oprogramowanie do wdrożenia
	* zawiera w sobie CI
	* wdrożenie jest *na przycisk*, wszystko jest przygotowane
* CD - Continuous Deployment
	* ciągłe wdrażanie na środowisko (w skrajnym wypadku na produkcję)
	* zawiera w sobie Continuous Delivery
	* wdrożenie idzie automatycznie

## Środowisko wykonawcze
* Część lub całość systemu
* Przeznaczona do wykonywania określonych czynności procesu wytwarzania oprogramowania
* Np. środowisko deweloperskie
	* celem jest wspieranie rozwoju oprogramowania
* Np. środowisko testowe
	* celem jest przeprowadzenie testów
* Np. środowisko produkcyjne
	* celem jest świadczenie usługi klientom

## Development pipeline
* Szereg czynności wykonywanych w celu dostarczenia nowej wersji oprogramowania
* Narzędzia CI/CD wspierają tworzenie pipeline'ów i ich wykonywanie

## Narzędzia CI/CD
* Jenkins
	* wykonywanie może być rozproszone na wiele węzłów
	* operacje wykonują się w kontenerach
* GitLab CI
* TeamCity
* CircleCI
* Azure Devops

Na kolokwium troche pytań testowych i 2 pytania otwarte
To co na wykładach i na slajdach