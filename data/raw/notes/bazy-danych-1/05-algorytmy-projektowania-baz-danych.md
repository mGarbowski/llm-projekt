# Wykład 06 (2023-03-30)

Kolos - 30 zadań bez cofania na 30 minut na Moodle

O 16:45-17:15, od 16 otwarte teamsy

## Projektowanie schematu
Równoważne bazy danych - te same zapytania dają te same rezultaty, Można matematycznie udowodnić równoważność dwóch baz

## Domknięcie
Domknięcie zbioru zależności funkcyjnych F nad zbiorem atrybutów - zbiór wszystkich zależności funkcyjnych będący
konsekwencją zbioru F (wywnioskowanych za pomocą reguł wnioskowania)

Równoważność - dwa zbiory zależności funkcyjnych generujące to samo domknięcie

Połączenie przez relacje przechodnią

Startuje się z określonym zbiorem i rozszerza do domknięcia i szuka się najmniejszego zbioru, z którego można by dojść
do tego samego domknięcia

### Przykład
F = {B->A, D->A, AB->D}

## Aksjomaty Armstronga
Reguły wyprowadzania dla zalezności funkcyjnych, poprawne i kompletne.

1. zwrotność X jest podzbiorem Y => Y->X
2. poszerzalność X->Y => XZ->YZ
3. przechodniość X->Y i Y->Z => X->Z

### Wyprowadzalne z aksjomatów

1. psudoprzechodniość X->Y i YW->Z => XW->Z
    * poszerzalność X->Y => XW->YW
    * przechodniość XW->YW i YW->Z => XW->Z
2. addytywność X->Y i X->Z => X->YZ
    * X->Y => XZ->YZ
    * X->Z => XX->XZ => X->XZ
    * X->XZ i XZ->YZ => X->YZ
3. dekompozycyjność

### Domknięcia zbioru atrybutów
Do wyznaczenia domknięcia zbioru atrybutów korzysta się ze zbioru zależności funkcyjnych

Do wyznaczania domknięcia zbioru zależności funkcyjnych używa się aksjomatów Armstronga

## Równoważność zbiorów zależności funkcyjnych
Zbiór zależności funkcyjnych F pokrywa zbiór zależności funkcyjnych E, jeśli każda zależność funkcyjna ze zbioru E
występuje w zbiorze F+

Dwa zbiory zależnośći funkcyjnych E i F są równoważne jeśli E+ = F+

Pokrycie minimalne zbioru zależności funkcyjnych E to najmmiejszy zbiór zależności F taki że

* Każda zależność w zbiorze F posiada po prawej stornie pojedynczy atrybut
* dowolna zależność funkcyjna ze zbioru zależności E występuje w domknięciu F+ zbioru F
* ...

## Atrybut nadmiarowy

## Atrybut znajdowania pokrycia minimalnego zbioru zależności funkcyjnych

### Przykład
Relacja {A,B,D}
E = {B->A, D->A, AB->D}

...
