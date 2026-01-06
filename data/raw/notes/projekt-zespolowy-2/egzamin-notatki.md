# PZSP2 – pytania na egzamin
## Co to jest przypadek użycia i w jaki sposób się go opisuje/dokumentuje? Jak przypadki użycia zostały opisane w dokumentacji Państwa projektu?

* Opis sposobu w jaki użytkownik (lub inny system) wchodzi w interakcję z systemem
* Dokumentowane przez scenariusze i diagramy UML przypadków użycia
	* wyróżnieni aktorzy
* W projekcie przygotowaliśmy scenariusze i diagramy dla przypadków biznesowych i systemowych

## Jakie mogą być związki pomiędzy przypadkami użycia? Czy któryś z tych związków wykorzystano w dokumentacji Państwa projektu?

* Uogólnienie, rozszerzenie, zawieranie
* W projekcie wykorzystaliśmy
	* zawieranie (podstawowe funkcje zawierają krok wprowadzenia danych)

## Co to są wymagania niefunkcjonalne/pozafunkcjonalne? Czy tego typu wymagania wystąpiły w Państwa projekcie?

* Ograniczenia jakim ma podlegać tworzenie i działanie systemu
	* niezawodność
	* wydajność
	* pielęgnowalność
	* przenośność
	* bezpieczeństwo (security/safety)
* W projekcie mieliśmy wymaganie wydajnościowe
	* maksymalny czas udzielenia odpowiedzi przez system

## Czym różni się aktor biznesowy od aktora systemowego w modelu przypadków użycia? Jacy aktorzy wystąpili w Państwa projekcie?

* Aktor biznesowy (osoba, podmiot) to klient, który ma jakiś cel do załatwienia przez system
* Aktor systemowy (użytkownik, system) ma bezpośredni dostęp do systemu (np. przez GUI, przez API)
* Może być jednocześnie biznesowy i systemowy (klient robi coś przez aplikację)
* Klient w banku (biznesowy) i pracownik banku z systemem na komputerze (systemowy)
* U nas jeden aktor biznesowy i systemowy
	* użytkownik - analityk / operator sieci telekomunikacyjnej

## Do czego wykorzystuje się diagram klas z języka UML? Jakie są jego podstawowe elementy? Czy i jak został wykorzystany w dokumentacji Państwa projektu?

* Do przedstawienia statycznej struktury problemu
	* model pojęciowy (analiza)
	* model projektowy (implementacja)
* Elementy
	* klasy
	* atrybuty
	* relacje (dziedziczenie, agregacja, kompozycja, opis krotności, obligatoryjności / wykluczania)
* Wykorzystaliśmy do
	* widoku logicznego w modelu 4+1 architektury
	* opisu architektury kodu w implementacji

## Do czego wykorzystuje się diagram stanów z języka UML? Jakie są jego podstawowe elementy? Czy i jak został wykorzystany w dokumentacji Państwa projektu?

* Do modelowania stanów i przejść między stanami
	* teoria automatów
* Elementy
	* stany
	* przejścia
	* zdarzenia
* Nie wykorzystaliśmy w naszym projekcie

## Jakie diagramy UML wykorzystuje się do modelowania architektury? Które z nich wykorzystane zostały w Państwa dokumentacji? Co one pokazywały?

* Wykorzystuje się diagramy
	* klas
	* komponentów
	* wdrożenia
	* pakietów
	* sekwencji
	* stanów
	* aktywności
	* przypadków użycia
* Użyliśmy modelu 4+1 z diagramami
	* przypadków użycia (scenariusze)
	* klas (widok logiczny)
	* aktywności (widok procesu)
	* komponentów (widok implementacji)
	* wdrożenia (widok fizyczny)
* Poza tym diagramy klas i pakietów w opisie implementacji

## Czym różnią się testy jednostkowe, integracyjne i systemowe? Które z nich i w jaki sposób były wykonywane w Państwa projekcie? Jakie biblioteki/narzędzia zostały wykorzystane?

* Testy jednostkowe
	* testowanie pojedynczego modułu w izolacji (np. jedna funkcja, jedna klasa, kilka klas)
* Testy integracyjne
	* test poprawności interakcji między modułami
* Testy systemowe
	* testy systemu jako całości pod kątem zgodności z wymaganiami i funkcjonalności
* W naszym projekcie
	* automatyczne testy jednostkowe - testowana logika biznesowa (pytest, jest)
	* automatyczne testy integracyjne - testy api optymalizatora, testy integracji z solverem (FastAPI TestClient, pytest)
	* manualne testy systemowe - lokalne uruchomienie aplikacji i klikanie w GUI (Docker)
	* narzędzia automatyczne spięte z potokiem CI (GitHub Actions)

## Jakie znasz miary funkcyjne wyrażania rozmiaru oprogramowania? Którą z nich byłoby najłatwiej zastosować w Państwa projekcie?

* Punkty funkcyjne
	* liczone na podstawie
	* liczby plików wew/zew
	* liczby wejść/wyjść
	* liczby zapytań
* Punkty obiektowe 
	* liczone na podstawie
	* liczby ekranów
	* liczby tworzonych raportów
	* liczby modułów w językach 3 generacji (normalnych)
* Punkty przypadków użycia
	* liczony na podstawie
	* złożoności środowiska
	* złożoności technicznej
	* złożoności aktorów
	* złożoności transakcji
* Wszystkie dałoby się zastosować bo dokumentacja zawiera dokładne opisy wszystkich wejść do tych funkcji i diagramy
	* najłatwiej punkty obiektowe - są jasne podziały, mało elementów, elementy dobrze opisane i trzeba tylko oszacować wagi

## Na czym polega prototypowanie oprogramowania? Jakie są korzyści z prototypowania? Jakie znasz rodzaje prototypów? Czy w Państwa projekcie tworzone były prototypy?

* Prototyp to prowizoryczna implementacja, która implementuje tylko część funkcjonalności systemu
* Korzyści
	* lepsze zrozumienie problemu
	* usprawnienie komunikacji
	* szybszy feedback od użytkownika
	* mniejszy koszt zmian
* Rodzaje
	* poziomy - szeroki i powierzchowny, nastawiony na poznanie potrzeb użytkownika
	* pionowy - fragment funkcjonalności, sprawdza architekturę, przelot przez wszystkie warstwy
	* porzucany
	* ewolucyjny
* Powstał prototyp optymalizatora
	* pionowy i porzucany
	* przelot przez warstwy Frontend-API-solver
	* przygotowany na prezentację a właściwy tworzony od nowa

## Jakie są główne wartości stojące za Manifestem Agile? Dlaczego te wartości są istotne w tworzeniu projektów informatycznych? Jak się mają te wartości do Państwa projektu?

* Wartości
	* skupienie na kliencie
	* samoorganizacja zespołów
	* zrównoważone tempo pracy
	* tworzenie minimalnego oprogramowania (kod i testy)
	* akceptowanie i reakcja na zmiany
	* iteracyjne tworzenie
	* testy są kluczowe
	* opisywanie wymagań jako scenariusze
* U nas
	* regularnie konsultacje z właścicielem (dr Kozdrowski)
	* nacisk na testy
	* ciągła integracja, działająca aplikacja na main branch
	* tylko wymagane funkcjonalności

## Praktyki Agile - proszę omówić co najmniej 3 praktyki organizacyjne i techniczne na przykładach metodyk Scrum i eXtreeme Programming. Które z nich wykorzystali Państwo w swoim projekcie?

* Daily build & CI
	* budowanie i integracja projektu tak często jak to możliwe
	* mamy testy automatyczne i potok w GitHub Actions
* Refactoring
	* zmiena kodu bez zmiany funkcjonalności
	* pokrycie logiki testami umożliwiało nam refaktoryzację
	* dawaliśmy sobie uwagi na code review
* Test Driven Development
	* stosowaliśmy przy skomplikowanej logice importera danych
	* testy jednostkowe

## Proszę omówić wybrane dwie klasyczne metodyki zwinne spośród listy: Scrum, XP, Kanban, DSDM. Dla wybranych metodyk: Jakie są role w zespole? Jakie praktyki są stosowane? Co wyróżnia daną metodykę? Co z tych elementów zostało użyte w Państwa projekcie?

SCRUM

* Role
	* developerzy
	* scrum master
	* product owner
* Spotkania
	* planowanie
	* daily
	* review
	* retro
* Praktyki
	* sprinty
	* 4 spotkania
	* zamrożenie wymagań na czas iteracji
	* tablica z zadaniami
	* definition of done
	* backlog
* Co wyróżnia
	* sprinty
	* jasny podział odpowiedzialności
	* regularne spotkania i adaptacja
* Nie nadaje się do tego typu projektu na studia, była tablica z zadaniami

Kanban

* Role nie są narzucone
* To bardziej narzędzie niż metodyka
	* można łączyć ze scrum
* Praktyki
	* minimalizacja aktualnie trwających prac (Work in progress)
	* tablica ze statusami zadań
	* ciągła praca, bez podziału na sprinty
* Co wyróżnia
	* tablica zadań
* Co stosowaliśmy
	* tablica
	* ciągłe dostarczanie


## Proszę omówić wybrane 2 skalowalne metodyki zwinne spośród listy: LeSS, SAFe, Nexus. Dla wybranej metodyki. W jaki sposób przebiega planowanie pracy w którą zaangażowanych jest wiele zespołów? Co wyróżnia daną metodykę? proszę podać propozycję użycia tych metodyk w projekcie podobnym do realizowanego przez Państwa, gdyby było zaangażowanych kilka zespołów.

LeSS

* Skalowalny Scrum, zgodny ze Scrum
* Planning 1 - PO i reprezentanci zespołów ustalają główne cele
* Planning 2 - planowanie sprintu w poszczególnych zespołach
* Daily Scrum w zespole
* Porządkowanie backlogu
* Review - wspólne dla zespołów
* Retro - wspólne lub zespołami
* Kordynacja - just talk, open space, scrum of scrums

Nexus

* Skalowalny Scrum
* Zbiór kilku zespołów Scrumowych
* Jeden PO i wspólny backlog dla zespołów
* Nexus Integration Team - PO, SM i zespół od integracji
	* członkowie NIT mogą być członkami zwykłych zespołów
* Wspólne review przez NIt (nie w zespołach)
* Daily i retro w zespołach i samych przedstawicieli

Dla kilku zespołów wybrałbym LeSS ze względu na większą prostotę organizacyjną, nie byłoby potrzeby dedykowanego zespołu do integracji
## Proszę przedstawić definicję projektu i wynikające z niej cechy projektu. Proszę wykorzystać Państwa projekt jako przykład.

* Tymczasowe przedsięwzięcie podejmowane aby dostarczyć unikatowy produkt, usługę lub rezultat
* Cechy
	* tymczasowe - ma początek i koniec
	* jest znany zakres prac lub kryterium zakończenia

## Proszę podać, jakie są typowe wady opisu zakresu projektu informatycznego i co jest ich przyczyną? Czy te wady wystąpiły w Państwa projekcie?

* Niekompletność
* Niejednoznaczność
* Niespójność
* Zmiana znanych wymagań
* Pojawienie się nowych wymagań
* U nas
	* na początku opis był niekompletny ale nie stanowiło to istotnej przeszkody w pracy
	* poza tym nie wystąpiły, zakres był mały i dobrze określiliśmy wymagania na początku

## Proszę wymienić podstawowe zmienne w zadaniu planowania projektu i omów zależności między nimi. Proszę się posłużyć Państwa projektem, aby zobrazować te zmienne.

* Zmienne
	* Czas
	* Koszt
	* Zakres
	* Zasoby
	* Jakość
* Kompromisy są nieunikalne
	* dobrze tanio i szybko
	* preferencje jakościowe - zakres, jakość > zasoby, czas, koszt
	* realne - czas, koszt > zakres, zasoby, jakość

## Co utrudnia planowanie projektów informatycznych? Proszę odnieść się do wiedzy przekazanej na wykładzie oraz do Państwa projektu.

* Nie wiadomo jak szacować potrzebny czas
* Nieprawidłowe określenie zakresu i wymagań
* Klient nie wie czego chce
* Różne strony różnie rozumieją wymagania i specyfikacje
* U nas
	* był problem ze zrozumieniem dziedziny i szczegółów zadania
	* wyjaśnione na drodze spotkań z właścicielem

## Proszę omów elementy składowe podejścia Design thinking? Dlaczego istotną rolę odgrywa tu prototypowanie? Które elementy Design thinking użyliście Państwo w projekcie?

* Empatyzacja
* Definiowanie problemu
* Generowanie pomysłów
* Budowanie prototypów
	* pozwala ocenić jakość rozwiązania
	* może zostać dłużej niż byśmy chcieli
* Testowanie
* U nas
	* empatyzacja - spotkania z właścicielem i mentorką
	* definicja - spisanie wymagań i przypadków użycia
	* prototypy (dobór bibliotek, integracja)
	* testowanie

## Jakie podejście do tworzenia systemu informatycznego jest właściwe w zależności od zakresu projektu? Proszę podać kilka przykładów. Jednym z nich niech będzie Państwa projekt.

* Design Thinking
	* ograniczona wiedza o zakresie
	* zmienny zakres
* Agile
	* częściowo sprecyzowana wiedza
	* znaczna zmienność
* Metodyki klasyczne (Prince2, PMBoK)
	* kompletna wiedza o zakresie
	* niska zmienność

## Proszę omówić harmonogramowanie, a w szczególności omówić pojęcie ścieżki krytycznej, późny i wczesny start / koniec. Proszę się odnieść do Państwa projektu.

* Ułożenie zadań o określonym czasie wykonania w skierowany graf acykliczny (DAG)
	* krawędzi reprezentują relację poprzedzania
	* modeluje to jak jedno zadanie zależy od innych
* Późny start
	* najpóźniejszy czas rozpoczęcia zadania bez opóźnienia całego projektu
* Wczesny start
	* najwcześniejszy moment kiedy można zacząć zadanie
* Ścieżka krytyczna
	* sekwencja zadań
	* jeśli którekolwiek się opóźni to cały projekt się opóźni

## Proszę podać własny przykład zastosowania metody OKR do wyrażenia celów projektu.

* Cel: Wdrożenie aplikacji mobilnej dla sklepu internetowego
	* KR: Wydanie w sklepie z aplikacjami w ciągu 6 miesięcy
	* KR: Średnia ocena użytkowników w sklepie powyżej 4.0 3 miesiące po wydaniu
	* KR: 5000 pobrań aplikacji w 3 miesiące po wydaniu

## Proszę podać, od jakich czynników zależy podjęcie decyzji i uruchomieniu projektu? Proszę się odnieść do Państwa projektu.

* Cele warte osiągnięcia, opłacalność
	* korzyści
	* koszty
* Zdolność organizacji do realizacji projektu
	* dostępność zasobów
* Zgodność z przepisami, polityką organizacji
* Ryzyko
* Nie ma odniesienia do naszego projektu, ponieważ jest realizowany w ramach obowiązkowego zaliczenia, a koordynatorzy przedmiotu zapewniają zasoby (elektronika), podają tematy itp
## Jak wygląda typowa budowa komitetu sterującego zalecana np. Standardem Prince2? Jak jest główna odpowiedzialność tego komitetu? Kto pełnił rolę komitetu sterującego w Państwa projekcie?

* Budowa komitetu
	* użytkownik końcowy
	* dostawca
	* kierownik projektu
* Odpowiada za nadzór strategiczny
	* decyzje o kierunku
	* zarządzanie ryzykiem i zasobami
	* zarządzanie interesariuszami
* Rolę komitetu w pewnym sensie pełnili koordynatorzy przedmiotu, mentorka i właściciel tematu
	* projekt ma bardzo mały zakres i trudno mówić o kierunku rozwoju
	* oni egzekwują od nas terminy i oceniają

## Omów planowanie projektu w metodyce Prince2. Etapy zarządcze, sposób ich sekwencjowania. Przygotowanie vs. Inicjowanie projektu. Proszę znaleźć przykłady, mogą być z projektów realizowanych przez Panią/Pana.

* Przygotowanie projektu
	* rozważanie i decyzja czy podjąć projekt
	* uzasadnienie biznesowe
	* powstaje dokumentacja
	* planowanie następnego etapu
	* powołanie kierownika i komitetu sterującego
* Inicjowanie projektu
	* zdefiniowanie organizacji projektu
	* zaplanowanie pracy, podział na etapy
	* określenie zarządzania ryzykiem, zmianami, jakością, komunikacją
	* więcej dokumentacji
* N etapów zarządczych
	* właściwa praca
	* do 1 miesiąca
	* sterowanie etapem
	* zarządzanie dostarczaniem produktów
	* zarządzanie końcem etapu
* Zamknięcie projektu
	* zatwierdzenie wymagań, jakości, ocena, podsumowanie
	* przez kierownika projektu

## Proszę wskazać zasadnicze składniki procesu zarządzania ryzykiem i omówić na czym polegają. Proszę odnieść się do Państwa projektu. Czy był realizowany proces zarządzania ryzykiem? Jak?

* Proces
	* identyfikacja
	* ocena - prawdopodobieństwo x wpływ
	* reakcja - zmniejszenie prawdopodobieństwa lub wpływu
	* monitorowanie - aktualizacja rejestru, ponowna ocena
* Prowadzi się rejestr ryzyk i rejestr zdarzeń
* U nas
	* rozważaliśmy ryzyka technologiczne (możliwość obsłużenia modelu przez solver open source)
	* przygotowaliśmy plan awaryjny (licencja na komercyjne oprogramowanie)
	* opisywaliśmy ryzyka w dokumentacji i omawialiśmy je na spotkaniach z właścicielem tematu

## Zarządzanie zmianą - jakie ma cele i jak się je realizuje? Proszę podać przykłady.

* Cele
	* minimalizowanie oporu
	* zwiększenie efektywności
	* wdrożenie nowych technologii i procesów
	* optymalizacja wydajności
* Realizacja
	* przygotowanie do zmiany - analiza i ocena
	* komunikacja
	* zaangażowanie pracowników - szkolenia, wsparcie
	* monitorowanie postępów - zbieranie feedbacku
* Przykład - wprowadzenie elektronicznego systemu rezerwacji biurek w open space
	* kierownicy analizują po co
	* informacje na spotkaniach, listach mailingowych
	* tutorial on-line dla pracowników jak korzystać
	* dashboard z metrykami z systemu do rezerwacji - kto, ile, kiedy itp.

## Trzy poziomy zarządzania jakością - omówić i uzasadnić potrzebę takiego ich uporządkowania. Proszę odnieść się do Państwa projektu. Jak zarządzano tam jakością? A jak można byłoby zarządzać jakością?

* Kultura organizacyjna
	* zbiór wartości, przekonań
	* współdzielony przez pracowników
	* postawa dbania o jakość
* Procesy / procedury
	* formalizacja założeń kultury
	* możliwość automatyzacji, monitoringu
* Normy techniczne
	* zewnętrzne standardy
* Uzasadnienie
	* kultura - wszyscy wiedzą i zależy im żeby dbać o jakość
	* procedury - pozwalają efektywnie wdrażać założenia tej kultury
	* normy - zewnętrzne ramy, muszą istnieć kultura i procesy żeby je wspierać
* U nas
	* rozumiemy zagadnienia jakości, bezpieczeństwa itp
	* mamy procedury - CI, code review, reguły ochrony main branch
	* normy - tutaj nie ma zastosowania