# Model fizyczny
* Na przykładzie bazy Oracle
* Wiele zagadnień dotyczy sytuacji, w której projektant bazy danych ma kontrolę / dostęp do fizycznego sprzętu na którym system będzie działał
	* nie ma zastosowania do chmury, czy złożonych macierzy dyskowych itp.
* Fizyczna niezależność danych
	* model fizyczny można modyfikować bez wpływu na model logiczny

## Struktura plików
* Pliki danych (data files)
	* rzeczywiste trwałe dane
* Pliki tymczasowe (temporary files)
	* sam system może potrzebować tymczasowych struktur do wykonywania niektórych poleceń
	* tabele tymczasowe - kończące życie na koniec transakcji
	* niekoniecznie zapisane na dysku (np. pliki w pamięci)
* Pliki dzienników (redo log files)
	* ochrona przed awarią
	* umożliwia odtwarzanie stanu bazy po awarii (włącznie z utratą plików danych)
* Pliki sterujące (control files)
	* gdzie szukać pozostałych plików na dysku

### Pliki dzienników
* Najważniejsze obiekty w całej bazie
* Stan można odtworzyć na podstawie dzienników
	* z dowolnego momentu w przeszłości
* Tworzą pętlę
	* muszą być co najmniej 2 online
	* po wypełnieniu pliku można go zarchiwizować (i trzymać całą historię bazy)
	* w Oracle tryb pracy Archive log
* Zapisuje informacje o tym co się stało w bazie danych
	* jakie operacje modyfikacji zostały wykonane
* System sekwencyjnie zapisuje wszystkie operacje
* Są stałej wielkości
	* po zapełnieniu system zamyka plik i przełącza się na kolejny
	* plik zostaje dostępny np. do zarchiwizowania
* Odtwarzanie
	* pliki danych podlegają backupowi
	* od backupu można odtworzyć na podstawie logu operacje
* Potrzebny jest dziennik pokrywający cały okres od ostatniego backupu
* W praktyce tworzy się i backup danych i backup dzienników
* Pliki online i offline
* Pliki online są zapisywane cyklicznie
* W trybie zapewniającym pełną ochronę przed awarią plik może być ponownie zapisany tylko wtedy, gdy został zarchiwizowany
	* system staje dopóki log nie zostanie zarchiwizowany
	* można wykonywać tylko odczyty
* Powstaje zbiór plików dziennika
	* pliki online z najnowszą historią zmian bazy
	* pliki offline, zarchiwizowane z dawniejszą historią
* W mniej bezpiecznym trybie pracy dostępne są tylko dzienniki online
	* najstarsze zostają nadpisane bez archiwizacji
* Jeśli backupy są robione częściej niż zapełnienie wszystkich plików logów online to nie są potrzebne logi offline
* Pliki dzienników przed awarią chroni replikacja
	* najlepiej na osobnych dyskach
	* zapis równoległy
	* bez pojedynczego punktu awarii
* Grupy plików
	* muszą być co najmniej 2 grupy
	* jedna jest aktywna, pozostałe dostępne do archiwizacji
	* system nie może funkcjonować, gdy wszystkie pliki grupy są niedostępne do zapisu
	* pliki jednej grupy powinny być umieszczone na różnych dyskach
	* fizyczna ochrona przed awarią

### Logiczna struktura danych
* Przestrzenie tabel (tablespaces)
* Segmenty (segments)
	* w ramach przestrzeni tabel
	* z grubsza odpowiadają tabelom
* Porcje (extents)
	* kawałek przestrzeni w ramach segmentu
	* składają się z bloków (odpowiedniość między blokiem systemu bazy danych a blokiem systemu operacyjnego)
* Nazwy z Oracle

### Cel projektu na poziomie plików
* Równomierne obciążenie dysków
* Równomierne rozłożenie obciążenia w czasie

### Przestrzenie tabel
* Przestrzenie danych
	* systemowe
	* pozostałe - normalne dane
* Przestrzenie przywracania (undo tablespaces)
* Przestrzenie tymczasowe (temporary tablespaces)
	* w plikach danych lub plikach tymczasowych
* Mogą być rozłożone dowolnie między dyskami
	* ręczna konfiguracja
* Strategia przydziału porcji do segmentu
	* liniowy przydział porcji równej wielkości
	* kolejne porcje 2 razy większe, logarytmiczny przyrost liczby porcji

### Segmenty użytkownika
* Tabela, partycja tabeli lub grono tabel (cluster)
	* jedna, część jednej, wiele
* Indeks lub partycja indeksu
* LOB lub partycja LOB
	* Large OBject
	* np. multimedia
	* lepiej przechowywać je w innym miejscu niż standardowe dane alfanumeryczne

### Segmenty systemowe
* Tymczasowe
	* tymczasowa przestrzeń dla zapytań
	* tabele i indeksy tymczasowe
* Przywracania (undo)
	* dla wykonywania operacji `ROLLBACK` - potrzebna są dane pierwotne sprzed transakcji
	* zapewnianie spójności odczytu
		* `SET TRANSACTION READ ONLY`
		* wszystkie operacje transakcji operują na stanie bazy danych z początku transakcji
		* inne transakcje modyfikujące dane w międzyczasie nie doprowadzą do niespójności odczytu
		* wykorzystuje ten sam mechanizm co do `ROLLBACK`
		* dane z zatwierdzonej transakcji nie są od razu kasowane tylko trzymane tak długo jak są potrzebne
	* wykonywanie zapytań historycznych (flashback)

### Zasady rozłożenia tabel i indeksów
* Indeksy powinny być umieszczone na innych dyskach niż indeksowana tabela
* Na ile to możliwe, należy każdy indeks tabeli umieszczać na oddzielnym dysku
* Duże tabele powinny być partycjonowane
	* równolegle należy partycjonować indeksy
* Jeżeli to możliwe, najczęściej używane tabele i indeksy powinny być umieszczone na najszybszych dyskach
* Małe tabele mają pomijalny wpływ na wydajność systemu
	* koszt bazodanowy liczy się w dostępach do dysku
	* system bazodanowy używa cache w pamięci operacyjnej
	* mała tabela może w całości mieścić się w cache - koszt bliski 0

## Partycjonowanie

### Cele
* Wzrost wydajności dzięki zmniejszemiu współzawodnictwa w dostępie do danych
* Wzrost wydajności dzięki zmniejszeniu wielkości przetwarzanych obiektów
* Ułatwienie administracji danymi dzięki separacji i zmniejszeniu wielkości obiektów
	* składowanie
	* odtwarzanie
	* przebudowa
	* łatwiej zrobić wiele małych backupów niż jeden duży
* Zwiększona dostępność dzięki możliwości wykonywania operacji na części danych

### Mechanizmy
* Partycjonowanie zakresowe (range partitioning)
	* przynależnośc do partycji jest określana na podstawie przynależności wartości klucza partycji do zakresu
	* klucz partycji to wybrana kolumna lub zbiór kolumn
	* ma sens kiedy dziedzina klucza partycji jest duża
* Partycjonowanie listowe (list partitioning)
	* przynależność do partycji jest określana na podstawie przynależności wartości klucza partycji do listy wartości
	* ma sens kiedy dziedzina klucza partycji jest mała
* Partycjonowanie losowe, mieszające (hash partitioning)
	* przynależność do partycji jest określana na podstawie wyniku funkcji mieszającej

### Partycjonowanie indeksów
* Każdy indeks można zdefiniować jako niepartycjonowany lub partycjonowany
* Partycjonowany indeks globalny (global partitioned)
	* partycjonowanie niezależnie od tabeli
* Partycjonowany indeks lokalny (local partitioned)
	* partycjonowanie indeksu identycznie jak tabeli
	* lokalny indeks prefiksowany (local prefixed) - klucz partycji jest kluczem indeksu (lub jego prefiksem)
		* dobre do partycjonowania po czasie
		* aktualne dane są w oddzielnej partycji
		* rzadko używane dane historyczne nie muszą być nawet przechowywane online (tylko backup)
	* lokalny indeks nieprefiksowany (local nonprefixed) - klucz partycji nie ma nic wspólnego z indeksem
		* punktowe wyszukiwanie danych wykonuje się dłużej
		* zrównoleglanie nie opłaca się do punktowego wyszukiwania małej liczby wierszy

#### Partycjonowany indeks lokalny
* Prosta i szybka przebudowa partycji indeksu przy zmianie partycji tabeli
* Niezależność partycji, wzrost dostępności
* Wygodny do obsługi danych w czasie, do tabel historycznych
* Możliwość redukcji partycji w zapytaniach
* Łatwa możliwość odtwarzania bazy do określonego punktu w czasie

#### Partycjonowany indeks globalny
* Kłopotliwa przebudowa partycji indeksu przy zmianie partycji tabeli
	* konieczna przebudowa wszystkich
* Brak niezależności partycji
* Możliwość redukcji partycji indeksu w zapytaniach
* Trudne odtwarzanie bazy do określonego punktów w czasie
	* koniecznośc odtworzenia wszystkich partycji

## Struktura fizyczna
* Pliki (files)
* Bloki (blocks)

### Blokowa struktura pliku
* Tabela o organizacji standardowej
* Wielkość bloku bazy danych jest skorelowana z wielkością bloku w systemie operacyjnym
* Wiersze są zapisywane w blokach
* Optymalna sytuacja to odpowiedniość 1 do 1 między blokiem bazy danych a blokeim systemu operacyjnego
* Organizacja oparta na rekordach byłaby niepraktyczna
	* przy rekordach stałej długości marnuje się miejsce na dysku na puste wartości (`NULL`, napisy mniejszej długości niż maksymalna)
	* przy rekordach zmiennej długości byłby problem przy wstawianiu danych
* Organizacja blokowa, bloki o organizacji rekordowej
* Blok bazodanowy może być wielokrotnością bloku dyskowego
	* do odczytu pojedynczego wiersza jest niewydajnie
	* do odczytu sekwencyjnego jest bardziej efektywne - tyle samo operacji dyskowych i mniej operacji systemu bazodanowego

### Struktura bloku
* Nagłówek bloku
	* dane bloku
	* katalog tabel
	* katalog wierszy
* Wiersze
	* nagłówek wiersza
	* liczba kolumn
	* ID klucza grona
	* ROWID następnika dla wiersza łańcuchowanego
	* kolumny
		* wielkość kolumny
		* dane kolumny

### Zarządzanie przestrzenią w blokach

#### Parametr `PTCFREE`
* Określa ile wolnego miejsca jest pozostawiane w bloku w celu zapewnienia miejsca na operacje `UPDATE`
* Jeżeli zajętość bloku spadłaby poniżej `PCTFREE`, blok usuwany z listy bloków wolnych
* Niskie
	* mało miejsca na operacje `UPDATE` - ryzyko migracji wierszy i spadku wydajności
	* wysokie wypełnienie bloków - efektywne wykorzystanie przestrzeni, efektywny przegląd
* Wysokie
	* dużo miejsca na operacje `UPDATE` - małe ryzyko migracji wierszy, stabilna wydajność
	* niższe wypełnienie bloków - niższa średnia wydajność

#### Parametr `PCTUSED`
* Określa taki poziom przestrzeni w bloku, że jeżeli zajętość spadnie poniżej niego, to blok powraca na początek listy bloków wolnych
* Niskie
	* szeroka histereza - rzadsza reorganizacja listy bloków wolnych
	* wyższa wydajność operacji modyfikacji
	* niskie średnie wypełnienie bloków - mało efektywne wykorzystanie przestrzeni
	* mało efektywny przegląd
* Wysokie
	* wąska histereza - częsta reorganizacja listy bloków wolnych
	* niższa wydajność operacji modyfikacji
	* wysokie średnie wypełnienie bloków
	* efektywne wykorzystanie przestrzeni
	* efektywny przegląd

### High Water Mark
* Gdzie był najdalszy `INSERT`
* `INSERT`y są wykonywane po kolei, więc wiadomo, że tu się kończy tabela
* Następny blok jest pusty, tu się kończy przegląd sekwencyjny
* Nigdy się nie cofa po operacjach `DELETE`
	* tylko po operacji `TRUNCATE
* W nowych wersjach Oracle jest lista bloków wolnych albo mapy bitowe`

### Położenie wierszy
* Standardowo wiersz mieści się w 1 bloku
* Łańcuchowanie wiersza (row chaining)
	* przechowanie wiersza w wielu blokach
	* kiedy wiersz jest większy niż blok
	* niekorzystne dla wydajności, lepiej podzielić tabelę pionowo tak, żeby wiersze mieściły się w jednym bloku
* Migracja wiersza (row migration)
	* przeniesienie całego wiersza do innego bloku, tak aby zmieścił się w bloku w całości
	* następuje po aktualizacji rośnie rozmiar wiersza i brakuje wolnego miejsca w bloku
	* bardzo niekorzystne dla wydajności
	* może wystąpić kiedy wiersz ma wiele kolumn, ale początkowo uzupełniana jest tylko ich mała część, w takiej sytuacji lepiej podzielić tabelę pionowo
* Podział wiersza
	* utworzenie kilku części wiersza, tak aby każda zawierała nie więcej niż 255 kolumn

## Metody dostępu do danych

### Indeks drzewiasty
* Struktura danych B+ dzrewa
	* zrównoważone, posortowane
* Wszystkie liście na tym samym poziomie
* Liście tworzą listę dwukierunkową
	* do wyszukiwania wielu kolejnych wartości (zakresowego)
* Liście zawierają `rowid` - adresy wierszy
* Węzły drzewa są blokami
	* takie same bloki jak w plikach bazy danych
	* bloki są spore (rzędu kilku kB)
	* dzrewa są niskie
	* wysokość zależy logarytmicznie od liczby wierszy (przy bardzo dużej podstawie)
	* wiele bloków mieści się w cache'u w pamięci operacyjnej
* Dostęp do danych wymaga wysokość drzewa + 1 dostępów dyskowych
	* z dokładnością do cache'owania węzłów
* Reorganizacja obciąża każdą z operacji `INSERT` `DELETE` i `UPDATE` na kolumnie klucza
* Może być używany do sortowania
* Może być używany do wyszukiwania zakresowego według porządku klucza
* Najbardziej uniwersalny typ indeksu
* Najlepiej funkcjonuje przy losowym wstawianiu klucza
	* przy monotonicznym wstawianiu będzie wypełniony w połowie
	* oracle pozwala odwrócić kolejność bitów i wstawianie monotonicznych wartości działa jak losowe
* Może wyszukiwać po całym kluczu lub po jego części

### Indeks mieszający (bezpośredni)
* Oparty na funkcji mieszającej
* Do segmentu tabeli jest przypisana określona liczba bloków
* Funkcja mieszająca jest modulo liczba bloków
* Wartość funkcji mieszającej od klucza wyznacza numer bloku do którego wiersz będzie wstawiony
* Nie wymaga żadnej struktury, żadnego dodatkowego miejsca na dysku
* Nie zostaje zaburzone przez wstawienia, modyfikacje, usunięcia
* Zapytanie wymaga 1 dostępu dyskowego w idealnym przypadku
* Nie może być używany do sortowania
* Zawsze wymaga całego klucza do wyszukiwania
* Nie ma możliwości wyszukiwania zakresowego
* Po zapełnieniu bloków silna degeneracja wydajności
	* są różne sposoby obsługi zapełnienia
	* w każdym wypadku występuje migracja wierszy
* Wymaga alokowania od razu całej przewidywanej wielkości segmentu tabeli
* Zmiana wielkości tabeli wymaga ponownego indeksowania (przepisania) całej tabeli
* Nie ma wskaźnika wysokiej wody, przegląd sekwencyjny wymaga przejrzenia wszystkich bloków
	* z bitmapami działa znacznie lepiej
* Można założyć tylko 1 indeks tego typu dla tabeli
	* organizuje położenie wierszy w tabeli

### Indeks mieszający pośredni
* Pośrednia struktura
	* hashmapa
	* hash bucket
* Funkcja mieszająca wyznacza pozycję w pośredniej strukturze
* Pośrednia struktura zawiera wskaźniki do wierzy w standardowo zorganizowanej tabeli
	* tabela zachowuje normalne cechy (poprawnie działający HWM)
* Dostęp do danych wymaga 2 odczytów z dysku (koszyka i samego wiersza)
* Wstępna alokacja dotyczy tylko koszyka, a nie tabeli
* Małe prawdopodobieństwo przepełnienia koszyka
* Może istnieć wiele indeksów tego typu na tabeli
* Wspierane w PostgreSQL i MySQL

### Grono tabel (cluster)
* Dla obu tabel stosuje się ten sam indeks mieszający
	* np. faktury i pozycja na fakturze
	* do funkcji mieszającej klucz główny faktury i klucz obcy pozycji (ta sama wartość)
	* wskazana kolumna w obu tabelach jest kluczem klastra
	* wszystkie dane dotyczące jednej faktury znajdują się w jednym bloku
* Przy standardowej organizacji z indeksem drzewiastym
	* odczyt rowid faktury z indeksu
	* odczyt wiersza faktury
	* odczyt rowid pozycji faktury
	* odczyt wiersza pozycji faktury
* Też pojawiają się wszystkie problemy indeksu mieszającego
	* przepełnienie bloków
	* będzie działać dobrze jeśli powiązane wiersze zmieszczą się w jednym bloku
* Wiele powiązanych tabel jest umieszczonych w 1 segmencie
* Wymaga zaindeksowania klucza grona indeksem mieszającym prostym
* Dostęp do wszystkich powiązanych wierszy obiektu - 1 odczyt
* Konieczność wstępnej alokacji segmentu dla wszystkich przewidywanych obiektów
	* musi zmieścić wszystkie wiersze wszystkich tabel

### Indeks bitmapowy
* Dobry kiedy można ograniczyć liczbę przegladanych bloków przy przeglądzie sekwencyjnym
	* operacje typu slice & dice w hurtowniach danych
	* mocno selektywne zapytanie (np. ogranicza liczbę wierszy do 10%)
* Tyle kolumn indeksu ile różnych wartości w kolumnie tabeli
* Bitmapa
	* 1 jeśli wartość występuje w danym wierszu
	* 0 jeśli wartość nie występuje w danym wierszu
* Wiersze uporządkowane zgodnie z fizycznym porządkiem w tabeli
* Złożone wyrażenie logiczne 
	* proste operacje (and, or) na kolumnach bitmapy
	* powstaje bitmapa (wektor bitowy) dla wyrażenia
* Operowanie na pojedynczych indeksach rzadko będą miały sens
* Zawiera mapę bitową dla każdej wartości klucza określającą położenie zawierających ją wierszy
* Musi być tworzony na kolumnach **mało selektywnych** o stałej dziedzinie
	* najlepiej jak kolumny klucza nie są modyfikowane
* Pozwala efektywnie obliczać masowo wyrażenia logiczne na indeksowanych wartościach
	* inaczej trzeba by obliczać wyrażenie oddzielnie przy przeglądzie każdego wiersza po kolei
* Najefektywniejsze gdy jest wiele indeksów bitmapowych na tabeli
* Fizycznie - B-drzewo dla każdej wartości klucza z mapami bitowymi w liściach drzewa
* Bardziej użyteczny w zastosowaniach OLAP
	* rzadko kiedy będzie przydatny w OLTP
* Dobre do bardzo szybkiego wyliczania `COUNT`
	* użyteczne nawet na pojedynczej kolumnie

### Indeks bitmapowy złączeniowy
* Indeks na wartości z tabeli połączonej
	* praktycznie indeksowany jest klucz obcy
	* wartość klucza indeksu pochodzi z tabeli nadrzędnej
* Musi być tworzony na mało selektywnym kluczu obcym o stałej dziedzinie
	* np. odwołanie do stabilnej tabeli słownikowej
	* pozwala korzystać w zapytaniach z wartości opisowaych bez sięgania do tabeli słownikowej
* System nie musi wykonywać złączenia
* Dobra do zastosowań OLAP
	* indeks dla tabeli faktów ale na wartości która jest w tabeli wymiarów

### Tabela o organizacji indeksowej
* Wiersze tabeli IOT są przechowywane w liściach B+ drzewa indeksu na kluczu głównym
	* wymaga o 1 dostępu mniej, wiersz jest w samym drzewie
	* same wiersze są umieszczone w kolejności klucza
* Wiersze mogą zmieniać położenie
	* przy zmianie wartości klucza
	* w odróżnieniu od standardowo zorganizowanej tabeli
* Można zakładać na takiej tabeli dodatkowe indeksy

### Indeks funkcyjny
* Indeks utworzony na wyrażeniu, a nie kolumnie
	* np. `ilość * cena`, bez przechowywania tej wartości w kolumnie
* Pozwala efektywnie wykonywać zapytania zawierające we frazie `WHERE` wyrażenia obliczane dla każdego wiersza
	* bez dodawania kolumny

### Indeks dziedziny aplikacji
* Application Domain Index (ADI)
* Pozwala na indeksowanie niestandardowych typów danych specyficznych dla aplikacji
* Wymaga specjalnego, dedykowanego oprogramowania 
	* m.in. realizacje operatorów porządkujących

## Optymalizacja

### Etapy realizacji zapytania
* Analiza zapytania (parsing)
* Opracowanie planu wykonania
	* optymalizator zapytań
	* opracowuje model dostępu
	* oblicza koszt
* Wykonanie
	* dostęp do indeksów
	* dostęp do tabel
	* stworzenie zbioru odpowiedzi
* Przekazanie rezultatu do aplikacji
	* przesłanie przez sieć
* Każdy z etapów może być przyspieszony
	* można np. zrezygnować z opracowywania planu wykonania jeśli zajmuje dłużej niż samo wykonanie

### Analiza zapytania
* Kroki analizy
	* analiza składniowa - zgodność ze składnią SQL
	* analiza semantyczna - dostęp do słownika danych (czy istnieją takie tabele, kolumny, itd)
* Przyspieszenie (uniknięcie) analizy
	* wykorzystanie wcześniej przeanalizowanych zapytań
	* pod warunkiem, że zapytania są identyczne co do treści (w tym białe znaki itd.)
	* system przechowuje wykonane zapytania w pamięci i reużywa ich, jeśli nowe zapytanie pasuje do sygnatury (cache)
	* używać np. `PreparedStatement` w JDBC

### Opracowanie planu wykonania
* Zasadniczy krok optymalizacji - celem jest znalezienie najefektywniejszego planu dla następnego kroku
* Opiera się na wiedzy optymalizatora o
	* wyniku analizy zapytania
	* mechanizmach dostępu do danych
	* zebranych statystykach dotyczących danych
	* wybranym trybie pracy i podpowiedziach programisty aplikacji
		* minimalizowany czas zwrócenia pierwszego wiersza (aplikacje interaktywne)
		* pierwszych n wierszy
		* wszystkich wierszy (programy wsadowe)
* W praktyce dąży się do minimalizacji operacji IO na dysku
* Przyspieszenie / uniknięcie optymalizacji
	* podpowiedzi ograniczają liczbę analizowanych możliwości
	* zapamiętywanie planów wykonania pozwala uniknąć kroku optymalizacji
	* optymalizacja zapytania może zajmować rzędy wielkości dłużej niż optymalizacja

#### Zarządzanie planami wykonania
* Mechanizm polega na zapisywaniu opracowanych planów wykonania w bazie danych do ponownego wykorzystania
* Kolejne wykonanie tego samego zapytania może się odbyć bez kroku opracowania planu
* Kolejne wykonania zapytania są realizowane w taki sam sposób pomimo zmian w bazie danych
* Możliwe jest zapamiętanie kilku planów, zarządzanie nimi i wybieranie najodpowiedniejszego do danej sytuajci
	* w zależności od stanu bazy danych, parametrów, stanu systemu
* Dąży się do tego, żeby zapytanie wykonywało się stabilnie
	* plan który wiadomo, że jest wystarczająco dobry

#### Możliwość użycia indeksów
* Treść zapytania może uniemożliwiać użycie indeksów
* Aby użycie indeksu na kolumnie było możliwe, predykaty w `WHERE` muszą mieć postać
	* `kolumna = wyrażenie`
	* `wyrażenie indeksowane = wyrażenie` - jeśli jest indeks funkcyjny
* Predykat np. `kolumna - wyrażenie = wyrażenie` uniemożliwi użycie indeksu
* Wyrażenie indeksowane po jednej stronie znaku równości

#### Metody dostępu do danych
* Sekwencyjny
	* przegląd wszystkich bloków należących do segmentu tabeli
	* optymalny dla zapytania zwracającego wiele wierszy (zazwyczaj powyżej ok. 10%)
	* optymalny dla małych tabel (mieszczących się w całości w pamięci)
	* nie ma narzutu z dostępu do indeksu
* Wykorzystanie indeksu drzewiastego
	* dostęp indeksowy lub indeksowo-sekwencyjny
	* optymalny dla zapytań zwracających mało wierszy z dużych tabel
	* możliwe wykorzystanie jednego lub wielu indeksów na tabeli
* Wiele indeksów
	* oddzielny indeks na imie, oddzielny na nazwisko
		* imie jest mniej selektywne
		* system wybierze bardziej selektywny i przefiltruje wynik
		* system użyje obu indeksów i znajdzie część wspólną
	* indeks złożony (nazisko, imie)
		* bardziej selektywny
		* od razu daje odpowiedź na pytanie
	* indeksy powinny być jak najbardziej selektywne i jak najlepiej odpowiadać zapotrzebowaniu aplikacji
* Wykorzystanie indeksu mieszającego
	* dostęp indeksowy
	* optymalny dla zapytań zwracających 1 lub kilka wierszy o tej samej wartości klucza
* Tabele o organizacji indeksowej
	* optymalny dla dostępu indeksowo-sekwencyjnego
* Wykorzystanie indeksów bitmapowych
	* optymalny dla dostępu do niewielkiej liczby wierszy z bardzo dużych tabel w oparciu o złożone wyrażenia logiczne

#### Metody wykonywania złączeń
* Skorzystanie ze struktury grona - bezkosztowe
* Metoda pętli zagnieżdżonych (Nested Loop Join)
* Metoda mieszająca (Hash Join)
* Metoda sortowania i łączenia (Sort-Merge Join)

##### Metoda pętli zagnieżdżonych
* Działanie
	* wybrane wiersze z tabeli zewnętrznej, mniejszej (sterującej) są przeglądane (najlepiej przez przegląd indeksu)
	* dla każdego wybranego wiersza tabeli sterującej wykonywana jest pętla wewnętrzna na drugiej tabeli złączenia (najlepiej przez przegląd indeksu)
	* tabela sterująca przeglądana 1 raz
	* druga tabela przeglądana tyle razy ile wierszy jest wybranych z tabeli sterującej
* Wybór optymalizatora
	* jeżeli zapytanie zwraca mało wierszy
	* jeżeli w jednej z tabel (sterującej) jest wybranych mało wierszy
	* jeżeli wybrana jest strategia `FIRST ROW`
* Lepiej wykonać mniej większych zapytań niż więcej małych

##### Metoda mieszająca
* Działanie
	* mniejsza tabela służy do wygenerowania tabeli wartości funkcji (hash table)
	* druga tabela jest przeglądana sekwencyjnie lub indeksowo-sekwencyjnie
	* dla każdego wiersza sprawdzane jest czy wartość wyliczonej funkcji mieszającej znajduje się w tabeli wartości funkcji
	* każda tabela przeglądana 1 raz
* Wybór optymalizatora
	* jeżeli złączenie jest równozłączeniem
	* łączone są duże zbiory danych
	* łączeniu podlega duża część danych małej tabeli
	* tabele są małe

##### Metoda sortowania i łączenia
* Działanie
	* zbiór wierszy z każdej z tabel jest sortowany według klucza złączenia i wyniki są umieszczane w strukturze tymczasowej
	* posortowane listy są łączone (algorytm zig-zag)
	* każda z tabel jest przeglądana 1 raz
	* wymaga przestrzeni na strukturę tymczasową
* Wybór optymalizatora
	* jeżeli metoda Hash Join nie może być użyta lub byłaby mniej efektywna
	* złączenie nie jest równozłączeniem
	* zbiory są posortowane
		* tabela o organizacji indeksowej
		* posortowana tabela tymczasowa - pośredni wynik zapytania z `ORDER BY`

#### Wybór metody dostępu
* 1 wiersz
	* użycie indeksu unikatowego
	* na kluczu głównym lub unikatowym
* Niewiele wierszy, prosty warunek
	* użycie indeksu nieunikatowego
* Niewiele wierszy, złożony warunek
	* użycie najbardziej selektywnego indeksu i sprawdzenie pozostałych warunków w każdym wierszu wskazanym przez indeks
	* użycie kilku indeksów i połączenie wyników (jak w Sort-Merge)
* Wiele wierszy
	* przegląd sekwencyjny
	* użycie indeksu bitmapowego

#### Statystyki tabel indeksów i systemu
* Tabele
	* liczba wierszy
	* liczba bloków
	* średnia wielkość wiersza
* Kolumny
	* liczba różnych wartości
	* liczba wartości `NULL`
	* histogram dystrybucji wartości - pomaga dobrać sposób wykonania
* Indeksy
	* liczba bloków węzłów liści
	* liczba poziomów
* System
	* statystyki IO
	* statystyki CPU
* Obliczanie
	* mechanizm zbierania dokładnych statystyk na podstawie analizy wszystkich weirszy
* Estymacja
	* mechanizm szacowania statystyk danych na podstawie analizy próbki wierszy

#### Strategia optymalizacji
* `FIRST_ROWS(n)`
	* zorientowana na optymalizację czasu odpowiedzi
	* minimalizacja czasu odczytu pierwszych n wierszy
* `ALL_ROWS`
	* minimalny czas wykonania całego zapytania
	* zorientowana na ogólną wydajność systemu

#### Podpowiedzi dla optymalizatora
* Strategie optymalizacji
* Włączenie mechanizmów optymalizacji danej wersji bazy danych
* Metoda dostepu do danych
* Kolejność złączeń
* Metoda złączenia
* Wykonanie równoległe
* Transformacja zapytania

### Przekazanie rezultatu do aplikacji
* Wymaga zastosowania odpowiedniego protokołu komunikacji dającego dodatkowy narzut
* Możliwe jest przekazywanie odpowiedzi nie pojedynczymi rekordami, a większymi paczkami
	* zmniejsza narzut na komunikację
	* im większa paczka tym większy czas oczekiwania, ale mniejszy narzut
	* dla dużej liczby wierszy lepsze duże paczki

## Tworzenie indeksów
* Dotyczy indeksów na kolumnach będących kryteriami wyszukiwania
* Każdy indeks może potencjalnie przyspieszyć jakieś zapytanie
* Nie należy tworzyć indeksów na małych tabelach
	* małe to takie, które są efektywniejsze bez indeksów
* Każdy indeks **zawsze** dodaje narzut na operacje modyfikacji
	* tylko czasem wspomaga niektóre zapytania
* Przy wielu kolumnach kryteriów najefektywniej jest
	* utworzyć indeks prosty na każdej z kolumn
	* rozszerzyć indeksy proste do złożonych dla najczęściej używanych kombinacji kryteriów
* Uzyskujemy możliwość obsługi przez indeks wszystkich zapytań przy liczbie indeksów równej liczbie kolumn kryteriów

### Opłacalne indeksy
* Na kluczach głównych
* Na kluczach unikatowych
* Na kluczach obcych
* Na selektywnych kolumnach będących kryteriami wyszukiwania (proste i złożone)
* Na wszystkich kolumnach występujących w zapytaniu (Index-Only Query)
	* dla bardzo szerokiej tabeli ale zapytanie odczytuje tylko kilka kolumn
	* opłaca się stworzyć indeks na wszystkich kolumnych używanych w zapytaniu
	* `SELECT` i `WHERE`
	* cała potrzebna informacja będzie w indeksie
	* w ogóle nie trzeba sięgać do tabeli
* **Na dużych tabelach**

### Nieopłacalne indeksy
* **Na małych tabelach**
	* sam narzut
	* brak korzyści - cała mieści się w pamięci
* Na kolumnach nie będących ani kluczami, ani kryteriami wyszukiwania
* Na kolumnach nieselektywnych
* Nie dotyczy indeksów bitmapowych

### Tworzenie indeksów bitmapowych
* Opłacalne
	* na kolumnach mało selektywnych o stałych dziedzinach
	* jeżeli w tabeli jest wiele kolumn z indeksami bitmapowymi
	* jeżeli zapytania zawierają złożone wyrażenia logiczne na indeksowanych kolumnach
	* jeżeli zapytania zawierają funkcję `COUNT`
	* **na bardzo dużych tabelach**

### Heurystyka
* Wyobraźmy sobie że jest n kolumn które mogą służyć jako kryteria wyszukiwania
* Minimalna liczba indeksów to n - każde zapytanie można obsłużyć indeksowo
* Dodatkowo można przyspieszyć przez indeks na większej liczbie kolumn
* Np. (nazwisko) i (imie, nazwisko) - najszybsze
* Dla większej liczby kolumn trzeba się zastanowić jakie zapytania będą najczęściej wykonywane
* Znając najczęstsze kombinacje można dołożyć kolumny do wybranych indeksów
* Każde zapytanie na 100% będzie obsłużone przez indeks
* Najczęstsze zapytania będą obsłużone przez dedykowane zapytania złożone
