# Ocena jakości

## Macierz pomyłek
* Confusion matrix
* Dla klasyfikacji
* W wierszach prawdziwe klasy $c$, w kolumnach przewidywane klasy $h$
* W komórce liczba przypadków na zbiorze $S$
	* $|S_{c=d_1,h=d_2}|$
* Na przekątnej poprawne predykcje
* Macierz pomyłek 2x2 - dla klasyfikacji binarnej
	* wiele miar jakości definiuje się dla tej postaci
	* uzasadnia się ich uogólnienia dla *dużej* macierzy pomyłek
* Praktyka
	* $1$ określa coś czego wykrywanie jest naszym priorytetem
	* nazwanie klasy (pozytywna/negatywna) jest umowne
	* np. jeśli wykrywamy awarie to awarię oznaczymy jako klasę pozytywną
	* czasem powtarza się wyliczanie wskaźników odwracając klasy (wzory są asymetryczne)

| c\h | 0   | 1   |
| --- | --- | --- |
| 0   | TN  | FP  |
| 1   | FN  | TP  |

## Miary jakości

### Błąd

$$ \frac{FP + FN}{TP + TN + FP + FN}$$

### Dokładność

$$ \frac{TP + TN}{TP + TN + FP + FN} $$

### Recall
* Inne nazwy
	* odzysk
	* true positive rate
	* sensitivity
	* czułość, wrażliwość
* Jaką część przypadków klasy $1$ model wykrył jako należące do tej klasy
* Chcemy maksymalizować
* Maksymalizowany przez model, który zawsze daje klasę $1$
	* nie można używać tylko tego wskaźnika

$$ TPrate = \frac{TP}{FN + TP} $$

### FP rate
* Jaką część przykładów klasy $0$ stanowią zaklasyfikowane jako $1$
* Chcemy minimalizować
	* szukamy poziomu równowagi między TP rate i FP rate

$$ FPrate = \frac{FP}{TN + FP} $$
### Precision
* Precyzja
* Jaką część stanowią prawdziwie pozytywne predykcje spośród wszystkich pozytywnych predykcji modelu
* Chcemy maksymalizować
	* komplementarne do odzysku
	* maksymalizacja obu naraz wymaga równowagi

$$ Precision = \frac{TP}{FP + TP} $$

### F-measure (F1)
* Średnia harmoniczna precyzji i odzysku
	* średnia harmoniczna jest bliższa mniejszej z wartości
* Można wprowadzić parametr określający względną ważność precyzji i odzysku
	* tutaj jednakowo ważne - współczynnik równy $1$
	* rzadko stosowane

$$
F1 
= \frac{1}{(\frac{1}{prec} + \frac{1}{recall})/2} 
= \frac{2 \cdot prec \cdot recall}{prec + recall}
$$

### Specificity
* Specyficzność

$$ 1 - FPrate $$

### Pary
* Stosowane pary wskaźników
	* TP rate, FP rate
	* Recall, Precision
	* Sensitivity, Specificity

## Analiza ROC
* Receiver operating characteristic
* Metodologia przeszczepiona z oceny jakości radarów
* Dwa wskaźniki
	* maskymalizowany (TP rate) na osi pionowej
	* minimalizowany (FP rate) na osi poziomej
* Użyteczne jeśli porównujemy wiele modeli lub jeden model, który może dawać różne odpowiedzi
	* modele oparte na prawdopodobieństwie
	* możemy przewidywać klasę na podstawie progu i prawdopodobieństwa ($P(1|x) \ge \delta$)
	* może być model, który nie daje prawdopodobieństw ale bazuje na funkcji decyzyjnej
	* coś liczbowego co określa przewidywaną klasę
	* wszystkie powszechnie używane modele mają taką właściwość
* Krzywa ROC
	* połączenie wielu punktów pracy przy różnych wartościach progu decyzyjnego
	* początek w $(0,0)$, koniec w $(1,1)$
	* punkt domyślny (dla progu prawdopodobieństwa $1/2$, dla funkcji decyzyjnej $0$)
	* na podstawie krzywej możemy wybrać lepszy punkt niż domyślny (dobrać próg)
	* zależy od zastosowanie jak będziemy wybierać najlepszy punkt roboczy
	* heurystyka - punkt najbliżej narożnika $(0,1)$
* Można na podstawie krzywej ocenić, nie konkretny punkt, a cały model
	* pole pod krzywą ROC
	* AUC - area under curve
	* interpretowane jako prawdopodobieństwo, że losowo wybrany przykład klasy 1 dostanie większą wartość prawdopodobieństwa przewidywania klasy 1
	* im więcej tym lepiej
	* wartość $1/2$ oznacza model, który nie rozróżnia klas
* Punktów na krzywej jest tyle, ile progów prawdopodobieństwa / funkci decyzyjnej można postawić + 2 skrajne
* Można porównywać krzywe dla różnych modeli
	* jeśli jedna krzywa jest w całości nad drugą, to ten model jest lepszy
* Też dla pary precision/recall 
 
### Rysowanie krzywej ROC
* Być może na kolokwium
* Tabela z prawdopodobieństwem klasy 1 i prawdziwą klasą
* Posortowana niemalejąco po prawdopodobieństwach
* Skalujemy osie na podstawie liczby przypadków
* Zaczynamy z takim progiem, że wszystkie wartości P są powyżej
	* same przewidywane jedynki
	* zaczynamy od punktu $(1,1)$
* Przesuwamy próg przed kolejną unikalną wartość
* Krzywa będzie się składać z widocznych odcinków jeśli będzie mało różnych wartości prawdopodobieństwa
	* np. jeśli zbiór danych jest mały
	* ale może model przewiduje mało różnych wartości
* Krzywa poniżej przekątnej - najprawdopodobniej złe przypisanie etykiet
	* inne do budowy modelu i inne do oceny
	* można spreparować taki złośliwy, sztuczny zbiór danych (ale wtedy zbiór uczący i testowy nie pochodzą z tego samego rozkładu)

## Miary jakości klasyfikacji wieloklasowej
* Analogiczne podejścia do OvR i OvO
	* OvO nie omawiamy szczegółowo
* OvR
	* jedna klasa traktowana jako pozytywna, reszta jako negatywne
	* tylko podczas oceny jakości
* Mikro-uśrednianie
	* predykcje i prawdziwe wartości dla każdego zadania binarnego scalane
	* na ich podstawie wyznaczane wskaźniki jakości
	* każda klasa jest ważna proporcjonalnie do jej częstości
* Makro-uśrednianie
	* wskaźniki jakości wyznaczane niezależnie dla każdego zadania binarnego
	* uśrednianie
	* każda klasa jest jednakowo ważna
* Do krzywej ROC
	* w lewej kolumnie prawdopodobieństwo klasy $d_1$
	* w prawej kolumnie $1$ dla klasy $d_1$, $0$ w przeciwnym przypadku
	* to samo dla kolejnych klas i potem scalamy (długie wektory)
	* tyle wierszy ile przykładów trenujących x liczba klas
	* OvR w wariancie mikrouśredniania
* Nie ma dobrej odpowiedzi którego należy użyć
* Różnica
	* w wariancie mikro klasy rzadko występujące wpływają w mniejszym stopniu na uśrendioną ocenę
	* w wariancie makro wszystkie klasy mają jednakowy wpływ niezależnie od częstości występowania w zbiorze
* Sprawdzać co domyślnie robią używane biblioteki jeśli z nich korzystamy

## Jakość regresji

### Błąd średniokwadratowy (MSE)

$$ MSE = \frac{1}{|S|} \sum_{x \in A}(f(x)-h(x))^2 $$

### Mean Absolute Error
* Gorsze własności analityczne

$$ MAE = \frac{1}{|S|} \sum_{x \in S}|f(x)-h(x)| $$
### RMSE
* Root Mean Squared Error
* Pierwotny zakres wartości
* Ułatwia interpretację

$$ RMSE = \sqrt{MSE} $$

### Relateive Absolute Error
* Blisko 1 to bardzo źle
* Ułatwia interpretację (mało czy dużo)
* $m_S(f)$ - średnia wartość $f$ na zbiorze $S$

$$ \frac{\sum_{x \in S} |f(x)-h(x)|}{\sum_{x \in S} |f(x) -m_S(f)|} $$

### Współczynnik determinacji
* Dobry model - wartości bliskie 1
* W ogólności może dać wartości ujemne

$$ R^2 = 1 -\frac{\sum_{x \in S}(f(x)-h(x))^2}{\sum_{x \in S}(f(x)-m_S(f)^2} $$
### Korelacja
* Współczynnik korelacji liniowej lub rangowej między wartościami $f$ i $h$

## Procedury oceny
* Jak postępujemy z danymi licząc miary jakości tak, żeby miary były wiarygodne
* Celem oceny jest dostarczenie estymacji prawdziwych wartości wskaźników jakości modelu na nowych danych, do których będzie stosowany w trakcie eksploatacji
* Ocena procedury modelowania
	* oceniany nie konkretny model, a sposób jego tworzenia
* Ocenia się model zbudowany na części danych
	* model produkcyjny należy trenować na całym zbiorze danych
* Obciążenie kontra wariancja
	* zbyt mały zbiór do oceny nie zapewnia wiarygodnej estymacji ze względy na wysoką wariancję (ocena bardziej podatna na losowość wyboru podzbiorów)
	* odłożenie dużej części danych do oceny wprowadza pesymistyczne obciążenie związane z obniżeniem jakości ocenianego modelu

### Osobny zbiór trenujący $T$ i testowy $Q$
* Holdout, train-test split
* Model tworzymy w oparciu o $T$
* Oceniamy na zbiorze $Q$
* Odkładamy dane na potrzeby oceny jakości
* Jest wystarczająco dobry jeśli w sumie mamy nadmiar danych
	* więcej danych niż możemy przetworzyć w sensownym czasie przy budowaniu modelu
	* produkcyjny model to ten sam co oceniany
* Możliwa redukcja wariancji przez wielokrotne powtarzanie

### k-krotna walidacja krzyżowa
* k-fold cross-validation, k-CV
* Cały zbiór danych $D$ dzielimy na losowe podzbiory $D_1, \ldots D_k$
	* rozłączne i równoliczne
* Iteracyjnie przechodzi się przez wszystki podzbiory
	* jak ozbiór trenujący bierzemy sumę wszystkich podzbiorów poza $D_i$
	* jako zbiór testowy bierzemy $D_i$
* Każdy podzbiór będzie użyty raz jako testowy i $k-1$ razy jako trenujący
* Niewielka wariancja oceny
* Typowe wartości $k = 5, 10
* Można powtórzyć kilka razy
	* n$\times$k-CV
* Makro-uśrednianie
	* obliczenie średniej i odchylenia z ocen ze wszystkich iteracji
	* najczęściej stosowane
* Mikro-uśrednianie
	* w każdym obiegu nie generujemy oceny tylko predykcje
	* scalenie predykcji i wyliczenie oceny
	* rzadziej stosowane
