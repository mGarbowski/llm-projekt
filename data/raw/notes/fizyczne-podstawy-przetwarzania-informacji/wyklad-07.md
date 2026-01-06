# Złącza ciał stałych (2024-04-25)

To co dzisiaj będzie już na 3 kolosie
za 2 tygodnie kolos 2

Złącze - kontakt dwóch różnych ciał

Dioda - dwu-końcówkowy przyrząd o nieliniowej charakterystyce prądowo-napięciowej

* Zjawiska kontaktowe
	* napięcie kontaktowe
	* przepływ prądu
	* pojemność

Praca wyjścia

* Kontakt metal-półprzewodnik (MS, dioda Schottkiego)
* Złącze pn
* Układ metal-izolator-półprzewodnik (MIS, MOS)

## Rodzaje złączy i diod
* Rodzaj złącza
	* Schottkiego (złącze MS)
	* Diody pn (złącza pn)
* Technologie
	* diody ostrzowe (MS, pn)problem z niezawodnością ale bardzo mała powierzchnia - mała pojemność pasożytnicza - bardzo szybka
	* diody planarne (MS, pn) - nakładane warstwy

## Napięcie kontaktowe
* Poziom Fermiego
	* charakteryzuje ciało stałe
	* do poziomu fermiego jest pełne obsadzenie w 0K
	* w wyższych temperaturach się rozlewa ponad poziom fermiego
* Poziom próżni jest jednakowy
* Praca wyjścia - odległość między poziomem próżni i poziomem Fermiego
	* średnio ile potrzebuje elektron żeby wyjść do poziomu próżni
* Elektrony chcą przejść z obszaru o wyższym poziomie do tego o niższym (od lewej do prawej na rysunku)
	* prawy obszar ładuje się ujemnie, po lewej zjonizowane dodatnio rdzenie
	* ładunek jest źródłem pola
	* pole skutkuje nachyleniem pasma
* Potencjał
	* wartość skalarna
	* w sposób ciągły się zmienia
	* na rysunku rośnie w dół
* Przerywana linia - poziom próżni - występuje różnica potencjałów
* W stanie równowagi poziomy fermiego się zrównują
* Mamy różnicę potencjałów czyli możemy tego użyć jako źródła prądu?
	* w stanie równowagi termodynamicznej nie ma przepływu prądu
	* jak coś podłączymy do obu obszarów to mamy kolejne kontakty i różnice się zerują - nie ma paradoksu
* Napięcie kontaktowe to wartość teoretyczna
	* nie do zmierzenia woltomierzem - to co napisane wyżej - nie będzie prądu
	* można zmierzyć pośrednio przez pojemność
	* wynika z różnicy prac wyjścia
	* przy złączu pn mówimy o napięciu dyfuzyjnym (inna nazwa)
	* przy MOS nazywane różnicą prac wyjścia

## Przepływ prądu
* Ze źródłem prądu zmiennego
* Pojemność różniczkowa
	* całkowita zmiana ładunku (po lewej taka samo jak po prawej)
	* różnica napięcia
	* pojemność jest funkcją napięcia

## Złącze metal-półprzewodnik (MS)
* Do każdego złącza trzeba doprowadzić kontakt
	* kontakt omowy - liniowa charakterystyka I(U), mały spadek napięcia
	* dioda schotkkiego - silnie nieliniowa zależność
	* właściwosci determinuje różnica w pracy wyjścia metalu i półprzewodnika

## Kontakt omowy
* praca wyjścia metalu jest mniejsza niż półprzewodnika
* pasma się zaginają
* przy powierzchni odległość między poziomem próżni a poziomem fermiego jest większa
	* stan akumulacji - koncentrują się nośniki większościowe

## Dioda Schottkiego
* Praca wyjścia metalu większa od półprzewodnika
* Elektrony przechodzą z prawej do lewej
	* prawa strona zostaje zubożona
	* przy powierzchni - obszar zubożony w elektrony i w dziury
* Powstaje bariera potencjału dla nośników większościowych
* Przepływ prądu
	* przy dodatnim napięciu - wykładnicza charakterystyka
	* przy zaporowym napięciu - bariera dla metalu zostaje taka sama, zanik prądu z półprzewodnika do metalu
	* prąd nasycenia - stały
* Współczynnik idealności
	* mniejszy od 1.2 to dobra dioda
* Niskie napięcie kolana
* Duża szybkość
	* działa "na nośnikach większościowych"
	* brak efektów magazynowania nośników mniejszościowych
	* wąskie gardło - nośniki mniejszościowe, ogranicza szybkość działania układu
* relaksacja dielektryczna - istniejące nośniki
	* rzędu 1 ps
	* w odwrotności daje 1THz

## Diody prostownicze i układy zasilania
* Charakterystyka nie pokazuje prądu wstecznego
* Dobrze się sprawdza dioda schottkiego

## Charakterystyka pojemnościowo-napięciowa C-V

* Obszar zubożony o pewnej grubości $x_d$
	* grubość zależy od napięcia
* Jak dla kondensatora płaskiego, tylko że tu odległość między okładkami zależy od napięcia
* Pojemność praktycznie nie zależy od częstotliwości
* Zamieniając skalę i przedłużając prostą, w punkcie przecięcia z osią wyznacza się napięcie kontaktowe


Na kolosie raczej pytania problemowe
np. czemu nie robi się z krzemu diod świecących
bez notatek
bez obliczeń, nie uczyć się wzorów