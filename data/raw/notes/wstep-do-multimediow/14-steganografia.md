# Steganografia i znaki wodne
Steganografia to sztuka i nauka osadzania tajnych wiadomości w wiadomości jawnej w taki sposób, aby nikt poza nadawcą i zamierzonym odbiorcą nie podejrzewał istnienia wiadomości tajnej

* Nadawca ma plik maskujący i tajną wiadomość
* Koder z pliku, tajnej wiadomości i klucza (opcjonalne szyfrowanie) tworzy obiekt Stego
* Odbiorca odbiera obiekt Stego
* Dekoder dekoduje obiekt Stego używając klucza (opcjonalne szyfrowanie)

## Charakterystyka steganografii
* Pojemność
	* całkowita liczba ukrytych bitów i odtworzonych przez system
	* chcemy ich upchnąć jak najwięcej ale żeby nikt się nie zorientował 
* Odporność na przekształcenia
	* wiadomość nie powinna być widoczna po przekształceniach
	* skalowaniem obroty, transalcja
	* transofrmacje, filtrowanie, zmiana nasycenia
	* kompresja, kwantyzacja
* Niewykrywalność
	* medium maskujące ma podobną charakterystykę bez i razem z tajną wiadomością
* Niedostrzegalność
	* niewidoczne dla człowieka
* Bezpieczeństwo
	* ukryta informacja niepodatna na usunięcie po odkryciu
	* chodzi o to, żeby trudno było zniszczyć wiadomość po wykryciu i przechwyceniu komunikacji
	* zależy od znajomości algorytmu

## Steganografia a kryptografia
* Steganografia ma na celu ukrycie istnienia kanału komunikacji
* Steganografia zapewnia bezpieczeństwo komunikacji, a nie samą ochronę danych
* Dane nigdy nie powinny być widoczne
* Struktura danych nie jest zmieniona
* Klucz i szyfrowanie są opcjonalne
* Po wykryciu obecności tajnej wiadomości każdy może użyć tajnych danych (jeśli nie są zaszyfrowane)

## Techniki
* Sieciowa
	* ukrywanie w nagłówkach pakietów
	* np. pola opcjonalne
* Tekstowa
	* zmiana formatu istniejącego tekstu (np. odstępy)
	* losowa i statystyczna generacja przy użyciu gramatyk bezkontekstowych
	* metody lingwistyczne - zmiana słów
* Audio
	* kodowanie na najmniej znaczących bitach (LSB)
	* kodowanie parzystości
	* kodowanie fazy
	* rozpraszanie widma
	* do formatów bez i z kompresją
* Obrazowa
	* kodowanie na LSB
	* kodowanie LSB na transformacie
	* maskowanie i filtrowanie
	* kodowanie powtarzalnego wzorca
	* szyfrowanie i rozpraszanie
* Steganografia wideo
	* połączenie technik audio i obrazowych
	* duża ilość danych maskujących
	* wbudowanie wiadomości w surowe dane lub po kompresji
	* wbudowanie wiadomości bezpośrednio w strumieniu (w nagłówkach)

### Steganografia LSB
* Najprostsza do realizacji i wykrycia
* Zmiana najmniej znaczących bitów
* Niezauważalne dla odbiorcy
* Nieodporna na zmiany wartości przy przekształceniach

### Steganografia LSB dla transformat
* Zmiana najmniej znaczących bitów w dziedzinie częstotliwości
* Po transformacji kosinusowej, falkowej, itd
* Trudniejsze do zauważenia i usunięcia
* Informacja po odwrotnej transformacji jest rozproszona po całym obrazie
* Może być problem przy przekroczeniu zakresów
* Selekcja współczynników
	* tylko o dużej wartości
	* tylko o małej wartości

### Rozpraszanie widmowe
* XOR ukrywanych bitów z sekwencją pseudolosową
* Możliwe do odzyskania przy użyciu tej samej sekwencji
* Sekwencja generowana przez rejestr przesuwny LFSR
	* linear feedback shift register

### Dołączanie bitów do strumienia
* Po każdym plastrze / każdej ramce
* W nagłówkach
* Ramki są poprzedzone kodami synchronizacyjnymi
* Bity spoza ramki są pomijane przez dekoder strumienia

## Znakowanie wodne
Proces, któr osadza dane zwane znakiem wodnym (znacznik lub etykieta) w obiekcie / pliku multimedialnym, tak że taki znak można później wykryć lub wyodrębnić w celu uzyskania potwierdzenia o obiekcie.

* Na wejściu obiekt do oznakowania i znak wodny
* Koder zanurza znak wodny w obiekcie
* Po transmisji, zdekodowaniu odzyskuje się podpis
* Ocenia się czy podpis jest skorelowany ze znakiem wodnym
	* mogła być próba usunięcia znaku wodnego

### Znak wodny
* Jest atrybutem pliku multimedialnego
* Widoczny lub niewidoczny
	* można ukryć metodami steganografii
* Może zawierać informacje o licencji itd
* Powinien być odporny na usunięcie
* Co innego niż odcisk palca i podpis
