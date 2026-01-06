# Modele analityczne

## Model
Model matematyczny jest odzwierciedleniem fragmentu rzeczywistości w formie zależności matematycznych (algebraicznych)

* Model abstrakcyjny i model danych
* Model powinien być ogólny, a szczególna sytuacja jest opisywana przez dane
* Model podlega walidacji - jak udowodnić poprawność

## Model rzeczowy
* $y = f(x,p)$
    * $x \in X$ - wektor zmiennych decyzyjnych
    * $p \in P$ - wektor parametrów
    * $y \in Y$ - wektor zmiennych wyjściowych
    * $X$ - zbiór decyzji dopuszczalnych
    * $Y$ - zbiór ograniczeń na zmienne wyjściowe
    * $P$ - zbiór ograniczeń na parametry

## Zadania analizy modelu
* Symulacja
* Symulacja odwrotna
* Optymalizacja jednokryterialna
* Analiza wielokryterialna

### Symulacja
* Na etapie weryfikacji modelu
* Podajemy przykładowe wejście i parametry
* Patrzymy, czy wyjścia mają sens

### Symulacja odwrotna
* Jakie powinny być zmienne decyzyjne, żeby uzyskać określone wyjście
* Zadanie optymalizacji 
* $\min_{x \in X} |y - \hat{y}| + \rho |x - \hat{x}|$
	* $\rho$ - czynnik regularyzacji

### Optymalizacja
* Minimalizacja funkcji kosztu, określonego wyjścia
* Dotyczy jednego wyjścia
* $\min_{x \in X} q_i$

### Analiza wielokryterialna
* Często konfliktowe cele (np. cena vs jakość)
* $\min_{x \in X} \bf{q}$ 
* Nie jest dobrze zdefiniowanym matematycznie zadaniem (nie jest optymalizacją w ścisłym sensie)

## Klasyfikacja modeli
* Statyczne
	* liniowe - jeśli się da, to najlepiej budować model liniowy, stosować aproksymacje, są łatwiejsze obliczeniowo, bardzo wydajne solvery
	* dyskretne
	* nieliniowe
* Dynamiczne
* Stochastyczne
* Inne (np. oparte o zbiory rozmyte)

## Zadanie liniowe
* $\min_{x \in X} c^Tx$ - minimalizacja kosztu
* $Ax \le b, x \ge 0$ - opis ograniczeń na $x$

### Poziomica funkcji
Zbiór punktów dziedziny funkcji rzeczywistej wielu zmiennych, dla których przyjmuje ona tę samą wartość

### Rough set
Do wygooglowania

## Operations research vs optimization
* Badania operacyjne  - zorientowane na zastosowania w przemyśle i usługach
* Optymalizacja - bardziej ogólny kontekst

## Modele w systemach zarządzania
Model musi być włączony w proces biznesowe, chyba że dotyczy jednorazowanego planowania lub analizy strategicznej.

* Modele planowania i realizacji produkcji i usług
	* planowanie (lokalizacja i dystrybucja)
	* zadania operacyjne (problem pakowania)
* Harmonogramowanie i szeregowanie zadań
* Modele dystrybucji (operacyjne)
	* najkrótsza ścieżka
	* sieci przepływowe
	* zadanie transportowe

## Narzędznia do modelowania i rozwiązywania zadań optymalizacji
* Narzędzia do modelowania
	* AMPL
	* AIMMS
	* GAMS
	* GNU MathProg
	* Pyomo (python)
* Solwery optymalizacyjne
	* MINOS
	* CPLEX
	* GUROBI
	* GLPK

## Model
* Model abstrakcyjny
	* zbiory, indeksy, parametry, zmienne decyzyjne
	* jest sparametryzowany
	* symbole, pod które zostaną podstawione wartości (dane)
* Instancja modelu
	* model abstrakcyjny o konkretnych wartościach parametrów
	* załadowany danymi

