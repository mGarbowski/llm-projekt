# Podstawy sieci

## Sieć
* Sieć - system komunikacyjny łączący węzły (hosty)
* Intersieć - sieć hierarchiczna - sieć łącząca sieci
* Internet - intersieć o światowym zasięgu bazująca na standardowych protokołach rodziny TCP/IP
	* i protokołach stowarzyszonych, protokołach wyższego poziomu
	* ICMP, ARP, DNS, SNMP, SMTP, FTP, HTTP, LDAP, telnet

TCP/IP - akronim na zestaw standardowych protokołów

AS - system autonomiczny
Autonomiczna sieć, która istnieje z punktu widzenia publicznego routingu

## Przykładowy program
```go
// simple TCP server (c) Grzegorz Blinowski for PSI 2023
package main

import (
	"flag" // command line parsing
	"fmt"  // printing
	"net"  // sockets
	"time" // clock time
)

const (
	SERVER_HOST = "localhost"
	SERVER_PORT = "8001"
	PROTO       = "tcp"
)
const (
	NET_BUF_SZ = 1024
)

func main() {
	// Command line parsing: -host <host-address> -port <port-numer>
	HostargPtr := flag.String("host", SERVER_HOST, "Host to connect to")
	PortargPtr := flag.String("port", SERVER_PORT, "Port to connect to")
	flag.Parse()

	server_socket, err := net.Listen(PROTO, *HostargPtr+":"+*PortargPtr)
	if err != nil {
		panic(err)
	}

	defer server_socket.Close()
	
	fmt.Println("waiting for client...")
	
	for {
		client_socket, err := server_socket.Accept()
		if err != nil {
			panic(err)
		}
		
		fmt.Println("Client connection accepted.")
		
		// concurrent server -serves multiple clients with go routine
		go func(csocket net.Conn) {
			buffer := make([]byte, NET_BUF_SZ)
			msgLen, err := csocket.Read(buffer)
			if err != nil {
				panic(err)
			}
		
			fmt.Printf("Received %d bytes from socket, data=[%s]\n", msgLen, string(buffer[:msgLen]))
			_, err = csocket.Write([]byte("ACK, resending your data with timestamp: " + time.Now().Format(time.UnixDate) + " " + string(buffer[:msgLen])))
			if err != nil {
				panic(err)
			}
			csocket.Close()
		}(client_socket)
	}
}

```

* Adresowanie
	* adresy sieciowe (IP) lub symboliczne (DNS)
	* porty sieciowe
* Sekwencja poleceń prowadząca do zainicjowania gniazda i *zestawienia łączności*
	* wykorzystanie funkcji gniazd
* Przesyłanie danych
	* niezawodność (dla TCP)
	* wielkość *porcji* przesłanych danych (organizacja transmisji i wydajność)
	* reprezentacja danych - dane mogą być różnie reprezentowane na różnych komputerach, różne wyrównanie pól struktury

## Stos sieciowy
* Warstwowa abstrakcja sieci komputerowych jako sposób na pogodzenie niezgodności sprzętowo-programowych
* Warstwa definiowana poprzez interfejsy (sprzętowe i programowe)
* W idealnym przypadku każda warstwa może podlegać reimplementacji bez naruszania pozostałych
* W sensie abstrakcyjnym komunikacja następuje na poziomie
	* warstwa hosta - odpowiadająca warstwa hosta
	* np. warstwa sieciowa komunikuje się z warstwą sieciową na drugiej maszynie
* Przykład - stos ISO/OSI odpowiada oprogramowaniu
	* (7) aplikacyjnemu
	* (6, 5) bibliotecznemu
	* (4, 3) systemowemu
	* (2, 1) zlokalizowanemu bezpośrednio na sprzęcie

### Stos ISO/OSI
* 7 - aplikacji
* 6 - prezentacji
* 5 - zastosowań
* 4 - transportu
* 3 - sieciowa
* 2 - kanałowa
* 1 - fizyczna

### Stos sieciowy na nasze potrzeby
* Procesu 
	* warstwy 5, 6, 7 ISO/OSI
	* np. WWW, FTP, SMTP
	* komunikaty
* Transportu
	* warstwa 4 ISO/OSI
	* TCP, UDP
	* komunikaty / segmenty
* Sieciowa
	* warstwa 3 ISO/OSI 
	* IP
	* pakiety
* Kanałowa
	* warstwy 1, 2 ISO/OSI
	* Ethernet, Wi-Fi
	* ramki, bity

## Zwielokrotnienie i rozdzielenie danych w stosie ISO/OSI
* Komputer może mieć wiele interfejsów
	* np. ethernet i WiFi
* Komputer może korzystać jednocześnie z oddzielnych stosów IPv4 i IPv6
* Oba stsoy mogą korzystać z tego samego interfejsu sieciowego
* Jeden proces może korzystać z obu stosów na raz
* Dane przechodzą przez kolejne warstwy

### Opakowanie nagłówków
* Zwielokrotnianie i rozdzielanie danych musi odbywać się na podstawie dodatkowej informacji
	* niezależnej od samych danych
* Każda warstwa oprogramowania sieciowego dokłada własny nagłówek
	* powstaje szereg enkapsulowanych nagłówków
* Przy odbiorze danych proces jest odwracany następuje dekapsulacja nagłówków
	* kolejne nagłówki są zdejmowane przez kolejne warstwy
* Na każdą porcję danych przypada pewien narzut związany z nagłówkami
	* trzeba brać to pod uwagę projektując protokół
* Przykładowo, po wysłaniu porcji danych otrzymujemy
	* nagłówek Ethernet
	* nagłówek IP
	* nagłówek UDP
	* dane
	* Ethernes FCS - na końcu!

## Protokoły datagramowe i połączeniowe
* Protokół datagramowy - bezpołączeniowy (connectionless service)
* Protokół połączeniowy (connection oriented service)
* Cechy obu
	* kontrola poprawności
	* sekwencyjność
	* niezawodność - kontrola poprawności i sekwencyjność
	* transmisja simplex lub full/half duplex

### Protokół datagramowy
* Metoda stosowana w sieciach komputerowych
* Nadawca i odbiorca
* Dane podzielone na datagramy
* Podróżuje przez sieć, ścieżka ustalona dynamicznie, oddzielnie dla każdego pakietu
* Każdy pakiet podróżuje niezależnie
* O dalszym losie pakietu decyduje ruter
* Ruter nie utrzymuje informacji o połączeniach
	* nierealne zapotrzebowanie na pamięć
* Droga może być za każdym razem inna
	* datagramy mogą ginąć
	* datagramy mogą przychodzić w zmienionej kolejności
	* datagramy mogą ulec zwielokrotnieniu

### Protokół połączeniowy
* Stosowana w sieciach telefonicznych
* Nadawca i odbiorca
* Komunikacja w fazach
	* zestawienie połączenia (obwodu)
	* wymiana informacji
	* rozłączenie
* Historycznie - zestawianie fizycznych połączeń
* Obecnie - wirtualne połączenia realizowane na protokołach datagramowych

### Dlaczego protokół datagramowy
* Założenia
	* łącza są kosztowne
	* ruch jest nieregularny, charakteryzuje się gwałtownymi skokami natężenia
	* sieć ma być niezawodna - odporna na awarię / zniszczenie pewnej liczby węzłów
* Wiele źródeł danych nadaje z maksymalną prędkością $R$
* Dane trafiają do bufora, z którego są transmitowane z maksymalną prędkością $R$
* Bufor absorbuje krótkotrwałe skoki natężenia ruchu pakietów - łącze nie musi mieć przepustowości $n \cdot R$
* Bufor ma ograniczony rozmiar, przy dłużej trwających skokach natężenia, pakiety będą ginąć
* Multipleksowanie, buforowanie, odrzucanie nadmiaru
	* ogranicza koszty
