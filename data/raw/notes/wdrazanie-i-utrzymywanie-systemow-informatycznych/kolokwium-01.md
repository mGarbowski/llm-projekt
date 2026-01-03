**1 Ansible:**  
a. wymaga działającej maszyny wirtualnej javy (JVM) na węzłach zarządzanych.  
**b. wymaga dystrybucji kluczy ssh w celu konfiguracji węzłów zarządzanych**
c. należy do klasy narzędzi agentowych  
d. nie może wykonywać poleceń wymagających uprawnień root-a

Ansible jest bezagentowy i łączy się przez SSH z maszynami zarządzanymi

**2 Dopuszczalny ciąg stanów dockera:**  
a. created->paused->running->stoped  
**b. paused->running->stopped->deleted**
c. created->stoped->running->deleted  
d. running->paused->running->deleted

![[docker-container-states.png]]

**3 Kontener:**  
a. nie pozwala na uruchomienie programów przeznaczonych dla innego systemu operacyjnego niż system gospodarza  
**b. zapewnia izolację programu uruchomionego w kontenerze od systemu operacyjnego gospodarza**
c. nie wymaga wsparcia systemu operacyjnego gospodarza  
d. dobrą praktyką jest jeden kontener działający na jednym systemie gospodarza

Izolacja dzięki Linux namespaces i cgroups,
a jest częściowo prawdziwe bo na windowsie wymaga WSL, nie jest przenośny między arm a x86

**4 Zaznacz fałszywe stwierdzenie na temat modelu bare metal:**  
a. zapewnia najbardziej efektywne wykorzystanie sprzętu  
**b. nie wymaga oprogramowania zależnego od platformy sprzętowej i systemu operacyjnego**
c. wyklucza wykorzystanie cloud computing  
d. węzły logiczne są związane z węzłami fizycznymi

c potencjalnie też fałszywe jeśli uznać kolokację za cloud computing

**5 Docker-compose:**  
**a. pozwala na definiowanie zbioru kontenerów i uruchamianie tak zdefiniowanego zbioru** 
b. jest narzędziem umożliwiającym orkiestrację kontenerów dockerowych  
c. posługuje się pojęciami: image, service, task, node  
d. zarządza stanem uruchomionych kontenerów dockerowych

**6 Fałszywe stwierdzenie na temat kubernetes:**  
**a. węzły (nodes) są uruchomione w kontekście Pod-a**
b. komponenty kontrolne k8s (np. api server, etcd, kube-proxy, kubelete) działają w Podach
c. w jednym węźle k8s może działać więcej niż jeden Pod
d. kube-scheduler zarządza cyklem życia Podów

Pod (jednostka wdrożeniowa) jest uruchamiany w kontekście węzła (maszyna fizyczna lub wirtualna)

**7 Development pipeline:**  
a. musi zawierać kroki manualne w celu nadzoru nad procesem CI/CD  
b. obejmuje fazę wygaszania systemu
c. wymaga wykorzystania kontenerów  
**d. w efekcie wykonania dostarcza nową wersję oprogramowania**

development pipeline (programistyczna linia produkcyjna) - ciąg kroków/czynności, które muszą być przeprowadzone w celu dostarczenia nowej wersji oprogramowania na właściwe środowisko wykonawcze

**8 Docker image:**  
**a. zawiera binaria i biblioteki potrzebne do uruchomienia programu**
b. nie jest specyficzny dla systemu operacyjnego gospodarza
c. jest rejestrem w obrazów dockerowych
d. musi znajdować się w lokalnym rejestrze

jest specyficzny dla jądra systemu operacyjnego - Linux, można odpalić na Windowsie wykorzystując WSL, można na dowolnej innej dystrybucji linuxa

**9 Zgodnie z definicją cloud computing NIST:**  
**a. w modelu PaaS klient usługi nie zarządza systemem operacyjnym**  
b. w modelu SaaS klient usług zarządza siecią  
c. w modelu IaaS dostawca usług zarządza licencjami na bazy danych  
d. SaaS = PaaS + IaaS

**10 Komenda docker exec:**  
a. startuje dockera
**b. uruchamia komendę w kontekście działającego kontenera**
c. wykonuje egzekucję dockera  
d. uruchamia główny program wykonawczy zdefiniowany w obrazie

**11 SDLC:** 
a. dotyczy systemów IT wytwarzanych i użytkowanych w modelu kaskadowym  
**b. obejmuje fazy wdrażania i rozwoju systemów IT**
c. obejmuje wdrażanie, utrzymanie i zarządzanie łańcuchem dostaw systemów IT  
d. nie obejmuje wygaszania systemów

SDLC - ogólny process rozwoju, wdrażania i wygaszania systemów informacyjnych, jest to proces wieloetapowy od inicjacji przez analizę, projekt, wdrożenie i utrzymanie aż do wygaszenia.

![[sdlc.png]]

**12 Zgodnie z zaleceniami architektonicznymi:**  
a. Pody mogą się komunikować między sobą bezpośrednio po adresach IP  
b. na jednej instancji systemu operacyjnego powinien być uruchomiony jeden kontener  
**c. na jednym kontenerze powinien być uruchomiony jeden proces**
d. na każdym Podzie k8s powinien być jeden kontener

a - stosuje się abstrakcje, np. Serwisy k8s
b - o to chodzi że można łatwo odpalić wiele kontenerów
c - z zaleceń w dokumentacji Dockera - Limiting each container to one process is a good rule of thumb, but it's not a hard and fast rule
d - niekoniecznie, może mieć sens żeby w jednym podzie było więcej

**13 Zaznacz fałszywe stwierdzenie na temat maszyny wirtualnej (VM):**  
**a. wymaga wsparcia procesora i systemu operacyjnego gospodarza**
b. aplikacje nie są świadome, że są uruchomione na VM
c. można uruchomić VM w kontekście innej VM (VM na VM)
d. mogą być uruchomione przez klienta usług w modelu IaaS

a - hypervisor typu 1 działa w ogóle bez OS gospodarza
b - generalnie tak, chociaż mogą to wykryć
c - można
d - na tym polega np EC2

**14 Orkiestracja:**  
a. nie wymaga stosowania kontenerów  
b. obniża koszty działania aplikacji w postaci skonteneryzowanej
c. zapewnia brak problemów utrzymaniowych
**d. umożliwia scentralizowane zarządzania aplikacjami skonteneryzowanej**

a - orkiestruje się kontenerami
b - autoscaling może obniżyć koszt - oszczędza się na infrastrukturze jak jest mały ruch, używa się tylko tyle ile potrzeba
c - nie rozwiązuje wszystkich problemów, np. zmiany wersji oprogramowania
d - 

**15 Pojęcia związane z Jenkinsem:**  
a. servic, executor build  
b. servant, butler, valet  
**c. build, executor, job**
d. master node, slave node, executor node

**16 Kubernetes Pod:**  
**a. może zawierać jeden lub wiele kontenerów**
b. definiuje logiczny zbiór serwisów k8s oraz politykę dostępu do nich
c. jest niezmienny (immutable)
d. pełni taką samą rolę jak task w docker swarm

a - Pod - najmniejsza jednostka wykonawcza K8s, może być realizowana przez jeden lub wiele konenerów
d - mniej więcej tak, ale task mapuje się na tylko 1 kontener, a pod na 1 lub więcej

**17 Zgodnie z modelem sieciowym dockera:**  
a. w trybie overlay nie ma możliwości dostępu do działającego kontenera z zewnątrz hosta  
b. w trybie host nie ma możliwości dostępu do działającego kontenera z zewnątrz host  
**c. w trybie bridge kontenery widzą się nawzajem w ramach jednego hosta ale nie są widoczne z zewnątrz**
d. w trybie host działający kontener ma adres z puli 172.17.0.1/24

**18 Procesy CI/CD:**  
a. mogą być wyłącznie stosowane w organizacjach zwinnych (agile)  
b. nie mogą być wyłącznie stosowane w modelach kaskadowych rozwoju oprogramowania  
c. służą zmniejszeniu kosztów wytwarzania oprogramowania
d. mogą skrócić czas do zebrania wymagań do wdrożenia oprogramowania

c i d są poprawne
c - zmniejsza koszty, bo automatyzacja przyspiesza powtarzalne czynności, pozwala wyłapywać błędy itp
d - skraca czas, bo wdrożenie może być szybsze jeśli wykonuje się automatycznie

**19 Kubectl:**  
a. działa wewnątrz kontenera dockerowego  
b. to komponent kontrolny działający w ramach centralnego węzła zarządzającego (master plane)
c. to komponent kontrolny działający na każdym węźle
**d. to komenda kontrolna do zarządzania klastrem**

**20 Maszyna wirtualna (VM):**  
**a. umożliwia uruchomienie systemu operacyjnego**
b. może być tylko jedna VM na jednym węźle fizycznym
c. jedna instancja może działać jednocześnie na wielu węzłach fizycznych
d. wymaga dostosowanych aplikacji, odmiennych od uruchamianych bez pośrednictwa VM

