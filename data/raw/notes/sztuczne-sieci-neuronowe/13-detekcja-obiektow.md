# Detekcja obiektów

## Zadania
* Rozpoznawanie obrazów - czy na obrazie jest kot
* Rozpoznawanie obiektów i ich lokalizacja - gdzie na obrazie jest kot
* Detekcja obiektów - jakie zwierzęta i gdzie są na obrazie
	* liczba obiektów nie jest znana

## Technika okna przesuwnego
* Prostokątny obszar o stałych rozmiarach
* Przesuwa się po obrazie z określonym krokiem
* Każdy podobszar jest klasyfikowany jako obiekt lub tło
* Potem każdy wybrany podobszar może być ponownie klasyfikowany pod kątem przynależności obiektu do konkretnej klasy
* Po przejściu całego obrazu okno można powiększyć i powtórzyć
* Bardzo kosztowne obliczeniowo
	* klasyfikacja na wszystkich podobszarach

## Indeks Jaccarda
* Intersection over Union (IoU)
* Miara dokładności detekcji
* Porównuje się bounding box wyznaczony przez algorytm z wyznaczonym ręcznie przez człowieka (ground truth)
* $J = \frac{A \cap B}{A \cup B}$
* Detekcję uznaje się za poprawną jeśli $J$ jest powyżej przyjętego progu (np. $0.5$)

## Algorytm NMS
* Non maximum suppression
* Algorytmy używające okien przesuwnych mogą zwrócić wiele bounding boxów dla tego samego obiektu
* NMS służy do grupowania bounding boxów
* Wiele nakładających się prostokątów (IoU powyżej progu) zamieniamy na 1 prostokąt przez uśrednianie ich współrzędnych

## Algorytm selektywnego poszukiwania
* Selective search
* Zamiast okna przesuwnego
* Najpierw grupowanie
* Przestrzeń poszukiwań obiektów ograniczona da wyznaczonych klastrów
* Mniej podobszarów do sprawdzenia

## R-CNN
* Regions with CNN
* Dwuetapowy detektor
* Wyznaczenie kandydatów na obiekty
	* pierwszy etap
	* np. algorytm selektywnego poszukiwania
	* wyznacza się ok. 2000 podobszarów do późniejszego sprawdzenia
	* ta mniej kosztowna obliczeniowo część detekcji
* Klasyfikacja kandydatów
	* docelowy klasyfikator
	* określa czy tło czy obiekt, jeśli obiekt to określa klasę
* Na koniec regiony agreguje się algorytmem NMS
* Bardzo nieefektywny
	* ekstrakcja cech działa niezależnie dla każdego z 2000 regionów

## Fast R-CNN
* Na początku tworzy się mapę cech dal całego obrazu
* Dla każdego kandydata na obiekt wyciąga się wektor cech stałej długości z tej mapy
* Na końcu jeden wektor z rozkładem prawdopodobieństwa klas i dla każdej klasy współrzędne bounding boxa
* Generowanie kandydatów na obiekty jest zupełnie niezależnym krokiem

## Faster R-CNN
* Mapa cech wyznaczona dla całego obrazu służy jednocześnie do detekcji kandydatów na obiekty
* Jedna sieć i do wyznaczania kandydatów i do klasyfikacji
* Wyznaczanie regionów zainteresowania (ROI)
	* Region Proposal Network (RPN)
	* wyznacza zestaw regionów wokół równomiernie rozmieszczonych punktów kotwic
	* dla każdego obszaru wyznacza się prawdopodobieństwo, że zawiera obiekt
	* przesunięcie regionu wyznaczane przez regresję
* Do drugiego etapu jest wybierane 2000 najlepszych kandydatów
	* wycina się region z mapy cech
	* klasyfikacja na podstawie wycinka mapy cech
	* regresja - lepsze dopasowanie obrysów do kandydatów na obiekty wyznaczonych przez RPN (przesunięcia)
* Warstwy konwolucyjne są współdzielone - wyznaczona mapa cech jest używana w 1 i 2 etapie

## YOLO
* You Only Look Once
* Dużo szybsze, a tylko trochę mniej dokładne niż Faster R-CNN
* Obraz odpowiednio przeskalowany
* Dzieli się obraz na siatkę $S \times S$
	* każda komórka odpowiada za wykrywanie obiektów w jej granicach
* Siec przewiduje położenie $B$ obrysów w każdej komórce
	* $(x,y,w,h,c)$
	* współrzędne
	* $c$ - confidence score
	* dodatkowo dla każdego obrysu przynależność do klasy (rozkład prawdopodobieństwa)
* Z jednego obrazu generuje wyjście wymiaru
	* $S \times S \times (B \cdot 5 + C)$
	* $C$ - liczba klas
* Maksymalna liczba znalezionych obiektów jest ograniczona rozmiarem siatki
* Nie nadaje się do wykrywania małych, gęsto rozmieszczonych obiektów
* Jedna sieć konwolucyjna - działa w czasie rzeczywistym
* Problem z detekcją obiektów, których proporcje znacznie się różnią od przykładów ze zbioru treningowego
