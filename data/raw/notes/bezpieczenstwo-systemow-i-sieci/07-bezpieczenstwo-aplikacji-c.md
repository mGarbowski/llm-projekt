# Bezpieczeństwo aplikacji C/C++

## Organizacja pamięci programu
* W pliku na dysku
	* instrukcje programu
	* dane o wymaganych bibliotekach
	* dane wstępnie zianicjowane
* W pamięci dodatkowo rezerwowana przestrzeń na
	* stos
	* stertę

### Stos
* Struktura danych typu LIFO
* Operacje push i pop
* W procesorze x86
	* realizacja skoków do funkcji i powrotu z funkcji do miejsca wywołania
	* przekazywanie parametrów wywołania funkcji
	* alokacja zmiennych lokalnych
	* rejestr ESP - wierzchołek stosu
	* stos rośnie w kierunku mniejszych adresów
	* wrzucanie argumentów wywołania funkcji na stos w odwrotnej kolejności - zaleta jest taka, że można obsłużyć zmienną liczbę argumentów (np. `printf`)

## Przepełnienie bufora
* Nadal bardzo powszechny typ ataku
* Bufor jako zmienna lokalna funkcji na stosie - tablica o zadanej wielkości
* Na stosie znajduje się też adres powrotu z funkcji
* Kopiowanie danych do bufora bez sprawdzenia ich długości może prowadzić do nadpisania adresu powrotnego
* Jako adres powrotny można podać początek bufora
	* w buforze umieszcza się dane do zinterpretowania jako kod wykonywalny (shellcode)
	* bajt `0x90` - instrukcja nop (nic nie robi)

### Atak na podatną funkcję
* Analiza podanych przez użytkownika parametrów
	* szczególnie interesujące jeśli program działa z suid - daje uprawnienia root'a
* Analiza zawartości pliku
	* odpowiednio spreparowany plik
	* można np. wysłać pocztą
* Parsowanie komunikatów sieciowych
	* analiza danych przychodzących z sieci
	* odpowiednio spreparowany komunikat sieciowy

## Zabezpieczenia przed buffer overflow
* Edukacja programistów
	* nie pisanie podatnych funkcji
* Audyt kodu
	* zastosowanie automatycznych narzędzi do wykrywania niebezpiecznych fragmentów kodu
* Mechanizmy ochronne kompilatora
	* kanarki
* Mechanizmy ochronne systemu
	* bit NX
	* ASLR

### Kanarki
* Stack Canaries
* Nazwa od kanarków używanych w kopalniach
* Umieszczenie losowo generowanej zmiennej na stosie przed adresem powrotu
* Zweryfikowanie przed wywołaniem `ret` że wartość nie została zmieniona
* Opcja GS w kompilatorze Visual Studio

### Bit NX, mechanizm DEP
* W systemie wykorzystującym pamięć wirtualną można oznaczyć strony stosu jako niemożliwe do wykonania
	* próba wykonania instrukcji z takiej strony zgłasza przerwanie sprzętowe
* Różne nazwy na różnych systemach operacyjnych i procesorach
	* NX - no execute (ogólna nazwa)
	* XD - execute disabled (Intel)
	* Enhanced Virus Protection (AMD)
	* DEP - Data Execution Prevention (Windows)
* Bit NX to mechanizm sprzętowy, nie każdy mikrokontroler to wspiera

### ASLR
* Address Space Layout Randomization
* Jeśli adresy pewnych sekcji programu są losowane to utrudnia pisanie exploitów
* Wymusza losowanie istotnych adresów
	* adres bazowy programu
	* adresy bazowe bibliotek
	* adres bazowy stosu
	* adres bazowy sterty
* Problemy
	* nie każdy system operacyjny to wspiera
	* stare biblioteki tego nie wspierają
	* dla bibliotek dzielonych, wartości są losowane przy restarcie systemu
	* wartości były losowane z małej puli


## Ataki na mechanizmy obrony
* DEP
	* ataki nie wykonują kodu na stosie
	* return to libc
	* return oriented programming
* ASLR
	* odgadnięcie lub poznanie wylosowanych adresów
	* format string

### Return to libc
* Nie nadpisuje adresu powrotnego adresem bufora
	* wykrywane przez mechanizm DEP
* Przygotowanie na stosie wartości odpowiadających prawidłowemu wywołaniu funkcji z libc
	* można tak manipulować wartościami, żeby połączyć kilka wywołań funkcji
* Nadpisanie adresu powrotu adresem funkcji z libc
	* legalne wywołanie, nie zostanie zablokowane

### Return oriented programming
* Ataki return to libc pozwalają tylko na wykonanie ograniczonych funkcji
* Dobiera się odpowiednie fragmenty funkcji w kodzie programu i nie skacze się na ich początek tylko na kilka ostatnich instrukcji
* Gadżet fragment kodu wykonujący pożądane instrukcje
* Przy odpowiednio dużym programie można w ten sposób zrealizować dowolną funkcjonalność
* Atak polega na dobraniu odpowiedniego zestawu gadżetów i odpowiednim spreparowaniu stosu
	* końcówki funkcji będą na ogół wykonywać instrukcje `pop` do rejestrów
	* umieszcza się na stosie wartości, które mają się znaleźć w rejestrach
	* umieszcza się adresy gadżetów nadpisujące adresy powrotu
	* dla wywołania wielu gadżetów jeden po drugim
* Można zaatakować nawet architekturę Harvard z oddzielną pamięcią dla programu
* Są narzędzia które znajdują komplety gadżetów w binarnym programie
* Kanarki mogą przed tym obronić

## Sterta
* Obszar pamięci przydzielanej procesowi na którym można dokonywać dynamicznej alokacji (`malloc`)
	* zaalokowaną pamięć należy zwrócić kiedy nie jest już używana (`free`)
* Bloki pamięci przydzielone procesowi są zarządzane za pomocą dynamicznych struktur danych
	* listy dwukierunkowe
* Ataki przepełnienia sterty są mniej oczywiste i wymagają dokładnej analizy kodu
	* nadpisanie wewnętrznych struktur sterty
	* nadpiasnie pamięci zaalokowanej dla obiektu
	* nadpisanie wskaźnika funkcji wirtualnej obiektu
* Obrona
	* edukacja programistów
	* dodanie warunków sprawdzających integralność struktur danych sterty
	* NX i ASLR
	* wykrywanie Heap Spraying przez oprogramowanie HIDS

### Heap Spraying
* Największym problemem ataków na stertę jest nieprzewidywalność alokacji
* Bardzo duże obszary pamięci alokowane dynamicznie muszą być umieszczone pod łatwo przewidywalnymi adresami

## Błędy z łańcuchami sterującymi
* Ataki przy wywołaniu `printf(buffer)` zamiast prawidłowego `printf("%s", buffer)`
* Odpowiednio sformatowane dane mogą zostać potraktowane jako łańcuch sterujący
* Znacznik `%n` pozwala na nadpisanie spreparowaną wartością adresu znajdującego się na stosie
* Umożliwia odczytanie pewnych adresów i poznanie ich przez atakującego
	* obejście dla ASLR