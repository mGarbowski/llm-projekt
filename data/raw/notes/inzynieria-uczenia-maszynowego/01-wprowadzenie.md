# Inżynieria uczenia maszynowego

Obejmuje proces przemysłowego wytwarzania modeli predykcyjnych, począwszy od analizy wymagań, przez projektowanie i tworzenie modeli, po ich wdrożenie, eksploatację i modernizację lub zastąpienie innymi podejściami.

* Uczenie maszynowe częściowo pokrywa się z metodami statystycznymi
* Sztuczna inteligencja to nie tylko uczenie maszynowe
* Zajmujemy się metodami, które opierają się na trenowaniu na zbiorach danych

## Czym różni się budowa modelu od normalnego programowania
* Programowanie imperatywne i deklaratywne
* Uczenie nadzorowane
	* uczenie - podawanie przykładów pożądanego działania
	* zastosowanie do generowania predykcji
	* nie wiemy jak dokładnie powinny przebiegać obliczenia
	* procesem uczenia sterują hiperparametry
	* sprawdzać poprawność może *wyrocznia*
* Uczenie nienadzorowane
	* np. zadanie klastrowania
	* uczenie - podajemy dane, o których strukturze chcemy wnioskować
	* zastosowanie do generowania predykcji
	* *wyrocznia* z definicji nie istnieje
	* definicja poprawności jest dyskusyjna
	* do oceny jakości wyników modelowania służą często kryteria zewnętrzne (użyteczność)

### Konsekwencje
* Wynik zależy od danych
	* jakość danych wpływa na jakość modelu
* Specyficzne podejście do testowania
* Czasami trudno ustalić, czy mamy poprawny wynik
* Dokładny przebieg obliczeń nie jest wyspecyfikowany
	* drobne zmiany danych wejściowych dają znacznie różny wynik
	* trudno ustalić co wpływa na zmianę

## Podejście do realizacji projektu

### SEMMA
* Sample
	* rozpoczynamy od wyciągnięcia próbki danych
	* żeby szybciej i mniejszym nakładem osiągnąć jakiś efekt
* Explore
	* analiza eksploracyjna
	* jakie są atrybuty, jakie mają rozkłady
	* lepsze zrozumienie danych
* Modify
	* selekcja zmiennych
	* transformacje
	* feature engineering
* Model
	* wybór odpowiednich metod
	* modelowanie
* Assess
	* ewaluacja uzyskanych wyników
* Nie jest bardzo sformalizowane
* Pomija aspekty biznesowe
* Raczej chwytliwy skrót niż dobra metodologia

### KDD
* Knowledge Discovery in Databases
* Iteracyjny proces dotyczący odkrywania wiedzy w bazach danych
* Sformalizowany w latach 90 (20 stron artykułu)
* Proces
	* zrozumienie domeny, z której pochodzą dane
	* utworzenie roboczego zbioru danych
	* oczyszczanie i preprocessing zebranych danych
	* redukcja wymiarowości, projekcje
	* dobór adekwatnego zadania modelowania do konkretnego celu
	* eksploracyjna analiza danych, wybór metody, ustalanie hiperparametrów
	* budowa modelu
	* analiza uzyskanych wyników modelowania
	* wdrożenie / zastosowanie przygotowanych modeli w praktyce
* Sprzężenie zwrotne
	* proces nie jest liniowy
	* wracamy się do poprzednich etapów (o 1 lub więcej, nawet do początku)

### CRISP-DM
* Cross-industry standard process for data mining
* Standard opisujący proces realizacji projektów data-mining
* Precyzyjny dokument opisujący standard
* Etapy
	* zrozumienie zagadnienia biznesowego
	* zrozumienie danych - może trzeba się cofnąć, zmienić dane albo zmienić oczekiwania
	* przygotowanie danych
	* modelowanie - może trzeba się cofnąć do przygotowania danych
	* ocena jakości
	* wdrożenie jeśli poszło dobrze
	* cofnięcie do początku jeśli model jest za słaby
* Warto poświęcić dużo czasu na pętlę zrozumienie biznesu - zrozumienie danych
* Iteracyjna praca nad modelem i przygotowaniem danych
* Dokładnie zdefiniowane jakie dokumenty (artefakty) powstają w ramach poszczególnych etapów
* Zrozumienie zagadnienia
	* biznesowe kryteria sukcesu - ile PLN
	* analityczne kryteria sukcesu - jaki błąd średniokwadratowy
* Modelowanie
	* około 10% czasu całego projektu
	* ewaluacja w sensie analitycznym
* Ewaluacja
	* w sensie biznesowym
* W projektach komercyjnych są różne wymagania co do dokumentacji
	* zależy od branży, organizacji
	* raczej nie tworzy się wszystkich opisanych dokumentów
	* i tak przechodzi się przez wszystkie etapy

## Iteracyjna realizacja projektu
* Podejście Model Development Process
* Iteracje można podzielić z grubsza na fazy
* W każdej fazie przechodzi się przez wszystkie etapy
	* ale pomiędzy fazami różnie rozkłada się nakład pracy na dany etap
	* na początku więcej czasu na przygotowanie danych i zrozumienie niż na audyt

## Perspektywy w projekcie UM
* Domenowa
	* ktoś musi rozumieć dziedzinę
	* product owner
* Analityczna
	* jakie metody pasują do danego zagadnienia
	* jakich danych potrzeba
* Techniczna
	* czy rozwiązanie da się wdrożyć i utrzymywać
	* czy spełnia kryteria niefunkcjonalne

## Podsumowanie
* Trzeba poświęcić czas na dokładne zrozumienie zadania
	* problemu i danych
* Dane są elementem determinującym co jesteśmy w stanie osiągnąć
* Obserwacje, założenia przyjmowane *po drodze* warto dokumentować
* Modelowanie jest tylko jednym z etapów
* Aby projekt mógł się udać trzeba określić kryteria sukcesu
* Praca z UM ma naturę iteracyjną i wymaga kilku perspektyw
* Tylko 10-20% projektów UM kończy się sukcesem
