# Wykład 09 (2023-03-22)

Plik wykonywalna nie musi być kompletnym programem - dynamiczne linkowanie

Plik pośredni jest wynikiem kompilacji jednego pliku, trzeba w nim wypełnić odwołania do innych modułów przez linker

Odwołania są wiązane z deklaracjami na podstawie nazw (podczas linkowania)

* Symbol zewnętrzny - używany ale zdefiniowany gdzie indziej
* Symbol publiczny / globalny - zdefiniowany, przeznaczony do użycia przez inne moduły

Konsolidator znajduje symbole publiczne z innych plików powiązane z używanymi symbolami zewnętrznymi.

## Porażka linkowania
* nie ma definicji dla którgokolwiek symbolu
* więcej niż jedna publiczna definicja o tej samej nazwie


## Symbole zewnętrzne i publiczne

### W języku C
* dana zadeklarowana jako `extern`
* funkcja niezdefiniowana w danym pliku (albo prototyp funkcji bez ciała)
* każda deklaracja poza procedurą jest domyślnie publiczna
* słowo kluczowe `static` oznacza zmienną lub procedurę prywatną dla modułu, zasięg widzialności powinno się maksymalnie ograniczać

### Assembler
* wymaga jawnej deklaracji symbolu jako zewnętrznego `extern`
* nazwa publiczna musi być jawnie zadeklarowana jako publiczna `global` / `public`


## Biblioteka
Kolekcja modułów pośrednich zebranych w jeden plik

Konsolidator włącza tylko te moduły z biblioteki, któe są zadeklarowane jako zewnętrzne (razem z ich zależnościami), biblioteka jest przeszukiwania do skutku


## Program w systemie operacyjnym
* System operacyjny nie wymusza konwencji wołania
* Ogranicza adresy w pamięci jakie są dostępne dla programu (sekcje)
* Musi zakończyć się wywołanie funkcji systemowej `exit`


## Ładowanie
Adresy są określane podczas ładowania


## Podstawowe funkcje systemu operacyjnego
* open, read ,write, close, seek
  * dostęp do plików
  * to samo przy odpowiednich uprawnieniach do interakcji z IO (terminal, drukarka)
  * terminal jest widziany jako dwa pliki nie wymagające otwierania
* sbrk
  * dynamiczna alokacja pamięci
  * zwraca wskaźnik na obszar pamięci o podanym rozmiarze
* exit
  * zakończenie wykonania programu
  * argument jest kodem zakończenia (0 dla poprawnego, nie 0 dla błędu)


## Architektura x86
* Nietypowa architektura CISC
* Firma Intel
* x86 oznacza architekturę 32-bitową
* omawiany model programowy - płaski tryb 32-bitowy
* x64 / x86-64 / AMD64 / Intel 64 - rozszerzenie do 64 bitów


## Charakterystyka
* mały zestaw rejestrów uniwersalnych
  * 8 rejestrów, niektóre z przypisanymi funkcjami
  * wskaźnik ramki
  * wskaźnik stosu
  * akumulator
  * akumulator pomocniczny
  * 4 trochę uniwersalne
* Głównie instrukcje dwuargumentowe
  * rejestr-rejestr, rejestr-pamięć, rejestr-stała
  * pamięć-rejestr, pamięć-stała
  * nie ma operacji pamięć-pamięć
  * jednostka stałopozycyjna - operacje na danych 8, 16, 32-bitowych