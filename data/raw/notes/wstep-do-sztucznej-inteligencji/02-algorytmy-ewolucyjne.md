# Algorytmy ewolucyjne

## Problem optymalizacji
* Optymalizacja - poszukiwanie najlepszego rozwiązania
* W praktyce często nie szuka się najlepszego możliwego rozwiązania tylko wystarczająco dobrego, lepszego niż to które mamy
* Jeśli nie znamy żadnego rozwiązania to może wystarczyć nawet rozwiązanie akceptowalne (spełniającce zadane ograniczenia)
* W uczeniu maszynowym wykorzystuje się metody optymalizacji (w siaciach neuronowych, SVM)
* W przypadku czasochłonnych modeli używa się aproksymatów

### Pojęcia
* Przestrzeń przeszukiwań
    * zbiór wartości $U$
    * metryka
* Zazwyczaj dokonuje się optymalizacji z ograniczeniami - pracujemy na podzbiorze zbioru wartości $D \subseteq U$
* Dana jest funkcja celu $q(x): D \rightarrow \mathbb{R}$
* Minimalizacja polega na szukaniu minimum globalnego
* Minimum lokalne - w sąsiedztwie nie ma lepszego
	* Funkcja o jednym optimum - unimodalna
	* Funkcja o wielu optimach - wielomodalna
* Ograniczenia kostkowe - istnieją wektory $l$ i $u$ takie że dla każdego $x$: $l_i \le x_i \le u_i$

### Rodzaje metod optymalizacji
* Lokalne - zatrzymują się na pierwszym napotkanym ekstremum lokalnym, szybkie
* Globalne - szukają ekstremum globalnego, są wolne i często nie dają gwarancji znalezienia rozwiązania

### Ograniczenia
* Twarde - nieprzekraczalne ze względu np na ograniczenia fizyczne, nie mogą być złamane
* Miękkie - mogą być chwilowo naruszane ale wynik musi je spełniać (często są praktyczne)

### Radzenie sobie z ograniczeniami
* Utrzymywanie dopuszczalności rozwiązań - tak generować dane żeby je spełniały
* Naprawa rozwiązań - np. rzutowanie, clamping
* Stosowanie funkcji kary $q_p(x) = q(x) + p(x)$, powinna być proporcjonalna do skali przekroczenia ograniczeń

### Rodzaje zadań optymalizacji
* Zadania ciągłe - $x_i \in \mathbb{R}$
* Zadania dyskretne - wartości $x_i$ należą do zbioru dyskretnego, problemy kombinatoryczne
	* Zadania kombinatoryczne - $x_i \in \{0, 1\}$

### Kodowanie rozwiązania
* Kodowanie binarne
* Wyliczeniowe (enum)
* Wektory liczb rzeczywistych
* Kodowanie specyficzne dla problemu (np. specjalne dla grafów)

### Punkt startowy
* Od czegoś trzeba zacząć
* Rozwiązanie losowe - może być trudne do wygenerowania przy skomplikowanych ograniczeniach
* Rozwiązanie wyznaczone dzięki wiedzy dziedzinowej
	* może przyspieszyć optymalizację
	* może być konieczny dla trudnych, wielowymiarowych problemów
	* może uwięzić optymalizator w ekstremum lokalnym

Funkcja Galara - ciekawy, typowy przypadek - trzeba znać na egzamin!!!

## Algorytmy ewolucyjne
* Inspirowane ewolucją naturalną przez działanie i nazewnictwo
* Początkowo wykorzystywały kodowanie binarne - algorytmy genetyczne
* To metody optymalizacji globalnej
	* nie ma gwarancji, że znajdą optimum globalne
	* do optymalizacji lokalnej są lepsze algorytmy

### Nazewnictwo
* Osobnik - reprezentuje punkt w przeszukiwanej przestrzeni, może zawierać dodatkowe informacje
* Populacja - zbiór osobników
* Mutacja - losowe zaburzenie zmiennych $x_i$ osobnika (genów)
* Krzyżowanie - nowy osobnik powstaje na podstawie genów istniejących osobników
* Chromosom - wszystkie geny, osobnik najczęsciej ma jeden chromosom

## Algorytm genetyczny
Osobniki kodowane binarnie

```python
def genetic_algorithm(
	fitness_function,
	population,
	population_size,
	mutation_probability,
	crossover_probability,
	max_iterations
):
	iteration = 0
	fitness = calc_fitness(population, fitness_function)
	best, best_fitness = find_best(population, fitness)
	
	while iteration < max_iterations:
		r = reproduction(population, fitness, population_size)
		m = mutation_and_crossover(r, mutation_probability, crossover_probability)
		
		fitness = calc_fitness(m, fitness_function)
		iter_best, iter_best_fitness = find_best(m, fitness_function)
		
		if iter_best_fitness < best_fitness:
			best_fitness = iter_best_fitness
			best = iter_best
			
		population = m
		t += 1
	return best, best_fitness
```

* Reprodukcja - losowy wybór punktów z populacji, lepszych z większym prawdopodobieństwem
* Krzyżowanie - wygenerowanie punktu pośredni pomiędzy rodzicami
	* dla każdej pary, jeśli $\mathcal{U} (0, 1) < p_m$ to wykonuje się krzyżowanie
	* w przeciwnym wypadku rodzice przechodzą bez zmian do następnej populacji
	* nie powinno niszczyć nauczonych schematów
* Mutacja - ma za zadanie wygenerować punkt z otoczenia punktu mutowanego
	* negacja bitów dla których $\mathcal{U} (0, 1) < p_m$ 
* Sukcesja - wybór populacji do następnej iteracji algorytmu
	* sukcesja generacyjna - następna populacja to populacja mutantów


### Klasyczny algorytm genetyczny
* Reprodukcja proporcjonalna (ruletkowa)
* Krzyżowanie jednopunktowe
* Sukcesja generacyjna
* Parametry
	* Duży rozmiar populacji - większy niż wymiarowość rozwiązania
	* Duże prawdopodobieństwo krzyżowania
	* Małe prawdopodobieństwo mutacji
	* To generalnie daje dobre wyniki ale można ustawić lepiej


### Reprodukcja proporcjonalna (ruletkowa)
Prawdopodobieństwo wyboru osobnika jest proporcjonalne do jego oceny - większy kawałek koła ruletki.

$$
p_s(P(t, j)) = \frac{q(P(t,j))}{\sum_k(q(P(t,k)))}
$$

### Krzyżowanie

#### Krzyżowanie jednopunktowe
* Losowanie 2 rodziców
* Losowany punkt przecięcia $i$ rodzica
* Z 2 rodziców powstaje 2 potomków przez zamianę części chromosomów
* Nie wszystkie kombinacje genów są osiągalne
#### Krzyżowanie dwupunktowe
* Losowanie 2 rodziców
* Losowanie 2 punktów przecięcia $i$ i $j$
* Zamienia się między chromosomami geny od $i$ do $j$
	* jeśli $j < i$ to idzie się od i do końca, a potem od początku do j
* Jest raczej lepsze od jednopunktowego

#### Krzyżowanie równomierne (jednorodne)
* Dla każdego genu losuje się od którego rodzica będzie pochodzić
* Kiedyś było uważane za złe ze względu na teorię schematów, teraz uważane za dobre

### Kodowanie rozwiązania
Można stosować oddzielne kodowanie  genotypu (to co jest poddawane mutacjom) i fenotypu (właściwych cech). Trzeba to przemyśleć tak, żeby mutacja zgodnie z założeniem dawała w rezultacie punkt zbliżony do pierwotnego


### Zalety i wady algorytmów genetycznych
* Bogata literatura
* Wiele dostępnych implementacji
* Wiele parametrów do konfiguracji
* Wiele komponentów do konkretyzacji (który rodzaj krzyżowania itd.)
* Można użyć nowszych wersji algorytmów genetycznych jeśli problem jest naturalnie binarnie zakodowany


## Algorytm ewolucyjny
```python
def evolutionary_algorithm(
	fitness_function,
	population,
	population_size,
	mutation_strength,
	crossover_probability,
	max_iterations
):
	iteration = 0
	fitness = calc_fitness(population, fitness_function)
	best, best_fitness = find_best(population, fitness)

	while not stop_condition(iteration, max_iterations, population, fitness):
		post_reproduction = reproduction(population, fitness, population_size)
		post_mutation = genetic_operations(
			post_reproduction, mutation_strength, crossover_probability
		)
		
		iter_fitness = calc_fitness(post_mutation, fitness_function)
		iter_best, iter_best_fitness = find_best(post_mutation, iter_fitness)

		if iter_best_fitness < best_fitness:
			best_fitness = iter_best_fitness
			best = iter_best

		population = succession(population, post_mutation, fitness, iter_fitness)
		iteration += 1
		
```

* Pracuje na liczbach rzeczywistych - gen to liczba rzeczywista
* Można stosować bardziej skomplikowane kryterium stopu 
	* np. od n pokoleń populacja nieznacznie się zmieniła
	* to nie jest takie łatwe bo mogą wystąpić okresy stagnacji
* Reprodukcja
	* wybiera lepsze punkty z populacji z większym prawdopodobieństwem niż słabsze
* Mutacja
	* każdy osobnik jest poddawany mutacji, parametrem jest siła mutacji $\sigma$
	* generuje punkt z otoczenia punktu mutowanego
* Krzyżowanie ma dawać rozwiązanie pośrednie między rodzicami
	* należy stosować tylko jeśli to ma sens
	* może być lepiej w ogóle nie używać jeśli nie pasuje do problemu
* Sukcesja
	* które osobniki przetrwają do następnej iteracji
	* są różne warianty

### Rozmiar populacji
* Uważa się, że im więcej tym lepiej ale wtedy są droższe obliczenia
* Małe populacje też mogą być dobre, bo słabsze osobniki mają mniejszą konkurencję a mogą zmutować w lepsze
* Klątwa wymiarowości - liczba obserwacji potrzebnych do dobrego próbkowania rośnie wykładniczo z liczbą wymiarów

### Inicjalizacja
* Ma wpływ na zdolność algorytmu do znalezienia rozwiązania i na jego szybkość
* Część populacji może prowadzić do dobrych rozwiązań a część utykać na optimach lokalnych
* Jeśli populacja jest mało różnorodna to przeszukiwanie będzie bardziej lokalne - lepsza eksploatacja (raczej nieporządane)
* Różnorodność populacji początkowej daje lepsze zdolności eksploracji - porządane
* Różnorodność populacji zmniejsza się w miarę optymalizacji

### Reprodukcja
* Proporcjonalna (ruletkowa)
* Rangowa - populację sortuje się po ocenie, pozycja osobnika po posortowaniu to jego ranga, wybór zależy od tej rangi

#### Reprodukcja progowa
* Osobniki poniżej progu są wyrzucane
* Pozostałe mają jednakową szansę na wybór

#### Reprodukcja turniejowa
* Losowanie grupy (np. 2) osobników z powtórzeniami
	* najsłabszy osobnik ma niezerową szansę na zostanie wybranym - jeśli rywalizuje sam ze sobą
	* lepsza eksploracja - być może warto go oszczędzić
* Najlepszy przechodzi dalej
* Powtarzane tyle razy ile ma być osobników
* Dobrze się sprawdza w praktyce, 
	* dobre zdolności eksploracyjne
	* łatwa w implementacji

### Mutacja
* Punkt po mutacji powinien pochodzić z otoczenia bieżącego punktu
* Stosuje się rozkład normalny - bliżej położone punkty bardziej prawdopodobne od dalej położonych

$$x = x + \sigma \cdot \mathcal{N}(0, 1)$$

### Krzyżowanie
Nie w każdym problemie ma to sens - osobnik potomny powinien być punktem pośrednim między rodzicami (bierze od obu tylko te dobre cechy)

#### Krzyżowanie wymieniające
* Przepisujemy część z jednego a część z drugiego rodzica
* Krzyżowanie równomierne
	* określamy prawdopodobieństwo i dla każdego genu losujemy czy przepisujemy gen z pierwszego czy drugiego rodzica
* Krzyżowanie jednopunktowe
	* losujemy punkt przecięcia chromosomu

#### Krzyżowanie uśredniające
* Uśrednia się cechy od obu rodziców
* Suma ważona z losową wagą
* Suma ważona z losowym wektorem wag

Zrozumieć na egzamin, niekoniecznie całą kategoryzację na pamięć

### Sukcesja
#### Sukcesja generacyjna
Następna populacja to populacja mutantów $P_{t+1} = M$

#### Sukcesja elitarna
* Wybór spośród
	* $k$ najlepszych osobników z poprzedniej populacji (elitę)
	* mutantów
	* bez $k$ najgorszych z połączonego zbioru
* Mniejsza szansa że zgubi najlepszego osobnika
* Dobre są małe wartości $k$ (np. 1)
* Jeśli elita jest za duża to algorytm osiada w optimach lokalnych

### Eksploracja vs eksploatacja
* Eksploraja - znajdowanie innych niż bieżące ekstrema lokalne (przeszukiwanie całej przestrzeni)
* Eksploatacja - zdolność do jak najdokładniejszego lokalizowania ekstremum (przeszukiwanie otoczenia domniemanego optimum)
* Te cele są ze sobą sprzeczne, w algorytmie musi być dobry balans
* Nacisk selektywny - zdolność poprawiania średniej oceny osobników w populacji
	* duży nacisk selektywny to lepsza eksploatacja i gorsza eksploracja
* Dąży się do kompromisu między eksploracją i eksploatacją

### Kształtowanie kompromisu
* Reprodukcja
* Sukcesja
	* generacyjna - lepsza eksploracja
	* elitarna z dużym k - lepsza eksploatacja
* Krzyżowanie
	* lepsza eksploatacja
	* szybka poprawa jakości osobników nie musi być dobra - algorytm mógł się skupić na jednym optimum lokalnym
* Mutacja
	* słaba mutacja - lepsza eksploatacja
	* silna mutacja - lepsza eksploracja

### Wady klasycznego algorytmu ewolucyjnego
* Dużo parametrów do konfigurowania
* Dużo algorytmów od wyboru na poszczególnych krokach (sukcesja, krzyżowanie, mutacja itd)

### Podsumowanie
* Są stosowane tylko w niektórych obszarach
* Atrakcyjna metafora
* Łatwość implementacji
* Dobre wyniki (nawet przy kiepskich implementacjach)


## Strategie ewolucyjne

### Strategia (1+1)
* Mamy punkt roboczy
* Losujemy punkt w jego sąsiedztwie
* Jeśli niegorszy to zastępuje aktualny punkt roboczy
* Populacja z jednym osobnikiem i jednym potomkiem
* Mechanizm adaptacji siły mutacji

```python
def strategy_one_plus_one(
	fitness_function,
	point,
	mutation_strength,
	adaptation_interval,
	max_iterations
):
	iteration = 1
	successes = 0
	best_fitness = fitness_function(point)
	
	while iteration <= max_iterations:
		new_point = point + mutation_strength * normal(0,1)
		new_fitness = fitness_function(new_point)
		
	if new_fitness <= best_fitness:
		successes += 1
		best_fitness = new_fitness
		point = new_point

	if iteration % adaptaion_interval == 0:  # adapt mutation_strength
		if successes / adaptation_interval > 1/5:
			mutation_strength *= 1.22
		if successes / adaptation_interval < 1/5:
			mutation_strength *= 0.82
		successes = 0
	
	iteration += 1
	return point, best_fitness
```

* Reguła 1/5 sukcesu powstała z analizy funkcji kwadratowych, parametry liczbowe dobrano eksperymentalnie
	* Ważny na egzamin (zapamiętać 1/5)
* Dużo sukcesów (ok 1/2) będzie kiedy punkt jest daleko od optimum - trzeba zwiększyć siłę mutacji
* Jeśli punkt jest blisko optimum to większa część wylosowanych punktów będzie słabsza - zmniejszamy siłę mutacji
* Strategia ma słabą odporność na minima lokalne

### Strategia $(\mu + \lambda)$
* $\mu$ - rozmiar bazowej populacji
* $\lambda$ - rozmiar populacji potomnej
* $\lambda > \mu$
* Osobnik zawiera 2 chromosomy
	* pierwszy zawiera właściwe geny
	* drugi zaweira wartości $\sigma$ używane do mutacji
* Reprodukcja - losowanie z powtórzeniami $\lambda$ osobników z populacji
* Krzyżowanie
	* najczęściej krzyżowanie przez uśrednianie z losową wagą
* Mutacja na 3 etapy
	* $a = \mathcal{N}(0, 1)$, $b_i = \mathcal{N}(0,1)$ dla każdego genu osobnika
	* $\sigma_i = \sigma_i exp(\tau' a + \tau b_i)$ 
		* $\tau = 1/\sqrt{2n}$
		* $\tau' = 1/\sqrt{2\sqrt{n}}$
	* $m_i = k_i + \sigma_i \mathcal{N}(0,1)$
		* $m$ to zmutowany osobnik
		* $k$ to osobnik po krzyżowaniu
* Sukcesja - $\mu$ najlepszych osobników z sumy populacji bazowej i mutantów
	* strategia elitarna - nie gubi najlepszych osobników
* Dobry osobnik o zbyt małym lub zbyt dużym zasięgu mutacji blokuje miejsce i ściąga do ekstremów lokalnych

### Strategia $(\mu, \lambda)$
* Cała populacja rodziców ginie, nowa populacja potomna powstaje tylko na podstawie $\lambda$ osobników potomnych
* Strategia nieelitarna, może zgubić najlepszego osobnika
* Większe zdolności eksploracyjne

### Cechy strategii ewolucyjnych
* Reprodukcja czysto losowa - bez nacisku selektywnego (nie bierze się pod uwagę ocen)
* Sukcesja deterministyczna z naciskiem selektywnym
* Najłatwiej zwiększyć szansę znalezienia optimum globalnego uruchamiając algorytm wielokrotnie z losowymi punktami startowymi

## Przykładowe pytania
* Rozumieć wymienione algorytmy (znać pseudokody)
* Czym się różnią genetyczne, ewolucyjne, strategie ewolucyjne
* Różnica między 1+1, $\mu+ \lambda$, $\mu, \lambda$

### Jaki wpływ na działanie algorytmu ma zasięg mutacji
* Mały zasięg - algorytm może dojść do najbliższego optimum lokalnego
* Średni zasięg - algorytm znajdzie optimum loklane ale ze względu na siłę mutacji może odkryć też inne, nie utknie w pierwszym napotkanym
* Duży zasięg - działanie jak metody Monte Carlo

### Co by było jakbyśmy chcieli prawdopodobieństwo sukcesu w ES(1+1) stabilizować na $0.5$
* Sukces jest wtedy, kiedy nowy punkt jest lepszy od poprzedniego
* Średnio $0.5$ sukcesów będzie jeśli punkt jest daleko od optimum
* Zasięg mutacji będzie ciągle zmniejszany i algorytm utknie w miejscu

### Jaki wpływ na działanie algorytmu ma zwiększanie rozmiaru elity w sukcesji elitarnej
* Większa elita - większa zdolność do eksploatacji
* Większa elita - mniejsza szansa na przeżycie słabego osobnika
	* słaby osobnik mógłby zmutować i przejść do innego optimum lokalnego
### Jaki wpływ na działanie algorytmu ma zwiększenie rozmiaru populacji?
* Większa populacja - mniej iteracji przy stałym budżecie - słabsza ewolucja
* Dobrą strategią jest malejący rozmiar populacji w miarę liczby iteracji

