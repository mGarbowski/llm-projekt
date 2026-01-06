# RAG c.d. (2025-11-28)
* Zamiast Rerankera może być Reader
	* Reader nie wykonuje generacji, tylko wybiera fragmenty tekstu
* Zapytanie jest używane przez retriever, reranker i generator
* Zbiór treningowy pod retrieval
	* pytanie + zbiór dokumentów
	* dokument może się powtarzać (relacja wiele do wielu)
* Raczej nie warto robić RAGa dla bazy wiedzy mniejszej niż 100 dokumentów (po chunkingu)
	* mniej - można podać całość do generatora
* Chunking
	* Najbardziej naiwne podejście - okno przesuwne, np. po 512 tokenów
* Źródła tekstu
	* pdf, doc - łatwo się parsuje
	* Apache Tika
	* html jest bardziej problematyczny - JS, renderowanie warunkowe itd

## Chunking
* Problem - dokumenty są długie
	* niedobór polskich retrieverów
* Może i nowe LLMy wspierają konteksty rzędu miliona tokenów ale drastycznie spada jakość już dla dużo mniejszych
* Najlepszy byłby podział na części spójne semantycznie
* Automatyczny chunking
	* nie wymagające założeń na temat struktury
	* okno przesuwne X tokenów
	* dzielenie po separatorach
	* Langchain - RecursiveCharacterTextSplitter
	* grupowanie zdań spójnych semantycznie za pomocą embeddingów
	* wykorzystanie LLMów do podziału - GLM4.6, DeepSeek dobrze sobie radzą
* Heurystyczny chunking
	* wykorzystanie informacji o strukturze dokumentu
	* wydzielenie części wspólnej (nagłówek najwyżsezgo rzędu), dołączany do wszystkich
	* podział po nagłówkach
* Do ewaluacji - zbiór testowy raczej z id dokumentów źródłowych - przed chunkowaniem


## Retrieval i reranking
* BM25 jest zaskakująco dobry, zwłaszcza dla długich tesktów


## Generator
* Dostaje query, top n wyników wyszukiwania (z rerankera)
* Generuje tekst
* Można wziąć gotowy LLM w trybie few-shot/zero-shot
	* może nie mieć odpowiedniej formy odpowiedzi
	* może być potrzeba dostrojenia
* SFT - daje większą stabilność odpowiedzi, mniej wrażliwy na konkretny dobór słów w prompcie
* Przygotowanie zbioru danych do dostrajania
	* można wykorzystać LLM do automatycznego generowania danych
	* np. podajemy dokument, niech LLM wygeneruje pytania
	* znaleźć inne chunki relewantne do wygenerowanych pytań
* W zbiorze można uwzględnić pytanie na które nie ma odpowiedzi w bazie wiedzy
	* żeby nauczyć model odmawiania odpowiedzi bez kontekstu
* Przy dostrajania, jeśli trenujemy model multiinstrukcyjny to zbiór treningowy musi być zbalansowany
	* inaczej model wyspecjalizuje się w nadreprezentowanym zadaniu, a pogorszy jakość w pozostałych
* Przy trneingu jeśli mamy out of memory - można zmniejszyć batch size a zwiększyć liczbę kroków akumulacji gradientu
	* kroki akumulacji gradientu - bardzo ważne!
	* wirtualny batch - dalej stabilne uczenie ale nie jest ładowane wszystko na raz do pamięci
* Learning rate w LoRA vs bez LoRA
	* w LoRA jest mniej wag do uczenia więc model szybciej się uczy
	* możemy startować w większym learning rate rzędu 1e-4, bez 1e-6
* Statystyki treningu
	* loss - wiadomo że ma spadać ale sama wartość nic nam nie mówi
	* wprowadza się miary podobne do miary Jaccarda (IoU) słów/bigramów wygenerowanego tekstu z oczekiwanym

## RAG-if-eval
* Podejście do benchmarkowania
* Szybkie i deterministyczne
* Oceniamy odpowiedzi na podstawie słów kluczowych
	* np. odpowiedź musi zawierać / nie może zawierać / powinien odmówić odpowiedzi

Chcę zrobić model do streszczania tekstu, czy lepiej stroić model base czy instruct - model base potrafi tylko robić autouzupełnianie, instruct już potrafi wykonywać zadania, w tym pewnie streszczania.
Instruct już był dostrojony więc ma zakrzywioną przestrzeń poznawczą
Jeśli mamy duży zbiór treningowy to możemy dostrajać model base (np. 20k instrukcji)
Jeśli mamy mało przykładów (np. <1k instrukcji) lepiej stroić model instruct


Uczenie kaskadowe
kilka sesji SFT z różnymi zbiorami treningowymi - model zapomina to czego się nauczył wzceśniej

Raczej najlepiej uczyć od razu do 1 zadania (jeśli potrzebujemy tylko 1 zadania) niż uczyć kaskadowo

## ShpaRAG
* Aplikacja do anotowania dokumentów na potrzeby RAGów