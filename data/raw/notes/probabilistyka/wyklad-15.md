# Regresja i testowanie hipotez (2024-01-22)

Najlepsza funkcja regresji (minimalizująca $E(Y-f(X))^2$)
$$f(x) = E(Y|X=x)$$

## Model regresji liniowej
$$Y = aX + b + \epsilon$$
$$a = \frac{cov(X,Y)}{VX}$$
$$b = EY - a \cdot EX$$

W praktyce wyznacza się oszacowania (estymatory) parametrów $a$ i $b$

$$
\hat{a} = \frac{\sum_{i=1}^n (x_i-\bar{x})(y_i-\bar{y})}{\sum_{i=1}^n \ldots}
$$
$$\hat{b} = \ldots$$
### Dowód
Szukamy parametrów $a$ i $b$ dla których $h(a,b) = E(Y-(aX+b))^2$ ma najmniejszą wartość

$$
h(a,b) = E(Y-(aX+b))^2 
= E(Y^2 + a^2X^2 + b^2 - 2aXY - 2bY +2abX)
$$

$$h(a,b) = EY^2 + a^2 \cdot EX^2 + b^2 - 2a \cdot EXY - 2b \cdot EY + 2ab \cdot EX$$

Szukamy $a$ i $b$, dla których $h$ osiąga minimum

$$\frac{\partial h}{\partial a} = 2a \cdot EX^2 - 2 \cdot EXY + 2b \cdot EX$$
$$\frac{\partial h}{\partial b} = 2b - 2 \cdot EY + 2a \cdot EX$$
$$\frac{\partial h}{\partial b} = 0 \implies b = EY - a \cdot EX$$
$$2aEX^2 - 2EXY + 2EX \cdot EY - 2a \cdot (EX)^2 = 0$$
$$\implies a(EX^2 - (EX)^2) = E(XY) - EX \cdot EY$$
$$\implies aVX = cov(X,Y)$$ $$\implies a = \frac{cov(X,Y)}{VX}$$

$$\frac{\partial^2 h}{\partial a^2} = 2EX^2$$
$$\frac{\partial^2 h}{\partial b^2} = 2$$
$$
\frac{\partial^2 h}{\partial a \partial b} 
= \frac{\partial^2 h}{\partial b \partial a} 
= 2x
$$

$$detM = 4EX^2 - 4(EX)^2 = 4VX > 0$$
$$\implies (a,b) = (\frac{cov(X,Y)}{VX}, EY-aEX) = argmin h(a,b)$$

## Testowanie hipotez

### Rozkład $\chi^2$
Niech $X_1, X_2, \ldots, X_n$ będą niezależnymi zmiennymi losowymi o identycznych rozkładach $N(0,1)$. Wtedy zmienna losowa $X = \sum_{i=1}^n X_i^2$ ma rozkład $\chi^2$ z $n \in \mathbb{N}$ stopniami swobody.

Gęstość: $\ldots$

Funkcja $\Gamma$: $\ldots$ 

### Rozkład t-Studenta
Niech $X_0, X_1, X_2, \ldots, X_n$ będą niezależnymi zmiennymi losowymi o identycznych rozkładach $N(0,1)$. Wtedy zmienna losowa $T = \frac{X_0}{...}$ 
...

### Hipoteza statystyczna
Każde przypuszczenie dotyczące nieznanego rozkładu badanej cechy populacji, o prawdziwości lub fałszywości którego decyduje się na podstawie wylosowanej próby.

Zawsze należy sformułować dwie hipotezy
* $H_0$ - hipoteza zerowa - hipoteza, którą podaje się w wątpliwość
	* np. $H_0: \theta = \theta_0$
* $H_1$ - hipoteza alternatywna - hipoteza, którą jesteśmy skłonni przyjąć, jeśli odrzucimy hipotezę zerową
	* $H_1: \theta \ne \theta_0$ - test dwustronny
	* $H_1: \theta > \theta_0$ - test jednostronny (prawostronny)
	* $H_1: \theta < \theta_0$ - test jednostronny (lewostronny)

Testowanie hipotezy to podjęcie jednej z 2 decyzji
* Odrzucenie hipotezy $H_0$ na korzyść $H_1$
* Nie ma podstaw do odrzucenia $H_0$ (nie można powiedzieć że jest prawdziwa)

### Błędy przy testowaniu hipotez
* Błąd $I$ rodzaju - odrzucić hipotezę $H_0$, gdy jest ona prawdziwa
* Błąd $II$ rodzaju - nie odrzucić hipotezy $H_0$, gdy prawdziwa jest $H_1$

### Poziom istotności testu
Oznaczany $\alpha$ - prawdopodobieństwo błądu $I$ rodzaju (zazwyczaj przyjmowane $0.05$)

### p-wartość testu
Najmniejszy poziom istotności, przy którym zostaje odrzucona $H_0$

## Klasyczna metoda weryfikacji hipotez statystycznych
* Sformułowanie hipotez
* Przyjęcie poziomu istotności testu
* Przyjęcie odpowiedniej statystyki testowej i obliczenie jej wartości dla wylosowanej próby
* Wyznaczenie zbioru krytycznego testu
* Podjęcie decyzji

Niech $t$ to wartośc statystyki testowej, a $C$ zbiorem krytycznym
* $t \in C$ - odrzucamy $H_0$ na korzyść $H_1$
* $t \notin C$ - nie odrzucamy $H_0$

### Przykład
Czas rozwiązywania zadania jest zmienną losową o rozkładzie normalnym. Studenci rozwiązują zadanie w czasie średnio: $17, 8.5, 20, 10.5, 11, 15.5$. Wg. wykładowcy średni czas powinien wynosić $12$ minut. Sprawdzić na poziomie istotności $0.05$ czy to za mało czasu jeśli
1. $\sigma = 5$ jest znane
2. $\sigma$ nie jest znane

(najpierw należałoby przetestować hipotezę, że rozkład jest normalny)

#### 1
$\sigma = 5$
$H_0: m=12$
$H_1 : m > 12$
oznaczenie $m_0 = 12$

Niech statystyka testowa $Z = \frac{\bar{X} - m_0}{\sigma}\sqrt{n} \sim |_{H_0} N(0,1)$ (przy założeniu prawdziwości $H_0$)
Jeśli $X_i$ mają rozkład normalny z parametrami $N(m, \sigma^2)$, to $\bar{X} \sim N(m, \frac{\sigma^2}{n})$ (centralne twierdzenie graniczne)

$z_{1-\alpha}$ - kwantyl rzędu $\alpha$
pole gęstości standardowego rozkładu normalnego na lewo to $1-\alpha$, a na prawo $\alpha$

Przedział krytyczny to $C = [z_{1-\alpha}, +\infty)$ (bo hipoteza to $m>12$)

$z = \frac{13.75 - 12}{5} \sqrt{6} \simeq 0.8573$ 
$z_{0.95} \simeq 1.645$
$z \notin C$ - nie ma podstaw do odrzucenia $H_0$ - nieprawda, że powinno być więcej niż $12$ minut

## Alternatywna metoda testowania hipotez
* Sformułowanie hipotez
* PRzyjęcie poziomu istotności
* Przyjęcie odpowiedniej statystyki testowej i obliczenie jej wartości dla wylosowanej próby
* Wyznaczenie p-wartości testu
* Podjęcie decyzji
	* $p \le \alpha$ - odrzucamy hipotezę $H_0$ na korzyść $H_1$
	* $p > \alpha$ to nie ma podstaw do odrzucenia $H_0$

Dla testu lewostronnego $p = P(T \le t)$
Dla testu prawostronnego $p = P(T \ge t)$
Dla testu dwustronnego $p = 2 \cdot min(P(T \le t), P(T \ge t))$

Do testowania czy zmienna ma rozkład normalny służy metoda shapiro
