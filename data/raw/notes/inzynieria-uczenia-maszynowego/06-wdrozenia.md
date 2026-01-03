# Wdrożenia

## Użycie jednokrotne vs wdrożenie
* Model użyty jednokrotnie
	* odpowiedź na konkretne pytanie / wygenerowanie predykcji
	* prawdopodobnie autor modelu będzie generować predykcje
	* całym projektem zajmuje się ten sam zespół
	* dane zebrano wcześniej
	* krótki cykl życia
	* przez cały cykl życia modelem zajmuje się człowiek
	* działanie w środowisku statycznym
* Gdy model będzie wdrożony
	* jest tylko jednym z elementów środowiska
	* zależy od innych elementów
	* każdy element może ulec awarii i powodować problemy
	* większa potrzeba automatyzacji
	* może osoby, które nie są autorami i nie mają kompletnej wiedzy o założeniach będą korzystać z modelu
	* dane mogą się zmieniać w czasie
	* możliwe że będzie modyfikowany po długim okresie
	* działanie w środowisku dynamicznym

## Środowisko dynamiczne
* Model ma wpływ na środowisko zewnętrzne
* Po wdrożeniu model trzeba będzie co jakiś czas odświeżać
* Predykcje generowane dzisiaj mogą wpłynąć na dane zebrane jutro
* Sprzężenie zwrotne

## Typowe składniki systemu korzystającego z UM
* Bazy danych
* Indeksy wyszukiwania
* Serwisy korzystające z predykcji
* Komponenty zarządzające zasobami (scheduler)
* Szyny / kolejki do przesyłania danych
* Elementy związane z bezpieczeństwem
* Inne modele
* Ludzie

## Problemy z atrybutami wejściowymi
* Model ma silne założenia co do rozkładu danych wejściowych
* Dobra publikacja o długu technicznym w uczeniu maszynowym

### Niestabilne atrybuty wejściowe
* Mogą się zmieniać z czasem
* Trendy, sezonowość, ewolucja samego zjawiska
* Inne moduły systemu mogą ewoluować
	* nowe wersje modeli
	* nowe wartości słownikowe
	* poprawki, optymalizacje, wersje bibliotek

### Zanikające korelacje
* Mamy dwa atrybuty skorelowane z $y$ i ze sobą nawzajem
* Korelacja nie oznacza związku przyczynowo-skutkowego
* Może do modelu wybierzemy $x_1$, a naprawdę przyczyną było $x_2$

### Przecieki informacji
* Zazwyczaj zakładamy aktualność i dostępność atrybutów wejściowych
* Przykład
	* przewidujemy temperaturę następnego dnia
	* w zebranym zbiorze danych mamy atrybut - ciśnienie z następnego dnia
	* w statycznym zbiorze danych da się to zebrać ale działając na bieżąco tego nie będzie
* Przykład
	* przewidywanie czy klient dokona zakupu
	* w danych wejściowych są odwiedzone podstrony sklepu
	* proces zbierający dane ignoruje strefy czasowe
	* mamy atrybut mówiący o odwiedzeniu strony podziękowania za zakup
* Co zrobić z atrybutem
	* usunąć
	* wziąć predykcję
	* wzięć wartość bez przesunięcia jeśli jest
* Przyczyny
	* niezrozumienie dziedziny
	* zaokrąglenie znaczników czasowych
	* nieuwzględnienie możliwych opóźnień
	* strefy czasowe / dziwne operacje na znacznikach czasowych

## Problemy z atrybutami wyjściowymi

### Użytkownicy modelu
* Mogą mieć błędne założenia odnośnie predykcji
* Nie zawsze wiemy kto i do czego będzie korzystał z modelu
* Zmieniając model wpływamy na działanie innych elementów systemu

### Kaskady korekt
* System B korzysta z A, C z B, ...
* Zmiana w jednym modelu wpływa na kolejne
* Brak synchronizacji w zmianach modeli
	* ważne żeby zespoły utrzymujące modele komunikowały się między sobą

### Ukryte sprzężenia zwrotne
* Działający model może wpływać na dane, na których będzie trenowany w przyszłości
* Sprzężenie może być wzmacniane przez inne systemy

## Pożądane cechy infrastruktury
* Dostęp do informacji diagnostycznych (logi)
* Automatyczna weryfikacja kluczowych miar i monitorowanie
	* właściwości danych
	* zależności wejściowych
	* jakość generowanych predykcji
	* metryki techniczne
* Wdrożenia na części ruchu
	* przeprowadzanie testów A/B
* Szybkie wycofanie modelu
