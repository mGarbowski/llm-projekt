# Modelowanie procesów biznesowych
Proces - zbiór działań przetwarzających surowce lub informacje w wyjściowe produkty lub informacje

Fundamentals of Business Process Management

## APQC
Framework klasyfikacji procesów

### Procesy operacyjne
* opracowanie wizji strategii
    * mało skomputeryzowane
    * systemy do monitorowania realizacji strategii
* rozwój, zarządzanie produktami i usługami
    * systemy MRP, MRPII
* marketing i sprzedaż
* zaopatrzenie, produkcja, dostawy
* obsługa klientów

### Procesy zarządzania i wspomagania
* zarządzanie zasobami ludzkimi
* zarządzanie systemami informacyjnymi
* zarządzanie zasobami finansowymi
* nabywanie, budowa i zarządzanie mieniem
* zarządzanie ryzykiem, zgodność z regulacjami
* zarządzanie relacjami zewnętrznymi
* zarządzanie wiedzą, doskonaleniem i zmianami


## Składowe procesu biznesowego
* Aktorzy
    * Klient
* Obiekty
* Zdarzenia
* Aktywności
* Punkty decyzyjne
* Wyniki

## Cykl życia procesu
* Identyfikacja procesu
    * widzimy potrzebę budowy jakiegoś procesu
    * reorganizacja firmy, wzorowane na gotowcach
* Odkrywanie procesu
    * tworzenie iteracyjne
    * na podstawie informacji zwrotnej od klientów
* Analiza
* Przeprojektowanie
* Implementacja
* Monitorowanie
    * ważne
    * średni czas obsługi, liczba zleceń itd.
    * można je zasymulować


## BPMN
* Business Process Model and Notation
* Graficzna notacji opisująca procesy biznesowe
* Ustandaryzowana, aktualnie w wersji 2.0

### Typy modeli
* Procesy
* Choreografie
* Współpraca

### Typy obiektów
* Węzły przepływu (flow nodes)
    * czynności
    * zdarzenia
    * bramki - elementy decyzyjne
* Połączenia (connecting objects)
* Miejsca realizacji procesu
    * baseny i tory (pools, swimlanes)
* Obiekty danych (data objects)
* Artefakty (artifacts)
    * elementy graficzne niebędące elementami przepływu
    * informacje uzupełniające
    * można definiować własne
    * adnotacje, grupy, powiązania
* Dekoratory (decorators)
    * odwzorowanie wzorców zachowań
    * komunikat (message)

### Analiza przepływów - token
Standard BPMN rozważa analizę przepływów z wykorzystaniem tokenów (żetonów).

Zdarzenie w systemie generuje żeton, analizujemy co dzieje się z żetonem, czy dojdzie do
przewidzianego punktu końcowego. Pojęcie z symulatorów zdarzeń dyskretnych. Token powstaje w zdarzeniu początkowym i dochodzi jakąś ścieżką do zdarzenia końcowego, w którym jest konsumowany.

### Podstawowe typy obiektów aktywnych
* Zdarzenie - kółko
    * początkowe / pośrednie / końcowe
    * może być wyzwalane czasowo
    * może być wyzwalane przez wiadomość
    * ogólne
    * wysłanie / odebranie wiadomości
    * reguły
    * czas
    * anulowanie / zerwanie
    * wyjątek / usterka
    * kompensaja
    * przerywające / nieprzerywające wątki procesów
    * przyczyny działań (catching)
    * skutki działań (thrownig)
* Zadanie (task) - zaokrąglony prostokąt
* Bramka logiczna (gateway) - romb

### Bizagi modeler
* Komercyjny program
* Darmowa wersja

## Zdarzenia

### Wiadomość
* Może być zdarzeniem rozpoczynającym proces
    * złożono zamówienie
* Może być na końcu procesu
    * poinformowanie klienta o zrealizowanym zamówieniu

### Kompensacja
* Cofnięcie aktywności (rollback)
* Np. cofnięcie rezerwacji hotelu po nieudanym zakupie biletów

### Link
* Do uproszczenia diagramu
* Kontynuacja diagramu w innym miejscu

### Sygnał
* Wiadomość musi mieć odbiorce i nadawcę
* Sygnał ma listę odbiorców

### Warunek
* Jako zdarzenie
* Związane z taskiem
* Przerywające / nieprzerywające


### Eskalacja
* Podjęcie określonych czynności żeby przywrócić system do stanu normalnego
* Np. powiadomienie administratora


## Zadania
* Symbolizowane przez prostokąt
* Dodatkowe tryby
    * zapętlone
    * ad hoc
    * wiele instancji
    * kompensacja
* Typy zadań
    * service - usługa sieciowa lub zautomatyzowana aplikacja
    * receive - oczekiwanie na komunikat
    * send - wysłanie komunikatu
    * user - zadanie wykonywane przez człowieka wspieranego przez aplikację
    * manual - zadanie wykonywane przez człowieka bez pomocy komputera
    * script - zadania wykonywane przez system
    * reference - odwołanie do już zdefiniowanych zadań

## Bramki
* Symbolizowana przez romb
* XOR
    * wykluczająca, sterowana danymi
    * token może pójść tylko jedną ścieżką
    * wykluczająca, sterowana zdarzeniami - zdarzenie określa którą ścieżką pójdzie proces
* OR
    * żeton może pójść jedną lub wieloma ścieżkami
* AND
    * żeton może przejść dalej przy spełnieniu wszystkich warunków

## Połączenia
* Przepływ (normal sequence flow)
* Przepływ warunkowy
* Przepływ (default sequence flow)
* Błąd (message flow)
* Asocjacja

### Prezentacja graficzna
* Linia ciągła - przebieg procesu
	* token podąża po liniach ciągłych
* Linia przerywana - przebieg komunikatu
* Linia kropkowana - powiązanie, asocjacja

## Partycje i tory
* Baseny i tory
* Między basenami strzałki przerywane
* Zazwyczaj basen oznacza czynność (proces), a tory aktorów w tym procesie


## Artefakty
* Pomocnicze informacje dotyczące procesów
* Opisy tekstowe
* Grupowanie zadań
* Obiekty danych
    * Informacja że coś jest w bazie danych
    * Dane wejściowe
    * Dane wyjściowe
* Asocjacje
	* Połączenie między artefaktami a obiektami BPMN


## Typy diagramów 
* Diagramy procesów
* Diagramy współpracy (baseny, przepływy wiadomości)
* Diagramy konwersacji (baseny, konwersacje i linki konwersacji)

### Proces biznesowy prywatny
* Wewnętrzny dla organizacji
* Nie jest dostępny dla aktorów zewnętrznych
* Modelowany w ramach jednego basenu
* W organizacji modeluje się wiele procesów wewnętrznych

### Proces biznesowy publiczny
* Pokazuje interakcję między procesem wewnętrznym a innym procesem lub aktorem 
* Pokazuje, że jest interakcja ale nie interesuje nas jakie dokładnie czynności są wykonywane
	* np. nie wiemy jak wygląda struktura procesu po drugiej stronie
	* po drugiej stronie modelujemy tylko przepływ komunikatów

### Proces współpracy
* Pokazuje współpracę między procesami, pokazuje interakcje i wewnętrzne zadania w obu basenach
	* zadania, przebieg procesu po obu stronach (basenach)
	* komunikaty między basenami
* Choreografia

### Diagram choreografii
* Aktywności to interakcje, wymiany wiadomości
* Modeluje współpracę bez torów, basenów itp
* Pozwala modelować współpracę, której zakres wychodzi poza granice organizacji

### Konwersacja
Diagram wysokopoziomowego modelu wymiany informacji między systemami

## Symulacje
* Pomagają określić np. ile osób należy przydzielić do odpowiednich zadań
    * Parametryzuje pensje, liczby pracowników, czasy wykonywania zadań
* Analizują przepływ tokenów w modelu
* Np. narzędzie BIMP

## Process Mining
* Zbiera się dane o istniejących procesach
* Analiza średnich czasów obsługi itp
* Element optymalizacji (właściwie poprawy wydajności)

## Narzędzia do modelowania
* BizAgi
* Aris
* Enterprise architect
