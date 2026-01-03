# Dobry styl programowania

## KISS
* Keep It Simple Software
* Prosty projekt
* Pojedyncza odpowiedzialność
* Przedkłada się czytelność kodu nad jego optymalność
	* najpierw identyfikuje się wąskie gardła w działającej aplikacji i potem optymalizuje

Programista spędza więcej czasu na czytaniu kodu niż na pisaniu, dla wydajnej pracy kod musi być czytelny.


## Standardy kodowania
* Podział na pliki źródłowe
* Nazewnictwo
	* format - inaczej zmienne, inaczej stałe itd.
* Formatowanie kodu źródłowego
* Konsekwentne stosowanie stylów kodowanie


## Narzędzia

* Wykrywanie błędów w programach
	* Kompilator (translator)
	* Stosujemy najwyższy poziom ostrzeżeń i dążymy do czystej kompilacji bez ostrzeżeń
	* Ostrzeżenie to błąd projektu
* Zarządzanie kodami źródłowymi
	* Stosowanie repozytoriów
	* git
* Systemy do automatycznej kompilacji
	* Kompilacje można podzielić na fazy
	* Nie wszystko trzeba kompilować jeśli kod się nie zmienił
	* Można rozproszyć obliczenia
* Optymalizacja oprogramowania
	* Nie optymalizować jeśli nie ma potrzeby
	* Najpierw skupić się na poprawie złożoności obliczeniowej algorytmu

## Najczęstsze przyczyny niepowodzenia projektu
* Niestabilne wymagania
* Optymistyczna estymacja kosztów realizacji (przede wszystkim czasu)
* Niska jakość oprogramowania
	* kod złej jakości ale działający to tak jakby go nie było

## Typowe warunki pracy programisty
* Praca z kodem zastanym - bardzo rzadko tworzy się aplikacje od początku
* Paleta narzędzi
* Wirtualizacja, konteneryzacja


## SCons
* Narzędzie do budowania projektu
* Opis projektu to skrypt Pythona
* Łatwo rozszerzalny
	* automatyczna analiza zależności
	* wsparcie dla wielu języków, bibliotek itd.
	* wsparcie dla wielu systemów operacyjnych
	* wsparcie dla kompilacji równoległej
	* detekcja zmiany zawartości plików przy użyciu sygnatury MD5


## Obiektowe wzorce projektowe
* standardowe rozwiązania często pojawiających się problemów projektowych
* sprawdzone w praktyce
* najczęściej dotyczą programowania obiektowego
* znajomość wzorców projektowych pozwala lepiej zrozumieć obiektowe podejście do programowania

### Tworzenie nowych klas
* dziedziczenie
* agregacja
	* daje prostszą kontrolę, należy ją preferować

### Agregacja
* Budowanie z mniejszych kawałków większej całości
* "składa się z", "posiada"
* Kompozycja jest szczególnym przypadkiem agregacji

### Dziedziczenie
* Wprowadza powiązanie między typami
* "jest", "może być traktowany jako"
* Kierownik jest szczególnym przypadkiem Pracownika