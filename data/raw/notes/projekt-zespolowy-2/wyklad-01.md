# (2024-10-11) Analiza wymagań

## Proces wytwarzania oprogramowania
* Analiza wymagań
	* zebranie i uporządkowanie wymagań użytkownika oraz określenie, co system będzie robił by je spełnić
	* jak system będzie wyglądać dla końcowego użytkownika
	* wymagania systemowe
* Projektowanie
	* odwzorowanie wymagań w konstrukcję systemu, czyli określenie jak system będzie realizowany
	* dobranie architektury, struktury oprogramowania, środowiska implementacji
* Implementacja
	* zbudowanie działającego systemu
* Testowanie
	* sprawdzanie poprawnośi działania i usuwania błędów
* Wdrożenie i pielęgnacja
	* instalacja oprogramowania
	* dalsze utrzymanie
	* usuwanie błędów
	* wprowadzanie zmian
	* utrzymanie często trwa dużo dłużej niż wytwarzanie

## Klasyfikacja wymagań

### Użytkownika i systemowe
* Wymagania użytkownika
	* to co mówi użytkownik
	* klient mówi czego chce
	* nie ma wystarczających szczegółów, żeby na ich podstawie zrealizować system
	* formułowane przez osobę, która nie jest ekspertem od wytwarzania oprogramowania
* Wymagania systemowe
	* szczegółowe
	* z jednego wymagania użytkownika może wynikać wiele wymagań systemowych
	* formułowane przez osobę świadomą aspektów wytwarzania oprogramowania

### Wymagania funkcjonalne i niefunkcjonalne
* Wymagania funkcjonalna
	* funkcje jakie realizuje system
	* np. system powinien księgować wszystkie wpłaty i wypłaty na koncie klienta
* Wymagania niefunkcjonalne
	* własności, jakie system musi spełniać
	* wymagania jakościowe
	* niezawodność (np. średni bezawaryjny czas pracy)
	* wydajność (np. średni czas zrealizowania transakcji)
	* pielęgnowalność (np. istnienie odpowiedniej dokumentacji)
	* przenośność (np. działa na Windowsie i na Macu, na arm i x86)
	* bezpieczeństwo

Analizę wymagań przeprowadza się w sposób iteracyjny. Pojawiają się wątpliwości, które trzeba rozwiązać.

### Wymagania zgodności
* Compliance requirements
* Trudne do sklasyfikowania jako funkcjonalne lub niefunkcjonalne
	* mogą się jasno przekstzałcić w jedne albo drugie w toku analizy
* Zgodność z regulacjami prawnymi
* Zgodność ze standardami
* Zgodność ze zwyczajami

## Modelowanie wymagań

### Proces biznesowy
* Ciąg czynności o określonym rezultacie
* Modele
	* diagram aktywności UML
	* notacja BPMN
* Działanie firmy można przedstawić jako zbiór procesów biznesowych

### Unified Modeling Language
* Standard do modelowanie bardzo różnych rzeczy
* Diagramy modelowania struktury (statycznych spektów)
	* np. diagram klas
* Diagramy zachowania
	* pokazują jak coś się zmienia w czasie
	* np. diagram sekwencji
* Przykłady diagramów
	* przypadków użycia - aktorzy i funkcjonalności systemu
	* klas
	* stanów
	* sekwencji - wymiana komunikatów między obiektami
	* komponentów
	* wdrożenia - fizyczna infrastruktura
	* aktywności - podobny do BPMN

### Modelowanie procesów biznesowych (diagram aktywności UML)
* Początek
* Koniec
	* rozróżnienie na zwykły koniec i koniec z niepowodzeniem
* Czynności (zaokrąglony prostokąt)
* Obiekt lub zbiór obiektów (prostokąt)
	* np. datastore - niezależny od użytej technologii
* Rozwidlenia i zejścia (równoległe)
	* czynności wykonywane współbieżnie
	* w punkcie zejścia następuje czekanie
* Rozejście i zejście warunkowe
* Sygnał
	* przychodzi do procesu z zewnątrz
	* generowane przez proces
	* upłynięcie czasu też może być sygnałem
* Notatka / komentarz (prostokąt z zagiętym rogiem)
	* połączony z elementem przerywaną linią
* Łącznik (litera w kółku)
	* odnośnik do innego miejsca
	* dla wizualnego podziału diagramu
* Stereotypy
	* etykieta doprecyzowująca znaczenie elementu
	* mechanizm rozszerzenia UML
	* definiowany przez osobę modelującą
	* znaczenia trzeba wytłumaczyć w dokumentacji
	* notacja `<<nazwa stereotypu>>`
* Modelowanie odpowiedzialności w postaci torów
	* podział między osoby / działy
	* tory (swimlane)
	* poziome lub pionowe tory
	* nazwa / rola odpowiedzialna za dane czynności
* Modelowanie odpowiedzialnosci w postaci boksów
	* prostokąty grupujące czynności, rozgałęzienia itd.

