# Gry dwuosobowe
Zajmujemy się grami
* w postaci ekstensywnej
* o sumie stałej (zerowej)
* sprawiedliwymi
* dwuosobowymi
* o skończonym czasie rozgrywki

Poszukiwanie strategii w takiej grze to problem przeszukiwania przestrzeni

## Podział gier

### Ze względu na kolejność podejmowania decyzji
* gry w postaci strategicznej (normalnej) - gracze podejmują decyzje jednocześnie, bez wiedzy o decyzjach innych uczestników
* gry w postaci ekstensywnej (rozwiniętej) - graczej podejmują decyzje sekwencyjnie, mając określone informacje o decyzjach

### Gry o sumie zerowej 
Zysk gracza oznacza stratę jego oponenta, interesy graczy są dokładnie przeciwstawne
* deterministyczne / hazardowe
* informacja pełna (warcaby) / informacja niepełna (statki)

## Deterministyczna gra dwuosobowa
* dwaj przeciwnicy, Min i Max
* wykonują ruchy naprzemiennie
* nie ma czynników losowych
* stan gry jest znany obu przeciwnikom
* koniec gry ma przypisany wynik - liczba rzeczywista nazywana wypłatą
* cel gry
	* dla gracza rozpoczynającego Max - maksymalizacja wypłaty
	* dla gracza Min - minimalizacja wypłaty

### Model
$$\langle S, P, s_0, T, w \rangle$$
* $s \in S$ - stan i informacja kto wykonuje ruch (np. ustawienie figur na szachownicy)
* $p \in P$ - funkcja następnika, reprezentuje ruchy (posunięcia w grze) $p: S \rightarrow S$ lista stanów spełniających reguły gry
* $s_0 \in S$ - stan początkowy
* $T \subset S$ - zbiór stanów terminalnych (np. mat w szachach)
* $w$ - funkcja wypłaty zdefiniowana dla stanów terminalnych
	* np 1: wygrana Max, 0: remis, -1: wygrana Min

Do wyznaczania następnego ruchu można użyć drzewa gry (właściwie to grafu acyklicznego) zbudowanego na podstawie modelu. Optymalne strategie można wyszukać w tym grafie

Sprawiedliwa gra - każdy z graczy *może* wygrać

### Przegląd wyczerpujący
Przez rekurencyjne przeglądanie drzewa reprezentowanego w pamięci można oetykietować pozostałe węzły (początkowo znane są tylko etykiety stanów terminalnych)
* dla gracza Max - maksymalna wypłata z następników
* dla gracza Min - minimalna wypłata z następników


* Znajduje optymalną strategię, gdy przeciwnik gra optymalnie
* Złożoność czasowa $O(b^N)$
	* $b$ - maksymalne rozgałęzienie drzewa
	* $N$ - maksymalna wysokość drzewa
* Wysokość drzewa nie przekracza $2N$
* Dla gry w szachy nie da się znaleźć rozwiązania przez pełne przeszukiwanie bo $b\simeq 35$, $N \simeq100$
	* drzewo nie zmieści się w żadnej pamięci

## Algorytm MiniMax
* Nie reprezentuje pełnego drzewa gry, niezależnie analizuje stany potomne
* Przegląda poddrzewo w głąb do określonej głębokośći (np. tylko 10 ruchów do przodu), pozwala analizować ścieżki o ograniczonej długości
* Oszczędza czas
* Wymaga funkcji oceny stanu $h(s)$
	* $w(s)$ dla stanów terminalnych
	* heurystyka dla stanów nieterminalnych

```python
def minimax(state, depth, is_max_move):
	if state.is_terminal() or depth == 0:
		return h(state)
	
	values = [
		minimax(next_state, depth-1, not is_max_move)
		for next_state in state.next()
	]
	
	if is_max_move:
		return max(values)
	else:
		return min(values)
	
```

## Algorytm MiniMax z przycinaniem $\alpha - \beta$
* Jeżeli analizowana ścieżka ma wybór gorszy niż obecnie najlepszy dla innej ścieżki, to nie ma sensu jej analizować (wiadomo że oponent na pewno nie wybierze tej ścieżki jeśli gra optymalnie)
* Taka strategia pozwala wyeliminować średnio połowę ścieżek przy przeszukiwaniu
* $\alpha$ - najlepszy obecnie wybór dla Max
* $\beta$ - najlepszy obecnie wybór dla Min

```python
def minimax_ab(state, depth, is_max_move, alfa=float('-inf'), beta=float('inf')):
	if state.is_terminal() or depth == 0:
		return h(state)
		
	if is_move_max:
		for s in state.next():
			alfa = max(alfa, minmax_ab(s, depth-1, not is_max_move, alfa, beta))
			if alfa >= beta:
				return alfa
		return alfa
	else:
		for s in state.next():
			beta = min(beta, minmax_ab(s, depth-1, not is_max_move, alfa, beta))
			if alfa >= beta:
				return beta
		return beta
```

## Algorytmy wspomagające
* Iteracyjne pogłębianie (jeżeli mamy czas to można uruchomić algorytm jezcze raz z większym $d$)
* Heurystyki określające kolejność analizy ruchu (przeglądać bardziej sensowne wcześniej)
* Heurystyki określające dokładność oszacowania wartości stanu
* Książka otwarć i zamknięć

Struktury danych do reprezentacji gry często stosują wzorzec projektowy VirtualProxy - leniwe tworzenie


## Algorytm uśredniony MiniMax (Expected MiniMax)
* Do gier niedeterministycznych z pełną informacją
* Drzewo ma węzły losowe
* Wypłata dla węzłów losowych uwzględnia prawdopodobieństwo

Do drzewa wprowadza się dodatkowe pośrednie poziomy reprezentujące wybory losowe
$w(n) = \sum P(s) \cdot w(s)$ - ważone względem prawdopodobieństwa (wartość oczekiwana wypłaty)

## Gry z niepełną informacją
Można zastosować expected minimax oddzielnie dla każdego rozdania - kiepsko się sprawdzają

