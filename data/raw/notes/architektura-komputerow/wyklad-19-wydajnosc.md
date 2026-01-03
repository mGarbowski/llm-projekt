# Wydajność

## Opóżnienia w procesorach superskalarnych i superpotokowych
15 stopni potoku, 4 instrukcje przetwarzane na raz - typowe parametry

Opóźnienie jest wzmacniane - więcej instrukcji może wykonywać się na raz - więcej instrukcji się nie wykonuje przy samym czekaniu

We współczesnych Intelach opóźnienie ze względu na skoki bez mechanizmów redukcji opóźnień zżerałoby ~80% wydajności

## Spekulatywne wykonanie instrukcji
* Procesor zgaduje jakie instrukcje ma wykonać
* jeśli zgadł dobrze to instrukcje się zatwierdza
* jeśli zgadł źle to trzeba anulować wykonane i wciągnięte do potoku instrukcje - wtedy jest spadek 80%

Spekulacja odbywa się wielopoziomowo - wiele skoków jest przewidywanych po sobie zanim pierwszy zostanie zweryfikowany, może trzeba będzie anulować wszystkie

## Skoki
* bezwarunkowe
* warunkowe
  * instrukcja może być wykonana bez skakania (niespełniony warunek)

* skoki statyczne - zawsze taki sam adres docelowy
  * względne - offset względem PC (liczba ze znakiem)
  * bezwzględne - nowa wartość ładowana do PC (adres docelowy)
* skoki dynamiczne - adres może się zmieniać (np. powrót z procedury)
  * funkcje callback - adres wołanej funkcji jako zmienna
  * metody wirtualne w C++

## Przewidywanie skoków
* Przewidzenie adresu skoku przed faktycznym wykonaniem
* Licznik poziomu spekulacji
  * każde zgadnięcie zwiększa
  * każde rozstrzygnięcie zmniejsza
* Jeśli rozstrzygnięcie skoku jest zgodne z przewidywaniem to licznik dla każdej instrukcji jest zmniejszany
* Jeśli rozstrzygnięcie jest sprzeczne z przewidywaniem to wszystkie instrukcje z niezerowym licznikiem są anulowane
* Instrukcja może zostać zatwierdzona kiedy poziom spekulacji wynosi 0
* Instrukcja wchodzi do potoku z bieżącym poziomem spekulacji

## Co to znaczy przewidzieć skok
* warunkowy - czy trzeba skakać
* każdy skok - pod jaki adres skakać
* przewidywanie wystąpienia instrukcji skoku w strumieniu instrukcji
  * procesor dowiaduje się że instrukcja jest skokiem dopiero w etapie dekodowania

## W któym momencie wiadomo jak wykonać skok
* skok statyczny bezwarunkowy - w momencie zdekodowania insturkcji
* skok statyczny warunkowy - po wyliczeniu warunku (późniejszy stopień potoku)
* skok dynamiczny - pobranie zmiennej z pamięci, najgorszy przypadek

## Przewidywanie statyczne i dynamiczne
* statyczne
  * przewidywanie nie wymaga gromadzenia informacji o wykonaniu programu
  * przewidywanie czy skok zostanie skoczony czy nie
* dynamiczne
  * gromadzenie informacji o tym jak wykonywał się program


## Przewidywanie statyczne
* przez kompilator lub programistę
  * zazwyczaj wiadomo że któraś ścieżka w kodzie jest bardziej prawdopodobna
  * można podpowiedzieć procesorowi że skok raczej będzie/nie będzie skakany
  * wprowadza się skok prawdopodobny i skok nieprawdopodobny (1b kodu operacyjnego) jako oddzielne instrukcje assemblerowe
* przewidywanie przez procesor
  * statystycznie 60% skoków warunkowych w tył jest realizowanych a w przód nierealizowanych
  * najbardziej znaczący bit przemieszczenia skoku względnego (ujemna waga) jest traktowany jako bit prawdopodobieństwa - wszystkie współczesne architektury


## Przewidywanie dynamiczne
* realizowane sprzętowo przez BTB - branch target buffer
  * działa jak kieszeń
  * gromadzi informacje o dotychczasowych skokach - pary - adres pod którym była instrukcja skoku i adres na który był skok
  * zapis do bufora przy rozstrzygnięciu wykonania skoku
* trafienie bufora - na podstawie adresu instrukcji zwraca adres docelowy jakiegoś poprzedniego skoku
  * skok wykonany przed zdekodowaniem
  * redukcja opóźnienia do 0
* mechanizm działa pod warunkiem że
  * nic się nie zmieniło w pamięci pod adresem
  * skok jest statyczny - nie załatwia powrotu z procedury i metod wirtualnych
  * jeśli skok był warunkowy to warunek jest tak samo spełniony/niespełniony jak był wcześniej
* skoki dynamiczne mogą być przewidywane jako statyczne
  * działa dobrze dla wskaźników na funkcje

## Przewidywanie adresów powrotów z procedur
* Wykorzystuje się sprzętowy stos powrotów
  * nie ma nic wspólnego ze stosem w pamięci
  * nie zależy od architektury (też dla RISC bez instrukcji push i pop)
* Działa pod warunkiem że każde wywołanie jest instrukcją `call` a powrót instrukcją `ret`
* Ślad jest niezależnie zapisywany też na stos powrotów
* Przy powrocie adres powrotny jest ściągany ze stosu sprzętowego a nie z pamięci
* Może być wykorzystany razem z buforem docelowym - bufor przewiduje wystąpienie powrotu a adres powrotu jest na stosie sprzętowym


## Predyktor elementarny
* Predyktor dwustanowy - przewiduje że następnym razem będzie to co było poprzednio
* Predyktor czterostanowy - zmiana decyzji po dwóch takich samych wykonaniach
  * strongly taken
  * weakly taken
  * weakly not taken
  * strongly not taken

## Predyktor dwupoziomowy
* prawdopodobieństwo warunkowe
* rejestr historii
  * wsuwa się po 1 bicie - czy skok był skoczony
  * może być oddzielny dla każdego skoku lub globalny dla wszystkich (gLocal, gShare)
* tablica predyktorów elementarnych jest indeksowana haszem adresu instrukcji skoku i historii


## Predyktor wielopoziomowy
* Wybiera predyktor który najlepiej będzie się uczył


## Fuzja instrukcji
* robienie jednej instrukcji z dwóch
* np. `cmp` i `jz`
* dwie instrukcje CISC traktowane jak pojedyncza instrukcja RISC