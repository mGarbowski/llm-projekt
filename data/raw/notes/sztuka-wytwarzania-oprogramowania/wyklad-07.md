# Cykl wytwarzania oprogramowania cd (2024-04-08)

## Testowanie oprogramowania
* Najważniejsza część z punktu widzenia klienta
	* nie zawsze klient zdaje sobie z tego sprawę
	* może lepiej nazwać to zapewnianiem jakości
* Weryfikuje zgodność programu z oczekiwaniami
* Nic innego nie daje informacji co program naprawdę robi
	* kod to życzenie programisty
	* istnieją metody weryfikacji formalnej, są piekielnie drogie
	* języki funkcyjne to zapewniają jeśli nie mają interakcji ze światem zewnętrznym
	* można np. wykazać poprawność albo określić złożoność samego algorytmu ale trudno dla całego systemu
	* modelowanie może pomagać ale zależy od procesu (czy model jest przetwarzany czy przepisywany) ale i jakości samego modelu

### Dwa użycia
* Oddzielny element cyklu, dedykowana czynność
	* raczej nazywany walidacją, kwalifikacją, certyfikacją
* Integralny element implementacji, codziennej pracy
	* nie można ocenić wykonanej pracy bez jej przetestowania
* Oba podejścia mają sens
* Testowanie może zweryfikować tylko czy nie ma znanych błędów
* Testy robi się na coś
	* jeśli test przechodzi to testowanie się nie powiodło - nie wykryto błędu
* Testowanie nie daje gwarancji poprawności działania
	* to nie znaczy że należy testować na produkcji

## Rodzaje testów
* Każde uruchomienie programu i obserwacja zachowania to też test
	* istnieją dedykowani specjaliści zajmujący się aspektami testowania
	* product assurance, quality assurance
* Testowanie nie musi dotyczyć wyłącznie kodu
	* np. zgodność instrukcji użytkownika z rzeczywistym oprogramowaniem

## Podział testów
### Czy program jest fizycznie uruchamiany
* dynamiczne
* statyczne
### Ze względu na obiekty objęte testem
* jednostkowe
	* najmniejszy moduł jaki jest sens testować
	* np. pojedyncza funkcja, klasa
* integracyjne
	* podział jest rozmyty
	* może być backend z rzeczywistą bazą
	* może być kilka klas
* systemowe
	* test całego systemu
* akceptacyjne
	* czy klient akceptuje produkt
	* właściwie to oddzielna kategoria
	* test akceptacyjny może dotyczyć jednostki
	* factory acceptance test i site acceptance test
	* dotyczą konkretnej wersji, konkretnego momentu w czasie

### Testy walidacyjne
Testy bezpośrenio weryfikujące wymagania


### Ze względu na podejście do obserwacji wyniku
* white box
	* wgląd do kodu źródłowego, szczegółów implementacyjnych
	* np kolejność wywołanych metod na mocku
* black box
	* bez znajomości szczegółów implementacyjnych
	* testy jednostkowe mogą być typu black box - sprawdzają działanie modułu
* gray box?
	* piszemy testy jednostkowe jak black box ale znamy implementację

### Ze względu na sposób przeprowadzenia
* automatyczne
* manualne
	* test może polegać na uruchomieniu programu w debuggerze i sprawdzeniu stanu rejestrów
	* nie wszystko można zautomatyzować

### Ze względu na badane aspekty
* testy funkcjonalne
	* sprawdzają wymagania funkcjonalne
	* większość testów jednostkowych to testy funkcjonalne
	* część testów integracyjnych to testy funkcjonalne
* testy wydajnościowe
	* raczej na poziomie systemowym albo integracyjnym
	* wyrobienie się w określonym czasie
	* obsłużenie liczby zapytań w określonym czasie
	* oszczędzanie baterii
	* określenie że mieścimy się w dostępnych zasobach przy normalnej pracy
* testy przeciążeniowe
	* granice wytrzymałości programu, warunki ekstremalne
	* jeśli wiemy że program się wysypie przy 5000 zapytań to przy 4000 możemy uruchomić drugą instancję
	* sam komunikat, że system jest przeciążony może być ok
* testy bezpieczeństwa (security)
	* czy ktoś niepowołany może uzyskać dostęp do danych itp
* testy bezpieczeństwa (safety)
	* np. sprawdzamy, że winda nie spada, kiedy system jest przeciążony
* testy niezawodności (dependability)
	* szersze niż safety
	* dostępność - prawdopodobieństwo, że system jest dostępny w chwili czasu
	* stabilność - prawdopodobieństwo że będzie działał w chwili Y jeśli działał w chwili X
* testy odporności (recovery)
	* odtworzenie systemu po tym jak padnie
	* można robić backup i nie testować jego odtwarzania (lepiej nie)
* testy zgodności (compatibility)
	* mogą być dołożone do testów akceptacyjnych
* testy dokumentacji

### Inne rodzaje testów
* testy dymne (smoke test)
	* kiedy nie można przetestować całego systemu
	* włączamy do prądu i patrzymy czy nie płonie
	* czy w ogóle jest sens odpalać wszystkie testy
* testy regresji (regression testing)
	* każdy test jest de facto testem regresji
	* test sprawdza czy nie zepsuliśmy czegoś co wcześniej działało
	* przy bardzo złożonych systemach można sprawdzić tylko część systemu, która została zmieniona
	* np. istnieje jedna instancja systemu i korzysta z pamięci flash
* testy destrukcyjne (destructive)
	* rozwalamy system i patrzymy na efekty
* testy interakcji z człowiekiem
	* testy tłumaczeń i regionalizacji
	* testy używalności (usability)
	* testy dostępności (accessibility)

## Dobry test
* cel jest jednoznacznie ustalony
* czytelny jak normalny kod
* określony warunek końca testu
* określony warunek oceny testu (zaakceptowania)
	* duży napis failed/passed
* jeśli możliwe to odwołanie do wymagań, z których test wynika
* idealnie
	* automatyczny
	* deterministyczny i powtarzalny
	* jednoznacznie i łatwo oceniany
	* szybki

## Testy jednostkowe
* najwyższa stopa zwrotu w jakości
* najlepszy przyjaciel programisty
	* wiadomo co jest zrobione na koniec dnia
* wymusza lepszą architekturę decoupling
	* żeby móc przetestować moduł to musi być niezależny od innych
* nie wszystko da się unit testować
* brak formalnej definicji jednostki
* nie zawsze odpowiada bezpośrednio wymaganiom
	* usunie drobne błędy ale nie poważne naruszenia funkcjonalności

## Automatyzacja cyklu
* wytwarzanie oprogramowania jest jakimś procesem
* lepiej gdybym nie musiał pamiętać o uruchomieniu testów po wypchnięciu na gita

### Automatyzacja procesu a jakość
* rozsądny poziom formalizacji zazwyczaj pomaga osiągnąć zakładane cele
* automatyzacja to forma formalizacji, mamy określony proces


## Continuous integration
* proces ciągłej integracji i weryfikacji zmian wprowadzonych do projektu
	* często stosowane razem z *feature branches*
* można zasymulować merge nowego brancha
* ma zapobiegać popsuciu głównej gałęzi kodu
* może przeprowadzać walidacje niedostępne programistom na co dzień
	* kompilacja kilkunastoma kompilatorami
	* wiele instancji
* nie rozwiązuje wszystkich problemów
* co może robić
	* kompilować kod
	* analizować kod statycznie
	* uruchamiać testy jednostkowe i zbierać pokrycie
	* uruchamiać testy walidacyjne / akceptacyjne
	* generować dokumentacje
	* przygotowywać pakiety instalacyjne
	* ...

## Continuous Delivery / Continuous Deployment
* Potok może dostarczyć produkt na serwery produkcyjne
* Stan repozytorium, który można przekazać klientowi

## Realizacja CI
* Najczęściej sprzęgnięte z systemem kontroli wersji
* Może wymagać dużo zasobów
* Stabilne / powtarzalne środowisko
	* wirtualizacja / konteneryzacja
* Proces dzieli się na samodzielne kroki
* Narzędza wbudowane w system kontroli wersji
	* Github Actions
	* Gitlab CI
* Narzędzia dedykowane
	* Jenkins
	* Travis CI

