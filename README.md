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

## Źródła
* https://medium.com/@jesvinkjustin/from-zero-to-rag-the-art-of-document-chunking-and-embedding-for-rag-d9764695cc46