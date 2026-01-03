# Wykład 03 (2023-02-27)


## Dane alfanumeryczne

### ASCII
* 128 pozycji, 7 bitów w podstawowej wersji
  * alfabet łaciński
  * cyfry
  * znaki interpunkcyjne, arytmetyczne
  * 95 znaków widocznych, 33 kody sterujące
* 256 pozycji, 8 bitów w wersji rozszerzonej do lokalnych potrzeb
* grupy symboli zaczynają się od pozycji o numerach 32 lub 16
  * (32) spacja
  * (48) cyfry
  * (65) wielkie litery
  * (97) małe litery
* kody sterujące
  * CR - carriage return - powrót na początek wiersza
  * LF - line feed - przejście do następnego wiersza
  * CAN - kasowanie znaku
  * na końcu linii CR, LF (Unix) lub CRLF (Windows)


### EBCDIC
* Używane przez komputery IBM
* 8 bitowe
* bazowany na BCD


### Unicode
* Reprezentacji wszystkich znaków używanych na świecie
* 32 bitowy, de facto 2^21 pozycji
* wstecznie kompatybilny z ASCII

### UTF-8
* reprezentacja znaku unicode na zmiennej liczbie bajtów
* wstecznie kompatybilny z ASCII
* można rozpoznać gdzie zaczyna się znak


### Zapis łańcuchów tekstowych (string)
Program musi wiedzieć gdzie kończy się łańcuch albo jaka jest jego długość
* łańcuch zakończony znakiem NUL (0x00) - C
* zapisanie liczby określającej długość na początku - Basic


## Dźwięk
* 8 kHz, 8 bitów - próbkowanie wystarczające do zrozumiałego przekazania mowy
* 48 kHz, 16 bitów - standard


## Obraz rastrowy
* prostokątna macierz pikseli
* pixel - picture element
* RGB 24-bitowe nie odzwierciedla możliwości ludzkiego oka


## Jednostki informacji
* tetrada - 4 bity
* oktet - 8 bitów
* bajt - różnie, zazwyczaj 8 bitów
* słowo - jednostka na której operuje komputer, zazwyczaaj 1/2/4/8/16 bajtów
* słowo procesora - jesdnostka informacji o długości naturalnej dla danego procesora (długość rejestru), 32 lub 64 bity
* słowo pamięci ...


## Zapis danych boolowskich
Wystarczyłby jeden bit ale większość architektur operuje minimalnie na bajcie.

Standardowo przy czytaniu wartość 0 oznacza fałsz, a dowolna inna oznacza prawdę. Przy zapisywaniu, językach pochodnych od C, prawda jest zapisywana jako liczba całkowita 1, w Visual Basic jako ciąg samych `1`.

W C są oddzielne operatory boolowskie (`||`, `&&`, `!`) i bitowe (`|`, `&`, `~`). Języki, które nie mają tego rozróżnienia zachowują się jak operatory bitowe. Trzeba uważać przy operacjach i przekazywaniu danych między programami używających innych reprezentacji.


## Zapis danych liczbowych

### Liczby ze znakiem
* Kod uzupełnień do dwóch (U2)
  * jedyny wykorzystywany współcześnie
* Kod uzupełnień do jedynek (U1)
* Kod znak-moduł (ZM)
* Zapis spolaryzowany (biased)
  * wykładnik w liczbie zmiennopozycyjnej
  * wygodniejszy przy projektowaniu FPU

### Własności sposobu kodowania
* Reprezentacja zera
* Symetria zakresu
* Reprezentacja znaku
* Zamiana znaku
* Łatwość wykonywania operacji arytmetycznych
  * dodawanie i odejmowanie U2 realizują identyczne układy do NKB
  * inaczej wykrywa się przepełnienie w NKB i U2
  * mnożenie dwóch n-bitowych liczb z wynikiem 2n-bitowym jest inne ale z n-bitowym wynikiem realizuje je identyczny układ co NKB

  
### Binary Coded Decimal (BCD)
* Wykorzystywany historycznie dla liczb dziesiętnych stałopozycyjnych.
* Używa 4 bity na każdą cyfrę
* Postać spakowana - 2 cyfry na bajt
* Postać niespakowana - 1 cyfra w bajcieh


### Zapis stałopozycyjny
* Przesunięcie wag w zapisie całkowitoliczbowym
* Takie same operacje arytmetyczne jak na liczbach całkowitych (ze skalowaniem przy mnożeniu i dzieleniu)
* Nie wymaga oddzielnych instrukcji dla procesora
* Dokładny wynik


### Zapis zmiennopozycyjny
* Standard IEEE754/IEC60559
* Bazuje na notacji wykładniczej
* Postać znormalizowana - część całkowita równa 1
* Wartości specjalne
  * +/- nieskończoność
  * głośna nieliczba - jednostka sygnalizuje błąd (na poziomie sprzętu) kiedy będzie podana jako argument
  * cicha nieliczba - jednostka przepisuje argument na wynik ale nie sygnalizuje błędu (dopiero na koniec obliczeń) 

Standardowe formaty
* binary32 (IEEE single)
* binary64 (IEEE double)
* BF16 - używany w sztucznej inteligencji
* 128-bitowa - obliczenia o wysokiej precyzji, nie wspierane sprzętowo (póki co)

Będzie przeliczanie IEEE single na kolokwium


## Arytmetyka zmiennopozycyjna
* Reprezentacja i wynik operacji są przybliżone
* Dodawanie nie jest przemienne, należy wykonywać w kolejności rosnącej wartości bezwzględnej
* Nie należy używać relacji równości, tylko `abs(a-b) < epsilon`
* 32-bitowy float ma mniejszą precyzję niż 32-bitowy int