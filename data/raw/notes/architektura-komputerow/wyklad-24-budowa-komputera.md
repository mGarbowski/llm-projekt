# Budowa komputera

## Architektura szynowa
* minikomputery (mini -> jedna szafa)
* Moduły wpakowane w szuflady
* Szuflady wsuwane do szafy łączą się z szyną
* Bardziej elastyczna konfiguracja, większa łatwość rozbudowywania
* Pamięć, sterowniki wejścia-wyjścia są widoczne dla procesora tak samo - jako komórki w przestrzeni adresowej
* Elegancki model logiczny
* Przy większych częstotliwościach zegara przestaje działać (rezonans itd)
* Szyna jest długa po to żeby przyłączyć dużo urządzeń wejścia-wyjścia
* Szybkość transmisji między procesorem a pamięcią jest bardziej krytyczna niż procesor-i/o


## Architektura dwuszynowa
* Szyna szybka
  * dla połączeń procesor-pamięć
  * krótsza
  * może działać przy wyższych częstotliwościach
* Most łączący obie szyny
* Szyna wolna
  * dla sterowników wejścia-wyjścia
  * niższa maksymalna częstotliwość pracy
* Wolna szyna wraz z rozwojem technologii stała się za wolna
  * dla środowisk graficznych
  * dla pamięci masowej
  * dla sterowników sieciowych


## Architektura trójszynowa
* Szyna pamięci
* Most północny - łączy szynę pamięci z szyną szybkich urządzeń zewnętrznych
* Szyna szybkich urządzeń zewnętrznych - sterowniki I/O (np. szybka pamięć masowa)
* Most południowy
* Szyna wolnych urządzeń zewnętrznych - sterowniki I/O (np. klawiatura, mysz itd)
* Szybka szyna zrobiła się za wolna dla animacji 3D


## Struktura komputera (rok 2004)
* Połączenia rozgałęzione (szyny) zastępuje się szybszymi nierozgałęzionymi (punk-punkt)
* Most północny
  * procesor i kieszenie (punkt-punkt)
  * pamięć operacyjna (punkt-punkt) i sterownik (potrzebny dla pamięci dynamicznej)
  * sterownik graficzny (punkt-punkt) z dedykowanym łączem
  * szyna szybkich urządzeń zewnętrznych (PCI)
* Most południowy
  * wszystkie potrzebne sterowniki do wolnych urządzeń zewnętrznych
  * już nie ma szyny

## Struktura komputera (rok 2006)
* Pamięć jest połączona bezpośrednio do procesora bez pośrednictwa mostu północnego
* Zastąpienie połączeń równoległych szeregowymi
  * żeby połączenie szeregowe działało sprawnie to połączenia muszą być ze sobą dobrze zsynchronizowane
  * robi się wiele niezależnych połączeń szeregowych
  * Połączenie PCI express (nie jest szyną!)
  * do sterowników graficznych połączenia x16
  * do sterowników IO połączenie x1
* Zwiększa się odległość między pamięcią a sterownikiem graficznym

## Współczesna struktura
* Nie ma żdanej szyny
* Same połączenia PCIe
* Sterownik graficzny podłączony bezpośrednio do procesora
* Organizacja logiczna transmisji danych jest podobna jak w sieci ethernet a w modelu programowym zachowuje się jak model szynowy



# Wydajność cd.

Zwiększenie długości potoku przekłada się na zwiększenie load-use penalty, potrzeba spekulatywnych sposobów dostępu do danych
Procesor zaciąga dane z pamięci zanim będą potrzebne (programowo lub sprzętowo)

Opóźnienie dostępu do L1 można maskować przez odpowiednie szeregowanie instrukcji (w superskalarach out-of-order)

Nie zawsze opłaca się buforować wszystko w najwyższej warstwie kieszeni
* np. obrazek nie mieści się w L1 a macierz filtra się mieści
* najlepiej trzymać dużą strukturę w L2 a małą w L1
* potrzeba możliwości sterowania buforowaniem z poziomu aplikacji

## Instrukcje sterowania kieszeniami
* instrukcje podpowiedzi (`nop` z punktu widzenia programu bo nie modyfikują ani rejestrów ani pamięci)
  * pobranie danej do bufora danych w procesorze
  * pobranie danych do L1 i ew. następnych
  * przemieszczenie linii w dół hierarchii
  * zapis linii kieszeni bez usuwania jej
* Efektywne użycie wymaga bardzo specjalistycznej wiedzy
* Nieefektywne użycia może znacznie pogorszyć wydajność
* Instrukcje są opisane w manualach intela itp


## Automatyczne pobieranie danych przez procesor
* Kolejka żądań odczytu z pamięci (load queue)
* Żądanie nie jest usuwane po wykonaniu tylko zapamiętywane
* Specjalny układ przegląda kolejkę i szuka zależności między adresami (np. zauważenie że procesor pobiera dane z co 20 komórki)


## Składanie zapisów (write combining)
* wielu danych nie można buforować (np. dane wymieniane ze sterownikami IO)
* zamiast buforowania w kieszeni stosuje się składający bufor zapisów
  * pojemność rzędu 1 linii kieszeni
  * pozwala na zapis wielu kolejnych bajtów w jednej transakcji pamięciowej
  * przy przekroczeniu granicy linii następuje pojedynczy zapis


## Instrukcje przesłań ze sterowaniem buforowaniem
* nie warto np. zaciągać struktury do kieszeni przy inicjowaniu jej
* instrukcja `MOVNTxx`


## Bufor pętli
* Kolejka instrukcji z układem wykrywania pętli
* Bufor mikrooperacji dla procesorów z transkodowaniem
* Wykrycie pętli mieszczącej się w kolejce powoduje wykonywanie instrukcji z bufora zamiast z pamięci


## Fuzja instrukcji
* Niektóre instrukcje bardzo często występują po sobie (`cmp`, `jcc`)
* Para instrukcji CISC jest wykonywana jako jedna instrukcja RISC po transkodowaniu


## Procesory wielowątkowe
* Duża liczba zależności międzyinstrukcyjnych powoduje częstą konieczność zatrzymywania potoku
* Zamiast czekać to wykonuje instrukcje z innego strumienia instrukcji (innego programu) - na pewno będą niezależne
* Potrzeba kolejnego licznika instrukcji i kolejnego zestawu rejestrów (dwa konteksty jednocześnie)
* Sprzętowa wielowątkowość (w każdym wysokowydajnym współczesnym procesorze)
* Co innego niż wielordzeniowość (wiele procesorów w jednym kawałku krzemu)