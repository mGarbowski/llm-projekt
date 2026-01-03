# Sieci ze zbieżnym stanem
* Sieć o charakterze pamięciowym
	* podajemy wzorce
	* sieć ustala wagi
	* podajemy kolejną uszkodzoną próbkę
	* sieć odtwarza tą próbkę
* Raczej zagadnienie historyczne

## Ogólna koncepcja
* Inspiracja biologią
	* naturalne neurony mrugają do siebie
	* informacja w cyrkulacji elektrycznej
	* ludzka pamięć - stan jest jakoś przechowywany
* Koncepcja sztucznej sieci
	* podajemy wektor wejściowy
	* wagi pozwalają powrócić do oryginalnego stanu przez przemnożenie

## Sieć Hopfielda
* Jedna warstwa neuronów
* Wejścia mnożone przez wagi
* Wyjścia są zapętlone z powrotem na wejście
	* na wejście neuronu trafiają wyjścia wszystkich innych neuronów (poza nim samym - $w_{ii}=0$)
	* wagi są symetryczne $w_{ij} = w_{ji}$
* Szukamy stanu, gdzie sieć się ustabilizuje
* W trybie odtwarzania wagi są zamrożone
	* podaje się wejście i wielokrotnie zapętla sygnał wyjściowy (sprzężenie zwrotne)
	* aż do ustabilizowania się odpowiedzi sieci (wyjść)
* W trakcie uczenia są aktualizowane
* Uczenie
	* metoda Hebba - $w_{k,j} = \frac{1}{n} \sum_{k=1}^M s_k^is_j^i$ (mnożenie wektorów)
	* metoda pseudoinwersji - wyprowadzenie ze wzoru macierzowego

### Nowoczesna sieć Hopfielda
* Pamięć asocjacyjna
* Opis problemu
	* dany jest zestaw wektorów binarnych $Z \subset \{-1, 1 \}^n$
	* uczymy sieć na tym zbiorze $Z$
	* dla danego wektora $v \in \{-1, 1\}^n$ sieć znajduje wektor w $Z$ najbliższy do $v$
* Połączenie między wszystkimi neuronami
	* asynchroniczna aktualizacja
	* tylko jeden neuron jest aktualizowany w danym momencie
	* niejednoznaczność, wynik zależy od kolejności
	* można np. narzucić zawsze tą samą kolejność
* Sieć ma $n$ neuronów ze stanem
	* stan początkowy - wektor wejściowy
	* stan końcowy - wektor wyjściowy
	* połączone każdy z każdym (graf pełny)
* Autoasocjacja - wyjście odtwarza wejście
* Działanie
	* $w_{i,j}$ - waga połączenia $i \rightarrow j$
	* symetryczne
	* waga do samego siebie równa $0$
	* $u_i$ - dodatkowy parametr
	* $s_i$ - stan neuronu $i$
* Trajektoria stanu
	* $\sum_j w_{j,i} s_j < u_i \rightarrow s_i$
	* $\sum_j w_{j,i} s_j > u_i \rightarrow s_i := 1$
* Asynchroniczne aktualizacje
	* w jednym momencie jest aktualizowany jeden neuron
	* kolejność może być losowa
	* może być predefiniowana
* Sieć szuka takich wag, które minimalizują lokalnie funkcję energii
	* $E=-\frac{1}{2} \sum_{i,j} w_{i,j} s_i s_j + \sum_i u_i s_i$
	* utworzenie sieci to utworzenie minimów lokalnych
	* wzór na liczbę minimów funkcji energii - ile różnych wzorców może zapamiętać sieć
	* $\simeq \frac{n}{2 \log_2 n}$
* Uczenie - metoda Storkey'a
	* pokazanie sieci kolejnych przykładów indeksowanych przez $t=1, 2, \ldots, T$
	* stan sieci w chwili $t$ reprezentuje $t$-ty przykład
	* $w_{i,j}(0) = 0$
	* $w_{i,j}(t) = w_{i,j}(t-1) + \frac{1}{n}s_i(t) s_j(t) - \frac{1}{n}s_i(t)h_{j,i}(t) - \frac{1}{n}h_{i,j}(t)s_j(t)$
	* $h_{i,j}(t) = \sum_{k=1, k\notin\{i, j \}}^n w_{i,k}(t-1)s_k(t)$
* Praktyczne zastosowania
	* pamięć asocjacyjna - zapamiętuje wzorce w trakcie uczenia, po podaniu wektora wejściowego, odpowiedzią będzie jeden z zapamiętanych wzorców, najbardziej podobny do wejścia
	* problemy optymalizacyjne - pozwala znaleźć rozwiązanie problemów optymalizacyjnych (NP) przez odpowiednią konstrukcję sieci i funkcji energii
	* rekonstrukcja danych, odszumianie

## Ograniczone maszyny Bolzmanna
* Restricted Bolzman Machines (RBM)
* Na wejściu wektor binarny
* Sieć stara się znaleźć najbardziej podobny, zapamiętany wektor
* Zastosowania
	* odszumianie danych
	* uzupełnianie danych
	* symulowanie pracy generatora
* Jedna warstwa wejściowa, jedna warstwa ukryta
* Stan
	* ukrytej - losowany z wejściową
	* wejściowej - losowany z ukrytą
	* początkowy wejściowej - dany
	* końcowy wejściowej to wynik
* Funkcja energii
	* $E(v,h) = - \sum_{i} a_i v_i - \sum_j b_j h_j - \sum_{i,j} v_i w_{ij} h_j$
	* a - obciążenia dla wejść
	* b - obciążenia dla neuronów ukrytych
	* v - wejścia
	* h - ukryte
* Uczenie
	* maksymalizacja entropii
* Contrastive divergence
	* losujemy jedną z próbek treningowych $v$
	* wyliczamy wartości stanów $h$
	* na podstawie $h$ próbujemy odtworzyć $v$ - $v'$
	* na podstawie $v'$ próbujemy odgadnąć $h$ - $h'$
	* aktualizacja wag ($w$) i obciążeń ($a$, $b$) przy na podstawie różnic między rzeczywistymi v,h a przewidywanymi
* Można wytrenować sieć, tak żeby nauczyły się wzorców obrazów
	* widoczne jednostki reprezentują piksele wejściowe
	* ukryte jednostki przechwytują cechy wyższego poziomu
* Po wytrenowaniu może rekonstruować obrazy z aktywacji ukrytych jednostek
	* i generować nowe przez próbkowanie z wyuczonej dystrybucji

## Głębokie Sieci Przekonań (DBN)
* Deep Belief Networks
* Problem
	* rzutowanie danych binarnych na przestrzeń o małym wymiarze
	* jak PCA, tylko nieliniowe i binarne
* Ogólny pomysł
	* kilka OMB połączonych ze sobą - stos
* Ukryta warstwa jednego RBM połączona(?) z widoczną warstwą kolejnego RBM
* Uczenie po kolei
* Po nauczeniu
	* w jedną stronę - ekstraktor cech wyjścia
	* w obie strony - generator próbek analogicznych do danych

## Samoorganizująca się mapa (SOM)
* Sieć Kohonena, Self-organizing map, SOM
* Cel - nisko-wymiarowa reprezentacja danych
	* jak nieliniowe PCA
	* nienadzorowane uczenie
	* grupowanie podobnych danych
* Koncept
	* kulki połączone sprężynami, sprężyny ulegają odkształceniom
	* każda kula ma jakąś wartość
	* bierzemy próbkę o jakiejś wartości, szukamy do której kuli jest najbardziej podobna
	* ta podobna kula jest aktualizowana - przyciąga do siebie sąsiednie kulki, w zależności od stopnia podobieństwa
	* odchylające się kulki ciągną za sobą sąsiadów
* Sieć odtwarza strukturę danych
* Nienadzorowane grupowanie
	* nie wymaga żadnych założeń
* Wytrenowaną sieć można wykorzystać jako klasyfikator
	* trzeba każdemu neuronowi przypisać klasę
* Neurony ułożone na siatce, zazwyczaj w $\mathbb{R}^2$
	* neuron ma wektor wag takiej wymiarowości jak dane wejściowe
* Uczenie
	* losowanie próbki
	* liczymy odległość próbki do każdego neuronu
	* wybieramy najbliższy
	* aktualizacja wszystkich wag neuronów zgodnie z funkcją sąsiedztwa
	* w implementacji sąsiedztwo zwęża się wraz z krokiem $t$
* Praktyczne zastosowanie
	* problem kompresji obrazów, RGB, każdy piksel kodowany przez 0-255
	* każdy piksel może mieć $256^3$ różnych wartości
	* wyświetlacz nie wyświetli $256^3$ różnych wartości tylko mniej
	* jak byśmy każdej trójce (r,g,b) przypisali stałego integera 8-bitowego - mamy 256 różnych barw piksela
	* możemy wcześniej wybrać takie 256 barw rozłożonych równomiernie
	* równomierna paleta raczej będzie słaba, jak wybrać dobrą
	* chcemy algorytmu, który z obrazka wejściowego wyznaczy najlepsze 256 barw
	* można wyznaczyć przez klasteryzację z 256 klastrami

Ważna jest umiejętność przetransformowanie problemu do formatu odpowiedniego dla wybranego modelu. Będą pojawiać się nowe, lepsze model SI

TSNE - jak PCE ale bierze pod uwagę etykiety
