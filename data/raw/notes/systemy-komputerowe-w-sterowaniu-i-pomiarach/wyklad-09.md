# Szeregowanie zadań (2024-05-06)
* Zdarzenie
	* każda sytuacja wymagająca interwencji systemu sterującego
* Zadanie
	* moduł programu wykonywany niezaleznie od innych modułów
	* czas odpowiedzi nie dłuższy niż ustalony
* Odpowiedź
	* zmiana stanu
	* sygnał sterujący lub komunikat dla obsługi

## Strategie szeregowania
* Szeregowanie stałe (pre-run)
	* znany, powtarzalny rozkład zadań
	* długie okresy powtarzania w stosunku do czasu wykonania zadań
	* cykliczny program sekwencyjny
* Szeregowanie na bieżąco (run-time)
	* brak powtarzalnego schematu wykonania zadań
	* czasy wykonania przekreaczają okresy powtarzania
	* system operacyjny wielozadaniowy z wywłaszczaniem

## Opis zadania
* Czas zgłoszenia (release time)
* Czas wykonania (execution time)
	* pomijając inne zadania w systemie
	* nie jest przerywane, nie musi czekać
* Czas odpowiedzi (response time)
	* różnica między czasem zgłoszenia, a odpowiedzią
	* raczej dłuższy niż czas wykonania
* Dozwolony termin zakończenia (deadline)
	* względny, czas od zgłoszenia
	* bezwzględy, do danej godziny
	* może być określony probabilistycznie, przez rozkład, średnią itd.
	* de facto ograniczenie czasu rzeczywistego
* Okres powtarzania (cycle)
	* dla zadań cyklicznych
	* w systemie mogą też występować zadania sporadzyczne, bez ustalonego okresu

## Zadania cykliczne
Obciążenie procesora - czas wykonania / okres powtarzania
Jeśli suma większa niż 1 to nie da się spełnić ograniczeń
Trzeba dobrać odpowiednie priorytety zadań, żeby dało się spełnić ograniczenia
Nie zawsze da się dobrać takie priorytety, nawet jeśli obciążenie procesora jest poniżej 100%
Dobrze jeśli cykle powtarzania są swoimi wielokrotnościami (harmoniczne), wtedy szeregowanie można powtarzać w jednakowych cyklach

## Algorytm RMS
* Rate Monotonic Scheduling
* Priorytety zadań proporcjonalne do częstotliwości
* Optymalny algorytm stało-priorytetowy
* Warunek dostateczny $\sum_{i=1}^n t_i/c_i \le n(2^{1/n}-1)$
	* $t_i$ - czas wykonania
	* $c_i$ - cykl
	* $n$ - liczba zadań
	* spełnienie gwarantuje, że zadania da się uszeregować
	* jeśli nie jest spełniony to może się da a może nie
	* w granicy $n \rightarrow \infty$ próg ok $70\%$ obciążenia

## Algorytm EDF
* Earliest Deadline First
* Priorytety zadań związane z terminem zakończenia
* Optymalny algorytm zmienno-priorytetowy
* Warunek dostateczny $\sum_{i=1}^n t_i/c_i \le 1$
* Nie stosuje się go w praktyce
	* jest mniej przewidywalny jeśli obciążenie przekracza 100%
	* nie pozwala określić które zadania są ważniejsze (a RMS pozwala)
	* RMS, kiedy nie może spełnić ograniczeń wybiera zadanie o najwyższym priorytecie

## Szeregowanie i synchronizacja
* Procesy blokuja sobie nawzajem wspólne zasoby
* Inwersja priorytetów - zadanie o wyższym priorytecie jest blokowane przez zadanie o niższym priorytecie
* Warunke dostateczny $\sum_{i=1}^n + \max_{i=1..n} b_i/c_i \le n(2^{1/n} - 1)$
	* $b_i$ - najdłuższy czas oczekiwania i-tego zadania na zadanie o niższym priorytecie
	* trudne do obliczenia, szacowane

## Zadania sporadyczne
* Nieznany z góry czas zgłoszenia
* Możliwe zgłoszenia *stadne*
	* zgłaszane wiele na raz

### Warianty obsługi
* Wykonanie w tle
	* priorytet niższy od zadań cyklicznych
	* nie narusza terminu zadań cyklicznych
	* długi czas odpowiedzi dla zadań sporadycznych
* Wykonanie na najwyższym priorytecie
	* w obsłudze przerwań
	* krótki czas odpowiedzi zadań sporadycznych
	* możliwe opóźnienie zadań cyklicznych

## Serwer sporadyczny
* Zadanie obsługujące zgłoszenia sporadyczne
* Alterantywny wariant obsługi zadań sporadycznych
* Algorytm serwera sporadycznego
	* serwer otrzymuje budżet czasu $s$ oraz okres odnowienia $c$
	* przez czas $s$ pracuje na wysokim priorytecie $p$
	* później priorytet spada do niskiego $l$
	* odzyskuje wysoki priorytet po okresie odnowienia $c$
* W środowisku RMS
	* przy pełnym obciążeniu serwer wykonuje się z priorytetem $p$ przez czas $s$ co okres $c$
	* jeżeli priorytet $p$ jest zgodny z regułą RMS, to warunek dający gwarancję uszeregowania wszystkich zadań ...

### Serwer sporadyczny POSIX
* Parametry
	* budżet czasu
	* okres odnawiania
	* priorytet wysoki
	* priorytet niski
	* maksymalna liczba odnowień
* Algorytm
	* budżet czasu zmniejsza się na bieżąco podczas wykonania zadania
	* Odnowienie jest planowane, gdy zadanie zaczyna być wykonywane z wysokim priorytetem po raz pierwszy od opuszczenia stanu gotowości i obejmuje całą część budżetu zużytą od aktywacji zadania
	* Zadanie nie może korzystać z wysokiego priorytetu po zaplanowaniu maksymalnej liczby odnowień
	* Maksymalna liczba odnowień wraca do wartości wyjściowej ...