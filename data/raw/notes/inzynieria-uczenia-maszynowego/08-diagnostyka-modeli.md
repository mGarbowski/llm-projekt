# Diagnostyka modeli

## Architektura środowiska produkcyjnego
* Wybór wariantu modelu powinien być przezroczysty dla klienta
* Dane online
	* model może dociągać atrybuty
	* podejścia continual learning - dotrenowywanie modelu na bieżąco, rzadziej stosowane

## Typowe pytania diagnostyczne
* Czy model został wywołany dla danego x
* Co zwrócił model dla danego x
* Które atrybuty mają największy wpływ na predykcję dla danego x
* Jaki wpływ mają na predykcję poszczególne atrybuty
* Jak zmieniłaby się predykcja na skutek modyfikacji atrybutu $x_i$

## Logi
* Mogą udzielić odpowiedzi na pytania
	* czy model został wywołany
	* jakie otrzymał dane wejściowe
	* jaka była jego odpowiedź
* Wygodne jeśli log zawiera zrzut danych, które faktycznie model wykorzystał
	* ogranicza konieczność cofania się w czasie żeby odtworzyć stan atrybutów
* Co jak logów jest dużo
	* próbkowanie
	* skrócenie retencji - trzymać krócej

## Wyjaśnianie predykcji (XAI)
* Regulacje wymuszają w niektórych przypadkach, żeby dostawca mógł wyjaśnić decyzje modelu
* Cel - dostarczenie danej grupie odbiorców szczegółowych informacji/wyjaśnień, dzięki którym zachowanie modelu staje się jasne

### Grupy odbiorców
* Osoby rozwijające modele
	* czy model działa
	* jak poprawić działanie
* Użytkownicy
	* zrozumienie swojej sytuacji
	* weryfikacja uczciwości decyzji modelu
	* co muszą zmienić aby dostać inną odpowiedź
* Użytkownicy - eksperci domenowi (np. lekarze)
	* czy modelowi można zaufać
	* przekonanie eksperta
* Regulatorzy, prawodawca
	* certyfikacja modeli
	* upewnienie się, że model nie narusza jakichś reguł
* Kadra kierownicza
	* ocena zgodności z regulacjami
	* ocena biznesowa

### Główne wątki i cele
* Budowa zaufania ekspertów domenowych do modeli
* Wykrywanie problemów z generalizacją
	* czy model bazuje na artefaktach z danych treningowych?
* Zwiększenie informatywności predykcji modelu
* Uchwycenie zależności przyczynowo-skutkowych przez modele
* Kwestie etyczne związane z ryzykiem dyskryminacji

## Białe i czarne skrzynki w XAI
* Czarna skrzynka
	* model, którego struktury nie znamy / nie mamy dostępu
* Skomplikowany model z wieloma atrybutami efektywnie jest dla człowieka czarną skrzynką
* Jeśli chcemy coś nazwać białą skrzynką
	* interpretowalna, prosta struktura
	* nie za dużo atrybutów
* Jeśli konieczna jest możliwość wyjaśniania predykcji
	* użycie modelu o interpretowalnej strukturze, nie za dużo wymiarów
	* metody wyjaśniania post-hoc dla czarnych skrzynek

### Białe skrzynki
* Znamy kompletną postać modelu, mamy do niej nieograniczony dostęp
* Struktura modelu (nie ma zbyt wielu)
	* modele liniowe
	* reguły decyzyjne / drzewa
	* naiwny klasyfikator bayesowski
	* kNN
	* EBM
* Dobór atrybutów
	* rozsądna wymiarowość
	* człowiek jest w stanie ogarnąć ok. 7 zmiennych
	* zrozumiałe, wysokopoziomowe atrybuty
	* odpowiednie nazewnictwo
* Nie wszystkie są tak samo łatwo interpretowalne

### Klasyfikacja białych skrzynek
* Poziom 1
	* człowiek jest w stanie zasymulować / odtworzyć działanie modelu bez pomocy narzędzi zewnętrznych
	* np. proste i zrozumiałe atrybuty, mało interakcji między atrybutami
* Poziom 2
	* człowiek jest w stanie dokonać dekompozycji modelu
	* zrozumienie danych wejściowych, parametrów, procesu obliczeniowego bez korzystania z zewnętrznych narzędzi
	* można prześledzić odpowiedź
	* np. proste i zrozumiałe atrybuty ale za duża liczba, dużo interakcji
* Poziom 3
	* można przeanalizować od strony algorytmicznej
	* jesteśmy w stanie dokonać dokładnej analizy matematycznej pozwalającej odpowiedzieć na pytanie, w jaki sposób została wygenerowana odpowiedź
	* np. liczba i skomplikowanie zmiennych powoduje, że nie jesteśmy w stanie przeanalizować modelu ręcznie

## Jakość a interpretowalność
* To generalnie przeciwstawne cele
* XAI dąży do poprawy interpretowalności przy zachowaniu jakości
*  Glass box
	* wyjaśnialność wpisana w założenia architektury

## Explainable Boosting Machine
* Model typu glass box
* Uogólniony model liniowy
* Iteracyjne tworzone małe drzewa korzystające tylko z 1 atrybutu
* Każda iteracja uruchamiana jest niezależnie i w losowej kolejności
	* wykorzystuje wszystkie atrybuty do utworzenia drzew
* Drzewa dla atrybutu x są agregowane do wygenerowania wykresów
* Dla każdego atrybutu generuje się wykres - profil
	* uśrednienie ze wszystkich iteracji
	* jak zmienia się predykcja modelu w zależności od atrybutu
* Predykcja modelu jest sumą wykresów
	* można zobaczyć wpływ każdego atrybutu
	* łatwe do interpretacji - jednowymiarowy wykres
	* wykresy działają niezależnie od siebie
	* eksperci są w stanie łatwo interpretować

## Metody agnostyczne względem struktury modelu
### Współczynnik Shapleya
* Pojęcie z teorii gier kooperacyjnych
* Scenariusz
	* $n$ zawodników w drużynie
	* wszyscy dążą do osiągnięcia wspólnego celu
	* sukces jest mierzalny - jesteśmy w stanie przydzielić mu wartość liczbową
	* zadanie - ustalić udział poszczególnych graczy w sukcesie
* $\phi_i(v) = \frac{1}{n!} \sum_\pi v(P_i^\pi \cup \{i\}) - v(P_i^\pi$)
	* $n$ - liczba graczy
	* $v(S) \in \mathbb{R}$ - funkcja oceniająca sukces z gry koalicji graczy $S$
	* $\pi$ - permutacja kolejności dołączania graczy do gry
	* $P_i^\pi$ - podzbiór graczy, którzy wejdą przed graczem $i$, dla permutacji $\pi$
	* $\phi_i(v)$ - kontrybucja $i$-tego gracza w sukcesie
* Zysk z dodania gracza uśredniony po wszystkich permutacjach
* Właściwości
	* rozdzielanie całego zysku pomiędzy n graczy
	* symetria - tak samo skuteczni gracze otrzymują takie same współczynniki
	* liniowość
	* gracz zerowy (neutralny) otrzymuje zerową wartość

### SHAP
* Pakiet, podejście bazujące na współczynniku Shapleya
* Ocena jak dany atrybut wpływa na wartość predykcji
	* atrybuty - zawodnicy
	* zestaw atrybutów - koalicja
	* wartość modelu - zysk, który chcemy podzielić między graczy
* Pokazuje wpływ atrybutów na różnicę względem średniej predykcji
	* dla konkretnego wiersza
* Ciężkie obliczeniowo - wszystkie permutacje atrybutów
* Zalety
	* solidne podstawy teoretyczne (z gier wieloosobowych)
	* działa dla potencjalnie dowolnych modeli uczących
	* dostępne wydajne implementacje w Python i R
* Wady
	* zakłada addytywny wpływ poszczególnych cech, może być błędne dla nieaddytywnych modeli
	* w przypadku dużych modeli, kosztowne obliczenia

### Wykresy break-down
* Koncepcyjnie zbliżona do SHAP
* Kontrybucja $i$-tej zmiennej do wyjaśnienia predykcji dla wektora $x$
	* jak w SHAP
* Arbitralnie wybrana jedna kolejność atrybutów
	* a nie wszystkie permutacje jak w SHAP
	* szybciej się liczy
	* zakłada addytywny wpływ poszczególnych cech
	* gorzej jeśli są interakcje między atrybutami
	* współczynnik Shapleya zakłamuje wyniki jeśli są interakcje - atrybutów nie można rozważać w oderwaniu od siebie (nieprawdziwa jest addytywna dekompozycja)
	* wpływ bardziej przypisuje się atrybutowi, który arbitralnie został wybrany jako pierwszy
* Wizualizacja dla pojedynczego wektora
	* intercept - model stały - średnia
	* na zielono co zwiększa predykcję względem średniej
	* na czerwono co zmniejsza
	* na dole wartość predykcji
	* wyjaśnienie dla konkretnego wektora
* Wizualizacja dla całej populacji
	* wykresy violin dla każdego atrybutu
* Zalety
	* podejście dla potencjalnie dowolnych modeli uczących
	* liniowa złożoność obliczeń względem liczby atrybutów
	* dostępne wydajne implementacje w R z dobrymi wizualizacjami
* Wady
	* istotna jest kolejność, w jakiej uwzględniane są atrybuty - arbitralna
	* zakłada addytywny wpływ poszczególnych cech (jak SHAP)

### Wykresy ceteris-paribus
* Oddzielnie oblicza się wpływ każdego czynnika traktowanego pojedynczo
* Wykres dla konkretnego przykładu
	* zamrażamy wszystkie atrybuty poza tym, który nas interesuje
	* robimy wykres odpowiedzi modelu od tego jednego atrybutu
* Analogicznie dla zmiennych kategorycznych - wszystkie kategorie i wykres słupkowy zamiast ciągłego
	* odchylenia od odpowiedzi modelu dla x
* Podobne - metoda Individual Conditional Expectation
* Dobra do porównywania zachowań różnych modeli
	* możemy ocenić, który model będzie lepszy do wdrożenia
	* gładki vs postrzępiony - może być istotne dla użytkownika-eksperta
* Szczególnie dobre jak analizujemy źle sklasyfikowane atrybuty
* Zalety
	* łatwa w komunikacji, graficzna reprezentacji
	* porównywanie różnych modeli, różnych wektorów wejściowych
* Wady
	* problematyczne są zmienne skorelowane
	* trudna interpretacja, gdy jest zbyt wiele zmiennych
	* niewygodne dla zmiennych dyskretnych o znacznej liczbie wartości

### Local Interpretable Model-agnostic Explanations (LIME)
* Model ma złożoną granicę decyzyjną
* W pobliżu konkretnego x, granicę może da się przybliżyć prostą (modelem liniowym)
* Lokalna aproksymacja
* Zakładamy że dane jest przekształcenie h, które rzutuje problem do przestrzeni wygodniejszej do interpretacji, o niższej wymiarowości
* Dopasowujemy model interpretowalny $f^*(h(x))$ na danych wylosowanych z sąsiedztwa
* Przekształcenia
	* opracowywane dla poszczególnych domen
	* zamiast ciągłych można kubełkować
	* kombinacje zmiennych dyskretnych
	* pojedyncze słowa zamiast całego tekstu (słowa kluczowe)
	* zastosowanie super-pikseli dla obrazków - grupowanie spójnych fragmentów obrazka
* Zalety
	* nie zakłada struktury klasyfikatora
	* dzięki odpowiednio dobranej przestrzeni, model jest łatwy w interpretacji
	* dobrze opisuje lokalne zachowanie wyjaśnianego modelu
* Wady
	* dobranie przekształcenia
	* im większa wymiarowość tym trudniejsze losowanie punktów z sąsiedztwa do trenowania modelu interpretowalnego

## Metody dla sieci neuronowych

### Mapy istotności
* Saliency maps
* Np. dla klasyfikatora
* Liczymy gradient wyjścia neurona dla danej klasy po wejściu
* Wymaga dostępu do modelu i wyliczania pochodnych
* Przedstawia się rezultat jako mapę nakładaną na obraz

### Algorytm RISE
* Podobne do map istotności ale nie wymaga dostępu do modelu i liczenia pochodnych
	* też dla modeli bez dostępnych wag (tylko przez API)
* Za pomocą losowego maskowania
* Jak maskowanie regionu nie zmienia predykcji to znaczy, że nie był istotny
* Ważona suma masek i predykcji daje mapę istotności
* Wymaga wielokrotnego wywołania modelu - kosztowne

### Propagacja istotności (LRP)
* Layer-wise Relevance Propagation
* Rozsmarowanie sygnału wyjściowego na poprzednią warstwę
	* propagacja aż do wejścia
* Szereg reguł określających jak propaguje się istotność
	* inne dla kombinacji typów warstw i funkcji aktywacji
* Różne algorytmy sprowadzają się do mniej lub bardziej przekonujących wizualizacji
	* w praktyce

## Jak zmienić decyzję modelu
* Przykładowy scenariusz - scoring kredytowy
	* wnioskujemy o kredyt hipoteczny
	* wstępny etap związany jest z automatyczną oceną ryzyka
	* wprowadzamy nasze dane do systemu
	* system ocenia ja negatywnie
* Co musielibyśmy zmienić, aby nasz wniosek został zaakceptowany
	* ceteris-paribus może się nadawać jeśli nie ma zbyt wielu atrybutów
* Żeby zmienić predykcję, trzeba przepchnąć x na drugą stronę granicy decyzyjnej
* Znalezienie takiego przekształcenia x - zadanie optymalizacyjne
	* raczej chcemy znaleźć najmniejszą możliwą różnicę wektora
	* standardowe metody optymalizacji (gradientowe, metaheurystyki)
* Ograniczenie do zmian możliwych do wykonania
	* np. zmniejszenie wieku
* Metoda DICE
	* chcemy jak najmniejsze modyfikacje
	* chcemy dużo różnorodnych modyfikacji
* Raczej chcemy ograniczyć znajdowane przekształcenia, który trzymają się takiego wycinka przestrzeni jak w zbiorze treningowym (przykład z czasem pracy)
	* optymalizacja z ograniczeniami
