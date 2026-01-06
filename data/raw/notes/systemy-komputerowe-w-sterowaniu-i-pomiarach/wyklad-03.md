# Wykład 3 (2024-03-04)
...

## Przykłady ...

### Cyfrowe przesyłanie głosu (VoIP)
* Zdigitalizowane pakiety głosu wysyłane w stały tempie co 10-30ms
* Maksymalne opóźnienie 150ms
* Nie zachowanie wymagań czasowych nie jest katastrofalne ale obniża jakość
* Dopuszczalna jest strata małej części pakietów (trzaski)

## System reaktywny
* Elementy
    * Zdarzenie
    * Zadanie - moduł programu wykonywany niezależnie od pozostałych modułów
    * Reakcja
* Czas odpowiedzi (wykonania zadania) nie przekracza ograniczeń


## Ograniczenia czasowe
* Ostre (hard real-time)
    * każde przekroczenie ograniczeń może prowadzić do katastrofalnego błędu systemu
    * projektowanie na najgorszy przypadek
    * bardzo istotna jest prawidłowa metodyka
    * nie można przetestować na produkcji systemu sterowania reaktorem atomowym
    * konieczny jest udział człowieka w weryfikacji działania (bez czarnych skrzynek i AI)
* Łagodne (soft real-time)
    * przekroczenie ograniczeń stopniowo degraduje jakość systemu ale nie niszczy zupełnie
    * projektowanie na wartości przeciętne
    * np. sterowanie grzejnikiem w pomieszczeniu
* Sztywne (firm real-time)
    * pojedyncze przekroczenia ograniczeń mogą być tolerowane
    * liczne przekroczenia pogarszają jakość systemu
    * np. przesyłanie dźwięku, obrazu


## Problemy implementacji
* Brak środowisk uruchomieniowych w środowisku pracy
    * Nie wszystko można przetestować na fizycznym modelu
    * Nie wszystko da się skutecznie zasymulować programowo
* Ograniczone zasoby sprzętowe
* Trudna weryfikacja projektu
    * poprawność
    * terminowość
* Konieczność wiarygodnej weryfikacji i walidacji
* Dominuje C, rzadziej asembler


## Środowisko skrośne
* Na innej maszynie tworzy się system i na innej uruchamia
* Kompilacja skrośna - na inny target
* Emulator układowy
    * pośredni pomiędzy komputerem programisty a docelowym systemem


## Systemy sterowania i zarządzania
* Zazwyczaj struktura hierarchiczna
* Proste sterowniki blisko sprzętu

