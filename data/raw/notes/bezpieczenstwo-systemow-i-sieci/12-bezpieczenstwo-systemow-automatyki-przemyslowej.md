# Bezpieczeństwo systemów automatyki przemysłowej

## Systemy automatyki przemysłowej
* Industrial Control System (ICS)
* Sprzęt i oprogramowanie
	* kontrola procesów przemysłowych w fabrykach
	* kontrola procesu wytwarzania energii
	* monitoring i obsługa instalacji przemysłowych (prąd, gaz, ciecz)
* Systemy DCS - distributed control system
* Systemy SCADA - supervisory control and data acquisition ze sterownikami PLC
* Czasami określa się jako systemy OT (operational technology) w odróżnieniu od IT
* Bezpieczeństwo może gwarantować całkowite odizolowanie od systemów IT i internetu
	* w praktyce rzadkie
* Coraz więcej systemów podłącza się do internetu

## Infrastruktura krytyczna
* Zaopatrzenie w energię, surowce energetyczne, paliwa
* Sieci teleinformatyczne
* Zaopatrzenie w żywność
* Zaopatrzenie w wodę
* Produkcja, składowanie, przechowywanie substancji chemicznych
* itd.

## Ataki na systemy ICS
* Mogą uszkodzić fizycznie bardzo drogi sprzęt
* Może prowadzić do zagrożenia życia ludzi
* Aktualnie większość ataków zaczyna się w sieci biurowej i w dalszej fazie uzyskuje dostęp do ICS
* Coraz więcej systemów podłączanych do internetu

## Stuxnet
* Część atakuje system Windows i rozprzestrzenia się przez zainfekowane dyski USB
* Infekował sterowniki PLC
* Atak na irański program atomowy

## Bezpieczeństwo
* Dawniej uważało się że odseparowanie systemów IT i OT zapewnia bezpieczeńśtwo
* Obecnie stawia się na bezpieczne połączenie systemów IT i OT
* Połączenie dobrze zdefiniowanych warstw z kontrolowanymi połączeniami między warstwami
	* np. kabel albo śwaitłowód przesyłający dane jednokierunkowo
	* zasada najniższych uprawnień
* Wiele protokołów ICS jest całkowicie pozbawionych mechanizmów bezpieczeństwa
	* nieszyfrowana transmisja
	* brak ochrony integralności danych
	* brak kontroli dostępu
	* często podejście security by obscurity
* Głównym sposobem zabezpieczenia systemów ICS jest segmentowanie sieci
	* komunikacja między segmentami wykorzystuje dedykowane urządzenia
	* zapory ogniowe dla ICS
	* diody danych
* Zapora ogniowa dla ICS
	* firewall warstwy 7 obsługujący odpowiedni protokół
	* możliwość blokowania wybranych oepracji (odczyt/zapis wybranych rejestrów)
* Dioda danyh
	* urzązenie umożliwiające komunikację w jednym kierunku
	* np. kabel ethernet z przeciętą jedną żyłą
