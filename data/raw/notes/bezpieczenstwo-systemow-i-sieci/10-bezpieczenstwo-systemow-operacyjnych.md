# Bezpieczeństwo systemów operacyjnych

## DOS
* System jedno-zadaniowy, jedno-użytkownikowy
* Brak zabezpieczeń
* Możliwość wykonania jednego programu, który ma pełen dostęp do wszystkich zasobów
	* można było pisać programy TSR - podczepiane pod przerwania

## Nowoczesne systemy operacyjne
* Wielozadaniowe, wielodostępne
* Od lat 90
	* Windows NT, Unix, Linux
* Wymaga mechanizmów ochrony
	* procesu od innych procesów
	* użytkowników i ich zasobów między sobą
	* struktury systemu operacyjnego przed użytkownikami
* Podstawowe mechanizmy ochrony
	* pierścienie ochrony procesora
	* pamięć wirtualna (MMU)

## Pierścienie ochrony
* Wprowadza się oddzielne domeny bezpieczeństwa o różnych prawach
* Tworzą hierarchię od najwyższego poziomu uprzywilejowania do najniższego
* *Groźne* instrukcje wymagają odpowiedniego poziomu uprzywilejowania
* Wykonanie akcji o wyższym poziomie wymaga kontaktu między domenami i zapewnia ochronę
* Najczęściej oparty na mechanizmach sprzętowych
* W x86 4 poziomy
* Jądro systemu operacyjnego działa na najbardziej uprzywilejowanym pierścieniu
* Wszystkie operacje wymagające komunikacji z IO są wykonywane za pośrednictwem systemu operacyjnego

## Pamięć wirtualna
* MMU dokonuje translacji adresów wirtualnych na fizyczne
* Przy niemożności dokonania translacji zgłasza wyjątek sprzętowy
	* zapewnia ochronę
	* umożliwia realizację pamięci wirtualnej na dysku
* Każdy proces użytkownika widzi ciągły obszar pamięci do własnej dyspozycji
* Proces nie może zmieniać danych innego procesu
	* poza specjlanymi mechanizmami systemu operacyjnego (pamięć dzielona)
* Możliwość oznaczenia strony jako niemożliwa do wykonania
	* zabezpiecza przed buffer overflow
* Manipulacje strukturami MMU wykonuje tylko jądro w uprzywilejowanym pierścieniu bezpieczeństwa
* Mapowanie adresów za pomocą tablicy stron

## Kontrola dostępu
* Użytkownik uwierzytelnia się w procesie logowania
* Każdy proces uruchomiony przez użytkownika będzie potomkiem procesu shella
	* dziedziczą prawa dostępu użytkownika
* Dla usługi (np. serwer HTTP) powinien być utworzony dedykowany użytkownik o minimalnych potrzebnych prawach dostępu
	* w razie naruszenia bezpieczeństwa nie ma pełnych uprawnień (np. roota)
* Kontrola dostępu do obiektu (pliku) związana jest z prawami, rodzajami operacji jakie może wykonać użytkownik
	* odczyt
	* zapis
	* wykonanie
* Możliwe realizacje
	* macierz dostępu
	* lista kontroli dostępu
	* lista możliwości
 
### Macierz dostępu
* W kolumnach zasoby
* W wierszach odpowiadający użytkownicy
* W komórkach prawa użytkownika do zasobu
* Teoretyczna metoda, nie stosowana w praktyce
	* słaba skalowalność

### Lista kontroli dostępu (Linux)
* Access Control List (ACL)
* Obiekt (plik) posiada listę określającą prawa dostępu dla określonych podmiotów
* W Linuxie są 3 podmioty
	* właściciel (user)
	* grupa (group)
	* pozostali (other)
* Możliwe prawa
	* odczyt (r, 4)
	* zapis (w, 2)
	* wykonanie (x, 1)
* Jest skomplikowane przy bardziej złożonych prawach dostępu
* Wyświetlenie praw przez `ls -l`
* Zmiana praw przez `chmod`

### Lista kontroli dostępu (Windows)
* 13 rodzajów praw
* 2 listy powiązane z obiektem
	* Directory ACL - prawa użytkowników lub grup
	* System ACL - akcje podlegające audytowi (logowane)
* Właściwości -> Zabezpieczenia -> Zaawansowane

### Rodzaje list kontroli dostępu
* Discretionary ACL
	* nieobowiązkowa, uznaniowa
	* użytkownik decyduje jakie prawa, komu daje
	* moża udostępnić informacje osobom niepowołanym
	* mechanizmy w Linux, Windows
* Mandatory ACL
	* prawa dostępu są ustalone przez dedykowany podmiot
	* użytkownik nie może ich zmienić
	* implementacja SELinux lub SMACK
	* Windows Update jest de facto administratorem każdego windowsa, bo tylko on ma dostęp do wszystkiego
	* Mandatory Integrity Control w Windowsie
* Role Based Access Control
	* większość użytkowników w większości instytucji można zaklasyfikować do kilkunastu grup
	* prawa przypisuje się do grup/ról
	* grupy/role przypisuje się użytkownikom

## Zaawansowane mechanizmy bezpieczeństwa

### Set uid bit
* Pozwala na uruchomineie programu z uprawnieniami właściciela pliku
	* np. program `passwd` do zmiany hasła wymaga modyfikacji plików systemowych
* Trzeba uważać na prawo `w` - można by podmienić program

### Sudo
* Aministratorem Linuxa jest użytkownik o uid 0 (root)
* Można stworzyć wielu użytkowników o tym samym uid
* Lepiej wykorzystać mechanizm `sudo`
	* uprawniony użytkownik może wykonać program z uprawnieniami administratora
* Lista użytkowników w pliku `/etc/sudoers`

### Chroot
* Zmiana korzenia drzewa systemu plików
* Po uruchomieniu systemu przełącza się system plików to innego katalogu *sandbox* z odpowiednią zawartością
* Współcześnie zastąpiony przez wirtualizację

### Ochrona plików systemu Windows
* Windows File Protection, później Windows Resource Protection
* Mechanizm nasługuje na zdarzenie związane ze zmianami plików w chronionych katalogach
* W momencie wykrycia zmiany, plik zostaje zastąpiony dobrą kopią z katalogu `%systemroot%\system32\dllcache`
* Uniemożliwia ubicie Windowsa przez usunięcie odpowiednich plików

## Zasada najmniejszych uprawnień
* Każdy podmiot posiada minimalny zestaw uprawnień pozwalający wykonać jego zadania
* Principle of least privilege
* Principle of minimal authority

## Zasada rozdzielenia obowiązków
* Ważne operacje wymagają współpracy co najmniej 2 osób
	* np. wykonanie przelewu na dużą kwotę w banku

## Rzeczywistość
* Wiele aplikacji pracuje z większymi uprawnieniami niż potrzebują
* Tradeoff między bezpieczeństwem a używalnością
* Security by design
	* nie można dokleić bezpieczeństwa na końcu
