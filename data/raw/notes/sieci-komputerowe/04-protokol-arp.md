# Address Resolution Protocol (ARP)
Służy do znalezienia jaki adres MAC odpowiada adresowi IP

Zapytanie z adresem IP jest wysyłane w trybie broadcast - do wszystkich komputerów sieci lokalnej (jest do tego specjalna wartość adresu MAC). Komputer posługujący się danym adresem IP zwraca żadającemu odpowiedź ze swoim adresem MAC. Adresy są cache'owane żeby uniknąć powielania zapytań (typowo na 2 minuty).

Routery nie przepuszczają pakietów z adresami broadcastowymi. Żeby poznać adres MAC trzeba wysłać żądanie do routera.

Karta sieciowa domyślnie odrzuca ramki nie adresowane na jej adres sprzętowy. Kartę sieciową można przełączyć w tryb w którym odbiera wszystkie ramki na potrzeby debuggowania (sniffer). Przełączniki sieciowe (switch) dostarczają ramki na podstawie adresu sprzętowego.

Konieczność podawania adresu MAC wynika głównie ze względów historycznych, najpierw były sieci lokalne.

## Pakiet
* MAC header
* hardware type
* protocol type
* hlen - długość pól hardware address
* plen - długość pól protocol address
* opcode
* sender hardware address
* sender protocol address
* receiver hardware address
* receiver protocol address

Polecenie `arp` w Linuxie


## Rozpoznawanie sąsiedztwa
Problem rozpoznawania sąsiedztwa - komputer musi podjąć decyzję czy skierować zapytanie do komputera w sieci lokalnej (sąsiadującego) czy do routera. Klasy adresu IP mają rozwiązywać ten problem

1. Komputer wysyła żądanie z docelowym adresem IP i adresem MAC swojego routera do tego routera
2. Router usuwa nagłówek MAC i tworzy nowy z własnym adresem jako źródło i adresem następnego routera jako odbiorcy.
3. Ostatni router pozyskuje adres MAC docelowego komputera w sieci lokalnej i odsyła odpowiedź

Nagłówki MAC są wymieniane przy każdym skoku, nagłówek IP pozostaje w zasadzie be zmian. IP opisuje trasę pakietu jako całość, od pierwotnego nadawcy do docelowego odbiorcy. Nagłówek MAC opisuje aktualny etap trasy.

