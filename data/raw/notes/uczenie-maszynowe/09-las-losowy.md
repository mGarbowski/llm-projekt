# Las losowy

## Modelowanie zespołowe
* Model składa się z wielu modeli
* Z jednego zbioru trenującego budujemy wiele modeli
* Na podstawie predykcji modeli składowych wyłaniamy ostateczną predykcję modelu $h_{1:m}$
* Modele składowe powinny się od siebie różnić
* Modele składowe nie mogą być całkiem złe
* Oczekujemy, że niedoskonałości poszczególnych modeli kompensują się po połączeniu
* Rozwinięcie metody *bagging*

### Bagging
* Bootstrat aggregating
* Wykonujemy wiele zaburzonych kopii zbioru trenującego $T$
* Zaburzenie przez generowanie prób bootstrapowych
	* losowanie ze zwracaniem ze zbioru $T$
	* z reguły losuje się $|T|$ przykładów
	* niektóre przykłady bedą zwielokrotnione, a niektóre nie zostaną wybrane
* Ile przykładów nie zostanie wylosowanych do żadnej próby bootstrapowej
* Jakie jest prawdopodobieństwo, że dany przykład nie zostanie wylosowany
	* $|T|=N$
	* $(1 - 1/N)^N \rightarrow 1/e \simeq 0.368$
	* ok. $37\%$ pierwotnego zbioru nie znajdzie się w próbie bootstrapowej
* Na próbowach bootstrapowych trenuje się różne modele
	* algorytmy różnią się wrażliwością na takie zaburzenia
* Algorytmy niestabilne - większe różnice przy zaburzeniu danych
	* intuicja - w trakcie uczenia podejmowane są dyskretne decyzje, które mogą doprowadzić do skokowej różnicy
	* np. indukcja reguł, drzewa decyzyjne (wybór podziału w węźle)
	* jeśli zmieni się rozkład atrybutów to może zmienić się decyzja co do podziału
* Łączenie predykcji
	* głosowanie, klasa większościowa - ta którą zgłosiło najwięcej modeli
	* klasa najbardziej prawdopodobna - sumowanie prawdopodobieństw pojedynczych predykcji
* Można użyć do regresji
	* uśrednianie predykcji
	* mało typowe rozwiązanie
* Metoda nie daje spektakularnej poprawy

## Las losowy
* Podobny jak bagging ale
	* modele to drzewa decyzyjne
	* budując każde z drzew wprowadzamy dodatkową losowość
* Dzięki losowości modele są bardziej zróżnicowane
	* daje spektakularną poprawę
* W trakcie budowy drzewa, w każdym węźle dokonujemy podziału na losowym podzbiorze atrybutów
	* nie losuje się podzbioru dla całego drzewa tylko każdorazowo w węźle
	* podział na podstawie zysku informacyjnego itd ale najpierw zawężamy zbiór atrybutów możliwych do wybrania
* Jeden z najlepszych w praktyce, bardzo powszechnie stosowany
* Trudno go niepoprawnie użyć
* Mało hiperparametrów
	* opłaca się budować drzewa do oporu - nie wybieramy kryterium stopu (dla pojedynczego drzewa niekoniecznie najlepsze ale tu chcemy zróżnicowanych drzew)
	* bez przycinania
	* liczba drzew - raczej im więcej tym lepiej, ogranicza nas czas na obliczenia (100, 200, 500)
	* jak duże podzbiory atrybutów losować - popularne heurystyki $\sqrt{n}, \log n$
* Można wyznaczać prawdopodobieństwa przewidywanych klas
	* rozkład głosów przy głosowaniu
