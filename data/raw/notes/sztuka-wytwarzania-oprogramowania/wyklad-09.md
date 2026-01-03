# Analiza oprogramowania (2024-05-06)
* Testowanie (badanie + weryfikacja oczekiwań)
* Metryki (pomiar)
* Ogólnie to szersze pojęcie
* Podstawowy podział
	* statyczna (bez uruchomienia programu)
	* dynamiczna

## Analiza statyczna
* Najczęściej używana w rozumieniu statycznej analizy kodu w poszukiwaniu błędów
* Co potrafi statyczna analiza kodu
	* wykryć błędy czasu wykonania (przypadki, które mogą nie być pokryte przez testy)
	* wskazać potencjalne błędy (weryfikacja wejścia, undefined behaviour)
	* pilnować zgodności ze standardem kodowania (linter)
* Bywa szybka
	* w porównaniu z uruchamianiem wielu testów
	* potrafi przeanalizować cały projekt
	* uruchomienie dla całego projektu może być wolne
* Potrafi wskazywać nieczytelności
* Żadna analiza nie daje gwarancji że błędu nie ma
* Miewa wyniki fałszywie pozytywne
	* opiera się na heurystykach
	* celem jest wskazanie fragmentów którym warto się przyjrzeć
	* lepiej mieć więcej false positives niż false negatives
* Powinna być elementem pracy nad projektem
* Im szybciej odpalana tym lepiej
	* wygodnie mieć wbudowaną w IDE
	* warto żeby była częścią potoku CI
* Dobrze mieć kilka różnych narzędzi
	* mają różne cechy i możliwości
* Tani sposób na usuwanie potencjalnie brzydkich (niebezpiecznych) kawałków kodu
* Musi być odpalana non-stop i zero tolerancji dla błędów
* Lepiej świadomie oznaczyć linijkę jako ignorowaną przez linter niż mieć masę warningów do na które nikt nie patrzy
* Warningi kompilatora to też analiza statyczna
	* warto traktować wszystkie warningi jako błędy (ale analiza statyczna nie jest nieomylna)

## Analiza dynamiczna
* Analizować można wszystko co dzieje się z programem i jego otoczeniem podczas wykonania
	* zawartość dysku, komunikaty sieciowe
* Nazwa najczęściej używana w stosunku do analizy programu o nieznanym kodzie źródłowym
	* testowanie to też dynamiczna analiza
* Daje rzeczywiste wyniki
	* trudno dostać false positive
* Bywa czasochłonna
* Jest zależna od reprezentatywności scenariusza
* Aplikacja może być uruchamiana w środowisku "realnym" i zwirtualizowanym
	* testy systemowe powinny być przeprowadzane na takim docelowym środowisku
	* wirtualizacja nie musi dotyczyć używania maszyn wirtualnych / kontenerów
	* Valgrind podmienia bibliotekę standardową C
* Monitorowane aspekty
	* użycie pamięci (wycieki)
	* użycie cache procesora
	* użycie procesora
	* wykorzystanie sieci
	* wykorzystanie dysku
* Wykorzystanie zebranych danych do poprawy wydajności - profilowanie

### Problemy profilowania
* Trzeba badać aplikację taką jaką dostaje klient
	* skompilowana z optymalizacjami
	* przy optymalizacji związek między kodem asemblerowym a źróðłowym jest niejasne
* Profilowanie może samo zaburzać pomiar
	* instrumentacja / symulacja
	* próbkowanie
* Wszystkie pomiary czasu są obarczone błędem
	* poza systemami czasu rzeczywistego
* Kluczowy jest wybór scenariusza
* Współczesne problemy
	* procesor niekoniecznie jest wąskim gardłem
	* teoretyczne złożoności warto weryfikować w praktyce
	* przeszukiwanie liniowe tablicy mieszczącej się w cache będzie szybsze niż przeszukiwanie binarne
	* wąskim gardłem często są zewnętrzene zasoby (trudno to sprofilować)
	* współczesne architektur procesorów premiują optymalizację na poziomie ułożenia danych w pamięci bardziej niż redukcję instrukcji/skoków

## Analiza aplikacji bez aplikacji
* Klient musi przekazać odpowiednie informacje
* Dobrze jest mieć dostępny stack-trace
* Można przygotować program tak, by generował raport stanu (core dump, death report)

## Logowanie
* Logowanie polega na umieszczeniu w określonych miejscach kodu instrukcji dodających do rejestru (log) informację że dana linijka się wykonała
	* np. z datą, wiadomością, parametrami
* Dobry system rozróżnia 
	* poziomy logowania (fatal, critical, error, warning, info, debug, trace)
	* źródło logowania (moduł systemu)
	* Punkt docelowy (sink, plik, rejestr systemu operacyjnego)
* Potężnie narzędzie ale musi być odpowiednio używane
	* określona szczegółowość
	* treść musi być przemyślana
	* język musi być odpowiedni dla odbiorcy
	* użytkownik musi być w stanie przekazać logi

### Problemy logowania
* Można logować za dużo i log staje się nieczytelne
	* megabajty tekstu
* Można logować za mało i log nie będzie miał dość informacji
* Logowanie wpływa na wydajność
	* używa IO
	* może być warto wywołać logger (formatować komunikat itp) tylko jeśli jest ustawiony odpowiedni poziom
* Może naruszać bezpieczeństwo
* Trzeba mieć na uwadze kto będzie czytał logi
	* tylko programista
	* użytkownik który ma sam sobie naprawić