# Przeszukiwanie iteracyjne z ograniczeniami (2024-12-04)

Przy systematycznym przeszukiwaniu (np. A* i problem plecakowy) to jasne jak to robić
redukuje się drzewo przeszukiwań

## Optymalizacja z ograniczeniami
* Funkcja celu $q: F \rightarrow R$
* Zbiór dopuszczalny $F \subseteq X$
	* podzbiór przestrzeni przeszukiwań
* Każdy punkt dopuszczalny spełnia ograniczenia $g_j(x) \le 0$

### Optymalizacja ciągła z ograniczeniami
* Funkcja celu
* Zbiór dopuszczalny
* Metryka
* Norma euklidesowa
* Każdy punkt dopuszczalny spełnia
	* ograniczenia kostkowe $l_i \le x_i \le u_i$ - zbiór rozwiązań dopuszczalnych to hiperprostopadłościan
	* ograniczenia funkcyjne $g_j(x) \le 0, h_j(x) = 0$

## Skąd się biorą ograniczenia
* Fizyka
	* temperatura nie może być poniżej zera absolutnego
	* twarde ograniczenia
* Ograniczenia miękkie
	* budżet który można troche przekroczyć
	* są wynikiem kompromisu między wieloma kryteriami optymalizacji

Optymalizacja wielokryterialna
* rozwiazania alternatywnie
* nie można jednoznacznie rozstrzygnąć które rozwiązanie jest lepsze
	* kryteria nie są porównywalne ze sobą

## Po wprowadzeniu przestrzeni przeszukiwań
* Ograniczenia zawężają przestrzeń przeszukiwań
* Po usunięciu krawędzi pojawiają się nowe minima lokalne
	* zadanie z jednym optimum może zamienić się w zadanie z wieloma optimami
* Przestrzeń przeszukiwań może przestać być spójna
	* nie do każdego punktu można dojść przez ciąg operacji na sąsiadach
* Anizotropowość zbioru dopuszczalnego
	* liczebność sąsiedztwa jest różna

## Kłopoty z ograniczeniami
* Jak rozpocząć przeszukiwanie
* Jak zapewnić dopuszczalność kolejno generowanych punktów
* Jak umożliwić przegląd całego zbioru dopuszczalnego
* Funkcja celu może dawać niewłaściwe sygnały
	* prowadzić do gorszego optimum lokalnego
	* prowadzić do sztucznego optimum lokalnego wynikającego z rozcięcia zbioru przeszukiwań
* Wynik mutacji może nie być symetryczny względem kierunków
	* obciążenie w stronę środka zbioru dopuszczalnego
	* ucieczka od ograniczeń
* Przeszukiwanie wyczerpujące - im więcej ograniczeń tym lepiej
	* A*
	* tym mniej musimy przeglądać
* Algorytmy iteracyjne
	* chcemy dostosować problem do standardowego schematu dla tych algorytmów
	* różowe okulary, metoda przeszukiwania jest nieświadoma

## Sposoby uwzględniania ograniczeń

|                                    | Zmiana przestrzeni przeszukiwań                  | Zmiana funkcji celu                      |
| ---------------------------------- | ------------------------------------------------ | ---------------------------------------- |
| Redefinicja zadania przeszukiwania | modyfikacja reprezentacji rozwiązań lub wariacji | funkcja kary                             |
| Wykorzystanie procedur naprawczych | naprawa rozwiązań widoczna dla metody            | naprawa rozwiązań niewidoczna dla metody |

* Dookreślenie funkcji celu poza zbiorem dopuszczalnym
	* ma informować algorytm czy idzie w dobrą stronę
* Sprawienie żeby nie było możliwości wygenerowania rozwiązań niedopuszczalnych

Np. do problemu gwiazdki na kolokwium
Są różne sposoby numerowania krawędzi, przyjmujemy arbitralny
Jest jakiś sposób numerowania, który charakteryzuje się tym że pierwsze x to rozwiązanie problemu
Możemy przeszukiwać przestrzeń permutacji krawędzi
Problem z ograniczeniami w przestrzeni wektorów binarnych zamieniamy na problem bez ograniczeń w przestrzeni permutacji krawędzi
Redefinicję problemu raczej znacznie ciężej wymyślić

Procedury naprawcze
Pomiędzy metodą a ewaluatorem jest naprawiacz


## Funkcja kary
* $q'(x) = q(x) + p(x)$
	* nie jest uniwersalne
* $p(x) = (g(x))^2$
	* kwadrat - pochodna zerowa w 0 i jest różniczkowalny jeśli g jest różniczkowalne
	* po zsumowaniu mogą być dodatkowe minima lokalne
* Można wprowadzić nieciągłość
	* skrajnie - kara równa nieskończoność (kara śmierci)
* substytutywna funkcja kary
	* poza zbiorem dopuszczalnym $q'(x) = p(x)$ - uniwersalne
	* $p(x) = Q + (g(x))^2$
	* Q to wartość maksymalna ze zbioru dopuszczalnego


## Narpawa rozwiązań

### Niewidoczna dla metody
* naprawa pomiędzy logiem a ewaluatorem
* ewaluowane jest dopiero to co wyszło z naprawy
* ale naprawiona informacja nie wraca do loga

### Przykłady naprawy
* Rzutowanie
	* kierunek od punktu naprawianego do środka zbioru
	* wyznaczany punkt przecięcia z granicą zbioru
	* czasami niejednoznaczne
	* skomplikowane
	* rozkład ciągły i na granicy delta diraca
	* poza zbiorem dopuszczalnym nie ma sygnału w którą stronę iść - błądzenie przypadkowe
* Rzutowanie prostopadłe
	* przy ograniczeniach kostkowych
	* uwzględnienie każdego ograniczenia
	* proste
* Odbijanie
	* odbicie względem przekroczonej krawędzi zbioru (kostkowego)
	* można powtarzać do skutku jeśli po pierwszym rzutowaniu wyleci z drugiej strony
	* bardziej podobny kształt rozkładu do teego sprzed naprawy
* Zawijanie
	* donut
* Reinicjacja
	* zpominamy o punkcie który wyleciał
	* zastępujemy punktem z pierwotnego rozkładu (np rozkład jednostajny w kostce)
	* nie ma związku między naprawianym punktem a naprawionym
	* histogram podniesiony
* Powtórna generacja
	* jak wygenerowany losowo sąsiad jest niedopuszczalny
	* losujemy znowu do wyczerpania cierpliwości
	* niesymetrycznie obcięty rozkład
	* funkcja celu już nie jest funkcją, tylko zmienną losową

## Naprawa rozwiązań widoczna dla metody
* Naprawa przed logiem
* Inne zachowanie algorytmu optymalizacyjnego
* Zmienia się sąsiedztwo
* Zmienia się rozkład próbkowania generowania sąsiadów
* Pojawia się obciążenie