# Infrastruktura klucza publicznego

## Dwa klucze
* Prywatny - znany tylko właścicielowi
* Publiczny - ogólnie rozpowszechniony

## Przykłady algorytmów szyfrowania asymetrycznego
* RSA
* Algorytm Diffiego-Hellmana
* Oparte okrzywe eliptyczne

## Szyfrowanie asymetryczne
* Szyfrujemy dane kluczem publicznym odbiorcy i je wysyłamy
* Odbiorca odszyfrowuje wiadomość swoim kluczem prywatnym
* Można zrobić na odwrót
	* zaszyfrować kluczem prywatnym, każdy może odszyfrować
	* wykorzystuje się do uwierzytelninaia i podpisów cyfrowych

### Uwierzytelnianie użytkownika
* Użytkownik wysyła nazwę i klucz publiczny (certyfikat)
* Strona wykonująca uwierzytelnienie wysyła losowe wyzwanie (challenge) z prośbą o zaszyfrowanie
* Po otrzymaniu zaszyfrowanej wiadomości próbuje ją odszyfrować
    * jeśli otrzyma wysłane wcześniej wyzwanie to jest ok

### Podpis cyfrowy
* Do potwierdzenia autentyczności lub wyrażenia zgody dotyczącej dokumentu cyfrowego
* Realizuje się przez zaszyfrowanie kluczem prywatnym skrótu dokumentu
	* szkoda czasu na cały dokument
* Każda osoba może zweryfikować podpis odszyfrowując skrót kluczem publicznym, wyliczyć samemu skrót dokumentu i porównać
    * jeśli skróty się zgadzają to podpis jest autentyczny

### Problemy
* Wymaga znajomości przypisania kluczy publicznych podmiotom
	* osobom, serwerom, urządzeniom sieciowym
* Wiarygodna dystrybucja tych informacji jest realizowana w oparciu o infrastrukturę klucza publicznego

## Infrastruktura Klucza Publicznego
* Wymaga istnienia zaufanej trzeciej strony
    * bez zaufania ten schemat nie działa
    * obie strony (sprawdzająca i sprawdzana) muszą ufać trzeciej stronie
    * powierzamy część bezpieczeństwa innemu podmiotowi
* Służy do zapewnienia wiarygodnego mapowania nazwy podmiotu do jego klucza publicznego

### Certyfikat
* Najważniejszy obiekt w PKI
* Wiąże w zaufany i możliwy do weryfikacji sposób informację o podmiocie i kluczu publicznym
* Standardy certyfikatów X.509 lub PKCS
* Elementy
    * nazwa podmiotu (osoba, serwer, router)
    * klucz publiczny podmiotu
    * podpis zaufanej trzeciej strony (CA) - chroni przed manipulacją certyfikatem
    * inne (timestampy, numer seryjny, id algorytmu, wskazanie na listę CRL)
* Standardowo reprezentacja binarna zakodowana w base64

### Typy certfikatów
* Autocertyfikat (self-signed)
	* zawierający klucz publiczny podpisany połączonym z nim kluczem prywatnym
    * początek łańcucha zaufania
* Certyfikat kwalifikowany
	* umożliwia składanie podpisu kwalifikowanego
    * uznawany w danej jurysdykcji za równoważny podpisowi odręcznemu (określone przez prawo)
    * raczej nie jest przesyłany pocztą czy na pendrivie tylko na dedykowanym sprzęcie odpornym na penetrację
* Certyfikat niekwalifikowany
	* każdy inny certyfikat

### Podpis zaufany
* Jedna z usług profilu zaufanego
* Dokumenty są podpisane podpisem cyfrowym ministra do spraw informatyzacji w czyimś imieniu
* Nie jest tożsamy z podpisem kwalifikowanym, wszystko zależy od konkretnych aktów prawnych

### Urząd certyfikacyjny (CA)
* Techniczna realizacja zaufanej trzeciej strony
    * zazwyczaj software
    * klucz ląduje na dysku
* W porządnym rozwiązaniu jest dedykowany moduł sprzętowy
	* odporny na penetrację (metalowa puszka, wyczyści się przy próbie rozkręcenia)
* Generuje certyfikaty korzystając ze swojego klucza prywatnego
	* podpisuje cudze klucze publiczne
* Dostępny publicznie certyfikat CA pozwala weryfikować prawdziwość certyfikatów wystawionych przez dane CA
* Verification Authority (VA) to w praktyce przeglądarka albo klient pocztowy

### Hierarchia urzędów certyfikacji
* To technicznie niemożliwe żeby wszystkich obsłużył jeden urząd
* Istnieje możliwość delegowania uprawnień do podpisywania certyfikatów przez inne podmioty
* Ścieżka zaufania
* Działanie
    * zweryfikowanie certyfikatu najniższego poziomu
    * to samo dla certyfikatu poziom wyżej
    * powtarzanie aż dojdziemy do certyfikatu, który jest zapisany jako zaufany
* Nie dodawać do przeglądarki niezaufanych certyfikatów
	* można wtedy wszystko podrobić 
    * np. pracodawca może odszyfrować komunikację z bankiem
* W systemy operacyjne i przeglądarki są wbudowane listy zaufanych certyfikatów

### Lista CRL
* Certificate Revocation List
* Lista odwołanych certyfikatów, którym już nie należy ufać
* Laptopa można ukraść, klucz prywatny można wysłać przez pomyłkę
* Certyfikat można zgłosić do listy CRL
* Przeglądarka powinna weryfikować taką listę
* Lista zaweira numery seryjne, jest generowana okresowo przez CA
* Musi być podpisana przez CA
* Jest specjalna lista certyfikatów odwołanych CA (Authority Revocation List)
* Może być za wolne
	* zbyt duży czas między wyciekiem klucza, a ogłoszeniem nowej listy CRL

### OCSP
* Alternatywa do list CRL
* Online Certificate Status Protocol
* Wysyła się zapytanie do CA, które wystawiło certyfikat
* CA odpowiada czy certyfikat jest ok
* Skraca czas między zgłoszeniem certyfikatu jako nieważny do wykrycia tego przez użytkowników

### Odzyskiwanie i powiernictwo kluczy
* Usługi urzędów certyfikacji, wspierane przez rządy
* Musi istnieć backup klucza prywatnego
* Ktoś ma dostęp do klucza

### Generacja kluczy na potrzeby PKI
* PKI nie musi generować dla nas kluczy
* Do wystawienia certyfikatu potrzeba tylko klucza publicznego
* **Nie ma potrzeby przekazywania klucza prywatnego**

## SCEP
* Simple Certificate Enrollment Protocol
* Umozliwia występowanie o certyfikat i zarządzanie listą CRL
* Oparty o HTTP

## Nieporozumienia z PKI

### Publiczna infrastruktura kluczy
* To co można nazwać *otwartym PKI*
* Każda nowa aplikacja może oprzeć pewne usługi (poufność itd) o istniejące certyfikaty
* 90% rynku należy do jednej firmy
* Problem - atak z mafią po środku
    * prośba o podpisanie niewinnych danych w celu uwierzytelnienia
    * w rzeczywistości podpisywany jest inny dokument
    * czy jest pewność, że software wyświetlający dokument, wyliczający skrót, sterowniki do czytnika karty nie był modyfikowany

### Zamknięte PKI
* Wykorzystanie technologii PKI dla zamkniętego środowiska
	* np. dla jednej organizacji
* Kryptografia asymetryczna w sieci SWIFT
    * PKI tylko dla określonych banków
    * te same urządzenia, ten sam software

## Wady PKI
* Cała infrastruktura opiera się na zaufanej trzeciej stornie na której wiarygodności budujemy bezpieczeństwo
* Sprawdzający i sprawdzany muszą mieć wspólny korzeń (zaufany CA)

## Alternatywa do PKI
* Sieć zaufania (web of trust) zamiast zaufanej trzeciej strony
* PGP, GPG
* Użytkownicy sami podpisują certyfikaty zaufanym i znanym im osobom
* Sami decydujemy czy ufamy danej osobie
* Key Signing Party

## SSL, TLS
* SSL został wymyślony przez firmę Netscape
* Dalej rozwijany przez IETF jako TLS

### Nawiązanie sesji TLS
* Klient nawiązuje połączenie TCP z serwerem
* Serwer odsyła certyfikat i wszystkie informacje o protokołach
* Klient (przeglądarka) weryfikuje certyfikat
* Klient sprawdza cały łańcuch certyfikatów, podpisy, daty ważności
* Klient generuje klucz sesyjny, szyfruje kluczem publicznym i odsyła
* Serwer odczytuje klucz sesyjny, odszyfrowując kluczem prywatnym
* Serwer może poprosić o certyfikat klienta
	* np. karta elektroniczna wydana przez pracodawcę
* Możliwość wzajemnego uwierzytelnienia

### Dodanie wsparcia TLS do aplikacji
* Aplikacja na każdym przychodzącym połączeniu zaczyna negocjację TLS
* Można zrobić oddzielny port dla szyfrowanej i nieszyfrowanej wersji protokołu
	* http 80 i https 443
* Mozna użyć tego samego portu i wydać komendę StartTLS 
	* opportunistic TLS

