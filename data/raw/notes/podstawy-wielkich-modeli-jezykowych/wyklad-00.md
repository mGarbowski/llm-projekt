# Wstęp

## Organizacja
* dr Jacek Komorowski
* Materiały na kanale teams
	* wykłady
	* tutoriale z torcha
* Używamy pytorch i huggingface
* Wykład
	* 10 pkt
	* jedno kolokwium
	* ostatni miesiąc zajęć
* Laboratorium
	* 14 pkt
	* 7x 2pkt
	* 2 tygodnie na przesłanie rozwiązania
	* start 10 X (piątek) i 14 X (wtorek)
* Projekt
	* 14 pkt
	* samodzielny lub zespoły 2-osobowe
	* tydzień na potwierdzenie tematu projektu i wykorzystywanych zbiorów danych
	* kod + raport + prezentacja wyników
	* na początku listopada więcej informacji
	* będą proponowane tematy
* Zaliczenie
	* min. 50% z każdej części

Będziemy też omawiać klasyczne architektury i metody - bywają szybsze, lepsze i tańsze niż LLM

Pomysł - RAG na podstawie moich notatek ze studiów

## Plan wykładu
* Wprowadzenie i podstawy
	* podstawy głębokiego uczenia i głębokich sieci neuronowych
	* pytorch
	* klasyczne metody reprezentacji i klasyfikacji tekstu
* Budowa wielkich modeli językowych
	* reprezentacja tekstów w języku naturalnym
	* metody tokenizacji
	* architektura transformer i jej składowe
	* rodziny architektur modeli językowych (tylko-koder, tylko-dekoder, ...)
* Uczenie wielkich modeli językowych
* Wykorzystanie i dostosowywanie modeli językowych
	* strategie generowania tekstu
	* wykorzystanie modeli do zadań NLP
	* metody efektywnego obliczeniowo dostrajania (PEFT)
* Modele wizyjno-językowe
	* uczenie reprezentacji wizyjno-językowej (CLIP)
	* generatywne modele wizyjno-językowe
* Zastosowania
	* generowanie tekstu wspomagane wyszukiwaniem (RAG)
	* systemy dialogowe
	* agenty językowe
* Polskie modele językowe
* Współczesne trendy rozwojowe

## Literatura
* Książki dostępne online, linki na slajdach
* Jurafsky
	* https://web.stanford.edu/~jurafsky/slp3/
* Książki ...
* PyTorch
	* samouczki w dokumentacji
* HuggingFace
	* LLM Course https://huggingface.co/learn/llm-course/chapter1/1
	* dokumentacja pakietu Transformers
* Wykłady dostępne online
	* Stanford CS224N: NLP with Deep Learning
	* CMU Advanced NLP Spring 2025
	* Berkeley Agent AI MOOC

# Wstęp

## Czym są wielkie modele językowe
* Generatywne modele językowe oparte o architekturę Transformer (transformator cech głębokich z atencją) z rodziny tylko-dekoder
* Trenowane na ogromnych zbiorach danych
	* setki miliardów lub biliony słów
	* główne zadanie - przewidywanie kolejnego słowa/tokenu na podstawie kontekstu
	* uczą się statystycznych wzorców języka
* Dzięki skalowaniu parametrów i danych wykazują zdolności emergentne (emergent abilities)
	* zdolność do wykonywania zadań, do których nie był specjalnie trenowany
	* rozumowanie, pisanie kodu, streszczanie, tłumaczenie
* Liczba parametrów - rzędu dziesiątek miliardów lub więcej

### Dwie perspektywy
* LLM jako klasyfikator probabilistyczny
	* estymacja prawdopodobieństwa kolejnego tokenu na podstawie kontekstu (poprzedzającej sekwencji)
	* wejście: kontekst (poprzedzająca sekwencja tokenów)
	* wyjście: rozkład prawdopodobieństwa kolejnego tokenu
	* funkcja straty: entropia krzyżowa (w fazie wstępnego trenowania i nadzorowanego dostrajania)
* LLM jako statystyczny model języka
	* podobnie jak tradycyjne modele językowe (n-gramowe, HMM, RNN) definiują rozkład prawdopodobieństwa
	* prawdopodobieństwo tokenu $x_n$ warunkowane poprzedzającą sekwencją $x_1, \ldots, x_{n-1}$
	* $P(x1, \ldots x_n) = \prod ...$ 
## Systemy dialogowe
* System dialogowy zapamiętuje historię konwersacji
	* na zewnątrz samego LLM
	* kontekst podawany na wejście
* Prompt systemowy
	* "jesteś asystentem AI ..."
	* podawany na wejście LLM przed promptem użytkownika
* System dialogowy może wywoływać dodatkowe narzędzia
	* LLM może wygenerować polecenie zrozumiałe dla systemu dialogowego
	* np. specjalny token
	* odpowiedź z narzędzia też jest doklejona do sekwencji wejściowej modelu 

## Autoregresyjne generowanie tekstu
* Podejście autoregresyjne przyczynkowe (causal)
	* generuje rozkład prawdopodobieństwa kolejnego tokenu
	* próbkowanie kolejnego tokenu (różne strategie) z rozkładu
	* doklejenie tokenu do sekwencji
	* powtórzenie aż do wygenerowania specjalnego tokenu end-of-sequence (lub przekroczenie limitu długości)
* Problem długiego ogona
	* kiedy wybiera się najbardziej prawdopodobny token(?)
	* powstaje długi, poprawny składniowo i bezsensowny tekst

## Trenowanie wstępne (pretraining)
* Na to poświęca się większość budżetu i zasobów obliczeniowych
* Zadanie - przewidywanie kolejnego tokenu na podstawie kontekstu
* Żeby model dobrze przewidywał prawdopodobieństwo kolejnego tokenu to musi nauczyć się wiedzy o świecie
* Olbrzymie zbiory danych
	* dane pozyskane z internetu (legalnie lub nie) - książki, repozytoria kodu, serwisy społecznościowe
	* często używa się syntetycznie generowane dane - np. trenowanie mniejszego modelu na podstawie generacji większego modelu
	* komercyjne LLM mające 7-70B parametrów - trening na zbiorze rzędu 1-15T tokenów (5-20TB tekstu)
* Koszty
	* GPT-3 - 5M USD
	* GPT-4 - 50-100M USD

## Rodziny architektur modeli językowych
* Tylko-dekoder
	* GPT
	* iteracyjne generowanie kolejnych tokenów
	* predykcja kolejnego tokenu
	* atencja przyczynowa - przepływ informacji od lewej do prawej
	* $x_i$ nie korzysta z $x_{i+1}$
* Tylko-koder
	* wyznacza kontekstową reprezentację tokenów w sekwencji 
	* atencja dwukierunkowa
	* trening - maskowane modelowanie języka
	* zwykle znacznie mniejsze rozmiary (rzędu 100M parametrów)
	* ekstrakcja reprezentacji, klasyfikacja tekstu
	* modele BERT, RoBERTA
	* zastosowania typu RAG
* Koder-dekoder
	* transformer z artykułu Attention is all you need
	* predykcja kolejnego tokenu na podstawie kontekstu
	* koder - atencja dwukierunkowa
	* dekoder - atencja przyczynowa
	* tokeny wejściowe mogą być innego typu niż wyjściowe
	* np. audio -> transkrypcja, obraz -> opis tekstowy, wideo -> tekstowe podsumowanie

### Tylko-dekoder
* Tekst wejściowy - po tokenizacji
	* wielkość słownika np. 128k tokenów
* Identyfikatory tokenów - indeks w LUT
* Wektorowe reprezentacje tokenów
	* rozmiar wektora np. 4096
	* wybór wektora po indeksie
	* wagi inicjowane losowo
	* aktualizowane w trakcie treningu
* Position embedding
	* dodanie do embeddingu wektora reprezentującego jego pozycję w sekwencji
	* różne podejścia, np. sinusowe
	* sama architektura nie korzysta gdzie indziej z informacji o pozycji
* Wiele bloków dekodera
	* losowo inicjowane wagi, uczone
	* np. 32
	* warstwa atencji
	* warstwa MLP
	* format wyjścia bloku taki sam jak wejścia - tensor (długość sekwencji/kontekstu, rozmiar wektora zanurzenia)
* Kontekstowe reprezentacje tokenów
	* bierze się ostatni wektor cech z sekwencji
	* warstwa liniowa - rozmiar zanurzenia x rozmiar słownika
	* wyznacza indeks tokenu - da się zamienić z powrotem na tekst
* Liczba wag modelu nie zależy od długości sekwencji

Przy treningu

* Równoległa predykcja dla każdego tokenu w sekwencji wejściowej
	* tylko przy treningu!
	* dla każdego wyjścia można policzyć stratę
	* do tego atencja musi być przyczynowa - żeby model przy treningu nie podglądał co jest dalej w sekwencji