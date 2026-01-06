# Teoria uczenia się

## PAC-nauczalność

* Probably Approximately Correct
* Jest właściwością klasy pojęć
* To nie jest tak słaba gwarancja jak brzmi
	* prawdopodobieństwo może być blisko $1$, a błąd blisko $0$
* Klasa pojęć $\mathbb{C}$ dla dziedziny $X$ jest PAC-nauczalna za pomocą przestrzeni modeli $\mathbb{H}$ jeśli
	* istnieje algorytm uczenia się używający $\mathbb{H}$
	* którego uruchomienie z dostępem do źródła przykładów $EX(\Omega,c)$ oraz z parametrami $\epsilon$ i $\delta$
	* daje w wyniku z prawdopodobieństwem co najmniej $1-\delta$ model $h \in \mathbb{H}$, dla którego $e_{\Omega,c}(h) \le \epsilon$
	* dla dowolnego pojęcia $c \in \mathbb{C}$, dowolnego rozkładu prawdopodobieństwa $\Omega$ na $X$ oraz dowolnych $0 < \epsilon < 1$ i $0 < \delta < 1$
* Źródło przykładów, a nie zbiór - nie zakładamy ograniczenia na jakąś liczbę przykładów
* Parametry $\epsilon$ i $\delta$ określają nasze wymagania do algorytmu
	* im bliższe $0$ tym lepszy model

### Przykład
* Algorytm uczy się prostokątu o bokach równoległych do osi układu współrzędnych
* Klasa pojęć = przestrzeń modeli = zbiór prostokątów o bokach równoległych do osi
* Algorytm - prostokąt najciaśniej dopasowany do punktów klasy $1$
* Chcemy zagwarantować, że $e_{\Omega,c}(h) < \epsilon$
* Sytuacja szczególna
	* klasa jest bardzo rzadka 
	* prawdopodobieństw wylosowania punktu o klasie 1 $<\epsilon$ - trywialny przypadek
* Prawdopodobieństwo wylosowania punktu klasy $1$ większe niż epsilon
* Odcinamy kawałek prostokąta $c$, który ma prawdopodobieństwo $\epsilon / 4$
* Odcinamy $4$ takie paski po bokach (nakładają się na rogach)
* Łącznie mają prawdopodobieństwo $\le \epsilon$
* Jeśli model jest prostokątem zachodzącym na odcięte paski to ma błąd mniejszy niż $\epsilon$
* To nie jest jedyna sytuacja, gdzie model ma błąd mniejszy niż $\epsilon$
	* chodzi o wskazanie jakiegoś przypadku, który może występować z wystarczająco dużym prawdopodobieństwem
* Żeby powstał taki model, który zachodzi na każdy pasek, to w każdym musi być co najmniej jeden punkt
	* warunek wystarczający małego błędu
* Obliczamy prawdopodobieństwo że tak nie będzie
* Dla jednego punktu, jest prawdopodobieństwo $1-\epsilon/4$ że nie leży w danym pasku
* Dla $m$ przykładów jest prawdopodobieństwo $(1-\epsilon/4)^m$ że żaden z nich nie należy do danego paska
* Prawdopodobieństwo że w conajmniej jednym pasku nie żadnego punkut $< 4(1-\epsilon/4)^m$
* Wystarczy mieć odpowiednio duże $m$
	* odpowiednio dużo danych
* PAC-nauczalność - możemy mieć taką pewność i błąd jak chcemy jeśli mamy wystarczająco dużo danych
* Dodatkowo korzysta się z $1+\alpha \le e^\alpha$
	* $4(1-\epsilon/4)^m \le 4e^{-m \epsilon / 4} \le \delta$
	* $m \ge 4 / \epsilon(\ln 4 + \ln 1/\delta)$
* W sytuacji rzeczywistej mamy ustalone $m$, możemy wyznaczyć jaki błąd prawie na pewno da się zagwarantować

## Spójne uczenie się
* Consistent learning
* Spójny model - zerowy błąd na zbiorze trenującym
* Spójny algorytm uczenia się - zwraca spójny model albo zawodzi
	* jeśli takiego modelu nie ma w $\mathbb{H}$
* Niezawodność spójnego uczenia się
	* można zagwarantować tylko jeśli $\mathbb{C} \subseteq \mathbb{H}$
* Przestrzeń wersji - zbiór wszystkich spójnych modeli
	* $VS_{\mathbb{H},T}(c) = \{h \in \mathbb{H} | e_{T,c}(h)=0 \}$

### Przykład
* $X = \{0,1\}^n$
* $\mathbb{H}$ = koniunkcje boolowskie
* Zaczynamy od koniunkcji ze wszystkimi literałami (daje stałe 0 logiczne)
* $a_1 \wedge \neg a_1 \wedge \ldots$
* Mamy zbiór danych i dla każdego przykładu o klasie 1 usuwamy te literały, które przeszkadzają
* Model zadziała jeśli faktyczne pojęcie też jest koniunkcją boolowską ($\mathbb{C} \subseteq \mathbb{H}$)
* Na pewno da model, który da zerowy błąd na zbiorze trenującym

### Błąd rzeczywisty spójnych modeli
* Algorytm spójne może zwrócić dowolny model spójny
	* potrzebujemy ograniczenia błędu rzeczywistego
* Przestrzeń wersji jest $\epsilon$-wyczerpana jeśli błąd rzeczywisty wszystkich należących do niej modeli nie przekracza $\epsilon$
* Prawdopodobieństwo, że pewien model o błędzie rzeczywistym powyżej $\epsilon$ należy do przestrzeni wersji nie przekracza $(1-\epsilon)^m \le e^{-m\epsilon}$
	* $m$ - liczba przykładów trenujących
* Dla skończonej przestrzeni modeli, prawdopodobieństwo, że którykolwiek model z tej przestrzeni o błędzie rzeczywistym powyżej $\epsilon$ należy do przestrzeni wersji nie przekracza $|\mathbb{H}|e^{-m\epsilon}$
	* $P(e_{\Omega,c}(h) > \epsilon) \le |\mathbb{H}|e^{-m\epsilon}$
	* ograniczamy przez $\delta$ - $|\mathbb{H}|e^{-m\epsilon} \le \delta$
	* $m \ge 1/ \epsilon(\ln |\mathbb{H}| + \ln 1/ \delta)$
	* $\epsilon \ge 1/m(\ln |\mathbb{H}| + \ln 1/ \delta)$
* Więc z prawdopodobieństwem $1 - \delta$
	* $e_{\Omega,c}(c) \le 1/m(\ln |\mathbb{H}| + \ln 1/ \delta)$
* Algorytmy spójne używające skończonej przestrzeni modeli mogą osiągnąć dowolnie mały błąd, mimo podatności na nadmierne dopasowanie
	* wystarczy wystarczająco dużo przykładów
* Dla ustalonej liczby przykładów można określić, jaki poziom błędu rzeczywistego może być probabilistycznie zagwarantowany

### Wyznaczanie $|\mathbb{H}|$
* Koniunkcje boolowskie
	* dla każdego atrybutu koniunkcja może zawierać literał, zanegowany literał lub nie zawierać go
	* dodatkowo liczymy stałe $0$ logiczne
	* $|\mathbb{H}| = 3^n + 1$
* Dowolne funkcje boolowskie
	* wszystkie możliwe sposoby etykietowania wszystkich możliwych $2^n$ przykładów z dziedziny
	* $|\mathbb{H}| = 2^{2^n}$

### Przykład
* Rozważania do tej pory były mało realistyczne, bo zakładały że wiemy że istnieje model idealnie pasujących do danych, zakładaliśmy że liczba modeli jest skończona
* Dziedzina - wektory binarne
* Przestrzeń modeli - drzewa decyzyjne
* Węzeł drzewa zawiera jakiś atrybut i zawiera 2 rozejścia (dla 1 i dla 0)
* Drzewo decyzyjne jest innym sposobem zapisu funkcji boolowskiej - jest odwzorowaniem łańcucha binarnego na zbiór $\{0, 1\}$
* Skrajny przypadek - każdy wektor jest dopasowany do oddzielnego liścia - liści jest $2^n$, każdy może mieć 1 z 2 klas, więc bez ograniczenia na głębokość będzie $2^{(2^n)}$ drzew
	* tyle co funkcji boolowskich
* Rozważmy drzewa ograniczone do drzew wysokości 3 (korzeń, 2 węzły, 4 liście)
	* $n \cdot (n-1)^2 \cdot 2^4$ - oszacowanie z góry, nie uwzględnia symetrii

## Agnostyczne uczenie się
* Nie ma pewności, że $c \in \mathbb{H}$
	* może nie istnieć model, który mógł by dać błąd mniejszy niż $0.1$
* Nie można zagwarantować dowolnie małego błędu, ale można zagwarantować dowolnie małą różnicę między błędem rzeczywistym a błędem na zbiorze trenującym
	* teraz rozważamy $P(e_{\Omega, c}(h) > e_{T,c}(h) + \epsilon) \le \delta$
	* wcześniej rozważaliśmy $P(e_{\Omega, c}(h) > \epsilon) \le \delta$
* Ograniczenie dla ustalonego modelu $h$ (Hoeffdinga)
	* $P(e_{\Omega, c}(h) > e_{T,c}(h) + \epsilon) \le e^{-2m\epsilon^2}$
	* nie omawiamy dokładnie
* Ryzyko zbyt dużego błędu dla któregokolwiek modelu
	* $P(e_{\Omega, c}(h) > e_{T,c}(h) + \epsilon) \le |\mathbb{H}|e^{-2m\epsilon^2} \le \delta$
	* $m \ge \frac{1}{2\epsilon^2} ( \ln|\mathbb{H}| + \ln1/\delta)$ 
	* $\epsilon \ge \sqrt{\frac{1}{2m} ( \ln|\mathbb{H}| + \ln1/\delta)}$ 
* Z prawdopodobieństwem $1-\delta$
	* $e_{\Omega,c}(h) \le e_{t,c}(h) + \sqrt{1/2m(\ln |\mathbb{H}| + \ln1/\delta)}$
	* ograniczenie dotyczy wszystkich modeli
	* nie ma gwarancji, że algorytm znajdzie najlepszy
	* mając $m$ przykładów możemy zapewnić taki epsilon lub większy - nie zakładając niczego o algorytmie
* Błąd rzeczywisty może być tak bliski błędowi na zbiozre trenującym jak chcemy (przy wystarczającej liczbie przykładów)
* Prawie na pewno błąd rzeczywisty nie będzie znacząco gorszy niż na zbiorze trenującym przy danej liczbie przykładów

## Wymiar VC
Wymiarem $VC$ przestrzeni modeli $\mathbb{H}$ jest maksymalna liczba $k$ taka, że **istnieje** $k$ przykładów, dla których każde z tych $2^k$ możliwych etykietowań jest realizowane przez pewien model z przestrzeni $\mathbb{H}$, albo $\infty$ jeśli warunek ten jest spełniony dla dowolnego $k$.

* Wymiar Vapnika-Chervonenkisa
* Intuicja
	* w dużej przestrzeni modeli trudno się uczyć bo jest więcej możliwości do wyboru
	* może jeśli modeli jest więcej to większa szansa żeby istniał dobry model
	* można rozważyć inne miary bogactwa przestrzeni modeli określająca jak trudno się w niej uczyć - wymiar VC
	* nie liczymy ile jest modeli, tylko na ile sposobów potrafią rozrzucać przykłady pomiędzy klasami
* Przy klasach binarnych i $k$ przykładach jest $2^k$ etykietowań
* Maksymalna liczba przykładów, którą na pewno można dokładnie klasyfikować dla dowolnego pojęcia $c$
* Modeli musi być $|\mathbb{H}| \ge 2^{VC(\mathbb{H})}$ więc $VC(\mathbb{H}) \le \log_2 |\mathbb{H}|$

### Przykład
* Dziedzina - liczby rzeczywiste
* Pojęcie - przedziały
* Dla jednego przykładu można wziąć przedział do którego należy lub taki do którego nie należy, VC >= 1
* Czy dla dwóch przykładów możliwe są wszystkie 4 etykietowania? - tak -> VC >= 2
* Dla 3 niemożliwe jest uzyskanie wszystkich etykietowań
	* nie ma przedziału który zawiera punkt 1 i 3, a nie 2 - VC = 2

### Przykład
* Dziedzina - $\mathbb{R}^2$
* Pojęcie - prostokąty
* Dla 3 przykładów - da się uzyskać wszystkie 8 etykietowań -> VC >= 3
	* nie da się dla punktów współliniowych, ale szukamy takiego $k$ dla których **istnieje** ..., nie dla dowolnych
	* nie musimy rozważać niewygodnych przypadków, wystarczy pokazać 1 konkretny układ
* Dla 4 się da -> VC >= 4
* Dla 5 raczej się nie da, ale trudniej udowodnić że VC jest nie większy niż n

### Przykład
* Model - prosta (ze znakiem), dwie klasy
* Chyba VC=3, może dla n wymiarów jest n+1
* W ogólności wymiar VC nie jest proporcjonalny do wymiarowości zadania (liczby atrybutów)
* Kontrprzykład - klasa binarna - znak wyrażenia $\sin(\alpha x)$, jest 1 wymiar ale da się tak dobrać $\alpha$, żeby osiągnąć wszystkie etykietowania, rozmieszaczmy przykłady w pozycjach $1/2^k$
* wymier VC jest nieskończony

### Przykład
* Wektory binarne, koniunkcje boolowskie
* Wybieramy przykład z jedynką i zerami na pozostałych pozycjach
* $VC \ge n$, można udowodnić że jest dokładnie $VC=n$

### Zastosowanie wymiaru VC
 Wymiar VC pozwala dostarczyć gwarancje dowolnie małego błędu (bliskiego błedowi na zbiorze trenującym) dla nieskończonych przestrzeni modeli.

**Spójne uczenie się** - do uzyskania przez spójny algorytm uczenia się z prawdopodobieństwem co najmniej $1-\delta$ modelu o błędzie rzeczywistym nieprzekraczającym $\epsilon$ wystarczy $m$ przykładów trenujących.

$$ m \ge \frac{1}{\epsilon} (4 \log_2(2/\delta) + 8VC(\mathbb{H}) \log_2(13/\epsilon)) $$

**Agnostyczne uczenie się** - z prawdopodobieństwem $1-\delta$

$$ e_{\Omega,c}(h) \le e_{T,c}(h) + \sqrt{\frac{1}{m}(VC(\mathbb{H})(\ln\frac{2m}{VC(\mathbb{H})}+1)+\ln(4/\delta))} $$

## Podsumowanie wniosków z teorii
* Jeśli jest dużo modeli (liczba lub przestrzeń modeli jest bogata i złożona (wymiar VC) to uczenie jest trudniejsze
* Zbyt bogata przestrzeń modeli zwiększa ryzyko nadmiernego dopasowania
	* potrzeba więcej przykładów trenujących żeby uzyskać mniejszy błąd
* Zbyt uboga przestrzeń modeli zwiększa ryzyko niedopasowania
	* zmniejsza szansę, że istnieje model o wystarczająco małym błędzie
* Trzeba znaleźć balans
* W praktyce spójne uczenie nie jest pożądane, mamy gwarancję teoretyczną małego błędu, ale może wymagać tak dużej liczby przykładów że jest nierealistyczne
	* często nie może istnieć model o zerowym błędzie - mamy za mało atrybutów
* Nadmierne dopasowanie jest tym większym problemem dla bogatej przestrzeni modeli i małego zbioru trenującego
* Praktyczne algorytmy mogą używać bogatych przestrzeni modeli, ale przycinają ją przez dodatkowe mechanizmy - efektywnie redukują wymiar VC
	* np. algorytm budowania drzew preferuje niższe drzewa
	* efektywny wymiar VC - można wyznaczać eksperymentalnie
* Brzytwa Ockhama - preferencja dla prostych modeli