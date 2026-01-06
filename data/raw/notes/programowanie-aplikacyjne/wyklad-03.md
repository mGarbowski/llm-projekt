# Wykład 03 (2023-10-18)

Java jest kompilowana do kodu pośredniego - pliki *.class

Java Virtual Machine - wykonuje kod pośredni
Java Runtime Environment - zawiera JVM, nie zawiera kompilatora i debuggera, potrzebny do wykonywania programów
Jaa Development Kit - zawiera JVM, potrzebny do tworzenia programów
Java Standard Edition - do aplikacji Desktop
Java Enterprise Edition (Jakarta EE) - do aplikacji korporacyjnych


Make porównuje timestampy między plikami `.c` a `.o`, w `#include` zawiera się tylko pliki `.h`, nigdy `.c`
Biblioteki statycznie linkowane są umieszczane w pliku wykonywalnym

W Javie nie ma linkowania, wynikiem kompilacji jest katalog plików `.class`
Uruchamia się jeden z plików, który zawiera funkcję `main`
Po odwołaniu do innej klasy jest ładowany odpowiedni plik w classpath
Uruchamianie programu to uruchomienie interpretera, który dopiero zaczyna wykonywać aplikację
Tak naprawdę to nie jest interpreter tylko kompilator Just-In-Time

## Porównanie Javy do C++
* Java daje łatwą przenośność między architekturami
* Jest językiem obiektowym - bez globalnych zmiennych i funkcji
* Wszystkie klasy dziedziczą z klasy Object
* Nie ma wielokrotnego dziedziczenia, można implementować wiele interfejsów
* Pojęcie interfejsu - definicja fukncjonalności i atrybutów bez implementacji
* Obiekty zawsze są referencją, obiekty tworzy się używając `new`, żyją na stercie
* Na stosie żyją tylko zmienne proste (w tym referencje)
* Automatyczne zarządzanie pamięcią - zwalnia się sama, bez jawnej dealokacji
    * Programista nie musi się tym martwić i nie może zrobić błędu (chyba że się bardzo postara)
    * Nie ma pointerów, obiekt nie musi być przez cały czas w tym samym miejscu (i tak nie można dostać jego adresu), OS ma łatwiej przy zarządzaniu pamięcią
    * Garbage Collector okresowo przesuwa obiekty w pamięci, może inteligentnie wybierać na to momenty
    * Liczy się referencje do obiektu, kiedy liczba spadnie do 0, obiekt można zwolnić z pamięci
    * Zwalniany obiekt może trzymać zasoby nie należące do Javy (np. uchwyty do plików) i źle napisany program może ubić system
    * Część zasobów trzeba zwalniać samodzielnie
* Struktura pakietów odwzorowuje położenie plików źródłowych i katalogów

## Konwencja języka
* Nazwy klas w `PascalCase`
* Nazwy pól i metod w `camelCase`
* Nazwy stałych `WIELKIMI_LITERAMI`

Convention over configuration - jak robimy coś zgodnie z konwencją to nie trzeba tego konfigurować, kiedyś ludzie musieli pisać dużo xmla

Stringi są niemutowalne

Kolokwium - połowa punktów za napisanie prostego programu commandline'owego na papierze......
porównania stringów

Język statycznie tpyowany - typ zmiennej jest określany w momencie deklaracji zmiennej

* byte - i8

domyśle dodawanie nie wyłapuje przepełnienia (ale są do tego klasy)
Do typów prostych są wrappery

Domyślnie Stringi używają UTF-16 !


