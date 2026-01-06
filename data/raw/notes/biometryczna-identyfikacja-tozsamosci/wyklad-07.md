# Biometria twarzy (2025-12-01)

## Wyzwania w rozpoznawaniu twarzy
* Przesłonięcia
* Wyraz twarzy
* Obrót
* Zarost
* Starzenie się
* Urazy, procedury medyczne
* Zdjęcie w warunkach kontrolowanych lub niekontrolowanych
* Rozróżnianie bliźniąt
* Zwykłe podobieństwo wyglądu

## Potok
* Detekcja twarzy
* Ustawienie w standardowej pozycji (alignment)
	* wyśrodkowanie
	* obrót
* Ekstrakcja cech

## Detekcja
* Krytyczny krok
* Często trudniejszy niż ekstrakcja cech
* Wyznaczanie cech z obszaru który nie jest twarzą nie może dać dobrego rezultatu
* Grupy algorytmów
	* oparte o regiony
	* oparte o przesuwające się okno
	* na egzamin
* Przykłady
	* retina face
	* mtcnn

### Oparte o regiony
* Jeden model wyznacza propozycje regionów
* Klasyfikator ocenia czy region zawiera twarz

### Oparte o przesuwające się okna
* Tworzy się piramidę obrazów różnej rozdzielczości
* Jeden rozmiar okna na obrazy różnej wielkości
	* wykrywa różne rozmiary obszaróœ

### Viola-Jones
* Stary detektor twarzy
* Oparty na falkach Haara
* Pewne obszary twarzy są jaśniejsze lub ciemniejsze względem siebie
* Przykładając falki można wykryć elementy odpowiadające charakterystyce twarzy
* Złożenie wielu słabych klasyfikatorów (setki) daje dobry klasyfikator
* Bardzo szybko można odrzucić obszar, który na pewno nie jest twarzą
* Jest implementacja w OpenCV
* Na egzamin
	* ważne że jest szybki bo działa jako kaskada
	* szybko odrzuca obszar niebędący twarzą
	* niedokładny

## Alignment
* Landmarki - punkty charakterystyczne twarzy
* Pozwalają na wyprostowanie obrazu
	* np. ustawienie oczu w linii poziomej
* Aproksymacja modelu 3D twarzy
* Poprawa oświetlenia
	* np. wyrównanie histogramu
* Wykorzystanie innych skanerów
	* bliska podczerwień
	* kamera głębi
	* termiczna podczerwień
	* bardzo dobrze się sprawdzają

## Ekstrakcja cech
* Ręcznie skonstruowane cechy
	* Filtry Gabora 2D
	* SIFT
	* SURF
	* HOG
	* LBP
* Modele neuronowe

### Local Binary Patterns
* Podobne tekstury mają podobne histogramy
* Obraz po detekcji dzieli się na n komórek
	* np. 16
* Kodowanie komórek
	* dla sąsiedztwa np. 3x3 sprawdzenie czy każdy piksel jest większy czy mniejszy od środkowego
	* przemnożenie maski binarnej przez predefiniowaną całkowitoliczbową maskę dla wyznaczenia wartości dla piksela
	* różne możliwości definiowania sąsiedztwa
* Mapowanie kodów
	* wariant 256 binów
	* wariant 59 binów - 58 niejednorodnych i wszystkie jednorodne do jednego bina
* Obliczenie histogramu
	* 59 cech
	* wektor liczb
* Normalizacja histogramów
	* będzie histogram dla każdej komórki
* Połączenie histogramów w jeden deskryptor

#### LBP do rozpoznawania twarzy
* Przykład
* Po kilka próbek na osobę
* Z każdego zdjęcia wyznaczany wektor cech
* Rozpoznawanie nieznanej osoby
	* wyznaczenie cech
	* znalezienie najbliższego dopasowania
	* próg podobieństwa

### Oparte o sieci neuronowe
* Głębokie struktury
* Głównie sieci splotowe
* System raczej nie ma klasyfikować na zamkniętym zbiorze
* FaceNet, triplet loss