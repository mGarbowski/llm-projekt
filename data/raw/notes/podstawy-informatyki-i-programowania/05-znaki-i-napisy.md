# Znaki i napisy (2022-11-03)

## Alfabet Morse'a
Pierwsze ustandaryzowane kodowanie angielskiego alfabetu - Alfabet Morse'a i pierwszy telegraf. Zoptymalizowany na podstawie częstotliwości występowania znaku (częściej występujący znak kodowany mniejszą liczbą).

Pojawia się problem z rozpoznaniem gdzie zaczyna się litera jeśli dołączy się w środku transmisji.

## ASCII
American Standard Code for Information Interchange (1963)

* Znaki kodowane na 7 bitach
* 0-31 Kody sterujące (CR, LF, NUL, ESC)
    * CR (Carriage Return) - powrót na początek wiersza
    * LF (Line feed) - przejście do następnej linii
* 32 spacja
* 48-57 cyfry
* 65-90 wielkie litery
* 97-122 małe litery
    * Przesunięte o 32 względem wielkich
* 127 (DEL) kasowanie znaku

Mógł być 7-bitowy, ale zaczęto wykorzystywać MSB jako kontrolny bit parzystości.

Kody detekcyjne i kody korekcyjne - techniki pozwalające wykryć i/lub naprawić błędy w transmisji danych .


## Strony kodowe
Powstało wiele standardów pokrywających konkretne narodowe symbole.

International Standards Organization (ISO) zajęła się normalizacją stron kodowych.

Międy klawiszem na klawiaturze a wyświetleniem symbolu jest bardzo daleka droga. System operacyjny dekoduje numer klawisza na znak według wybranego układu klawiatury itd.


## Unicode
Tworzony przez międzynarodowe konsorcjum Unicode. Zwiększona potrzeba ustandaryzowania z pojawieniem się internetu.

Standard stron kodowych, każdy znak ma mieć przypisany numer (2^32 miejsc w tabeli 2^16 x 2^16). Pierwsza kolumna tabeli (64K znaków) to Basic Multilingual Plane na symbole wszystkich języków.

Znak != glif, ten sam znak może mieć być reprezentowany w różnych czcionkach i z różnymi atrybutami (podkreślenie, pogrubienie, wielkość itp.)

Numer Unicode to nie to samo co reprezentacja w pamięci komputera. Szkoda używać 4B jeśli znak zmieści się na 1B.

Wszystkie kody znaków w ASCII i Unicode są takie same.


## UTF-8
Unicode Transformation Format

Oszczędne kodowanie numerów znaków w Unicode. Rozwiązuje problem rozpoznania gdzie zaczyna się znak.

Wszystkie kody znaków ASCII i UTF-8 są takie same. Nawet jeśli plik tekstowy jest zakodowany w UTF-8 a program tego nie wspiera to większość znaków i tak wyświetli się poprawnie (bo mieści się w ASCII)

Sekwencja bajtów jest ustalona w pliku (nie zależy od specyfikacji little/big endian)

### Wady
* Znaki alfabetów niełacińskich zajmują więcej bajtów (do 6B) niż w narodowych standardach kodowania
* Niejednoznaczność zapisu
    * wiele kodów opisuje tak smao wyglądający znak np. '-'
    * sprawia problemy przy wyszukiwaniu

| liczba bajtów | bajt 1   | bajt 2   | bajt 3   | bajt 4   | bajt 5   | bajt 6   |
| ------------- | -------- | -------- | -------- | -------- | -------- | -------- |
| 1             | 0xxxxxxx |          |          |          |          |          |
| 2             | 110xxxxx | 10xxxxxx |          |          |          |          |
| 3             | 1110xxxx | 10xxxxxx | 10xxxxxx |          |          |          |
| 4             | 11110xxx | 10xxxxxx | 10xxxxxx | 10xxxxxx |          |          |
| 5             | 111110xx | 10xxxxxx | 10xxxxxx | 10xxxxxx | 10xxxxxx |          |
| 6             | 1111110x | 10xxxxxx | 10xxxxxx | 10xxxxxx | 10xxxxxx | 10xxxxxx |

Na 1 bajcie - tak samo jak ASCII

Na kilku bajtach
* w pierwszym jest tyle 1 ile bajtów ma znak, potem jedno 0
* każdy kolejny bajt zaczyna się od 10

W ten sposób rozwiązuje się problem z rozpoznaniem znaku jeśli rozpocznie się odczyt w środku transmisji

## UTF-16
* Bardziej kompaktowy dla chińskiego i japońskiego
* Musi być obsługiwany przez procesory XML
* Niezgodne z ASCII


## UTF-32
* Po prostu 32 bity kodu Unicode w NKB
* Różnica w little / big endian
* Niezgodne z ASCII


## Byte Order Mark (BOM)
Specjalny znak na początku pliku, określa sposób kodowania (wersję UTF) i little endian / big endian


## Napisy
Jak określić gdzie w pamięci kończy się napis skoro może być różnej długości

* length-prefixed string - najpierw długość, potem znaki
    * używane dawniej (Pascal)
    * szybkie określenie długości
* null-terminated string - znak specjalny na końcu (ASCII 0)
    * obecnie najczęściej używany
    * kosztowne sprawdzenie długości (szczególnie w UTF-8 gdzie nie wystarczy policzyć bajtów)

### W języku C
W programie: `char napis[] = "Hi Peter";`
W pamięci: `48 69 20 50 65 74 65 72 00` <- NUL na końcu

Napis trzeaba kopiować razem z końcowym 00 albo będą problemy.

Zmienna `napis` jest adresem piewszej litery (stąd indeksowanie od 0)

`*(napis + 1)` litera na indeksie 1 i potencjalna podatność na atak (bez sprawdzenia zakresu). To rozwiązują języki wyższego poziomu i obiekty string.


### W języku C++
`std::string napis("Hi Peter");`

Napis jako obiekt
* umieszcza ciąg bajtów zakończony 0x00 w pamięci (tak jak w C)
* rezerwuje pamięć na wydłużenie napisu
* przechowuje informacje o długości napisu - size i dostępnym (zarezerwowanym) miejscu - capacity


## Null-terminated string
* Problem przy kopiowaniu - trzeba pamiętać o końcowym 0x00
* Wstawienie 0x00 w środek napisu powoduje obcięcie, a reszta zostaje w pamięci
  * wyciek danych, potencjalny problem z bezpieczeńśtwem
* Błędne indeksowanie prowadzi do sięgnięcia do danych poza napisem

## Row hammer
Exploit bezpieczeństwa w pamięci DRAM. Zmiana zawartości komórek, które nie były zaadresowane przez odwoływanie się do sąsiednich komórek. Wykorzystuje efekt uboczny, elektryczne oddziaływanie między komórkami.
