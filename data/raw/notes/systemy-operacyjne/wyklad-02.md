Jeszcze nie wiadomo co z laboratoriami,
będzie co innego niż rok temu,
będą instrukcje do ustawienia środowiska

System musi
* śledzić zasoby systemu
* narzucać strategie przydziału zasobów
* przydzielać zasoby
* odzyskiwać zasoby

Tworzenie maszyny wirtualnej przekształca maszynę rzeczywistą w maszynę o cechach wymaganych przez przyjęty tryb przetwarzania (przeznaczenie systemu komputerowego)

# Historia systemów operacyjnych

## Tryby przetwarzania
* tryb wsadowy (batch, off-line)
    * automatyzacja powtarzalnych zadań
    * skryptowanie, bez interaktywności
    * współczesne CI/CD
    * celem jest brak interakcji z użytkownikiem
* tryb interaktywny (on-line, interactive)
    * szybka reakcja systemu
    * kontrola przebiegu wykonania zadania
    * mniejsze wykorzystanie zasobów
* tryb czasu rzeczywistego
    * użytkownikiem jest proces technologiczny, który narzuca wymagania czasowe
    * jest nieprzekraczalny limit czasu na wykonywanie zadań
    * system okresowo bada stan procesu technologicznego


## Generacje systemów operacyjnych
* Pierwsza generacja (1945-1955) - lampy i przekaźniki
    * Architektura von Neumana
        * system binarny, arytmometr
        * strumień wejścia wyjścia i sterowania
        * instrukcje warunkowe
        * program i dane w pamięci
* Druga generacja (1955-1965) - tranzystory i systemy wsadowe
    * systemy typu mainframe
    * zwiększenie utylizacji czasu procesora przez przetwarzanie wsadowe
* Trzecia generacja (1965-1980) - układy zintegrowane i wieloprogramowanie
    * wieloprogramowanie zapobiega marnowaniu czasu procesora (oczekiwania na I/O)
    * spooling - Simultaneous Peripheral Operation On Line - kolejkowanie (np. przy dostępie do drukarki)
    * dzielenie czasu (time sharing) umożliwia pracę wielu użytkowników jednocześnie
    * przetwarzanie wsadowe i interaktywne
    * nie ma maszyn peryferyjnych (takich jak IBM 1401)
    * pojęcie terminala - wiele klawiatur i monitorów do jednego komputera
    * Unix, System V, BSD, MULTICS
    * POSIX - standard zgodności z systemem Unix (interfejs na poziomie wywołań systemowych)
* Czwarta generacja (1980-...) - komputery osobiste
    * Systemu GUI
    * MS DOS, Windows, Macintosh, Minix, Linux
    * IBM opublikował specyfikację PC, zaczęły powstawać klony

