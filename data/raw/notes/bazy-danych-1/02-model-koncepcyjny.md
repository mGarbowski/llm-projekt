# Modelowanie koncepcyjne

## Entity-Relationship
Byty (encje) i związki między bytami

* Encje - posiadają atrybuty, wchodzą w związki z innymi encjami, są utrwalane
* Atrybuty
    * klucze
    * pozostałe
* Związki
    * też mogą mieć przypisane atrybuty

Istnieją kryteria co do wyboru atrybutu na klucz

Encja jest jednoznacznie identyfikowalna przez atrybuty

Model generalnie nie modeluje jednoznacznie rzeczywistego zagadnienia (mogą być różne poprawne modele, niektóre mogą być lepiej dostosowane do optymalnej realizacji w bazie)

Modeluje strukturę danych a nie działania na nich

## Diagramy związków encji (ERD)
* encje jako prostokąty (węzły)
* związki jako linie (krawędzie)
* opisana krotność związku (0, 1, n) - jeden do wielu, wiele do wielu itp.

Atrybuty wyliczane - zależą od liczności powiązanych encji, wyznaczane dynamicznie

UML

## Encja
Fizycznie istneijący lub koncepcyjny obiekt

* Typ encji
  * określa zbiór encji
  * ma nazwę i atrybuty
* Instancja encji - specyficzne wystąpienie encji

### Silne i słabe
* Słabe encje - nie może istnieć w bazie samodzielnie bez odpowiedniej instancji innej encji
* Silne encje - nie są zależne od istnienia innych encji


## Atrybuty
* Cecha, właściwość encji lub związku
* Ma określoną dziedzinę dozwolonych wartości
* Atrybut prosty - niepodzielny (atomowy)
* Atrybut złożony - może być podzielony na mniejsze, prostrsze
  * Nie jest oczywiste co jest atrybutem a co powiązaną encją (adres), uznaniowe.
* Atrybut pochodny - zależy od innych atrybutów, wyliczalny


## Klucze
Klucz to zbiór atrybutów jednoznacznie identyfikujący encję. Na atrybuty encji można nałożyć ograniczenie unikalności.


## Związki
Encje mogą być wzajemnie połączone przez związki

* typ związku
* element związku - jeden z typów połączonych encji
* egzemplarz związku - instancja
* atrybuty związku
* stopień typu związku
* nazwy ról w związku (etykiety na krawędziach)

Krotność - 0, 1, wiele, m..n

Wykluczenie - jeśli encja jest w jednej relacji to nie może być w drugiej


## Więzy integralności
Definiowanie dziedzin i semantycznych warunków poprawności

* klucze
* więzy jednoznaczności
* integralność referencyjna
* integralność domenowa
* więzy zasadnicze


## Decyzje na poziomie koncepcyjnym
* dokładność - powinien odzwierciedlać specyfikację
* unikanie redundancji
* prostota
* wybór włściwych związków
* dobór właściwych elementów do modelowania obiektu świata rzeczywistego


## Model EER
Rozszerzony model ER, powiązany z modelem obiektowym - podklasy, agregacja itd.