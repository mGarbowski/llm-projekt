# Light field, AR i VR

## Jak opisać światło w świecie
* Plenoptic function
* Z którego punktu $(x,y,z)$
* Z jakiego kąta $(\varphi, \theta)$
* Z jaką częstotliwością $\lambda$
* W jakim czasie $t$
* $L(x,y,z,\varphi, \theta, \lambda, t)$

## Light field
* Uproszczenie funkcji plenoptycznej
* Wszystkie promienie przechodzą przez powierzchnię jak przez okno
* Promienie światła parametryzowane przez 4-wymiarową funkcję
	* pozycja otworka z kamery otworkowej na płaszczyźnie 2D $(u,v)$
	* pozycja piksela na 2D sensorze $(s,t)$
* Uproszczenie funkcji plenoptycznej - $L(u,v,s,t)$
* Kamera light field
	* synchronizowane zdjęcie z wielu pozycji
	* każda pozycja widzi odrobinę inny obraz
	* możliwość tworzenia wirtualnej kamery  - inny zakres widzenia

### Urządzenia
* Kamery plenoptyczne - Raytrix
	* specjalna soczewka - wiele soczewek przesuniętych względem siebie
	* nie ma problemu z synchronizacją
* Macierz kamer
	* problem synchronizacji
* Optyka z wieloma aperturami
	* pelican imaging

### Nowe możliwości produkcji
* Poruszanie wirtualną kamerą
* Kompozycje oparte na głębi
	* przez nałożenie kilku obrazów


### Macierze kamer
* Różne możliwości - inny trade-off
* Rzadka macierz
	* elastyczny widok
	* mniej miejsca i zasobów
	* gorsza jakość
* Duża, gęsta macierz
	* elastyczny widok
	* dobra jakość
	* dużo miejsca i zasobów
* Mała macierz
	* dobra jakość
	* mało miejsca i zasobów
	* słaba elastyczność widoku

## AR
* Augmented reality
* Wzbogacenie rzeczywistości o informacje generowane komputerowo
	* wizualne
	* dźwiękowe
	* dotykowe
* Źródła danych
	* kamera
	* gps
	* żyroskop
	* akcelerometr
	* wszystko co mamy pod ręką np. w smartfonie

### Zastosowania
* Rozrywka
	* np. pokemony
* Turystyka
	* wyświetlanie dodatkowych informacji o obiektach
	* lokalizacja z wykorzystaniem obrazu
* Medycyna
	* informacje o stanie pacjenta
	* podgląd różnych źródeł danych
* Przemysł
	* informacje o urządzeniach

### Wymagane funkcje
* Wykrywanie punktów / płaszczyzn
* Estymacja oświetlenia
* Śledzenie obrazów
* Śledzenie twarzy
* Cloud anchors
	* multiplayer

### Technologia
* ARKit - Apple
* ArCore - Google
* Vuforia


### QR code
* Kod graficzny
* Umożliwia kodowanie różnego typu informacji
	* linków
	* tekstu
* Szybkie znalezienie dzięki 3 kwadratom w rogach
	* wzory pozycjonowania
* Informacja o formacie
	* poziom korekcji błędów
	* wersja kodu

## Analiza obrazu
* Wykorzystanie klasycznych algorytmów w celu szybkiej analizy obrazu
	* wyznaczanie krawędzi
	* przechodzenie między przestrzeniami barw
	* progowanie
	* porównanie ze wzorcem
	* itd.

### Punkty charakterystyczne
* Cecha w kontekście wizji komputerowej
	* pewien zbiór informacji na temat zawartości obrazu, który zwykle dotyczy jakiegoś jego fragmentu i umożliwia identyfikację
* Punkty charakterystyczne
	* punkty pozwalające dobrze określać obiekty/obrazy
	* np. narożniki, krawędzie

### Detektor
* Wykrywanie punktów charakterystycznych
* Klasyczne, zaimplementowane w OpenCV
	* SIFT
	* Harris
	* SURF
	* FAST
* Też rozwiązania oparte o sieci neuronowe

#### Harris
* Wykrywanie narożników
	* sąsiedztwo zawiera dwie dominujące i różne krawędzie
	* krawędź to nagła zmiana jasności
* Badanie funkcji dla każdego piksela
	* $c(u,v) = \sum_{x,y} w(x,y) |I(x+u,y+v) - I(x,y)|^2$
	* $w(x,y)$ - waga piksela
	* $I(x,y)$ - wartość piksela
* Maksymalizacja funkcji $c$
	* $c(u,v) = \begin{bmatrix}u \ v\end{bmatrix} M \begin{bmatrix}u \\ v \end{bmatrix}$
	* $M = \sum_{x,y} w(x,y) \begin{bmatrix} I_x^2 & I_xI_y \\ I_xI_y & I_y^2 \\ \end{bmatrix}$
* Wyznaczamy $R = \det M - \kappa(\mathrm{tr} M)^2$
	* $\mathrm{tr}$ - ślad macierzy - suma elementów na głównej przekątnej
* Wybieramy maksima o wartości $R$ powyżej ustalonego progu

### Deskryptor
* Skrócony opis cechy
* Rozpatrywane pod względem konstrukcji i szybkości obliczeń
* Typy
	* rzeczywiste
	* binarne
* Przykładowy deskryptor - SIFT

#### Census Transform
* Deskryptor binarny
* Sprawdzamy sąsiedztwo piksela
	* 1 jeśli piksel z sąsiedztwa jest większy niż piksel, 0 jeśli mniejszy
* Deskryptor - złożenie wartości bitów z okna
* Dopasowanie - dystans Hamminga

#### Inne deskryptory binarne
* FREAK
* ORB
* BRISK
* AKAZE
* LBP
#### SIFT
* Scale invariant feature transform
* Wyznaczanie punktów charakterystycznych, niekoniecznie krawędziowych
* Algorytm
	* utworzenie piramidy obrazów
	* na każdym poziomie piramidy filtr Gaussa $k\sigma$
	* obliczenie różnicy gaussianów
* Wyszukiwanie ekstremów
* Lokalne ekstrema są potencjalnymi punktami charakterystycznymi
* Jeżeli intensywność kandydata jest mniejsza niż pewien próg to jest odrzucany
* Analiza Hesjanu w celu odrzucenia punktów leżących na krawędziach
	* sprawdzenie stosunku wartości własnych macierzy
	* jeśli stosunek max do min większy niż pewien próg to punkt jest odrzucany
* Deskryptor - domyślnie 128 wymiarów
	* sąsiedztwo punktu charakterystycznego 16x16
	* podział sąsiedztwa na bloki 4x4
	* dla każdego bloku tworzony jest histogram orientacji ze skokiem co 45 stopni

### Dopasowanie
* Chcemy znaleźć punkty z takimi samymi (podobnymi) deskryptorami
* Najprościej - porównanie ze wszystkimi
* FLANN matcher
	* partycjonowanie przestrzeni na kratki w celu szybszego przeszukiwania
	* wykorzystanie kd-drzew
* Problemy z dopasowaniem
	* problemy typu dopasowanie wielu do 1, 1 do wielu

### Wykorzystanie sieci neuronowych
* Zwykle rozwiązania end-to-end
	* detektor i deskryptor
* Przykłady
	* Superpoint
	* LIFT

## SLAM
* Symultaniczna lokalizacja i mapowanie
* Mapowanie
	* budowanie reprezentacji świata
* Lokalizacja
	* znalezienie miejsca danej kamery w odtworzonym świecie
* Problemy
	* drift
	* akumulacja błędu w czasie

## VR
* Doświadczenie
	* imersja
	* śledzenie 6DoF
	* kontrolery ruchowe
* Wymagany specjalny sprzęt
	* gogle, kontrolery
* Ostatnio gogle posiadają też tryby mixed reality

### Problemy
* Motion sickness
	* problemy z błędnikiem - oczy widzą ruch a ciało stoi
* Zmęczenie oczu
	* problem konwergencja-akomodacja jak przy stereo
* Ciężar
* FoV
	* technologia nie pokrywa całego pola widzenia - widać ramki
* Izolacja od otoczenia
