# Zadania ARKO

## Wprowadzenie

### 1. Co to jest bajt
Najmniejsza adresowalna jednostka pamięci w komputerze, najczęściej 8 bitów ale niekoniecznie

### 2. Dlaczego do wyrażania pojemności pamięci operacyjnej powinno się używać krotności binarnych, a nie dziesiętnych?
Ponieważ komputer używa systemu binarnego

### 3. Dlaczego zasoby pamięciowe współczesnych komputerów mają budowę hierarchiczną?
Pamięć nie może być jednocześnie dowolnie duża i dowolnie szybka, parametry wzajemnie się wykluczają.

Hierarchiczna budowa umożliwia zróżnicowanie tych parametrów tak, żeby cała hierarchia pamięci była i szybka i pojemna

### 4. Jaka jest ogólna zasada przemieszczania obiektów pomiędzy warstwami hierarchii pamięci?
Najczęściej używane obiekty są przesuwane jak najwyżej (najszybsza pamięć) a nieużywane są spychane niżej (wolniejsza pamięć)

### 5. Jakie mechanizmy decydują o przemieszczaniu obiektów na stykach poszczególnych warstw hierarchii pamięci?
| styk                               | zarządzany przez                         |
|------------------------------------|------------------------------------------|
| rejestry-reszta                    | kompilator lub programista w assemblerze |
| cache-pamięć operacyjna            | sprzęt                                   |
| pamięć operacyjna-pamięć wirtualna | system operacyjny                        |
| pamięć wirtualna-system plików     | użytkownik lub program użytkowy          |
| lokalny-zdalny                     | użytkownik lub program użytkowy          |

### 6. Które dwie warstwy hierarchii pamięci są realizowane przy użyciu tej samej struktury i tego samego fizycznego urządzenia? Jakie jest to urządzenie?
Pamięć wirtualna i lokalny system plików fizycznie znajdują się na dysku (HDD/SSD)

### 7. Czym w taksonomii Skillicorna różni się połączenie procesora instrukcji z hierarchią pamięci instrukcji od połączenia procesora danych z hierarchią pamięci danych?
* procesor instrukcji - hierarchia pamięci instrukcji
  * przepływ jednokierunkowy
  * procesor wysyła żądanie pobrania instrukcji
  * hierarchia pamięci zwraca instrukcję
* procesor danych - hierarchia pamięci danych
  * przepływ jednokierunkowy -> procesor wysyła żądanie zapisu / odczytu
  * przepływ dwukierunkowy -> zapis / odczyt danych

### 8. Czym różni się „silne” od „słabego” sprzężenia procesorów w taksonomii Skillicorna?
* słabe sprzężenie - każdy procesor ma swoją hierarchię pamięci, procesory komunikują się przez odrębny kanał
* silne sprzężenie - wspólna hierarchia pamięci używana przez wszystkie procesory

### 9. Dlaczego w architekturze Harvard nie można wprowadzić nowego programu w czasie pracy komputera?
W architekturze Harvard dane i instrukcje są przechowywane w oddzielnych hierarchiach pamięci, instrukcje mogą być tylko odczytywane więc niemożliwe jest zmodyfikowanie programu

### 10. Na czym polega „wąskie gardło” w architekturze Princeton?
Ponieważ instrukcje i dane są przechowywane w tej samej pamięci, w danym momencie procesor może albo pobierać instrukcje albo operować na danych

### 11. Dlaczego w architekturze Harvard-Princeton nie jest możliwa automodyfikacja programu?
Górne warstwy hierarchii pamięci (cache) instrukcji i danych są od siebie oddzielone. Program użytkowy nie ma kontroli nad położeniem obiektów w hierarchii pamięci więc nie może dokonać automodyfikacji

## Reprezentacje danych

### 12. Jaką wagę ma najbardziej znaczący bit 16-bitowej liczby zapisanej w kodzie U2?
-(2^15)

### 13. Podać postaci binarne słów 8-bitowych reprezentujących liczby całkowite -120, -64, -21, -10, -5 i -1 w kodach U2, znak-moduł i spolaryzowanym o wartości podkładu 127.

### 14. Dlaczego w zapisie liczb zmiennopozycyjnych IEEE754 nie ma potrzeby przechowywania części całkowitej części znaczącej liczby?
W zapisie IEEE754 część całkowita wynosi domyślnie 1 więc nie ma potrzeby jej zapamiętywać

### 15. Podać postaci binarne słów 32-bitowych reprezentujących liczby -256, -19, -10.125, -0.75, 0.625, 10, 15.5, 16.5 w zapisie zmiennopozycyjnym IEEE binary32.

### 16. W jaki sposób można zmienić znak liczby zapisanej w kodzie U2 używając wyłącznie jednoargumentowych operacji logicznych i arytmetycznych?
Zanegować wszystkie bity i dodać 1
```asm
not eax
inc eax
```

### 17. W jaki sposób wykrywa się nadmiar podczas dodawania liczb w kodzie NKB, a jak podczas dodawania liczb w kodzie U2?
* NKB - przeniesienie z najbardziej znaczącego bitu
* U2 - XOR najbardziej znaczącego bitu i przeniesienia
### 18. Na czym polega naturalne wyrównanie danych?
* Dana w pamięci musi być zapisana pod adresem, który jest podzielny przez jej rozmiar
* Dostęp do danych jest najszybszy kiedy zajmują jak najmniej słów w pamięci
* 1 słowo pamięci - 1 przesłanie
* Wyrównanie naturalne zapewnia najszybszy możliwy dostęp niezależnie od długości słowa w pamięci

### 19. Narysować układ pól struktury o podanej deklaracji w języku C i określić wartość operatora sizeof dla tej struktury, przyjmując naturalne rozmiary typów dla 32-bitowego procesora z 8-bitowymi bajtami. (Poprawność rozwiązania można sprawdzić pisząc program w języku C wyświetlający wartości sizeof dla struktury i offsetof dla poszczególnych jej pól)

### 20. Dla podanej deklaracji struktury w języku C podać wartość operatora offsetof – przemieszczenie pola struktury względem początku struktury, przyjmując naturalne rozmiary typów dla 32-bitowego procesora z 8-bitowymi bajtami. (Poprawność rozwiązania można sprawdzić pisząc program w języku C wyświetlający wartości sizeof dla struktury i offsetof dla poszczególnych jej pól). 

### 21. Naszkicować orientacyjną mapę przestrzeni adresowej procesu użytkowego w kilku systemach operacyjnych na podstawie wartości adresów obiektów należących do różnych sekcji, wyświetlanych przez program napisany w języku C. 

### 22. Na podstawie mapy z poprzedniego zadania oszacować, czy dany system operacyjny narzuca istotne ograniczenie na rozmiar sterty i stosu, wynikające z samych wartości adresów poszczególnych sekcji. 

### 23. Znając wartość danej 32-bitowej oraz jej adres określić adresy i wartości poszczególnych jej bajtów przy konwencji adresowania little-endian i big-endian

## Użytkowy model programowy 

### 24. Co wskazuje rejestr PC podczas wykonywania instrukcji (po jej pobraniu)? 
* Adres następnej instrukcji w pamięci - nextPC, w sekcji TEXT
* W przypadku skoku jest ładowany adresem docelowym
* Inkrementowany podczas pobierania instrukcji tak, że kiedy instrukcja się wykonuje to PC wskazuje na następną

### 25. Wymienić i scharakteryzować sekcje pamięci programu jednowątkowego (czas życia, rozmiar stały/zmienny, zawartość). 
* Kod (TEXT)
  * zawiera instrukcje programu
  * może zawierać stałe dane - tabele dla `switch`, literały
  * statyczny - obecny w pamięci przez cały czas życia programu
  * tylko do odczytu
  * adresy określone przed uruchomieniem programu (najpóźniej podczas ładowania do pamięci)
* Dane statyczne (STATIC)
  * stałe (RODATA)
  * zmienne zainicjowane (DATA)
  * zmienne niezainicjowane (BSS)
    * zerowane na początku
  * czas życia równy czasowi życia programu
  * stały rozmiar
  * adresy określane przed uruchomieniem programu
* Dane dynamiczne automatyczne (STACK)
  * stos
  * argumenty i zmienne lokalne procedur
  * zmienny rozmiar, tworzone i usuwane w trakcie działania programu
  * kolejność usuwania odwrotna do kolejności tworzenia
  * oddzielne dla każdego wątku
  * położenie określone przed uruchomieniem wątku
* Dane dynamiczne kontrolowane (HEAP)
  * sterta
  * tworzone i usuwane jawnie przez programistę (`malloc`, `free`)
  * czas życia nie jest związany z zakończeniem procedur
  * dowolna kolejność tworzenia i usuwania
  * alokowane przez procedury biblioteki standardowej języka, która korzysta z funkcji systemowych
  * przypisanie adresów w chwili tworzenia
  * 
### 26. Jakie dodatkowe sekcje pamięci muszą, a jakie mogą występować w programach wielowątkowych? 
* Każdy wątek musi mieć własny stos
* Opcjonalnie wątki mogą mieć własne dane statyczne
  * zainicjowane (TDATA)
  * niezainicjowane (TBSS)


### 27. Opisać czynności wykonywane kolejno przez procesor podczas wykonania instrukcji PUSH i POP na stosie „pełnym schodzącym”. 
* pełny - wskaźnik stosu wskazuje na ostatnio dodaną wartość
* schodzący - rośnie w storne niższych adresów
* PUSH
  * dekrementacja wskaźnika stosu
  * składowanie danej pod adresem wierzchołka stosu
* POP
  * załadowanie danej z wierzchołka stosu
  * inkrementacja wskaźnika stosu

### 28. Opisać czynności wykonywane kolejno przez procesor podczas wykonania instrukcji PUSH i POP na stosie „pustym wchodzącym”. 
* pusty - wskaźnik stosu wskazuje na następną wolną komórkę pamięci (?)
* wchodzący - rośnie w stronę większych adresów (?)
* PUSH
  * składowanie danej pod adresem aktualnego wierzchołka stosu
  * inkrementacja wierzchołka stosu
* POP
  * dekrementacja wierchołka stosu
  * ładowanie danej spod adresu aktualnego wskaźnika stosu

### 29. Znając wartość danej 32-bitowej oraz wartość początkową wskaźnika stosu określić adresy i wartości poszczególnych jej bajtów po umieszczeniu jej na stosie „pełnym schodzącym” przez procesor działający w konwencji little-endian. 

### 30. Na czym polega wykonanie instrukcji skoku ze śladem? 
Zapamiętanie wartości nextPC w rejestrze i załadowanie adresu skoku do PC

### 31. Jakie instrukcje procesora są używane przez kompilator do dzielenia przez potęgi dwójki liczbzapisanych w kodzie (a)NKB (b)U2?
* NKB - SHR - przesunięcie logiczne w prawo
* U2 - SAR - przesunięcie arytmetyczne w prawo

### 32. Podać wartość dziesiętną liczby w kodzie U2, która jest wynikiem wykonania na podanej liczbie (np. -66, -12, 130) zapisanej w U2 operacji przesunięcia o jeden bit (a) logicznego wlewo, (b) logicznego w prawo, (c) arytmetycznego w prawo. 

### 33. Czym różni się instrukcja x86 SUB (odejmowanie) od CMP (porównanie)?
`CMP` nie zapisuje nigdzie wyniku, tylko ustawia znaczniki (do późniejszego wykorzystania np przy skoku warunkowym)

### 34. Dlaczego adresowanie ramki stosu przy użyciu wskaźnika ramki jest na ogół wygodniejsze, niż przy użyciu wskaźnika stosu? 
* Jest wygodniejsze, ponieważ procedura może operować na wskaźniku stosu więc zmienają się offsety pod jakimi znajdują się zmienne (względem SP)
* Wskaźnik ramki stosu nie zmienia się w trakcie wykonywania ciała procedury więc offsety są stałe

### 35. Narysować ramkę stosu funkcji o podanej deklaracji zgodnie z konwencją wołania x86 oraz określić  adresy argumentów i prawdopodobne adresy zmiennych lokalnych, zakładając, że obiekty w ramce stosu są adresowane względem wskaźnika ramki

### 36. Jakie tryby adresowania są niezbędne do implementacji języka wysokiego poziomu? 
* Rejestrowy bezpośredni `mov eax, ebx`
* Natychmiastowy `mov eax, 123`
* Jeden z trybów rejestrowych pośrednich
  * np. rejestrowy pośredni z przemieszczeniem `mov eax, [esp-8]`
  
### 37. Określić nazwy trybów adresowania argumentów podanej instrukcji asemblerowej x86. 
| Tryb adresowania                       | instrukcja               |
|----------------------------------------|--------------------------|
| Rejestrowy bezpośredni                 | `mov eax, ebx`           |
| Natychmisatowy                         | `mov eax, 123`           |
| Rejestrowy pośredni prosty             | `mov eax, [ebx]`         |
| Rejestrowy pośredni z przemieszczeniem | `mov eax, [ebx+4]`       |
| Dwurejestrowy pośredni                 | `mov eax, [ebx+ecx]`     |
| Absolutny                              | `mov eax, [x]`           |
| Indeksowy                              | `mov eax, [ebx + ecx*4]` |


### 38. Jaką informację przechowuje znacznik parzystości? 
Czy liczba jedynek w najmniej znaczącym bajcie wyniku operacji jest parzysta

### 39. Podać wartości znaczników x86 po wykonaniu instrukcji dodawania/odejmowania/operacji logicznej o podanych wartościach i długości argumentów/wyniku. 
* ZF - czy wynik operacji wynosi 0
* SF - kopia najbardziej znaczącego bitu wyniku
* CF - przeniesienie wychodzące z najbardziej znaczącego bitu wyniku (nadmiar dla liczb be znaku)
* OF - czy wystąpił nadmiar w kodzie U2
* AF - przeniesienie pomocnicze BCD
* PF - czy w najmniej znaczącym bajcie wyniku operacji jest parzysta liczba jedynek 

### 40. Na czym polega ortogonalność instrukcji względem trybów adresowania? 
W każdej instrukcji można użyć każdego trybu adresowania

### 41. Do jakich celów kompilatory języków wysokiego poziomu używają rejestrów w typowych architekturach CISC, a do jakich w RISC? 
* CISC
  * wykonywanie obliczeń
  * przechowywanie wyników pośrednich
  * typowo mała liczba rejestrów nie umożliwia przekazywania argumentów i zwracania wyników przez rejestry
* RISC
  * przekazywanie argumentów (skalarnych) do procedur
  * przechowywanie zmiennych lokalnych (skalarnych)
  * znaczne ograniczenie liczby odwołań do pamięci i przyspieszenie kodu
  * typowo duża liczba rejestrów umożliwia ograniczenie odwołań do pamięci

### 42. Dlaczego programy dla procesorów RISC na ogół zajmują w pamięci więcej miejsca niż równoważne im programy dla procesorów CISC?
* Instrukcje RISC mają stałą długość, często większą niż średnia długość instrukcji dla programu CISC
* Operację równoważną jednej instrukcji CISC często wymaga kilku instrukcji RISC

### 43. Dlaczego procesory RISC nie mają zwykle instrukcji ładowania do rejestru 32-bitowej danej natychmiastowej? W jaki inny sposób może być zrealizowana ta operacja? 
* Długość instrukcji jest stała, kiedy wynosi 32 bity to nie zmieści całej stałej 32-bitowej
* Można załadować 32-bitową daną natychmiastową używając dwóch instrukcji
  * `li` - load immediate najmniej znaczące 12 bitów
  * `lui` - load upper immediate, bardziej znaczące 20 bitów
* Można umieścić ją w pamięci jako daną statyczną

### 44. Dlaczego w architekturach RISC na ogół nie występuje instrukcja powrotu z procedury? Jaka instrukcja jest używana w tych architekturach do powrotu z procedur? 

### 45. Dlaczego w architekturze RISC-V nie ma instrukcji SUBI – odejmowania stałej natychmiastowej bez pułapki przy nadmiarze? 

### 46. Wymienić nazwy rejestrów x86 (w trybie 32-bitowym) i podać funkcje rejestrów, które mają sztywno przypisane zastosowanie.
* 32-bitowe
  * EAX - główny akumulator
  * ECX - licznik iteracji
  * EDX - dzielna / iloczyn (w mnożeniu/dzieleniu jednoargumentowym)
  * EBX
  * ESP - wskaźnik stosu
  * EBP - wskaźnik ramki
  * ESI - wskaźnik źródła (do instrukcji iteracyjnych)
  * EDI - wskaźnik przeznaczenia (do instrukcji iteracyjnych)
  * EFLAGS - rejestr stanu
  * EIP - licznik instrukcji
* 16-bitowe
  * AX
  * CX
  * DX
  * BX
  * SP
  * BP
  * SI
  * DI
* 8-bitowe
  * AH, AL
  * CH, CL
  * DH, DL
  * Bh, BL

### 47. Jaka instrukcja procesorów x86 służy do szybkiego mnożenia liczb całkowitych przez 3, 5 i 9? 
`LEA`

### 48. Jaki częsty błąd programisty, popełniany przy programowaniu asemblerowym, powoduje sygnalizację nadmiaru dzielenia w procesorze x86?
Nie rozszerzenie dzielnej (zerowanie rejestru edx lub dopełnienie bitem znaku)

### 49. W jakim celu w jednostkach wektorowych wprowadzono instrukcję iloczynu logicznego z negacją jednego z argumentów? 
* Dla umożliwienia realizacji przypisania trójargumentowego `x = cond ? a : b`
* Oblicza się wynik `a` dla `cond == true`
* Oblicza się wynik `b` dla `cond == false`
* Oblicza się maskę warunku - same `1` w miejscu elementu wektora, który spełnia warunek
* Sumuje się iloczyn maski z `a` z iloczynem zanegowanej maski z `b` - po to jest operacja `ANDN`

### 50. Jaką postać ma wynik instrukcji porównania danych wykonywanej przez jednostkę wektorową? 
* Ma postać maski bitowej
* Ta sama długość co wektor argumentu
* Zawiera same `1` na miejscach elementów wektora, które spełniają warunek i same `0` na miejscach elementów które nie spełniają 

### 51. Instrukcja PCMPEQB jednostki wektorowej MMX porównuje dwa 64-bitowe wektory 8-bitowych liczb całkowitych. Określić wartość wyniku tej instrukcji dla argumentów źródłowych 0x11222334455667788 i 0x1111444466667777. 
0x1100001100111100

|          |    |    |    |    |    |    |    |    |
|----------|----|----|----|----|----|----|----|----|
| v1       | 11 | 22 | 33 | 44 | 55 | 66 | 77 | 88 |
| v2       | 11 | 11 | 44 | 44 | 66 | 66 | 77 | 77 |
| v1 == v2 | 11 | 00 | 00 | 11 | 00 | 11 | 11 | 00 |


### 52. Czym różni się w zapisie binarnym i wykonaniu instrukcja skoku względnego (zwykle określana jako branch) od instrukcji skoku bezwzględnego (zwykle nazywanej jump)? 
* skok względny (branch) - w instrukcji zapisane jest przemieszczenie skoku - liczba dodawana do nextPC
* skok bezwzględny (jump) - w instrukcji zapisany jest absolutny adres - liczba ładowana do PC

### 53. W jaki sposób kończy się wykonanie programu działającego pod kontrolą systemu operacyjnego – skąd system operacyjny wie, która instrukcja programu jest ostatnią
Program kończy się wywołaniem odpowiedniej procedury systemowej (`exit`) (?)


## Jednostka wykonawcza procesora

### 54. Jakie warunki musi spełniać model programowy procesora, aby możliwa była realizacja tego procesora w postaci struktury jednocyklowej?
* Model programowy klasy RISC
* Architektura Harvard - stała pamięć programu typu ROM

### 55. Jaką operację realizuje jednostka arytmetyczno-logiczna podczas wykonywania instrukcji ładowania i składowania w procesorze jednocyklowym i w prostych procesorach potokowych?
Oblicza adres danej - suma zawartości rejestru bazowego i przemieszczenia

### 56. Podać przykład sekwencji instrukcji generującej hazard typu odczyt po zapisie (RAW).
```
add   t1, t2, t3
add   t4, t5, t1
```
* Wynik pierwszej instrukcji jest argumentem do kolejnej
* Druga instrukcja może pobrać zawartość t1 zanim pierwsza instrukcja zapisze wynik swojej operacji

### 57. Dlaczego usuwanie hazardu RAW przy użyciu obejść jest efektywniejsze, niż przy użyciu innych mechanizmów?
* Metoda administracyjna
  * Zakaz używania instrukcji powodujących hazard
  * Trzeba dodawać puste instrukcje `nop`
  * Instrukcje `nop` zajmą większość programu
* Wykrywanie i poślizg
  * Układ wykrywa hazard porównując numery rejestrów w poszczególnych stopniach potoku
  * Jeśli występuje hazard to stopnie IF i RD są zatrzymywane
  * Automatyczne wstrzykiwanie instrukcji `nop`
  * Będzie bardzo dużo takich zatrzymań (jak przy metodzie administracyjnej)
* Obejścia
  * Eliminuje hazard RAW bez wprowadzania żadnych opóźnień - najlepsza
  * Dodatkowe szyny z wyjść ALU i MEM na wejście RD
  * Wszystkie wyniki które już istnieją ale nie są jeszcze zapisane do rejestru/pamięci są dostępne do odczytu po szynie obejścia 

### 58. Dlaczego hazardu RAW przy ładowaniu danej z pamięci nie można usunąć bez wprowadzenia opóźnienia?
```
lw    t4, ...
add   t6, t5, t4
```

* Load-use penalty
* Dana jest dostępna w stopniu MEM a używana w stopniu RD
* Kiedy instrukcja używająca jest w stopniu RD to ładująca jest jeszcze w ALU - nie ma jeszcze danej
* Nie da się wyeliminować opóźnienia ze względu na odstęp między stopniami RD i MEM
* Odstęp można zredukować przez obejścia

### 59. Skąd bierze się opóźnienie skoków w architekturach potokowych?
* Opóźnienie skoku bierze się z odległości między stopniem IF i ALU
* Adres skoku jest wyliczany w stopniu ALU
* W stopniu RD już przebywa instrukcja która była po skoku - marnuje czas procesora

### 60. Co to jest skok opóźniony?
* Delayed branch
* Technika redukcji opóźnienia skoku używana w krótkich potokach
* Skok opóźniony - Wykonaj instrukcję bezpośrednio za skokiem i skocz
* Slot opóźnienia - miejsce na instrukcję za skokiem
  * wypełniony użyteczną instrukcją jeśli warunek skoku od niej nie zależy
  * wypełniony `nop` w przeciwnym wypadku

### 61. Dlaczego skoków opóźnionych nie stosuje się w architekturach o długich potokach?
* Więcej stopni potoku -> większa odległość między stopniem pobrania instrukcji a wyliczeniem adresu -> większe opóźnienie
* Slot opóźnienia się wydłuża ale rzadko daje się wypełnić użytecznymi instrukcjami
* Przewidywanie skoków jest bardziej skuteczną metodą

### 62. Wymienić dwa sposoby potokowych realizacji modeli programowych CISC.
* Procesor z transkodowaniem instrukcji
  * Instrukcje CISC transkodowane na RISC
  * potok RISC
* Potok CISC

### 63. W jakich procesorach występuje transkoder instrukcji i na czym polega jego działanie?
* Występuje w realizacji procesorów CISC z transkodowaniem i jednostką wykonawczą typu RISC
* Transkoder pobiera instrukcje CISC i zamienia je na sekwencje instrukcji RISC
  * 1-1 dla prostych instrukcji
  * 1-2..4 dla bardziej złożonych instrukcji
  * Bardzo złożone są trzymane jako procedury RISC i pobierane z pamięci ROM

### 64. Kiedy procesor superskalarny może równocześnie rozpocząć wykonanie dwóch lub większej liczby instrukcji?
Kiedy instrukcje nie zależą od wcześniejszych, które są kierowane do potoku w tym samym cyklu

### 65. W jakich architekturach występują hazardy WAR i WAW? W jaki sposób można je usunąć?
Występują w architekturach z superskalarnych (ze zmianą kolejności instrukcji)

Hazardy są powodowane przez wielokrotne używanie tych samych zmiennych (rejestrów procesora) do przechowywania różnych wartości

Hazardy rozwiązuje się przez dodanie większej liczby rejestrów, niewidocznych w modelu programowym i dynamiczne przypisywanie tych fizycznych rejestrów do rejestrów modelu programowego - register renaming

### 66. Dlaczego opóźnienie skoków i opóźnienie ładowania danych mają duży wpływ na wydajność współczesnych procesorów?
Współczesne procesory stosuję architekturę wielopotokową, opóźnienia związane ze skokami lub ładowaniem danych, które wstrzymują potoki powodują utratę cykli w każdym potoku względem idealnej wydajności.

W superskalarach opóźnienie jest o tyle gorsze że liczbe straconych cykli mnoży się przez liczbę potoków

### 67. Na czym polega fuzja instrukcji spotykana we współczesnych procesorach x86? Podać przykład instrukcji, które mogą podlegać fuzji
* Fuzja polega na łączeniu dwóch instrukcji programu w jedną wewnątrz procesora
* Często występujące pary (`cmp`, `jcc`) instrukcji CISC zamieniane na jedną instrukcję RISC 

## Kieszenie 

### 68. Co to jest linia kieszeni?
Pojedynczy element przechowywany w kieszeni, blok danych (dłuższy od słowa pamięci) + znaczniki (w tym adres)

### 69. Opisać optymalny algorytm wyznaczania ofiar w kieszeni.
Należy wymienić tą linię, która najdłużej nie będzie używana w przyszłości (nie da się zrealizować bo nie wiadomo co będzie będzie potrzebne w przyszłości).

Heurystyka LRU - należy wyrzucić tą linię która najdłużej nie była używana (nie jest faktycznie optymalny ale jest najlepszy możliwy do zrealizowania)

### 70. Podać przykłady fragmentów programów, przy wykonaniu których zastosowanie kieszeni asocjacyjnej z algorytmem LRU do wyznaczania ofiar daje wyniki znaczne gorsze/lepsze niż zastosowanie kieszeni bezpośrednio adresowanej.
* Najgorszy przypadek
  * zbiór roboczy większy od pojemności kieszeni
  * 100% chybień
  * W pierwszej iteracji pętli zapełni się n komórek kieszeni
  * Zapisanie w kieszeni n+1 komórki wymaga wyrzucenia pierwszej itd.
  * Przy kolejnej iteracji pętli każdą instrukcję po kolei trzeba pobrać z pamięci
* Idealny przypadek
  * zbiór roboczy mniejszy lub równy pojemności kieszeni
  * 100% trafień
  * kieszeń wypełni się w pierwszej iteracji pętli i każda kolejna będzie tylko czytać z kieszeni

### 71. Określić, które bity adresu służą do adresowania danych wewnątrz linii, które do wyboru zbioru, a które są używane w znacznikach adresów znając całkowitą pojemność kieszeni, jej asocjacyjność i długość linii. (Przyjmujemy, że przy dostępie do kieszeni używa się adresów wirtualnych.)
* 24 KiB, 6, 32 B
  * najmniej znaczące 5b na wybór bajtu z linii (1 z 32)
  * jest 24KiB / (6 * 32B) = 128 zbiorów -> 7 bajtów na wybranie zbioru
  * najbardziej znaczące (n-12)b w znaczniku 
* 32 KiB, 8, 64 B
  * 6b na wybór bajtu z linii
  * 6b na wybór 1 z 64 = 32KiB/(8*64B) zbiorów
  * (n-12)b w znaczniku
* 16 KiB, 2, 32 B
  * 5b na wybór 1 z 32 bajtów w linii
  * 8b na wybór 1 z 256 = 16KiB/(2*32B) zbiorów
  * (n-13)b w znaczniku
* 128 KiB, 8, 64 B
  * 6b na wybór 1 z 64 bajtów w linii
  * 8b na wybór 1 z 256 = 128KiB/(8*64B) zbiorów
  * (n-14)b w znaczniku

### 72. Od czego zależy współczynnik trafień kieszeni?
* Pojemności kieszeni
* Organizacji i algorytmu wymiany
* Wykonywanego programu

### 73. Podać wzór na średni czas dostępu hierarchii pamięci złożonej z dwóch poziomów kieszeni i pamięci operacyjnej.
Dostęp do danego stopnia = średni czas dostępu do tego stopnia + średni czas dostępu do reszty hierarchii pamięci
t_avg_n = h_n * t_n + (1-h_n) * t_avg_n+1

t_avg_l1 = h_l1 * t_l1 + (1-h_l1) * t_avg_l2
t_avg_l2 = h_l2 * t_l2 + (1-h_l2) * t_mem

### 74. Obliczyć średni czas dostępu do hierarchii pamięci o podanych parametrach (czasy dostępu, współczynniki trafień kieszeni).
* Czas dostępu L1 -> 1 cykl
* Czas dostępu L2 -> 5 cykli
* Czas dostępu pamięci -> 100 cykli
* Współczynnik trafień L1 -> 0.96
* Współczynnik trafień L2 -> 0.99

Średni czas dostępu do hierarchii
1 * 0.96 + (1-0.96) * (5 * 0.99 + (1-0.99) * 100) = 1.198

### 75. Jakie przesłania danych mają miejsce w przypadku chybienia odczytu kieszeni L1 powodującego chybienie/trafienie w kieszeni L2, jeśli kieszenie te współpracują na zasadzie inkluzywnej/wyłącznej?
#### Kieszeń inkluzywna
* Trafienie L2
  * L2 do L1
  * L1 do procesora
  * usunięcie ofiary z L1
* Chybienie L2
  * pamięć do L2
  * L2 do L1
  * L1 do procesora
  * usunięcie ofiary z L2 i tej samej linii z L1

#### Kieszeń wyłączna
* Trafienie L2
  * Wymiana linii między L1 i L2
* Chybienie L2
  * Ofiara z L1 do L2
  * Ofiara z L2 do pamięci
  * Linia z pamięci do L1

### 76. Podać przykład sytuacji (operacji wykonywanych w programie), gdy kieszeń z alokacją linii przy chybieniu zapisu (WB/WA) będzie działać wolniej, niż kieszeń bez alokacji (WB/NWA).
???

### 77. Kiedy może wystąpić niespójność zawartości kieszeni i pamięci operacyjnej?
Problem może wystąpić kiedy jest więcej niż 1 ścieżka dostępu do hierarchii pamięci

* Oddzielne kieszenie L1 do kodu i danych
* Dwa procesory z oddzielnymi kieszeniami L1 i wspólną resztą hierarchii
* Procesor z kieszenią i sterownik IO odwołujący się bezpośrednio do pamięci

## Zarządzanie zasobami

### 78. Na czym polega ochrona procesora?
* Na zapewnieniu, że żaden proces nie może zmonopolizować czasu procesora (system operacyjny przełącza procesy)
* Ograniczenie dostępu do specjalnych zasobów (np systemowy rejestr stanu dostępny tylko na poziomie uprzywilejowania systemu)
* Timer systemowy zgłasza wyjątek co określony czas, system operacyjny przejmuje kontrolę

### 79. Wymienić funkcje (zadania) systemu zarządzania pamięcią. 
* Sprzętowa relokacja - kilka zadań może wykonywać się jednocześnie i używać tych samych wartości adresów, które będą mapowane do innych fizycznych komórek pamięci w sposób niewidoczny dla zadania
* Ochrona
  * zabezpieczenie przed dostępem poza sekcje pamięci przydzielone do procesu
  * zabezpieczenie przed niewłaściwym dostępem do własnych sekcji pamięci procesu
    * zapis do sekcji stałych
    * zapis do sekcji kodu
    * wykonywanie instrukcji z sekcji danych
* Dynamiczna alokacja i dealokacja - powiększanie i zmniejszanie rozmiaru przestrzeni adresowej dostępnej dla procesu w trakcie jego pracy
* Wirtualizacja - uniezalenienie rozmiaru pamięci dostępnej dla zadania od faktycznie dostępnej pamięci operacyjnej (wielkość zamontowana w komputerze i stopień wykorzystania przez inne zadania)

### 80. Na czym polega i do czego służy sprzętowa relokacja adresów?
* Relokacja służy temu, żeby wiele zadań (np. o dokładnie tym samym kodzie i zahardkodowanych adresach) mogły poprawnie wykonywać się jednocześnie
* Polega na mapowaniu wirtualnych adresów używanych w programie przez jednostkę relokacji na fizyczne adresy komórek pamięci

### 81. Dlaczego adresy logiczne o wartościach bliskich 0 nie są na ogół dostępne dla programów użytkowych we współczesnych systemach operacyjnych?
(???) To gwarantuje że odwołanie do pamięci przez `nullptr` od razu spowoduje błąd

### 82. Jakie informacje zawiera deskryptor segmentu/strony? 
#### Deskryptor strony
* znacznik ważności
* znaczniki praw dostępu do strony
* fizyczny numer strony
* dodatkowe atrybuty wykorzystywane przez system operacyjny
  * no-execute
  * ...

#### Deskryptor segmentu
* adres bazowy segmentu
* rozmiar segmentu
* znacnzik ważności deskryptora
* prawa dostępu do segmentu
* dodatkowe pola
  * bity do wykorzystania przez oprogramowanie
  * dodatkowe znaczniki ...

### 83. W jaki sposób jednostka segmentacji generuje adres liniowy?
* Sumuje liniowy adres bazowy segmentu i adres wewnątrzsegmentowy (offset)
* Jeśli nie zgadzają się prawa dostępu / zakres adresu to zgłasza wyjątek

### 84. Co oznaczają bity dostępu i modyfikacji w deskryptorze strony? Kiedy i przez co są one zerowane i ustawiane w stan 1?
* bit dostępu - czy był odczyt ze strony
* bit modyfikacji - czy był zapis do strony
* ustawiane przez przez system operacyjny
* wykorzystywane przy mechanizmie zapisu typu write-back - strona jest zapisywana na dysk tylko jeśli naprawdę trzeba

### 85. W jakich sytuacjach jednostka segmentacji/stronicowania zgłasza błąd segmentu/strony?
* nieważny deskryptor
* tryb dostępu niezgodny z uprawnieniami określonymi w deskryptorze
* (jednostka segmentacji) adres wewnątrzsegmentowy przekracza rozmiar segmentu

### 86. Dlaczego do przechowywania deskryptorów stron używa się struktur tablicowo-drzewiastych, a nie zwykłych wektorów?
* Zastosowanie struktury tablicowo-drzewiastej eliminuje konieczność przechowywania przez każdy proces deskryptorów dla całej przestrzeni adresowej (4MiB w trybie 32-bitowym)
* Proces najczęściej wykorzystuje tlyko małą część przestrzeni adresowej
* Mniejsza tablica 2 poziomu przechowuje wskaźniki do tablic wykorzystywanych deskryptorów stron  albo puste wskaźniki
* Zmniejsza się narzut zajętej pamięci przez proces związany ze stronicowaniem

### 87. Co to jest „table walk”? 
Przeglądanie drzewiasto-tablicowej struktury deskryptorów stron z pamięci, konieczne po chybieniu bufora translacji

### 88. Skąd bierze się wysoki koszt czasowy chybień bufora translacji?
Chybienie bufora translacji wymaga wykonania kilku dostępów do pamięci, we współczesnych procesorach superskalarnych koszt czasowy odwołania do pamięci jest rzędu wykonania kilkuset instrukcji

### 89. Jakie deskryptory stron są oznaczone jako globalne i jakie znaczenie ma ten atrybut deskryptora?
* Deskryptory stron systemowych (ważnych dla wszystkich procesów) są oznaczane jako globalne
* Deskryptory z ustawionym znacznikiem nie są usuwane z bufora translacji przy przełączaniu procesów - oszczędność czasu

### 90. Jakie pola zawiera nieważny deskryptor strony? 
* znacznik ważności ustawiony na 0

### 91. Dlaczego rozróżnienie prawa dostępu do odczytu danych i do pobrania instrukcji wjednostce zarządzania pamięcią podnosi bezpieczeństwo systemu?
Uniemożliwienie pobrania danych i wykonania ich jako instrukcji zabezpiecza przed atakiem typu buffer overflow z wykonaniem wstrzykniętego kodu

### 92. Jednostka stronicowania procesora przechowuje deskryptory stron w strukturze tablicowo-drzewiastej, w której tablice mają rozmiar strony. Podstawowy rozmiar strony jest równy p,  a rozmiar deskryptora – d. Określić kolejno następujące parametry jednostki stronicowania, translującej adres wirtualny nie krótszy niż a bitów:- minimalną liczbę poziomów struktury tablicowo-drzewiastej,- maksymalną długość adresu wirtualnego przy tej liczbie poziomów,- budowę adresu wirtualnego – jego podział na indeksy tablic i adres wewnątrztrzstronicowy,- możliwe rozmiary „dużych” stron.Przykładowe dane: a) p = 8 KiB, d = 8 B, a = 40; b) p = 16 KiB, d = 8 B, a = 48; c) p = 8 KiB, d = 4 B, a = 32. 
### 93. Przyjmując parametry jednostki stronicowania z poprzedniego zadania, oszacować całkowity rozmiar prywatnych tablic deskryptorów stron najmniejszego procesu użytkowego korzystającego ze sterty, przy założeniu, że każda z czterech sekcji pamięci procesu jest opisana oddzielną tablicą stron o rozmiarze podstawowym.

## Wyjątki
### 94. Co to jest wyjątek?
Zdarzenie w systemie komputerowym wymagające przerwania wykonania bieżącego strumienia instrukcji i przekazania sterowania do systemu operacyjnego

### 95. Wymienić i scharakteryzować poszczególne klasy wyjątków, podać po kilka przykładów wyjątków poszczególnych klas.
* Asynchroniczne - nie wynikają z wykonywanych instrukcji lub niemożliwe do powiązania z konkretną instrukcją
  * przerwania
    * timer systemowy
    * przesunięcie myszy
    * wciśnięcie klawisza na klawiaturze
    * nadejście pakietu z sieci lokalnej
  * błędy krytyczne
* Synchroniczne - wynikające z wykonania instrukcje, obsługiwane natychmiast po wygenerowaniu
  * pułapki
    * wywołania systemowe
    * nadmiary operacji arytmetycznych
    * tryb śledzenia (do debuggowania)
  * błędy
    * naprawialne
    * nienaprawialne
    * naruszenie zasad ochrony procesora / pamięci
    * błąd wyrównania danych
    * próba wykonania niezdefiniowanej instrukcji

### 96. Czym różni się obsługa przerwań od obsługi innych wyjątków?
Obsługa przerwania może być odsunięta w czasie

### 97. Co wskazuje wartość licznika instrukcji zapamiętywana podczas obsługi wyjątków poszczególnych typów?
* nextPC
  * przerwania
  * pułapki wywołania systemu i śledzenia
* currentPC
  * pułapki sygnalizujące błąd wykonania (do identyfikacja miejsca błędu)
  * błędy (nie udało się wykonać instrukcji, nextPC jest niedostępny lub nieważny)

### 98. Dlaczego do wywoływania usług systemowych przez program użytkowy nie można użyć instrukcji skoku ze śladem? 
### 99. Czym różni się instrukcja powrotu z obsługi wyjątku od instrukcji powrotu ze zwykłej procedury.
Przy powrocie z obsługi wyjątku trzeba przywrócić rejestr stanu procesora (dostępne tylko na poziomie uprzywilejowania systemu)

### 100. W jaki sposób zmienia się priorytet procesora podczas obsługi przerwania? 
Procesor przyjmuje priorytet obsługiwanego przerwania

### 101. Jaka relacja musi zachodzić pomiędzy priorytetem przerwania i priorytetem procesora, aby przerwanie mogło zostać obsłużone?
Priorytet przerwania musi być wyższy od aktualnego priorytetu procesora

### 102. Co to jest „późne przybycie” przerwania?
* Opóźnienie obsługi przerwania o wyższym priorytecie zgłoszonym podczas obsługi przerwania o niższym priorytecie
* Opóźnienie wynika z podwójnego składowania kontekstu na stosie systemowym

### 103. Na czym polega łańcuchowanie przerwań, zrealizowane w architekturze ARMv6/v7?
* Dotyczy sytuacji kiedy podczas obsługi przerwania zostaje zgłoszony przerwanie o mniejszym lub równym priorytecie
* Przy powrocie z obsługi aktualnego przerwania, jeśli odtwarzany kontekst ma niższy priorytet niż oczekujące przerwanie, to nie odtwarza się tego kontekstu (mniejsze opóźnienie) i przechodzi od razu do obsługi oczekującego przerwania
* Nie wykonują się żadne instrukcje kodu o niższym priorytecie

### 104. Wyjaśnić różnicę pomiędzy poziomem zaufania i priorytetem procesora. 
### 105. Jakie informacje są zapamiętywane przez procesor podczas obsługi błędu strony?

### 106. Na czym polega restart instrukcji, stosowany przy obsłudze błędów?
Przywrócenie stanu procesora sprzed wykonania instrukcji, która wygenerowała błąd po powrocie z procedury obsługi błędu

### 107. Dlaczego we współczesnych architekturach przy obsłudze błędów przez procesor używa się metody restartu instrukcji, a nie kontynuacji?
Jest łatwiejsze przy spekulatywnym wykonywaniu instrukcji, nie wymaga odtwarzania kontekstu mikrokodu procesora w środku instrukcji

### 108. Jaki jest skutek wykonania przez program użytkowy instrukcji powrotu z obsługi wyjątku?
Przeładowanie zawartości rejestru stanu - możliwe tylko w trybie systemowym bo pozwala na zmianę poziomu uprzywilejowania

### 109. Co to jest błąd podwójny?
* Błąd pojawiający się podczas obsługi innego błędu (np. związany z zarządzaniem pamięcią)
* Nie ma ważnej wartości PC
* Jest błędem w systemie operacyjnym

### 110. Co to jest przechwycenie? 
### 111. Wyjaśnić zasadę ataku typu buffer overflow i rolę atrybutu strony executable w zapobieganiu tego typu atakom.
* Buffer overflow polega na wstrzyknięciu przez użytkownika kodu do pamięci (przy niebezpiecznym czytaniu stringa w C, bez sprawdzenia zakresu) i wykonaniu tego kodu
* Znacznik executable zabezpiecza przed tym atakiem w ten sposób, że nie zezwala na wykonywanie strony oznaczonej jako dane, tak jakby były instrukcjami

## Pamięć wirtualna
### 112. Jakie mechanizmy musi udostępniać procesor, aby mógł on pracować w systemie pamięci wirtualnej?
### 113. Opisać rolę poszczególnych składników sprzętowych i programowych w implementacji pamięci wirtualnej.
### 114. Kiedy strona zaalokowana dla procesu przez system operacyjny może mieć nieważny deskryptor?
### 115. Na czym polega „leniwa” alokacja pamięci?
### 116. Co to jest aliasowanie deskryptorów?

## Wejście-wyjście 
### 117. Dlaczego we współczesnych komputerach uniwersalnych w zasadzie nie stosuje się obsługi urządzeń wejścia-wyjścia przy użyciu aktywnego oczekiwania?
Aktywne oczekiwanie marnuje czas procesora czekając w pętli na gotowość urządzenia, kiedy zamiast tego, mógłby przełączyć się na wykonywanie innego zadania

### 118. Jakie urządzenia wejścia-wyjścia wymagają obsługi przy użyciu bezpośredniego dostępu do pamięci (scharakteryzować cechy takich urządzeń)?
* Szybkie urządzenia (dsykim sterowniki sieciowe, dźwiękowe, graficzne, USB)
* Obsługa z użyciem przerwań wymagałaby zbyt dużego narzutu związanego z obsługą przerwania przy każdej transmisji (a nie raz na blok jak w DMA)

### 119. Wymienić rejestry kanału bezpośredniego dostępu do pamięci i opisać sposób ich zaprogramowania przez system operacyjny oraz modyfikacji przez sprzęt podczas transmisji.
* Rejestr adresu bufora danych w pamięci
  * przed transmisją bloku danych ładowany adresem początkowym bufora
  * inkrementowany po każdym przesłaniu
* Licznik transmitowanych danych
  * ładowany długością bloku
  * dekrementowany po każdym przesłaniu

### 120. Wyjaśnić z czego wynikają ograniczenia żywotności popularnych urządzeń pamięci masowej – stałych dysków magnetycznych i urządzeń półprzewodnikowych (SSD, karty pamięci)
* Dyski magnetyczny - zużycie mechaniczne ruchomych talerzy i głowic
* Półprzewodnikowe