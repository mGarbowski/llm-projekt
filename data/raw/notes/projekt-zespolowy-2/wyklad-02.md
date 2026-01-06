# Modelowanie przypadków użycia (2024-10-25)
Jest diagram UML to scenariuszy użycia, ale określa tylko elementy z jakich diagram może się składać

* Opisuje sposoby wykorzystania systemu
	* opisuje jak użytkownicy korzystają z systemu
* Użytkownik - aktor
	* aktorem może być człowiek lub zewnętrzny system
	* użytkownicy mają role (student, prowadzący)
* Opis zaczyna się od identyfikacji użytkowników
* Potem określa się co ci użytkownicy będą mogli zrobić
* Opisanie tych sposobów - przypadki użycia
	* scenariusze - numerowane, kolejne kroki, bardziej użyteczny
	* graficzna postać
* Kroki w scenariuszu na początku są na dużym poziomie ogólności
* Diagram UML
	* ludziki reprezentują aktorów
	* elipsy reprezentują przypadki użycia
	* aktorzy są połączeni z przypadkami użycia w których uczestniczą
	* pełni tylko rolę pomocniczą
	* strzałka wychodzi od aktora inicjującego przypadek użycia

## Biznesowy i systemowy model przypadków użycia
* Osoby które bezpośrednio korzystają z systemu (interfejsu użytkownika) - aktorzy systemowi
	* np. pracownicy banku
* Aktorzy systemowi mogą załatwiać sprawy klientów, którzy nie korzystają z systemu - aktorzy biznesowi
	* np. klient w fizycznym banku, osoba wypożyczająca książkę w bibliotece
* Aktor może być jednocześnie aktorem systemowym i biznesowym
	* kiedy klient biznesowy może bezpośrednio korzystać z systemu
	* np. klient korzystający z bankowości internetowej
* Często zaczyna się modelowanie od biznesowego modelu przypadków użycia
	* jakie sprawy załatwiają klienci
* Czas też może być aktorem
* Systemowy model
	* jakie operacje mogą wykonywać użytkownicy systemu
* Często nie tworzymy niskopoziomowych wymagań od razu tylko dochodzi się do nich stopniowo

## Przykład - biblioteka
* Przypadki użycia powinny mieć unikalny identyfikator
	* podział na systemowe i biznesowe
* Każdy przypadek użycia ma aktorów, którzy są zaangażowani w jego realizację
* Przypadek użycia może mieć scenariusz główny i scenariusze alternatywne
	* scenariusz główny - typowy przebieg, kiedy wszystko poszło dobrze
	* scenariusze alternatywne - coś poszło nie tak (np. książka nie jest dostępna do wypożyczenia)
* W przypadkach użycia mogą pojawić się specyficzne pojęcia
	* w dokumentacji powinien istnieć słownik pojęć tłumaczący specyficzne terminy dla domeny
* Schematyczna budowa zdań
	* aktor/system + czynność
* Nie wszystkie przypadki użycia będą wynikać wprost z wymagań
	* zadaniem analityka jest znalezienie takich przypadków

W ramach dokumentacji projektu powinna powstać dokumentacja przypadków użycia (może wystarczą systemowe)

### Systemowe przypadki użycia
* Zapis jak dla przypadków biznesowych
	* uszczegóławia jak realizowane będą w systemie przypadki biznesowe
	* funkcje użytkownika
* Tylko aktorzy systemowi
* Odnośniki do reguł biznesowych
	* dla uproszczenia zapisu
	* odzwierciedlają bieżącą politykę działania instytucji
* Między funkcjami użytkownika moga istnieć logiczne powiązania
	* np. zarejestrowanie rezerwacji łączy się z przeglądaniem katalogu
	* dla uniknięcia redundancji w opisie przypadków użycia ...
* Może korzystać z innych funkcji użytkownika - odnośnik

### Relacje między przypadkami użycia
* Uogólnienie/specjalizacja
	* np. rejestracja rezerwacji jest szczególnym przypadkiem przeglądania katalogu
	* strzałka z grotem
* Włączenie
	* wykorzystanie innego przypadku użycia
	* przerywana strzałka ze stereotypem `<<include>>`
* Rozszerzanie
	* przerywana strzałka ze stereotypem `<<extend>>`
	* podobne do relacji uogólnienia
	* np. w miejscu FU5 (wybór operacji) może wykonać się FU6 albo FU7
	* opcjonalne wykonanie
* Biznesowe przypadki użycia są zazwyczaj na tyle ogólne, że nie modeluje się relacji pomiędzy nimi
* Na diagramie przypadków wystarczy strzałka od aktora do przypadku specjalizującego / rozszerzającego
	* domyślnie *dziedziczenie* aktora
* Do przypadków specjalizujących / rozszerzających może dojść więcej aktorów
	* np. czas jak na slajdach wykładowych

Trzeba się zastanowić czy specyfikacja systemu jest kompletna - jeśli wprowadzę jakieś dane to gdzie są wykorzystywane? jeśli system korzysta z danych, to skąd się one wzięły w systemie?

Można zbudować macierz zależności między biznesowymi przypadkami użycia, a systemowymi przypadkami, które je wspierają. Kolumna bez zależności powinna nas zaniepokoić - przypadek biznesowy nie jest nigdzie obsłużony. Wiersz bez zależności powinien nas zaniepokoić - dodajemy funkcje które nie są potrzebne.