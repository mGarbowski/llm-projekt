# Metryki (2024-04-22)
* Metryka - miara odległości między elementami zbioru
	* służy przede wszystkim do porównywania
* W inżynierii oprogramowania - liczbowa reprezentacja wybranej cechy oprogramowania
	* powinna być obiektywnie mierzalna
* Używane do
	* oceny oprogramowania (np. jakości)
	* estymacji kosztów
	* walidacji wymagań

## Metryki i procesy
* Metryki mogą dotyczyć procesów (wytwarzania oprogramowania)
	* np. liczba otwartych issues
	* może warto śledzić wybrane metryki
* Może pomagać określać postęp w pracy
* Może pomóc pilnować oczekiwanej jakości

## Przykładowe metryki
* Wielkość programu (pliku wykonywalnego / paczki instalacyjnej)
	* żeby nowa gra nie zajmowała całego dysku
	* żeby strona internetowa szybko się ładowała
* Czas wykonania programu
* Czas ładowania programu
* Zużycie pamięci / procesora / dysku przez program
* Liczba linii kodu (LOC)
	* obiektywna
	* nie może służyć porównywaniu programów w różnych kategoriach złożoności
	* można robić zgrubne oszacowania do podobnych projektów
* Procent linii komentarzy w kodzie
	* dobre dla nagłówków bibliotek
	* w kodzie to słaby pomysł
* Złożoność cyklometryczna
	* liczba punktów decyzyjnych w kodzie + 1
	* bez żadnego `if`a wynosi 1
	* próba mierzenia złożoności kodu
	* może sygnalizować potencjalnie złe funkcje
	* źle traktuje instrukcje `switch`
* Liczba linii w funkcji / module
* Liczba argumentów w funkcji / pól w klasie
	* powiązane ze seobą argumenty można upakować w klasę
* Głębokość zagnieżdżeń w kodzie
* Warto przyjąć jakieś wartości ostrzegawcze i robić inspekcje, gdy zostaną przekroczone
* Mogą być dynamiczne i statyczne

## Metryki oprogramowania
* Mogą występować jako
	* średnie
	* maksymalne
	* zmierzone w specyficznych warunkach
* Sposób pomiaru jest elementem definiującym metrykę
* Często stosuje się skróty myślowe, ale warto pamiętać o ścisłym definiowaniu

## Metryki kodu
* Aspekty, które powinne same wyjść podczas code review
* Są obiektywne, więc mogą ucinać jałowe dyskusje
	* automat zauważy rzeczy, które mogą przemknąć przez code review
	* warto je podpiąć pod CI
	* klienci mogą wymagać *dowodów*
* Mogą zmusić do szybszego naprawiania kodu
* Bardziej ambitne metryki próbują mierzyć poziom powiązań (coupling) lub samą utrzymywalność kodu


## Metryki procesów
* Pomiarom można poddawać proces wytwarzania oprogramowania
	* to nie jest zadanie tylko dla menadżerów
* Przykłady
	* czs poświęcony przez zespół (np. w stosunku do zpalanowanego czasu)
	* częstotliwość zgłaszania problemów
	* czas rozwiązania problemów zgłaszanych przez klientów
	* *masa* w sprintach
* Warto interesować się przyjętymi w firmie metrykami
	* może pomóc lepiej pracować

## Metryki testów
* Wszystkie metryki do kodu nadają się też do testów
* Kod testu to też kod!
* Dla testów można przyjąć inne wartości metryk, ale te same zasady co do kodu stosują się do testów
	* testy to najlepsza dokumentacja
* Jest grupa metryk specyficzna dla testowania
* Pokrycie (coverage)
	* może pomóc ocenić jakość testów (w obrębie danego projektu)


### Pokrycie
* Pokrycie linii - linie kodu wywołane przez test
* Pokrycie gałęzi - ściezki kodu wykonane przez test
	* dla `if`a muszą być dwa testy żeby uzyskać 100%
* Pokrycie decyzji - każda wykonana decyzja
	* jeśli w warunku jest `and` to jest więcej niż 1 decyzja
	* w większości języków operatory są *short-circuiting* - nie ma de facto 4 możliwości dla `and`
	* pokrycie gałęzi w kodzie asemblerowym
* Pokrycie wymagań przez testy
	* mniej obiektywne
	* czy każde testowalne wymaganie ma swój test
* Jak dobrze napiszemy testy i jakiś kod nie jest pokryty to może nie jest potrzebny
* Raczej mierzy się z wyłączoną optymalizacją
	* inaczej trudno określić pokrycie bo linijki *wylatują* z kodu maszynowego
	* czesto wymaga ingerencji w kod wykonywalny
	* często wolniejsze niż przy normalnym działaniu
* Nie musi dotyczyć testów jednostkowych
* Pokrycie 100% dla całego projektu jest nierealne
	* może dla samej biblioteki albo jej konkretnych fragmentów
* To ze badamy pokrycie, nie oznacza od razu, że robimy white-box
	* pokrycie dotyczy mierzenie, a nie sposobu konstrukcji testu
	* ale trzeba mieć wgląd do kodu żeby było sens mierzyć pokrycie

### Pokrycie a jakość
* Pokrycie inne niż 100% gałęzi oznacza, że są miejsca w programie, których nie uruchomiliśmy
	* nie wiemy co się w nich dzieje
* Uzyskanie 100% jest naprawdę drogie
	* przyjmujje się że 80-90% to już dobrze
	* wszystkie moduły funkcjonalne są pokryte na 100%, a części operujące na dysku, bazie danych (funkcja `main`) itp nie są
	* oprogramowanie krytyczne musi mieć 100%
	* TDD pomaga uzyskać 100%
* 100% pokrycia nie gwarantuje poprawności działania programu
* Jakoś testu opiera się na jego konstrukcji i zgodności z wymaganiami
	* to może być niemierzalne
	* asercje muszą być odpowiednie
	* scenariusz musi być reprezentatywny
	* trzeba sprawdzać wartości brzegowe

## Jak napisać dobry test funkcjonalny
* Żeby w pełni przetestować `int fun(int a)` trzeba by napisać $2^{32}$ testów
	* chyba że wiemy coś o kodzie (white-box) albo o wymaganiach (black-box)
	* jeśli wiem że funkcja ma sens dla wartości $[0,100)$ to można napisać przynajmniej 101 testów (w przedziale i tuż za krańcami, ew. wartości minimalna i maksymalna int)
* Testowanie dla kilku reprezentatywnych wartości - **klasy równoważności**
	* dobrze zacząć pisanie testów od określenia klas równoważności

### Dobry test jednostkowy
* Automatyczny
* Powtarzalny i deterministyczny
* Szybki
* Jednoznaczny
* Skoncentrowany na pojedynczym aspekcie
* Czytelny
* Niezależny
	* zmiana kolejności wykonywania testów nie powinna wpływać na wynik

## Podsumowanie
* Nic nie zastąpi code review
* Metryki mogą pomagać wychwytywać problemy
	* porównać program z dzisiaj z programem z wczoraj
* Może dostarczyć dowodów na podparcie odczuć
* dobry kod i dobre testy to wciąż domena rzetelności i profesjonalizmu
	* automaty mogą pomóc, ale nie mogą zastąpić dobrego procesu inżynieryjnego