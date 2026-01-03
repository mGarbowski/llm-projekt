# ZPR- W08 -2020 11 24

## Biblioteki
* Dostępne w formie kodu źródłowego
	* wykorzystują szablony
	* brak problemów z łączeniem (konsolidacją)
* Biblioteki binarne
	* muszą być zgodne z aplikacją (platformą)
	* skraca czas budowania aplikacji
	* kod może być ukryty
* Biblioteki statyczne
	* Windows - .lib
	* Linux - .a
	* skompresowane wyniki kompilacji + tablica symboli
	* potrzebna w czasie budowania aplikacji, konsolidowana z kodem aplikacji
	* wbudowana w binarną aplikację
	* nie trzeba ich dostarczać razem z aplikacją
* Biblioteki dynamiczne
	* Windows - .dll
	* Linux - .so
	* kod PIC (position independent code) + tablica symboli
	* nie są wstawiane w kod binarny aplikacji
	* specjalna instrukcja wyłapywana przez system operacyjny
	* mniejszy rozmiar aplikacji
	* musi być dostępna, dostarczona razem z aplikacją
	* uzgadnianie adresów - dłuższe ładowanie
	* instalując bibliotekę dynamiczną w systemie możemy nadpisać wersję używaną przez inne programy - do rozwiązania przez wersjonowanie
	* ładowane podczas startu aplikacji
	* ładowane podczas pracy aplikacji (np. wtyczki)

### Biblioteki ładowane dynamicznie
* Udogodnienia, które nie są dostępne w czasie kompilacji
* Interfejs klasy bazowej musi być znany w trakcie kompilacji
* Biblioteka upraszczająca wykorzystanie wtyczek zawiera
	* zarządce wtyczek - rejestracja, inicjacja, finalizacja
	* wtyczka
	* klasy pomocnicze
* Boost.DLL, Qt

### Reprezentacja wtyczki bez użycia refleksji (RTTI)
* Dostarczenie metod, nadpisywanych w klasach konkretnych
* Wada
	* typy, które nie dostarczają interfejsu muszą go implementować

### Mechanizm refleksji
* Dostarczony jest tylko interfejs
* Badanie istnienia interfejsu przez `dynamic_cast`
* Klasy, które nie dostarczają interfejsu nie muszą go implementować

## Testowanie
* Utrzymywanie działającej wersji przez cały czas trwania projektu
	* łatwiej poprawić jeden błąd

### Testowanie modułów
* Rola testowania
	* klient upewnia się, że projekt działa zgodnie z założeniami
	* programista upewnia się, że kod działa tak jak on zakłada
* Dostarczenie testów to jedna z początkowych faz implementacji - TDD
* Pisanie testów powinno być proste
* Test to pierwszy przypadek użycia
* Wiele małych testów (test-case), które można grupować (test-suite)
* Możliwość wyboru ilości wyświetlanej informacji w razie niepowodzenia testu, możliwość śledzenia postępu
* Biblioteki
	* Boost.Test
	* cppunit
* Miary jakości testów
	* ile błędów pozwalają wykrać - trudna do obliczenia
	* pokrycie kodu testami (linii / ścieżek)
	* testowanie mutacyjne - modyfikuje się kod (zamienia plus na minus) i sprawdza się ile testów nie przechodzi

### Boost.Test
* WARN
	* ostrzeżenie
	* problemy mniej istotne niż poprawność (np. wydajność)
* CHECK
	* błąd
	* standardowa asercja
	* test będzie kontynuowany
* REQUIRE
	* błąd krytyczny
	* kiedy kontynuacja testu nie ma sensu
* Warunki liczbowe
	* BITWISE_EQUAL - zgodność bitów
	* EQUAL - operator==
	* SMALL - wartość bezwzględna mniejsza niż epsilon
	* CLOSE - wartość bezwzględna różnicy nie większa niż epsilon
* Wyjątki
	* NO_THROW - nie powinno generować wyjątku
	* THROW - powinno zgłosić wyjątek danego typu
	* EXCEPTION - powinno rzucić wyjątek spełniający predykat
* Generowanie wiadomości
	* MESSAGE - jeśli warunek fałszywy to generuje wiadomość
* Testy dziedziczą po test_case
* Zbiory testów
	* test_suite
	* można ustawić timeout
	* istnieje główny zbiór testów
	* program wykonywalny wywołuje ten zbiór
* Może wypisywać informację o platformie
* Sterowanie poziomem logowania
* Wielkość komunikatu
* Komunikat czytelny dla człowieka albo raport w xml do użycia w innych narzędziach
* Może pokazywać postęp
* Kolejność zpaisania lub losowa

## SCons
* Narzędzie do budowania aplikacji
* Opisuje projekt jako skrypt języka Python
* Wspiera kompilację równoległą
* Detekcja zmiany zawartości przez porównanie sygnatur MD5 (zamiast timestampów)

## System zarządzania wersjami, repozytorium
* Serwer plików
* Przechowuje kolejne wersje plików i katalogów
* Umożliwia wycofywanie zmian i pracę grupową

## Debugger
* Wykorzystuje instrukcje pułapki procesora
* Aplikację trzeba skompilować w sepcjalnym trybie
* Rola maleje jeśli stosujemy testy jednostkowe

## Narzędzie do wysyłania komunikatów
* Boost.Log
* Często jedyny mechanizm do śledzenia błędów
	* w środowisku produkcyjnym
* Mniej uniwersalne niż debugger
* Definiuje się poziom logowania
* Obserwatorzy
	* konsola
	* plik
	* UNIX Syslog

## Ciągła integracja
* Jenkins
* Współpracuje z repozytorium
* Uruchamianiebudowania, testów jednostkowych, testów funkcjonalnych
* Wiele obsługiwanych repozzytoriów
* Narzędzia do budowania dla różnych środowisk
* Rozbudowany zbiór wtyczek
* Interfejs webowy

## Architektury systemów komputerowych
* Architektury trójwarstwowe
	* warstwa trwałości (danych)
	* warstwa logiki (przetwarzania)
	* warstwa prezentacji (interfejs użytkownika)
* Architektury klient-serwer