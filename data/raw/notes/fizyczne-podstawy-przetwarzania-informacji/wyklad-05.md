# Elektronika ciała stałego c.d. (2025-04-11)

* Tranzystor MOS
	* kanał ma swoją długość, rzędu 1-2nm
	* miniaturyzacja we wszystkich wymiarach
	* mierzymy charakterystyki prądowo-napięciowe
	* napięcie progowe - najważniejszy parametr
	* żeby je skutecznie zamodelować trzeba wziąć pod uwagę kwantyzację energii
* Mówimy o nanoelektronice jako odrębnej poddziedzinie nie tylko ze względu na skalę miniaturyzacji, ale też ze względu na to że rządzi się mechaniką kwantową
* Półprzewodniki do elektroniki wysokotemperaturowej
	* granica między półprzewodnikiem a izolatorem jest umowna
	* w wysokiej temperaturze będzie wyższa wartość przerwy energetycznej niż 2eV
* Struktura pasmowa jest konsekwencją periodyczności (w krysztale)

## Dynamika elektronu w krysztale
* k - wektor falowy
	* w fizyce klasycznej mówimy o pędzie
* E(k) - parabola
	* energia jest proporcjonalna to kwadratu pędu
* W rzeczywistym krysztale to nie jest takie proste
	* sieć krystaliczna drga (w temperaturze powyżej 0K)
	* gradient potencjału - pole elektryczne
* W rzeczywistym krysztale pojawiają się lokalne minima - tam E(k) jest lokalnie parabolą
	* półprzewodniki z prostą przerwą zabronioną (GaAs) - minimum pasma przewodnictwa i maksimum pasma walencyjnego dla tego samego k
	* półprzewodniki ze skośną przerwą zabronioną (krzem) - minimum pasma przewodzenia jest w innym k niż maksimum pasma walencyjnego
	* różnica jest istotna przy zastosowaniach optycznych
	* pęd i energia muszą zostać zachowane
	* przy skośnej przerwie przy emisji fotonu jest też emitowany fonon
	* raczej nie robi się diod świecących z krzemu z tego powodu
	* kolor światła w diodzie świecącej wynika z szerokości przerwy zabronionej
	* do diod świecących - prosta przerwa zabroniona

## Efekt fotoelektryczny wewnętrzny
* Próg absorpcji
* Materiały mają różną charakterystykę absorpcji
* Od tego zależy czy ciało będzie przezroczyste czy nie
* Szkło krzemowe
	* ciało amorficzne
	* SiO2
	* przepuszcza całe promieniowanie widzialne
	* ultrafiolet jest pochłaniany - powoduje emisję elektronów
* Szkło kwarcowe
	* ma większą szerokość przerwy zabronionej
	* uporządkowana struktura SiO2
	* mniejsza granica absorpcji (długość fali)
	* przepuszcza ultrafiolet

## Pamięć nieulotna (EPROM)
* utrzymuje stan po wyłączeniu zasilania
* jest studnia potencjału
* w studni są elektrony (ładunek) lub nie ma
* jak wyłączymy zasilanie to elektrony dalej tam są
* jak zresetować (stare pamięci)
	* przykładamy duże napięcie i naświetlamy powierzchnię półprzewodnika ultrafioletem
	* elektrony dostają energię i mogą wyjść poza barierę
	* okienko ze szkła kwarcowego - żeby przepuścić ultrafiolet
	* niewygodne, podwyższa koszt, naświetlanie może długo trwać
* Jak resetować (współcześnie)
	* w pełni elektrycznie
	* jak zwiększymy napięcie to rośnie gradient potencjału
	* elektron może przemieścić się do wolnego stanu energetycznego (tunelowanie)
	* procesem kasowania jest tunelowanie przez trójkątną barierę potencjału

## Masa efektywna
* Krótszy kanał w tranzystorze - powinien działać szybciej bo jest mniejszy dystans do przebycia
* Miniaturyzacja zwiększa szybkość działania
* Łatwiej przyspieszyć lżejszy elektron (masa efektywna)
* W ciele stałym masa efektywna jest inna niż dla swobodnego elektronu
* Masa efektywna - jak ostra jest parabola E(k)
* W arsenku galu
	* 0.067 masy elektronu swobodnego
* W krzemie
	* 0.97 albo 0.19 masy elektronu swobodnego ???
* W arsenku galu elektrony będą szybsze
	* decyduje ekonomia
	* krzem bierze się z piasku, jest łatwo dostępny
	* produkcja z GaAs jest ok. 5 razy droższa
* Masę efektywną można zmniejszyć
	* atom germanu jest większy od krzemu
	* jak zastąpimy w krysztale krzemu część atomów germanem
	* te większe naprężają strukturę krystaliczną
	* doświadczalnie widzimy że to zmniejsza masę efektywną

## Filtry optyczne
* Zastosowanie różnych progów absorpcji krzemu i germanu

## Diody świecące
* Nie ma specjalnie wyboru przy kolorze zielonym
* Problem z diodą świecącą na biało
	* element świecący na niebiesko, np. GaN
	* obudowa pokryta luminoforem, pobiera energię od diody i oddaje w zakresie widzialnym

## Koncentracja ładunków
* Ile elektronów (lub dziur) mamy w krysztale
* Koncentracja - liczba nośników w jednostce objętości (cm^3)
* n - koncentracja elektronów
* p - koncentracja dziur
* Koncentracja równowagowa
	* $n_0$, $p_0$
	* w równowadze termodynamicznym
	* w ustalonej temperaturze, np. 300K
	* elektrony ruszają się
* Procesy wstrzykiwania z zewnątrz
* strumienie elektronowe się kompensują
	* wypadkowy prąd jest 0


### Opis formalny
* Koncentracja elektronów w paśmie przewodnictwa
	* obowiązuje zakaz Pauliego
	* w danej temperaturze elektrony zajmują poziomy z jakimś prawdopodobieństwem
* Rozkład Fermiego-Diraca
	* $E_F$ - poziomy powyżej są wolne, poziomy poniżej są obsadzone
	* leży gdzieś po środku przerwy zabronionej
	* im bliżej pasma przewodnictwa tym więcej elektronów
	* $p_0n_0$ nie zależy od $E_F$

## Półprzewodnik samoistny
* $p_0=n_0=n_i$, - koncentracja samoistna
* Tylko przez samoistne przechodzenie...
* Poziom Fermiego $E_i$ w połowie przerwy zabronionej (mniej więcej)
* W krzemie w 300K $n_i=10^{10}/cm^3$
	* bardzo słabo przewodzi prąd
* Dla porównania w metalu jest rzędu $10^{22}$
	* prąd będzie dużo większy
* Krzem samoistny to idealnie czysty, bez defektów i domieszek
	* inne atomy wbudowują się w sieć krystaliczną
* Liczba samoistnych elektronów mocno zależy od $E_G$ (przerwy)
	* większa przerwa - mniejsza koncentracja
* Zastosowania krzemu samoistnego
	* rezystor (termistor, fotorezystor)

## Półprzewodnik niesamoistny (domieszkowy)
* Najczęściej w praktyce
* Typy
	* donorowy
	* akceptorowy
* Donorowy
	* atom krzemu zastąpiony np. atomem fosforu
	* ma 5 elektronów walencyjnych, 4 tworzą wiązania, a 1 jest swobodny
	* piąty elektron jest ciągle związany z jądrem
	* wystarczy niewiele energii żeby przeniósł się do pasma przewodnictwa
	* jądro zostaje dodatnio zjonizowane
	* donory zwiększają koncentrację elektronów, dziur nie
	* półprzewodnik typu n
	* $n_0 > p_0$, liczba dziur wynika z temperatury