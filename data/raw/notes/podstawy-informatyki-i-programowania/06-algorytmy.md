# Algorytmy

Dekompozycja problemu

Dobra inżynieria oprogramownia - niskie sprzężenie między warstwami programu

Mieszanie odpowiedzialności w kodzie utrudnia testowanie

W Pythonie wszystko jest obiektem przekazanym przez referencję


## Dobry algorytm
* Jednoznzaczny
  * kłóci się z niektórymi paradygmatami programowania (deklaratywnym)
* Dowolny sposób opisu
  * język naturalny
  * postać graficzna
* Nie określa sposobu implementacji
  * nadaje się do implementacji np. w różnych językach
  * Implementacja powinna maksymalnie wykorzystywać feature'y języka
* Daje się zastosować w wielu różnych problemach
  * musi być jednocześnie ogólny i precyzyjny
  * po to jest dekompozycja problemów
  * może na któryś z naszych podproblemów już ktoś wymyślił algorytm


## Schematy blokowe
* Bloki przedstawiają rodzaj działań
* Linie łączące bloki przedstawiają kolejność


## Dwa różne minusy
* binarny a - b
* unarny -a

Rozróżnienie syntaktyki i gramatyki języka programowania - jaka jest struktura i co znaczy

Każdy operator ma zdefiniowany priorytet i łączność

## Operatory unarne
* a++ postinkrementacja
* a-- postdekrementacja
* ++a preinkrementacja
* --a predekrementacja

Preinkrementacja najpierw zwiększa wartość zmiennej
```c
  int x = 10;
  int a = ++x;
  // a == 11 i x == 11
```

### Statement
nie zwraca wartości (while, for, if)

### Expression
zwraca wartość (a = b + c)
