# Prywatność i bezpieczeństwo

## Perspektywy
* Dane
	* wykorzystywane do trenowania modeli
	* mogą zawierać elementy wrażliwe
	* wymagają szczególnej ochrony
	* dobre dane są tak w ogóle cenne
* Modele mogą stać się celem ataków
	* atakujący może wymusić inne niż pożądane zachowanie modelu
	* np. destabilizacja działania, wykradanie danych
* Wykorzystanie metod UM jako narzędzi w zagadnieniach związanych z bezpieczeństwem i prywatnością
	* np. fake news

## Prywatność

### Naruszenia w kontekście UM
* W kontekście danych uczących
	* kradzież, wyciek danych
	* brak zgody na gromadzenie i stosowanie danych
	* przetwarzanie danych w nieuprawniony sposób (RODO)
	* często model oznaczony jako open source mógł pod spodem używać czegoś z ograniczeniami licencyjnymi - nie nadaje się do zastosowania komercyjnego
	* trzeba przeglądać licencje, na których udostępniane są modele i zbiory danych (z pomocą prawników)
* W kontekście gotowego modelu
	* ustalenie czy informacje o konkretnej osobie były w zbiorze treningowym (np. model wytrenowany na grupie chorych)
	* inwersja - gdy mając dostęp do modelu próbujemy poznać atrybuty konkretnej osoby ze zbioru treningowego
	* trudniej przekonać kogoś do udostępnienia swoich danych jeśli nie możemy zagwarantować prywatności i anonimowości tych danych

### Obrona prywatności
* Anonimizacja
	* podmiana danych (np. login) na hasz / losowy ciąg
	* bywa zawodna
	* przykład Netflixa - skorelowanie z aktywnością w innych portalach (np. te same filmy ocenione w IMDb)
* Prywatność różnicowa
	* chcemy udzielić gwarancji co do prywatności i formalnie to udowodnić
	* jeśli zgodzisz się udostępnić swoje dane, to nie będziesz poszkodowany bardziej niż gdybyś ich nie udostępnił
	* nie udostępniamy surowych danych, agregatów itp.
	* do danych domieszana jest losowość
	* im silniejszy szum, tym silniejsze gwarancje, ale gorsze dane
	* nie da się zaatakować pojedynczego wiersza z dużą pewnością
	* do danego typu atrybutu dobieramy odpowiedni rozkład szumu
* Federated learning
	* nie przechowywać w jednym miejscu danych uczących - nie mają jak wyciec
	* informacje użytkowników są trzymane na ich urządzeniach
	* rozproszone trenowanie
	* zamiast danych, pobieramy z urządzeń gradienty
	* aktualizacja wag modelu jest rozsyłana do urządzeń
	* jeśli model jest za duży to np. tylko aktualizacje ostatniej warstwy
	* potrzebna jest duża baza użytkowników i kontrola nad ekosystemem
	* aktualizacje są całkiem asynchroniczne - problem techniczny

## UM jako cel ataków

### Modele zagrożeń
* Definiuje założenia o tym, do czego ma dostęp atakujący
* Analizujemy techniki ataku i obrony w świecie opisanym przez model zagrożenia
* Co może atakujący na etapie treningu (od najłatwiejszej do najtrudniejszej)
	* poznanie zbioru treningowego
	* wstrzyknięcie wiersza danych
	* modyfikacja istniejącego wiersza
	* zakłócenie logiki
* Co może atakujący na etapie inferencji
	* poznanie potoku
	* poznanie modelu
	* modyfikacja architektury
	* modyfikacja parametrów
* W definiowaniu modeli wyróżniamy
	* black box - znany potok i model, ale bez dostępu do konkretnych parametrów modelu
	* white box - atakujący ma pełen dostęp do kopii modelu

### Techniki zabezpieczenia
* Wszystkie da się obejść
* Filtrowanie
	* np. w LLMach - czy prompt narusza jakieś reguły

### Klasyczne techniki ataków
* Wstrzykiwanie treści / zmiana kolejności wykonywania instrukcji
* Wirtualizacja - symulowanie fikcyjnych scenariuszy
	* rozbicie prompta na dłuższą interakcję

### Złośliwe dane
* Adversarial examples
* Mamy poprawnie klasyfikowane zdjęcie
	* dodajemy do zdjęcia szum, niezauważalny dla człowieka
	* zaszumione zdjęcie jest niepoprawnie klasyfikowane
* Celowo spreparowane przez dodawanie małych zaburzeń, które powodują, że model zwróci nie to co powinien, a to na czym zależy atakującemu
* Możemy zdefiniować szukanie takiego złośliwego zaburzenia jako zadanie optymalizacyjne
	* model jest zamrożony
	* modyfikujemy zaburzenie
	* jak najmniejsze zaburzenie
	* dodanie zaburzenia do wejścia zmienia predykcję

### Modele zagrożenia, a metody ataku
* Czarne skrzynki
* Białe skrzynki
	* atakujący może np. policzyć gradient (na kopii modelu, efektywnie)
* Dodatkowe ograniczenia
	* maksymalna liczba wywołań - dla modeli dostępnych jako serwisy
* Jeśli metoda obrony chroni przed atakiem na białą skrzynkę, to tym bardziej chroni przed atakiem na czarną skrzynkę

### Metoda DeepFool
* Atak na białą skrzynkę - wymaga obliczania gradientu
* Założenie - w okolicy aktualnego punktu, funkcja straty może być przybliżona funkcją liniową (hiperpłaszczyzną)
	* skalowanie kroku ($\beta$)
* Metoda gradientowa
* Powtarzane dopóki przewidywana klasa się nie zmieni

### Boundary attack
* Atak na czarne skrzynki
	* nie korzysta z gradientu
* Atak z konkretnym celem
	* chcemy zmiany klasyfikacji na konkretną klasę
* Metoda startuje z punktu klasyfikowanego tak jak chce atakujący
* W kolejnych krokach stara się przemieszczać po granicy decyzyjnej i przejść jak najbliżej obrazu wejściowego
	* ślizganie po granicy decyzyjnej
* Wolna optymalizacja, jeśli nie mamy dostępu do gradientu

### Techniki obrony
* Pierwsze, mało skuteczne podejścia
	* dodawanie szumów, dyskretyzacja odpowiedzi - maskowanie gradientów
	* rozszerzyć zbiór uczący o złośliwe dane
	* wykrywanie, czy dany przykład został złośliwie zaburzony
* Złośliwe dane przenoszą się między architekturami i modelami!
	* chyba kwestia podobnych zbiorów treningowych
* Adversarial / robust training
	* inaczej sformułowane zadanie uczenia modelu
	* optymalizuje zachowanie w najgorszym z możliwych przypadków
	* minimalizacja straty przy maksymalnym dozwolonym zaburzeniu (przed takimi chronimy)
	* funkcję celu można tylko przybliżać
	* wplecenie ataków do procesu uczenia modeli
	* znacznie wydłuża uczenie
