# OpenGL c.d. (2025-12-16)

## Frame buffer
* Możena używać wielu frame bufferów, oddzielnie na pozycje, oddzielnie na wektory normalne, mapy oświetlenia
* Potem zawartość trafia do front/back buffera
* Każde przejście do frame buffera to kompletny pipeline z vertex shaderem i fragment shaderem
* Fragment shader może zapisywać dane wyjściowe do wielu różnych bufferów

## Bufor głębi
...

pierwszy framebuffer jest traktowany jako tekstura
jest nakładana na fullscreen quad w celu wyswietlenia na ekran

## Tesselation shader
* opcjonalny
* podział prymitywów na mniejsze
* składa się z dwóch shaderów
* operuje na prymitywach `GL_PATCHERS` - łaty
* tesselation control shader
	* ustawia jaki ma być podział siatki
* tesselation evaluation shader
	* wyliczenie wartości

## Współrzędne barycentryczne
* Opisanie pozycji wewnątrz trójkąta jako proporcje wierzchołków trójkąta
* Sumują się do 1
* Poza trójkątem - jeden z parametrów jest ujemny

## Geometry shader
* Pozwala na tworzenie własnych prymitywów

## Compute shader
* Nie jest połączony z pipelinem renderowania
* Analogiczne przeznaczenie do CUDA
	* CUDA jest bardziej rozwijana

Unika się IFów w shaderach
problem wydajnościowy jeśli shadery mają różny czas wykonywania

## Anti-aliasing
* supersampling - wiele próbek dla jednego piksela
* OpenGL ma zaimplementowany MSAA
	* więcej wywołań fragment shadera na krawędziach
	* sam jakoś wykrywa krawędzie
	* wykonywany we fragment shaderze w dodatkowym przejściu przez potok
* temporal antyaliasing
* oparte o sieci neuronowe

## Blending
* `glEnable(GL_BLEND)`
* domyślny w OpenGL działa na podstawie kanau alfa
* przy losowej kolejności wychodzą artefakty
* do poprawnego wyrenderowania trzeba posortować obiekty
	* najpierw wszystkie nieprzezroczyste
	* przezroczyste renderujemy od najdalszych do najbliższych kamery - drogie do robienia co klatke

## Efekty cząsteczkowe
* Symulowanie efektów takich jak ogień czy dym
* Cząsteczki mają cykl życia, wielkośc, kształt, teksturę
* częstotliwosć generowania nowych cząsteczek
* trajektorie ruchu
* dobre zastosowanie dla compute shader
* można użyć instancjonowanego renderowania
	* w renderze najdroższe jest `glDrawArrays`
	* zamiast wywoływania wiele razy można raz wołać `glDrawArraysInstanced`

## Post processing
* Przetwarzanie obrazu po renderingu

lepiej używać `clamp` zamiast if

## Bloom
* Oddzielny render dla wszystkich obiektów i tylko dla źródeł światła
* na źródłach światła zrobiony blur
* sumowanie obu obrazów