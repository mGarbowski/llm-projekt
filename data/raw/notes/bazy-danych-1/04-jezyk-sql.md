# Język SQL
Transformacja do postaci normalnej poza uniemożliwianiem anomalii pozbywa się też redundancji i zapewnia bardziej efektywne przechowywanie danych


## Język SQL
* standard ANSI
* bazuje na rachunku relacyjnym
* deklaratywny - określa wyniik a nie sposób jego uzyskania
* operacje na zbiorach (relacjach)
* przetwarzanie wielu danych za pomocą pojedynczej instrukcji

## Kategorie instrukcji
* DML - Data Manipulation Language - operacje CRUD
    * INSERT
    * UPDATE
    * DELETE
* DDL - Data Definition Language - zarządzanie schematem
    * CREATE
    * ALTER
    * DROP
    * TRUNCATE
* DCL - Data Control Language - kontrola dostępu
    * GRANT
    * REVOKE
* DQL - Data Query Language
    * SELECT
* TCL - Transaction Control Language
    * COMMIT
    * ROLLBACK

## Budowa języka
* Identyfikoatory - nazwy obiektów
* Literały - stałe
* Operatory - arytmetyczne, logiczne, znakowe
* Słowa kluczowe - instrukcje, klauzule, typy danych, funkcje
* Komentarze

Instrukcja zaczyna się klauzulą czyli słowem kluczowym, które określa operację

## Instrukcja `SELECT`
* pobiera informacje z wielu relacji
* rezultatem jest tymczasowa relacja
* rezultat nie musi być w 3 postaci normalnej
* rezultat może być wejściem innej instrukcji `SELECT`
* sekcje mogą zawierać złożone konstrukcje - podzapytania, zapytania skorelowane itp.


### Budowa
* `SELECT <atrybuty>` - atrybuty wybierane z relacji (wybór kolumn)
* `FROM <tabele>` - wybór źródeł rekordów (tabel)
* `WHERE <warunki>` - warunki dotyczące krotek (wybór wierszy)
* `GROUP BY <atrybuty>` - grupowanie rekordów
* `HAVING <warunki>` - warunki dotyczące wyboru grup
* `ORDER BY [ASC|DESC]` - sortowanie

### Kolejność przetwarzania instrukcji
* `FROM`
* `WHERE`
* `GROUP BY`
* `HAVING`
* `SELECT`
* `ORDER BY`

### Klauzula `SELECT`
* nazwy kolumn
* wszstkie kolumny `*`
* stałe
* funkcje skalarne
* wyrażenia arytmetyczne, tekstowe
* warunkowe `CASE ... WHEN`
* podzapytania zwracające pojedynczy element skalarny - niezalecane, bo nie są optymalizowane
* zmienne
* `DISTINCT` - tylko unikalne wartości
* `TOP` - ograniczenie liczby rekordów, użyteczne w połączeniu z sortowaniem
* elementy można aliasować używając `AS`

### Klauzula `FROM`
* Wybór źródeł rekordów
    * tabele
    * podzapytania
* Źródła mogą być aliasowane z użyciem `AS`

### Klauzula WHERE
* Porównania `=`, `<>`, `<`, `>`, `<=`, `>=`
* `BETWEEN ... AND ...`
* `IN`, `ANY`, `ALL`
* Filtrowanie wartości znakowych `LIKE`, `%`
* Podzapytania
* Funkcje skalarne `COUNT`, `MAX`, `MIN`, `SUM`, `AVG`


## Podzapytania
Instrukcja `SELECT` umieszczona wewnątrz innego zapytania `SELECT`, może występować w klauzulach `SELECT`, `FROM`, `WHERE`, `HAVING`

* nieskorelowane - niezależne od kontekstu, mogą funkcjonować jako samodzielne zapytania
* skorelowane - odwołanie do atrybutu spoza podzapytania, można przekształcić w nieskorelowane używając złączenia

Podzapytanie nieskorelowane
```sql
SELECT student.nazwisko
FROM student
WHERE student.wiek > 30 AND student.id_grupy IN (
    SELECT id_grupy
    FROM grupa
    WHERE typ = 'dzienne magisterskie'
)
```

Podzapytanie skorelowane - nazwy grup większych niż 10-osobowe na kierunku informatyka
```sql
SELECT DISTINCT s.grupa
FROM studenci AS s
WHERE s.kierunek='informatyka' AND (
    SELECT COUNT(id_stud)
               FORM studenci AS r
WHERE s.grupa = r.grupa
    ) > 10
```


## Instrukcje DML
Służy do podstawowych operacji na danych

* `INSERT` - wprowadzanie danych
* `UPDATE` - zmiana danych
* `DELETE` - usunięcie danych

```sql
INSERT INTO studenci (num_ind, imie, nazwisko, kierunek, grupa) VALUES (123456, 'Jan', 'Kowalski', 'informatyka', 107);
```

```sql
UPDATE studenci SET stypendium = stypendium * 1.1 WHERE rok_st > 2;
```

```sql
DELETE FROM pracownicy WHERE imie = 'Jan' AND naziwsko = 'Kowalski';
```

## Instrukcje DCL
Nadawanie uprawnień do obiektów w bazie danych

* `GRANT` - nadawanie uprawnień globalnie lub do pojedynczych obiektów konkretnemu użytkownikowi
* `REVOKE` - odebranie użytkownikowi wskazanych uprawnień
* `DENY` - blokowanie dostępu

## Logika trójwartościowa, `NULL`
* `NULL` reprezentuje nieznane, brakujące lub nieistotne dane
* to co innego niż 0 i zbiór pusty
* porównanie wartości `NULL` z dowolną wartością zwraca wartość `UNKNOWN`
    * `NULL` nie jest równy sam sobie
    * `NULL` nie jest prawdą i negacja `NULL` nie jest prawdą
* Stosuje się tylko porównania typu `x IS NULL` albo `x IS NOT NULL`
* Wartości `NULL` są ignorowane przez większość funkcji agregujących, nie przez `COUNT(*)`

![Tabela prawdy w logice trójwartościowej](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fi.stack.imgur.com%2FyRBgu.png&f=1&nofb=1&ipt=2b19b6795de47cf26e1f21e0b850f4dc4e26a78812d53a0522f11946ac9e4ccc&ipo=images)

```sql
SELECT id_stud, nazwisko, nazwa, status
FROM studenci AS a, zapisy_na_przedmiot AS z, przedmiot AS p
WHERE s.id_stud = z.id_stud
  AND z.id_przed = p.id_przed
  AND status IS NOT NULL
```

## Instrukcje DDL
Zarządzanie schematem bazy danych, instrukcje umożliwiają operowanie na strukturach, wktórych są przechowywane dane

* `CREATE` - utworzenie struktury (tabeli, indeksu, ...)
* `DROP` - usunięcie struktury
* `ALTER` - modyfikacja struktury

```sql
CREATE TABLE studenci (
                          num_ind INTEGER,
                          imie VARCHAR(255),
                          nazwisko VARCHAR(255),
                          kierunek VARCHAR(255),
                          grupa VARCHAR(255),
);
```


## Łączenie
![Venn diagram](https://i.stack.imgur.com/UI25E.jpg)

* wewnętrzne
    * CROSS JOIN - iloczyn kartezjański, każdy z każdym, mało wydajne
    * INNER JOIN - określone atrybuty w klauzuli `ON`
    * NATURAL JOIN - równozłączenie relacje po atrybutach o tych samych nazwach
* zewnętrzene
    * LEFT/RIGHT OUTER JOIN - wynik INNER JOIN + wiersze z lewej / prawej tabeli dla których warunek nie jest spełniony
    * FULL OUTER JOIN - wynik INNER JOIN + wiersze z obu tabel dla których warunek nie jest spełniony



## Operacje na zbiorach
* Operacje na wynikach całych tabel wejściowych
* Tabele muszą mieć takie same atrybuty
* Operacje są wykonywane od góry do dołu


* UNION - suma zbiorów
* EXCEPT - odejmowanie zbiorów
* INTERSECT - iloczyn zbiorów

## Operatory `EXISTS`, `ALL`, `ANY`
Przykład

```sql
SELECT nazwisko
FROM studenci
WHERE stypendium >= ALL (
    SELECT stypendium * 1.3
    FROM studenci
    WHERE grupa = 'abc'
)
```

## Integralność
* Sprawdzane przed wykonaniem zapytania
* na poziomie atrybutów (dziedzina, zakres wartości)
* na poziomie relacji - klucz podstawowy
* na poziomie związków - klucz obcy
* reguły integralności - ograniczenia na poziomie bazy danych, parametry statystyczne
* `UNIQUE`
* `NOT NULL`
* `CHECK` - warunek logiczny, dowolnie złożony, może zawierać zagnieżdżone zapytanie `SELECT
* `ASSERTION` - ogólne więzy integralności

### Operacje kaskadowe
Klucz obcy musi odpowiadać rekordowi w innej tabeli, modyfikacja lub usunięcie takiego rekordu wymaga podjęcia czynności w rekordzie który się do niego odwołuje przez klucz obcy

* Definiuje się w klauzulach
    * `ON UPDATE`
    * `ON DELETE`
* Czynności
    * `NO ACTION`
    * `CASCADE`
    * `SET NULL`
    * `SET DEFAULT`


## Wyzwalacze
* `CREATE TRIGGER ...`
* reakcja na zdarzenia
* tworzone na elemencie (tabeli, widoku, bazie danych)
* definiuje się punkt czasowy

## Widok (perspektywa)
Tabela dynamicznie wyliczona z innych tabel, nie przechowują danych trwale.

* ograniczenie widoczności
* przyspieszenie operacji / pojedynczych zapytań
* prezentowanie tych samych danych w różny sposób
* ułatwienie dostępu

### Mogą być aktualizowane
* leniwie
* natychmiastowo
* okresowo

```sql
CREATE VIEW studenci_inf
AS SELECT *
   FROM studenci
   WHERE kierunek = 'inf'
```

Perspektywy zmaterializowane - trwale przechowujądane

## Tablica tymczasowa
* Klauzula `WITH`
* Upraszcza zapis zapytania
* Zagnieżdżone `SELECT` można zastąpić przez `JOIN`
