 # Sieci Bayesa

* Graficzny model probabilistyczny reprezentujący realcje między zmiennymi losowymi
* Zwięzła reprezentacja prawdopodobieństwa łącznego
* Dobre do reprezentacji wiedzy w systemach eksperckich
* Graf acykliczny
	* wierzchołki odpowiadają dyskretnym zmiennym losowym
	* krawędzie reprezentują bezpośrednie zależności między zmiennymi
	* każda zmienna ma rozkład prawdopodobieństwa (warunkowy jeśli są wchodzące krawędzie)

## Założenie Markowa
Zakłada się, że wszystkie bezpośrednie zależności są przedstawione przez krawędzie w sieci


## Warunkowa niezależność
### Łańcuch
Dla sieci w postaci łańcucha A -> B -> C

* Są 2 zależności bezpośrednie
* Jeśli wartość B jest ustalona, to obserwacja A nie wnosi żadnych nowych informacji o C
* Przy ustalonym B, C jest warunkowo niezależne od A

### Wspólna przyczyna
Dla sieci z B->A, B->C

* Jak w łańcuchu, prz ustalonym B, A nie dostarcza nowych informacji o C
* C jest warunkowo niezależne od A przy ustalonym B
* $P(C|A\wedge B) = P(C|B)$

### Wspólny efekt
Dla sieci z A->B, C->B

* Zdarzenie ma 2 przyczyny
* A i C są niezależne, ale stają sie zależne po aobserwowaniu B

## d-separacja
* Pozwala rozszerzyć pojęcie warunkowej niezależności na zbiory zmiennych (węzły w sieci)
* $A \perp C|B$ - znajomość $B$ blokuje przepływ informacji między $C$ i $A$
* Przy wspólnym efekcie - znajomość $B$ odblokowuje przepływ informacji między $C$ i $A$
* Ścieżka pomiędzy zbiorami wierzchołków $X$ i $Y$ - dowolna ścieżka (ignorując kierunki) ścieżka w grafie sieci łącząca wierzchołek z $X$ z wierzchołkiem z $Y$
* Ścieżka między $X$ i $Y$ jest zablokowana przez zbiór $E$ jeśli istnieje taki wierzchołek $Z$, że
	* $Z \in E$ i $Z$ jest fragmentem łańcucha w ścieżce $(\ldots \rightarrow Z \rightarrow \ldots)$
	* $Z \in E$ i jest wspólną przyczyną dla dwóch sąsiadujących w ścieżce węzłów $(\ldots \leftarrow Z \rightarrow \ldots)$
	* $Z$ ani potomkowie nie należą do $E$, $Z$ występuje jako wspólny efekt w ścieżce $(\ldots \rightarrow Z \leftarrow \ldots)$
* Zbiór $E$ d-separuje zbiory $X$ i $Y$ jeśli każda ścieżka między tymi zbiorami jest blokowana przez $E$
	* $X$ i $Y$ są warunkowo niezależne po zaobserwowaniu $E$


## Warunkowa niezależność
* Otoczka Markova (Markov blanket) węzła X to zestaw tych węzłów, których wartość trzeba ustalić, żeby X był warunkowo niezależny od reszty sieci
* Otoczka składa się z rodziców, dzieci i rodziców tych dzieci węzła X

## Próbkowanie z użyciem otoczki Markowa

Dla każdej możliwej wawrtości $x$ zmiennej losowej $X$
$$
P(X=x | OM(X)) = \alpha P(X=x | Rodzice(X)) \prod_{Z_i \in Dzieci(X)}P(Z_i=z_i | Rodzice(Z_i))
$$

* $\alpha$ - współczynnik normalizujący (prawdopodobieństwa sumują się do $1$), można zaimplementować algorytm bez tego skalowania

## Wnioskowanie przy pomocy MCMC
Mamy graf z węzłem R o rodzicach Q i S
* Dowody: obserwuje my $R=T$
* Pytanie: jaki jest rozkład $S$

### Działanie
* Inicjowanie wartości w wierzchołkach grafu - tym co jets w zbiorze dowodów lub wartością losową jeśli nie ma
* Zlicza się wystąpienia stanów dla zmiennej z zapytania z losowych próbek
	* Losuje się węzył nie będący dowodem
	* Wylosowanie wartości korzystając z otoczki Markowa
	* Aktualizuje się licznik
* Otrzymuje się rozkład zmiennej na podstawie liczników
	* normalizacja, żeby prawdopodobieństwa sumowały się do $1$

Stan początkowy może nie mieć logicznego sensu ale w miarę kolejnych iteracji przybliża się prawdziwy rozkład


## Dokładne wnioskowanie
Tylko dla prostych struktur(?)

Przekonanie odnośnie stanu $Y$
$$
Bel(Y) = P(Y|X=x)
$$

Sieć dwuelementowa - proste użycie twierdzenie Bayesa

Łańcuch - wnioskowanie bezpośrednio z tabel rozkładów albo z twierdzenia Bayesa dla wnioskowania w odwrotnej kolejności

W ogólnym przypadku - problem NP-trydny

Drzewa i lasy - algorytm propagacji przekonań

W praktyce dla większych sieci stosuje się algorytmy przybliżone (np. MCMC)

## Estymacja parametrów sieci
* znamy strukturę grafu (sieci Bayesa)
* nie znamy prawdopodobieństw
* mamy zbiór danych z pomiarami wszystkich zmiennych
* chcemy oszacować prawdopodobieństwa na podstawie danynch
	* tak dopasowujemy parametry, żeby sieć mogła wygenerować to co zaobserwowaliśmy

## Metoda Największej Wiarygodności
Szukamy takich parametrów rozkładu, dla których zbiór danych wydaje się najbardziej wiarygodny

Zakładamy że zbiór składa się z niezależnych próbek - liczymy iloczyn
Obliczanie iloczynu jest problematyczne (błędy numeryczne), można sumować logarytmy

Można stosować MNW do każdego modelu którego wyjście można interpretować jako prawdopodobieństwa

## Szersza perspektywa na wnioskowanie Bayesowskie
Na podstawie zaobserwowanych danych aktualizujemy model rzeczywistości proporcjonalnie do
* wstępnych założeń odnośnie postaci modelu $P(\theta)$
* dopasowania danych (obserwacji) do tego modelu $P(X|\theta)$

## Maximum a posteriori (MAP)
MNW + wiedza pierwotna
$$
\hat{\theta} = argmax_\theta P(X|\theta)P(\theta)
$$

Rozkłady beta - do określania pewności w pierwotny model, bardzo elastyczny