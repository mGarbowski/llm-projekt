# Indeksowanie

## Indeskowanie multimediów
* Potrzeba wynika z dużej ilości multimediów
* Danych multimedialnych jest coraz więcej
* Coraz trudniej wyszukiwać / filtrować
* Dane są użyteczne jeśli można je odnaleźć
* Najprościej indeksować przez opis tekstowy
	* dla dokumentów tekstowych to łatwe, np. słowa kluczowe
	* dla audio / wideo można dodać tekstowe atrybuty
	* opis jest subiektywny, może zwracać uwagę na inne aspekty
	* "co autor miał na myśli"
* Pojawia się potrzeba automatyzacji opisów / indeksowania

## Wyszukiwanie tekstowe
* Dla danych audiowizualnych trzeba stworzyć odpowiedni opis
* Słowa kluczowe mogą być wieloznaczne
* Różni ludzie mogą opisać to samo zdjęcie w różny sposób

## Informacja o danych
* Może być nadawany przez twórcę i nie wynikać z treści
	* data i sposób uzyskania
	* autor, prawa autorskie
	* odsyłacze do powiązanych materiałów
	* raczej dodawane ręcznie
* Opis sygnałowy (zawarty w treści)
	* niezależny od kontekstu i twórcy
	* możliwe mapowanie na cechy semantyczne
	* nie ogranicza możliwości wyszukiwania
	* cechy bez wartości semantycznej
	* możliwa automatyczna ekstrakcja cech
* Opis semantyczny (zawarty w treści)
	* cechy wysokopoziomowe
	* zależny od kontekstu i twórcy
	* odnosi się do ludzkiej interpretacji
	* ogranicza wyszukiwanie tylko do użytych pojęć
	* typowo ręczna i półautomatyczna ekstrakcja cech (wymaga weryfikacji)
	* subiektywny
* Oba typy opisu są potrzebne w praktyce

## Metadane
* Opis danych multimedialnych w celu ich indeksowania
	* tekst naturalny
	* słowa kluczowe
	* tekst ustrukturyzowany (XML, JSON)
	* cechy wizualne (kolor, tekstura, kształt, ...)
	* cechy audio (widmo, linia melodyczna, ...)
* Wyszukiwanie "językiem obrazu" - szkic obrazu jako zapytanie

## Wyszukiwanie semantyczne
* Można przybliżyć wyszukiwanie semantyczne wykorzystując różne cechy opisu sygnałowego
* Np. "bramki z meczów piłkarskich"
	* szybki ruch kamery
	* powtórki
* Wyszukiwanie abstrakcyjnych pojęć ("nadzieja", "tragedia")
	* raczej nie dają się wyciągnąć z cech sygnałowych obrazu

## Automatyczna adnotacja
* Proces, w którym system komputerowy automatycznie przypisuje metadane w postaci podpisów lub słów kluczowych do obrazu cyfrowego
* Realizowana za pomocą wieloklasowej klasyfikacji z bardzo dużą liczbą klas
* Sieci neuronowe uzyskują najlepsze wyniki
* Uczenie z dodatkowym opisem tekstowym umożliwia generowanie zdań dla nowych obrazów

## System z indeksowaniem
* Wykorzystanie deskryptorów jako zwięzłego zapisu metadanych/cech
	* podobieństwo deskryptorów oznacza podobieństwo treści
* Standaryzacja technik pozwalających na wyszukiwanie, przeglądanie, filtrowanie danych multimedialnych
* Dane audiowizualne na wejściu
	* podlegają ekstrakcji cech - powstają deskryptory audiowizualne
	* dane zapisywane w bazie razem z deskryptorami
* Użytkownik wykonuje zapytanie
	* dostaje wynik na podstawie podobieństwa do deskryptorów, a nie plików multimedialnych
	* wybiera mały podzbiór danych
	* odległość euklidesowa deskryptorów (wektorów liczb)

## Standard MPEG-7
* Multimedia Content Description Interface
* Standard do wyszukiwania, przeglądania i filtrowania
* Cechy uzyskane po ekstrakcji opisuje się w tym standardzie
* Definicja języka opisu (DDL) opartego na XML
* Zawiera definicje różnych deskryptorów (metadanych)
	* ogólne - data/czas, komentarze, autorzy, podział na ujęcia
	* wizualne - kolor, tekstura, kształt, ruch
	* audio - melodia, widmo
* Definiuje relacje między deskryptorami (grupowania i hierarchizacja)

### Wymagania
* Deskryptor powinien być
	* ogólny
	* efektywny do wyszukiwania i filtrowania
	* upakowany (mały rozmiar)
	* niezależny od skali, obrotu, kompresji itd

### Opis sceny
* Do skutecznego opisu sceny dobrze jest ją posegmentować na obiekty
	* opisana przez wiele deskryptorów
	* deskryptory ułożone hierarchicznie, odzwierciedlają hierarchię obiektów na scenie
	* deskryptory kolorów
	* opisy tekstowe dodawane ręcznie
* Obiekty muszą najpierw zostać wyróżnione
* Podejście obiektowe było modne dawniej
* Wymaga dużego nakładu pracy i nie daje dużych korzyści

### Podsumowania
* Deskryptor jako spis treści
	* pozwala znaleźć reprezentatywne fragmenty
	* np. na podstawie kluczowych ramek
* Podsumowanie może być hierarchiczne
* Podobnie jak pole MFRA w kontenerze MP4

### Deskryptory koloru 

#### Deskryptor koloru dominującego
* Reprezentuje do 8 dominujących kolorów
* Na różne sposoby można określać w jaki sposób się je wyznacza
* Kolor opisywany przez indeks kwantyzacji
	* opcjonalnie wariancja wartości kolorów w klastrze
	* opcjonalnie koherencja przestrzenna kolorów (jak rozproszone / skupione)

#### Porównywanie kolorów dominujących
* Mogą być różne liczby kolorów w deskryptorach
* Bierze się pod uwagę procentowe udziały kolorów w obrazie
	* sumują się do 1
	* pozostałe kolory są pomijane
* Oblicza się odległość między histogramami na podstawie wzoru

#### Skalowalny histogram kolorów
* Kolory w przestrzeni HSV
	* 256 komórek
	* współrzędne kwantowane do mniejszej liczby poziomów nieliniowo do 4 bitów
* Transformacja Haara skwantyzowanych wartości
	* obliczanie sum i różnic kolejnych par
	* redukuje się do jednej wartości
	* umożliwia skalowanie histogramu (liczby komórek)
* Skalowalna reprezentacja histogramu
	* zmienna liczba kolorów
	* zmienna dokładność reprezentacji wartości
	* pomijanie mniej znaczących płaszczyzn bitowych

#### Deskryptor Color Structure
* Histogram koloru z uwzględnieniem struktury pikseli danego koloru
* Informacja czy piksele danego koloru stanowią drobne elementy czy zwarte grupy
* Przykłada się maskę do obrazu wielokrotnie

#### Deskryptor Color Layout
* Jakie kolory są reprezentatyzwne dla odpowiednich części obrazu
* Reprezentanci jako średnia lub kolor dominujący

#### Deskryptor Color Temperature Browsing
* Określa temperaturę barwową związaną z wrażeniem ciepła
* Związane z częstotliwościami emitowanymi przez ciało doskonale czarne
* Jeden bajt, wartości 0-255

### Deskryptory tekstury
* Texture Browsing
	* cechy powtarzanych wzorców
	* regularność
	* kierunkowość
	* skala
* Homogeneous Texture
	* rozkład energii i odchylenia w kanałach częstotliwościowych
	* transformacja w układzie biegunowym
* Edge Histogram
	* globalne i lokalne histogramy krawędzi

### Deskryptory kształtu
* Region Shape
	* kształt jako ważona suma regionów bazowych
	* obiekt może składać się z wielu regionów
	* transformata biegunowa Angular Radial Transform (ART)
* Contour Shape
	* opis konturu obiektu jako punkty przegięcia wzdłuż krzywizny
	* maksymalne krzywizny konturu 
	* przestrzeń CSS - curvature scale space
	* można iteracyjnie redukować liczbę punktów przegięcia
	* funkcja filtrowana filtrem dolnoprzepustowym

### Deskryptory ruchu
* Motion Activity
	* ogólne parametry określające natężenie ruchu i rozmieszczenie
	* wektory ruchu
	* podobnie jak przy estymacji ruchu dla kompresji wideo
* Camera Motion
	* opis ruchu kamery za pomocą zestawu operacji podstawowych
* Motion Trajectory
	* opis trajektorii wybranego punktu poruszającego się obiektu za pomocą wielomianów

### Deskryptory twarzy
* Face Recognition
	* opis cech twarzy do celów automatycznej identyfikacji i weryfikacji osób

### Podsumowanie
Deskryptory MPEG-7 są rzadko używane bezpośrednio ale pokazują możliwe cechy sygnałowe przydatne jako wejście dla CNN. Takie cechy można wyznaczyć podczas wstępnego przetwarzania, przed podaniem danych do sieci neuronowej.
