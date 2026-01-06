# Atrybuty

## Typy atrybutów
* Ciągłe
	* najwygodniejsze dla nas do pracy
* Dyskretne
	* porządkowe (S, M, L, XL)
	* nominalne (czerwony, zielony, niebieski)
	* trzeba je przekształcić żeby zastosować do typowych modeli (operują na atrybutach ciągłych)
* Sekwencje
	* uporządkowane (niekoniecznie w czasie)
	* np. kolejne słowa
* Szeregi czasowe
	* uporządkowane czasowo
	* np. dźwięk
* Obrazy
	* tensor $n \times m \times c$ 
* Znaczniki czasowe

## Czemu to jest istotne
* Wartości atrybutów są kodowane za pomocą liczb
	* dla atrybutów ciągłych nie ma problemu
* Sortowanie lub uśrednianie atrybutów nominalnych jest błędne
	* algorytm może to zrobić jak np. ponumerujemy kolory
	* to nie ma logicznego sensu
* Liczenie korelacji liniowej atrybutów dyskretnych nie ma sensu!
	* tylko dla ciągłych
* Normalizacja znaczników czasowych

## Rozkład atrybutów
* Pierwsza rzecz którą się robi przy projekcie
* Rozkład prawdopodobieństwa zmiennej losowej
* Inaczej podchodzimy do ciągłych i dyskretnych
* Frameworki liczą dystrybuanty i funkcje gęstości
* Ważne jest żeby mniej więcej rozumieć jak rozkład wygląda
	* móc porównać z nowa paczką danych, czy ona istotnie zmienia rozkłady
* Funkcję gęstości prawdopodobieństwa aproksymujemy za pomocą histogramów

## Pojęcia
* Funkcja gęstości zmiennej losowej
	* $P(x \in B) = \int_B f(x)dx$
* Dystrybuanta
	* $F(x) = P(X \le x)$
* Funkcja masy prawdopodobieństwa
	* określa p-stwo że zmienna losowa przyjmie wartość x
	* odpowiednik funkcji gęstości dla rozkładów dyskretnych

## Podstawowe rodziny rozkładów
* Jednostajny
	* zdarzenia mają takie same prawdopodobieństwo wystąpienia
* Normalny
	* spotykany w wielu miejscach w przyrodzie
	* ogony szybko zbiegają do zera
* Log-normalny
	* zmienna losowa, której logarytm ma rozkład normalny
	* np. ilość opadów deszczu
* t-Studenta
	* gdy szacujemy wartość oczekiwaną rozkładu normalnego za pomocą średniej z n-elementowej próby losowej
	* średnia jest opisywana rozkładem t-Studenta
	* parametr $\nu = n-1$
* Chi kwadrat
	* suma kwadratów $k$ niezależnych zmiennych losowych z rozkładu normalnego standardowego
	* wykorzystywany w testach statystycznych
* Weibull
	* zadania związane z analizą przeżycia
* Bernouliego
	* prawdopodobieństwo sukcesu eksperymentu binarnego
* Beta
	* do opisu rozkładu parametru p w rozkładzie Bernouliego
	* parametry $\alpha$, $\beta$
* Geometryczny
	* oczekiwana liczba prób do uzyskania pierwszego sukcesu, gdy każdą próbę opisuje rozkład Bernouliego
* Dwumianowy
	* liczba sukcesów w serii $n$ niezależnych eksperymentów
* Poissona
	* p-stwo wystąpienia n zdarzeń w danym okresie, gdy szansa pojedynczego zdarzenia jest znana
* Wykładniczy
	* czas między zdarzeniami opisywanymi rozkładem Poissona
* Zipfa
	* związany z prawem zipfa
	* jeśli dane da się uszeregować, to p-stwo wystąpienia uszeregowania jest proporcjonalne do odwrotności pozycji w rankingu
	* słowa w języku naturalnym
	* NLP
* W praktyce wszystko traktuje się jak rozkład normalny
	* w określonych dziedzinach wiemy jakiego rozkładu się spodziewamy

## Dane niezbalansowane
* W jednej klasie jest mało przykładów w stosunku do innej klasy
* Bez uwzględnienia problemu model może być obciążony w stronę klasy większościowej

### Przykład
* Detekcja rzadkiej choroby na podstawie objawów
* Reprezentatywny zbiór danych
	* 990 pomiarów od zdrowych
	* 10 pomiarów od chorych
* Naiwny klasyfikator da 99%

### Możliwe strategie
* Modyfikacja zbioru danych
	* undersampling - próbkujemy klasę większościową żeby zmniejszyć jej liczność
	* oversampling - próbkowanie ze zwracaniem klasy mniejszościowej
	* nie jest konieczne uzyskanie idealnego zbalansowania (1:1), zazwyczaj 1:10 to już ok
* Modyfikacja zadania
	* łączenie klas mniejszościowych
* Modyfikacja procesu uczenia
	* ważenie przykładów
	* algorytmy, które biorą pod uwagę niezbalansowanie
* Stosując dowolną ze strategii - trzeba pamiętać o poprawnej interpretacji uzyskiwanych rezultatów
	* metryki ze zmodyfikowanego zbioru treningowego mogą się nie przenosić na zbiór testowy

## Braki w danych
* Bardzo częsty problem
* Przyczyny
	* błędy podczas wprowadzania danych
	* awarie podczas wykonywania pomiarów
	* błędy techniczne
	* sytuacje brzegowe, w których pomiar może być niemożliwy

## Taksonomia brakujących danych
* Całkowicie losowe braki danych - MCAR
* Losowe braki danych - MAR
* Braki nielosowe - MNAR

### MCAR
* Jakby o fakcie wystąpienia braku wartości decydował rzut ważoną monetą
* Bardzo rzadka sytuacja
* Możemy takie dane pominąć
* Wyciągane na podstawie tych danych wnioski nie są zaburzone
* Przykład
	* ankieta online ma pole recenzja z 10% brakujących wartości
	* brak wynika z niedeterministycznych problemów sieciowych serwera - MCAR
	* części użytkowników w przeglądarce nie działał edytor - nie jest MCAR, zależy od ukrytej zmiennej

### MAR
* Niezależny od wszystkich zmiennych ukrytych
* Mogą zależeć od innych atrybutów, które zbieramy
* Nie można ich pominąć bo zaburzymy wyniki modelowania
* Populacja elementów ze zbioru danych mająca te same wartości atrybutów zmierzonych, będzie miała ten sam rozkład braków atrybutu $x_i$
* Przykład
	* braki w wypełnieniu recenzji (poprzedni przykład) jeśli rodzaj przeglądarki jest jednym z atrybutów

### MNAR
* Rozkład jest zależny od zmiennych ukrytych
* Nie jesteśmy w stanie wyeliminować warunkując na atrybutach obserwowanych
* Elementy ze zbioru danych mają te same wartości atrybutów zmierzonych, będą miały różne rozkłady braków atrybutu $x_i$
* Trudna do wykrycia sytuacja
* Przykład
	* problem z przykładu wcześniej zależy i od przeglądarki i od wersji systemu operacyjnego

### W praktyce
* Jeśli braków jest mało to nie zaburzy modelowania
* Dodajemy atrybut znacznikowy
	* analizujemy zależności z innymi atrybutami
	* nie wykryjemy zależności - zakładamy że jest MCAR i możemy usunąć
	* jeśli wykryjemy - MAR
* MNAR będzie trudny do wykrycia
	* można usunąć cały atrybut jeśli obawiamy się wpływu

## Praca z niekompletnymi danymi
* Usuwanie wierszy lub całych atrybutów
* Metody imputacji danych
* Modelowanie z wykorzystaniem zmiennych wskaźnikowych sygnalizujących braki
* Użycie algorytmów uczenia, które nie wymagają kompletnych danych (np. drzew)

## Błędy w danych
* Zawsze trzeba się liczyć z błędami
* Niedokładności pomiarów
	* naturalne zjawisko związane z pomiarami
	* zmniejsza informatywność atrybutu
* Niepoprawne wartości dyskretne
	* np. literówki
	* błąd w procesie zbierania danych lub niekompletność naszej wiedzy
	* należy ustalić przyczynę
* Niespójne wartości zmiennej celu
	* duży red flag
	* przykłady o identycznych wartościach atrybutu i innej zmiennej celu
	* potencjalnie do rozwiązania po stronie klienta
	* może brakować nam atrybutu, który pozwoliłby na rozróżnienie tych przypadków
	* mogą być błędy etykietowania
	* warto przedyskutować z klientem jakich rozkładów się spodziewa na podstawie wiedzy dziedzinowej

## Elementy odstające
* Elementy, które znacznie się różnią od reszty obserwacji
* Niejasna granica
* Przyczyny
	* naturalne, rzadko pojawiające się w danych obserwacje (wiek 103)
	* błędy (wiek -12)
	* sygnał, że mamy nieodpowiednie założenia odnośnie rozkładu danych (np. modelujemy złym rozkładem)

### Wykrywanie elementów odstających
* Interquartile range
	* minimum Q1 - 1.5IQR
	* maximum Q3 + 1.5IQR
	* wszystko poza jest uznawane za outlier
	* często stosowana heurystyka
* Q-Q plot
	* narzędzie do prównywania 2 rozkładów danych
	* w dwóch paczkach porównujemy atrybuty
	* paczkę danych porównujemy z założonym rozkładem
	* graficzne narzędzie
	* można sprawdzić czy nowa paczka danych od klienta ma taki rozkład jak to co już mamy
	* dla wszystkich rozkładów
* Reguła 3 std dla rozkładu normalnego
	* oddalenie od więcej niż 3 std od średniej to outlier
* Uznanie obserwacji za odstającą jest często arbitralną decyzją analityka

### Konsekwencje usuwania elementów odstających
* Ignorujemy sygnały, że modelujemy złym rozkładem
* Narażamy się na tzw. czarne łabędzie
	* przykład o bardzo dużych konsekwencjach dla systemu

## Rozkłady z grubymi ogonami
* Rozkład normalny jest wygodny, często występuje w przyrodzie
	* wygodne własności analityczne
* Te właściwości nie dotyczą rozkładów z grubymi ogonami
* Jeśli mamy do czynienia z rozkładami o grubych ogonach, a koszt pomyłki w przypadku wystąpienia czarnego łabędzia będzie nieograniczony - zrezygnujmy z modelowania

### Rozkład Cauchy'ego
* Nie jest zdefiniowana wartość oczekiwana
* Całkiem prawdopodobne są zdarzenie dużo bardziej oddalone od środka

## Normalizacja
* Problemy ze zróżnicowanymi zakresami wartości
	* duże wartości mogą zdominować proces uczenia
	* utrudniona interpretacja wyników - jakie wagi będą duże a jakie małe
	* błędy numeryczne prowadzące do niestabilnego uczenia

### Metody
* Skalowanie do ustalonego przedziału
	* problemy jeśli nie znamy z góry zakresów możliwych wartości
* Standaryzaja / standardyzacja
	* jeśli zmienna losowa miała rozkład normalny to po tym będzie miała normalny standardowy
	* nie gwarantuje że wartości zachowają jakiś przedział (rozkład normalny jest teoretycznie nieograniczony)
	* odjęcie średniej i podzielenie przez odchylenie standardowe
* Przekształcenie logarytmiczne
	* jeśli wartości różnią się znacznie rzędem wielkości
* Przeskalowanie wektora tak, żeby miał długość 1
	* atrybut nie zawsze będzie 1-wymiarowym skalarem
	* podzielenie przez normę wektora
* Przekształcenie wartości bezwzględnych na względne (zmiana jednostek)
* Czy na produkcji mogą się pojawić wartości z szerszego zakresu niż w zbiorze treningowym
	* problem ze stałym przedziałem
	* przy standaryzacji nie ma problemu

## Interakcje
* Przykład
	* przewidywanie czynszu
	* w jednym mieście kamienice są droższe niż bloki a w drugim na odwrót
	* model liniowy nie poradzi sobie z niektórymi zależnościami
* Sklejenie kilku atrybutów dyskretnych w 1
	* każda kombinacja 2 atrybutów
	* model liniowy sobie poradzi
	* może przyporządkować inną wagę każdej wartości atrybutu sklejonego
	* nie musi uwzględniać kombinacji które nie występują
* Można zachować prosty, łatwy w interpretacji model i zachować dobre wyniki
	* przez modyfikację atrybutów
* Notacja na slajdzie - mnożenie wektora wag przez atrybut
	* atrybut dyskretny trzeba odpowiednio zakodować

## Kodowanie atrybutów dyskretnych
* Przypisanie kolejnych liczb całkowitych
	* może ok jeśli atrybut jest porządkowy (rozmiar koszulki S,M,L,XL)
	* czy M jest 2 razy większe niż S?
	* nie jest ok jeśli atrybut nie jest porządkowy, wprowadza nieistniejącą hierarchię (np. kolor czerwony, zielony, niebieski)
* Kodowanie częstotliwościowe / częstościowe
	* im częściej występuje wartość atrybutu, tym większą wartość dostaje
	* ok kiedy to częstość ma dla nas znaczenie, a nie sama wartość
	* problem jeśli dwie wartości mają jednakową częstość
* Kodowanie wskaźnikowe / one-hot encoding
	* kodowanie wartości dyskretnej jako wektor (a nie skalar)
	* dużo zer i jedna jedynka
	* wektor wag ma wtedy ten sam wymiar
	* standard dla atrybutów dyskretnych
	* rzadka reprezentacja
	* nadmiarowa reprezentacja, mało kompaktowa - w praktyce to nie ma kluczowego znaczenia
* Zanurzenia

## Zanurzenia
* Reprezentacja wektorowa obiektu z jakiejś przestrzeni
* Jest dobra jeśli zachowuje określone właściwości, relacje ze świata rzeczywistego
	* jak wektor reprezentuje obrazki zwierząt
	* dobre zanurzenie - wektory dla 2 psów powinny być mniej oddalone od siebie niż wektory dla psa i kota
	* przeniesienie semantyki i relacji
* Tworzenie zanurzeń
	* przez transfer uczenia - fragment gotowego modelu, powszechne w wizji komputerowej i przetwarzaniu tekstu
	* tworzenie modeli realizujących funkcje zanurzające

### Autokoder (autoenkoder)
* Model który przewiduje swoje wejście
	* zadanie jest trywialne $y=x$
	* ograniczamy postać funkcji
* Przekształcenie zawężające
	* np. wejście ma 1000 wymiarów, jakaś pośrednia warstwa 250, a wyjście znowu 1000
	* wymuszamy wąskie gardło
* Jeśli model dobrze przewiduje swoje wejście to ta wąska warstwa nauczyła się kompresować tą informację
	* wąska reprezentacja musi zawierać potrzebne informacje
* Struktura
	* enkoder - rzutuje do zawężonej reprezentacji
	* dekoder - odtwarza z zawężonej reprezentacji do pełnej wymiarowości
* Po wytrenowaniu potrzebny jest tylko enkoder
	* możemy go użyć do generowania zanurzeń
* Ograniczenia
	* nie mamy kontroli nad formą tych zanurzeń, nie możemy wymusić właściwości

### Metric learning
* Pozwala wymusić, żeby zanurzenia dla grup obiektów były blisko siebie, a innych daleko od siebie
* Odległość w przestrzeni zanurzonej
	* minimalizowana gdy oba elementy są do siebie podobne w oryginalnej przestrzeni
	* maksymalizacja w przeciwnym przypadku
* Zastosowania - wyszukiwarki wielomodalne
	* zdjęcia na podstawie tekstu
	* obiekty z różnych przestrzeni rzutujemy do tej samej przestrzeni zanurzeń (i tekst i obrazki do $\mathbb{R}^n$)
	* można dowolnie dużo modalności zrzutować do takiej przestrzeni
	* mogą być oddzielne modele dla różnych modalności ale ich wyjście w tej samej przestrzeni (trenowane jednocześnie)
* Dane wejściowe do generowania zanurzeń
	* dla wyszukiwarki wielomodalnej
	* tekst, zdjęcie, czy para jest pozytywna czy negatywna
	* pozytywna: tekst: "pies", zdjęcie: zdjęcie psa
	* negatywna: tekst: "kot", zdjęcie: zdjęcie psa

Zanurzenia to bardzo silna technika, za pomocą metric learning można mieć kontrolę,
standard jeśli chodzi o pracę z tekstem i obrazami


## Selekcja atrybutów
Jak wybrać najbardziej informatywny zestaw atrybutów do modelowania

### Współczynnik korelacji
* Korelacja liniowa / Pearsona
	* znormalizowana kowariancja
	* **tylko dla atrybutów ciągłych**
* Korelacja rangowa / Spearmana
* Wykrywają tylko zależności liniowe
* Zerowa korelacja nie mówi, że atrybuty są niezależne

### Współczynnik informacji wzajemnej
* Zdefiniowane dla pary zmiennych, na prawdopodobieństwtach
	* dla zmiennych dyskretnych
	* dla zmiennych ciągłych po kubełkowaniu
* Nie pokazuje kierunku zależności, tylko siłę
* Nie jest znormalizowany
* Działa dla przypadków nieliniowych (niektórych)

Liczymy korelację / współczynnik informacji wzajemnej atrybutu z etykietą, chcemy tych atrybutów o jak największej zależności

### Regularyzacja L1
* Składnik dodawany do funkcji celu
* Kara za zbyt duże wagi
* Wagi do bezużytecznych atrybutów będą zerowane
* Jeśli procesowi uczenia opłaca się wyzerować wagę to znaczy że atrybut nie jest potrzebny

### Selekcja w przód / wstecz
* W przód (forward selection)
	* na początku modele z pojedynczymi atrybutami
	* dodajemy te które są dobre
* Wstecz (backward selection)
	* na początku wszystkie atrybuty
	* usuwamy po 1 i patrzymy na którym nic nie traci
* Forward-backward
		dodajemy dwa, usuwamy jeden

### Selekcja za pomocą testu $\chi^2$
* Test niezależności dwóch zmiennych losowych, których wspólne występowanie da się opisać w formie tabelarycznej
* U nas - pogwałcenie zasad statystyki, przyjmujemy że im więcej tym silniejszy wpływ
* Wyliczamy wartości dla wszystkich atrybutów, sortujemy od najwyższej do najniższej
* Można policzyć też $\chi^2$ dla szumu
	* wiemy że nie niesie informacji
	* każdy atrybut co ma mniejszą wartość nie niesie informacji
* Liczba wartości szumu powinna być podobna do liczby unikalnych wartości prawdziwych atrybutów

### Selekcja za pomocą lasu losowego
* Można wyciągnąć ranking atrybutów z wytrenowanego modelu
* Na podstawie oceny podziałów
	* każdy węzeł drzewa dzieli dane korzystając z jednego atrybutu
	* im lepszy atrybut tym lepszy podział
	* atrybut oceniamy na podstawie sumarycznej oceny podziałów w których brał udział
	* wyliczany na zbiorze trenującym
	* przeszacowuje wagę cech o wielu wartościach
* Na podstawie spadku jakości modelu po permutacji atrybutu
	* oceniamy jakość modelu na zewnętrznym zbiorze danych
	* losowo przetasowujemy wartości atrybutu $x_i$
	* jeszcze raz oceniamy model
	* spadek jakości - ocena atrybutu $x_i$
	* najlepiej liczyć na osobnym podzbiorze do selekcji atrybutów
