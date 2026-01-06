# Model relacyjny

## Mapowanie modelu ER na model relacyjny
* Encja - tabela
	* zwyczajowo nazwa w liczbie mnogiej
* Atrybut - kolumna
* UID - klucz główny
* Związek - klucz obcy
* Mapowanie podtypów
	* implementacja jawna
	* implementacja generyczna
	* implementacja hybrydowa
* Mapowanie łuków
	* implementacja jawna
	* implementacja generyczna
* Często można stworzyć model ER na wiele sposobów, a modele logiczne będą bardzo podobne

### Związek jednoznaczny
* Mapowanie związku jednoznacznego jest oczywiste
* Hierarchiczna relacja
* W tabeli podrzędnej będzie klucz obcy

### Związek jednojednoznaczny
* Mapowanie jest tak oczywiste
* Związek jest symetryczyny więc trzeba podjąć jakąś decyzję
* Zostaje hierarchia - encja podstawowa i zależna
	* encja zależna będzie miała unikalny klucz obcy
* Można umieścić klucz po stronie encji podstawowej
	* np. numer dokumentu w osobie
* Przekłada się odpowiedzialność za utrzymanie spójności danych przez aplikację
* Można umieścić klucze obce po obu stronach
	* jeśli to jest przydatne, zależy jakie są potrzeby aplikacji
	* faktycznie implementuje się oba końce związku
	* uwzględnia się opcjonalność po obu stronach
* Kluczem głównym w tabeli zależnej może być ten sam klucz co w tabeli podstawowej
	* id osoby jest kluczem tabeli dokumenty
	* id dokumentu jest unikalne
	* działa w obie strony jako klucz obcy
* W niektórych sytuacjach może opłacać się dodać klucz sztuczny
	* ten sam klulcz sztuczny może być kluczem głównym i obcym po obu stronach
* Można dwie encje połączyć w jedną tabelę
	* na jedno wychodzi, jeśli związek jest jednojednoznaczny
	* najczęściej optymalne rozwiązanie
	* wymaga analizy dziedziny biznesowej (np. czy dokument może istnieć niezależnie od osoby)
* Jeśli z obu stron jest opcjonalny to związek jest symetryczny i nie ma jasnej reguły co wybrać
	* decyzja projektowa
* To że w bazie relacyjnej informacja o powiązaniu istnieje tylko po stornie tej tabeli, w której jest klucz obcy może być problematyczne
	* żeby dostać się do podrzędnych obiektów trzeba wykonwać bardziej skomplikowane zapytanie

### Związek identyfikujący
* Klucz główny zawiera klucz obcy i jeszcze jakiś atrybut
	* np. numer faktury i numer pozycji na fakturze

### Wskazania do wprowadzenia klucza sztucznego
* Zbyt wiele segmentów klucza
	* 4 to już na pewno za dużo
	* 3 jest dyskusyjne
	* zajmują więcej miejsca w indeksie
	* w tabeli podrzędnej musi być tyle samo segmentów, żeby mieć klucz obcy
* Klucz znakowy o dużej wielkości
	* analogicznie jak do klucza o wielu segmentach
* Niepewność co do 100% określoności lub unikatowości klucza
	* czy cecha zawsze występuje
	* czy zawsze o niej wiemy
* Możliwosć zmienności wartości klucza
	* zmiana klucza głównego bardzo obciąża system
	* trzeba zmienić we wszystkich tabelach podrzędnych
* Klucz sztuczny to atrybut, który nie istniał w modelu ER
	* ma znaczenie tylko techniczne
	* jest oderwany od rzeczywistości
	* my go nadajemy, więc możemy mieć pewność że będzie unikalny, nigdy się nie zmieni itd.

### Encja łącząca
* Tabela zawierająca tylko klucze obce, które tworzą klucz główny
* Tabela o złożonym kluczu głównym i atrybutach
* Tabela z własnym, prostym kluczem głównym (np. sztucznym) i zwykłymi kluczami obcymi
* Hybrydowa
	* np. dla związku identyfikującego

### Zachowanie kluczy obcych
* Operacje `INSERT` i `UPDATE` do tabeli podrzędnej muszą być weryfikowane pod kątem poprawności klucza obcego
* Operacje `DELETE` i `UPDATE` do tabeli nadrzędnej muszą być weryfikowane pod kątem powiązanych rekordów
* Klauzula `ON UPDATE` zakłada aktualizację klucza głównego
	* może lepiej żeby w ogóle nie było możliwe
* Operacja jest zabroniona, domyślne (`RESTRICT`, `NO ACTION`)
* Kaskada (`CASCADE`)
	* system automatycznie usuwa wiersze podrzędne
* Ustawienie wartości klucza obcego na `NULL` (`SET NULL`)
* Ustawienie wartości domyślnej (`SET DEFAULT`)
	* można użyć dla związku obligatoryjnego
	* podpina wszystkie obiekty podrzędne do jednego wirtualnego obiektu

### Implementacja podtypów
* Najczęściej stosuje się implemetację generyczną
* Kiedy pojawia się problem z dostępem sekwencyjnym - implementacja hybrydowa
* W szczególnych przypadkach implementacja jawna
	* np. nie posługujemy się nadtypem

#### Implementacja jawna
* Oddzielne tabele dla każdego podtypu
* Każda tabela zawiera kolumny odpowiadające podtypowi
* Dla nadtypu nie ma tabeli
	* definiuje się perspektywę (widok)
	* widok zawiera wszystkie kolumny z obu podtypów (`UNION ALL`) z wartościami `NULL` w odpowiednich miejscach
	* operacje teoriomnogościowe w SQL są mało wydajne
* Optymalna obsługa podtypów
* Problem wydajnościowy przy dostępie indeksowym do wierszy nadtypu
	* są wykonywane 2 `SELECT`y, 1 na pewno niepotrzebne
	* może być problem wydajnościowy
* Dla dostępu sekwencyjnego do wierszy nadtypu nie ma różnicy
	* system ma tyle samo pracy do wykonania
* Problem z implementacją unikatowego identyfikatora nadtypu
	* nie ma jednego, wspólnego klucza głównego
	* można zrobić trigger
	* można generować sztuczny klucz (wspólna sekwencja dla obu tabel, UUID)
	* konieczność implementacji łuku po stronie tabeli nadrzędnej
* Mało wydajna zmiana przynależności obiektu do podtypu
	* wykonanie `DELETE` i `INSERT`
	* czy to problem - zależy o stabilności przypisania do podtypów
* Rzadziej używana w praktyce
	* może być lepsza w określonych warunkach

Operacja `UNION ALL` skleja dwa zbiory (nie usuwa duplikatów, jest wydajny), nie jest tożsama z sumą teoriomnogościową (`UNION`)

#### Implementacja generyczna
* Jedna tabela z atrybutami wszystkich podtypów
* Dla podtypów zdefiniowane widoki na tabeli generycznej
* Dodatkowa kolumna określa przynależność do podtypu - selektor
* Traci się zapewnienie obligatoryjności atrybutów podtypu na poziomie kolumn
	* można to zapewnić przez `CHECK` zależny od kolumny selektora
	* klauzule mogą zrobić się bardzo skomplikowane ze wzrostem liczby atrybutów i podtypów
* Optymalna obsługa nadtypu
* Problem wydajnościowy przy dostępie sekwencyjnym do wierszy podtypów
	* odrzuca się wiersze odpowiadające pozostałym podtypom
* Łatwa zmiana przynależności obiektu do podtypu
	* zmiana wartości selektora

#### Implementacja hybrydowa
* Tabela dla nadtypu i tabele dla każdego podtypu
	* jedyny przykład, gdzie z każdej encji powstaje tabela
* Klucz główny tabeli nadtypu jest jednocześnie kluczem głównym i kluczem obcym tabeli podtypu
* Widok dla nadtypu i widoki dla podtypów
	* dla nadtypu stosuje się outer join
* Bardziej skompikowana niż implementacja jawna i generyczna ale pozbawiona ich wad
	* optymalizator wybierze najlepszą opcję dostępu
* Generalnie mniej wydajne, bo w zapytaniach występują złączenia
	* można poprawić wydajność stosując klastrowanie tabel
* Nie ma problemu z implementacją unikatowego identyfikatora
* Nie ma problemu z implementacją zależności referencyjnych
* Najbardziej złożona zmiana przynależności do podtypu

### Implementacja łuków

#### Implementacja jawna
* Dwa klucze obce
* Deklaratywne definiowanie więzów integralności
	* `CHECK` zapewnia ich wzajemne wykluczenie
* Jedyne możliwe rozwiazanie, gdy klucze są różnych typów
* Nie nadaje się do związków identyfikujących
	* żaden segment klucza głównego nie może być `NULL`
	* trzeba wprowadzić sztuczny klucz główny

#### Implementacja generyczna
* W praktyce nie stosowana
* Jedna kolumna z pseudo kluczem obcym
* Kolumna selektora określa jakiej tabeli dotyczy pseudo klucz obcy
* Nie ma tak naprawdę klucza obcego (więzu integralności)
* Obsługa przez triggery
* Może być wygodne dla związków identyfikujących
* Niemożliwe do zastosowania, gdy klucze są różnych typów
* Więzy integralności muszą być definiowane proceduralnie (przez triggery)

## Normalizacja
* Usuwa z modelu danych anomalie związane z modyfikacją
	* wstawianie, aktualizacja, usuwanie
* Zły model może mieć redundancję danych, normalizacja usuwa tą redundancję
* Sam model uniemożliwia wykonanie pewnych niepoprawnych operacji
* Poprawne utworzenie modelu ER w praktyce zapewnia uzyskanie modelu relacyjnego w postaci BCNF
	* przygotowując model na zdrowy rozsądek wyjdzie postać normalna
* Model znormalizowany zawiera wiele tabel
	* zapytania mogą wymagać wykonywania wielu złączeń
	* to może prowadzić do mało wydajnych zapytań

## Denormalizacja
* Przeprowadzana w celu wyeliminowania problemów wydajnościowych
* Istotą jest takie przekształcenie, które umożliwi bardziej efektywny dostęp do bazy danych **bez utraty korzyści wynikających z normalizacji**
* Model musi być znormalizowany żeby wykonać denormalizację
	* to nie jest operacja odwrotna do normalizacji
* Najpierw potrzeba poprawnego modelu, do którego wprowadza się kontrolowaną redundancję
	* wprowadzenie redundancji może wprowadzić dodatkowy narzut związany np. z obsługą modyfikacji
* Opiera się na analizie stosunku zysków do strat
	* zysk z szybszego dostępu
	* straty wydajności operacji modyfikacji przez redundancję
* Najbardziej twórcza, najmniej automatyczna czynność przy projektowaniu bazy danych
* Zawsze dotyczy konkretnych zapytań, które wiemy że są zadawane do bazy i chcemy je optymalizować
* Już na etapie projektowania można sobie uświadomić jakie problemy trzeba będzie rozwiązać
	* już wtedy można stwierdzić że jakiś element wymaga denormalizacji
	* niektóre problemy wyjdą dopiero kiedy zobaczymy "zastoje" w działającym systemie

### Dekodowanie danych
* Np. numer PESEL - jest w nim zakodowana data urodzenia
* Zapisanie oddzielnej kolumny na datę urodzenia wprowadziłoby redundancję
* Na poszczególnych kolumnach można potworzyć indeksy
* `INSERT`, `UPDATE` i `DELETE` kosztuą tyle samo
	* indeksy spowalniają `INSERT` i `DELETE`
* Mówiąc o koszcie bierze się pod uwagę głównie wymianę danych między pamięcią operacyjną a dyskiem

### Pre-join (atrybuty)
* Umieszczenie w tabeli podrzędnej atrybutów z tabeli nadrzędnej (zduplikowanie)
* Unika się złączenia
* Tym większy zysk i bardziej złożone są struktury
* Jawna redundancja
* `INSERT`, `UPDATE`, `DELETE` kosztują tyle samo dla tabeli podrzędnej (tej która wprowadza redundancję)
	* aplikacja i tak musi mieć dostęp do tych danych np. przy wyświetlaniu w GUI
* Dla tabeli nadrzędnej
	* logika aplikacji może wykluczać pewne operacje
	* `INSERT` można robić tak samo niezależnie od innych tabel
	* `UPDATE` - działanie zależy od logiki aplikacji (zabronione, kaskadowanie, bez zmian)
	* np. czy dane klienta na fakturze mogą się zmieniać w czasie
* Przy denormalizacji można odkryć niuanse o modelu danych
	* przykład z danymi klienta na fakturze - co z modyfikacjami
* Często stosowana technika, daje dużo możliwości
* Dodatkowe kolumny i indeksy na tych kolumnach pozwalają na wyszukiwanie bez złączeń
* Kaskadowanie operacji można zrealizować triggerami
	* raczej chcemy obsługiwać denormalizację z poziomu aplikacji
	* triggery raczej w ostateczności (kiedy nie możemy modyfikować aplikacji)

### Pre-join (klucze obce)
* Kiedy jest długi łańcuch tabel
* Chcemy dane z tabeli na początku i na końcu łańcucha
* Jeśli w `SELECT` pojawia się mniej tabel niż we `FROM` to może być problem
* W tabeli dalej w łańcuchu wprowadza się redundantny klucz obcy
* Można wykonać jedno złączenie zamiast wielu
* Wywiedzione zależności
* Aplikacja zapewnia spójność - obie ścieżki prowadzą do tego samego rekordu

### Pre-join (słowniki)
* Można wprowadzić związki *na skróty*, których nie ma w modelu pojęciowym

### Kolumny wyliczane
* Np. mamy kolumny ilość i cena jednostkowa, a chcemy znać wartość (iloczyn)
* Wyszukiwanie po wartości wymaga przeglądania sekwencyjnego i wyliczania iloczynu za każdym razem
* Można dodać wartość jako oddzielną kolumnę
* Dodatkową kolumnę można zaindeksować
	* niektóre bazy (Oracle) wspierają indeksy funkcyjne - nie ma potrzeby wykonywać takiej denormalizacji
* Wartość wyliczana przez trigger

### Kolumny agregujące
* Zapisanie wartości funkcji agregującej jako oddzielną kolumnę
	* np. suma z tabeli podrzędnej
* Odczyt bez grupowania, przeglądu sekwencyjnego i sortowania
* Można założyć indeks na kolumnie
* Przyspiesza zapytanie o rzędy wielkości
* Utrzymywanie przez triggery
	* na `UPDATE`, `INSERT` i `DELETE` w tabeli podrzędnej
* Na poziomie aplikacji może być łatwiej
	* np. i tak musi trzymać wyliczoną wartość, żeby ją wyświetlić
	* zerowy koszt, duża korzyść
* Dobre dla obiektu o złożonej, hierarchicznej strukturze
* Problem przy wielopoziomowej zależności (suma sum)
	* może być nienaturalne z punktu widzenia aplikacji - wymagać dodatkowych zapytań
	* triggery mogą być lepsze
* Takie rozwiązanie może działać bardzo wolno jeśli agregacja dotyczy rekordów, do których dostaje się więcej niż jeden użytkownik na raz
	* normalnie patrzę np. tylko na swoje faktury
	* te same towary widzą wszyscy użytkownicy i blokują się nawzajem
	* zależy od tego jak dane są używane w aplikacji
	* trzeba dobrze rozumieć działanie aplikacji i zachowanie użytkowników

### Tabele agregujące
* Możemy potrzebować więcej szczegółów, bardziej granularny podział niż w pojedynczej kolumnie 
	* np. obroty klienta z podziałem na miesiące
* Dotyczy przede wszystkim zagadnień analitycznych, a nie operacyjnych
* Specjalne wartości w kolumnach mogą sygnalizować zagregowane wartości
	* np. miesiąc o numerze 0 - suma dla całego roku
* Obsługa
	* na poziomie aplikacji może być kłopotliwe 
	* aplikacja zajmuje się działalnościami operacyjnymi
	* nie powinna wykonywać niezwiązanych zadań
	* dobrze sprawdzi się obsługa przez triggery

### Agregujący widok zmaterializowany
* Jest obsługiwana automatycznie, trzeba ją tylko odpowiednio skonfigurować
	* nie trzeba pisać żadnego kodu, triggerów itp
	* triggery działają synchronicznie
	* daje więcej możliwości konfiguracyjnych niż tabela agregująca
	* może znacznie mniej obciążać system przy `INSERT` i `UPDATE`
* Jest pod każdym względem lepszy niż tabela agregująca

## Widoki zmaterializowane
* Stworzenie zwykłego widoku to dodanie *nazwanego zapytania*
	* nie powstaje żadna tabela
	* zapytanie do widoku jest zamieniane na zapytanie do odpowiednich tabel
	* upraszcza składnię zapytania ale nie zmienia tego jak fizycznie jest wykonywane
* Utworzenie widoku zmaterializowanego tworzy fizyczną tabelę
	* standardowo zostanie uzupełniona danymi zapytania przy utworzeniu
	* z punktu widzenia użytkownika zachowuje się jak perspektywa, służy do odczytu danych
	* zapytanie po prostu odczytuje dane z tabeli
* Dane są przenoszone w momencie tworzenie ale trzeba je odświeżać, bo inaczej stracą ważność

### Konfiguracja
* `BUILD IMMEDIATE` - wypełnienie danymi przy utworzeniu
* `REFRESH FORCE ON DEMAND`
	* odświeżanie na żądanie
	* operacje na tabelach operacyjnych nie są obciążone odświeżaniem tabel analiztycznych
* `REFRESH START WITH ... NEXT`
	* okresowe odświeżanie na podstawie czasu (o konkretnej godzinie itp)
* Jeśli tabela zawiera dane zagregowane po miesiącach to jest sens odświeżać ją na początku miesiąca
	* w środku miesiąca dane nie mają statystycznie sensu
	* kolosalna poprawa względem odświeżania przy każdym INSERT do tabeli operacyjnej

### Zastosowania
* Replikacja danych, przetwarzanie rozproszone
	* centralna baza replikowana do wielu baz lokalnych
	* tworzy się snapshot centralnej bazy i przesyła
* Hurtownie danych, agregacja
	* dane analityczne trzymane w zupełnie innej bazie niż dane operacyjne
	* dane do widoku zmaterializowanego są pobierane z innej bazy
* Optymalizacja zapytań
	* jest celem denormalizacji
	* wprowadzenie redundancji wymaga obsłużenia przez aplikację we właściwy sposób
	* część problemów wydajnościowych wyjdzie dopiero po wdrożeniu aplikacji
* Query Rewrite
	* rozwiązanie Oracle
	* silnik wykrywa zapytanie do oryginalnej tabeli, które pokrywa się z instniejącą perspektywą zmaterializowaną
	* silnik automatycznie zamienia zapytanie na zapytanie do perspektywy zmaterializowanej
	* wystarczy stworzyć strukturę w bazie i zostanie ona wykorzystana bez modyfikowania aplikacji
	* pozwala zoptymalizować działający system
* Systemy mobilne
	* jak replikacja tylko, że dane są przepisywane z serwera do klienta
	* użytkownik może pracować offline

### Rodzaje
* Jednokierunkowe - read only
	* może być dowolne zapytanie z grupowaniem itd.
* Dwukierunkowe - odczyt i zapis
	* tylko proste zapytania (w starszych wersjach)
	* bardziej złożone zapytania ze złączeniami (w nowszych systemach)
	* nie może być grupowania - zapis nie miałby sensu
	* triggery typu `INSTEAD OF`

### Tryby odświeżania
* `ON STATEMENT` - tak samo jak przy użyciu triggera
* `ON COMMIT` - na końcu transakcji
	* wiersze zablokowane na krótszy czas
* `ON DEMAND` - na żądanie
* `START WITH ... NEXT ...` - cykliczne
	* mało elastyczne bo zapisane na sztywno w bazie
	* lepiej użyć `ON DEMAND` i odpalać np. przez `cron`
* `NEVER` - niedopuszczalne
	* snapshot stanu bazy danych
	* np. archiwalny zapis stanu na koniec roku
* `ON QUERY` - odświeżanie w czasie rzeczywistym
	* jak `ON DEMAND` w momencie zapytania
	* nie odświeża całej tabeli
	* wylicza tylko dane potrzebne do zapytania
	* daje bieżące dane bez odświeżania
	* lokalny cache

### Opcje odświeżania
* `COMPLETE` - pełne
	* skasowanie danych z tabeli docelowej
	* wykonanie zapytania na tabeli źródłowej i zapisanie danych do tabeli docelowej
	* może trwać długo jeśli jest dużo danych w tabelach i zapytanie jest skomplikowane
	* dobre jeśli mały wolumen i dużo operacji
* `FAST` - szybkie
	* utrzymywany jest log operacji na tabeli źródłowej
	* zapytanie musi być proste, musi być jednoznaczna odpowiedniość między wierszami w obu tabelach
	* system powtarza operacje z logu na tabeli docelowej
	* podobne działanie jak przyrostowa obsługa przez triggery
	* czas odświeżania nie zależy od wolumenu danych tylko od liczby operacji
	* może być wolniejsze od pełnego odświeżenia jeśli operacji było dużo
	* dobre jeśli duży wolumen i mało operacji
* `FORCE` - wymuszone
	* jeśli można `FAST` to `FAST`, a jak nie to `COMPLETE`
	* zapytanie musi być odpowiednio proste
* Wybór odpowiedniej opcji na podstawie testów wydajnościowych
	* no chyba że z góry wiemy jak będzie

### Rollup
* `... GROUP BY ROLLUP ...`
* Powstają dodatkowe wiersze agregujące dla każdego poziomu grupowania
* Np. przy agregacji po miesiącach są też wiersze agregujące dla całego roku

## Model Zewnętrzny
* Zapewnienie właściwego widoku danych dla różnych aplikacji i użytkowników
	* aplikacje wykorzystują odrębne modele danych tylko przez widoki
	* dane są bardziej chronione i dostosowane do różnych potrzeb
* Jeden logiczny model dla instytucji, oddzielne widoki dla departamentów
* Stosowany w dużych organizacjach
* Ma sens tylko jeśli jest ich wiele dla jednego modelu logicznego
* Zastosowanie
	* dostosowanie widoku danych
	* przyspieszenie dostępu do danych
	* ograniczenie dostępu do danych
* Narzędzia
	* perspektywy
	* perspektywy zmaterializowane
	* prawa dostępu
	* triggery `INSTEAD OF`
* Logiczna niezależność danych
	* w bazie może równocześnie istnieć wiele modeli zewnętrznych dla tego samego modelu logicznego

## Podsumowanie
* Trzeba mieć na uwadze działanie aplikacji i zachowanie użytkowników
* Model relacyjny wyprowadzony z ER raczej będzie znormalizowany
* Denormalizacja może być konieczna dla zapewnienia dobrej wydajności
	* lepiej to przewidzieć i zdenormalizować na etapie projektowania
