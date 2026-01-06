# Adresowanie w sieci
Każdy z nagłówków MAC, IP, TCP/UDP zawiera adres nadawcy i odbiorcy.

TCP - numer portu, rozszerza adres IP komputera (interfejsu sieciowego). Numer portu adresuje proces na komputerze (działający program), są przydzielane przez system operacyjny.

Adresy w nagłówkach IP i MAC są redundantne, oba wskazują na interfejs sieciowy (komputer). Jest tak częściowo z przyczyn historycznych.

Adresy MAC (inaczej EUI-48) są globalnie unikalne, historycznie dzieliły się na 3 bajty prefiksu przydzielanego producentowi i 3 bajty numeru seryjnego, obecnie przydziela się dłuższe prefiksy dla mniejszych producentów.

Adresy MAC nie nadają się do routingu w sieci globalnej, tabele routingu IP pozwalają na oszczędniejsze i bardziej efektywne adresowanie dzięki agregacji. Sposób przydzielania adresów IP jest nastawiony na umożliwienie agregacji. Hierarchia instytucji IANA -> rejestry regionalne -> dostawcy internetu (ISP) jest nastawiona na odzwierciedlenie topologii sieci.

Program może bez problemu wypełnić pola adresu nadawcy. Port odbiorcy wynika z rodzaju usługi (port 80 dla HTTP itd.). IANA określa listę well-known services, która przydziela numery portu usługom. Adres IP jest rozwiązywany na podstawie nazwy domeny przez protokół DNS. Adres sprzętowy (MAC) jest rozwiązywany na podstawie adresu IP przez protokół ARP (Address Resolution Protocol).
