# OpenGL - teksturowanie (2025-12-09)

## Element Array Buffer
* Wskazuje GPU kolejność rysowania wierzchołków

## Back-face culling
* Renderowane są tylko te ściany które trzeba wyświetlić
* Trójkąt ma ścianę przednią i tylną
	* podwójny nakład obliczeniowy
* Trzeba zdefiniować która ściana ma być rysowana
* Wektor normalny ściany jest dostępny na poziomie fragmentu - we fragment shaderze
* Back-face culling jest na etapie rasteryzacji - pomiędzy VS i FS
* Trójkąt można rysować zgodnie ze wskazówkami zegara lub przeciwnie
	* dwie ściany trójkąta można tak rozróżnić
* Standard w grafice komputerowej - ściana przeciwna do ruchu wskazówek zegara to ściana przednia
	* można to przełączyć w OpenGL
* `glEnable(GL_CULL_FACE)`
* W każdym środowisku do modelowania 3D jest możliwość konfiguracji kolejności wierzchołków przy eksporcie

## Tekstura
* Tekstura to funkcja wielowaymiarowa
	* najczęściej 2D
	* najczęściej tożsama z bitmapą
	* ale też tekstury 3D
	* też tekstury proceduralne
* `texture(u,v) -> (R,G,B)`
	* współrzędne uv zawierają się w przedziałach $[0,1]$
	* dla bitmapy robi się interpolację
	* funkcja wbudowana w GLSL
	* podajemy sampler jako argument
* Obiekt 3D musi mieć UV mapę
* Praktycznie nigdy nie zdarza się sytuacja, gdzie tekstura nie zostaje pomniejszona/powiększona

### Mipmapping
* Oszczędzenie czasu na skalowanie tekstur kosztem zajęcia pamięci na GPU na trzymanie przeskalowanych tekstur

### Filtrowanie tekstury
* Można skonfigurować filtrowanie tekstury przy skalowaniu
	* najbliższy sąsiad
	* interpolacja liniowa

## Teksturowanie we fragment shader
* Sampler podaje się do shadera jako uniform
* Przełączanie się między teksturami jest drogie
	* nie wrzuca się do uniformu całej tekstury
	* wrzuca się pośredni element - sampler
	* sampler jest stały
	* żeby zmienić teksturę - zmienia się teksturę w samplerze
* Do bindowania używamy id samplera a nie id tekstury
