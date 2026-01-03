# Test Driven Development

## Feedback loop
* Jak dużo czasu minie między momentem kiedy coś zrobimy, a kiedy dowiemy się jaki to coś miało efekt
	* czy kod działa
	* czy kod spełnia wymagania
	* czy system spełnia oczekiwania użytkowników
	* czy nic nie zepsuliśmy
* Sprowadza się do pytania jak długo uruchamiają się testy

## Waterfall
* Szczególnie przy przetargach
* Kolejne etapy
	* specyfikacja
	* projektowanie
	* implementacja
	* testowanie
* Specyfikacja
	* określenie wymagań funkcjonalnych itp
* Projektowanie
	* domena architektów
	* dobór technologii
	* powstają diagramy, schematy architektury itp
* Implementacja
	* domena zespołów deweloperskich
* Testowanie
	* testerzy są oddzielną grupą od osób pracujących na pozostałych etapach
	* problemy z komunikacją
	* testowanie na samym końcu
	* konflikt testerów z deweloperami
	* bez automatyzacji testów (głównie z braku czasu)

## Agile
* Podział czasu pod kątem funkcjonalności
	* dostarcza się po kolei funkcjonalności
	* krótsze fazy projektowania, implementacji, testowania
	* krótsze cykle
* Testowanie
	* testerzy są częścią zespołu
	* współbieżnie z implementacją
	* *shift left* - chcemy jak najwcześniej dostawać feedback od testerów
	* ścisła współpraca z biznesem
	* automatyzacja testów

## Extreme Programming
* Jeśli coś jest trudne to rób to częściej
* Cały kod powinien mieć testy
* Kod musi przejść wszystkie testy zanim zostanie wdrożony/wydany
* Kiedy znajdujemy błąd, dodajemy od razu test który go wykrywa

## Piramida testów
* Testy manualne
* Automatyczne testy UI
* Testy akceptacyjne
* Testy integracyjne
* Testy jednostkowe
* Im niżej na piramidzie tym więcej tego typu testów powinno być i tym szybciej można je wykonać

### Testy manualne
* Na początku koszt jest mały
* Łatwo znaleźć błędy
* Elastyczne
* Nie wszystko da się łatwo przetestować ręcznie
* Powtarzalność jest kosztowna
	* każde przeklikanie kosztuje czas

### Testy automatyczne
* Duży koszt na początku
* Konieczność poznania nowych narzędzi
* Nie wszystko da się przetestować automatycznie
	* nie wszystko warto automatyzować
* Szybki feedback
* Jednoznaczne rezultaty
* Nie tak nudne jak testy manualne
* Mniejsze koszty w dłuższej perspektywie

### Testy UI/E2E
* Testy działającej aplikacji
	* głównie oparte o przeglądarkę
* Narzędzia
	* cypress
	* playwright
* Wrażliwe na zmiany w interfejsie użytkownika
	* warto opierać asercje np. na id elementów zamiast na tekście, który może się zmieniać
* Wolne
* Duży próg wejścia

### Testy akceptacyjne
* Testują cały system
* Dokumentują jak powinna działać aplikacja
* Czytelne dla ludzi nietechnicznych
* Narzędzia
	* Cucumber
* Podejście Bhaviour Driven Development
	* opis scenariuszy w języku naturalnym, odpowiednio sformalizowany
	* można implementować odpowiednie parsowanie wyrażeń w języku naturalnym
	* czytelne jako specyfikacja
	* specification by example
	* bardzo czasochłonne
	* może być użyteczne nawet bez automatyzacji, do czytelnego opisania wymagań

### Testy integracyjne
* Test kilku warstw aplikacji
	* np. serwisu z bazą danych
* Jak komponenty wchodzą ze sobą w interakcje

### Testy jednostkowe
* Test małej funkcjonalności
	* dyskusyjne co można nazwać jednostką
	* w praktyce np. jedna metoda, jedna klasa, kilka klas
* Szybkie
* Można pokryć wiele przypadków brzegowych
* Kruche
	* wiele sposobów na jakie można źle napisać test
* Własności FIRST
	* fast
	* isolated
	* repeatable
	* self-verifying
	* timely - napisany w odpowiednim momencie
* Dają pewność że kod jest poprawny
* Pozytywnie wpływają na jakosć kodu
	* pisanie kodu tak, żeby dało się go przetestować
	* wymusza dobrą architekturę
* Pomagają w znalezieniu błędu
* Przyśpieszają pracę programisty

### Kiedy testować
* Testowanie po napisaniu kodu
	* może okazać się że kodu nie da się przetestować
	* trudniej wpaść na przypadki brzegowe
* Test przed napisaniem kodu
	* do kodu który chcielibyśmy mieć
	* zmusza do myślenia o tym jak będzie się używać kodu
* Test-Driven Development

## Test Driven Development
* Cykl red, green, refactor
	* piszemy test, który nie przechodzi
	* piszemy implementację tak, żeby test przeszedł
	* refaktoryzujemy implementację, poprawiamy jakość kodu
* Red
	* do czego dążymy, jak powinien zachowywać się system
* Green
	* piszemy tylko tyle żeby zadowolić test
	* skupiamy się na funkcjonalności, nie na estetyce kodu
* Refactor
	* zmiana struktury kodu bez zmiany działania
* Zasady TDD
	* Nie możesz napisać produkcyjnego kodu jeśli nie napisałeś wcześniej testu jednostkowego który nie przechodzi
	* Nie możesz napisać większego testu niż to konieczne żeby nie przeszedł
	* Nie możesz napisać więcej kodu produkcyjnego niż potrzeba żeby napisany test przeszedł
* Zalety
	* szybki feedback
	* jakość wbudowana w proces wytwarzania oprogramowania
	* możliwość refaktoringu
	* łatwiej wprowadzać nowe zmiany
	* inkrementalny postęp
* Efekty uboczne
	* testowalność kodu
	* lepsze zrozumienie dziedziny i kryteriów akceptacji
	* testy są żywą dokumentacją kodu
	* mniej błędów
