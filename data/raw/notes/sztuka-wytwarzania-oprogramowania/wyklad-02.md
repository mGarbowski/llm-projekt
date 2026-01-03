# Warsztat inżyniera oprogramowania (2024-02-26)
* Będzie swobodne przerzucanie między grupami z labów
* Zapisy na teams
* Wykłady są nagrywane


## Standardy kodowania
* Standard kodowania to też narzędzie
* Cel: usystematyzowanie procesu wytwarzania kodu i samego kodu
* Ujednolicenie przekłada się na lepszą utrzymywalność kodu i łatwiejszą pracę w zespole
    * Utrzymywalność - dobre oprogramowanie dzisiaj będzie też łatwo dostarczyć jutro (na inny system, z innymi wymaganiami itd.)
* Zbiór reguł ma pomagać osiągnąć zakładaną jakość
* Conventions / standards / style - stosowane zamiennie
* Standard to coś więcej niż głębokość wcięć
* Dojrzałość to stosowanie obowiązującego standardu, ważny jest konsensus


### Styl
* Wcięcia, białe znaki, klamerki, białe linie itd.
* Czasami są standardy opracowane przez twórców języków (PEP8), rozsądnie jest je stosować
* Styl nie musi być składnikiem standardu

### Nazewnictwo
* Notacja i semantyka
* Kod ma być czytelny i zrozumiały dla programisty
* Dobre nazywanie nie jest łatwe
* Zmienna to rzeczownik
* Funkcja to czasownik
* **zawsze** po angielsku

### Inne
* Komentowanie
    * Jak chcę napisać komentarz to może jednak da się ten kod napisać lepiej
    * Publiczne API, biblioteki należy komentować (kiedy wytwarzana biblioteka jest produktem)
* Długość funkcji, liczba parametrów
* Wykorzystywane paradygmaty
    * bardziej funkcyjnie czy obiektowo
* Reguły bezpieczeństwa
    * np. bez gołych pointerów
    * np. wszystkie parametry funkcji mają być `const`
* Reguły wynikające ze specyfiki przemysłu
    * np. bez dynamicznej alokacji

### Podsumowanie
* Nie ma jedynego poprawnego standardu
* Powinien być osiągany przez konsensus w zespole
* Przestarzałe standardy lepiej zmieniać ewolucyjnie
* Istnieją formalne standardy przemysłowe (np. MISRA C dla branży automotive)
* Istnieją de-facto standardy (DRY, SOLID, itd.)


## SOLID
* Reguły dobrego projektowania kodu obiektowego
* To nie są sztywne reguły, trzeba wyczuć jak daleko je stosować

### Single Responsibility Principle
* Klasa / funkcja powinna robić tylko jedną rzecz
* Stosuje się nie tylko do OO
* Klasę powinno się zmieniać tylko z jednego powodu (funkcjonalności)
* Jeśli opisuję klasę i używam "i" to coś może być nie tak

### Open-Closed principle
* Moduły powinny być otwarte na rozszerzenie, ale zamknięte na modyfikację
* Jeśli chcę dodać nowe rzeczy to klasa powinna to umożliwiać bez modyfikowania jej kodu
* Nie trzeba modyfikować kodu modułu żeby użyć go w inny sposób
* Zmiana innego modułu nie powinna wpływać na mój
* np. zapis do strumienia (bardziej ogólne) zamiast zapisu do pliku

### Liskov Substitution Principle
Funkcje, które używają referencji do klas bazowych, muszą być w stanie używać również obiektów klas
dziedziczących po klasach bazowych, bez dokładnej znajomości tych obiektów.

* Każdy obiekt pochodny powinien być dobrym zamiennikiem obiektu bazowego
* Każda klasa stanowi pewien kontrakt, LSP jest tu kluczowe
* Czy `Square` może dziedziczyć po `Rectangle`
    * nadpisanie `setWidth` i `setHeight` może złamać kontrakt tam, gdzie jest używana klasa bazowa
* Być może lepiej nie robić w ogóle `set` i zrobić wszystkie obiekty niemutowalnymi 

### Interface Segregation Principle
* Wiele dedykowanych interfejsów jest lepsze niż jeden ogólny
* Klient nie powinien być zmuszany by zależał od interfejsu, którego nie potrzebuje
* Niepotrzebne zależności wydłużają czasy budowania/kompilacji
* Jeśli klasa wykonuje zapis to może też wykonywać odczyt
    * Może łamać SRP, ale te operacje i tak są ze sobą mocno powiązane
    * Można implementować interfejsy `Serializer` i `Deserializer`
    * Kod wykorzystujący tą klasę może wybrać jeden z nich

```cpp
auto area(std::shared_ptr<Rectangle> r) {
    return r->width() * r->height();
}
```
Zależy i od `Rectangle` i `shared_ptr`

```cpp
auto area(const Rectangle &r) {
    return r.width() * r.height();
}
```
Jest lepsze bo zadziała dla każdego prostokąta (zależy tylko od 1 interfejsu)

Przykłady na kolosa zazwyczaj łamią wszystkie reguły


### Dependency inversion
* Abstrakcje nie powinny zależeć od konkretów tylko na odwrót
* Obiekty wysokiego poziomu i niskiego poziomu nie powinny zależeć od siebie nawzajem tylko od wspólnej abstrakcji
* Klasa, która reprezentuje koło nie powinna być rekompilowana po zaktualizowaniu sterowników GPU
* Jak jest problem to pewnie można wstawić warstwę abstrakcji


## Clean Code
Książka z 2009, z niej pochodzą zasady SOLID. Clean Coder też dobre.

