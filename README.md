# LLM - projekt

Mikołaj Garbowski

![Zrzut ekranu z aplikacji](docs/screenshot.png)

## Opis
Celem projektu jest implementacja systemu Retrieval-Augmented Generation (RAG) wykorzystującego
duży model językowy (LLM) do generowania odpowiedzi na pytania użytkownika na podstawie bazy dokumentów oraz
ewaluacja skuteczności opracowanego rozwiązania na samodzielnie przygotowanym zbiorze testowym.

Za zbiór dokumentów posłużą moje notatki z wykładów na Politechnice Warszawskiej w formacie markdown,
sporządzone w toku studiów inżynierskich.

## Modele i algorytmy

System ma charakter edukacyjny i będzie uruchamiany na moim PC wyposażonym w GPU NVIDIA GTX 1060 6GB.
Wybierając modele, biorę pod uwagę te ograniczenia sprzętowe.

Duży model językowy (generator) będzie uruchomiony na GPU, natomiast pozostałe modele (retriever, reranker) będą uruchomione na CPU.

* Generator - `speakleash/Bielik-1.5B-v3.0-Instruct`
* Retriever
  * PostgreSQL full-text search (wariant leksykalny)
  * bi-enkoder `sdadas/mmlw-retrieval-roberta-large` (przetestowany na laboratorium)
* Reranker
  * przetestowany na laboratorium
  * cross-enkoder `sdadas/polish-reranker-roberta-v3`

Do weryfikacji pozostaje wydajność modeli uruchomionych na CPU


## Koncepcja implementacji
* Dokumenty zostaną podzielone na fargmenty (chunki)
  * chunk ma się mieścić w kontekście modeli (przede wszystkim retrievera i rerankera)
* Chunki z zanurzeniami i metadanymi będą zapisane w pazie PostgreSQL z rozszerzeniem pgvector
* Aplikacja backend FastAPI + SentenceTransformers + transformers
  * retrieval
    * 2 warianty
    * leksykalny - full-text search w PostgreSQL
    * semantyczny - bi-enkoder do wyznaczania wektorów zanurzeń, indeks w pgvector
  * reranking - cross-enkoder na wynikach retrieval
  * generacja odpowiedzi - LLM na podstawie promptu z pytaniem i najistotniejszymi chunkami wg. rerankera
  * endpoint REST API
* Aplikacja frontend - prosta aplikacja w React z okienkiem czatu

## Ewaluacja rozwiązania
* Zbiór testowy
  * własny przygotowany na podstawie zbioru notatek
  * ręcznie i posiłkując się LLM do pomocy
  * format (pytanie, lista istotnych fragmentów (id), wzorcowa odpowiedź)
  * plik `.jsonl`
* Ewaluacja komponentu retrieval
  * porównanie wariantów
    * semantyczne
    * leksykalne
    * semantyczne + leksykalne + reranker
  * metryki
    * Recall@k
    * MRR (Mean Reciprocal Rank)
* Ewaluacja jakości generowanych odpowiedzi
  * metryki
      * ROGUE
      * BLUE
      * BERTScore

## Źródła
* https://medium.com/@jesvinkjustin/from-zero-to-rag-the-art-of-document-chunking-and-embedding-for-rag-d9764695cc46
* https://medium.com/@nitinprodduturi/using-postgresql-as-a-vector-database-for-rag-retrieval-augmented-generation-c62cfebd9560

## TODO
* Przygotowanie zbioru testowego
* Ewaluacja
* Konfiguracja modułów dla języka polskiego w PostgreSQL
  * na razie jest używany wariant `simple` - daleki od ideału dla tego zastosowania
