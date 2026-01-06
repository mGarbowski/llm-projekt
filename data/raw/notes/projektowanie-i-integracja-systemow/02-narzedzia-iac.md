# Narzędzia, Infrastructure as code
## Zarządzanie zadaniami
* Najważniejsze żeby były w jednym miejscu
* Narzędzie do kontrolowania pracowników
	* monitorowanie poświęconego czasu
	* przydatne do planowania, szacowania czasu na przyszłość itp

### Narzędzia
* JIRA
	* de facto standard na rynku
	* darmowa licencja do 10 użytkowników
	* duży koszt komercyjnych licencji
* Asana
* Redmine
* Trello

## Zarządzanie dokumentacją
* Narzędzia
	* Confluence - zintegrowany z Jirą
	* SharePoint
	* MediaWiki - silnik wikipedii
	* GitHub - moduł wiki
* Zależy od struktury organizacji
* Narzędzia są wtórne do projektu, dostosowujemy narzędzia do problemu
* Dokumentację pisze się kiedy ktoś każe to zrobić
* Dokumentacja przestaje być aktualna w momencie opublikowania
* Najlepszą dokumentacją kodu jest sam kod
* Dokumentowanie publicznego API jest bardzo istotne
	* dokumentowanie usługi

## Git
* Metody zarządzania branchami
	* feature branches
	* trunk based development
	* git flow
* Nie warto zabijać projektu przez narzucanie skomplikowanych reguł
	* dostosowujemy do problemu
	* zależy od skali projektu
* Warto utrzymywać stan głównej gałęzi, który może wejść na produkcję
	* nie ważne co, kod na masterze nie może zabić produkcji
	* można używać feature switches - ogranicza się liczbę branchy i upraszcza deployment
* Branch, który żyje długo będzie sprawiać problemy
	* szybko może się rozjechać z masterem

### Platformy
* GitHub
* GitLab
* Bitbucket
* Samodzielnie hostowane

### GitFlow
* Main (master)
	* kod produkcyjny
* Develop
	* główna gałąź rozwojowa
	* tu programiści wrzucają zmiany
* Hotfix
	* jak coś się posypie na produkcji
	* wychodzi z mastera
	* doraźna poprawka
	* merge'owana do mastera i wdrożona
	* musi być też zmerge'owane do develop - bardzo ważne
* Release
	* stabilny stan gałęzi develop
	* już bez zmian funkcjonalnych, tylko bugfixy
	* release candidate
	* scalany do mastera i do develop
* Feature
	* nie wiemy kiedy wejdą na release
	* wychodzą od develop
	* kiedy jest gotowy to merge'ujemy do develop
* CI
	* master - wdrożenie na produkcję
	* wszędzie - odpalenie testów
	* develop - zbudowanie i wypchnięcie artefaktów

### GitHub Flow
* Feature branches
* Pull requests
	* dyskusja i review
	* kiedy jest ok to merge do mastera
* Wygodne do małych projektów
	* na projekt z PIS może być dobre
* Przy wejściu kodu na produkcję może się nie sprawdzać

### Integracja Jiry z Gitem
* Warto
* Commity są automatycznie linkowane z zadaniami
	* w commit message podaje się id zadania

## CI/CD
* Continuous - codebase ma być ciągle karmiony commitami
	* minimum raz dziennie
	* commit nie oznacza działającego programu, nie musi być gotowego feature'a, nie musi się budować
	* mniejszą porcję kodu łatwiej poddać review
* Deployment / Delievery
	* wszystko automatycznie oprócz wdrożenia (na kliknięcie)
	* wszystko automatycznie
* Zalety
	* szybsze dostarczanie rzeczy na produkcję
	* łatwiejsze testowanie
	* łatwiejsze wycofywanie zmian (w teorii, nie jeśli są zmiany w bazie danych)

### Review
* Kiedy/jak robić review
	* zacząć od sprawdzania testów (zanim spojrzę na kod)
* Przynajmniej raz dziennie
* Jak kod się nie buduje to nie sprawdzam - nie zawsze dobre podejście

### Narzędzia
* Jenkins
* GitLab
* Bamboo - bardzo złe

## Artefakty
* .jar, obraz dockera, .zip ze stroną
* Warto trzymać na własnych serwerach, serwisy narzucają ograniczenia
* Narzędzia
	* Nexus
	* Artifactory
* Przechowuje wynik budowania kodu
* Stąd brana jest aplikacja do wdrożenia
* Trzyma historię wszystkich wydanych wersji

### Jenkins
* Pipeline'y
	* zazwyczaj odpowiedzialność devopsa, a nie programisty
* na projekcie używamy stosu złozonego z oddzielnych narzędzi, ale np gitlab ma to zintegrowane na jednej platformie

## Infrastrucutre as a Code
* Nie chcemy sytuacji, gdzie jest tylko jedna osoba, która wie jak działa infrastruktura
* Nie chcemy oddzielnie konfigurować wielu serwerów
* Ciężko zrobić to dobrze
* Przyspiesza proces
* Zapewnia weryfikowalność
	* np. pull request z nową konfiguracją
* Bezpieczeństwo
	* zabezpiecza przed pomyłkami
* Możliwość śledzenia zmian
* Kod dokumentuje infrastrukturę

### Ansible
* Jest bezstanowy, do konfiguracji spoko
	* nie spoko do zarządzania zasobami
* Narzędzie do
	* zarządzania konfiguracją systemu operacyjnego
	* wdrażania aplikacji
	* automatyzacji zadań

### Terraform
* Zachowuje stan
* Nie sprawdza faktycznego stanu środowiska
* Nie można wtedy modyfikować stanu środowiska ręcznie, tylko przez terraform

## Orkiestrowanie kontenerami

### Podejścia do wirtualizacji
* Maszyny wirtualne
	* oddzielne emulowane serwery
	* zajmuje dużo zasobów (oddzielne systemy operacyjne)
	* maszyny są od siebie odseparowane (jeśli nie ma błędów w procesorze)
	* hypervisor
* Docker
	* jeden system operacyjny
	* może być na maszynie wirtualnej
	* działa dobrze tylko na linuxie, wykorzystuje jego kernel
	* nie ma pełnej wirtualizacji
	* procesy odseparowane za pomocą namespace'ów z kernela linuxa
	* cgroups do zarządzania zasobami (np. ograniczenie przydziału RAMu)
	* obraz dockerowy daje zamrożony wycinek rzeczywistości - konkretna wersja debiana, konkretna wersja javy
	* obraz udostępnia się w świat i wszędzie można go identycznie odpalić
	* w kontenerze jest tylko to czego potrzebuję
	* nie muszę instalować niczego żeby odpalić aplikację
	* mogą być problemy z bezpieczeństwem (wyjście z kontenera na zewnątrz)
	* dużo lżejsze jest postawienie kontenera niż maszyny wirtualnej

### Kubernetes
* Uruchamia kontenery Dockerowe
* Dostarcza warstwę abstrakcji nad wieloma maszynami
* Orkiestrowanie kontenerami