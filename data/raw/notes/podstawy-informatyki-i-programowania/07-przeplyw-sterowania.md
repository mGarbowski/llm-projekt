# Przepływ sterowania (control flow)

## Pętla
* procesor potrzebuje operacji porównania i zapętlenia
* potrzebuje skoku do początku bloku kodu
  * skoki przez modyfikację rejestru Program Counter


## Instrukcje porównania
Porównanie liczb to sprawdzenie wartości ich różnicy

| warunek | True jeśli a-b |
| ------- | -------------- |
| a > b   | dodatnia       |
| a < b   | ujemna         |
| a == b  | zero           |

Od tego są flagi ALU N (Negative) i Z (Zero)

### Liczba przeciwna
* A -> -A+1
* Dodanie do negacji 0 i 1 bitu przeniesienia

Dodawanie lub odejmowanie można zrealizować przez przepuszczenie argumentów do ALU przez multiplekser odpowiednio z afirmacją / negacją każdego bitu.

Przez połączenia wyjść rejestrów można zrobić operacjie bit-wise -> multipleksery i dodawanie 0 przez przeniesienie

Tak można zrealizować operację odejmowania `SUB`


## Instrukcje skoku
Skok warunkowy
* JZ - skacz jeśli zero
* JG - skacz jeśli większe
* JL - skacz jeśli mniejsze

Skok bezwarunkowy - JMP

Instrukcja skoku wymaga argumentu - adresu instrukcji do której chcemy skoczyć
* Można rozważyć skoki bliskie i dalekie
* Może nie potrzeba aż 64b adresu jeśli chcę skoczyć o kilka linijek dalej
* Adresowanie bezpośrednie i pośrednie


`JZ R0` skok pod adres, który siedzi w rejestrze R0

`JG [R1]` skok pod adres zapisany w komórce pamięci, której adres jest w rejestrze

```py
while i < 10:
    i += 1
```

```
    mov     [i], R0
START_WHILE_LABEL:
    sub     R0, 10
    jg      END_WHILE_LABEL
    jz      END_WHILE_LABEL
    add     R0, 1
    mov     A, R0
    jmp     START_WHILE_LABEL
END_WHILE_LABEL:
    mov     R0, [i]
```
Zmienna i siedzi w dwóch miejscach - pamięci i rejestrze. Może pojawić się hazard.

Wystarczy raz odczytać `i` z pamięci na początku i raz zapisać do pamięci na końcu. Dostęp do rejestru jest znacznie szybszy. Skopiowanie zmiennej z pamięci do rejestru jest dużą optymalizacją.

Label'e odpowiadają adresom instrukcji w pamięci
