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

Duży model językowy (generator) będzie uruchomiony na GPU, natomiast pozostałe modele (retriever, reranker) będą
uruchomione na CPU.

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

## Zbiór testowy

Na potrzeby ewaluacji opracowałem zbiór testowy składający się z 38 pytań
wraz z listą istotnych fragmentów dokumentów oraz wzorcowymi odpowiedziami.

Plik [`test.jsonl`](./data/eval/test.jsonl) w formacie JSONL (każda linijka to osobny JSON),
pojedynczy wiersz jest w formacie:

```json
{
  "query": "Co to jest partycjonowanie zakresowe i kiedy warto je stosować?",
  "relevantDocs": [
    "25a8cb17-d17f-4522-8243-3da0f8f6491f",
    "decb07c0-fb6e-4fb5-80ac-520eda2521e2"
  ],
  "referenceAnswers": [
    "Partycjonowanie zakresowe dzieli dane na partycje według zakresów wartości klucza..."
  ]
}
```

Został przygotowany z użyciem LLM GPT-5 mini i poddany ręcznej weryfikacji i korekcie.

## Ewaluacja

Oddzielnie przeprowadziłem ewaluację komponentu retrieval oraz jakości generowanych odpowiedzi (pełnego potoku RAG).

### Retrieval

Metryki są wyliczane na podstawie `relevantDocs` w zbiorze testowym i wyników zwróconych przez komponent retrieval.
Porównywane są trzy warianty:

* leksykalny (PostgreSQL full-text search)
* semantyczny (bi-enkoder)
* leksykalne + semantyczny + reranker

Porównywane są miary jakości Recall@k (niezależne od kolejności dokumentów w wyniku)
oraz MRR@k (uwzględniające kolejność, im wyżej w rankingu jest pierwszy istotny dokument tym lepiej).

|           | Fulltext Retriever | Semantic Retriever | Reranking Retriever |
|:----------|-------------------:|-------------------:|--------------------:|
| Recall@1  |               0.19 |               0.33 |                0.50 |
| Recall@3  |               0.30 |               0.59 |                0.67 |
| Recall@5  |               0.33 |               0.66 |                0.71 |
| Recall@10 |               0.35 |               0.71 |                0.73 |
| MRR@1     |               0.29 |               0.55 |                0.79 |
| MRR@3     |               0.35 |               0.69 |                0.86 |
| MRR@5     |               0.36 |               0.70 |                0.86 |
| MRR@10    |               0.37 |               0.70 |                0.86 |

### Generacja odpowiedzi

Metryki są wyliczane na podstawie `referenceAnswers` w zbiorze testowym i odpowiedzi wygenerowanych przez pełny potok
RAG
(z użyciem wariantu wyszukiwania leksykalnego + semantycznego + rerankingu).

|                        |  Wartość |
|:-----------------------|---------:|
| BERT Score - Precision | 0.647105 |
| BERT Score - Recall    | 0.728052 |
| BERT Score - F1        | 0.684386 |
| ROUGE-L - Precision    | 0.126731 |
| ROUGE-L - Recall       | 0.356810 |
| ROUGE-L - F1           | 0.175511 |
| BLEU Score             | 3.740200 |

## Źródła

* https://medium.com/@jesvinkjustin/from-zero-to-rag-the-art-of-document-chunking-and-embedding-for-rag-d9764695cc46
* https://medium.com/@nitinprodduturi/using-postgresql-as-a-vector-database-for-rag-retrieval-augmented-generation-c62cfebd9560
* https://www.evidentlyai.com/ranking-metrics/precision-recall-at-k
* https://www.evidentlyai.com/ranking-metrics/mean-reciprocal-rank-mrr

## TODO

* Konfiguracja modułów dla języka polskiego w PostgreSQL
    * na razie jest używany wariant `simple` - daleki od ideału dla tego zastosowania
* Poprawienie klasy Pipeline
    * pełna parametryzacja zapytań
* Otypowanie endpointów API
* Dopracowanie frontendu
    * UI po polsku
    * błąd z podwójną wiadomością na czacie
* Dopracować prompt generatora
