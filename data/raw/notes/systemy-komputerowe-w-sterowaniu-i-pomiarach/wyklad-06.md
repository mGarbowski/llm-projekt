# Proces projektowy (2024-03-25)

## Realizacja systemu wbudowanego
1. analiza wymagań
2. projektowanie systemu
3. projekt wstępny (oprogramowania)
4. projekt szczegółowy (oprogramowania)
5. ...


Chodzi o to żeby system i spełniał wymagania i był odpowiednio tani.
Problemem jest to że zaczynamy nie wiedząc do końca jaka będzie implementacja
Na początkowych etapach ustala się co będzie realizowane programowo a co sprzętowo

Przykład sterowania osprzętem sali wykładowej (rozwijany ekran, oświetlenie główne sterowane płynnie, sterowanie pomocnicze włączone/wyłączone)

Generalnie PWM jest preferowany nad użycie przetwornika analogowo-cyfrowego (jest tańszy, bardziej odporny na zakłócenia)


## Analiza wymagań
Analizujemy jakie będą wejścia i wyjścia mikrokontrolera

Obsługa stanów nienormalnych
* jednocześnie sygnał do zwinięcia i rozwinięcia ekranu - wyłączenie silnika
* brak sygnalizacji zwinięcia / rozwinięcia ekranu po 12s - wyłączenie silnika

### Lista zdarzeń
1. Rozwiń ekran
2. Zwiń ekran
3. ...

Ustalamy reakcję systemu na zdarzenia - tabelka, reakcja typowa, alternatywna, brak reakcji

Model zachowania można wyrazić jako maszynę stanów (automat skończony). Z odpowiedzi opisanych w tabeli może nie być jednoznacznie ustalony


### Ograniczenia czasowe
Może wynikać z fizycznych właściwości instalacji lub z interakcji z człowiekiem

Np. 
* Czas reakcji na sygnał rozwinięcia lub zwinięcia przycisku
	* szybkość rzowijania ekranu
	* odległość czujnika od końca ekranu
	* droga hamowania ekranu
	* zwłoka wyłączenia silnika
* Czas reakcji na naciśnięcie przycisku

## Projektowanie systemu
* co można realizować programowo a co sprzętowo

### Projekt sprzętu
* Wybór mikrokontrolera
* Projekt sprzęgu procesowego - połączenie instalacji z mikrokontrolerem
	* np. optoizolacja wejść i wyjść, zasilanie, wzmacniacz
* Projekt płytki
	* złącza
	* rozmieszczenie elementów
	* projekt druku

Mikrokontroler CISC - jedna instrukcja nie przekłada się na jeden takt zegara

## Projekt wstępny
Dodanie do tabeli reakcji na zdarzenia ograniczeń czasowych
Można podzielić je na grupy, które będą przypisane do zadań

Problem - jednocześnie trzeba reagować na zdarzenia i generować falę PWM (o zadanym wypełnieniu)

Do generowania PWM o częstotliwość 1kHz można wykorzystać timer i rejestr (licznik), który ulega przepełnieniu co odpowiednią do częstotliowści zegara 


### Szeregowanie zadań
* Problematyczne bo jeszcze nie znamy implementacji
* Określona długość ścieżki w kodzie 
	* liczba instrukcji C w danej ścieżce (tylko wybranej gałęzi if-a)
* Trzeba policzyć liczbę instrukcji asemblerowych w wynikowym kodzie i uwzględnić maksymalny czas wykonywania (ile taktów zegara na instrukcję, jakie taktowanie zegara)
* Część zadań wykonywanych w pętli głównej, część w przerwaniach

warunek z inkrementacją i przepełnieniem - spowolnienie wykonywania instrukcji w ifie 256 razy

to jak rejestruje się procedurę obsługi przerwania zależy od platformy

W przykładowym kodzie jest hazard jeśli przerwanie wystąpi na końcu impulsu sygnału PWM
Można zabezpieczyć się przez wyłączenie przerwań (EA = 0, EA=1)