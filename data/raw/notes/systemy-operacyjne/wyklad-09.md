# (2023-11-28)

W komunikacji międzyprocesowej zawsze uczestniczy jądro

Zalety wielowątkowości
* umożliwia pracę na tych samych zasobach przez wiele strumieni wykonania jednocześnie

Debugger nie pomoże przy bugach w wielowątkowości

Wątki tego samego procesu mogą wymieniać informacje przez zmienne globalne

### Wątki można zrealizować bez wywołań systemowych (user level thread)
* Musi przyjąć jakąś funkcję do wywołania
* Musi mieć przydzielony fragment pamięci z segmentu stosu
* Jakiś identyfikator
* Struktura z informacjami o stanie
* Szybkie, nie ma przełączania do jądra ale wywołania operacji IO zatrzyma cały proces
* realizowane przez biblioteki języków programowania
* liczba wątków jest ograniczona przez rozmiar segmentu stosu, można tworzyć tysiące

### Wątki zrealizowany w systemie operacyjnym (kernel level thread)
* Tworzeniem i przełączaniem zajmuje się scheduler jądra, szereguje wątki a nie procesy
* Drogie tworzenie i przełączanie wątków
* Duże wykorzystanie pamięci jądra
* Szeregowanie jest bardziej efektywne bo IO wątku nie zablokuje całego procesu

### Wątki hybrydowe
Najbardziej efektywne jest rozwiązanie hybrydowe

* Wątek poziomu jądra można rozgałęzić na wiele wątków poziomu użytkownika (realizowane w bibliotekach)
* Nie ma sensu tworzyć więcej wątków poziomu jądra niż logicznych procesorów w komputerze bo będą konkurować o czas same ze sobą
* Można utworzyć 1000 wątków bibliotecznych ale np. tylko 4 będą się wykonywać równolegle

Ważne na kolokwium!

### Light-weight process (LWP)
Jeden wątek poziomu jądra

Można wymusić wykluczenie wątku ze standardowego szeregowania i przydzielenia mu dedykowanego procesora


## Serwer wielowątkowy
Do wielu zastosowań opłaca się mieć wiele wątków
* Jeden wątków typu dispatcher
* Wiele wątków typu worker
* Jeśli jest więcej pracy niż wolnych wątków worker to kolejkujemy (buforujemy) zlecenia


## Metody konstrukcji serwerów
* Serwer wielowątkowy - współbieżny, blokujące wywołania systemowe
* Proces jendowątkowy - brak współbieżności, blokujące wywołania systemowe
* Automaty skończone - współbieżne, nieblokujące wywołania systemowe, przerwania
	* asynchroniczne wejście wyjście

## Architektura w systemie Solaris (System V)
* Procesy
* Wątki poziomu użytkownika
* LWP - odwzorowanie wątków poziomu jądra
* Wątki poziomu jądra

## Cechy dobrego szeregowania
* sprawiedliwe - każdemu równą część CPU
* zgodne z przyjątą polityką
* wyrównywanie - zbliżona zajętość wszystkich części systemu

### Systemy wsadowe
* przepustowość - maksymalizaja liczby zadań w czasie
* czas w systemie - minimalny między uruchomieniem a zakończeniem
* wykorzystanie procesora - minimalizacja przerw w pracy procesora

### Systemy interaktywne
* czas odpowiedzi - możliwie szybka odpowiedź na żądanie
* proporcjonalność - spełnianie oczekiwań użytkownika

### Systemy czasu rzeczywistego
* spełnianie wymagań - ograniczenia czasowe
* przewidywalność