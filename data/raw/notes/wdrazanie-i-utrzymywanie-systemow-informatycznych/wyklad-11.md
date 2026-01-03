# Bezpieczeństwo w utrzymywaniu (2025-05-08)

## Cyberbezpieczeństwo
* Każdy system jest narażony na cyberataki
	* jest wart zaatakowania
* Nie ma systemów absolutnie bezpiecznych
* Bezpieczeństwo jest przeciwstawne łatwości użytkowania
* Rachunek wartości oczekiwanej
	* jaka jest szansa, że ktoś wykorzysta podatność
	* jakie będą koszty wykorzystania podatności
* Podatności są zarówno w domenie rozwoju i utrzymania

## Cyberbezpieczeństwo a utrzymanie
* Podatność
	* słabość danego systemu wynikająca z błędów wewnętrznych lub błędów użytkownika
* Podatność zero-day
	* cały świat się o niej dowiaduje i większość systemów nie jest na nią odporna
* Niektóre podatności są konsekwencją decyzji architektonicznych i powstają w fazie budowy systemów
	* np. decyzja o sposobie uwierzytelnienia użytkownika
* Utrzymanie dodaje od siebie podatności
* Na końcu za usuwanie lub przeciwdziałanie wszystkim rodzajom podatności odpowiada utrzymanie
	* rozpoznanie ataku
	* zidentyfikowanie jak poważne są skutki ataku

## Podstawowe pojęcia
* Uwierzytelnienie - sprawdzenie tożsamości użytkownika / systemu, który ma dostęp do chronionego systemu
	* posiadana informacja (hasło)
	* posiadana cecha (biometria)
	* posiadany przedmiot (fizyczny klucz)
* Autoryzacja - weryfikacja uprawnień uprzednio uwierzytelnionego użytkownika / systemu

## OWASP
* The Open Web Application Security Project
	* aplikacje dostępne przez HTTP
* Społeczność praktyków bezpieczeństwa
* Tworzą otwarte raporty dotyczące bezpieczeństwa
	* top 10 kategorii podatności
	* ASVS - Application Security Verification Standard

### OWASP Top 10
* Broken Access Control
	* naruszenie przyznanych uprawnień (autoryzacji)
* Cryptographic Failures
	* wszelkie błędy, które powodują wyciek poufnych informacji
* Injection
	* uruchamianie przez serwer niebezpiecznego kodu wstrzykniętego przez użytkownika (XSS, SQL injection)
* Insecure Design
	* niewłaściwy / niesprawdzony projekt i architektura
	* trudno przewidzieć wszystkie przypadki brzegowe
* Security Misconfiguration
	* brak konfiguracji bezpieczeństwa
	* np. domyślne hasła, niepotrzebnie otwarte porty, uruchomione nieużywane usługi
* Vulnerable and Outdated Components
	* przestarzałe, dziurawe wersje komponentów
	* np. zaniedbanie aktualizacji
* Identification and Authentication Failures
	* słabe hasła
	* podpowiedzi bezpieczeństwa
	* sesje z nieograniczonym czasem
* Software and Data Integrity Failures
	* podatności spowodowane przez używanie oprogramowania z niesprawdzonych źródeł
	* każdy projekt używa masy zależności open source
* Security Logging and Monitoring Failures
	* brak logowania
	* nieanalizowanie logów pod względem bezpieczeństwa
	* brak alertów bezpieczeństwa
	* duży potencjał na zastosowanie AI do wykrywania wzorców
* Server Side Request Forgery (SSRF)
	* umieszczenie na serwerze kodu wykonywalnego

### OWASP ASVS
* Trzy poziomy wymagań bezpieczeństwa aplikacji webowych
* Kompaktowy standard, warto poczytać
* Level 1
	* dla aplikacji o niskim poziomie bezpieczeństwa (podstawowy)
	* zapewnione przez testy penetracyjne
* Level 2
	* dla aplikacji, które przechowują dane wrażliwe (poziom rekomendowany)
* Level 3
	* dla aplikacji krytycznych, które przetwarzają transakcje finansowe o wysokim poziomie
	* dane medyczne, inne wymagające dużego poziomu zaufania
* Wymagania mają strukturę
	* treść
	* stosowalność do poziomu (L1-L3)
	* referencja do katalogu słabości (Common Weakness Enumeration)
	* referencja do wymagań bezpieczeństwa NIST
* Podzielone na 14 rozdziałów
	* architektura, projektowanie i modelowanie zagrożeń
	* uwierzytelnianie
	* zarządzanie sesją
	* autoryzacja
	* walidacja, kodowanie parametrów wejściowych
	* kryptografia
	* ...
	* złoścliwy kod
	* logika biznesowa
	* API i WebServices
	* konfiguracja

Za tydzień nie ma wykładu