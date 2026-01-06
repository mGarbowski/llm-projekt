# Uczenie ze wzmocnieniem
Reinforcement learning (RL)

* Uczenie się celowego zachowania na podstawie interakcji ze środowiskiem na podstawie prób i błędów
* Cel ucznia (agenta) - długoterminowa maksymalizacja nagród
* Działania ucznia (akcje) podlegają ocenie, źródło oceny lepiej nazwać krytykiem niż nauczycielem (bo nie ma dokładnej wiedzy)
* Ocena nazywana jest wzmocnieniem (termin z badań nad uczeniem się zwierząt) - jeżeli pewna akcja prowadzi do lepszego stanu to prawdopodobieństwa wybrania tej akcji będzie wzmacniane

## Uczeń i środowisko
* Stan początkowy
* Wzmocnienie początkowe
* Uczeń generuje akcję na podstawie aktualnego stanu
* Środowisko przyjmuje akcję i coś z nią zrobi (wykona albo nie wykona)
* Środowisko przekazuje uczniowi nowy stan i nowe wzmocnienie
* W praktyce nagroda (wzmocnienie) najczęściej jest równa $0$, nie w każdej iteracji
* Zwykle zakłada się nieznajomość i niepewność środowiska
* Te same akcje mogą powodować przejście do różnych stanów
* Stan absorbujący kończy epizod algorytmu
* Uczeń maksymalizuje funkcję oceny, która opiera się na otrzymanych wzmocnieniach

### Zadanie ucznia
* Ma nauczyć się takiej strategii wybierania akcji, która długofalowo maksymalizuje nagrody
* Powinien uwzględniać wcześniej odwiedzone stany jeśli doprowadziły do dobrego rezultatu
* Zwykle maksymalizuje się zdyskontowaną sumę nagród
	* współczynnik dyskontowania reguluje jak ważne są względem siebie krótko i długoterminowe wzmocnienia
	* $\mathbb{E}[\sum_{t=0}^\infty \gamma^t \cdot r_t]$
	* $\gamma \in [0,1]$

## Zadania epizodyczne
* Zwykle interakcje ucznia ze środowiskiem są podzielone na serie prób - epizody
* Dla interesujących zdarzeń można zdefiniować stan absorbujący, który kończy epizod
* Stan absorbujący może być związany z sukcesem lub porażką
* Każdy epizod zaczyna się od chwili $t=0$ ale wiedza ucznia przechodzi do kolejnych epizodów
* Zwykle nie wiemy ile kroków zajmie epizod

## Model Markowa
Model matematyczny dla RL to model Markowa

$$
\langle X, A, \rho, \sigma \rangle
$$
* $X$ - skończony zbiór stanów
* $A$ - skończony zbiór akcji
* $\rho(x,a)$ - funkcja wzmocnienia (zmienna losowa)
* $\sigma(x,a)$ - funkcja przejść stanów (zmienna losowa) 

* W każdym kroku nagroda i stan zależą tylko od stanu aktualnego
* Strategia definiuje zasady zgodnie z którymi wybierane są akcje czyli to funkcja $\pi: X \rightarrow A$
	* posługiwanie się strategią $\pi$ oznacza zawsze wykonywanie akcji $a_t = \pi(x_t)$
* Do oceny strategii służy funkcja wartości
	* $V^{\pi}(x) = \mathbb{E}_\pi [\sum_{t=0}^\infty \gamma^t r_t | x_0 = x]$
* Można oceniać pary stan-akcja
	* $Q^\pi(x, a) = \mathbb{E}_\pi [\rho(x,a) + \sum_{t=0}^\infty \gamma^t r_t | x_0 = x, a_0 = a]$
	* $V^\pi(x) = Q^\pi(x, \pi(x))$

### Ocena strategii
* Strategia jest lepsza jeśli nie jest gorsza i istnieje stan dla którego jest lepsza
* Jeśli nie istnieje lepsza strategia to strategia jest optymalna
	* optymalność zależy od współczynnik dyskontowania $\gamma$
* Strategia zachłanna
	* w każdym stanie wybiera akcję, która daje największą ocenę $Q(x,a)$

## Metody różnic czasowych
* W każdym kroku generujemy prognozę na podstawie dostępnej informacji
* Zakładamy że kolejne prognozy są coraz lepsze
* W kroku $t$
	* $a_t \leftarrow \pi(x_t)$
	* $r_t, x_{t+1} \leftarrow$ wykonaj $a_t$
	* $\Delta = r_t + \gamma V_t(x_{t+1}) - V_t(x_t)$
	* $V_{t+1} \leftarrow V_t + \beta \Delta$


## Algorytm AHC
Adaptive Heuristic Critic

```python
def ahc(t_max, gamma, beta_v, beta_p):
	t = 0
	V, state = initialize()
	preference = initialize()
	while t <= t_max:
		reward, next_state = make_action(preference(state))
		delta = reward + gamma * V[next_state] - V[state]
		V[state] += beta_v * delta
		preference[state, action] += beta_p * delta
		
		state = next_state
		t += 1
```

* Parametr $\beta$ - szybkość uczenia
* Już się nie stosuje w praktyce, są lepsze

## Q-learning
* Często stosowany w praktyce
* Korzysta z funkcji $Q$ ocena pary stan akcja (tabela dwuwymiarowa)
* W każdym kroku każda akcja musi mieć szansę być wybrana - na potrzeby eksploracji
* Współczynnik kroku beta (learning rate)
	* dla 0 agent się nie uczy tylko wykorzystuje już zdobytą wiedzę
	* dla 1 agent patrzy tylko na najnowsze informacje i zpaomina stare
	* 1 jest akceptowalne tylko dla środowisk deterministycznych
* Współczynnik dyskontowania gamma
	* dla 0 agent patrzy tylko na nagrody, nie uwzględnia zdobytej wiedzy
	* dla bliskich 1 agent dąży do długoterminowego maksymalizowania nagród

```python
def q_learning(t_max, gamma, beta):
	t = 0
	state, Q = initialize()
	while t <= t_max:
		action = choose_action(state, Q)
		reward, next_state = make_action(action)
		delta = reward + gamma * max(Q[next_state]) - Q[state, action]
		Q[state, action] += beta * delta
		
		state = next_state
		t += 1
```

### Wybór akcji
* Strategia $\epsilon$-zachłanna
	* z prawdopodobieństwem $\epsilon$ wybierana losowa akcja
	* z prawdopodobieństwem $1-\epsilon$ wybierana zachłanna akcja na podstawie Q
	* $\epsilon$ może maleć w czasie - wtedy na początku będzie więcej eksploracji a potem eksploatacji
* Wybór oparty na rozkładzie Boltzmanna
* Strategie licznikowe
	* ile razy akcja była wykonana
	* ile kroków minęło od jej ostatniego wykonania
	* modyfikowanie na podstawie liczników poprzednich strategii


## Eksploracja vs eksploatacja
* Zachłanne wybieranie akcji uniemożliwia przeszukanie całej przestrzeni
* Całkowicie losowe wybieranie akcji nie korzysta ze zgromadzonej wiedzy
	* w nietrywialnych środowiskach można nie dojść do stanu akceptującego w rozsądnym czasie

Zapamiętać na egzamin jak się oblicza wyceny

## Algorytm SARSA
State Action Reward State Action

```python
def sarsa(t_max, gamma, beta):
	t = 0
	state, Q = initialize()
	action = choose_action(state, Q)
	while t <= t_max:
		reward, next_state = make_action(action)
		next_action = choose_action(next_state, Q)
		delta = reward + gamma * Q[next_state, next_action] - Q[state, action]
		Q[state, action] += beta * delta
		
		state = next_state
		t += 1

```

* Akcja jest wybierana i wykonywana, nie jest wybierana maksymalna dla następnego kroku 
* Ta sama akcja do poruszania się i wyliczania delty

## SARSA vs Q-Learning
* Q-Learning szybciej znajduje optymalną drogą
* SARSA wybiera bardziej ostrożne strategie
	* lepszy jeśli pomyłki są kosztowne
* Jeśli $\epsilon$ dąży do $0$ to oba nauczą się tej samej ścieżki

Na egzamin
* obliczenia
* różnice i podobieństwa między algorytmami (Q-Learning vs SARSA, Q-Learning vs AHC)
* nie będzie liczenia równań Bellmana


## Programowanie dynamiczne
* Dla procesu Markowa istnieje strategia optymalna, trzeba mieć pełną wiedzę o procesie decyzyjnym żeby ją znaleźć - nie opłaca się stosować np Q-Learning
* Nie każdy problem da się rozwiązać programowaniem dynamicznym, musi dzielić się na etapy (podproblemy) i tą wiedzę da się wykorzystać do rozwiązania większego problemu
* Problem dyliżansu
* Opiera się na równaniach Bellmana

## RL vs programowanie dynamiczne
### Programowanie dynamiczne
* Wyznacza strategię optymalną
* Wymaga znajomości wartości oczekiwanych nagród i prawdopodobieństw przejść
* Duża złożoność obliczeniowa

### RL
* Nabycie umiejętności działania, może nie być optymalne
* Może nie rozważać całej przestrzeni
* Nie wymaga pełnej znajomości, odpytuje się środowisko
* Środowisko może się powoli zmieniać w czasie (zmieniać swoje parametry, Q-Learning będzie się douczał)