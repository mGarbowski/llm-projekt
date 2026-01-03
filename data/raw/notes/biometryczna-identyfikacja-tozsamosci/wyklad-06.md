# Statystyczna ocena systemów biometrycznych (2025-11-24)

## Problem ewaluacji systemów biometrycznych
* Niepewność pomiarów
* Jaki eksperyment należy wykonać żeby ocenić system
* Jakie powinny być wartości progów
* Jaka powinna być liczność próbek w bazie danych
* Jakie poziomy błędów możemy zagwarantować odbiorcy systemu

## Norma ISO
* Ocena technologiczna
	* off-line
	* tylko część algorytmiczna
	* istniejąca lub specjalnie utworzona próba badawcza
* Ocena w scenariuszu zastosowań
	* off-line lub on-line
	* dla określonego scenariusza i określonej grupy docelowej
	* środowisko przypominające środowisko docelowe
* Ocena w warunkach operacyjnych
	* on-line
	* normalna eksploatacja systemu
	* pilotaż

### Ocena technologiczna
* Ocena wybranego komponentu systemu - np. algorytmu
* Próba ustalona, pobrana przez uniwersalny sensor
* Próba nie powinna być znana twórcom komponentu
* Wyniki powinny być powtarzalne
* Znaczne niedoszacowanie błędów w stosunku do zastosowania w warunkach operacyjnych
	* niereprezentatywna próba
	* pomija się trudności z pobraniem próbki biometrycznej

### Ocena w scenariuszu zastosowań
* Testowanie kompletnego systemu
* Środowisko testowe bliskie produkcyjnemu
* Każdy system powinien mieć własny sensor
* Powtarzalność pod warunkiem kontroli scenariusza
* Niedoszacowanie błędów w porównaniu do warunków operacyjnych
	* proces nadal jest nadzorowany

### Ocena w warunkach operacyjnych
* Program pilotażowy
* Warunki mogą być nienadzorowane
* Warunki mogą się zmieniać w nieprzewidziany sposób
	* zalecana rejestracja zmian
* Brak powtarzalności wyników
* Najbardziej wiarygodna ocena funkcjonowania systemu
	* nie zawsze możliwa
	* kosztowna

## Modelowanie niepewności

### Próba losowa
* Populacja generalna $X$
* Próba losowa zmiennej losowej $X$
* Z próby losowej pozyskujemy próbki, które są próbkami biometrycznymi

### Tworzenie próby losowej w biometrii
* Prezentacja charakterystyki biometrycznej
	* pojedyncze pobranie próbki
	* np. wykonanie jednego zdjęcia tęczówki
* Podejście
	* jedna lub kilka prezentacji
	* np. w celu doboru najlepszej
* Transakcja
	* co się dzieje jak człowiek podchodzi do systemu biometrycznego, robi co trzeba i dostaje decyzję
	* składa się z jednego lub kilku podejść - jeśli system pozwala na powtórzenie

### Probabilistyka i statystyka
* Probabilistyka zakłada znajomość rozkładu
* Statystyka - dowolna funkcja próby losowej $g(X_1, \ldots, X_n)$
	* statystyka jest zmienną losową
	* brak założeń o pełnej znajomości rozkładów prawdopodobieństwa zmiennych losowych
	* wyciąganie wniosków dotyczących badanej cechy w populacji generalnej na podstawie próby losowej

### Estymacja
* Szacowanie nieznanego parametru rozkładu za pomocą wartości statystyki (konkretnej liczby)
* Estymator - dowolna statystyka
* Pożądane cechy estymatora
	* nieobciążoność - wartość oczekiwana jest równa estymowanemu parametrowi
	* zgodność - wzór ...
* Przykłady estymatorów w biometrii
	* średnia arytmetyczna z wyników porównań
	* FNMR

## Ocena procesów pozyskiwania próbek i rejestracji

### Niepowodzenia pozyskania próbki
* Czemu nie można pobrać próbki
	* dane nie mogły być zaprezentowane (choroba, zranienie, ...)
	* błąd algorytmu, timeout
	* błąd przetwarzania próbki
	* niewystarczająca jakość cech
* Częstość FTA - failure to acquire
	* liczba podejść zakończonych niepowodzeniem / liczba wszystkich podejść

### Niepowodzenie rejestracji
* Powody
	* tak jak FTA
	* próbka nie została zaakceptowana w wyniku próbnej weryfikacji
* Estymator - częstość FTE - failure to enroll

## Ocena zgodności próbek
* Rodzaje próbek
	* próbki własne - tej samej klasy
	* próbki obce - innej klasy, w tym fałszerstwa bezwysiłkowe
	* fałszerstwa zaawansowane - specjalnie spreparowane
* Dopasowanie próbek
	* stopień podobieństwa/niepodobieństwa lub dopasowania/niedopasowania
	* nie zawsze jest łatwe przejście między podobieństwem i niepodobieńśtwwem
* Decyzja
	* ...

## Testowanie hipotez
* Porównanie biometrii to testowanie hipotezy statystycznej
* Hipoteza zerowa
* Hipoteza alternatywna
* Najprostszy przypadek
	* ...
* Przykłady
	* ...

### Test statystyczny
* Metoda przyporządkowująca realizacjom próbie losowej decyzje przyjęcia bądź odrzucenia weryfikowanej hipotezy z ustalonym prawdopodobieństwem
	* próba losowa - wynik porównania próbek biometrycznych
* Statystyka testowa
	* wykorzystywana do oceny hipotezy $H_0$
	* zbiór krytyczny i zbiór przyjęć hipotezy
	* np. znormalizowany Hamming distance
* Błąd I rodzaju $\alpha$ - false non-match (FNMR)
* Błąd II rodzaju $\beta$ - false match (FMR)
* Nieodrzucenie prawdziwej hipotezy $(1-\alpha)$
* Odrzucenie fałszywej hipotezy $(1-\beta)$

### Ocena fałszywego niedopasowania
* FNMR - w mianowniku tylko wewnątrzklasowe podejścia
* FNMR jest funkcją progu decyzyjnego

### Ocena fałszywego dopasowania
* FM - w mianowniku liczba porównań międzyklasowych
* FMR - nie włącza się fałszerstw zaawansowanych - na egzamin

## Różnice w ocenie podejścia i transakcji
* Ocena systemu polega na badaniu transakcji, a nie pojedynczych podejść
* FRR
	* funkcja polityki decyzyjnej 
	* FRR = FTA + (1-FTA)FNMR
	* liczba odrzuconych autentycznych transakcji / liczba transakcji wewnątrzklasowych
* FAR
	* FAR = (1-FTA)FMR
	* nie uwzględnia się niepozyskanych próbek

### Krzywa ROC
* Dla klasyfikacji binarnej
* Na osi y 1-FAR lub 1-FMR
* na osi x FRR lub FNMR
* Krzywa parametryczna, parametrem jest wartość progu
* Klasyfikator losowy - krzywa idzie po przekątnej
* Im bliżej lewego górnego rogu przechodzi krzywa tym lepszy klasyfikator

### Krzywa DET
* Dla klasyfikacji binarnej
* Deterction Error Tradeoff
* FAR(FRR)
* Skala odwrotnej dystrybuanty rozkładu normalnego
	* dla rozkładów normalnych - proste
	* inne fajne właściwości ...

### Krzywa CMC
* Dla weryfikacji
* Skumulowana charakterystyka dopasowania
* Cumulative Match Characteristic
* r - identyfikację uznajemy za skuteczną, jeśli właściwa osoba będzie zwrócona wśród $r$ najbardziej dopasowanych
* Na osi y odsetek poprawnych identyfikacji
* Na egzamin

### Systemy zamknięte vs otwarte
* Systemy zamknięte
	* wszyscy są zarejestrowani w systemie
* Systemy otwarte
	* nie wszyscy są zarejestrowani
	* FNIR - częstość fałszywie negatywnej identyfikacji
	* FPIR  - częstość fałszywie poprawnej identyfikacji

## Uwagi praktyczne
* Podział baz danych na rozłączne zbiory
	* estymacyjny (treningowy)
	* walidacyjny
	* testowy
* Istnieje wiele możliwych podziału bazy
	* staramy się żeby wynikowe porównania były niezależne - wymaga dużych zbiorów
	* przy małych zbiorach ...
* Zasady wykorzystania biometrycznych baz danych
	* 2 sposoby podziału próbek na estymacyjne i testowe
	* podział obrazów - obrazy dla tej samej osoby mogą trafić do obu - ok dla systemu zamkniętego
	* podział obiektów - wszystkie obrazy jednego obiektu są albo w jednym albo w drugim zbiorze
* Projektowanie rozpoznawania biometrycznego
	* EER nie jest najważniejsze
		* EER prawdopodobnie nie wypadnie w punkcie pracy który nas w ogóle nie interesuje
	* Różne punkty pracy systemu w zależności od zastosowania
		* tradeoff między wygodą a bezpieczeństwem


## Przykładowe pytanie na egzamin
* Na slajdzie
* Wykreślić krzywą ROC
