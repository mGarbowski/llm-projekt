# 2024-12-11

## Naprawa rozwiązań widoczna dla metody
Rozwiązania są najpierw naprawiane, potem trafiają do loga i są poddawane ewaluacji

Złączenie metody naprawy z algorytmem optymalizacyjnym skutkuje zmianą sposobu generowania sąsiadów - zmianą relacji sąsiedztwa
Sposób jest różny i zależny od tego, w którym miejscu przestrzeni przeszukiwań znajduje się punkt (jak oddalony jest od granic)

## Obciążenia naprawy rozwiązań
Wykresy

Na górze zachowanie średniej dla rozkładu normalnego przy ograniczeniach od -1 do 1
sprawdzamy jaka jest wartość oczekiwana po wygenerowaniu i naprawie, odejmujemy wartość modyfikowanego losowo punktu

oczekujemy wartości 0

różnica w stronę środka (z dala od ograniczeń)

Przy projekcji i odbiciu, stopień ucieczki jest mniejszy niż przy zawijaniu i reinicjacji

dolne wykresy - wariancja po naprawie / wariancja przed naprawą

### Widoczna dla DE
![[Pasted image 20250124165137.png]]

benchmarki są wrażliwe na sposób naprawy rozwiązań
najlepsze wyniki średnio daje metoda ponownego próbkowania

schemat naprawy istotnie wpływa na wynik jeśli optimum jest blisko ograniczeń - warianty mogą mniej lub bardziej odsuwać populację od ograniczeń

Rzutowanie - wiele punktów na ramce kostki
odbijanie i reinicjacja - podobne chmury punktów
zawijanie - ogrągła chmura zawinięta na inne narożniki

### Naprawa niewidoczna dla DE
![[Pasted image 20250124165218.png]]
rzutowania - funkcja celu jest płaska za ograniczeniami
poziomice - takie zachowanie jak wcześniej tłumaczyliśmy na 2D

## Styl Lamarckowski i Darwinowski
Darwinowskie - cechy nabyte nie są dziedziczone
Lamarckowskie - cechy nabyte są dziedziczone

naprawa niewidoczna (darwinowska) działa gorzej (porównanie ECDF)

rozważania o wyższości jednych metod nad drugimi nie są uniwersalne, trzeba by to zbadać dla inynch algorytmów niż DE

resampling - ponowne losowanie sasiada, reinicjacja - losowanie z calej przestrzeni z oryginalnym rozkladem bez zwiazku z mutowanym

w ewolucji różnicowej z naprawą lamarckowską

ewolucja różnicowa w początkowej fazie głównie będzie się zajmować uwzględnianiem ograniczeń, a w końcowej ograniczenia sprawiają że staje się prawie bezużyteczny

odbijanie lamarckowskie i optimum blisko granicy - chmura utrzymuje się w pewnej odległości od ograniczenia

# Hybrydyzacja metaheurystyk z metodami optymalizacji lokalnej, algorytmy memetyczne


Uwzględnianie ograniczeń też jest wariantem optymalizacji
(problem spełniania ograniczeń)

proces wyznaczania punktu naprawianego jest procesem optymalizacji - maksymalizacja funkcji charakterystycznej zbioru dopuszczalnego

metoda optymalizacji globalnej i optymalizacja lokalna w miejsce naprawy

też warianty darwinowski i lamarkowski

## Zbiór przyciągania
zbiór tych punktów, z których można wyprowadzić ścieżkę wzdłuż której f celu maleje i koniec ścieżki znajduje sie w optimum lokalnym

definicja praktyczna - punkt należy do zbioru przyciągania jeśli algorytm optymalizacji lokalnej wystartowany w tym punkcie trafi do optimum lokalnego

## Wariant lamarkowski
Do loga będą trafiać same optima lokalne (przy idealnej optymalizacji lokalnej) - z punktu widzenia metody optymalizacji globalnej przestrzeń przeszukiwań składa się wyłącznie z optimów lokalnych

Jedyny mechanizm, który pozwoliłby przejść od jednego optimum lokalnego do drugeigo to złoty strzał z mutacją, jeśli zakres mutacji nie umożliwia odpowiedniego przeskoku to algorytm nigdy nie wyjdzie poza zbiór przyciągania opt lokalnego
Dla nieidealnej optymalizacji lokalnej warunek jest troche słabszy

## Wariant darwinowski
Zmieniają się wartości funkcji celu - każdy punkt będzie wyceniany jak najbliższe optimum lokalne
funkcja celu będzie schodkowa

Symulowane wyżarzanie w tym wariancie - przez większość czasu błądzi przypadkowo po zbiorze przyciągania optimum lokalnego
dopiero przy granicy zbioru przyciągania będzie uwzględniona wartość f celu przy akceptacji nowego punktu
Łatwiej przejsć do lepszego zbioru przyciągania w wariancie z hybrydyzacją lokalną
Może być trudniej podejść do granicy przez błądzenie przypadkowe
z hybrydyzacją jest łatwiej jeśli optimum jest blisko granicy zbioru przyciągania

W praktyce metody optymalizacji lokalnej nie dają idealnych wyników
Funkcja celu raczej nie jest przedziałami stała

## Eksperyment myślowy
rysunek ...
mutacja ma rozkład jednostajny na odcinku (-a, a)

wariant lamarkowski z AE

jak cała populacja jest w otoczeniu opt globalnego
a większe od 1 i selekcja bez elity - jest niezerowe prawdopodobieństwo, że wszystkie punkty przejdą do gorszego zbioru przyciągania
a musi być większe od 4 żeby populacja mogła wrócić z powrotem do opt globlanego

ucieczka od opt globalnego w AE może też wystąpić bez hybrydyzacji
jak otoczenie opt globalnego wąskie a lokalnego szerokie
zasięg mutacji gaussowskiej - w odpowiedniej odległości od średniej numerycznie już się nie da wygenerować mutanta
survival of the flattest

wąskie optima - jak w funkcjach straty neuronowych klasyfikatorów obrazów - np. zmiana jednego piksela obrazka - takie problemy są przy optymalizacji gradientowej jak w uczeniu sieci
