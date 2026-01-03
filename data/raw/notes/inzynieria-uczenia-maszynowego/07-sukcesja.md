# Sukcesja

* Jak wiedzieć czy to co wdrażamy jest lepsze od tego co było wcześniej
* Zadanie jest trywialne jeśli jesteśmy w stanie ocenić model dla pojedynczego, statycznego zadania modelowania
	* np. miary jakości na zbiorze testowym
* W rzeczywistości miary jakości są tylko przybliżeniem tego o co nam naprawdę chodzi
* Im bardziej dojrzały system tym kolejne iteracje zazwyczaj dają coraz mniejszą poprawę jakości
* Chcemy oszacować wpływ przyczynowo-skutkowy wyboru modelu na to jak spełniany jest cel biznesowy
	* nie tylko korelację
	* bezpośrednie zbadanie wpływu jest trudne
	* badamy biznesowe miary jakości, zakładamy że są dobrze powiązane z celem biznesowym

## Analiza przyczynowo-skutkowa
* Pearla - strukturalne modele przyczynowo-skutkowe
	* rozwinięcie sieci bayesowskich
* Rubina-Neymana - koncepcja potencjalnych wyników
	* podstawa dla prób kontrolowanych, eksperymentów A/B

### Strukturalny model przyczynowo-skutkowy
* Graf opisuje relacje przyczynowo-skutkowe wiedzy zmiennymi losowymi
* Krawędź od przyczyny do skutku
	* przy sieciach bayesa nie zakładamy przyczynowości
	* założenie - wiemy co jest przyczyną, a co skutkiem
* Operator oznaczających wykonywanie akcji
	* $P(X | do(Y))$
* Musimy być w stanie opisać cały graf
	* graf jest kompletny i uwzględnia wszystkie zmienne
* The book of why - dobry podręcznik wprowadzający

### Model Rubina-Neymana
* Bazuje na koncepcji potencjalnych wyników
	* porównuje się alternatywne rzeczywistości
	* jeśli 2 rzeczywistości różnią się tylko jednym parametrem to zmiana jakości wynika ze zmiany tego parametru
* Próby RCT - losowe próby kontrolowane
	* w informatyce to eksperymenty A/B
	* reprezentatywną populację dzieli się na 2 grupy
	* w jednej prowadzi się interwencję, coś się zmienia (np. podaje lek)
	* w grupie kontrolnej nic się nie zmienia (np. podaje placebo)
	* po jakimś czasie wykonujemy pomiary w obu grupach
* Kluczowe elementy 
	* losowy przydział osób do grupy, osoba nie może zmienić grupy
	* grupy muszą być reprezentatywne dla populacji - duże i zróżnicowane
	* konieczna jest interwencja - jakaś zmiana pomiędzy grupami
	* wynik obserwowany dla danej osoby nie powinien wpływać ani zależeć od sposobu przydziału innych osób do grup (SUTVA)

## Eksperymenty A/B

### Nomenklatura
* Użytkownicy - osobne jednostki korzystające z naszego modelu
	* nie zawsze osoby fizyczne
	* odpowiednik populacji
* Warianty - porównywane wersje naszego modelu uczenia maszynowego
* Grupy kontrolne
	* grupy użytkowników, dla których nic się nie zmienia
	* jest im serwowana poprzednia wersja modelu
	* bez interwencji
* Interwencje - momenty wdrożenia produkcyjnego

### Przeprowadzanie eksperymentu
* Środowisko produkcyjne musi umożliwiać równoległe korzystanie z obu modeli
* Są zbierane miary jakości z podziałem na A i B
* Procedura
	* ustalamy adekwatną wielkość próby i czas trwania eksperymentu
	* dzielimy ruch na niezależne części odpowiedniej wielkości
	* czekamy, aż uzbiera się do analizy próbka danych pożądanej wielkości

### Podział ruchu
* Próbka ruchu musi być reprezentatywna
* Im mniejsza różnica pomiędzy jakością modeli, tym większa próba jest potrzebna do jej wykrycia
* Raz przydzielony użytkownik nie może zmieniać wariantu
* Może występować efekt świeżości
	* nowy wariant wydaje się lepszy tylko dlatego że jest nowy
* Żeby użytkownicy nie przeskakiwali między grupami
	* musimy przechowywać informację gdzie trafia użytkownik
	* można zapisywać przypisanie do grup w bazie danych
	* można użyć funkcji mieszających (consistent hashing) i identyfikatory użytkowników
* Naruszenie SUTVA
	* kiedy oba modele współdzielą zasoby
	* np. wspólny budżet, jeden model wyczerpie, drugiemu już nic nie zostanie

### Jak długo powinien trwać eksperyment
* Na tyle długo żeby dostać reprezentatywną próbę w obu grupach
* Na tyle długo żeby być w stanie wykryć różnicę między wariantami
* Istotna jest sezonowość, duża próbka ale z jednego dnia może nie być reprezentatywna
	* zazwyczaj wielokrotność całych tygodni

## Testy statystyczne
* Statystycznie istotne $\simeq$ chyba nieprzypadkowe

### Przykład - fabryka monet
* Chcemy mieć monety symetryczne
* Rzucamy jedną monetą 100 razy
	* jeśli jest symetryczna to oczekujemy ok 0.5 orłów
	* jeśli jest asymetryczna to będzie wyraźna przewaga jednej ze stron
* Jeśli odsetek orłów zbyt odbiega od symetryczności
	* $|\mu - 0.5| > m_\alpha$
* Jak ustalić próg $m_\alpha$ - wartość krytyczną

### Wartość krytyczna i statystyka
* Wartość krytyczna to punkt odcięcia, który rozdziela eksperymenty prowadzące do odrzucenia hipotezy eksperymentalnej od tych które nie dają do tego podstaw
	* odrzucenie hipotezy zerowej na rzecz hipotezy alternatywnej
* Z wartością krytyczną porównujemy określony wskaźnik liczbowy obliczany na podstawie danych z naszego eksperymentu
* Funkcja wyliczająca wartość tego wskaźnika - statystyka testowa
	* $|\mu - 0.5|$ z przykładu to statystyka
* Test dwustronny i jednostronny
	* dwustronny - odrzucamy hipotezę zerową jeśli dostaniemy wartość za dużą lub za małą
	* jednostronny - odrzucamy hipotezę zerową jeśli dostaniemy wartość za dużą (albo oddzielnie za małą)

### Przykład - formalny opis
* Wykonujemy $N$ rzutów monetą
* Odsetek wyrzuconych orłów $\mu$
* hipoteza zerowa - moneta jest symetryczna,
	* $H_0: \mu = 0.5$
* Hipoteza alternatywna - moneta jest asymetryczna
	* $H_1: \mu \ne 0.5$
* W przypadku dużego N rozkład zmiennej $\mu$ będzie dawał się przybliżać rozkładem normalnym
	* możemy zastosować statystykę testową testu z

### Test z
* $n$ - liczba prób
* $k$ - liczba sukcesów
* $z$ - ma rozkład standardowy normalny kiedy hipoteza jest prawdziwa
	* ogony są mało prawdopodobne
* Próg istotności $\alpha$, np. 5%
	* na co to wpływa - widać jak testujemy nie jedną monetę, tylko wiele
* Nie daje nam pewności

### Błędy typu 1 i typu 2 - intuicja
* Błąd typu 1
	* niepoprawne odrzucenie hipotezy zerowej $H_0$
	* jeśli $\alpha=0.05$
	* testując 100 symetrycznych monet, test niepoprawnie odrzuci jako asymetryczne 5 z nich
	* uznajemy rezultaty mało prawdopodobne jako podstawę do odrzucenia hipotezy
* Błąd typu 2
	* jeśli $\beta = 0.8$
	* testując 100 asymetrycznych monet, test nie będzie w stanie wykryć 20 z nich
	* przeoczenia odrzucenia $H_0$ na rzecz $H_a$
* Błędy typu 1 występują z prawdopodobieństwem $\alpha$
* Błędy typu 2 występują z prawdopodobieństwem $\beta$

### Moc testu statystycznego
* $(1-\beta)$
* Prawdopodobieństwo niepopełnienia błędu typu 2
* Zależy od $\alpha$ i od wielkości próby $N$ i od siły efektu
* $\beta$ wylicza się eksperymentalnie, np. przez symulację
* Większa wielkość próby - większa moc
	* mniejszy błąd, test jest bardziej czuły
* Większe $\alpha$ - większe ryzyko błędu I rodzaju, mniejsze II rodzaju
	* mniejsze $\beta$, większa moc

### Ogólna procedura stosowania testów statystycznych
* W uczeniu maszynowym testy z jednym ogonem (jakość wzrosła / błąd spadł)
* Ustalamy hipotezy testowe
* Wybieramy odpowiedni do hipotez test statystyczny
	* każdy test ma określone założenia
	* np. test z jest do wyników binarnych, odpowiedniej liczby prób, itd.
	* test z, test t-studenta
* Ustalamy poziom istotności, obliczamy wartość krytyczną
* Wyliczamy wartość statystyki testowej i porównujemy ją z wartością krytyczną
	* w zależności od porównania odrzucamy / nie odrzucamy hipotezę zerową
* Użycie testów statystycznych pozwala kontrolować liczbę i charakter popełnianych błędów

## Testy statystyczna w testach A/B
* W serwisie wydzielamy 2 warianty
	* może być więcej ale dzielimy ruch (dostępne próbki danych) na mniejsze porcje
* Procedura
	* ustalamy wielkość próby i czas trwania eksperymentu
	* dzielimy ruch na niezależne części i uruchamiamy oba warianty
	* czekamy aż uzbiera się próbka danych do analizy pożądanej wielkości
	* analizujemy wyniki ustalając, który wariant działa lepiej
* Ważne jest stałe przypisanie użytkowników do grup
* W dojrzałych systemach różnice w metrykach będą bardziej subtelne
* Hipoteza zerowa $H_0: q_A \le q_B$
	* nowy model jest gorszy (niższa jakość)
	* chcielibyśmy odrzucić hipotezę zerową

### Analiza wyników
* Jakości wariantów $q_A$, $q_B$
* Hipoteza zerowa - wariant A nie jest lepszy niż B - mamy nadziej odrzucić hipotezę
* Hipoteza alternatywna - wariant A jest lepszy niż B
* Testy
	* t-Studenta
	* z

### Test t-Studenta
* Założenia
	* miarę jakości możemy opisać rozkładem normalnym
	* mamy podobną wariancję miar jakości obu wariantów
	* próby dla wariantów A i B są różnoliczne
* Jest wiele sformułowań wzoru w zależności od założeń
* Wartość która wychodzi ze wzoru porównujemy z wartością krytyczną
* Liczba stopni swobody
	* związane z nieobciążonym oszacowaniem wariancji
	* istotne dla małych próbek (odejmowanie 1 od liczby próbek)

### Minimal Detectable Effect (MDE)
* Minimalna wielkość efektu potrzebna do uzyskania założonego poziomu mocy przy ustalonym $\alpha$ i wielkości próby
* Prawdopodobieństwo odrzucenia $H_0$ pod warunkiem że $H_1$ jest prawdziwa
* Żeby ustalić wielkość próby
	* ustalamy jaki najmniejszy efekt chcemy wykryć

### p-wartość
* Test odpowiada na pytanie - czy możemy odrzucić hipotezę $H_0$ mówiącą, że wariant A nie jest lepszy od wariantu B
	* na przyjętym poziomie istotności
* p-wartość to prawdopodobieństwa zaobserwowania wartości statystyki, jeśli hipoteza $H_0$ jest prawdziwa
	* wartość statystyki, która wyszła z eksperymentu
* p-wartość **nie** jest prawdopodobieństwem prawdziwości $H_1$
	* nieuprawnione stwierdzenie
	* nie w podejściu częstościowym - na nim bazują testy
	* szukamy stałej, której wartości nie znamy
* Dla różnych statystyk wartości są w różnych skalach
* Pakiety statystyczne podają p-wartość

## Podejście bayesowskie do eksperymentów A/B

### Twierdzenie Bayesa

$$P(h|d) = \frac{P(d|h)P(h)}{P(d)}$$

* $P(h|d)$ - prawdopodobieństwo prawdziwości hipotezy, kiedy zaobserwowaliśmy dane
* $P(d|h)$ - prawdopodobieństwo zaobserwowanych danych pod warunkiem że hipoteza jest prawdziwa
* $P(h)$ - wstępne przekonanie, że hipoteza jest prawdziwa
* $P(d)$ - nasze wstępne przekonanie odnośnie zaobserwowania danych

### Wnioskowanie bayesowskie
* Chcemy poznać parametr rozkładu zmiennej losowej
* Ustalamy wiedzę pierwotną
* Wykonujemy eksperyment, zbieramy obserwacje
* Aktualizujemy nasze przekonania odnośnie rozkładu tego parametru

### Analiza eksperymentu A/B w podejściu bayesowskim
* Miary jakości traktujemy jako zmienne losowe, chcemy znaleźć ich rozkłady - $\mu_A$, $\mu_B$
	* wcześniej traktowaliśmy je jako nieznane stałe
* Potrzebujemy przyjętych a priori rozkładów tych zmiennych
* Po przeprowadzeniu eksperymentu i zebraniu danych aktualizujemy rozkłady
* Skąd brać założenia a priori
	* wiedza ekspercka
	* poprzednie eksperymenty

### Funkcja straty
* Mając rozkłady możemy policzyć prawdopodobieństwo, że wariant A jest lepszy od B
* Strata związana z wdrożeniem gorszego modelu
	* język biznesu
* Wartość oczekiwaną straty jako funkcję wybranego wariantu liczymy używając rozkładu łącznego zmiennych $\mu_A, \mu_B$
* Jak dużą stratę poniesiemy jeśli popełniliśmy błąd
* Możemy założyć maksymalną stratę $\epsilon$
* Procedura
	* uruchamiamy eksperyment
	* zbieramy dane do oszacowania miar jakości
	* wyliczamy wartość oczekiwanej straty dla obu wariantów
	* jeśli dla któregoś z wariantów $E_L(v) < \epsilon$ - możemy ten wariant uznać za lepszy

### Czas trwania eksperymentu
* Nie ma prostego wzoru
* W praktyce - symulacja Monte Carlo do określenia ile trzeba zebrać danych, żeby prawdopodobieństwo wyboru lepszego wariantu było np. >90%
* Zwykle wymaga mniej danych niż analiza częstościowa

## Analiza częstościowa a bayesowska
* Częstościowa
	* bardziej restrykcyjne założenia odnośnie rozkładów prawdopodobieństw
	* p-wartości są trudne w interpretacji
	* zazwyczaj potrzeba więcej danych
	* bardziej popularne
* Bayesowska
	* łatwiejsze w interpretacji
	* potrzebują mniej danych do udzielenia odpowiedzi
	* bardziej kosztowne obliczeniowo
	* mniej popularne

## Eksperymenty A/B - problemy
* Ukryte zmienne wpływające na wynik
* Obciążone próbki
* Sprzężenia zwrotne
* Nakładające się eksperymenty
* Brak niezależności między grupami (SUTVA)
* Problemy z interpretacją metryk

Bardzo dobra podlinkowana publikacja o eksperymentach A/B, The book of why

### Problemy z interpretacją wyników
* Wykorzystanie testów statystycznych o zbyt małej mocy
* Odrzucanie hipotezy zerowej tuż po przekroczeniu wartości krytycznej
* Przedwczesne zatrzymywanie eksperymentów
* Analizowanie tylko agregowanych wyników, bez sprawdzania podgrup
	* paradoks Simpsona
* Wpływ wartości odstających na uzyskane wyniki
* Efekt świeżości

## Inne metody porównywania modeli

### Eksperymenty A/B nie zawsze są możliwe
* Za mało użytkowników
* Użytkownicy nie mają stałych identyfikatorów
* System nie wspiera podziału ruchu
* Bardzo dynamiczna sytuacja

### Causal Impact
* Wywodzi się z teorii analiz przyczynowo-skutkowych
* Bazuje na koncepcji syntetycznej grupy kontrolnej
	* zachowanie syntetycznej grupy kontrolnej jest estymowane (szereg czasowy)
* Przydatny w szerszym kontekście niż sukcesja modeli

#### Założenia
* To co mierzymy fluktuuje w czasie - szereg czasowy
* Interwencja wpływa na przebieg tego szeregu (wdrożenie nowego modelu)
* Porównujemy dwie rzeczywistości na podstawie
	* zmierzonego zachowania szeregu
	* zachowania szeregu estymującego $y_t$ korzystając tylko ze zmiennych na które interwencja nie może wpływać
* W okresie przygotowawczym trenujemy model, a po interwencji używamy modelu do predykcji
	* model nie wie o interwencji
	* nie ma założeń co do użytego modelu
	* implementacja wykorzystuje bayesowski model w przestrzeni stanów - bardzo dobry do szeregów czasowych
* Bierzemy różnicę między rzeczywistym szeregiem (wpływ interwencji), a estymowanym szeregiem (model prognozuje co by było, na podstawie danych sprzed interwencji)

#### Syntetyczna grupa kontrolna
* Przykłady zmiennych, na które nie wpływa interwencja
	* kalendarz
	* wskaźniki makroekonomiczne
	* pogoda
	* pomiary z innego, niepowiązanego obszaru naszej domeny
