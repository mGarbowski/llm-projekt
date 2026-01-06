# Funkcje skrótu

## Usługi ochrony informacji 
* Uwierzytelnienie - daje pewność, że ten kto nawiązuje komunikację, jest tym za kogo się podaje
* Poufność - zapewnienie aby informację poznały tylko uprawnione osoby
* Niezaprzeczalność - punkt, który wygenerował informację nie może się wyprzeć tego faktu
* Integralność - zapewnienie możliwości wykrycia modyfikacji danych
* Kontorla dostępu
* Dostępność

## Poufność a integralność
* Poufność zapewnia szyfrowanie
* Szyfr nie zapewnia integralności
    * dane przelewu są zaszyfrowane w trybie ECB
    * manipulując odpowiednimi blokami można zmanipulować konkretnym fragmentem (np. kwotą)
    * słowo zaszyfrowane tym samym kluczem będzie miało tą samą postać
    * mozna to poprawić dodając sól
    * szyfry strumieniowe albo CBC przed tym chronią
* Bit flipping attack (na szyfr strumieniowy)
    * trzeba znać pozycję np. kwoty w szyfrogramie
    * `C[pozycja] xor kwota = klucz[pozycja]`
    * `C'[pozycja] = nowa_kwota xor klucz[pozycja]`
* Poufność nie gwarantuje integralności
* Do ochrony integralności służą Message Authentication Codes (MAC)
* Kody uwierzytelniające wykorzystują funkcję skrótu
    * wejściem jest tekst dowolnej długości
    * wyjściem jest losowo wyglądający tekst o stałej długości
    * skrót jest zupełnie inny nawet dla zbliżonych wejść

## Właściwości funkcji skrótu
* Wejściem są dane dowolnej długości
* Wyjściem są dane stałej długości, wyglądające na losowe 
* Jednokierunkowość
	* łatwo policzyć `h(M)` 
	* nie ma prostego sposobu na wyliczenie `M` na podstawie `h(M)`
* Bezkolizyjność
	* trudno znaleźć dwie dowolne wartości `M` i `M'` dla których `h(m) = h(M')`
* Nie używać MD4, MD5, SHA-1
* Używać SHA-2, SHA-3, Keccak

## Message Authentication Code
* Trywialne podejście
    * ustalony wspólny klucz $k$
    * `MAC = h(k || M)`
    * MAC jest dołączany do wiadomości
    * Odbiorca też oblicza skrót i porównuje z tym który dostał
* Trywialne podejście umożliwia dodanie dalszej części wiadomości
* HMAC (keyed-hash MAC) - bezpieczne rozwiązanie
    * `HMAC = h(k xor A || h(k xor B || M))`
    * `A` - stała `0x5C`
    * `B` - stała `0x36`
* CMAC (cipher based MAC) - bezpieczne rozwiązanie
	* wykorzystanie specjalnie zaprojektowanych trybów szyfrów blokowych
	* do generowania MAC lub jednoczesnego szyfrowania i generowania MAC

## Zastosowania funkcji skrótu
* Uwierzytelnianie użytkownika hasłem (lokalne)
* Uwierzytelnianie przez sieć
* Podpis cyfrowy

### Uwierzytelnianie użytkownika hasłem
* **Hasła nie są zapisywane tekstem jawnym**
* Przechowywane i przesyłane są skróty haseł
* Przy uwierzytelnianiu wyliczany jest skrót hasła podanego przez użytkownika i porównuje się z zapisanym
* Funkcja skrótu gwarantuje, że nie będzie można łatwo odgadnąć hasła użytkownika
* Problemy
	* słabe, przewidywalne hasła użytkowników
	* podatność na ataki słownikowe słabych haseł
	* hasła łamane po wykradnięciu `/etc/passwd` 
* Hasła przeniesione z `/etc/passwd` do `/etc/shadow`
	* wiele programów potrzebuje dostępu do `/etc/passwd`
	* `/etc/shadow` ma bardziej restrykcyjne prawa dostępu
	* w `/etc/shadow` przechowywane są id funkcji skrótu, sól i hash
* Przed wyliczenie skrótu, do hasła dodaje się losowy ciąg znaków - sól
	* sól przechowywana tekstem jawnym
	* identyczne hasła po dodaniu soli dają różne hasze
* Łamanie haseł
	* przeszukiwanie wszystkich możliwych haseł - brute force
	* ataki słownikowe
	* wykorzystanie informacji z wycieków haseł
	* tablice tęczowe

### Uwierzytelnianie zdalne - protokół CHAP
* Challenge Handshake Authentication Protocol
* Działanie
	* A i B mają wspólny sekret
	* A chce uwierzytelnić się przed B
	* B wysyła losowy ciąg danych
	* A dokleja do ciągu sekret i odsyła skrót tego ciągu
	* B robi to samo i porównuje wynik
* Hasło nie jest przesyłane w postaci jawnej
* Odpowiednie dobranie wyzwania zapobiega atakom typu powtórzenie
* Możliwość wzajemnego uwierzytelnienia
	* sprawdzenie, czy serwer do którego się łączymy zna nasze hasło

## Architektura AAA
* Authentication (uwierzytelnienie)
* Authorization (autoryzacja)
* Accounting - ile zasobów wykorzystuje
* Można wynieść funkcjonalność na dedykowany serwer
    * czy zezwolić na podłączenie klienta
    * czy umożliwić logowanie administratora do urządzenia
    * czy zezwolić administratorowi na wykonanie określonego polecenia
* Protokoły komunikacji z serwerem uwierzytelniającym
    * Radius
    * Tacacs+
    * Diameter

## Protokół 802.1x
* Umożliwia podjęcie deyzji co do dalszej transmisji danych klienta przez urządzenie dostępowe (AP, switch) dopiero po uprzednim uweirzytelnieniu
* Najczęściej przy podłączaniu do WiFi
* Bazuje na Extensible Authentication Protocol (EAP)
* Przy każdym podłączeniu do WiFi

## Liczby losowe na potrzeby kryptografii
* W kryptografii często potrzebne są liczby losowe
    * generowanie kluczy asymetrycznych
    * generowanie kluczy sesji
    * generowanie loswego wyzwania
    * wektory inicjalizujące
* Funkcje typu `rand()` (odwołujących się do czasu itp) **nie nadają się do celów kryptograficznych**
* Należy używać kryptograficznie bezpiecznych generatorów liczb psudolosowych (CSPRNG)
	* generowane w oparciu o wiele trudnych do przewidzenia czynników
	* pid, liczba taktów procesora od starty, czas, liczba operacji IO, itd.
* Najbezpieczniej jest używać sprzętowych generatorów liczb losowych (TRNG)
    * wykorzystują prawdziwie losowe zjawiska fizyczne
    * szum termiczny, rozpad promieniotwórczy, efekt fotoelektryczny
