# Wirtualne sieci prywatne
Nie mylić z vlan!

* Dostęp danych poufnych poprzez sieć (niezaufaną)

## Szyfr asymetryczny
* zapewnienie tajności - klucz deszyfrujący jest tajny, klucz szyfrujący jest publiczny
  * każdy może zaszyfrować tekst, tylko ja mogę go rozszyfrować
* zapewnienie autentyczności - klucz szyfrujący jest tajny, klucz deszyfrujący jest publiczny
  * jeśli coś da się odszyfrować moim kluczem publicznym to znaczy że ja to zaszyfrowałem (podpisałem)
* zapewnienie tajności i autentyczności
  * dwie pary kluczy
  * podatność man in the middle
  * zabezpieczenie przed atakiem polega na wymianie certyfikatu wystawionego przez zaufaną trzecią stronę (urząd certyfikacji)
    * dane identyfikacyjne osoby
    * klucz publiczny osoby
    * podpisany kluczem tajnym urzędu certyfikacji
    * obie strony nie wymieniają się kluczami, tylko certyfikatami (które zawierają klucze)

## Rodzaje połączeń
* Komputer-komputer
  * jedna sesja TCP do zabezpieczenia
* Komputer-sieć
* sieć-sieć


## Secure Socket Layer

## Tunelowanie portów SSH
* `ssh -L 5555:localhost:25 user@host`
* Zapytanie wysyłane przez klienta na jego lokalny port 5555
* ssh szyfruje te pakiety i przesyła je na port 25 serwera zdalnego
* sshd serwera deszyfruje pakiet

## TCP over TCP
Jest jawny nagłówek TCP i drugi zaszyfrowany. Z punktu widzenia zaszyfrowanego nagłówka, wszystkie pakiety przechodzą i może ustawiać zbyt duże okno

To może być problem

## Point to Point Tunneling Protocol
Nie jest uznawany za bezpieczny

* protokół PPP
* uwierzytelnianie CHAP
* szyfrwoanie RC4 (złamane)
* tunel GRE (nie pomylić protokołu)

Wtedy stos protokołów wygląda tak

* TCP
* IP
* PPP
* GRE
* IP


## Layer 2 Tuneling Protocol
RFC 2661

* TCP
* IP
* PPP
* L2TP
* UDP/TCP
* IP
* ...


## IPSec
Najlepszy protokół do tworzenia wirtualnych sieci prywatnych

* AH - authentication header - w niektórych państwach nielegalne jest szyfrowanie danych w sieciach publicznych
* ESP - encapsulatiing security payload
* IPcomp - ip payload compression
* IKE - internet key exchange
* ISAKMP - internet security association and key management
  * połączenia sieć-sieć mogą trwać bardzo długo, lepiej co jakiś czas wymienić klucz symetryczny 

### transport mode
Szyfrowanie wszystkiego powyżej nagłówka IP

### tunnel mode
* Szyfrowanie całego pakietu IP łącznie z nagłówkiem i dodanie nowego
* Dobre do połączeń sieć-sieć, można stosować adresy prywatne w enkapsulowanych nagłówkach IP


schneier