# 2025-04-04

## Organizacja
Bogdan Majkusiak
Kontakt przez maila

Kolos 2 - 9 V
Kolos 3 - 6 VI

Nie uczyć się wzorów, nie będzie pytań o wzory
Chodzi o zrozumienie mechanizmów fizycznych
Na kolokwium nie będzie obliczeń

## Przetwarzanie informacji
Technika przetwarzania informacji opiera się na jakimś nośniku
W elektronice nośnikiem jest elektron, przepływ elektronów

## Dziedziny elektroniki
Elektronika informacji - elektron jest nośnikiem (obecność lub brak koduje informację)
Elektronika dużych mocy - zarządzanie energią elektronów
Technologia elektronowa - wykorzystuje elektron jako nośnik energii

Inne nośniki informacji - fala elektromagnetyczna o różnej długości
technika mikrofalowa, radiotechnika, technika światłowodowa
Fotonika - pojedynczy foton jako nośnik
Spintronika, elektronika spinowa - spin elektronu jako nośnik informacji
Mechanika, mechatronika - informacja kodowana w ruchu, przemieszczeniu

### Generacje elektroniki
* Elektronika lampowa
	* 1907
	* dalej ma niszowe zastosowania - wzmacniacze muzyczne
* Elektronika półprzewodnikowa (dyskretna)
	* Shockley, tranzystor bipolarny, 1947
* Elektronika półprzewodnikowych układów scalonych
	* tranzystory w jednym kawałku krzemu
* Nanoelektronika
	* oparte o zjawiska mechaniki kwantowej
	* skala nanometrów
	* w laboratoriach, jeszcze nie komercyjnie
* Elektronika molekularna
	* te same zjawiska co nanoelektronika
	* inna technologia
	* realizowana na molekułach
	* w laboratoriach, jeszcze nie komercyjnie

## Działy elektroniki
* Podstawy fizyczne
	* kwantowe i klasyczne
* Elektronika ciała stałego
* Elektronika złączy ciał stałych

Zjawiska fizyczne
Przyrządy
Układy i systemy

## Dlaczego mówimy o podstawach fizyki kwantowej
* Podstawowe właściwości ciał stałych
	* struktura energetyczna
* Przyrządy współczesnej elektroniki wykorzystują zjawiska kwantowe
	* np. dioda tunelowa
* Miniaturyzacja przyrządów klasycznej elektroniki *aktywuje* zjawisko kwantowe
	* zmienia się działanie i musi być uwzględnione w opisie
* Przyszłe generacje będą w coraz większym stopniu bazować na regułach kwantowych
* Ale działanie większości przyrządów elektroniki współczesnej bazuje na fizyce klasycznej

# Elektronika ciała stałego
* Stan elektronu zapisują 4 liczby kwantowe
* Główna liczba kwantowa $n$ - orbita (1, 2, 3)
* Podpowłoki, orbitale - orbitalna liczba kwantowa $l$ 
	* od 0 do n-1
	* oznaczane s, p, ...
	* s - sferyczny, odpowiada $l=0$
	* p - odpowiada $l=1$
* Magnetyzna liczba kwantowa
	* od -l do l
* Atom sodu
	* $1s^22s^2p^63s^1$

## Wiązania
* Jonowe
	* np. NaCL
	* sód ma 11 elektronów, na ostatniej powłoce tylko 1 elektron ($3s^1$)
	* chlor ma 7 elektronów walencyjnych ($3s^2p^5$)
	* sód jonizuje się dodatnio, a chlor ujemnie
	* elektrostatyczne przyciąganie
* Kowalencyjne
	* najważniejsze dla nas
	* np. dwa atomy wodoru z elektronami o przeciwnych spinach
	* cząsteczka nie powstanie jeśli spiny są jednakowe
	* wiązanie jest bardzo silne - trzeba wnieść bardzo dużą energię żeby przerwać wiązanie
	* np. w krysztale diamentu
* Metaliczne
	* między atomami o niewielkiej liczbie elektronów walencyjnych
	* prawdopodobieństwo znalezienia nierozróżnialnych elektronów jest rozproszone w krysztale
* Molekularne
	* różnej natury
	* między molekułami
	* wiązania Van Der Waalsa

## Kryształ węgla
Inaczej są obsadzane podpowłoki jak jest jeden atom, a jak jest wiele
W diamencie - hybrydyzacja - łączą się 2s i 2p - 4 orbitale $sp^3$
Grafen  - silnie 3 razy $sp^2$, czwarty elektron tworzy słabe wiązanie $\pi$ - między warstwami w graficie

## Kryształ krzemu
Na slajdzie uproszczona, płaska reprezentacja (przestrzennie jest podobna struktura do diamentu)
Rdzeń atomowy - bez elektronów walencyjnych (?)

## Pasma energetyczne
* Przy odizolowanych atomach - dyskretne poziomy dla orbitali
* Wynika z równania Schrodingera
* Jak atomy zbliżają się do siebie
	* $3s^2$, $3p^6$ - najsłabsza energia
	* pasma zaczynają się rozszczepiać - funkcje falowe nakładają się na siebie
	* w takiej odległości w jakiej krzem krystalizuje (ok 0.235nm)
	* powstają 2 pasma z $3s^2$, $3p^6$
	* pasmo walencyjne - 4n stanów, 4n elektronów (w pełni obsadzone), górna energia $E_V$
	* pasmo przewodnictwa - 4n stanów, 0 elektronów - dolna energia $E_C$
* Jak pojawi się wolny elektron
* Kryształ o okresowo zmieniającej się energii potencjalnej
	* pasma energii dozwolonych i zabronionych
	* $E_G$ - szerokość przerwy zabronionej

## Podział ciał stałych
* Metale
	* dużo elektronów swobodnych, mogą się przemieszczać
	* nie ma przerwy energetycznej(?)
* Półprzewodniki
	* $0 < E_G < 2eV$
* Izolatory
	* $E_G > 2eV$
* W temperaturze zera bezwzględnego
* Półprzewodniki i izolatory to w zasadzie to samo, umawiamy się na arbitralną granicę
* W temperaturze pokojowej pojawiają się wolne elektrony w półprzewodnikach
	* w krzemie $10^{10}$
	* dla porównania w miedzi $10^{22}$
* Jeśli elektronika ma działać w wysokich temperaturach, to używa się materiałów o większej przerwie energetycznej
	* zamiast krzemu np. węglik krzemu, azotek glinu
* Podział na półprzewodniki i izolatory - **umowny**

## Elektrony i dziury w krzemie
* krzem ma na tyle wąską przerwę, że w temperaturze powyżej 0 część elektronów przechodzi do pasma przewodzenia
* bez przyłożenia potencjału poruszają się chaotycznie
* wolny stan energetyczny - dziura
	* dziura ma swoją energię, pęd, wektor falowy
* Przeniesienie elektronu do pasma przewodzenia
	* np. oświetlenie - kwant światła przenosi większą energię niż $E_G$
	* np. termicznie - drgania
* Potrzebujemy opisu dynamiki
	* jak przyłożymy pole to elektron zareaguje z jakimś opóźnieniem
	* masa cząstek
	* pęd - h/2pi * wektor falowy
* W ciele stałym dynamikę elektronu opisuje masa efektywna
	* druga pochodna energii po wektorze falowym
* W próżni zależność E(k) jest paraboliczna
	* W krysztale jest bardziej złożona, paraboliczna tylko przy minimach lokalnych
* Rozróżniamy dwa typy półprzewodników
	* prosta przerwa zabroniona
	* skośna przerwa zabroniona
* Przejście elektronu z pasma przewodnictwa do pasma walencyjnego
	* emisja fotonu, rekombinacja
	* w krzemie jest zmiana i energii i pędu - skośna przerwa
	* potrzebny jest udział trzeciej cząstki - fonon - energia drgań sieci krystalicznej, niesie duży pęd
	* elektron, dziura, fonon
* Do diod świecących - arsenek galu a nie krzem
	* ma prostą przerwę zabronioną
* Generacja - odwrotny proces do rekombinacji
	* absorpcja promieniowania wiąże się z szerokością przerwy zabronionej