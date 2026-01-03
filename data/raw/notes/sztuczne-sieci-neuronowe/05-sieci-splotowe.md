# Sieci splotowe

## Splot w matematyce
* Rodzaj złożenia dwóch funkcji na przedziale
* Do zastosowań w wizji komputerowej i rozpoznawaniu obrazów - splot dyskretny
* Splot 2 wektorów 1D będzie dłuższy niż wektory wejściowe

$$ (h \ast f)(t) = \int_{-\infty}^\infty h(t-\tau)f(\tau)d\tau $$

## Splot 2D
* Co z pikselami na brzegach
	* można dołożyć zera
	* można dopełnić tymi samymi wartościami co na brzegach
	* można obciąć macierz maski (np. w rogu będzie obcięta z 3x3 do 2x2)
* Filtry uśredniające
	* same jedynki (przeskalowane żeby sumowały się do 1) - rozmycie
	* gauss
	* dobre na szum gaussowski
* Filtry górnoprzepustowe
	* kierunkowo wykrywające krawędzie
	* działa jak gradient
	* laplasjany - jak drugie pochodne, więcej szczegółów
* Dodanie obrazu krawędziowego do oryginalnego - wyostrzenie
	* w obrazie barwnym wykonuje się operację osobno dla każdego kanału

## W sieciach neuronowych
* Wagi masek do splotu są trenowane w procesie uczenia
* W pierwszych warstwach robią operacje rozmycia
* W późniejszych warstwach robią wykrywanie krawędzi
* Czemu sieci gęste nie nadają się do przetwarzania obrazów
	* przy rozwinięciu macierzy w wektor traci się informacje o sąsiedztwie
* Operacja splotu po całym obrazie
	* uwzględnia zależności przestrzenne
* Też do dźwięków - zamienia się na spektrogramy - macierzowa reprezentacja
* Dopiero złożenie kilku warstw splotowych pozwala wyszukiwać bardziej złożone zależności

## Warstwa splotowa
* Obraz szary - macierz
* Obraz barwny - 3 wymiary (3 kanały barwy)
* Powierzchnia maski - pole recepcyjne
* Pola recepcyjne pokrywają poprzednią warstwę
* Neuron oblicza pozycję na wyjściu
* Warstwa splotowa 1x1 służy do zmiany liczby kanałów w wejściu

## Działanie warstwy splotowej
* Funkcja aktywacji - zazwyczaj ReLU
* Sigmoidy dają wolniejszą naukę
* Neuron może mieć obciążenie - dodawane do wyjścia po przemnożeniu przez maskę

## Parametry warstwy splotowej
* Głębokość - liczba kanałów wyjściowych (liczba różnych filtrów)
* Wysokość i szerokość pola recepcyjnego
	* zazwyczaj kwadratowe
	* nieparzysty rozmiar - ustalony środek
* Krok (stride) - co ile pikseli są pola recepcyjne
	* większość implementacji ma 1 piksel (standrardowo)
* Ramka (padding)
	* jak obsługiwać piksele na krawędziach
	* jak szeroko dookoła obrazu sięga obwódka wypełniona zerami
* Dylacja
	* rozproszenie pola recepcyjnego
	* równomiernie oddalone od siebie komórki macierzy
* Trzeba zwracać uwagę na domyślne ustawienia
	* w zastosowaniach przemysłowych na innym środowisku się trenuje, a na innym wdraża na produkcji
	* często runtime to dedykowany mikrokontroler
	* przenoszenie przez framework ONNX

## Warstwa łącząca
* Pooling, subsampling
* Np. okno 2x2 z operacją maximum/średnią
* Też ma konfigurowany krok
	* np. krok równy rozmiarowi maski

## Warstwa gęsta
* Dense
* Tak samo jak w perceptronie wielowarstwowym

## Cała struktura
* Wyjście
	* klasyfikacja - tyle wyjść ile klas
	* identyfikacja - jedno wyjście tak/nie
* Algorytm propagacji wstecz do wyliczania gradientów
* Do detekcji jednego obiektu - można dołożyć do wektora wyjść x,y,w,h
	* do detekcji wielu obiektów ta architektura się nie nadaje
	* można wycinać fragmenty zdjęcia i je klasyfikować
	* po zaklasyfikowaniu fragmentu można rozszerzać okno
* Nie nadaje się do wszystkiego
	* detekcja
	* segmentacja
	* do tego są dedykowane architektury
* Nadają się do reprezentacji macierzowych

## Znane architektury
* LeNet (1989)
	* warstwy splotowe ze zmniejszającymi się wymiarami
	* na koniec warstwy gęste
* LeNet-5 (1998)
	* 4 warstwy konwolucyjne, 2 gęste
* AlexNet (2012)
* ZFNet
	* optymalizacja AlexNet
	* autorzy pracy robili wizualizacje w pośrednich warstwach
* VGGNet (2014)
	* wystarczają filtry 3x3
	* więcej warstw splotowych to raczej lepiej
* GoogleNet
	* rzadka reprezentacja filtra
	* moduły incepcji
	* kilka operacji splotowych na raz na tym samym obszarze (różne rozmiary sąsiedztwa)
	* skuteczność na zbiorze testowym zbliżona do człowieka
* ResNet
	* jeśli dodawanie warstw nie poprawia wyniku
	* skip connection
	* warstwa rezydualna inicjowana zerami
	* wyjście $f(x) + x$
	* szybciej się uczą
