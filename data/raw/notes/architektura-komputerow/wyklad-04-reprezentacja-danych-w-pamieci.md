# Wykład 04 (2023-03-01)

Każdy etap obliczeń zmiennopozycyjnych wprowadza błąd. Błędy się kumulują

## Binarny zapis liczb dziesiętnych zmiennopozpycyjnych
Historycznie wykorzystywano obliczenia na BCD (język COBOL). Współczesny standard IEEE754-2008 umożliwia precyzyjną reprezentację zmiennopozycyjnych liczb dziesiętnych.

I tak wprowadza błąd w obliczeniahc zmiennopozycyjnych ale nie ma błędu wynikającego z przeliczania na system binarny. Jest przy tym dużo bardziej oszczędny niż BCD.

Nie ma jednoznacznej znormalizowanej formy. Standard jest strasznie skomplikowany.

Declety - grupy 3 cyfr dziesiętnych zakodowane na 10 bitach.


## Organizacja pamięci
Kiedy dana zajmuje wiele bajtów, to za jej adres przyjmuje się najmniejszy adres

### Little endian
* LSB na najmniejszym adresie, MSB na największym
* numeracja bitów jest zgodna z wagami
* łatwiejsze rzutowanie typów - adres danej 8-bitowej będzie taki sam jak 32-bitowej
* większość współczesnych architektur, x86, ARM teoretycznie da się przełączyć

### Big endian
* MSB na najmniejszym adresie, LSB na największym
* Rzutowanie typu wymaga zmiany wartości wskaźnika
* Można porównywać łańcuchy znaków większymi kawałkami na raz - szybsze sortowanie tekstu
* Często używane w wielkich komputerach


Z logicznego punktu widzenia pamięć jest wektorem bajtów. Fizyczna budowa pamięci jest dwuwymiarowa, wiersze składają się ze słów 32/64/128 bitowych podzielonych na pojedyncze adresowalne bajty. Całe słowo można odczytać w jednym dostępie, czas dostępu do danych zależy od tego jak jest rozmieszczona w pamięci - będzie szybciej jeśli zmieści się w jednym wierszu pamięci.


## Wyrównanie danych
Dane układa się w pamięci w taki sposób, który pozwoli zminimalizować czas dostępu. 

Software nie musi znać szerokości słowa pamięci żeby zapewnić najszybszy możliwy dostęp. Wystarczy że dana znajdzie się pod adresem podzielnym przez jej długość - wyrównanie naturalne (size alignment). W nowych architekturach próba odczytu zapisu łamiącego tą zasadę jest zakazany i rzuca błąd.

Typ danych w definicji implementacji języka ma określone wyrównanie i rozmiar, we wszystkich współczesnych językach te wartości są równe.


## Wektory i tablice
Elementy zajmują kolejne komórki pamięci. Grupowanie danych w wektorze nie ma żadnego narzutu, cały wektor ma takie wyrównanie jak pojedynczy element.

Wielowymiarowa tablica jest wektorem wektorów.


## Struktury
Kompilator stosuje wyrównanie naturalne. Generalnie nie musi zachować kolejności zmiennych skalarnych.

Kompilator musi zachować kolejność pól struktury zgodnie z jej deklaracją (jak napisał programista). Musi tak być żeby móc utworzyć wektor struktur i zachować przenośność.

Struktura zaczyna się od adresu właściwego dla wyrównania najdłuższego wyrównania elementu struktury. Całkowita zajmowana pamięć przez strukturę jest wielokrotnością najdłuższego pola. Każdy element musi być wyrównany naturalnie.

Kolejność zmiennych decyduje o tym ile miejsca w pamięci zajmie struktura. Najlepiej posortować pola po wielkości pola. Część bajtów może być marnowana.

... obrazek


## Dane wektorowe
Procesory mają szerokie rejestry a składowe danych multimedialnych (obraz, dźwięk) zajmują typowo 8 lub 16 bitów. Żeby lepiej wykorzystać rejestry procesora, można załadować cały wektor i operować na całym wektorze na raz. 