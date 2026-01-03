# ZPR- W06 -2020 11 10

## Łączenie C i C++
* Kompilatory muszą być zgodne
	* w taki sam sposób reprezentować dane
* Problemy
	* dekorowanie nazw dla linkera
	* struktury danych
	* funkcja main
	* operacje na stercie

### Dekorowanie nazw
* W C nazwy nie mogą być przeciążone, a w C++ tak
* `extern "C" { ... }` - zapobiega dekorowaniu nazw
* Typy wbudowane, struktury i unie są wspólne dla obu języków
* Funkcja z bloku będzie bezpieczna do użycia w kodzie C

### Funkcja main
* Należy wybrać tą z C++
	* zapewnia prawidłową inicjację składowych statycznych
	* zapewnia wołanie destruktorów składowych statycznych

### Struktury danych
* Wymieniać dane między modułami tylko za pomocą
	* typów wbudowanych
	* POD - plain old data
	* struktur bez funkcji wirtualnych

### Zarządzanie stertą
* Obiekty zaalokowane przez `new` powinny być zwalniane przez `delete`
* Pamięć zaalokowana przez `malloc` powinna być zwalniana przez `free`

## Łączenie C++ i Python

### Python
* Język interpretowany
* Dynamiczna kontrola typów
* Brak enkapsulacji
* Zarządzanie pamięcią przez garbage collection
* Dokumentacja w kodzie źródłowym
* Zmienna liczba argumentów funkcji i metod
* Wszystkie metody zachowują się jak wirtualne
* `isinstance`, `issubclass`
* Można dodawać metody do obiektu dynamicznie, w trakcie działania
* Pakiety
	* katalog zawierający plik `__init__.py`, może być pusty
* Ścieżka poszukiwań modułów
	* `sys.path`
	* zmienna środowiskowa `PYTHONPATH`
* Automatyczna instalacja pakietów

### Potrzeba użycia różnych języków
* Nie ma języka do wszystkiego
* System komputerowy zawwsze
	* ma ograniczenia czasowe, tworzenie całości powinno być możliwie szybkie
	* posiada pewne elementy, które są wąskim gardłem - powinny być zaimplementowane wydajnie (20% kodu)
* System komputerowy często
	* posiada elementy, których autor nie chce udostępniać (ukryć kod źródłowy przed użytkownikiem)
	* posiada pewne fragmenty, które powinny być dostępne dla użytkownika (aby dostosować aplikację do indywidualnych potrzeb, np. konfiguracja)
* Powody rozszerzenia Pythona w C++
	* kod wykonywany jest szybciej
	* wykorzystanie istniejącego kodu
	* kod jest ukryty przed użytkownikiem
* Powody osadzenia Pythona w C++
	* brak potrzeby kompilacji
	* wykorzystanie bibliotek Pythona
	* kod dostępny dla użytkownika
* Interfejsy
	* Python C API
	* Boost Python
* Interpreter Pythona jest dostarczony jako biblioteka dzielona