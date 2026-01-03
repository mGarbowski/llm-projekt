# Wielowątkowość (ZPR- W09 -2020 12 01)
Procesor działa znacznie szybciej niż urządzenia zewnętrzne (IO) i pamięć, żeby nie marnować czasu procesora potrzebujemy wielu strumieni sterowania.

Wieloprocesowe systemy operacyjne - na platforny jedno procesorowe i wieloprocesorowe

## Aplikacje wielowątkowe
* Wątek realizuje niezależne ciągi instrukcji w ramach procesu
* Wątki współdzielą kod, dane i zasoby
* Mechanizm przełączania nie wprowadza dużych narzutów
* Pozwala na reakcję na zlecenia użytkownika podczas przeprowadzania obliczeń
* Lepiej wykorzystuje dostępną moc obliczeniową
	* szczególnie na platformach wieloprocesorowych
* Może obsługiwać wiele zleceń równolegle
* Poprawnie zaprojektowana jest szybsza na platformach wieloprocesorowych

## Aplikacje wielowątkowe w C++
* Współdzielone
	* obiekty globalne
	* obiekty dynamiczne
	* obiekty automatyczne jeśli dostęp jest przez wskaźnik lub referencję
	* Zasoby systmu operacyjnego (pliki, okna, itp.)
	* kod wykonywany
* Niezależne
	* rejestry
	* ciąg wykonywanych instrukcji
	* stos
	* zmienne automatyczne
* Program ma zawsze jeden wątek główny (funkcja `main()`)
	* może tworzyć dodatkowe wątki (wątki obliczeniowe / pomocnicze)
* Nie wszystkie funkcje biblioteki standardowej mogą być używane w aplikacjach współbieżnych
	* niewspółbieżna wersja biblioteki standardowej jest szybsza i mniejsza
	* wybór przez flagę kompilatora (`-pthread`)
* Niektóre funkcje odziedziczone z biblioteki C nie mają bezpiecznej wersji
	* używać random, regex, chrono zamiast odpowiedników z cstdlib
* Mechanizmy tworzenia i synchronizacji wątków są dostępne od standardu C++11
* Obsługa czasu
	* Boost.Date_Time
	* std::chrono - oparta o szablony
* Obsługa wątków przez `std::thread`

## Wyścigi
* Mogą występować kiedy wiele wątków pisze lub czyta tę samą pamięć
* Teoretycznie można wykryć wyścigi analizując wszystkie możliwe przeploty instrukcji
	* nierealistyczne
* Rozwiązanie przez synchronizację (blokady)

## Blokady - mutex
* Wzajemne wyklucznaie
* Służy do tworzenia sekcji krytycznych
	* wspierany przez system operacyjny
* `std::mutex`
* `std::lock_guard`

## Zakleszczenia (deadlock)
* Każdy z wątków czeka na jakiś inny (jest zablokowany)
* Żaden z nich nie może dalej pracować
* Rozwiązanie
	* zajmowanie blokad zawsze w tej samej kolejności
	* stosowanie innych mechanizmów synchronizujących
* Samozakleszczenie
	* brak zwalniania sekcji krytycznej np. w algorytmach rekurencyjnych
	* rowiązanie `std::recursive_mutex` - sprawdza identyfikator wątku

### Rodzaje prostych blokad w bibliotece standardowej
* `std::mutex`
	* lock
		* wolny - zajmuje
		* zajęty - blokuje
	* try_lock
		* wolny - zajmuje, zwraca true
		* zajęty - zwraca false
* `std::recursive_mutex`
	* jak wyżej
* `std::timed_mutex`
	* jak wyżej
	* try_lock_for(time_duration)
		* wolny - zajmuje, zwraca true
		* zajęty - blokuje na dany czas, zwraca false i przywraca sterowanie
	* try_lock_until(time_point)
		* jak wyżej


### Kończenie wątku
* Nie należy kończyć wątku inaczej niż przez wymuszenie zakończenia funkcji głównej wątku

```cpp
class MyThread {
public:
	MyThread(): finish_(false) {}
	
	void finish() { finish_ = true; }

	void operator()() {
		while (!finish_) {
			// przetwarzanie
			// sprawdzenie czy ma się zakończyć
		}
	}
private:
	volatile bool finish_;
}
```

Tak to jest implementowane w bibliotece standardowej

volatile - dostęp nie jest optymalizowany, asynchroniczna z punktu widzenia wątku

## Wątki i mechanizm wyjątków
* Wyjątki mogą być rzucane i wyłapywane w niezależnych wątkach
* Wyjątek nie powinien wyjść poza wątek, który go rzucił

## Skalowalność
* Mechanizm służy do tego, żeby przyspieszyć działanie aplikacji
* Wątki mogą pracować niezależnie gdy
	* odczytują współdzielone dane
	* zapisują lokalne dane
* Problematyczny jest zapis współdzielonych danych
* Wyróżnia się szybką i wolną ścieżkę w funkcjach
	* ściezka szybka - bez blokad

## Problem czytelników i pisarzy
* Wymaga bardziej skomplikowanego mechanizmu synchronizacji niż mutex
* Czytelnici - wątki nie wykluczające się nawzajem
* Pisarze - wątki wykluczające wszystkie inne wątki (czytelników i innych pisarzy)
* `std::shared_mutex`
* Dla czytelników
	* lock_shared,
	* try_lock_shared
	* timed_lock_shared
* Dla pisarzy
	* lock
	* try_lock
	* timed_lock
* Może pojawić się problem zagłodzenia

## Zagłodzenie (starvation)
* Nie ma zakleszczenia, ale wątek czeka w nieskończoność na wejście do sekcji krytycznej
* Np. pisarz nie może wejść do sekcji krytycznej, bo zawsze jest w niej jakiś czytelnik
* Implementacja `std::shared_mutex` gwarantuje poprawną obsługę bez zakleszczenia

## Problemy z usuwaniem błędów w aplikacjach wielowątkowych
* Niektóre błędy są niepowtarzalne
	* nie zawsze zachodzi taki sam przeplot
* Zachowanie wersji debug i release może się różnić
	* co będzie w pamięci, a co w rejestrach
* Testy na platformach z jednym procesorem mogą nie pokazać błędów które wystąpią na platformach wieloprocesorowych
* Aplikację należy poprawnie projektować

## Wzorzec monitora
* Pasywny obiekt
* Metody moga być wołane przez wszystkie wątki
* Obiekt zapewnia synchronizację wewnętrznie
	* np. posiada mutex jako składową

## Przetwarzanie potokowe
* Algorytmy wykorzystujące przetwarzanie potokowe wygodnie tworzyć przy wykorzystaniu wątków
* Sekwencyjne przetwarzanie (najpierw całe dane przepuszczone przez krok 1 itd)
	* wymagają dużych buforów
* Przetwarzanie danych porcjami
	* problem z doborem rozmiaru porcji
* Wykorzystanie mechanizmu wątków
	* nie ma problemu z doborem rozmiaru porcji
	* dostosowuje się automatycznie - któryś wątek będzie czekał

## Aktywny obiekt
* Asynchroniczne wołanie komend
* Komenda wykonuje się w niezależnym wątku
* Operacje są komendami, które można przechowywać w kolejkach
* Zarządca dysponuje pulą wątków
	* liczba np. wynikająca z platformy
* Klient dostarcza konkretną komendę zarządcy
	* zarządca dodaje komendę do kolejki
* Klient dostaje proxy do wyniku
	* po zakończeniu wykonania zamieniane na właściwy wynik
	* obiekt future (jeśli komenda zwraca wynik)

## Boost.Asio
* Asynchroniczna obsługa IO
* Przenośna obsługa zegarów, gniazd, portów szeregowych
* Zarządzanie 1000 połączeń sieciowych przez 1000 wątków nie ma sensu
	* i tak jest jedna karta sieciowa
	* tu nie sprawdza się mechanizm przełączania wątków, bo i tak tylko 1 może działać w danym momencie
* Obsługa asynchroniczna
	* 1 wątek
	* rejestruje się procedurę obsługi zdarzenia
	* nie wymaga synchronizacji
	* pętla obsługi zdarzeń (uruchamiana przez `boost::asio::io_service::run()`)

## Inne biblioteki boost 
* Boost.Compute
	* umożliwia używanie CPU lub GPU
* Boost.Interprocess
	* komunikacja międzyprocesowa
