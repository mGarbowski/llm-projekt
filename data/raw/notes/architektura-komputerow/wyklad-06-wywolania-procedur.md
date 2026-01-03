# Wykład 06 (2023-03-08)

## Wywołanie funkcji / procedury
1. Włożenie argumentów na stos
    * W C, najpierw ostatni, pierwszy na wierzchołku stosu
2. Skok ze śladem

Powrót - załadowanie wierzchołka stosu (śladu) do PC, przed powrotem wszystkie zmienne lokalne są niszczone. Ma sens tylko wtedy kiedy na wierzchołku stosu leży ślad.

Według konwencji C, za niszczenie argumentów (zdjęcie ze stosu) odpowiada funkcja wołająca 


## Realizacja stosu
Przykładowa, prosta, współcześnie robi się bardziej wydajnie

* Pojedynczy, ciągły obszar w przestrzeni adresowej
* Adres wierzchołka stosu jest trzymany w specjalnym rejestrze (SP - Stack Pointer)
  * typowo wierzchołek oznacza adres ostatnio wwpechniętej danej
  * typowo rośnie w kierunku mniejszych adresów
* Operacje
  * PUSH - zmniejszenie SP o rozmiar danej i umieszczenie jej pod podanym adresem
  * POP - zdjęcie danej ze stosu i potem zwiększenie SP

Stworzenie / zniszczenie zmiennej - zmiana PC ale dane zostają w pamięci, znikają z punktu widzenia programu, zainicjowana zmienna ma taką wartość jaka ostatnio była tam w pamięci, `PC+=sizeof(data)`, `PC-=sizeof(data)`


## Sekcja statyczna
Przed uruchomoieniem programu adres każdej danej statycznej (TEXT, zmienne statyczne) jest dokładnie znany. Assembler tłumaczy symboliczną nazwę procedury na konkretną wartość liczbową - adres.

Ostateczną konsolidację programu robi współcześnie system operacyjny (Address Space Randomization)

## Sekcja dynamiczna
Obiekty dynamiczne nie mają stałych adresów, nie mogą być znane przed uruchomieniem

* argumenty i zmienne lokalne procedur
* obiekty alokowane na stercie
* zmienne statyczne wątku
* zmienne statyczne bilbiotek współdzielonych


## Promocja całkowitoliczbowa
Dotyczy tylko argumentów procedur

Dla procesora 32-bitowego
* adresy są 32-bitowe i typ int ma 32 bity
* obowiązuje wyrównanie naturalne
* wszystkie dane krótsze niż int zajmują na stosie tyle co int


## Ramka stosu
Procedura ma dostęp do zmiennych globalnych i do własnych zmiennych lokalnych - własny kawałek stosu - ramka stosu procedury

Argumenty + ślad -> rekord aktywacji procedury

Adresowanie danych w ramce stosu -> jako suma SP i stałej (przesunięcie). Jeśli nie jest procedurą liściem to wartość wierzhołka stosu może się zmienić i trzeba użyć innych przesunięć, kompilator może to wyliczyć, trudno to debuggować