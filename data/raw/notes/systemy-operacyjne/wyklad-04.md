# Wykład 04 (2023-10-24)

usr - unix system resources - wewnętrzne zasoby systemu

przeczytać 2 rozdziały z książki o unixie
w starej książce są te ważne rzeczy które przetrwały do dzisiaj

Poza zwykłymi plikami w systemie plików są pliki specjalne
* katalogi
* procesy
* urządzenia blokowe i znakowe
* semafory
* potoki

Polecenia w shellu pisze się po to żeby je raz uruchomić a nie po to żeby je później rozumieć xd

identification
authentication - uwierzytelnienie
authorization

są 2 prompty, oddzielny dla pierwszej linii polecenia i oddzielny dla każdej kolejnej

katalog roboczy jest atrybutem procesu

polecenia wbudowane powłoki zmieniają środowisko (atrybuty procesu) samej powłoki, nie mogą być oddzielnymi programami

Pętla powłoki...

Plikiem konfiguracyjnym dla sh jest `~/.profile` i `/etc/profile` dla wszystkich użytkowników
Skrypty raczej pisze się dla `sh` bo jest dobrze ustandaryzowany, ubuntu łamie standard
Dobrze żeby pliki konfiguracyjny były ukryte (nazwa zaczyna się od .)
Wyrażenie regularne `*` nie łapie nazw plików zaczynających się od `.`
Dobrze byłoby nie usuwać plików `.` i `..`

`rm -rf *` nie usunie kropkowych plików

Kodem sukcesu jest 0
Root to użytkownik o uid 0

Można ustawić różnych użytkowników na to samo id ale różne loginy (np. wielu administratorów), oddzielne katalogi home
Wystarczą 2 linijki w /etc/passwd


Funkcje muszę zostać zdefiniowane przed użyciem, nie podaje się sygnatury funkcji
Każda zmienna jest łańcuchem znaków

Między dwoma średnikami jest instrukcja pusta

`shift` ucina z listy argumentów pierwszy argument - pozwala zawwsze obrabiać pierwszy argument
Skrypt do przeczytania i uruchomienia i zrozumienia

