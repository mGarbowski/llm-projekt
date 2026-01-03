# Architektura tylko-koder

## Architektura
* Bardzo podobna do tylko-dekoder
* W bloku kodera w bloku atencji nie ma masek atencji
* Do wyznaczania reprezentacji tekstu
	* bierze pod uwagę od razu cały kontekst

## Rodzina architektur
* BERT (2019)
	* słownik 30k tokenów, tokenizator WordPiece
	* okno kontekstu 512 tokenów
	* wyuczone kodowanie pozycyjne
	* wersja Base - 110M parametrów, reprezentacja 768
	* wersja Large - 340M parametrów, reprezentacja 1024
* XLM-Roberta
	* trenowany na 100 różnych językach
* Modern BERT (2024)
	* tokenizator BPE
	* 395M parametrów w większej wersji - bardzo mało
	* GeGLU - gated-linear unit
		* jedna odnoga liniowa+GELU
		* druga odnoga z warstwą liniową i sigmoidem
		* na wyjściu mnożenie elementwise z obu odnóg
	* alternating attention - na przemian globalna i lokalna atencja
		* bardziej wydajne obliczeniowo

Do RAG
* pierwszy wybór - coś klasycznego jak tf-idf
* drugi wybór - tylko koder dostrojony do wyznaczania reprezentacji
## Trening
* Nie można trenować tak jak dekodera - do przewidywania kolejnego tokenu
	* nie ma maski atencji więc model widzi jaki będzie kolejny token
* Maskowane modelowanie języka
	* losowo wybrane 15% tokenów
	* 80% z nich zastąpione przez specjalny token maski
	* 10% zostaje zastąpione prze zlosowo wybrany token ze słownika
	* 10% zostaje bez zmian
* Predykcja zamaskowanych tokenów
	* entropia krzyżowa
* Trening jest mniej skuteczny niż przy dekoderach
	* bo tylko do niektórych wyjść przykłada się funkcję straty
	* w treningu kodera nie można zamaskować wszystkiego bo nie będzie z czego wyznaczać reprezentacji
* Drugie zadanie - predykcja następnego zdania (NSP)
	* sieć dostaje dwa zdania
	* musi ocenić, czy drugie zdanie jest kontynuacją pierwszego
	* detekcja parafrazy, ocena spójności
	* podaje się na wejście dwie sekwencje rozdzielone specjalnym tokenem separatora
	* Kontekstową reprezentację wyznacza się od pierwszego specjalnego tokenu `[CLS]`
	* do tego wyjścia przyłożona głowica klasyfikacji
	* tak samo się robi przy użyciu koderów do klasyfikacji tekstu

## Wykorzystanie modeli klasy tylko-koder
* Wyznaczają dobre kontekstowe reprezentacje
* Interpretacja, klasyfikacja, wyszukiwanie tekstu
* Indeksowanie i wyszukiwanie danyhc tekstowych
	* moduł wyszukiwania /indeksowania w RAG
* Analiza sentymentu

## Klasyfikacja
* Mamy zdanie wejściowe
* Out of the box, koder daje reprezentacje dla każdego tokenu
* Można uśrednić te tokeny i średnią traktować jako kontekstową reprezentację
* Można dokleić na początek specjalny token `[CLS]` i z wyjścia dla tego tokena wyznaczać reprezentację
* Tokenizator musi być zgodny z wersją modelu
	* tokenizatory w wersji uncased - tekst jest zamieniany na małe litery
* `transformers.AutoModelForSequenceClassification`
	* automatycznie dodaje głowicę klasyfikacyjną do wyjścia dla pierwszego tokena (CLS)
* W `transformers` już jest zaimplementowana pętla treningowa

Pytanie na egzaminie dyplomowym o macierz pomyłek dla klasyfikacji wieloklasowej

Kodery są zazwyczaj dużo mniejsze, szybsze i tańsze niż dekodery

## Sentence Transformers
* Biblioteka zawierająca implementacje metod wyznaczania wektorowej reprezentacji zdań i dłuższych fragmentów
* BERT out of the box nie był dostrojony do wyznaczania reprezentacji
* Biblioteka zawiera wagi dostrojonych modeli - też dla języka polskiego

## Quiz
Jakie podejście zastosować do

* Klasyfikacja emaili od klientów
	* tylko-koder do klasyfikacji (jak wyżej)
* Generowanie kodu w Pythonie na podstawie opisu w języku naturalnym
	* tylko-dekoder dostrojony do tego zadania
* Ekstrakcja informacji w ustrukturyzowanej formie np. JSON z tekstu w języku naturalnym
	* tylko-dekoder, dostrojony albo few-shot learning
* Wygenerowanie opisu w języku naturalnym dla podanego zdjęcia
	* architektura koder wizyjny-dekoder
	* koder generuje reprezentację obrazu
	* dekoder dostaje reprezentację obrazu i generuje kolejne tokeny tekstu