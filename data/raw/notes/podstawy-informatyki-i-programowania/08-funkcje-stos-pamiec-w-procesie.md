# Funkcje, stos i struktura pamięci procesu

## Funkcje
Mając instrukcję skoku można skoczyć na początek fragmentu kodu, który realizuje konkretną funkcję. Trzeba jakoś wiedzieć do której instrukcji wrócić po zakończeniu funkcji.

skoczyć -> przetworzyć -> wrócić

Licznik instrukcji zwiększa się w fazie Instruction Fetch, kiedy instrukcja jest wykonywana, rejestr już trzyma adres następnej instrukcji.

* Komputer odkłada na wierzch stosu stan przetwarzania i adres powrotny dla funkcji (PC)
* Skacze do instrukcji funkcji i wykonuje operacje
* Wraca do poprzedniego stanu operacji (ze stosu)


## Stos
Struktura LIFO Last In - First Out

Ostatni włożony element wychodzi jako pierwszy


### Do zrealizowania stosu potrzeba
* operacji push
* operacji pop
* rejestru do obsługi stosu
  * SP Stack Pointer - adres wierzchołka stosu (albo pierwszego niewykorzystanego miejsca wyżej)


## Surowe wywołanie funkcji
```
    push AFTER_CALL_LABEL
    jmp FUNC_LABEL
AFTER_CALL_LABEL:
    ...

FUNC_LABEL:
    ...
    pop PC
```

### Ramka wywołania
Adres powrotny zrzucony na stos

* Odłóż adres powrotny na szczyt stosu
* Skocz na początek funkcji
* Po wykonaniu funkcji zdejmij zdejmij adres powrotny z wierzchołka stosu i zapisz go do PC - skok
* Zagnieżdżone wywołania spowodują wrzucenie na stos kolejnych ramek wywołania


## Instrukcje call i ret
Można uprościć surowe wołanie funkcji przez wprowadzenie specjalnych instrukcji

### Call
Zrzuca na stos adres następnej instrukcji po `call` i robi skok do adresu docelowego funkcji

### Ret
Zdejmuje ze stosu adres powrotny do rejestru Program Counter (wykonuje skok)

```
    call FUN_LABEL
    ...
FUN_LABEL:
    # kod funkcji
    ret
```

Nie trzeba przygotowywać ani sprzątać stosu - zrobi się automatycznie


## Zwrócenie wyniku z funkcji
* Do rejestru procesora (w x86 standardowo do EAX lub RAX)
  * wartość może się nie zmieścić w rejestrze
* Wkorzystując ramkę wywołania funkcji
  * zarezerwować w ramce miejsce na wynik

Kompilator może przeznaczyć rejestr na odłożenie wyniku bez zapisywania go w pamięci i wczytaniu z powrotem - trzeba ustalić konwencję mechanizmu wywoływania.

## Zachowanie kontekstu
Funkcja z zagnieżdżonego wywołania też potrzebuje rejestrów, żeby wykonać swoje operacje.

Wywołanie funkcji zależy od stanu rejestrów procesora. Trzeba je zachować przed skokiem i odtworzyć po powrocie, żeby funkcja mogła mieć dostęp do swoich danych.


Można to zrealizować przez odłożenie stanu rejestrów na stosie przed i zdjęcie ze stosu po wykonaniu skoku.


## Przekazanie argumentów do funkcji
* Przez rejestry procesora
  * najczęściej się nie zmieszczą
* Przez ramkę wywołania
  * trzeba zarezerwować w niej miejsce na argumenty

### Parametr funkcji
W kodzie statycznym (wewnątrz funkcji)

### Argument funkcji
W momencie wywołania funkjci przypisane jako wartość parametrów


## Zmienne lokalne
Muszą być widoczne tylko w ramach konkretnego wywołania, w zagnieżdżonym wywołaniu, zmienne nazywają się tak samo i trzymają inne wartości.

Można je trzymać w ramce wywołania na stosie. Po powrocie z wywołania przestaną istnieć\* razem z ramką (będą możliwe do nadpisania ale w rzeczywistości zostaną na stosie).

Argumenty też są zmiennymi lokalnymi.


## Rejestr bazowy (Base Pointer) - EBP
W trakcie wykonywania funkcji na stosie są trzymane informacje o adresie powrotu itp. Ale stos może pracować podczas wykonywania funkcji. SP nie nadaje się do adresowania zmiennych lokalnych, ale sposób adresowania musi być jakoś uzależniony od wierzhołka stosu.

EBP przechowuje adres bieżącej ramki. Sam musi być przechowywany w ramce i zostać odtworzony po powrocie z funkcji. Służy do adresowania zmiennych lokalnych w ramach aktualnej ramki.


## Ramka stosu w x86

| Adres względem EBP | Zawartość                                              |
| ------------------ | ------------------------------------------------------ |
| [ebp+16]           | Trzeci argument funkcji                                |
| [ebp+12]           | Drugi argument funkcji                                 |
| [ebp+8]            | Pierwszy argument funkcji                              |
| [ebp+4]            | Poprzedni PC - adres powrotny z funkcji                |
| [ebp]              | Poprzedni EBP - adres bazowy ramki funkcji wywołującej |
| [ebp-4]            | Pierwsza zmienna lokalna                               |
| [ebp-8]            | Pierwsza zmienna lokalna                               |
| [ebp-12]           | Pierwsza zmienna lokalna                               |

* Stos rośnie "w dół" - w stronę niższych adresów
* Zmienne lokalne i argumenty adresowane względem EBP
* Przesunięcia względem EBP są takie same dla każdego wykonania danej funkcji (określone w momencie kompilacji)
* Argumenty na początku ramki - muszą być znane przed samym wywołaniem
* poprzedni PC i poprzedni EBP na środku ramki
* Zmienne lokalne na końcu ramki


## Czemu stos rośnie w dół
Ze względu na sposób organizacji pamięci procesu przez system operacyjny.

* Procesor przełącza się między wykonywaniem różnych procesów (context switch)
* Do odtworzenia stanu procesu trzeba odtworzyć stan rejestrów
* Scheduler wybiera procesy do odtworzenia, po sygnale przerwania
* Proces dostaje pamięć wirtualną
* OS wirtualizuje dostęp do pamięci i decyduje kto gdzie może się dostać

### Mechanizm stronicowania pamięci
* Proces użytkownika nigdy nie dostanie całej pamięci
* Część pamięci zawsze zajmuje sam system operacyjny, musi być wmapowany w pamięć wirtualną procesu
  * w 32 bitowym systemie (4GiB pamięci) 1GiB jest zarezerwowany na kernel, dla procesu użytkownika zostają 3GiB
  * procesy mogą wywołać funkcje kernela
  * wywołania funkcji kernela przez 2 różne procesy muszą być oddzielone
* Część pamięci jest zarezerwowana na wektor przerwań
  * potrzebny do przełączania procesów

Program ma dostęp tylko do środkowej części pamięci

![Układ pamięci w procesie](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fkangxiaoning.github.io%2Fimages%2Fos%2Flinux-process-memory-layout.png&f=1&nofb=1&ipt=039885e9134c772a6baa0e859eea0fd65788888eaccd44d147c379d108e446be&ipo=images)

### Segmenty pamięci
* Text segment - kod assemblerowy wykonywanych instrukcji
* Data - wartości statyczne
* Niezainicjalizowane dane
* Sterta
  * obiekty, których rozmiar jest nieznany w czasie kompilacji
  * nie da się zarezerwować pamięci na stosie jeśli nie wiadomo ile potrzeba
* Stos
* Kernel

Stos rośnie z góry na dół a sterta z dołu na góre - rosną do środka. Lepiej żeby się nie spotkały.


## Przekazywanie argumentów
* Wartość
  * wywołana funkcja dostaje kopię wartości
  * oryginał się nie zmienia
* Adres (pointer, wskaźnik)
  * wywołana funkcja dostaje adres
  * zmienia oryginalną wartość
* Referencja
  * to samo co przez adres tylko z prostym zapisem (bez `*` i `&` jak w C++)


## Python
W Pythonie wszystko jest przekazywane przez referencję

* typy mutowalne - referencja na obiekt oryginalny
* typy niemutowalne - przy zmodyfikowaniu zmiennej powstaje nowy obiekt więc zachowuje się jak przez wartość

```py
b = a
```
Przypisuje do zmiennej `b` referencję na obiekt na który wskazuje zmienna `a`


### Kopia płytka
```py
b = copy.copy(a)
```
Kopiuje obiekt z referencji zmiennej `a`

Ale np. dwie różne listy trzymają referencje na te same obiekty

### Kopia głęboka
```py
b = copy.deepcopy()
```

Kopiuje rekurencyjne wszystkie zagnieżdżone obiekty

Nie kopiuje typów niemutowalnych - one i tak się nie zmieną, każda ich modyfikacja tworzy nową instancję i zmieni tylko jedną referencję


## Lambda
Skoro zmienna jest adresem i funkcja jest adresem to:

* można przypisać funkcję do zmiennej
* można przekazać funkcję jako argument do innej funkcji
* można zwrócić funkcję jako wynik innej funkcji

Funkcja nie musi być nazwana

```py
action = lambda message, data: print(message + str(data))
```
```py
def action(message, data):
    print(message + str(data))
```

## Rekurencja
Funkcja może wywołać sama siebie

```py
def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    return 1
```

* Rekurencji musi się kiedyś skończyć, inaczej skończy się pamięć.
* W interpreterze Pythona jest ustawiony limit
* W językach kompilowanych - system operacyjny blokuje sięganie po niedozwolone fragmenty pamięci (poza pamięć przydzieloną dla stosu)
  * Segmentaion fault - przerwanie przy sięgnięciu po niedozwolony segment pamięci, system zabija proces
  * System może nie mieć modułu zarządzania pamięcią - stos zajmie całą przestrzeń adresową


## Buffer overflow
Napis jako zmienna lokalna znajduje się w ramce stosu, da się sięgnąć po dalsze komórki pamięci (ignorując znak końca napisu).

Skopiowanie dłuższej zawartości do zbyt krótkiego bufora może nadpisać adres powrotny który też znajduje się w ramce. Na przykład adres do złośliwego kodu wstrzykniętego gdzieś dalej w buforze. 

```c
int main(int argc, char* argv[]) {
    func(argv[1]);
}

void func(char* v) {
    char buffer[10];
    strcpy(buffer, v);
}
```

![Schemat stosu przy buffer overflow](./obrazy/https://cdn.acunetix.com/wp-content/uploads/2019/06/11110858/buffer-overflow-910x471.png)

NOP - no operation - nic nie robi

W języku C, funkcje `printf`, `sprintf`, `strcat`, `strcpy` i `gets` nie mają żadnych zabezpieczeń przed buffer overflow.

Zmienne po powrocie z wywołania funkcji pozostają na stosie dopóki nie zostaną nadpisane - kolejne niebezpieczeństwo np. do wykorzystania przy buffer overflow.