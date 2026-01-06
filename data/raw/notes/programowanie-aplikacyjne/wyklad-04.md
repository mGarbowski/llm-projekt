# Wykład 04 (2023-10-25)
* Będzie założone zadanie na leonie na każdy etap projektu
* Będą dopisani prowadzący do listy
* Każda osoba z grupy wysyła link do repozytorium w Gitlabie, w README ma być proponowany opis zadania (po spotkaniu z prowadzącym będziemy korygować)
* My mamy się skontaktować z prowadzącym kiedy zostanie przydzielony

## Porównywanie obiektów
* `==` sprawdza równość referencji a nie wartości, zachowanie dla stringów może się różnić w zależności od optymalizacji kompilatora
* Do porównywania wartości służy metoda `.equals`

## Formatowanie stringów
* Konkatenacja z `+` jest mało wydajna bo zawsze tworzy nowy obiekt
* `String.format()`
* String buffer, String builder

## Czytanie z konsoli
Klasa `Scanner`
* nextLine
* nextNumber

## AutoCloseable
Obiekty które implementują ten interfejs można używać w bloku try-with-resources i same się zamkną po zakończeniu bloku try
Wyjątek w konstruktorze nie będzie obsłużony, spójne z UML

## Kolekcje
Będą na kolokwium
Powinno się korzystać z gotowców

## Strumienie
Przetwarzanie sekwencji elementów
Miały pomóc z przetwarzaniem wielowątkowym
Deklaratywny kod, może być lepiej zoptymalizowany, zrównoleglony

## Równoległość w Javie
* klasa Thread
* klasa ThreadPool
* użycie strumieni

## Synchronized i semafory
Klasa Semaphore
słowo kluczowe synchronized przed metodą

## Asynchroniczne przetwarzanie
ExecutorService, Future
Korzystają z oddzielnych wątków ale programista nie dotyka bezpośrednio wątków i nie ma(?) jak popsuć
