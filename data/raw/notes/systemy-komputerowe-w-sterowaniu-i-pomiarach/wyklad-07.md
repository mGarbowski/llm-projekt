# Komunikacja międzyprocesowa w Linuxie (2024-04-15)

* Zalety rozwiązanie z wieloma procesami
	* lepsza separacja realizowanych zadań
	* w razie awarii jednego procesu, łatwiej zapewnić poprawną pracę reszty systemu

## Różnice względem wielowątkowego programu
* Oddzielne przestrzenie adresowe
	* nie ma logicznego sensu przekazanie wskaźnika
* Nie ma możliwości bezpośredniej komunikacji (modyfikowania zmiennych)

## Dostępne formy komunikacji
* Sygnały
	* przerywa działanie procesu
	* brutalne, może być niespójny stan
* Potoki
* Gniazda
* Kolejki komunikatów
* Semafory
* Pamięć dzielona

## Uruchamianie procesów
* Proces główny uruchamia inne procesy jako potomne
	* może utworzyć jakieś obiekty, które odziedziczą procesy potomne
* Dodatkowe procesy są uruchamiane niezależnie
	* przez skrypt albo linię poleceń
	* można łatwo uruchomić system w różnych wersjach (produkcyjna, diagnostyczna, itp)
* `fork`
	* proces potomny dziedziczy otwarte pliki i kolejki komunikatów
	* zazwyczaj potem wywołuje się `execve` - załadowany inny program
	* strony działają  jako copy-on-write - oszczędza się pamięć na identyczną kopię
* `posix_spawn`
	* podobne jak `fork`
	* lepsza kontrola
* `clone`
	* może zachować się jak `pthread_create` - współdzielenie wszystkiego
	* może działać jak `fork`
	* dużo parametrów wywołania, precyzyjna kontrola
* `system`, `popen`
	* wywołanie innego programu jak przez shella
	* niezalecane
	* łatwe do zaatakowania

Są przykładowe programy

## Kolejki komunikatów
* Kanał umożliwiający komunikację jednokierunkową
* Na jeden koniec wkłada się dane
* Z drugiego końca wyjmuje się dane
* W potoku przesyła się nieustrukturyzowane bajty
* W kolejce są komunikaty
	* określona struktura
* Do komunikacji dwukierunkowej powinno się użyć 2 oddzielnych kolejek
* Dla jednego producenta i wielu konsumentów lepiej użyć oddzielnej kolejki dla każdego
* Może być jedna kolejka jeśli mamy pulę procesów typu worker i chcemy żeby którykolwiek obsłużył dane
* Oczekiwanie na dostępność komunikatu w kolejce
	* proces powinien się usypiać na czas oczekiwania
	* nie ma co marnować energii
* Kolejka przypomina plik
* `poll`
	* tworzy się tablicę deskryptorów plików i oczekuje aż coś się z nimi stanie
	* zwraca jeśli coś się zmieni, będzie timeout albo przyjdzie sygnał 
* `select`

## Odnalezienie kolejki
* Jeśli proces uruchamia się przez fork to rodzic bierze jeden koniec, a dziecko drugi
* Jeśli procesy uruchamiają się niezależnie to muszą mieć możliwość znalezienia kolejki
	* Do tego są kolejki nazwane
* `mq_open`
	* otwarcie lub utworzenie kolejki
	* można określić maksymalną liczbę komunikatów, maksymalny rozmiar komunikatu
	* flaga readonly, writeonly, readwrite - niezalecane
	* blokująca / nieblokująca
* `mq_close`
	* zamyka kolejkę
	* nie usuwa
* `mq_unlink` - usunięcie kolejki
* `mq_send` - wysyłanie komunikatu
* `mq_receive` - odbieranie komunikatu
	* zwraca rozmiar rzeczywiście otrzymanego komunikatu
* Komunikaty mogą mieć priorytety
* Bufor musi pomieścić komunikat o maksymalnym rozmiarze
* `mq_timedreceive`
	* odczyt blokujący z timeoutem
* `mq_notify` - powiadomienie o komunikacie używając sygnału
* Trzeba pamiętać o usunięciu

## Wady kolejek
* Dane są kopiowane 2 razy
* Pamięć dzielone na poziomie jądra systemu
* Problem można obejść
	* przesyłać w kolejce tylko pomocnicze struktury, deskryptory danych
	* właściwe dane przechowywać w pamięci dzielonej

## Pamięć współdzielona
* Nazwane
* Pliki w `/dev/shm`
* Równoczesny dostęp wymaga mechanizmów synchronizacji bo inaczej będą niespójności
* `shm_open`
	* utworzenie i otwarcie
	* tryby dostępu jak do plików
	* inne flagi
* `ftruncate` - nowy obszar ma domyślnie rozmiar 0, trzeba jawnie nadać mu rozmiar
* `mmap`, `munmap`
	* uzyskanie dostępu do pamięci dzielonej
	* nie trzeba mapować całego obszaru
	* uprawnienia jak do pliku
	* można pozwolić na wykonywanie kodu w załadowanym obszarze
	* czy ma być współdzielone, czy robić copy-on-write
	* `mmap` służy nie tylko do pamięci dzielonej, można zmapować plik do pamięci (dobre dla aplikacji bazodanowych, działa jak bufor)
* `shm_unlink` - usunięcie obszaru
* `close` - zamknięcie, ale nie usunięcie
* Usunięty obiekt dalej istnieje tak długo jak ktoś go trzyma (zostanie faktycznie usunięty dopiero po zamknięciu)

### Zagrożenia przy pamięci współdzielonej
* Procesor optymalizuje dostęp do pamięci
	* dostęp bez standardowych mechanizmów do synchronizacji może dać dziwne efekty
	* procesor może sam przestawić kolejność zapisów do kolejnych adresów
	* mechanizm barier w jądrze
* `gcc` może obsłużyć specjalne atomowe tryby dostępu do pamięci, które korzystają z barier (fence)
* można po prostu korzystać z semaforów, mutexów itp

## Synchronizacja dostępu do pamięci współdzielonej
* Te same obiekty co do wątków z `pthread`
	* odpowiednia flaga dla procesów
* Semafory
* Mutexy
* Zmienne warunkowe
* Blokady zapis/odczyt
* Wirujące blokady (spinlock, rygle pętlowe)
* Bariery

### Semafory
* `sem_init` - tworzenie
* `sem_destroy` - niszczenie
* `sem_wait` - zamknięcie, uzyskanie dostępu, blokuje proces
	* `sem_trywait` - nieblokująca próba uzyskania dostępu, zwraca informację czy się udało
	* `sem_timedwait` - blokujące dostęp ale z timeoutem
* `sem_post` - zwolnienie
* Nienazwane semafory - mogą być trzymane w pamięci dzielonej
* Można utworzyć nazwany semafor
	* dostępne dla zainteresowanych procesów przez nazwę
	* `sem_open`
	* `sem_close`
	* `sem_unlink` - pamiętać o usunięciu przez ostatniego użytkownika

### Mutexy
* Tylko jeden proces/wątek może mieć dostęp
* `pthread_mutex_init`
* `pthread_mutex_lock`
* `pthread_mutex_unlock`
* `pthread_mutex_setpshared` - do dzielenia między procesami
* `pthread_mutex_setrobust`
	* ustala co ma się dziać z mutexem jeśli zostanie osierocony
	* np. proces zamknie mutex i wyleci na błędzie bez otwierania mutexu
	* można dostać wiadomość, można przejąć, można zostawić zablokowany

### Zmienne warunkowe
* Oczekują na spełnienie określonego warunku
* `pthread_cond_init`
* `pthread_cond_wait`
	* oczekiwanie przy zamkniętym mutexie
	* mutex jest zwolniony kiedy proces czeka na zmienną
	* chroni przed jednoczesnym wejściem w oczekiwanie przez 2 procesy
	* zapobiega wyścigowi
* `pthread_cond_signal` - budzi 1 proces oczekujący
* `pthread_cond_broadcast` - budzi wszystkie procesy oczekujące

### Blokady zapis/odczyt
* Jeśli proces tylko czyta dane to i tak zajmuje semafor innym konsumentom
* Pojawia się konieczność rozróżnienia konsumenta od producenta
* Chcemy żeby
	* producent blokował dostęp wszytkim konsumentom i innym producentom
	* konsument blokował producentów ale nie innych konsumentów
* Jest ryzyko zagłodzenia producenta
* `pthread_rwlockattr_setkind_np`
	* pozwala określić preferencje
	* pozwala preferować konsumenta - przeciwdziałać zagłodzeniu (nie dopuszczać nowych konsumentów)
	* zależy od charakterystyki systemu co lepsze
* `pthread_rw_lock_init`
* `pthread_rw_lock_destroy`
* `pthread_rw_lock_wrlock`
* `pthread_rw_lock_rdlock`

### Bariery
* Określamy liczbę procesów jakie mają dotrzeć do fragmentu w kodzie zanim wszystkie zostaną odblokowane

### Rygle pętlowe
* Semafor usypia proces
	* wywłaszczenia, przełączenie kontekstu
	* kiedyś scheduler wznowi proces
* Jeśli wiemy że oczekiwanie będzie krótkie to można nie dać uśpić procesu dobrowolnie

## Jak realizować komunikację z wieloma konsumentami
* Dane trzymać w pamięci współdzielonej np w buforze cyklicznym
	* trzeba synchronizować dostęp
* Kolejką rozsyłać komunikaty o dostępności danych