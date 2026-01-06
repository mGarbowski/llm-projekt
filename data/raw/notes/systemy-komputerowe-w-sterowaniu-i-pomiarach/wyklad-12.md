# Obsługa IO (2024-05-27)
## Komunikacja ze sprzętem
* Każdy system potrzebuje IO żeby pełnić dowolną użyteczną funkcję
* Z komunikacją z peryferiami wiąże się wiele zagadnień związanych z pracą w czasie rzeczywistym
	* np. karta dźwiękowa
* Niektóre urządzenia mogą wymagać spełnienia ściśle określonych wymagań czasowych
	* zachowanie minimalnego odstępu między pewnymi działaniami
	* nie przekroczenie maksymalnego dopuszczalnego odstępu między pewnymi działaniami

## Urządzenie IO z punktu widzenia procesora
* Zbiór rejestrów
* Poszczególne bity lub grupy bitów w tych rejestrach mają określone znaczenie wpływające na pracę sprzętu
	* zapis / odczyt do rejestru może mieć konsekwencje
* Dostęp do rejestrów
	* dostępne za pośrednictwem magistrali
	* wybór urządzenia i rejestru przez podanie adresu
	* np. bardziej znaczące bity wybierają urządzenie, a mniej znaczące rejestr tetgo urządzenia
	* zapis / odczyt pod wybrany adres
* Każda magistrala w hierarchii ma własny system adresowania
* Urządzenia potrzebują do pracy sygnału zegarowego
* Urządzenie może generować asynchroniczne przerwania
	* wymaga połączenia do odpowiednich linii
	* może być 1 linia przerwań w prostych systemach
	* może być oddzielny kontroler przerwań albo hierarchia kontrolerów przerwań

## Magistrala systemowa
* W praktyce magistrala często pozwala na odróżnienie operacji na IO i pamięci

## I2C
* Kontroler I2C podłączony do magistrali systemowej (zarządzana przez procesor)
* Oddzielna magistrala I2C  do komunikacji kontrolera z urządzeniami IO
* Hierarchiczna struktura

## Połączenia między CPU a sprzętem
* Dawniej tworzono pliki opisu płyty
	* w strukturach C opisywano hierarchię
	* każda zmiana wymaga rekompilacji jądra
* Opisu płyty potrzebuje jądro systemu i bootloader
* Obecnie standardowe rozwiązanie - drzewo urządzeń
	* potrzeba wzięła się z procesorów ARM, które wymagają wyłączania i włączania wybranych komponentów dla oszczędzania mocy (np. w urządzeniach mobilnych)
	* struktura pliku podobna do JSON
	* dostęp do wartości po ścieżkach
	* można używać odwołań do węzłów po ich etykietach
	* określa z jakim sterownikiem urządzenie ma współpracować
	* deklaracja zgodności, a nie nazwa sterowanika, która może się zmieniać

## Dynamiczne drzewo urządzeń
* Nakładana na określony węzeł
* Jedna nakładka może obsługiwać wiele urządzeń
* Nakłada się przez odpowiednie komendy bootloadera
* Modyfikowanie drzewa urządzeń podczas pracy systemu jest niebezpieczne
	* ze względu na możliwość użycia odniesień w poprzek hierarchii
	* modyfikacja wymaga prześledzenia zależności
	* do raspberry pi jest komenda `dtoverlay`

## Dodatkowe komplikacje
* Jeśli system ma magistralę obsługującą autodetekcję lub hotplugging to obsługa się komplikuje
* Demon systemowy udev, eudev, mdev 
	* może automatycznie ładować i usuwać sterowniki
	* tworzyć i usuwać pliki specjalne urządzeń
	* pozwala konfigurować kontrolę dostępu do urządzeń

## Obsługa urządzenia
* Urządzenie jest już podłączone do systemu, do magistrali systemowej
* Specjalne instrukcje procesora jeśli architektura to wspiera `in`, `out`
* Kontrola uprawnień przez `ioperm`, `iopl`
* Rejestry mogą być zmapowane do pamięci
	* `/dev/mem` - dostęp do fizycznej przestrzeni adresowej CPU
* Sterownik `uio` pozwala tworzyć sterowniki w przestrzeni użytkownika dla urządzeń z rejestrami zmapowanymi do pamięci
	* specjalny plik mapuje się przez `mmap`
	* rejestry są dostępne w zmapowanym bloku pamięci
	* trzeba uważać na to co się zapisuje pod dany adres, bo sygnał może pójść prosto na magistralę
	* trzeba uważać na odpowiednie wyrównanie
	* może wymagać napisania kodu jądra do włączania i wyłączania przerwań
* Przy rejestrach zmapowanych do pamięci
	* można zdefiniować odpowiednią strukturę
	* musi być dobrze wyrównana
	* wtedy można pisać i czytać do rejestrów przez pola struktury
	* trzeba uwzględnić optymalizacje kompilatora kodu (użycie `volatile`)
	* trzeba uwzględnić optymalizacje odczytów pamięci samych procesorów (trzeba użyć odpowiednich funkcji libc)

## Pełne wykorzystanie możliwości urządzenia
* Sekcje krytyczne, pełna kontrola nad przerwaniami, ...
* Trzeba stworzyć własny sterownik