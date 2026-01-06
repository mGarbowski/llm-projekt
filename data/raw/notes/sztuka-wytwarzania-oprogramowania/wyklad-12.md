# Współbieżne wzorce projektowe 2 (2024-05-27)
* Procesor działa znacznie szybciej niż inne urządzenia
* Współczesne komputery są wieloprocesorowe
* Wątek realizuje niezależne ciągi instrukcji w ramach jednego procesu
* Niewłaściwe stosowanie blokad może prowadzić do zakleszczeń

## Obsługa urządzeń IO
* System operacyjny zapewnia 3 metody obsługi urządzeń IO
* Synchroniczne blokujące
	* sterowanie wraca, gdy operacja jest zakończona
* Synchroniczne nieblokujące
	* sterowanie wraca natychmiast z informacją, czy udało się zrealizować operację
	* może zwracań np. liczbę odczytanych bajtów
	* operację można ponowić
* Asynchroniczne
	* sterowanie wraca natychmiast
	* użytkownik dostarcza uchwyt (callback), który będzie wołany gdy operacja się zakończy

## Obsługa IO bazująca na wątkach
* Wykorzystuje synchroniczne metody obsługi IO
* Sekwencyjna (prosta) struktura sterowania
* Każde urządzenie obsługuje się w oddzielnym wątku
	* podczas oczekiwania inne wątki mogą pracować
	* słabo się skaluje np. dla 1000 gniazd TCP (i tak nie ma 1000 kart sieciowych)
* Przesyłanie danych z takim wątkiem wymaga mechanizmów synchronizacji
* Narzuty
	* synchronizacja
	* blokady
	* mechanizm przełączania wątków

## Obsługa IO bazująca na zdarzeniach
* Wykorzystuje synchroniczne lub asynchroniczne metody obsługi IO
* Kolejka zdarzeń i pętla obsługi zdarzeń
* Odwrócenie sterowania - rejestrujemy uchwyty, które będą wykonywane
* Brak kontroli nad kolejnością obsługi
* Brak narzutów na synchronizację, blokady, wątki


## Boost.Asio
* Synchroniczna / asynchroniczna obsługa IO w C++
* Przenośna obsługa
	* zegarów (timer)
	* gniazd UDP i TCP
	* portów szeregowych
	* sygnałów
	* uchwytów do plików
* Wsparcie dla Windows, Linux, Mac

## Wzorzec projektowy reaktora
* Obsługa urządzeń oparta o zdarzenia
* Odwrócenie sterowania
* Wykorzystuje nieblokujące, synchroniczne operacje IO
* Klient rejestruje w reaktorze uchwyty do obsługi
* ...

## Wzorzec projektowy proaktora
* Obsługa zdarzeń oparta o zdarzenia
* Odwrócenie sterowania
* Wykorzystuje asynchroniczne operacje IO
* ...

Z punktu widzenia programisty aplikacji różnica jest nieistotna, korzysta się z nich tak samo


## Instrukcje atomowe
* Niektóre operacje są transakcjami - wykonują się w całości albo wcale
* Za pomocą takich operacji możemy tworzyć algorytmy współbieżne bez blokad (lock-free)
* Takie algorytmy mogą działać szybciej niż tworzenie sekcji krytycznych
* Operacje atomowe może gwarantować sprzęt (procesor)
* `++x` nie jest atomowa
	* odczyt z pamięci do rejestru
	* inkrementacja
	* zapis do pamięci
* Szablon `std::atomic`
	* typy danych, które mogą być atomowe
	* narzuty przy operacjach na typach atomowych
	* pozwala tworzyć algorytmy bez blokad
* `std::atomic<bool>` są zawsze atomowe, bez blokad
	* inne typy będą działać poprawnie, ale nie zawsze bez blokad
	* może wewnętrznie używać mutexa
	* jest sens ich używać kiedy nie mają wewnętrzenej blokady
	* zawsze dostarcza poprawną implementację `load` i `store`
	* `compare_exchange_weak`, `compare_exchange_strong`
		* warunkowa, atomowa zamiana
		* podstawowa operacja dla algorytmów lock-free
* Podsumowanie
	* są wolniejsze niż nieatomowe ale gwarantują poprawność
	* warto je stosować do tworzenia współbieżnych struktur danych
	* algorytmy lock-free są trudne do implementacji i zrozumienia
	* operacje atomowe mogą być szybsze lub wolniejsze od blokad, zależy jak często występują wyścigi

## Specjalne typy atomowe
* Liczby całkowite
* Liczby rzeczywiste
* Wskaźniki
	* też sprytne wskaźniki
* Działają dużo szybciej niż blokady (np. użycie mutexa)

## Algorytmy bez blokad
* Wyścigi są dopuszczone
* W przypadku wyścigu operacja jest powielana
* Założenie że wyścigi wystąpią rzadko i powiela się do skutku
* Niedeterministyczny czas działania

## Współbieżna blokada
* Problem czytelników i pisarzy
	* w sekcji krytycznej może być wielu czytelników na raz
	* pisarz wyklucza wszystkie inne wątki z sekcji krytycznej
* `std::shared_mutex` i `boost::shared_mutex`
	* np. dla wątku czytelnika
* Metody
	* lock
	* try_lock
	* timed_lock
	* lock_shared
	* try_lock_shared
	* timed_lock_shared

## Zagłodzenie (starvation)
* Wątek nie może się wykonywać, ponieważ cały czas jest blokowany
* Co innego niż zakleszczenie
* Np. w problemie czytelników i pisarzy
* Wymaga innych mechanizmów zapobiegawczych
	* `std::shared_mutex` rozwiązuje to poprawnie

## Kolos
* Metryki
	* kodu
	* procesu
* Pokrycie kodu
* Jakość testów
* Analiza oprogramowania
	* analiza dynamiczna
	* analiza statyczna
* Refaktoring
	* zapachy kodu
	* jak poprawiać kod
* Współbieżność
	* wątki, wyścigi, skalowalność
	* blokady, zakleszczenia
	* operacje atomowe (`std::atomic`)
	* obsługa IO
* Wzorce projektowe
	* RAII
	* blokada z podwójnym sprawdzaniem
	* pasywny obiekt
	* reaktor, proaktor
* Z własnymi notatkami
* W kodzie może być kilka problemów, nawet jeśli w treści jest wymienione jedno
* Zadania na stronie przedmiotu

Będzie sprawdzian dodatkowy dla chętnych, do zdobycia punkty w zakresie [-6, 6], ustny, cały materiał, bez notatek, trzeba się zapisać