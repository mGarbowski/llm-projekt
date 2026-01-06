# Wzajemne wyklucanie i synchronizacja

## Kolokwium
* będzie podana jutro lista pytań
* to co było powiedziane że będzie to będzie
	* prosty skrypt shella (niedopuszczony bash)
	* 4 albo 5 pytań

## Algorytm Petersona
Wywołania `enter_region` i `leave_region`

Przykład jest dla 2 procesów ale da się uogólnić dla większej liczby

`turn == process` obsługuje przypadek kiedy procesy w tym samym czasie próbują wejść do sekcji krytycznej bo warunek może być spełniony tylko dla jednego z dwóch procesów
ten który ustawił turn na swoje id wejdzie jako pierwszy po tym jak drugi proces nadpisze `turn` swoim id


## Instrukcja `TSL`
Test and set lock  (xchg - exchange) - instrukcja assemblera
Dwa argumenty - rejestr i zmienna w pamięci
instrukcja wymienia zawartości miejscami
z punktu widzenia innych instrukcji (procesów, wątków) ta instrukcja jest atomowa, niepodzielna i to zapwewnia sprzęt (np. przez blokadę magistrali systemowej)

W języku C są wstawki assemblerowe

Można interpretować tą instrukcję jako `if (condition) then set flag`

```asm
enter_region:
	; w register musi być nie-zero na początku
	tsl register, flag
	cmp register, #0
	jnz enter_region
	ret

leave_region:
	mov flag, #0
	ret
```

ponieważ `tsl` nie może być przerwane przez inne instrukcje to tylko jeden proces zobaczy w rejestrze wartość `0`

## Wada aktywnego oczekiwania
* marnuje się czas procesora na busy loop
* możliwość blokady systemu przy wielopriorytetowym sposobie szeregowania procesów - inwersja priorytetów
* planista może przydzielić czas procesowi, który czeka na wejście do sekcji krytycznej - bez sensu

## Semafor
Remedium na rozwiązanie ze `sleep` i `wakeup`
p zawsze opuszcza bezwarunkowo ale może musieć wcześniej poczekać

Semafor pozwala realizować kontrolę przepływu

### Mutex
Semafor binarny
Służy tylko do zapewniania mechanizmu wzajemnego wykluczania w dostępie do sekcji krytycznej

Implementacja może być bardziej wydajna dla mutexu niż dla liczącego semafora

W implementacji można wykorzystać instrukcję `TSL`

## Monitory
Zbiór procedur, zmiennych i struktur danych zgrupowanych w module (obiekcie), tylko jeden proces może przebywać na raz w module (metodach obiektu)

Wzajemne wykluczanie jest zapewnione wewnętrznie w implementacji

Mądry programista może zaimplementować dobrą klasę i wystawić bezpieczny interfejs

instrukcje nie są atomowe ale to nie szkodzi bo o to dba monitor

koncepcje Hoare'a i Hansena działania operacji `signal`

`synchronized` w Javie jest niezalecane przez twórców