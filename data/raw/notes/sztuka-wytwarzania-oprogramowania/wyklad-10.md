# Refaktoring (2024-05-13)
* Modyfikaja projektu aplikacji bez zmiany jej funkcjonalności
	* kod ale też projekt wyższego poziomu
* Ma na celu poprawę jakości i utrzymywalności projektu (kodu)
* Nie jest odrębnym procesem, tylkko stałym elementem pracy
	* w TDD jest obowiązkowy w każdym mini-cyklu
	* w dużych/starych projektach może być wymagany żeby dodać obsługę nowego wymagania
	* jeśli jest na to czas to warto poprawiać każdy zły kawałek kodu
* Książka Refactoring - Martin Fowler

## Po co refaktoryzować
* Dług techniczny projektów rośnie
	* entropia w układzie izolowanym może tylko wzrastać
	* kapitalizuje odstetki - robi się coraz gorzej z każdym odroczeniem poprawy
* Nikt nie pisze idealego kodu
	* code review wymusza refaktoring
* Kod gnije (code rot)
	* nowe wymagania mogą być niewygodne do implementacji
	* zmiany w jednej części kodu mogą wpłynąć na to jak inny fragment pasuje do reszty
	* wiedza zespołu się powiększa w trakcie tworzenia projektu, niektóre rzeczy można później zrobić lepiej
	* zmiany technologii, nowe biblioteki, moda

## Błędy refaktoringu
* Przepisanie od zera to nie refaktoring
	* najczęściej strzelanie sobie w stopę
* Nie ruszać czegoś co działa
	* zależy co się rozumie przez *działa*
	* utrzymywalność często definiuje czy biznes działa (a nie tylko kod)
* Strach przed regresją oprogramowania
* Jedyne co pomaga to testy
	* najlepiej jeśli pokrywają całość oczekiwań klienta
	* pokrywają przynajmniej część, którą chcemy refaktorować
* Strach przed ugrzęźnięciem w refaktoringu
	* trzeba wiedzieć kiedy przestać

## Dobry refaktoring
* Robiony małymi krokami
* Testowany na każdym kroku
	* czy funkcjonalność nie jest zmieniana
* Spowodowany możliwie obiektywnymi powodami
* Zazwyczaj robiony przy okazji innego zadania
* Zakończony w rozsądnym czasie
	* nie ma dobrej reguły

## Po czym poznać że kod wymaga refaktoringu
* Zgniły kod posiada zapachy (code smells)
* Zduplikowany kod
* Nieczytelne nazwy
* Długa metoda
* Duża klasa
	* jeśli większość metod używa większości składowych to raczej jest ok
* Dużo parametrów
	* grupowanie w obiekty
	* w C++ są bezkosztowe abstrakcje
* Parametry boolowskie 
	* lepiej użyć enum, bardziej czytelne
* Złamane reguły SOLID
* Zazdrość (feature envy)
* Zlepki danych (data clumps)
	* `Point` zamiast `x, y, z`
* Obsesja prymitywów
* Wyrażenie switch
	* nie każde użycie jest złe
	* często przy przetwarzaniu serializowanych danych
	* nie powinien zastępować polimorfizmu
* Złożony schemat dziedziczenia
* Nieuzasadniona generyczność
	* warto pisać generyczny kod jeśli jest taka potrzeba
* Tymczasowa wartość
	* `int tmp`
	* `std::swap`
* Wywołania łańcuchowe
	* `a().b().c()`
	* są użycia które są ok
* Komentarze
	* komentarz zostawiony w miejscu którego nie potrafiłem zrobić lepiej
	* zostaje tech debt dla następnej osoby

## Operacje refaktoryzujące
* Extract Method
* Inline method
	* dla krótkiej metody wywoływanej w jednym miejscu
	* operacje są odwracalne
	* refaktoring można robić w obie strony
* Replace Temp with Query
	* `int tmp = f(); g(tmp);`
	* `g(f())`
	* zależy co będzie bardziej czytelne
* Move Method / Field
* Extract / Inline Class
* Remove Middle Man
	* może stać w sprzeczności ze wzorcami projektowymi (bridge, proxy)
* Encapsulate Field
	* dobry setter to taki, który coś sprawdza
	* jeśli para get/set nic szczególnego nie robi to równie dobrze można zamienić pole na publiczne
* Rename Method / Field
* Collapse Hierarchy
* Pull Up Field / Method
	* przesunięcie w hierarchii klas
* Push Down Field / Method
* Extract Interface / Superclass
* Separate Query From Modifier
	* jeśli metoda cokolwiek zwraca to powinna być `const`
	* oddzielne metody które coś zwracają i które modyfikują stan
* Replace Parameter with Explicite Methods
* Replace Inheritance with Delegation


## Jak refaktorować
* Trzeba mieć testy
	* szybkie testy jednostkowe są najwygodniejsze
	* ale nie wszystko sprawdzą
* Małe kroki
* Nie bać się refaktorować starego kodu
* Nie robić od razu rewolucje
* Nie naruszać lokalnego standardu kodowania
	* o ile nie wymusza złych praktyk
	* ewolucyjne zmiany
* Przede wszystkim realizować potrzeby klienta
* Może być tak źle że trzeba go zaplanować
	* ciężko przekonać żeby ktoś za to zapłacił

## Refactoring Katas
Dobre linki do trenowania przed lab 4