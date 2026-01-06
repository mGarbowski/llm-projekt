# Złożoność obliczeniowa

To że jedno rozwiązanie jest lepsze od drugiego może oznaczać, że jest
* Bardziej efektywne
  * szybsze
  * używa mniej zasobów (np. mniej RAMu)
* Bardziej skalowalne
  * może być zrównoleglone, przetwarzane naraz przez kilka jednostek
* Bardziej dokładne


## Cechy algorytmu
Algorytm jest skończonym ciągiem instrukcji. Każda z nich musi być zrozumiała i wykonalna dla realizującego. Musi rządzić się dobrze określonymi regułami.

Powinien być ogólny - nie dla jednego konkretnego zestawu danych tylko jak największego.

Liczba kroków algorytmu zależy od jego samego, ilości danych i wartości danych. Liczba potrzebnych kroków powinna być skończona i algorytm powinien się kiedyś zakończyć (własność stopu).
  

## Złożoność
Złożoność problemu / algorytmu to ilość zasobów konieczna do jego rozwiązania / wykonania.

Złożoność problemu to nie to samo co złożoność algorytmu. Na rozwiązanie jednego problemu może istnieć wiele algorytmów. Wtedy złożoność problemu to najmniejsza ze złożoności dostępnych algorytmów.

Więcej danych to nie zawsze więcej operacji - może nie trzeba przeglądać całego zbioru.

Więcej operacji to nie zawsze więcej czasu - może da się wykorzystać więcej zasobów i zrównnoleglić algorytm (np. na kilku rdzeniach na raz)


## Zapotrzebowanie na zasoby
* Czas
* Przestrzeń - pamięć operacyjna, przestrzeń dyskowa
* Liczba potrzebnych operacji arytmetycznych, przekształceń
* Dostęp do zewnętrznych urządzeń / systemów (sieć)


## Przeszukiwanie liniowe i binarne
Przeszukiwanie liniowe - sprawdzanie po kolei każdego elementu w ciągu, dopóki nie znajdzie się szukanego albo dojdzie do końca. Złożoność liniowa O(n) - wydłużenie ciągu 2 razy -> 2 razy więcej operacji.

Przeszukiwanie binarne - dla uporządkowanego ciągu, metoda bisekcji. Po sprawdzeniu jednego elementu wiadomo, że szukany będzie większy lub mniejszy i jedną połowę ciągu można odrzucić. Złożoność logarytmiczna O(log2(n)) - wydłużenie ciągu 2 razy -> 1 operacja więcej.


## Złożoność czasowa O()
Notacja dużego O nie podaje konkretnego czasu działania algorytmu, ale charakter wpływu rozmiaru danych na czas wykonywania.

Ważny jest tylko rząd wielkości - $O(3n^2 + 4n + 1) = O(n^2)$.
O(f(n)) mówi o rzędzie wielkości dla dużych wartości n - asymptotycznie dla n dążącego do nieskończoności.

Jest jakiś punkt przegięcia po którym algorytm O(log(n)) będzie lepszy od algorytmu O(n). Dla mniejszych danych, może bardziej opłacać się użycie O(n).

Dwa algorytmy o złożoności liniowej O(n) mogą różnić się czasem wykonywania (czynnik stały, wyraz wolny).

Przeszukiwanie liniowe O(n) z wykorzystaniem cache'y procesora, może być dużo szybsze niż wyszukiwanie binarne i sięganie do pamięci po drzewo binarne.

Może opłaca się posortować listę O(nlog(n)), żeby móc użyć szybszego wyszukiwania binarnego O(log(n)) jeśli będzie się wyszukiwać wielokrotnie.


## Analiza algorytmu
Czas działania zależy nie tylko od liczności danych ale też wartości i dostępności.

Rozpatruje się różne typy złożoności
* W najgorszym wypadku (worst-case)
* W najlepszym wypadku (best-case)
* Średnio (average-case)

Dla przeszukiwania liniowego
* worst-case -> O(n) - przeszukanie całej tablicy
* average-case -> O(n/2) = O(n) - w połowie tablicy
* best-case -> O(1) - na pierwszej sprawdzonej pozycji


## [Złożoności](https://www.bigocheatsheet.com/)
* stała (constant) - O(1)
* logarytmiczna - O(log(n))
* liniowa - O(n)
* wielomianowa (polynomial) - O(n^2), O(n^3), O(n^k)
* wykładnicza (exponential) - O(k^n), O(k^n^n), O(n!)


O(n) nie musi oznaczać sukcesu np. jeśli zbiór danych jest odpowiednio duży albo jeśli algorytm nie jest skalowalny.

![wykres złożoności](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fera86.github.io%2Fassets%2Fimages%2Fposts%2Fbig-o-chart.png&f=1&nofb=1&ipt=b8008c71ec5645f45ad07f49fa16e03c720d5ba61f937f3f131a7cdf824c7ee9&ipo=images)


## Luka algorytmiczna
Luka algorytmiczna - zakres złożoności ograniczony z dołu przez formalne dowody matematyczne, że nie może istnieć lepszy algorytm i ograniczony z góry przez najlepszy znany algorytm.

Jeśli luka nie istnieje to problem jest algorytmicznie zamknięty. Np. na przeszukiwanie nieuporządkowanej tablicy - udowodniono, że złożoność nie może być lepsza niż O(n) i jest znany algorytm O(n).


## Struktury danych
Struktury danych różnią się złożonością czasową i przestrzenną. Spsób używania danych powinien determinować w jakiej strukturze należy je przechowywać.

![Tabela złożoności dla struktur danych](https://he-s3.s3.amazonaws.com/media/uploads/c14cb1f.JPG)


## Problem komiwojażera
W rozwiązaniu problemu komiwojażera sprawdzenie jednej z możliwych ścieżek jest problemem wielomianowym O(n), ale jest wykładniczo O(n!) dużo kombinacji ścieżek (eksplozja wykładnicza).

Nie ma reguły co do wyboru ścieżki, można trafić na najlepszą w pierwszej permutacji albo równie dobrze w ostatniej - wybór jest niedeterministyczny.

## Problemy P i NP
Problemy P (Polynomial) - Łatwe do rozwiązania, rozwiązania łatwe do zweryfikowania w czasie wielomianowym.

Problemy NP (Nondeterministic Polynomial) - rozwiązanie łatwe do zweryfikowania w czasie wielomianowym. Np problemy decyzyjne wykładnicze: problem komiwojażera, porównywanie grafów, problem plecakowy, kolorowanie mapy.

Klasa problemów P jest podzbiorem NP $P \subseteq NP$

Nie wiadomo czy $P=NP$, dowód miałby poważne konsekwencje.


## Dokładność
Czasami wystarczy rozwiązanie akceptowalne, które można znaleźć w krótkim czasie a nie idealne.
