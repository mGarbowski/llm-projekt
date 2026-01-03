# Frameworki frontendowe w kontekście budowania aplikacji web (2025-01-13)

## Frameworki
* Zestaw bibliotek i narzędzi ułatwiających budowę aplikacji webowych
* Usprawnia pracę zespołową
* Zarządzanie złożonością dużych projektów
* Gotowe rozwiązania dla typowych problemów
	* routing
	* stan aplikacji

### Rodzaje
* Komponentowe
	* React
	* Vue
* Kompleksowe
	* Angular
	* Svelte
* Wyspowe
	* Astro
	* Qwik
	* Eleventy

### React
* Metaframeworki oparte o React (Next.js)
* Bardziej biblioteka niż framework
* JSX
* Bogaty ekosystem narzędzi
* Stworzony przez Facebook
* Najpopularniejszy z wymienionych ale używany w 4.6% wszystkich stron internetowych

### Vue
* Lekki i łatwy do nauki
* Elastyczny w użyciu
	* biblioteka lub pełny framework
* Wsparcie społeczności

### Angular
* W pełni zintegrowane funkcje
	* routing
	* testy
	* dependency injection
* Google
* Bardziej stroma krzywa uczenia się niż Vue i React
* Tylko Typescript

### Svelte
* Kompilator zamiast runtime
* Generuje czysty kod js
	* eliminuje potrzebę dużych bibliotek w czasie działania
* Bardzo lekki

### Zalety frameworków
* Skrócenie czasu pracy
* Standaryzacja kodu

### Wady frameworków
* Krzywa nauki
* Zależności od konkretnych rozwiązań
* Nadmiar kodu w małych projektach

### Kierunki rozwoju
* Server side rendering
	* Next
	* Nuxt
* Static site generation
	* Jamstack
	* Gatsby
* Bezframeworkowe podejście
	* rosnące zainteresowanie narzędzami z ograniczonym runtime (Svelte)
* Microfrontends
	* rozdzielenie aplikacji na mniejsze moduły

### Jak wybrać framework
* Duże aplikacje
	* Angular, React
* Małe, średnie
	* Vue, Svelte
* Pod kątem SEO
	* Next, Nuxt
	* niekorzystne są SPA
* Do rozważenia zasoby zespołu
	* doświadczenie
	* dostępność programistów
* Społeczność i wsparcie
	* popularne frameworki mają lepszą dokumentację i więcej bibliotek

## Architektura komponentowa
* Aplikacja dzieli się na mniejsze części - komponenty
* Komponenty mogą być wykorzystywane w wielu aplikacjach
* Skraca czas budowy nowych aplikacja i obniża koszty
	* ze względu na reużywanie komponentów
* Poszczególne komponenty mogą powstawać równolegle
* Komponent powinien mieć dobrze wyspecyfikowany interfejs
* Wspiera modyfikowalność aplikacji
	* funkcjonalność skupia się w dedykowanych komponentach
* Spójność (coherence) komponentów wspiera modyfikowalność

## Architektura wyspowa
* Część aplikacji jest statyczna, a część dynamiczna
* Wydzielamy, które elementy będą interaktywne (wyspy)
	* one będą renderowane niezależnie od elementów statycznych
* Główna strona jest wstępnie wygenerowana (jak w SSG)
	* zapewnia szybki czas wczytywania
* Dynamiczne elementy (formularze, karuzele) są ładowane i renderowane indywidualnie po stronie klienta
	* renderowane tylko kiedy są widoczne
* Hydratacja
* Tylko wyspy potrzebują JS

## MPA
* Multi-Page Applications
* Każda podstrona jest osobnym dokumentem HTML ładowanym z serwera
* Serwer zwraca widoki na podstawie żądań
* Przydatne tam, gdzie kluczowe jest SEO ale interaktywność jest minimalna
* Wolniejsze przełączanie się między podstronami

## SPA
* Single Page Applications
* Alternatywa dla MPA
* Serwer zwraca tylko prosty plik HTML
	* najczęściej pojedynczy div i informacje o stylach i skryptach
	* logika budowania aplikacji po stronie klienta
* Serwer jest odciążony, szybkie odpowiedzi
* Problematyczne dla SEO
	* wyszukiwarki nadal słabo sobie radzą ze stronami bez odpowiedniej struktury HTML
* Problem z udostępnianiem treści w mediach społecznościowych
	* meta tags
* Mogą być budowane w sposób modułowy i komponentowy
* Nie ma dużych wymagań od serwera, tylko serwowanie statycznych plików html, css, js

## SSR
* Server Side Rendering
* Nowe MPA
* Aplikacja jes renderowana po stronie serwera na żądanie
	* odpowiedź serwera zawiera częściowo przygotowane widoki
* Lepsze dla SEO
	* można zarządzać znacznikami meta
	* część HTML jest już przygotowana
* Pozwala optymalizować widoki z dużą liczbą komponentów
* Nie jest optymalny gdy mamy niewiele komponentów leniwie ładowanych
* Nie mają dostępu do obiektów typowo przeglądarkowych (np. `window`)
* Nie mogą być łatwo łączone z PWA

## SSG
* Static Site Generation
* Strona budowana tak jak przy podejściu SPA
* opisuje proces kompilacji i renderowania strony
* Powstaje zestaw statycznych plików
* Szybkie i skalowalne
* Next, Gatsby
* Nie jest idealne przy dużych, złożonych aplikacjach
	* potencjalnie bardzo długie czasy budowania

## Podejście hybrydowe
* Łączą różne podejścia (SPA, SSR, SSG) w jednym projekcie
* Dla maksymalizacji wydajności i elastyczności
* Next
* Korzyści
	* optymalizacja SEO
	* elastyczność - dostosowanie do ptrzeb konkretnej strony
	* szybkość ładowania - SSG daję natychmiastową dostępność, a SSR dba o aktualność danych

## PWA
* Progressive Web Applications
* Pozwala tworzyć aplikacji webowe, które działają jak natywne aplikacje mobilne
	* offline mode
	* powiadomienia push
	* szybkie ładowanie
* Najczęściej wykorzystuje SPA
	* dodatkowe możliwości dzięki Service Workers
* Często stosowane w aplikacjach mobilnych

## Meta-frameworki oparte o React
* Rozszerzają możliwości Reacta dodając dodatkowe funkcje
	* SSR
	* SSG
* Przykłady
	* Next
	* Remix
	* Gatsby
	* Expo
	* blitz

## Typescript
* Język programowania
* Nadzbiór Javascript
* Dodaje statyczne i silne typowanie
* Kompiluje się do Javascriptu
* Można go używać z WebAssembly oraz środowiskach takich jak Deno, ts-node
* Wprowadzony przez Microsoft w 2012

### Zalety
* Wyłapuje błędy w kodzie
* Lepsze podpowiadanie ksładni i współpraca z narzędziami
* Łatwiejsza refaktoryzacja
* Sposób na zapisywanie kontraktów

### Wady
* Weryfikacja typoów tylko w czasie kompilacji
* Dodatkowa złożoność dla programistów
* Problematyczne przy bardzo generycznych aplikacjach
* Nie rozwiązuje problemów JSa
* Wymaga doinstalowania kompilatora do środowiska programistycznego

### Dynamiczne typowanie
* Nadawanie zmiennym typów w czasie działania programu
* Zmienne nie posiadają typów przypisanych
* Wartość niesie typ, a nie zmienna
* Javascript, Python, Ruby

### Statyczne typowanie
* Nadawanie zmiennym typów w czasie kompilacji programu poprzez ich deklarację
* Raz badany typ nie może zostać zmieniony
* Wykrywa proste błędy

### Duck typing
* Typ obiektu sprawdzamy na podstawie zawartych w nim pól, a nie deklaracji typu
* Wykorzystywane powszechnie w JS, ale spotykane też w TS

### C# i Java
* ...

### Typescript
* Wkorzystuje typowanie strukturalne
* Lepiej myśleć o typie jako o zestawie wartości
* Nawet jeśli obiekty nie są jednego typu to obiekt spełniający dany interfejs może być użyty nawet tam, gdzie nie było zadeklarowanej relacji

### Kompilacja do Javascriptu
* Sprawdzanie typów przed kompilacją
* System typów jest usuwany podczas przekształcenia AST do kodu JS
* Prawidłowy kod Javascript jest prawidłowym kodem Typescript

### Abstract Syntax Tree
* Abstrakcyjna reprezentacja struktury kodu źródłowego
* Węzły odpowiadają konstrukcjom języka programowania
* Krawędzie łączą węzły w logiczny sposób odwzorowując strukturę kodu

### Proces kompilacji i uruchomienia
* TS source -> TS AST
* AST sprawdzane pod kątem typów
* TS AST -> JS source
* ...

### Mapowanie kodu źródłowego
* Umożliwia tworzenie plików typu sourceMap
* js.map, jsx.map
* Powiązanie pomiędzy kodem js i ts
* Ułatwiają debuggowanie kodu

### Podstawowe typy
* boolean
* number
	* zmiennopozycyjne
* string
	* template string - przekazywanie zmiennych, wielolinijkowe
* symbol
	* gwarantuje unikalność
	* nie są enumerowalne
* bigint
	* dowolnie duże liczby całkowite
	* nie można mieszać z number
* null i undefined
	* nullowalne lub opcjonalne wartości
* Array
	* typ generyczny
	* dwa zapisy `Array<T>`, `T[]`
* tuple
	* skończona lista elementów
* enum
	* zbiór nazwanych wartości
	* domyślnie to kolejne liczby od 0
	* można przypisać napisy
* void
	* brak wartości
	* dla funkcji które nic nie zwracają
* any
	* dowolna wartość
	* zaprzeczenie statycznego i silnego typowania
	* typ nas nie obchodzi (nie oznacza że jest nieznany)
* never
	* wartość, która nigdy nie wystąpi
	* funkcja z nieskończoną pętlą albo zawsze rzucająca wyjątek
	* do wyłapywania sytuacji, które nie powinny się zdarzyć
* unknown
	* nieznany typ
	* można przypisać dowolną wartość, ale nie można nic z niego odczytać
* object
	* wszystko, co nie jest typem prymitywnym
* Object
	* własności i metody, które są wspólne dla wszystkich obiektów w JS
	* używany głównie do dziedziczenia

### type
* Można definiować własne typy
* Też aliasy typów

### interface
* Alternatywny sposób definiowania typu
* Mozna rozszerzać interfejs
* Klasa może implementować interfejs
* Lepsze przy programowaniu obiektowym
* Podlegają mechanizmowi łączenia deklaracji
	* dwa interfejsy o tej samej nazwie zostaną połączone
	* przydaje się do rozszerzania interfejsów z zewnętrznych bibliotek

### Typy generyczne
* Typ generyczny zakłada, że część typu może być sparametryzowana
* Funkcje generyczne, generyczne klasym generyczne interfejsy

### Inferencja
* Mechanizm wnioskowania typów
* TS wnioskuje typy na podstawie przypisania wartości do zmiennej, na podstawie ciała funkcji
* Pozwala unikać wszędzie jawnego podawania typów

### Narrowing
* Mechanizm zawężania typów
* type guards - typeof, instanceof

### Kontrola przepływu
* Analiza przepływu sterowania
* Kompilator na podstawie analizy wnioskuje typy zmiennych
* Umożliwia zawężenie typów zmiennych w określonych blokach

### Typy nominalne
* TS opiera się o typy strukturalne
* Do tej pory nie ma nominalnych typów w TS

### Branding
* Pola prefixowane przez `__`
* `type UserID = number & { __brand: "UserID" };`

### Flavoring
* Jak branding ale pole `__flavor` jest opcjonalne

### Przyszłość Typescript
* W nowym standardzie JS prawdopodobnie pojawi się statyczne typowanie
* Nie jest jedynym systemem typów
	* JSDoc, Flow, LiveScript, CoffeScript, Kotlin/JS

## Nowoczesny CSS
* Największym problemem CSS jest enkapsulacja (jej brak)
* Wszystkie style są traktowane jako globalne

### ICSS
* Interoperable CSS
* Pseudoselektory `:import` i `:export`

### CSS Modules
* Domyślny sposób deklarowania styli w Create React App
* Pozwala na wykorzystnaie preprocessorów (Sass)
* Pliki ze stylami są traktowane jako moduły
* Każdy komponent posiada swój własny plik moduł ze stylami
* Łatwa enkapsulacja styli
	* unikalne id doklejane do nazwy klasy


### JSS
* Nie jest powiązany z żadnym frameworkiem
* Pakiety do łączenia z różnymi frameworkami
* CSS w obiektach JS


### Styled components
* Bazuje na rozwiązaniach JSS
* Tworzenie styli jako komponentów
* Mechanizm tagged templates
* Działają tak jak inne elementy JSX
* Zezwala na rozszerzanie komponentów React poprzez dodawanie styli do nich
	* wykorzystanie props
* Reużywalne
* Emotion, Material UI

### Tagged templates
...


### Tailwind CSS
* Stylowanie za pomocą atomowych klas CSS
	* utility classes
* Szybkie i intuicyjne
* Brak predefiniowanych komponentów
* Podejście utility-first
	* nie piszemy własnych klas jeśli nie musimy
* Elastyczność
* Łatwość konfiguracji
	* wszystko w jednym pliku
	* można definiować własne kolory itd
* Responsywność
	* wbudowane klasy do tego
* Brak nadmiarowego kodu
* Integracja z narzędziami
* Ekosystem
	* rozbudowana dokumentacja
	* społeczność
	* rozszerzenia
* Zaśmieca kod JSX
	* może dzielić komponent na komponenty wizualne i logiczne
