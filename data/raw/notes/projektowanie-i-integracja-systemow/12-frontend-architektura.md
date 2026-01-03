# Architektura aplikacji frontendowych (2025-01-20)

## Silniki i moduły

### Silnik javascript
* Program odpowiedzialny za wykonywanie kodu JS
* interpretuje
* garbage collection
* optymalizacja
* Etapy
	* parsowanie kodu źródłowego -> AST
	* kompilacja kodu JIT, AST -> kod maszynowy
	* wykonanie kodu - silnik śledzi najczęściej używane fragmenty (hot paths)
	* automatyczne zarządzanie pamięcią (garbage collection)
	* optymalizacja w trakcie działania - silnik analizuje wykonywany kod i stosuje optymalizacje w czasie rzeczywistym

### Silniki JS
* V8
	* Chrome
	* Node
	* Deno
	* napisany w C++
* SpiderMonkey
	* Netscape
	* Firefox
	* pierwszy silnik JS
* JavaScriptCore (Nitro)
	* Apple, Safari
	* BunJS
	* optymalizowany pod macOS
* Chakra
	* Microsoft, Edge (dawniej)

### Funkcje optymalizacyjne
* Inlining - wbudowanie wywołań funkcji do kodu
* Garbage Collection
* Speculative Optimization - przewidywanie typów danych i optymalizacja

### Przyszłość silników
* WebAssembly
	* komplementarny do JS
	* wsparcie dla wydajnych aplikacji (gry, narzędzia obliczeniowe)
* Zwiększona wydajność
	* ulepszenia w JIT
	* lepsza obsługa wielordzeniowych procesorów
* Nowe standardy ECMAScript

### WebAssembly
* Niskopoziomowy format kodu binarnego przeznaczony do uruchamiania w przeglądarkach internetowych
* Zaprojektowany z naciskiem na wydajność
* Na wszystkie platformy wspierające JS
* Prędkość zbliżona do natywnej
* Obsługuje wiele języków
	* C, C++, Rust, Python, Go
* Zgodny z zasadami bezpieczeństwa przeglądarek
* Istotny krok w rozwoju technologii webowych

### AMD
* Asynchronous Module Definition
* Standard definiowania modułów
* Zaproponowany przez Adobe
* Popularność spada na rzecz ES Modules
* Moduły są ładowane asynchronicznie
* Używane głównie w starszych aplikacjach webowych
	* RequireJS

### Require.js
* Pierwsza próba rozwiązania problemu zarządzaniem zależnościami JS w przeglądarce
	* konflikty nazw
	* prawidłowa kolejność ładowania skryptów
* Część interfejsów tożsama ze specyfikacją CommonJS

### CommonJS
* Standard ujednolicający system modułów w JS
* Wykorzystywany przede wszystkim do NodeJS
	* przeglądarki nie wspierają CommonJS same z siebie
	* trzeba użyć transpilerów
* `require`, `module.exports`
* Moduł najczęściej tożsamy z jednym plikiem

### ES Modules
* Część standardu ecmascript
* `import`, `export`

### Porównanie CJS i ESM
* ESM
	* nowsze
	* frontend i backend
	* wszystkie importy są asynchroniczne
	* obsługuje `import`, `await`, `async`
* CJS
	* wykorzystywane w tradycyjnych serwerach NodeJS
	* moduły ładowane synchronicznie
	* problematyczne w dużych asynchronicznych operacjach
* Trudne stosować oba w jednym projekcie

## MVC, Flux, Redux, MVVM

### Globalne zarządzanie stanem
* Pojedynczy obiekt globalny dostępny do odczytu i zmiany z dowolnej części naszej aplikacji
* Problematyczne dla architektury aplikacji
* Scentralizowane, wszystko w jednym miejscu
* Przydatne gdy dane są potrzebne wielu komponentom
	* zapewnia że komponenty mają najbardziej aktualne wersje
	* komponenty nasłuchują na zmiany i odświeżają się
* Unika się jawnego przesyłania danych między komponentami

### Kiedy wawrto używać globalnego zarządzania stanem
* dane są współdzielone między komponentami (koszyk w ecommerce, język)
* złożone zależności pomiędzy komponentami
	* prop drilling w React
	* trzeba przekazywać dane przez wiele poziomów pośrednich
* stan jest często modyfikowany
	* globalny stan pozwala utrzymać spójność
	* np. system powiadomień
* zapytania asynchroniczne i ich stan
	* kontrowersyjne
* zarządzanie stanem interfejsu użytkownika
	* modale, toasty, spinnery
* wymóg spójności danych
	* jedna zmiana wpływa na wiele komponentów

### Kiedy nie używać
* Małe aplikacje
	* wystarczy lokalne zarządzanie stanem
* proste aplikacje bez złożonej logiki
* dane są izolowane
	* specyficzne per komponent

### MVC
* Wzorzec architektoniczny dedykowany aplikacjom GUI
* Zaprojektowany przez Xerox w 1979
* Odseparowanie modelu (reprezentacji danych) od widoku (interfejs użytkownika)
* Za logikę w aplikacji odpowiada kontroler
* Wykorzystywany we frameworkach
	* Django, Ruby on Rails, Angular, ...
* Nadal popularny na frontendzie
* Model reprezentuje wiedze
	* może być pojedynczym obiektem lub strukturą obiektów
	* odpowiada za logikę biznesową
	* całą wiedza na temat danych w aplikacji
	* dane stają się niezależne od ich pochodzenia
* Widok
	* wizualna reprezentacja modelu
	* to co widzi użytkownik
	* zmiana wyglądu bez konieczności zmiany logiki
	* nie musi zakładać pełnego gui (np. linia poleceń)
* Kontroler
	* logika aplikacji
	* przetwarzranie, przekształcanie danych z modelu
	* przekazanie danych do widoku
	* odbiór danych od użytkownika

### Problemy z MVC w aplikacjach frontendowych
* Warstwa logiki pozostaje na serwerze
* Mamy tylko dwa punkty styku - request, response
* W przypadku aplikacji CSR, kontroler jest mocno uzależniony od widoku
* Widok i kontroler tworzą dwukierunkowe powiązania
* Przeładowane modele
	* i dane interfejsu użytkownika i stan aplikacji
* Złamanie SRP
	* kontroler obsługuje zdarzenia i logikę biznesową
	* model nie ma rozdzielenia zarządzaniem stanu interfejsu od stanu aplikacji

### Two way data binding
* Angular, Vue
* Zakłada dwukierunkowy przepływ danych widok-model
* Nie skaluje się
	* trudne do utrzymania relacje many-to-many
	* ilość relacji niekontrolowanie wzrasta

### The zombie unseen messages count
* casus w Facebooku
* często powtarzający się bug

### One way data binding
* Przepływają tylko w jednym kierunku
* Np. w React od rodzica do dziecka
* Najczęściej wyświetlanie danych z modelu w widoku

### Architektura FLUX
* Wzorzec projektowy CQRS
* Jednokierunkowy przepływ danych
* Akcje są jedynym sposobem na zmianę stanu aplikacji
* dispatchery przekazują akcje do magazynu
* magazyn jest jedynym źródłem prawdy
* stan aplikacji jest pobierany z magazynu, przekazywany do widoku
* aplikacja może mieć wiele magazynów
* jeśli jest wiele magazynów
	* dispatcher wysyła do każdego
	* to magazyn będzie wiedział czy akcja dotyczy jego
	* magazyn jest odpowiedzialny za specyficzną domenę
* magazyn emituje zdarzenia do widoku controller-view odpowiedzialnego za propagację zdarzeń do pozostałych widoków
	* przerenderowanie całego drzewa
* Zalety
	* proste i wydajne wykrywanie zmian
	* wystarczy porównać stary obiekt stanu z nowym
	* w idealnym wdrożeniu architektury stosuje się niemutowalne struktury danych
	* daje kontrolę nad danymi, pozwala na modularne zarządznaie nimi
* Wady
	* skomplikowana i trudna w opanowaniu
	* wymaga dużego nakładu przy wdrożeniu i utrzymaniu

### Czy flux to nowe mvc
* logika rozproszona na wiele magazynów może być tożsama z wieloma kontrolerami
* ...

### Redux
* Implementacja architektury Flux
* Jeden magazyn (jedno źródło prawdy)
* niemutowalny stan
* magazyn nie moyfikuje danych
* logika aktualizacji stanu jest wydzielona do reduktorów
* akcja
	* obiekt posiadający właściwość type
	* informacje niezbędne do wykonania zmiany na magazynie
	* opcjonalny `payload`
* kreator kacji
	* funkcja zwracająca akcji
	* uproszczony zapis
	* parametryzacja
* jakie typy danych można umieścić w akcji
	* nie nakłada żadnyhc dodatkowych ograniczeń
	* obiekty serializowalne za pomocą `JSON.stringify`
* dispatcher
	* funkcje, które pozwalają na wyemitowanie akcji do magazynu
	* efektem jest wywołanie reducera i aktualizacja magazyna
	* jedyny sposób na przekazanie danych w celu aktualizacji stanu
* reduktor
	* czysta funkcja
	* wywoływana z aktualnym stanem i akcją
	* zwraca nowy stan
	* jeśli nie wie jak obsłużyć akcję, zwraca niemodyfikowany stan
	* nie powinien mutować otrzymanego stanu
	* jedyna opcja zmiany stanu
* czyste funkcje
	* nie korzystają ze zmiennych globalnych
	* nie modyfikują danych zewnętrznych
	* nie mają efektów ubocznych
	* zawsze ten sam wnyik dla tych samych argumentów
* stan początkowy
	* ...
* magazyn
	* scentralizowany
	* jeden obiekt JS
	* jendokierunkowy przepływ danych
	* zmiana tylko przez reducery
	* stan jest niemutowalny, każda zmiana tworzy nowy obiekt
	* komponenty aplikacji mogą subskrybować na zmiany stanu
	* struktura drzewiasta
	* przyjmuje reducer przy tworzeniu
	* można wyciągnąć typ stanu aplikacji przez `ReturnType<...>` w TS - przydatne do selektorów
* preloaded state
	* stan inicjujący
	* przydatny, gdy chcemy przywrócić sesję, najpierw pobrać dane z serwera
* provider
	* komponent z `react-redux`
	* udostępnia magazyn całej aplikacji

### Architektura aplikacji redux
* Warianty
	* containers, components
	* slices
	* duck duck pattern
* Staramy się odseparować redux os reszty aplikacji
* Warto zadbać o odpowiednią strukturę katalogów

### Components i containers
* Komponenty logiki
	* containers
	* pobierają dane z reduxa i przekazują dalej przez props
* Komponenty widoku
	* nie powinny mieć nic wspólnego z reduxem
	* przyjmują dane od rodziców

#### Architektura
* src
	* store
		* actions
		* selectors
		* reducers
	* app
		* components
		* containers
		* contexts
	* utils

### Duck duck pattern
* Przechowywanie całego kodu redux dla określonej domeny w jednym pliku
	* plik zwany *kaczką*
* Zalety
	* uproszczona struktura kodu - kod reduxa w jednym miejscu
	* wspomaga reużywalność

#### Architektura
* src
	* ducks
		* todos
		* user
		* timer

### Struktura projektu feature-based
 * Aplikacja dzieli się na domeny / funkcjonalności
 * każdy feature zaiwera własne reducery, akcje, komponenty, widoki
 * Funkcjonalności nie przenikają się między sobą

### Slices
* Podział aplikacji na domeny biznesowe
* Łatwa w implementacji z wykorzystaniem `redux/toolkit`
* Dzieli się główny reducer na mniejsze części (slices)

#### Architektura
* arc
	* app
		* hooks
		* slices
		* store
	* features
		* user
		* todos
		* times
	* utils

Redux pozwala na pisanie reducerów tak jakby stan był mutowalny (a nie jest)


## MVVM
* Architektura aplikacji desktopowych i webowych
* Model-View-ViewModel
* np. w Angular
* Zalety
	* oddzielenie warstw
	* testowanie logiki biznesowej niezależnie od interfejsu użytkownika
* Model
	* dane i logika biznesowa
	* przechowuje i zarządza stanem aplikacji
	* np. klasa USER
* View
	* interfejs użytkownika
	* interakcja, kontrolki, formularze
* ViewModel
	* pośrendik między modlee i widokiem
	* logika prezentacyjna - mapowanie, transformacja danych
	* pobiera dane z modelu, przygotowuje do wyświeltenia na widokiu

### Różnica między MVC a MVVM
* ...

## Mikrofrontendy

### Aplikacje monolityczne
* tradycyjny sposób budowy oprogramownaia
* system implementowany w kontekście jednej aplikacji
* problemy z elastycznością i skalowaniem
* niski próg wejścia dla progrmaistów
* prostszy i krótszy development
	* jeśli nie pracuje nad tym zbyt wiele osób
* jeden błąd może zatrzymać całą aplikację
* nie każdy monolit jest zły
	* zależy od kontekstu biznesowego

### Monorepo
* Jedno repozytorium z jednym projektem
* rozdzielenie serwisów polega nie wydzieleniu wielu aplikacji w jednym repozytorium
* musi istnieć aplikacja nadrzędna, która spina mniejsze serwisy
* problemy z wyizolowaniem zależności w różnych wersjach
* idealne gdy wszystkie projekty używają tego samego języka i tych samych technologii
* narzędzia
	* **yarn workspaces**
	* nx
	* turborepo
	* lerna
* idealne dla projektów o dużej skali gdzie różne części muszą być ze sobą ściśle zintegorwane

### Mikroserwisy
* systemy rozproszone, dzielone wg funkcji biznesowych
* bardziej skomplikowana architektura
* trudne do wprowadzenia zmiany jesli objemuja wiele uslug
* niezależne skalowanie uslug od siebie
* blad w jednym serwisie nie ubija calej aplikacji
* wieksza kontrola nad dlugiem technologicznym

### iframe
* Stara technologia
* Jedna apikacja zbiorcza, w niej umieszczamy mikroaplikacje
	* każda w osobnym iframe
* Można tam załadować cokolwiek
* Są od siebie odizolowane
	* style nie wpływają na siebie
* Problematyczne jest zapewnienie komunikacji między iframe'ami
* Komunikacja
	* postMessage
	* query params w URL - z aplikacji nadrzędnej do iframe
* Trudno zapewnić accessibility
* Problem wydajnościowy
	* tak jak oddzielna zakładka

### WebComponents
* Znacznie nowsze podejście
* Natywna enkapsulacja drzewa dom
	* wykorzystanie shadow dom
* bardziej podatne na zmiany z zewnątrz
* rozwiązanie natywne, też proste we wdrożeniu
	* nie wymaga zewnętrznych bibliotek
* shaodw dom
	* wyizolowanie czesci dom
	* pozwala na oddzielenie stylow, zawartosci i interakcji od glownego dokumentu DOM

### Single SPA
* framework do komponowania roznych aplikacji frontendowych

