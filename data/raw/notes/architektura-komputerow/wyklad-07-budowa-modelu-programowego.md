# Ciąg dalszy 


Predykaty - uogólnione znaczniki (zmienne boolowskie) przechowywane w procesorze, ponumerowane, instrukcje warunkowe odwołują się do predykatu po numerze


## Operacje warunkowe w jednostce wektorowej
Nie można zrobić rozgałęzienia zależnego od pojedynczej wartości bo wiele jest przetwarzanych na raz.

Możliwy jest tylko wybór między dwiema wartościami (operator trójargumentowy), zachodzi jednocześnie dla wszystkich. Oblicza się wektor warunków i dwa wektory wyników, potem łączone w wektor wynikowy

wylicza się maskę `m`

`x = (m & a) | (~m & b)`

procesory wspierają operację ANDN, nowe jednostki wyliczają to w jednej instrukcji

## Budowa aplikacyjnego modelu programowego

### Podejścia
* CISC - klasyczne
* RISC - nowoczesne
* VLIW
* Post-RISC - aktualne

## CISC
Complex Instruction Set Computer - komputer o liście złożonych instrukcji

architektury System360, VAX, x86, x86_64

* Jedna instrukcja maszynowa powinna umożliwić realizację jednej prostej instrukcji w języku wysokiego poziomu
* Wszystkie zmienne zadeklarowane przez programistę są na stałe przechowywane w pamięci, procesor musi sięgać do pamięci, rejestry procesora pełnią tylko rolę tymczasową, trzymają wyniki pośrednie, nie trzymają obiektów programu
* Instrukcje mają różne długości
* Instrukcje operują na argumentach o różnej długości (oddzielne dodawanie 8, 16, 32 bitowe), długość argumentu zapisana w instrukcji
* Stos w pamięci i operacje na stosie (push, pop, skok ze śladem)
* Najczęściej model znacznikowy operacji warunkowych
* Instrukcje dwuargumentowe - wynik zastępuje argument źródłowy

### Problemy
* wymaga złożonej jednostki wykonawczej (duża skomplikowana, mikroprogramowana)
* duża liczba odwołań do pamięci
* duża liczba i złożoność trybu adresowania

## RISC
Reduced Instruction Set Computer - komputer o liście uproszczonych instrukcji

architektury MIPS, SPARC, POWER_IBM
RISC-V

* Główna koncepcja - skalarne dane lokalne procedury są przechowywane w rejestrach procesora
  * mniej odwołań do pamięci
  * przeładowanie rejestrów przy wywoływaniu procedur (prolog i epilog)
* Większa liczba rejestrów
* Operacje trujargumentowe - źródło nie jest niszczone, bo są tam trzymane dane
* Tylko jeden tryb adresowania realizowany sprzętowo
  * prostsze kodowanie instrukcji
  * zazwyczaj tylko tryb rejestrowy pośredni z przemieszczeniem


* Proste instrukcje - prostsza jednostka wykonawcza (nie wykorzystuje mikroprogramu)
* Każda instrukcja ma tylko 1 argument docelowy - wyklucza operacje stosowe (bo push i pop są dwuargumentowe)
* Złożone operacje można złożyć z kilku instrukcji (w tym tryby adresowania)
* Instrukcje arytmetyczne i logiczne operują tylko na rejestrach i argumentach natychmiastowych
* Dana zajmuje cały rejestr i operacje arytmetyczne działają na całych rejestrach (nie ma oddzielnych operacji)
* Architektura load-store, procesor operuje na pamięci tylko poprzez ładowanie z pamięci do rejestru i składowania z rejestru do pamięci
  * jedyne instrukcje, któe wymagają podania długości argumentu

* Stała długość instrukcji
  * potrzeba ich więcej
  * program zajmuje więcej pamięci
  * rozpoznawane przez układ kombinacyjny - szybkie
* Proste operacje wymagają wielu instrukcji
* Problem z ładowaniem stałej do rejestru
  * załadowanie stałej 32-bitowej wymaga dwóch instrukcji


## VLIW
Very Long Instruction Word

* procesor jest złożony z kilku jednostek
* wykonuje operacje równolegle
* instrukcji są grupowane w paczki, każda operacja wykonywana przez inną część procesroa 


## Post-Risc
Ewolucja architektury RISC, wygodniejsza i wydajniejsza

* Dwie długości instrukcji
  * kompromis
  * wsparcie dla push i pop

ARMv6, 7, 8, 9
* instrukcje 16 i 32-bitowe
* rejestr śladu
* wielokrotny push i pop - cały prolog lub epilog w jednej instrukcji


## Zapis binarny instrukcji
* CISC - różne długości
* RISC - jedna długosć
* Post-RISC - dwie długości

### Budowa
* kod operacji
* specyfikacja celu / argumentów


## Skok
* bezwarunkowy
  * statyczne - na stały adres docelowy
  * zmienny adres docelowy (z rejestru albo z pamięci, return jest skokiem dynamicznym)
* warunkowy

* jump - skok bezwzględny, w instrukcji podana wartość ładowana do PC
* branch - skok względny, w instrukcji podana wartość dodawana do PC (przemieszczenie)