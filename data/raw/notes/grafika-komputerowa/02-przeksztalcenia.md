# Przekształcenia
* Obiekty znajdują się w przestrzeni i w niej się przemieszczają
* Reprezentacja punktu w przestrzeni $(x,y,z)$
	* wymaga zdefiniowania układu współrzędnych
## Wektory
* Reprezentacja
	* ruchu, siły
	* przemieszczenia
* Operacje
	* dodawanie
	* odejmowania
	* skalowanie
	* normalizacja
	* iloczyny

### Iloczyn skalarny
* Kąt między wektorami
* $v \cdot w = \|v\| \|w\| \cos(\theta)$

### Iloczyn wektorowy
* Wynikowy wektor jest prostopadły do dwóch wykorzystanych
* Wyznaczanie wektora normalnego
* $\|v \times w \| = \|v\| \|w\| \sin(\theta)$

### Wektor normalny
* Wektor prostopadły do powierzchni
* Zwykle długość wektora to 1
* Może być zdefiniowany jako wynik iloczynu wektorowego dwóch wektorów stycznych do powierzchni
* Reprezentuje orientację

## System współrzędnych
* Definiuje początek przestrzeni
* 3 niezależne liniowo wektory
	* osie x, y, z
* Czasem łatwiej definiować rzeczy w lokalnych układach współrzędnych
* Ręczność
	* lewoskrętny
	* prawoskrętny

### Przestrzeń świata
* Punkt $(0,0,0)$
* Wektory
	* $(1,0,0)$
	* $(0,1,0)$
	* $(0,0,1)$
* Wszystko inne definiowane w relacji do tego systemu

## Transformacje
* Mapowanie punktów na inne punkty i wektorów na inne wektory
	* $p' = T(p)$
	* $v'=T(v)$
* Liniowe
	* $T(sv) = sT(v)$
	* $T(v_1+v_2) = T(v_1) + T(v_2)$
* Ciągłe
	* sąsiedztwo $p$ lub $v$ przekształcane jest na sąsiedztwo $p'$ lub $v'$
* Jeden do jednego i odwracalne
	* $p = T^{-1}(T(p))$

### Transformacje afiniczne
* Transformacje liniowe + translacja
	* identyczność
	* translacja
	* rotacja
	* skalowanie
	* pochylenie

### Współrzędne jednorodne
* Reprezentacja $N$ wymiarowej przestrzeni rzutowej za pomocą układu $N+1$ współrzędnych
* $(x, y, z, w) = (x/w, y/w, z/w)$
* Upraszcza przekształcenia - translację też można zapisać jako mnożenie macierzy

### Identyczność
Przekształcenie dające ten sam obiekt

$$I = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}$$

### Skalowanie
* Proporcjonalna zmiana długości elementu
* Skalowanie może przemieszczać obiekt
* Jeśli obiekt nie zaczyna się w punkcie $(0,0,0)$ obiekt trzeba przesunąć do 0, przeskalować i przesunąć z powrotem
* Kąty nie są zachowane jeśli skalowanie nie jest jednorodne
	* kiedy skala jest różna w różnych osiach
	* $S_x \ne S_y$

$$S = \begin{bmatrix}
S_x & 0 & 0 & 0 \\
0 & S_y & 0 & 0 \\
0 & 0 & S_z & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}$$

$$S \cdot \begin{bmatrix}x \\ y \\ z \\ 1\end{bmatrix} = \begin{bmatrix}S_xx \\ S_yy \\ S_zz\\ 1\end{bmatrix}$$

### Rotacja
* Każda rotacja może być przedstawiona jako kompozycja 3 rotacji nałożonych przeciwnie do ruchu wskazówek zegara
	* kąty Eulera
* Oddzielne macierze dla każdej osi
* Zachowuje kąty pomiędzy poszczególnymi częściami obiektu
* Obiekt zmienia położenie jeśli punkt obrotu jest inny niż 0
	* można przesunąć do 0, obrócić i cofnąć
* Pivot - punkt wokół którego robimy obrót

$$
R_x(\theta) = \begin{bmatrix}
1 & 0 & 0 & 0 \\
0 & \cos \theta & -\sin \theta & 0 \\
0 & \sin \theta & \cos \theta & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
\quad
R_y(\theta) = \begin{bmatrix}
\cos\theta & 0 & \sin\theta & 0 \\
0 & 1 & 0 & 0 \\
-\sin\theta & 0 & \cos\theta & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
\quad
R_z(\theta) = \begin{bmatrix}
\cos\theta & -\sin\theta & 0 & 0 \\
\sin\theta & \cos\theta & 0 & 0 \\
0 & 0 & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}
$$

### Pochylenie / ścinanie
* ang. shear
* Powoduje skośny kształt obiektów w którymś z wymiarów
* Przydatne do augmentacji danych

$$Sh = \begin{bmatrix}
1 & sh_x^y & sh_x^z & 0 \\
sh_y^x & 1 & sh_y^z & 0 \\
sh_z^x & sh_z^y & 1 & 0 \\
0 & 0 & 0 & 1 \\
\end{bmatrix}$$

### Translacja
* Przesunięcie punktu o wektor

$$T(\Delta x, \Delta y, \Delta z) = \begin{bmatrix}
1 & 0 & 0 & \Delta x \\
0 & 1 & 0 & \Delta y \\
0 & 0 & 1 & \Delta z \\
0 & 0 & 0 & 1 \\
\end{bmatrix}$$

## Składanie przekształceń
* Mnożenie macierzy przez siebie
* Przed wykonywaniem obliczeń lepiej utworzyć pojedynczą macierz
	* zwykle poddajemy temu samemu zestawowi transformacji więcej niż jeden punkt
* Kolejność ma znaczenie
	* mnożenie macierzy od prawej do lewej
