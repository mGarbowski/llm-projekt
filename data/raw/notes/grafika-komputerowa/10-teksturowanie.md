# Teksturowanie
* Proces który na wejściu otrzymuje powierzchnię i dokonuje modyfikacji jej wyglądu
	* obraz
	* funkcja
	* inne źródło danych

## Potok teksturowania
* Lokalizacja obiektu w przestrzeni $(x,y,z)$
	* tekstura jest powiązana z obiektem
* Projekcja w celu otrzymania współrzędnych tekstury
	* współrzędne $(u,v)$
	* wierzchołek w modelu typowo będzie miał powiązane współrzędne uv
* Funkcja korespondencji
	* przejście od uv do przestrzeni tekstury
* Pobranie wartości z tekstury
* Przekształcona wartość tekstury
* Przekształcenie odczytanych wartości
* Modyfikacja właściwości powierzchni
	* np. diffuse - kolor
	* równie dobrze można modyfikować inne właściwości, np. wektory normalne

## Współrzędne tekstur
* Pierwszym krokiem jest pobranie współrzędnych obiektu i przekształcenie ich na współrzędne tekstur $(u,v)$
* Dla części obiektów mamy z automatu
	* kule, cylindry
* Typowo trzeba to jednak zrobić ręcznie
	* np. twarz się rozpłaszcza do prostokąta
	* problem jak rozciąć model to wypłaszczenia
* Często na jednej teksturze umieszcza się wiele obiektów
	* dla optymalizacji
* Projekcja siatki

## Corresponder function
* Przekształcenie współrzędnych tekstury do przestrzeni tekstury
* Wybranie części obrazu
* Przekształcenie macierzowe współrzędnych
* Wyjście poza granice tekstury
	* powielenie
	* odbicie
	* clamping

## Obrazy a teksturowanie
* Teksel - elementarny fragment tekstury
* Teksturę może stanowić dowolna mapa bitowa
* W typowym przypadku obiekt jest za mały lub za duży względem tekstury, potrzeba jakiegoś odwzorowania

### Magnifikacja
* Rozdzielczość tekstury jest mniejsza niż rozdzielczość ekranu
* Filtrowanie
	* najbliższy sąsiad
	* dwuliniowe - interpolacja

#### Interpolacja dwuliniowa
* Znajdź 4 sąsiadujące teksele
* Wykonaj interpolację liniową w dwóch wymiarach

### Minifikacja
* Rozdzielczość tekstury jest większa od rozdzielczości ekranu
* Jednemu pikselowi może odpowiadać wiele tekseli
* Rozwiązania
	* filtrowanie - ale jest aliasing
	* wykorzystanie mipmap

#### Mipmapping
* Wstępne obliczanie tekstur o zmniejszonej rozdzielczości
* Każdy kolejny poziom 2 razy mniejszy
	* można uśredniać
	* można wybrać maximum itp.
* Zajętość pamięci jest rzędu 133% - nie tak duży narzut
* Parametr $d$
	* texture level detail
	* poziom mapy właściwy do wykorzystania
	* można powiązać z LOD, a można obliczać w locie
* Teksturę można odczytywać w sposób dyskretny (współrzędne) lub ciągły - wartość z $[0,1]$

## Tekstury objętościowe
* Rzadko stosowane
* Współrzędne $(u,v,w)$
* Interpolacja trójliniowa
* Proceduralne
	* definicja RGB w każdym punkcie przestrzeni 3D
* Wokselowe
	* kolor w każdym wokselu
* Można zapisać jako kostkę albo jako tablicę tekstur 2D

## Proceduralne generowanie tekstur
* Zamiast odczytywania wartości z obrazu można generować w locie
* Wykorzystuje się szumy, np. szum Perlina
* Wykorzystanie tekstury komórkowej
* Symulacje fizyczne

### Szum Perlina
* W każdym punkcie węzłowym $v_i$ o wartości całkowitej
	* funkcja równa $0$
	* funkcja ma gradient $g_i$
* Dla każdego węzła $v_i$ w którym gradient jest równy $g_i$ można stworzyć funkcję
	* $y_i(x) = g_i(x-v_i)$
* W przedziale $v_i \le x \le v_{i+1}$ można interpolować kolejnymi funkcjami liniowymi $y_i, y_{i+1}$ korzystając z funkcji $a(t)$
	* $f(x) = y_i(x)(1-a(t)) + y_{i+1}(x)a(t)$
	* $a(t) = x - floor(x)$
* Jest dobra biblioteka do Pythona
* Jak szum się dobrze pokoloruje to wychodzą ładne tekstury

## Mapowanie alfa
* Wykorzystanie dodatkowego kanału tekstury
* Efekty
	* pominięcie niechcianych wartości tekstury
	* można zdefiniować maskę
	* przypisuje się wartość 0 do tekseli
* Rendering roślin
	* najprostsze - dwa prostokątny skrzyżowane ze sobą z odpowiednią teksturą

## Bump mapping
* Symulacja nierówności powierzchni
* Zmienia się wektory normalne do wyznaczania oświetlenia
	* podmiana wartością wczytaną z tekstury
	* wykorzystanie pola wysokości
	* mapa normalnych
* Nie modyfikuje samej geometrii
* Wady
	* Krawędzie obiektu nie ulegają zmianie (dalej są gładkie)

## Parallax mapping
* Problemy z bump mapping
	* perturbacje nie przemieszczają się z widokiem
	* perturbacje nie blokują się nawzajem
* Perturbacje są przechowywane w teksturze wysokości
* W czasie oglądania powierzchni
	* pobiera się wartość z tekstury wysokości
	* wykorzystuje się tą wysokość do przesunięcia współrzędnych tekstury

## Displacement mapping
* Zmienia powierzchnię obiektu
* Przesuwanie punktów nad powierzchnię wzdłuż normalnych o wartość określoną w teksturze
