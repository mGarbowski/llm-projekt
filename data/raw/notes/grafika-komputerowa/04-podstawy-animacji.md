# Podstawy animacji
* Animować - dawać czemuś życie
* Animacja komputerowa - wszelkie obliczenia komputerowe używane do wytworzenia obrazów z zamiarem uzyskania wrażenia ruchu
* Animacja
	* ożywienie postaci na podstawie ścieżki dźwiękowej, fabuły, scenerii i grupowania dostarczonego przez dział rozmieszczenia
	* dodanie szczegółów do postaci, które umożliwiają "aktorowi" zagranie danej sceny
* Najbardziej rozpowszechniona - praca z systemami ścieżkowymi
	* ang. track based systems
	* możliwość zmiany wyglądu krzywych - operacje na stycznych i na punktach kontrolnych

## Percepcja ruchu
* Ciąg obszarów pokazywanych szybko jeden po drugim jest odbierany przez obserwatora jako pojedynczy ruchomy obraz
	* działanie układu oko-mózg
* Trwanie wrażenia wzrokowego
	* ang. persistence of vision
	* zachowanie śladu obrazu przez krótką chwilę po usunięciu bodźca wzrokowego przez siatkówkę oka
* Ruchy beta
	* iluzja optyczna, gdzie szybka zmiana statycznych obrazów tworzy płynnie zmieniającą się scenę
	* zachodzi dla częstotliwości wyświetlania klatek (frame rate) >10-12
	* podstawa filmu i animacji
* Dlaczego to działa
	* nerw optyczny odpowiada na zmiany światła ok. 10 razy na sekundę
	* 2 razy więcej klatek rejestrowane jest jako ruch zamiast pojedynczych obrazów

### Frame rate
* Liczba klatek wyświetlanych w ciągu sekundy
* Standardowo dla filmu 24 fps
* Aplikacja interaktywna - 12 fps

## Pipeline animacyjny
* Fazy projektu
	* tworzenie fabuły
	* pre-produkcja - adresacja technicznych możliwości i wyzwań
	* produkcja
	* post-produkcja - dopracowywanie finalnego efektu i poprawianie błędów
* Dział pipeline
	* dba o poprawne przesyłanie danych między działami
	* dostarcza narzędzia ułatwiające pracę artystom
	* automatyzuje pracę (np. cache'owanie animacji)

## Podział filmu
* Klatka - pojedynczy obraz w filmie
* Ujęcie - zbiór klatek, który opisuje akcję z jednego punktu widzenia
* Sekwencja - zbiór ujęć, który można wyodrębnić na podstawie obszaru, w którym odbywa się akcja
* Produkcja - cała animacja

## Rodzaje klatek
* Klatka kluczowa
	* nadaje główny ruch
	* w przypadku postaci zawiera pozę kluczową
	* po obejrzeniu tylko póz kluczowych da się stwierdzić co się dzieje w animacji
	* w praktyce - zachowany zestaw parametrów ustawiony ręcznie przez animatora - zmienne artykulacji
* Klatka pośrednia
	* występuje pomiędzy klatkami kluczowymi
	* zwiera pozy pośrednie - przechodzące od jednej do drugiej pozy kluczowej
	* zwykle generowane, czasem poprawiane przez animatora

## Interpolacja animacji
* Wyznaczanie wartości pośrednich między klatkami kluczowymi
* Interpolacja liniowa
* Interpolacja Hermite'a
	* krzywe sklejane Camulla-Roma
* Wykorzystanie krzywych Beziera

### Interpolacja liniowa
* $p(u) = (1-u)p_0 + up_1$
	* $p_0,p_1$ - punkty między którymi chcemy dokonać interpolacji

## Interpolacja Hermite

$$p(u) = U^TMB$$
$$U^T = [u^3 \ u^2 \ u \ 1]$$
$$M=\begin{bmatrix}
2 & -2 & 1 & 1 \\
-3 & 3 & -2 & -1 \\
0 & 0 & 1 & 0 \\
1 & 0 & 0 & 0 \\
\end{bmatrix}$$
$$B = \begin{bmatrix}
p_i \\
p_{i+1} \\
p'_i \\
p'_{i+1} \\
\end{bmatrix}$$

### Krzywe sklejane Camulla-Roma
* Krzywa zbudowana z wielomianowych łuków Hermite
* Pochodne w punktach łączenia łuków są przyjmowane na podstawie prostej konstrukcji geometrycznej
* Dla każdego punktu łączenia łuków $p_i$, wektor $p'_i$ jest równe połowie różnicy punktu następnego $p_{i+1}$ i poprzedniego $p_{i-1}$
* Zaleta - szybkość obliczeń
* Wada - wektor pochodnej nie zależny od położenia punktu dla którego jest liczony

### Sterowanie ruchem wzdłuż krzywej
* Przy opisie parametrycznym krzywej
	* zmiana parametru $u$ ze stałym krokiem nie oznacza, że kolejne punkty leżą w tej samej odległości od siebie
* Parametryzacja łukowa
	* $s=S(u)$ - zależność między długością łuku $s$, a parametrem krzywej $u$
	* stałe przyrosty wartości $s$ - ruch ze stałą prędkością
	* zmienne przyrosty $s$ - ruch przyspieszony i opóźniony
	* w ogólnym przypadku nie ma rozwiązania analitycznego

## Interpolacja obrotów
* Przekształcenie bryły sztywnej
	* wykorzystanie macierzy
	* interpolowanie obrotów nie jest oczywiste, bezpośrednie interpolowanie macierzy przekształceń może dać bezsensowny wynik
* Reprezentacje położeń kątowych
	* z ustalonymi osiami
	* kąty Eulera
	* z użyciem kąta i osi obrotu
	* kwaterniony

### Reprezentacja z ustalonymi osiami
* Obroty wokół osi układu współrzędnych przy ustalonej kolejności obracania
	* np. x-y-x
	* nie mogą być po sobie dwa obroty wokół tej samej osi
* Gimbal lock
	* dwie osie obrotu mogą się nałożyć
	* problem z interpolacją położeń kątowych
	* tracony jest jeden stopień swobody

### Reprezentacja z użyciem kątów Eulera
* Osie obrotu są osiami lokalnego układu współrzędnych i obracają się razem z obiektem
* Przekształcenie
	* sekwencja trzech obrotów
	* kolejne obroty są w nowych układach współrzędnych

### Reprezentacja z użyciem kąta i osi obrotu
* Twierdzenie Eulera o obrotach
	* do dowolnego położenia kątowego można przejść z innego za pomocą jednego obrotu wokół pewnej osi
* Interpolacja może być wykonana przez osobną interpolację osi obrotu i interpolację położenia kątowego
	* składanie obrotów
* Rozwiązanie - kwaterniony

## Ekstrapolacja animacji
* Określa w jaki sposób krzywa powinna się zachowywać przed pierwszą i po ostatniej klatce kluczowej
* Przykładowe typy
	* stała
	* liniowa

## Motion capture
* Technika przechwytywania ruchów aktora i zapisywania ich w przestrzeni 3D
* Wykorzystane specjalne znaczniki śledzone przez szereg kamer
	* znaczniki pokryte materiałem odblaskowym
	* wykorzystanie triangulacji do określenia pozycji 3D
	* precyzyjna pozycja może być estymowana poprzez znalezienie centroidu Gaussianu
* Systemy posiadają od 2 do 48 kamer
* Wersje z aktywnymi markerami
	* każdy z markerów emituje swoje światło
	* możliwość zbierania informacji z dalszych odległości
	* markery są lepiej identyfikowalne
* Estymacja pozycji
	* dąży się do estymacji pozy bez wykorzystania znaczników
	* sieci neuronowe uczony na danych motion capture
	* estymacja szkieletu
	* mniejsza precyzja
	* OpenPose - biblioteka
* Czy motion capture zapewnia idealną animację
	* wymaga czyszczenia danych
	* animacje potrafią wyglądać sztucznie
* Dolina niesamowitości
	* ang. uncanny valley
	* kiedy coś przypominające i funkcjonujące jak człowiek wywołuje nieprzyjemne odczucia i odrazę
* Idealne do filmów fabularnych
	* realistyczne postacie i żywi aktorzy

## Morfing
* Jedną z technik animacji jest deformowanie obiektów
* Zmiana kształtu
	* transformacje wierzchołków i brył
	* transformacje punktów sterujących krzywych
* Morfing - płynne przejście z jednego obiektu do drugiego
