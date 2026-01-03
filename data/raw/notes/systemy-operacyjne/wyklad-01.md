# Wprowadzenie

## System operacyjny
zbiór programów i procedur spełniające 2 podstawowe funkcje
* zarządzanie zasobami systemu komputerowego
	* musi je przydzielać każdemu procesowi sprawiedliwie
	* nie ma żadnej drogi na obejście systemu operacyjnego przy dostępie do tych zasobów
* tworzenie maszyny wirtualnej (tworzenie abstrakcji dla programisty)

## Zasób systemu
Każdy element sprzętowy lub programowy, który może być przydzielony danemu procesowi

### Zasoby sprzętowe
* czas procesora
* pamięć opoeracyjna
* urządzenia zewnętrzne
* inne komputery połączone w sieci

### Zasoby programowe
* pliki
* bufory
* semafory
* tablice systemowe

Procesy dostają przydział zasobów za pośrednictwem wywołań systemowych

Zasobami zarządza się w czasi i w przestrzeni (w którym momencie, które kawałki)

## Tworzenie maszyny wirtualnej
Polega na udostępnieniu użytkownikowi (programiście) abstrakcji systemu łatwiejszej do wykorzystywania / oprogramowywania