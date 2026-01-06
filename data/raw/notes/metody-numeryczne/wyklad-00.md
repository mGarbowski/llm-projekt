# Organizacja
* Inny prowazdący od projektów
	* projekt zacznie się w 3 tygodniu
	* za tydzień będzie harmonogram przedmiotu
* Kontakt mailem
* W podręczniku w każdym rozdziale są zadania
	* do opanowania na kolokwia
* Materiały na studia3
* Projekt
	* 3 indywidualne zadania projektowe
	* co tydzień jest termin kiedy prowadzący jest dostępny
	* oceniane są sprawozdania
	* będą terminy z obowiązkową obecnością
* Podręcznik pokrywa się z wykładem
	* zakres wykładu jest węższy
* Sciąganie kodów realizujących algorytmy z internetu jest ok tlyko trzeba je testować

## Ocena
* 2 kolokwia po 30pkt
	* można mieć 1 kartkę własnych notatek (odręcznych) i kalkulator
	* będzie kolokwium poprawkowe
* 3 projekty za 40pkt łącznie
	* min 20pkt
	* każdy projekt jest obowiązkowy
* W sumie min 50pkt

## Maszynowa reprezentacja liczb

### Reprezentacja zmiennoprzecinkowa
* $x_{t,r}=m_t \cdot P^{c_r}$
* $m_t$ mantysa
	* $|m_t| < 1$
	* $t$ liczba bitów mantysy
* $c_r$ wykładnik (cecha)
	* $r$ liczba bitów wykładnika
* $P$ podstawa, ograniczamy się do $P=2$
* Naturalna reprezentacja znormalizowana $0.5 < m_t < 1$
* Kolejne potęgi dwójki rosną płynnie od końca mantysy do początku wykładnika
* Zbiór liczb maszynowych dla reprezentacji znormalizowanej musi być uzupełniony o 0

### IEEE 754
* $1 \le |m_t| < 2$
* Format 32-bitowy
	* 1 bit znaku
	* wykładnik 8-bitowy kodowany z przesunięciem 127
	* mantysa 24-bitowa (pierwszy bit zawsze równy 1, w reprezentacji 23 bity)
* Wzór ...
* Zakres ...
* Zbiór liczb maszynowych jest skończony
* Im dłuższa mantysa (większe $t$) tym bardziej gęsty jest zbiór liczb maszynowych
* Im dłuższa cecha (większe $r$) tym większy zakres liczb

### Najlepsze przybliżenie liczby $x$
$$
|rd(x) - x| \le \min_{g \in M} |g-x|
$$
Postulat jest spełniony przez typowe zaokrąglenie

Błąd zaokrąglenia mantysy, błąd bezwzględny (roundoff error)

$$
|m-m_t| \le 2^{-(t+1)}
$$

### Względny błąd reprezentacji

$$
\frac{rd(x)-x}{x}
= \frac{m_t \cdot 2^c - m\cdot 2^c}{m \cdot 2^c}
= \frac{m_t - m}{m}
$$

Oszaowanie błędu względnego zaokrąglenia

...

Uniwersalna zalezność, nie zależy od przyjętego wzorca normalizacji mantysy

Maksymalny błąd względny reprezentacji zmiennoprzecinkowej liczby zależy jedynie od liczby bitów mantysy - precyzja maszynowa (machine precision), oznaczany jako $eps = 2^{-t}$.

$$
|rd(x) - x| \le eps \cdot |x|
$$
$$
rd(x) - x = \epsilon \cdot x \quad |\epsilon| \le eps
$$
$$
rd(x) = x(1+\epsilon)
$$

### Aproksymacja liczby przez obcięcie
Błąd obcięcia (truncation error, chopping error)
Zamiast zaokrąglania, obcina się nadmiarowe bity mantysy
$m_t$ jest z niedomiarem $\le 2^{-t}$
teraz $eps=2^{-t+1}$

W przypadku stosowania słowa o podwójnej długości mantysy
$$
eps_{mdl} = (eps)^2
$$

mdl - mantissa double length

W standardzie IEEE 754, reprezentacja podwójnej precyzji

* 1 bit znaku
* 11 bitów wykładnika
* 52 bity mantysy (więcej niż dwukrotnie dłuższa)

## Arytmetyka zmiennopozycyjna
Wynikiem działań na liczbach maszynowych nie są na ogół liczby maszynowe

Wyniki działań elementarnych

$$
fl(x \pm y) = (x \pm y) \cdot (1+\epsilon)
$$

$$
fl(x \cdot y) = (x \cdot y) \cdot (1 + \epsilon)
$$

$$
fl(x/y)=(x/y) \cdot (1 + \epsilon)
$$

$$
fl(\sqrt{x}) = \sqrt{x} \cdot (1 + \epsilon)
$$

Standard IEEE 754 wymaga organizacji ALU zapewniającą osiągnięcie takiej dokadnoci

eps można też zdefiniować jako najmniejszą liczbę, która dodana do 1 zmienia wynik

$$
eps = \min \{ g \in M: \quad fl(1+g), g>0 \}
$$

Błędy ulegają propagacji, całkowity błąd względny wyniku z reguły jest znacznie większy od dokładności maszynowej

### Sposoby analizy błedu wyniku

* błąd średni (metoda probabilistyczna)
* maksymalny możliwy moduł błędu (metoda najgorszego przypadku)
* metody analityczne (w prostszych przypadkach)

### Przykład
Dla operacji $y = a + b$

$$y = [a(1+ \epsilon_a) _ b(1 + \epsilon_b)](1 + \epsilon_l)$$

Pomijamy $\epsilon \cdot \epsilon$ 

Oszacowanie błedu....

$$
\frac{|a| + |b|}{|a+b|} \cdot 2eps$$

Bład będzie inny dla liczb o jednakowym znaku i o różnych znakach
zjawisko redukcji cyfr znaczących

## Uwarunkowanie zadania
Matematyczne zadanie obliczeniowe $\phi: \mathbb{R}^n \rightarrow \mathbb{R}^m$
$w = \phi(d)$
wektor danych, wektor wyników

Zadanie obliczeniowe jest źle uwarunkowane jeśli niewielkie (względne) zabużenia danych zadania powodują duże (względne) zmiany jego rozwiązania

Wskaźnik uwarunkowania - wielkość charakteryzująca ilościowo zmiany wartości wyniku w stosunku do zmian wartości danych (iloraz)

### Przykład
$$w = \phi(a,b) = \sum_{i=1}^na_ib_i$$

...

Uwarunkowanie zadania zależy od konkretnych wartości danych, to nie jest ogólna własność np. danego algorytmu

