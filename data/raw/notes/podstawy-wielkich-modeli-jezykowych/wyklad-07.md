
# Information Retrieval

## Terminologia
* Wyszukiwanie leksykalne
	* dopasowanie słów w zapytaniu z dokumentami
	* słowa kluczowe
	* rzadkie (sparse search)
	* szukamy dokumentu $d_i$ o jakiejś części wspólnej z zapytaniem $\langle q \cap d_i \rangle$
	* wykorzystuje się odwrócone indeksy - słownik i dla każdego słowa lista dokumentów, w których występuje
* Wyszukiwanie semantyczne
	* to samo znaczenie, niekoniecznie te same słowa
	* gęste (dense search)
	* np. podobieństwo wg. miary cosinusowej $\cos(q, d_i)$

* Unigram - pojedyncze słowo
	* bigram - sklejone 2 słowa

### Wyszukiwanie leksykalne
* Problem jeśli zapytanie zawiera takie słowa, że przecięcie list dokumentów ze słownika jest puste - nie ma w zbiorze takiego dokumentu, które zawiera wszystkie słowa z zapytania
* VSM - przestrzeń wektorów słów
	* wymiar - liczba unikalnych słów w korpusie dokumentów
	* waga słowa - one-hot, tf-idf
	* dopasowanie dokumentu o największym podobieństwie wektora
	* zapytanie rzutowane na wektor
* Tak działa Apache Lucene - inverted index + VSM
	* dobre ale nie uwzględnia semantyki, ani kolejności słów

## Wyszukiwanie semantyczne
* Pierwsze reprezentacje - Word2Vec
* Mniejsza wymiarowość wektora reprezentacji
* Obecnie - enkodery

## Information Retrieval
* Wyciągnięcie informacji z dużej kolekcji dokumentów tekstowych
* Tradycyjne metody - tf-idf, bm25
	* łatwo interpretowalne
	* nienadzorowane
	* robust
* Neural Information Retrieval
	* oparte o sieci neuronowe
	* może być lepsze ale wymaga dostrajania
	* wymaga wysokiej jakości zbiorów treningowych

## BM25
* Używany przez ElasticSearch
	* lepszy od tf-idf
	* oparty na tf-idf
	* wygładzanie, ważenie, uwzględnienie długości i średniej długości dokumentu

## Podejścia wykorzystujące DL
* Wyjście enkodera - wektor per token
	* można zrobić average pooling wyjścia żeby mieć jeden token
* Bi-Encoder
	* 2 zdania (zapytanie i dokument)
	* dla obu wyznaczane wektory zanurzeń
	* porównanie przez podobieństwo cosinusowe
	* bardzo efektywne - dla korpusu dokumentów można policzyć reprezentację raz, a przy wyszukiwaniu tylko dla zapytania
	* zanurzenia przechowuje się w indeksie
	* FAISS - biblioteka do wydajnego wyszukiwania wektorów, aproksymowanego
	* w treningu triplet loss - kotwica, przykład pozytywny i przykład negatywny
	* szukanie hard negatives - podobny do zapytania ale nie są pozytywne
	* lepiej nie traktować wszystkich nie-pozytywnych przykładów jako negatywne - mogą być zależności nieuwzględnione w zbiorze treningowym
* Cross-encoder (reranker)
	* 2 zdania sklejone i podane na wejście enkodera
	* do enkodera doczepiona głowica klasyfikacji
	* waga $[0,1]$ - podobieństwo
	* bardzo nieefektywne - tyle inferencji ile dokumentów w przeszukiwanym zbiorze
	* bardziej skuteczne
	* reranker jest tym mocniejszy im mocniejszy jest model w środku - lepiej LLM tylko-dekoder niż np. BERT

### Ewaluacja re-rankera
* Retrieval
	* można łączyć kilka metod
	* jest zbiór najbardziej relewantnych dokumentów
	* np. bi-enkodery, wyszukiwanie rzadkie
* Dokumenty przepuszczone przez cross-encoder
	* wybrane top k
	* posortowanie po istotności
* Połączenie bardziej wydajnego bi-enkodera z mniej wydajnem ale bardziej skutecznym cross-encodrem

## Chunking
* Dokumenty są długie
* Retrievery i rerankery mają ograniczone rozmiary kontekstu
* Trzeba podzielić tekst na kawałki
* Jak podzielić, żeby zmieścić się w kontekście ale zachować semantykę, uniknąć rozdrobnienie informacji na kilka chunków

## Stemming i lematyzacja
* Stemmer - wybiera rdzeń słowa jako część wspólną
* Lematyzator - zamienia na gramatycznie poprawną formę bazową (np. bezokolicznik dla czasownika w różnych formach)
* Morfologik - narzędzie dla języka polskiego

## PIRB
* Polish Information Retrieval Benchmark

# RAG
* Retrieval Augmented Generation
* Odpowiadanie na pytania przy wykorzystaniu lokalnej bazy wiedzy
* Klasyczny potok składa się z
	* retriever - jeden lub więcej
	* reranker
	* generator (reader) - model udzielający odpowiedzi na pytania
* Sam LLM nie ma aktualnej wiedzy, tylko wiedzę z czasu treningu