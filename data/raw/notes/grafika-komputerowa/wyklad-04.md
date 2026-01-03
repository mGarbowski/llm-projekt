# Wprowadzenie do OpenGL

* Slajdy i kod na LeOnie
* Open Graphics Library
* Pierwsze popularne API do wykorzystania akceleracji sprzętowej (GPU) do renderowania grafiki w czasie rzeczywistym
* Nie jest biblioteką, tylko API
* OpenGL działa jak maszyna stanu
	* ustawienie koloru czerwonego - zostanie dopóki go nie zmienimy
* Wieloplatformowy
	* to samo API do windowsa, maca, linuxa, androida
* Względnie łatwy
* Konkurencyjne
	* DirectX - Windows, Xbox
	* Vulkan - wieloplatformowy ale trudny
* Nie obejmuje obsługi wejścia i integracji z systemem operacyjnym (dźwięk, klawiatura, wyświetlanie)

## Biblioteki
* Opakowują OpenGL, ułatwiają wykorzystanie
* GLFW
	* tworzenie okna
	* obsługa urządzeń wejścia
* GLEW
	* wspomaganie obsługi OpenGL i rozszerzeń
* Assimp
	* wczytywanie modeli 3D
* GLM
	* operacje wektorowe i macierzowe
* STB Image
	* wczytywanie plików graficznych do teksturowania obiektów

## Przykład kodu OpenGL
* Prefixy w nazwach funkcji
	* był tworzony zanim istniał C++ i przestrzenie nazw

## Wersje OpenGL
* Omawiamy wersję 3.0
	* obecnie standard
* W początkach grafiki czasu rzeczywistego
	* OpenGL implementował fixed pipeline - przekształcenie sceny 3D do 2D (rasteryzacja) - szybsze niż raytracing
	* immediate mode - dane o wierzchołkach trzymane w RAM ale co klatkę przysyłane do VRAM
* Vulkan wyparł OpenGL
	* OpenGL był dostosowany do rasteryzacji
	* GPU stały się na tyle szybkie żeby używać raytracing w czasie rzeczywistym
	* konstrukcja OpenGL nie pasuje do raytracingu
	* Vulkan wspiera i rasteryzację i raytracing

## Vertex Buffer Object
* Bufor w karcie graficznej
* Zawiera przygotowane przez programistę dane
* Wierzchołki mają parametry
	* pozycja
	* kolor
	* wektor normalny
	* współrzędne tekstury
* Dwa podejścia
	* osobne bufory na każdy atrybut
	* wszystkie atrybuty w jednym buforze i informacja jak je czytać

## Vertex Array Object
* Zawiera wszystkie dane o wierzchołkach
* Zawiera referencje do kilku VBO
* VBO to wskaźnik do pamięci GPU
	* karta zwraca id typu glInt
* glVertexAttribPointer
	* identyfikator atrybutu - taki będzie w shaderze
	* ilość danych dla pojedynczego wierzchołka
	* typ danych
	* czy normalizować dane - to chyba już jest deprecated
	* wielkość struktury danych dla wierzchołka (najczęściej sizeof struktury)
	* offset -  atrybutu w strukturze danych
	* trzeba to wołać dla każdego atrybutu wierzchołka
* każdy atrybut trzeba włączyć
	* glEnableVertexAttrib...

Mamy rozwiązany problem immediate mode

## Programy cieniujące
* Program cieniujący (shader program) składa się z minimum dwóch shaderów
	* vertex shader - wyliczenie danych dla wierzchołka
	* fragment shader - wyliczanie danych dla fragmentu utożsamianego z pikselem
* Przepływ danych
	* Atrybuty - mamy trójkąt z 3 wierzchołkami
	* Dla każdego wierzchołka jest odpalany Vertex Shader
	* Rasteryzaja - wyliczenie na które fragmenty przypada trójkąt
	* Dla każdego z tych fragmentów uruchamia się Fragment Shader
	* shadery uruchamiają się równolegle
* Shadery w programie GLSL
* zmienne wejściowe
	* layout (location = x) - x ustawiony w glVerteAttribPointer
* zmienne uniform
	* ustawiane z poiomu CPU
	* stałe dla każdego shadera
* zmienne wyjściowe
	* zmienne wyjściowa vertex shadera - są poddawane interpolacji i trafiają jako wejście do fragment shadera
	* interpolację robi karta graficzna
	* zmienne są linkowane ze sobą po nazwie
	* trzeba uważać na zgodność typów
* main
	* operacje
	* vertex shader wylicza pozycję
* fragment shader
	* wyjście - zawsze kolor
	* może być więcej wyjść, o tym potem

## GLSL
* Swizzling - dowolny dostęp do pól wektora
	* v.x
	* v.xy
	* v.yx
	* v.xx

## Rysowanie trójkąta
* OpenGL jest maszyną stanów - frame buffer trzeba wyczyścić 
* W OpenGL jest 10 wbudowanych prymitywów
* Do GPU przesyła się listę wierzchoków, trzeba dodatkowo podać informację czym są te wierzchołki

## Podwójne buforowanie
* Dwa bufory front i back
* Jeden zawiera wyświetlaną klatkę
* Do drugiego zapisuje się wyliczaną kolejną klatkę
* Po narysowaniu podmienia się te bufory

## Macierz modelu
* manipulacja modelem w przestrzeni 3D