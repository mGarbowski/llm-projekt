# Analiza korelacji
Badanie istnienia liniowego związku między cechami populacji (zmiennymi losowymi)

Korelacja dodatnia - wzrostowi wartości jednej cechy towarzyszy wzrost wartości drugiej cechy
Korelacja ujemna - wzrostowi wartości jednej cechy towarzyszy spadek wartości drugiej cechy
Korelacja zerowa - brak korelacji, cechy są nieskorelowane

Rodzaje korelacji
* .
	* Cecha X ma wpływ na cechę Y
	* Cecha Y wpływa na X
	* Obie cechy wpływają na siebie
* Istnieje cecha, która wpływa jednocześnie na X i Y
* Występowanie korelacji jest przypadkowe (korelacja pozorna / fałszywa)


## Wartość oczekiwana
Niech $g: \mathbb{R}^2 \rightarrow \mathbb{R}$ i  $g(X,Y)$ będzie zmienną losową jendowymiarową

$$
E(g(X,Y)) = \sum_{(x,y)\in S_{XY}} g(x,y) \cdot P(X=x, Y=y)
$$

$$
EX = \sum_{(x,y) \in S_{XY}} x \cdot P(X=x,Y=y)
$$

$$
EY = \sum_{(x,y) \in S_{XY}} y \cdot P(X=x,Y=y)
$$

$$
E(XY) = \sum_{(x,y) \in S_{XY}} xy \cdot P(X=x,Y=y)
$$


$$
E(g(X,Y)) = \int\int_{\mathbb{R}^2} g(x,y)f_{XY}(x,y)dxdy
$$


## Przykład 2
Wektor $(X,Y)$ ma rozkład jednostajny w prostokącie $D=[0,6] \times [0,2]$. Wyznaczyć $EX$, $EY$, $E(XY)$

$$
(X,Y) \sim U([0,6] \times [0,2]) \implies X \sim U([0,6]), Y \sim U([0,2])
$$
$EX = 3$
$EY = 1$

$$
f_{XY}(x,y) = \frac{1}{12} \mathbb{1}_D(x,y)
$$

$$
E(XY) = \int\int_D xy f_{XY}(x,y)dxdy = \int_0^6[\int_0^2 \frac{1}{12} xy dy]dx
= \ldots = 3
$$

Jak zmienne są niezależne to $E(XY) = EX \cdot EY$, w ogólnym przypadku tak nie jest, implikacja nie działa w drugą stronę

Punkt $(EX, EY)$ jest środkiem ciężkości obszaru $D$ (czyli nośnika tego rozkładu) - zawsze

## Przykład 3.
$D$ - trójkąt o wierzchołkach $(0,0)$, $(0,1)$, $(1,0)$
$f_{XY}(x,y) = 2 \cdot \mathbb{1}_D(x,y)$

środek ciężkości będzie na wysokości opuszczonej na przeciwprostokątną - $(1/3, 1/3)$
$EX = EY = 1/3$
$$
E(XY) = \int \int_D xy \cdot 2 dxdy
= \int_0^1 [ \int_0^{1-x} 2xy \cdot dy]dx
= \int_0^1x\cdot [y^2]_0^{1-x} dx
= \int_0^1x\cdot(1-x)^2dx
= \frac{1}{12}
\ne EX \cdot EY
$$

## Kowariancja
Kowariancja zmiennych losowych $X$ i $Y$ dla których istnieją $EX$, $EY$, $E(XY)$ to liczba

$$
cov(X,Y) = E[(X-EX)(Y-EY)]
$$

$$
cov(X,Y) = E(XY) - EX \cdot EY
$$


* kowariancja dodatnia - oba nawiasy dodatnie - jak X rośnie to Y rośnie
	* albo oba nawiasy ujemne - jak X maleje to Y maleje


* Dpdatnia korelacja między cechami $X$, i $Y$ $cov(X,Y) > 0, \rho(X,Y) > 0$
* Ujemna korelacja między cechami  $X$, i $Y$ $cov(X,Y) < 0, \rho(X,Y) < 0$
* Cechy $X$ i $Y$ nieskorelowane: $cov(X,Y) = 0, \rho(X,Y) = 0$

### Własności
* $cov(X,Y) = cov(Y,X)$
* $cov(X,X) = VX$
* $cov(a,X) = 0$ dla $a \in \mathbb{R}$
* $cov(aX + b, cY + d) = ac\cdot cov(X,Y)$
* $cov(aX_1 + bX_2, cY_1 + dY_2) = \ldots$


## Współczynnik korelacji
$\rho$ to współczynnik korelacji - mówi jak silna jest ta korelacja

Niech $VX, VY > 0$

$$
\rho(X,Y) = \frac{cov(X,Y)}{\sqrt{VX \cdot VY}}
$$


### Dla próby
Kiedy nie znamy rozkładu dla całej popoulacji

$$
cov(X,Y) = \frac{1}{n-1} \cdot \sum_{k=1}^n (x_k - \bar{x}) (y_k - \bar{y})
$$

Współczynnik korelacji (współczynnik korelacji próbkowej Pearsona)

$$
r(X,Y) = \frac
{\cdot \sum_{k=1}^n (x_k - \bar{x}) (y_k - \bar{y})}
{\sum_{k=1}^n (x_k - \bar{x})^2 \cdot \sum_{k=1}^n (y_k - \bar{y})^2}
$$

### Własności
* $-1 \le \rho \le 1$
* $|\rho(X,Y)| = 1 \iff$ istnieją takie $a,b \in \mathbb{R}$, że $Y = aX + b$ (leżą na prostej)
* $X$ i $Y$ są nieskorelowane $\iff \rho(X,Y) = 0$

### Orientacyjne przedziały
* $|\rho| < 0.25$ - korelacja bardzo słaba (pomijalna)
* $0.25 \le |\rho| \lt 0.5$ - korelacja słaba
* $0.5 \le |\rho| \lt 0.75$ - korelacja umiarkowana
* $0.75 \le |\rho| \lt 1$ - korelacja silna
* $|\rho| = 1$ - korelacja pełna


Jeśli zmienne losowe X i Y są niezależne to cov(X,Y) = 0.
Ale z tego że X i Y są nieskorelowane nie wynika że są niezależne (może być inna nieliniowa zależność)

W rozkładzie normalnym X i Y są niezależne $\iff cov(X,Y) = 0$


### Wyprowadzenie wzoru

$$
cov(X,Y) = E[(X-EX)(YY-EY)]
= E[XY - XEY - YEX + EX \cdot EY]
= E(XY) - E(X\cdot EY) - E(Y \cdot EX) + E(EX \cdot EY)
= E(XY) - EY \cdot EX - EX \cdot EY + EX \cdot EY
= E(XY) - EX \cdot EY
$$

$$
V(X+Y) = VX + 2cov(X,Y) + VY
$$
$$
V(X-Y) = VX - 2cov(X,Y) + VY
$$

