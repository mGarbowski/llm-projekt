# Wykład 12 (2023-04-03)

## Mnożenie i dzielenie przez potęgi 2
* mnożenie przez 2^n - przesunięcie w lewo o n
* dzielenie przez 2^n - przesunięcie w prawo o n
* reszta z dzielenia - ...

## Procedury
Wywołanie jest kosztowne czasowo

Nie używa się gdy
* wywołanie jest tylko w jednym miejscu
* ciało wykonuje się w zbliżonym czasie do narzutu związanego z wywołaniem
  * zamiast procedur można używać makrogeneracji żeby unikać powtarzania instrukcji

  
Inaczej pisze się procedurę, która ma być wołana z C i która będzie wołana tylko przez inne procedury assemblerowe. Funkcja, która nie jest publicznie dostępna nie musi przestrzegać konwencji wołania C


## Pisanie pętli
Pętla powinna kończyć się skokiem warunkowym zamykającym pętle - wtedy pętla musi się wykonać minimu jeden raz (można zrobić skok bezwarunkowy do warunku końcowego tylko raz przed pętlą)

Bardziej ekonomicznie jest zrobić tylko skok warunkowy na końcu niż warunkowy na początku i bezwarunkowy na końcu

Pętle o znanej liczbie iteracji można zrealizować odliczając w dół i kończąc pętle dekrementacją licznika i skokiem do początku jeśli nie zero

Niektóre można zrealizować używając instrukcji iterowanych


## Korzystanie ze znaczników
Wszystkie operacje arytmetyczne i logiczne ustawiają znaczniki - nie trzeba jawnie wykonywać porównania

Instrukcje argumentowe ustawiają znaczniki nietypowo

## Skoki
Skoki są bardzo kosztowne, rzędu kilkudziesięciu innych instrukcji

Procesory mają układy przewidywania skoków, im mniej skoków tym wydajniej działają

Skoki zależne od wartości danych są ciężkie do przewidywania

Czasami skok można zastąpić operacją kopiowania warunkowego


## Optymalizacja wywołań procedur
### Funkcja kończąca się wywołaniem innej funkcji
Zamiast kończyć funkcji instrukcjami

```asm
call proc2
ret
```
Wtedy trzeba 2 razy zdejmować ślad ze stosu

Lepiej zrobić tylko `jmp` bez wkładania i usuwania śladu, wtedy wołana funkcja zdejmie ze stosu ślad funkcji wołającej który jest na czubku sotsu

Jeśli procedury występują w kodzie jedna po drugiej to może w ogóle nie trzeba wołać


## Typowe błędy
* Ponowne ustawienie znaczników po operacji arytmetycznej
* Skoki warunkowe przeskakujące przez skok bezwarunkowy
* Użycie mnożenia i dzielenia kiedy można było użyć przesunięcia bitowego albo LEA
* Kodowanie stałych - powinno się pisać tak jak jest najłatwiej do przeczytania
* Używanie nic nie znaczących etykiet
* Użwanie zmiennych statycznych do przechowywania danych lub rejestrów - do tego jest stos
* W procedurze powinna być tylko jedna instrukcja powrotu - inaczej trudno się debugguje


## Kolokwium
* na komputerach w laboratorium
* zwrócić uwagę na terminy!
* kilkanaście pytań
  * głównie wielokrotnego wyboru
  * mogą być obliczeniowe
    * konwersje binarno-dziesiętne
    * zmiennopozycyjne
    * precyzja we float
    * operacje z nadmiarem
    * jak są ustawiane znaczniki
    * "jaki jest wynik ośmiobitowego dodawanie liczb ze znakiem"
  * ramka stosu x86
  * układ struktur z wyrównaniem naturalnym, `sizeof`, przemieszczenie pola względem struktury, zawierająca wektory, reguła promocji przy przekazywaniu argumentów, przemieszczenie pola kiedy jest argumentem funkcji a kiedy zmienną lokalną
* są przykładowe pytania
* moodle PW
* będzie test testowy
* będą przykłady na wykładzie po świętach
* prolog i epilog
* rejestry saved i temporary

Pierwszy argument [ebp+8]

Zmienne lokalne adresy mniejsze od ebp