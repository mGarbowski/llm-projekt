# Logika rozmyta (2024-01-18)
Logika rozmyta pozwala na rozszerzenie wnioskowania na pojęcia nieostre

Zadeh

Zastosowania w automatyce - zdrowo rozsądkowe reguły w sterowaniu maszynami
Typowe zastosowanie - sterowniki ale też stosuje się do modeli regresyjnych

Zbiór (uniwersum U) i funkcja charakterystyczna dla każdego podzbioru A - należy/nie należy to zdanie logiczne

## Zbiór rozmyty i funkcja przynależności
Funkcja charakterystyczna podzbioru przyjmuje wartości z przedziału $[0,1]$
Funkcję definiuje się arbitralnie - tak żeby było wygodnie
Najczęściej trapez, trójkąt, singleton, krzywa Gaussa

Można wybrać taką funkcję przynależności które nie osiągają nigdy 1 albo 0

Wartość funkcji można traktować jako wartość logiczną w logice rozmytej

Koniunkcja - T-Norma
* jak wartości przynależności będą tylko 0 i 1 to powinna zachowywać się jak w klasycznej logice
* może być iloczyn
* może być minimum

Alternatywa - S-Norma
* może być maksimum
* może być suma - iloczyn (jak prawdopodobieństwo sumy, wzór włączeń-wyłączeń dla więcej niż 2)

T-Norma i S-Norma bierze się z pary (min i max, suma i iloczyn algebraiczne)

## Wnioskowanie
Żeby wnioskować w logice rozmytej najpierw trzeba przetłumaczyć pojęcia ze świata rzeczywistego na logikę rozmytą, przeprowadzić wnioskowanie rozmyte i potem przetłumaczyć z powrotem 

Rozmywanie i wyostrzanie korzystają z definicji funkcji przynależności

### Rozmywanie
Definiuje się kształty funkcji przynależności dla podzbiorów z uniwersum
Dla każdej wartości oblicza się wartości przynależności do wszystkich zbiorów rozmytych
Najczęściej tak się określa funkcje przynależności żeby wartości sumowały się do 1

### Wnioskowanie
* Przynależności do pojęć na wejściu
* Wnioskowanie z użyciem reguł logiki formalnej
* Przynależności do pojęć na wyjściu

### Wyostrzanie
Z wartości przynależności generuje wartość liczbową na wyjściu
Przed wyostrzaniem mogą być niezerowe przynależności do sprzecznych pojęć (jednoczesnie lubię i nie lubię, w różnym stopniu)

To jak zdefiniuje się wyostrzanie jest arbitralne

Stosuje się operator S-Normy wejściowych przynależności z wykresami funkcji a potem np maksimum albo środek ciężkości

Wygodnie przyjąć funkcje wyostrzające w postaci signletonów (Takagi-Sugeno)

Przykład z samochodem dojeżdżającym do skrzyżowania na żółtym świetle

Będzie do policzenia na egzaminie

## Budowanie systemu rozmytego
Budowa systemu rozmytego jest budową systemu regresji

### Projektowaniu podlegają
* klasy funkcji przynależności
* wybór s-normy i t-normy
* wybór sposobu wyostrzania

To sprowadza się do wyboru gotowej klasy systemu

### Strojeniu podlegają
* Liczba zbiorów rozmytych
* Parametry funkcji przynależności
* Reguły

Testowanie modelu z zadanymi parametrami w symulacjach
Można optymalizować parametry metodami przeszukiwania (gradient itd)

Można przyjąć duży zbiór potencjalnych reguł (np. iloczyn kartezjański wszystkich dyskretnych wartości) przeszukiwać zbiór podzbiorów

Trzeba mieć jakieś dane na których można by budować optymalizator, można użyć drzewa decyzyjnego do zbudowania zbioru reguł
