# Systemy związane z bezpieczeństwem (2024-05-13)

## Bezpieczeństwo (safety)
Brak nieakceptowalnego ryzyka śmiarci lub uszczerbku na zdrowiu człowieka wynikającego z działania systemu lub pośrednio z uszkodzenia środowiska.

## System związany z bezpieczeństwem
System, którego prawidłowe działanie jest niezbędne do zapewnienia lub utrzymania bezpieczeństwa ludzi

* światła uliczne
* centrala pożarowa w inteligentnym budynku
* system zabezpieczenie robota przemysłowego

## Ryzyko

### Zdarzenie zagrażające
Zdarzenie, którego wynikiem jest fizyczny uraz lub pogorszenie stanu zdrowia ludzi, bezpośrednio i pośrednio na skutek szkód w środowisku

### Ocena zagrożenia
Ryzyko = Prawdopodobieństwo x Stopień szkodliwości

Stopień szkodliwości w umownej jednostce, określony w ramach danego systemu

### Redukcja ryzyka
* Ryzyko systemu - bez działań ograniczających
* Akceptowalny poziom ryzyka
	* przyjęty podczas projektowania systemu
* Redukcja ryzyka
	* poniżej maksymalnego akceptowalnego poziomu
	* dąży się do jak największej redukcji

### Funkcja bezpieczeństwa
Funkcja przeznaczona do utrzymania bezpiecznego stanu instalacji w odniesieniu do kontrolnego zdarzenia zagrażającego. Może być integralną częścią sterownika lub odrębnym urządzeniem.

Powinny raczej dublować czujniki i elementy wykonawcze (np. oddzielny termometr dla regulatora i funkcji bezpieczeństwa na wypadek awarii jednego z nich).


## Analiza bezpieczeństwa

### Drzewo niezdatności
* Fault-tree analysis (FTA)
* Zdarzenia
	* proste (liście)
	* pośrednie
	* szczytowe (korzeń)
* Analiza systemu i celów jego działania
	* utworzenie drzewa wymaga znajomości działania układu
* Identyfikacja zdarzeń zagrażających
* Budowanie drzewa dla każdego zdarzenia
* Badanie drzewa w celu określenia
	* które zdarzenia proste powodują awarię
	* tolerancji na uszkodzenia
	* prawopodobieństwa uszkodzenia systemu
	* lokalizacji elementów krytycznych (należy je zdublować)
* Podczas projektu
	* wprowadzenie zabezpieczeń (elementy, funkcje)
	* określenie planu diagnostyki, spodziewanych napraw

### Opis zdarzenia
* Kod identyfikacyjny
* Nazwa zdarzenia
* Opis
* Prawdopodobieństwo
* Zależności czasowe

### Metody analizy
* Przegląd drzewa
* Wyznaczenie funkcji boolowskich
* Wyznaczenie minimalnych przekrojów
	* zbiorów zdarzeń prostych powodujących wystąpienie zdarzenia szczytowego

## IEC 61508
* Bezpieczeństwo funkcjonalne programowalnych systemów związanych z bezpieczeństwem
* Dotyczy działania systemu i wpływu czynników zewnętrznych
	* np. poduszka powietrzna redukuje ryzyko przy wypadku (zdarzeniu zewnętrznym dla samochodu)
* Norma określa 
	* standardy przy tworzeniu systemów
	* metody probabilistyczne do szacowania ryzyka
	* cykl utrzymania bezpieczeństwa

### Bezpieczeństwo funkcjonalne
Część bezpieczeństwa, która zależy od prawidłowej pracy systemu, tzn. od prawidłowej odpowiedzi na sygnały wejściowe

### Cykl utrzymania bezpieczeństwa
* Identyfikacja i ocena zagrożeń
* Analiza bezpieczeństwa
* Określenie i alokacja wymagań bezpieczeństwa
* Planowanie i realizacja funkcji bezpieczeństwa
* Ocena i zatwierdzenie
* Eksploatacja, obsługa, naprawy

### Poziom nienaruszalności bezpieczeństwa
(Safety Integrity Level)

Prawdopodobieństwo, że system wykona wymagane funkcje bezpieczeństwa w zadanych warunkach i czasie. Dotyczy systemu jako całość.

### Tryby pracy systemu bezpieczeństwa
* Na rzadkie przywołanie - prawdopodobieństwo nie zadziałania w trakcie obsługi żądania
* Na częste lub ciągłe przywołanie - prawdopodobieństwo nie zadziałania na godzinę
* Poziomy od 1 do 4 określają zakresy prawdopodobieństwa dla obu trybów

### Szacowanie wymaganego poziomu SIL
* Skutki awarii
* Częstotliwość / czas / okres przebywania ludzi w warunkach zagrożenia
* Nieuchronność zagrożenia
* Prawdopodobieństwo zdarzenia
* Na podstawie tych kryteriów określa się poziom SIL 1-4

### Projektowanie architektury oprogramowania
* Metody strukturalne
	* diagramy klas, sekwencji itd
* Meteody półformalne
	* np. języki graficzne do projektowania PLC
* Formalne
	* odpowiednia notacja matematyczna
	* np. metoda specyfikacji agentów ...
* Narzędzia CASE wspomagające specyfikację
	* narzędzia do generowania kodu źródłowego
	* np. z języków graficznych
* Wykrywanie i diagnostyka efektów
* Kody detekcyjne i korekcyjne
* Korekcja defektów metodami sztucznej inteligencji
* Rekonfiguracja dynamiczna
* W zależności od poziomu SIL mogą być
	* neutralne
	* nie zalecane
	* zalecane
	* mocno zalecane

### Projektowanie szczegółowe i implementacja
* Metody strukturalne, półformalne i formalne
* Narzędzia CASE
* Programowanie strukturalne
* Podejście modułowe
* Brak obiektów dynamicznych i skoków, ograniczone użycie przerwań, wskaźników, rekursji
