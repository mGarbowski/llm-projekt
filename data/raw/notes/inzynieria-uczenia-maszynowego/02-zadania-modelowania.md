# Definiowanie zadań modelowania

## Kluczowe elementy
* Jakie jest zadanie biznesowe / domenowe
	* czy je dostatecznie dobrze rozumiemy
	* jakie są ograniczenia (czasowe, zasobów, formalne, ...)
* Jakie są zadania modelowania
	* czy są odpowiednie dane do budowy modeli
	* czy rozumiemy proces, który je wygenerował
* Jakie są kryteria sukcesu
	* na poziomie zadań modelowania (analityczne)
	* biznesowe

## Formułowanie zadania biznesowego
* Potrzebny jest ekspert domenowy
	* np. product owner w metodologiach zwinnych
	* dobrze rozumie zagadnienie, którym mamy się zająć i wynikające z niego potrzeby
	* zna specyfikę pracy nad modelowaniem danych
	* jest osobą decyzyjną w zakresie projektu - wspólne ustalenia są wiążące
* Analizujemy kontekst w jakim występuje potrzeba biznesowa
	* jaka jest obecna sytuacja
	* co ma zostać wprowadzone / zmienione
	* jakie właściwości / cechy powinno mieć docelowe rozwiązanie
	* jakie są założenia, oczekiwania, ograniczenia, zasoby

## Biznesowe kryteria sukcesu
* Pytanie pomocnicze - co chcemy zrobić?
* Poprawiamy istniejące podejście?
	* niekoniecznie stosujące UM
* Spełniamy jasno sprecyzowane wymaganie klienta?
* Staramy się przewyższyć konkurencję / standardy branżowe?
* Prowadzimy wstępne prace badawcze / rozpoznajemy temat?
	* z ograniczeniami czasowymi / zasobowymi / budżetowymi
* Klienta interesuje zwrot z inwestycji?

## Mapowanie zadania domenowego na analityczne
* Precyzujemy zadania modelowania i relacje między nimi
* Zazwyczaj - definiujemy jedno lub kilka zadań, których wyniki łączymy tak, aby realizowały zadanie biznesowe
* Określamy jak będziemy weryfikować kryteria sukcesu
	* pozwolą stwierdzić czy przygotowane rozwiązanie spełnia oczekiwania klienta
	* pomagają ustalić, czy potrzebna będzie jeszcze kolejna iteracja pracy nad projektem

Jeśli nie wiemy jak dany problem biznesowy w bezpośredni sposób wyrazić w postaci zadań modelowania - często skuteczne będzie jedno z dwóch podejść
	
* Wyszukiwanie analogii
	* staramy się zidentyfikować zadania domenowe o podobnej strukturze, dla których wiemy jak zdefiniować zadania analityczne
	* być może z innych dziedzin
* Dekompozycja
	* rozkładamy zadanie na bardziej podstawowe elementy, które wiemy jak rozwiązać

## Podstawowe typy zadań modelowania

### Klasyfikacja
* Przewidujemy klasę dla danych wejściowych
* Model $f: X \rightarrow \{c_1, c_2, \ldots, c_m\}$
* Przykładowe zastosowania
	* rozpoznawanie obrazów
	* detekcja spamu
	* określanie gatunku utworów muzycznych
* Przykładowe metody
	* regresja logistyczna
	* naiwny klasyfikator bayesowski
	* SVM
	* perceptrony wielowarstwowe (MLP)

### Regresja / aproksymacja
* Predykcje są liczbami ciągłymi
* Model $f: X \rightarrow Y \subset \mathbb{R}^m$
* Przykładowe zastosowania
	* przewidywanie parametrów procesów technologicznych, zysku z inwestycji, obrotów firmy
* Przykładowe metody
	* regresja liniowa
	* SVR
	* random forest
	* sieci MLP

### Grupowanie
* Poszukujemy funkcji, która podzieli dane na rozłączne grupy
* Zadanie bez nadzoru
* Model $f: X \rightarrow \{g_1, \ldots, g_m\}$
	* liczba grup często ustalana empirycznie lub na podstawie wiedzy eksperckiej
* Przykładowe zastosowania
	* segmentacja klientów
	* automatyczna kategoryzacja produktów
	* wyszukiwanie podobnych produktów
* Przykładowe metody
	* k-średnich
	* sieci SOM
	* affinity propagation
	* DBSCAM

### Analiza szeregów czasowych
* Chcemy przewidzieć przyszłe wartości szeregu czasowego $x_1, x_2, \ldots$
	* $x_i \in \mathbb{R}$
* Postać modelu zależy od konkretnej metody
* Przykładowe zastosowania
	* przewidywanie wahań giełdowych
	* wskaźników ekonometrycznych
	* temperatury powietrza
* Przykładowe metody
	* ARIMA
	* wygładzanie wykładnicze
	* metody regresji

### Modelowanie sekwencji
* Poszukujemy funkcji, która dla danej sekwencji wejściowej będzie przewidywać sekwencję / sygnał wyjściowy
* Model $f: X \rightarrow Y$
	* $X$ przestrzeń sygnałów wejściowych
	* $Y$ przestrzeń sygnałów wyjściowych
* Przykładowe zastosowania
	* tłumaczenie maszynowe
	* klasyfikacja tekstów
* Przykładowe metody
	* sieci LSTM
	* GRU
	* transformery

### Rankingowanie
* Poszukujemy funkcji porządkującej elementy z danej przestrzeni pod kątem ich relewantności dla użytkownika
	* np. produkty opisane przez zestaw atrybutów
* W przypadku podejścia oceniającego relewantność pojedynczego elementu
	* $f: X \rightarrow [0,b]$
	* $b < \infty$
* Przykładowe zastosowania
	* sortowanie wyników wyszukiwania
* Stosowane są metody z dziedziny learning-to-rank

### Generowanie rekomendacji
* Poszukujemy funkcji, która na podstawie wektora informacji kontekstowych dla danego użytkownika zwróci wektor elementów dla tego użytkownika odpowiednich
* Przykładowe zastosowania
	* polecanie utworów muzycznych, filmów, produktów w sklepach internetowych
* Przykładowe metody
	* collaborative filtering
	* k-najbliższych sąsiadów
	* Gru4Rec

### Analiza przeżycia
* Przewidywanie długości życia badanych obiektów w przypadku, gdy występuje tzw. cenzurowanie danych
	* nie mamy kompletu informacji o długości życia obiektów w danej próbie
* Przykładowe zastosowania
	* badania medyczne
	* diagnostyka silników lotniczych (predictive maintenance)
	* modelowanie aukcji vickreya
* Przykładowe metody
	* krzywe Kaplana-Meiera lub Wibulla

### Modele generatywne
* Modele generatywne umożliwiają konstrukcję elementów należących do skomplikowanych przestrzeni (np. obrazów)
	* Generative Adversarial Networks
	* Variational Autoencoders
	* Stable Diffusion
	* LLMs

### Modele językowe
* Pozwalają oszacować prawdopodobieństwo $P(w|w_1,\ldots,w_n)$
	* $w$ - interesujące nas słowo / token
	* $w_1,\ldots,w_n$ - słowa / tokeny zapewniające kontekst
* W zależności od tego jak wygląda kontekst możemy mieć modele do generowania tekstu lub jego rozumienia
	* Generowanie (np. GPT) - *Ala ma ???*
	* Rozumienie (np. BERT) - *Ala ??? kota*

## Składniki budowy modelu predykcyjnego
* Struktura modelu
* Funkcja celu
* Metoda optymalizacji

## Wstępny dobór metod modelowania
* Typ zadania
* Charakter danych uczących
	* wielkość zbioru
	* wartości brakujące
	* typy atrybutów
	* rozkłady atrybutów
	* struktura zależności między atrybutami
* Jakie modele sugeruje nam literatura? Jakie wcześniej nam zadziałały?
* Jakie metody dobrze znamy?
* Co jest wspierane przez ekosystem, w którym będzie działać model?
* Jakie mamy zasoby sprzętowe?
* Jak istotne będzie wyjaśnianie predykcji (i inne aspekty niefunkcjonalne)?

### Podsumowanie
* Biznesowe kryteria / miary jakości
	* perspektywa klienta
	* sprawdzają czy rzeczywiste zadanie zostanie rozwiązane
* Zadania modelowania, analityczne kryteria sukcesu
	* ułatwiają pracę analitykom
	* pozwalają dopasować się do standardowych zagadnień
* Mapowanie czasami nie jest oczywiste, wymaga doświadczenia
* Dochodzi jeszcze perspektywa techniczna
* Nie zawsze da się zmierzyć kryteria biznesowe na danych offline

## Wymagania
### Wymagania techniczne
* Zazwyczaj *typowe* dla systemów informatycznych
	* maksymalny czas odpowiedzi
	* minimalna przepustowość
	* ograniczenia na użycie zasobów
	* dopasowanie do konkretnych technologii
	* itd.

### Wymagania funkcjonalne
* Określają cel, jaki ma realizować system - jego funkcje
* Powinny być kompletne i spójne
* W przypadku UM - specyfikowane przez miary jakości i kryteria sukcesu

### Wymagania niefunkcjonalne
* Dotyczą tego jak ma działać
* Określają dodatkowe ograniczenia odnoście jego zachowania

### Wymagania niefunkcjonalne w UM
* Zagadnienie jeszcze nie do końca zbadane
	* mało publikacji na ten temat
* Powoli krystalizuje się zestaw istotnych z praktycznego punktu widzenia aspektów
	* transparentność / zdolność wyjaśniania predykcji (XAI)
	* kwestie związane z bezpieczeństwem i prywatnością (adversarial examples, prywatność różnicowa)
	* fairness / kwestie dyskryminacji
	* testowalność, niezawodność, łatwość utrzymania, itd.
