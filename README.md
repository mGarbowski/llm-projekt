# LLM - projekt

## Wytyczne

Szanowny Panie Profesorze
Chciałbym zrealizować własny temat projektu na przedmiocie LLM
 
Projekt, o którym myślałem to aplikacja RAG wykorzystująca zbiór moich notatek z wykładów na politechnice (pliki markdown pogrupowane w katalogi).
 
Czy zaakceptował by Pan taki temat, a jeśli tak to jakie byłyby wymagania do takiego projektu?
 
Pozdrawiam
Mikołaj Garbowski
 
Dzień Dobry, zaproponowany temat jest bardzo dobry. Jeśli chodzi o wymagania, to oczekiwałbym:
Implementacji prototypu rozwiązania
Ewaluacji skuteczności opracowanego rozwiązania na samodzielnie przygotowanym zbiorze testowym. 
Ewaluacja dwóch składowych:
 ocena jakości komponentu odpowiadającego za wyszukiwanie dokumentów czy ich części (retrieval) z wykorzystaniem metryk takich, jak Recall@k czy MRR (Mean Reciprocal Rank)
ocena jakości wygenerowanych odpowiedzi - z wykrozystaniem metryk takich, jak ROGUE, BLUE czy BERTScore
Aby wykonać taką ewaluację należałoby samodzielnie przygotować zbiór danych testowych. Nie musi to być duży zbiór - kilkanaście czy kilkadziesiąt przykładów wystarczy.
Aby ocenić jakość komponentu odpowiadającego za wyszukiwanie (Retrieval) - należy przygotować zbiór zawierający przykładowe pytania i dla każdego z nich listę dokumentów zawierających poszukiwane informacje. Pozwoli to policzyć metryki takie jak Recall@k czy MRR (Mean Reciprocal Rank):
Aby ocenić jakiś wygnerowanych odpowiedzi nalezy przygotować zbiór zawierający przykładowe pytania i wzorcowe odpowiedzi. Można zrobić to ręcznie (przygotować wzorcową odpowiedź dla każdego pytania). A może wykorzystać jakiś większy LLM, aby wygenerował testowy zbiór danych - korzystając np. z promptu “Given this lecture note, generate 5 exam-style questions and answers.”

Do ewaluacji rozwiązania RAG można wykrozystać bibliotekę ragas https://github.com/explodinggradients/ragas. Liczy wiele popularnych metryk - po Pana stronie pozostałoby przygotowanie odpowiedniego zbioru testowego. Jak pisałem wcześniej, może to być relatywnie mały zbiór.

## Modele i algorytmy

System ma charakter edukacyjny i będzie uruchamiany na moim PC wposażonym w GPU NVIDIA GTX 1060 6GB,
wybierając modele biorę pod uwagę te ograniczenia sprzętowe.

Duży model językowy (generator) będzie uruchomiony na GPU, natomiast pozostałe modele (retriever, reranker) będa uruchomione na CPU.

* Generator - `speakleash/Bielik-1.5B-v3.0-Instruct`
* Retriever
  * przetestowane na laboratorium
  * algorytm BM25
  * bi-enkoder `sdadas/mmlw-retrieval-roberta-large`
* Reranker
  * przetestowany na laboratorium
  * cross-enkoder `sdadas/polish-reranker-roberta-v3`

Do weryfikacji pozostaje wydajność modeli uruchomionych na CPU


## Koncepcja implementacji
* Dokumenty zostaną podzielone na fargmenty (chunki)
  * chunk ma się mieścić w kontekście modeli (przede wszystkim retrievera i rerankera)
* Dla chunków zostaną wylicozne 2 wektory zanurzeń
  * jeden klasycznym algorytmem (BM25)
  * jeden za pomocą bi-enkodera
* Chunki z zanurzeniami i metadanymi będą zapisane w pazie PostgreSQL z rozszerzeniem pgvector
* Aplikacja backend FastAPI + SentenceTransformers + transformers
  * retrieval - 2 zapytania do bazy - najbliższi sąsiedzi wg BM25 i bi-enkodera
  * reranking - cross-enkoder na wynikach retrieval
  * generacja odpowiedzi - LLM na podstawie promptu z pytaniem i najistotniejszymi chunkami wg. rerankera
  * endpoint REST API
* Aplikacja frontend - prosta aplikacja w React z okienkiem czatu


## Źródła
* https://medium.com/@jesvinkjustin/from-zero-to-rag-the-art-of-document-chunking-and-embedding-for-rag-d9764695cc46
* https://medium.com/@nitinprodduturi/using-postgresql-as-a-vector-database-for-rag-retrieval-augmented-generation-c62cfebd9560