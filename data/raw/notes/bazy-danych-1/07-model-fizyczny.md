# Składowanie i dostęp do danych
Model fizyczny

Na poziomie fizycznym dokonuje się denormalizacji, żeby optymalizować czas (a nie poprawność).

Można podzielić tabelę pionowo, żeby oddzielić te kolumny do których częściej odwołują się zapytania

Można dodać kolumnę, która jest często dołączana

Tego typu optymalizacje wykonuje administrator bazy (nie dzieje się automatycznie) na podstawie logów zapytań albo przewidywań na etapie projektowym

* Na poziomie logicznym dążymy do zachowania spójności
* Na poziomie fizycznym dążymy do zapewnienia najlepszej szybkości

### Model fizyczny
Opiera się na pojęciach pliku i rekordu

* plik obiektu bazy danych składa się z rekordów w tym samym formacie (najczęściej)
* Rekordy są grupowane w bloki (bo z dysku do pamięci odczytuje się dane sektorami)
* Format rekordu jest listą nazw pól z określeniem typów danych
* Na poziomie fizycznym klucze identyfikujące rekordy mogą być niejednoznaczne


Operacje set-at-a-time

### Organizacja i metody dostępu
* zapis sekwencyjny
* użycie funkcji haszującej
* struktury drzewiaste

## Zwiększanie wydajności dostępu do danych na dysku
* Buforowanie danych
* Odpowiednia organizacja danych na dysku
* Wczytywanie danych przed zgłoszeniem żądania
* Odpowiednie szeregowanie żądań wejścia-wyjścia

## Metody organizacji plików
* Plik stertowy - nieuporządkowany
  * kiedy często są czytane wszystkie rekordy
  * stosowane razem z indeksami - w indeksie szuka się szybko po kluczu i dostaje wskaźnik na miejsce gdzie są powiązane dane
* Pliki sekwencyjne
* Pliki uporządkowane
  * porządkowane w trakcie zapisu
  * wolniejszy zapis ale szybsze przeszukiwanie (logarytmiczne)
* Pliki mieszające - haszowane
* B-drzewa


## Klastrowanie
Fizyczna organizacja danych odzwierciedla niektóre aspekty organizacji logicznej

Jeśli tabele są często złączane to można przechowywać je złączone na dysku. To zależy jakie operacje wykonuje się częściej, trzba policzyć czy trade-off się opłaca


## Indeksy
Pomocnicza struktura przyspieszająca dostęp do danych (drzewa, haszowanie, bitmapy)

Zapytanie może skończyć się na indeksie

### Rodzaje
* indeks podstawowy (primary) - na atrybucie porządkującym plik (klucz główny)
* indeks zgrupowany (clustering)
* indeks pomocniczy (secondary) - na atrybucie, który nie musi być unikalny

* gęsty - dla każdego rekordu
* rzadki - tylko dla wybranych rekordów


## B+ drzewo
* Zrównoważone drzewo
* Węzły wewnętrzne służą do wspomagania wyszukiwania
* Węzły liści zawierają rekordy indeksu ze wskaźnikami do rekordów
* Wiele kluczy i dzieci w jednym węźle
* Różni się od B-drzewa tym, że właściwe informacje znajdują się tylko w liściach
* Liście są też połączone poziomo (do wyszukiwania zakresów)

## Indeks z funkcją haszującą
* Funkcja haszująca oblicza bezpośrednią lokalizację rekordu danych w tablicy
* Występują konflikty

## Indeks bitmapowy
* Funkcja charakterystyczna
* Dodaje się wektory dla złożonych warunków
* Zakresy, kubełki

Sposób przechowywania danych i sposób dostępu to oddzielne rzeczy 