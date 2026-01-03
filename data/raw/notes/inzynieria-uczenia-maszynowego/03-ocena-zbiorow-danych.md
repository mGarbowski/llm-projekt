# Ocena zbiorów danych

## Czy zbiór danych uczących jest odpowiedni
* Ilość
	* zazwyczaj im więcej tym lepiej
* Jakość
	* jeśli dostępne atrybuty nie niosą silnego sygnału / informacji (niska jakość) to więcej danych nie pomoże
* Reprezentatywność

## Reprezentatywność danych
* Dane do analizy są próbą losową pochodzącą z pewnej większej populacji / z docelowego rozkładu $\mathcal{D}$ 
* Reprezentatywna próba losowa, to taka która pozwala w przybliżeniu opisać całą populację / rozkład $\mathcal{D}$
* Niereprezentatywna próba zawiera dane pochodzące ze specyficznego wycinka populacji

### Tworzenie reprezentatywnego zbioru danych
* Żeby zapewnić reprezentatywność zbioru danych trzeba losować do niego elementy zgodnie z rozkładem $\mathcal{D}$
	* idealny przypadek
	* problem - nie znamy rozkładu
* W uczeniu maszynowym pojawiają się skomplikowane rozkłady
	* np. rozkład zdań w języku polskim
* Trudno w ogóle dowieść, że generator działa zgodnie z zadanym rozkładem

### Problem z reprezentatywnością
* W większości przypadków dane są w mniejszym lub większym stopniu obciążone
	* nie znamy rozkładu
	* brak możliwości próbkowania z rozkładu
	* wysokie koszty pozyskania danych
	* zbyt mały zbiór

### Ocena reprezentatywności
* Jeśli znamy postać rozkładu $\mathcal{D}$
	* wykresy QQ (kwantyl-kwantyl)
	* testy statystyczne
	* histogramy
	* rzadko spotykany scenariusz
* Jeśli nie znamy $\mathcal{D}$
	* pozostaje stosowanie wiedzy o dziedzinie (wiedzy eksperckiej)
	* czy w danych występują najważniejsze atrybuty

## Jakość
* Typowe problemy
	* błędy w danych, zaszumienie
	* brakujące wartości
	* niespójność
	* informatywność
* Więcej na kolejnych wykładach

## Ilość

### Minimalna wielkość zbioru uczącego - metody klasyczne
* Znana heurystyka - wielkość zbioru uczącego powinna być 10 razy większa niż liczba parametrów estymowanych przez model
* W uczeniu głębokim modele z miliardami parametrów
* Za mało danych - większy problem przeuczenia
* Nie ma jednoznacznej odpowiedzi, uniwersalnej heurystyki do dobrania rozmiaru zbioru uczącego
* Liczenie przykładów ma niuanse
	* przy dużych modelach językowych mówimy o liczeniu tokenów, jedno zdanie to wiele tokenów
	* stosuje się regularyzację
	* stosuje się przekształcenia obrazów
* W praktyce porównuje się działanie modelu z innymi znanymi modelami

### Metody klasyczne vs uczenie maszynowe
* W metodach klasycznych są relatywnie proste struktury modeli
	* łatwiejsza analiza
	* mniej parametrów
	* możliwe precyzyjne założenia odnośnie rozkładów zmiennych wejściowych i wyjściowych
	* założenia odnośnie danych uczących da się wyprowadzić analitycznie
* W metodach uczenia maszynowego modele realizują skomplikowane (potencjalnie dowolne) funkcje nieliniowe
	* trudna, czasami niemożliwa analiza
	* skomplikowane przestrzenie danych wejściowych i wyjściowych
	* wymagania odnośnie danych uczących wynikają w dużej mierze z obserwacji praktycznych / doświadczenia
	* istniejące gwarancje teoretyczne okazują się zbyt mało precyzyjne w praktyce (np. twierdzenie o uniwersalnej aproksymacji dla sieci neuronowych)

### Podział dostępnych danych
* Typowa praktyka - podział na 3 części
* Zbiór uczący
	* do trenowania modelu
* Zbiór walidacyjny
	* do strojenia parametrów
	* selekcji atrybutów
	* podejmowania decyzji odnośnie dalszych kroków
* Zbiór testowy
	* jedynie do testowania
	* nie podejmujemy na jego podstawie decyzji wpływających na model
* Modele wygrywające konkursy na Kaggle raczej nie będą się nadawać do wdrożenia produkcyjnego
* Testować powinniśmy na najlepszych danych jakie mamy
	* chcemy mieć wiarygodną ocenę
	* lepiej żeby dane uczące były obciążone niż testowe i walidacyjne
	* łatwiej i taniej zebrać obciążony zbiór
	* zjawisko covariate shift

## Obciążenie i wariancja modelu
* **Modelu**, a nie danych
* Bias/variance tradeoff
* Obciążenie - błąd wynikający z jego niedopasowania do rzeczywistości / błędnych założeń / nieodpowiedniej struktury
	* błąd na zbiorze treningowym
* Wariancja modelu wynika z nadmiernego dopasowania do konkretnej próbki danych
	* różnica błędu pomiędzy zbiorem treningowym, a walidacyjnym
* Kompromis
	* bardziej skomplikowany model - zmniejsza obciążenie, zwiększa wariancja
* Małe obciążenie, mała wariancja
	* pożądana sytuacja
	* mały błąd na zbiorze walidacyjnym i treningowym
* Małe obciążenie, duża wariancja
	* nadmierne dopasowanie
	* zbyt skomplikowany model lub za mały zbiór uczący
	* model wycisnął z danych co się da, ale nie generalizuje się
* Duże obciążenie, mała wariancja
	* niedostatecznie dobry model
	* zbyt trudne zadanie lub nieodpowiednia architektura
* Duże obciążenie, duża wariancja
	* najgorsza sytuacja
	* nadmiernie dopasowany model słabej jakości
	* zbyt trudne zadanie, nieodpowiednia architektura lub zbyt mały zbiór uczący
	* na pewno przyda się więcej danych
	* do rozwagi zmiana architektury
* Skąd wiemy jakie obciążenie jest duże, a jakie małe
	* zależy od poziomu wyników, który nas satysfakcjonuje
	* powiązane (może nie bezpośrednio) z kryteriami sukcesu

### Zbiór walidacyjny / testowy a miary jakości
* Im mniej danych, tym mniej precyzyjnie określają jakość
* W klasyfikacji binarnej
	* jeśli zbiór ma 100 elementów, to nie wykryjemy różnicy dokładności mniejszej niż 1%
* Przy strojeniu hiperparametrów
	* różnica na 5. miejscu po przecinku - to raczej błędy numeryczne, nie ma sensu tego rozważać

### Przykładowa sytuacja
Trenujemy model regresji logistycznej na dużym reprezentatywnym zbiorze danych, ... proces o skomplikowanej nieliniowej naturze

Prawdopodobnie będziemy mieć problem z obciążeniem - prosty model do modelowania złożonego, nieliniowego zjawiska

## Jak dużo danych wymaga nasz model
* Nie ma jasnych kryteriów oceny
	* generalnie im więcej parametrów, bardziej skomplikowany model, tym większe zbiory są potrzebne
* Często prostszy algorytm uczący zasilony bardzo dużą ilością danych okazuje się lepszy niż skomplikowane, eksperckie podejścia

## Co robić jak mamy za mały zbiór danych do modelowania

### Zmiana metody modelowania
* Prostszy model, bardziej zaawansowane atrybuty
* Transfer learning, few-shot learning, in-context learning
* Zmiana zadania modelowania
	* np. detekcja anomalii zamiast klasyfikacji binarnej
	* np. przy klasyfikacji wieloklasowej, gdzie pewne klasy są bardzo mało liczne

### Zwiększenie ilości danych
* Najlepiej zebrać więcej danych ze źródła
	* nie zawsze możliwe
* Multiplikacja istniejących danych
* Generowanie danych syntetycznych
* Manualne etykietowanie danych

## Użycie prostego modelu
* Im bardziej skomplikowany model tym więcej danych potrzeba
* Każde zadanie klasyfikacji można załatwić klasyfikatorem liniowym - w odpowiedniej przestrzeni
	* bardziej zaawansowane atrybuty pozwalają użyć prostszego modelu
* Bardziej zaawansowane atrybuty
	* wytworzone na podstawie wiedzy eksperckiej
	* opracowanie z wykorzystaniem innych modeli przez tzw. transfer wiedzy

### Przykład
* Atrybuty
	* timestamp
	* nazwa produktu
	* cena
	* ocena
	* treść recenzji
	* czy klient wróci (etykieta)
* Można zrobić model liniowy na samej cenie i ocenie
* Można zastosować gotowy model do wykrywania sentymentu w tekście i zamienić treść recenzji na binarną zmienną
* Można zastosować kodowanie dyskretne nazwy produktu
* Można wyciągnąć markę z nazwy produktu i zakodować ją dyskretnie
* Można zastąpić cenę centylem ceny w tej samej kategorii - informacja czy cena to dużo czy mało zamiast surowej liczby
* Na cenę można patrzeć w odniesieniu do
	* grupy podobnych produktów
	* marki
	* historii ceny tego samego produktu
	* cena wyrwana z kontekstu niewiele mówi
* Przekształcenie oceny
	* czy jest dobra na tle danego recenzenta
* Przekształcenie timestampu
	* czy weekend
	* czy święta
	* czy przed świętami
* Z jednego atrybutu można wyprowadzić nawet kilkadziesiąt atrybutów pochodnych

## Transfer wiedzy / Uczenie transferowe
* Transfer learning
* Wiedzę z trenowania modelu na jednym zbiorze danych stosujemy do innego zadania
	* ekstrakcja cech
	* dostrajanie modelu na nowych danych
* Dotyczy szczególnie sieci neuronowych
	* model ma warstwy
	* początkowe warstwy są odpowiedzialne za ekstrakcję cech
	* końcowe warstwy odpowiadają za klasyfikację cech
	* gdzieś po środku będzie pośrednia reprezentacja wektorowa danych wejściowych, zależy gdzie przetniemy
	* przecinając sieć blisko końca dostajemy reprezentację wektorową w bogatej przestrzeni
	* analogia do zastosowania przekształceń jądrowych w SVM
* Podejścia
	* linear probing - zamrożenie początkowej części sieci i modyfikowanie tylko ostatnich warstw sieci (główki klasyfikacyjnej), tańsze obliczeniowo, do linear probing wystarczy nawet model dostępny przez API
	* full fine tuning - dostrajamy wszystkie wagi, potencjalnie bardziej dokładne wyniki
* Dobre dla wizji komputerowej, NLP
	* dostępne są modele trenowane na ogromnych zbiorach

### Przykłady
* Tworząc klasyfikator znaków drogowych
	* zamiast przetwarzać surowe dane można użyć sieć wytrenowaną na ImageNet, która wygeneruje postać wektorową
	* wektory będą wejściem dla budowanego modelu
* Model do analizy sentymentu wiadomości tekstowych
	* można użyć modelu BERT i douczyć warstwy klasyfikacji

### Przykładowe popularnie stosowane struktury
* Wizja komputerowa
	* ResNet
	* AlexNet/VGG
	* Inception (GoogleNet)
* NLP
	* BERT / RoBERTa
	* GPT
	* ELMo

### Duże modele
* Foundational models
* Zaawansowane architektury neuronowe trenowane na masowych zbiorach danych (cały internet)

### In-context learning
* Strategia adaptacji modelu do nowych zadań bez aktualizacji wag
* Podaje się odpowiednie prompty do gotowego modelu z demonstracjami, a potem właściwy

### Przykład EvoLLM
* Zwykły LLM dostaje prompta z danymi generacji do algorytmu ewolucyjnego
* LLM przewiduje kolejnego osobnika
* raczej jako ciekawostka

### Przykład TabPFN
* Do danych tabelarycznych
* Wytrenowany na sztucznie generowanych zbiorach danych tabelarycznych
* Dostaje zbiór treningowy i atrybuty testowe jako prompt
* Bazuje na grafach przyczynowo-skutkowych (rozwinięcie sieci bayesowskich)
	* na podstawie tego grafu generuje się sztuczny zbiór danych
* Duży czas inferencji
* Zapamiętać i doczytać, potencjalnie bardzo dobre narzędzie

## Generowanie danych syntetycznych
* Przydatne gdy uzyskanie odpowiedniej ilości danych jest trudne lub kosztowne
* Metody
	* modele przyczynowo skutkowe (SCM)
	* generatywne modele neuronowe
	* symulacje monte carlo - przyjmujemy założenia odnośnie jakiejś losowości, piszemy logikę, która symuluje nasze dane - przykład z overbooking
	* symulacje fizykalne

## Multiplikacja istniejących danych
* Zwłaszcza w wizji komputerowej
	* zaszumianie
	* transformacje (translacja, obrót)
	* losowanie przypadków negatywnych
	* oversampling, bootstrapping i modele zagregowane
	* wytrenowanie modelu generatywnego do tworzenia większej ilości danych

### Dane syntetyczne w testach
* Użyteczne do weryfikowania czy algorytm zachowuje się zgodnie z oczekiwaniami (testy jednostkowe)
	* czy jest w stanie wykryć zależności, które są w danych
	* czy nie uczy się szumu - nieistniejących zależności
	* jak sobie poradzi z wartościami odstającymi
* Narzędzia
	* `dataset` z scikit-learn - `make_regression, make_classification, make_blobs`
	* programowanie probabilistyczne - PyMC3
	* prosty generator własnej roboty


## Uczenie aktywne
* Active Learning
* Model wybiera próbki, o których etykiety pyta
* Procedura
	* model jest trenowany na dostępnym zbiorze etykietowanych danych
	* iteracyjny wybór próbek - algorytm wybiera próbkę, człowiek lub wyrocznia etykietuje
	* aktualizacja modelu - trening na rozszerzonym zbiorze
* Strategie wyboru próbek
	* największa niepewność predykcji (funkcja $1-\max_{\hat{y}} P(\hat{y}|x)$, entropia)
	* rozbieżność predykcji - dla modeli komitetowych, jak komitet nie jest zgodny (entropia)
	* największa gęstość informacji - nie patrzy na y, patrzy gdzie w obszarze nieoetykietowanych przykładów znajduje się przykład - bierzemy tego, który jest najbardziej podobny do innych (reprezentatywny dla klastra)
	* itd.
* Trzeba wybrać jakąś strategię
* Zalety
	* zmniejsza koszty etykietowania
	* poprawa dokładności modelu - skupia się na trudnych przypadkach, które więcej wnoszą do uczenia
	* przydatne gdy mamy mało danych
	* dobre przy niezbalansowanych danych, ze zróżnicowaną dystrybucją
* Wady
	* źle dobrana strategia wprowadza obciążenie selekcji - gorsza generalizacja
	* jakość i spójność etykiet wyroczni ma istotny wpływ na wyniki
	* wymaga początkowego zestawu danych
	* komplikuje proces uczenia
	* wybór próbek może być obciążający obliczeniowo

## Manualne etykietowanie danych
* Złożony problem bo raczej pracuje nad tym wiele osób
* Bezpieczniej zrobić niewielką próbkę i uzgodnić całym zespołem przed adnotowaniem całego zbioru
* Mierzenie zgodności adnotacji
	* współczynnik Kappa Cohena
	* obliczane na podstawie tabeli kontyngencji
	* korekta na to że zgodność może być przypadkowa
