# Infrastruktura

## Typy chmur
* Kolokacja
* IaaS (infrastructure)
* Paas (platform)
* Saas (software)

### Kolokacja
* Sprzęt firmy włożony do czyjejś lokalizacji
	* nie martwimy się systemem przeciwpożarowym, prądem, chłodzeniem

### IaaS
* Sprzęt jest dostarczany przez operatora
* Nasza odpowiedzialność zaczyna się na etapie instalacji systemu operacyjnego
* Nasza decyzja - bare metal / wirtualizacja
* Awaria dysku - problem dostawcy

### PaaS
* np AWS
* np. dostarcza maszyny wirtualne
* działy w dużych organizacjach świadczą usługi innym działom

### SaaS
* Pojedyncza aplikacja
* Konfiguracja w ramach aplikacji
* Warianty typu
	* baza danych jako serwis
	* kolejka jako serwis
	* streaming wideo jako serwis

### Aspekty praktyczne
* ...

## Prywatna vs publiczna
* Narzędzia prywatnej chmury
	* vmware
	* openstack
	* proxmox
* Chmury publiczne
	* AWS
	* GCP
	* Azure
* Kwestie prawne są istotne przy wyborze platformy
	* RODO ogranicza gdzie geograficznie mogą być przechowywane dane
* Rozwiązania hybrydowe
* Nie najważniejsze jest co się wybierze, a jak się tym zarządza
	* IaC - dokumentuje infrastrukturę

## Infrastructure as Code
* Dokumentuje architekturę
* Jest powtarzalne
	* np. daje możliwość zestawienia środowiska testowego analogicznego do produkcji
* Terraform
	* działa między operatorami
	* darmowe ale closed source
	* OpenTofu - port open source
* Każdy dostawca ma swoje rozwiązanie typu template

## Configuration as Code
* Wszelkie zmiany konfiguracyjne dokumentowane w kodzie
* Ansible
	* open source
* Puppet
	* darmowy, nie do końca open source?
* Chef
	* zamknięty
* Wszelkie zmiany w systemie operacyjnym
	* użytkownicy
	* firewall
	* uruchamianie aplikacji

## Abstrakcja zasobów
* Aplikacje które my wytwarzamy
* Kubernetes
* Apache Mesos
	* system operacyjny serwerowni
	* konfiguracje per serwerownie, a nie per serwer

## Przykład opentofu
* Zasób
	* coś co powołujemy do życia
	* np. maszyna wirtualna
	* provisioner - wykonuje operacje (np. na AWS), konektor do środowiska które wykonuje polecenia
* tofu plan
	* plan wykonania
* tofu apply
	* można coś napsuć
* tfstate
	* bieżący stan
	* nie monitoruje tego co się dzieje na bieżąco
* terraform.lock
	* hashe pobranych z rejestru pakietów (?)
* pluginy do konkretnych platform chmurowych (AWS, GCP) ale też do usług (rabbitmq)
	* zaciera się podział do czego używa się ansible a do czego terraform/opentofu
* jest opcja testowania tego co zostało wykonane
	* np. chcemy dowiedzieć się jakie adresy IP mają utworzone hosty

## Przykład Ansible
* Nie na Windowsie!
* ansible-playbook
* Na ogół dzieli się na wiele plików
* zmienne można mieć w oddzielnych plikach a można mieć zaszyte w playbooku
* inventory
	* format ini
	* format yml
* zwyczajowo - dzieli się na role
	* to co się wykonuje - tasks
	* główny task - main
	* handlers - wywoływany przez instrukcję notify
	* templates - format jininja
	* defaults - jeśli zmienne nie zostały gdzie indziej nadpisane
* inlude_tasks - łączenie poleceń z różnych plików
* dekompozycja problemu na małe zadania
* ansible łącząc się do hosta zbiera o nim informacje
* można definiować zmienne per host
	* mogą być zaszyfrowane - możemy je trzymać w repozytorium
* można korzystać z gotowych ról

## Przykład Kubernetes
* Nasza aplikacja została spakowana w kontener
* Minikube - klaster na jednym hoście
* node - maszyny (wirtualne lub fizyczne)
* pod - instancja
* zajmuje się balansowaniem ruchu
* umożliwia autoskalowanie
	* w godzinach szczytu uruchamia się więcej maszyn
	* kiedy ruch spada wyłącza się nadmiarowe maszyny
* Do obsługi poważnych obciążeń kładzie się na hardwarze
	* bez wirtualizacji