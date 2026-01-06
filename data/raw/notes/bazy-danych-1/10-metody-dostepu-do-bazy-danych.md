# Wprowadzenie do interfejsów i elementów aplikacji bazodanowych (2023-05-25)


## Strategie współpracy z bazą danych
* Osadzanie zapytań w uniwersalnym języku programowania
  * Tekst zapytania stanowi część kodu źródłowego programu
  * Zapytanie weryfikowane syntaktycznie w trakcie kompilacji
  * Czytelny kod
  * Zapytanie jest statyczne, nie można zmienić w trakcie wykonywania
* Biblioteki typu JDBC, ODBC
  * Możliwość generowanie zapytań w runtime
  * brak weryfikacji podczas kompilacji
* Natywne języki programowania baz danych (np. PL/SQL)
  * wyzwalacze
  * kursory
    * jawne
    * niejawne


# Bazy analityczne
Bazy które mają wspierać analityke mają inną specyfikę niż bazy transakcyjne, można to rozdzielić na oddzielne bazy

* OLTP
  * bieżąca działalność
  * duża liczba prostych zapytań
  * dodawanie, usuwanie i modyfikacja danych
  * szybki dostęp do aktualnych informacji
* OLAP
  * analizy, raporty
  * odczyt informacji i cykliczne uzupełnianie
  * schematy
    * gwiazda
    * płatek śniegu
    * konstelacja faktów

Proces analityczny
* deskryptywna - co się stało
* diagnostyczna - czemu się stało
* predykcyjna - co się stanie
* preskryptywna - jak można to zoptymalizować
* modele uczenia maszynowego