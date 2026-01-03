# Bezpieczeństwo aplikacji webowych

## Tendencje ataków
* Coraz więcej ataków na aplikacje webowe
* Powstaje coraz więcej aplikacji z dużą liczbą podatności
* Potrzeba posiadania zdobytych maszyn w celu wykorzystania ich podczas kolejnych ataków
* Automatyczne skanery wyszukujące podatnych stron

## Narzędzia

### WebScarab
* Specjalne proxy umożliwia modyfikację dowolnej informacji przesyłanej między przeglądarką a serwerem WWW
	* cookies
	* nagłówki HTTP
	* treść odpowiedzi
* Do pentestów

### WebGoat
* Aplikacja edukacyjna stworzona przez OWASP
* Zawiera przykładowe aplikacje z celowo wprowadzonymi podatnościami
* Do nauki pentestów

## Protokół HTTP
* Tekstowy protokół typu request/response
* Początkowo stosowany do prezentowania statycznych informacji
	* najczęściej opisanych za pomocą języka HTML
* Podstawowa metoda używania przez przeglądarkę
	* GET - do pobierania zasobów z serwera WWW
	* POST - wysyłanie danych na serwer

## Najczęstsze typy ataków na aplikacji sieciowe

### Ataki związane z sesją
* Protokół HTTP jest bezstanowy, aplikacja musi sama zapewnić realizację sesji
* Rozpoznawanie sesji jest realizowane jako przesyłanie pewnej informacji identyfikującej klienta w żądaniu
* Wykorzystywane metody zapewnienia sesji
	* cookies
	* doklejanie identyfikatora sesji do adresu (URL rewriting)
	* ukryte pola w stronach
* Sesje
	* ID sesji jest generowany przy pierwszym żądaniu od nowego klienta
	* klient dołącza otrzymane ID do kolejnych zapytań
* Niebezpieczeństwa
	* najczęstsze ataki polegają na przechwyceniu sesji - poznaniu identyfikatora (Session Hijacking)
	* atak wymuszający użycie identyfikatora sesji (Session Fixation)
	* odgadnięcie numeru sesji
	* przechwycenie sesji może umożliwić ominięcie uwierzytelniania
	* wykradnięcie identyfikatora przez podsłuch lub atak XSS
* Przeciwdziałanie
	* zmiana identyfikatora sesji po zmianie poziomu uprawnień (np. po zalogowaniu)
* Dobre praktyki
	* szyfrowanie ruchu, zabezpieczenie przed podsłuchem
	* wygaszanie sesji po wylogowaniu
	* wygaszanie sesji po upływie czasu nieaktywności (sensownie krótkiego - tradeoff między bezpieczeństwem a używalnością)

### Ataki wstrzyknięcia
Spowodowanie że dane wyłamują się z kontekstu danych i są interpretowane jako kod wykonywany bez kontroli autora aplikacji

#### SQL Injection
* Odpowiednia manipulacja zapytaniem może prowadzić do innych zagrożeń, niż tylko ujawnienie większej liczby danych
* Dowolna modyfikacja bazy danych (`DROP TABLE users;`)
* Atak DoS na serwer baz danych
* Blind SQL injection
	* dane nie są bezpośrednio wyświetlane
	* jest sprawdzany jakiś warunek
	* też można wyciągnąć wszystkie dane przez napisanie odpowiednich warunków
* Timing attack

#### Inne ataki
* XSS
* XPATH injection
* JSON injection
* HTTP Response Spliting
* ORM injection
* Cmd injection
* LDAP injection
* Wszędzie gdzie użytkownik podaje dane, trzeba je sprawdzać

#### Command Injection
* Kiedy program wywołuje polecenia systemu operacyjnego (`exec(...)` itp.)
* Duży problem na urządzeniach wbudowanych i IoT
* Przy sprzyjających warunkach można dostać bezpośredni dostęp do maszyny
	* reverse shell
* Przeciwdziałanie
	* unikanie bezpośredniego interpretowania danych
	* *escapowanie* danych
	* silna kontrola typów (konwersja)
	* walidacja parametrów (zwłaszcza po stronie serwera)

#### Cross Site Scripting (XSS)
* HTML injection
* wykorzystywany z językami skryptowymi (js)
* Dwa rodzaje
	* Reflected XSS - odesłane (odbite) przez serwer
	* Stored XSS
* Stored XSS
	* dane użytkowników są przechowywane w bazie danych
	* nieautoryzowany kod może być wysyłany też innym użytkownikom
	* np. przeglądanie profilu innego użytkownika ze złośliwym kodem

### Cross Site Request Forgery (CSRF)
* Wykorzystuje działanie przeglądarek, które po uwierzytelnieniu użytkownika wysyłają dane tej sesji z dowolnego okienka aplikacji
* Przeciwdziałanie
	* do ważnych linków doklejany jest dodatkowy, losowy identyfikator, niemożliwy do przewidzenia przez atakującego
	* ważne linki chronimy dodatkowym potwierdzeniem wkyonywanym przez użytkownika
	* edukacja użytkowników

## OWASP
* Organizacja non-profit zajmująca się propagowaniem wiedzy dotyczącej aplikacji webowych
	* OWASP Top Ten
* CWE - Common Weakness Enumeration
	* katalog podatności z przykładami w kodzie
	* dobre do szukania rozwiązań konkretnych problemów
