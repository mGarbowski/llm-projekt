# Obsługa wejścia/wyjścia (2024-01-16)

## Obsługa przerwań
(powtórka)
Są mechanizmem reagowania na normalnie występujące asynchroniczne zdarzenia

Urządzenia zewnętrzne mają fizyczne linie sygnałowe do kontrolera przerwań. 
To kontroler przerwań ma dostęp do magistrali systemowej
Kontroler ustala priorytety
CPU w pętli odpytuje kontroler przerwań (na poziomie mikrorozkazu) o najważniejsze przerwanie
CPU musi odesłać sygnał potwierdzający odbiór

Przerwanie o wyższym priorytecie może przerwać obsługę przerwania o niższym priorytecie

Przerwanie precyzyjne - pozostawia proces w dobrze zdefiniowanym stanie

## Direct Memory Access (DMA)
Większość operacji IO to transfer danych między pamięcią główną a urządzeniem zewnętrznych (zazwyczaj duży blok danych)

Odczyt danych bez DMA (aktywne oczekiwanie lub przerwania) odbywa się w słowach procesora (mało), na odczyt jednego bloku potrzeba np kilkuset przerwań, każde przerwanie do przełączenie kontekstu, które unieważnia cache

Układ DMA to procesor (prosty), kontroluje wymianę danych między pamięcią główną a urządzeniami zewnętrznymi.
Operacja zapisu bloku na dysk z DMA
1. Procesor zleca układowi DMA wykonanie zapisu
2. Procesor przełącza się i wykonuje inne procesy
3. DMA będzie rywalizować z CPU o dostęp do magistrali (arbitraż dostępu do szyny, to obniża wydajność)
4. DMA zajmuje magistralę w czasie tych cykli procesora kiedy CPU nie czyta z pamięci
5. Nie ma przerwań generowanych przez urządzenia zewnętrzne
6. Na koniec odczytu, kontroler DMA generuje przerwanie informujące CPU o zakończeniu operacji

Zamiast kilkuset przerwań jest jedno przerwanie
Operacje z DMA nie muszą być szybsze niż bez DMA, to zależy

## Typy urządzeni zewnętrznych
* Urządzenie blokowe
	* Jeśli na poziomie urządzenia istnieje pojęcie adresu
	* Np dysk twardy
* Urządzenie znakowe
	* Np. klawiatura
* Urządzenia komunikacyjne / sieciowe
	* nie pasują ani do blokowych ani do znakowych
* Zegary

W Unixie każde urządzenie jest widoczne w pliku jako plik specjalny (pozycja katalogowa)
Wiąże nazwę z grupą atrybutów identyfikującą odpowiednią strukturę jądra (a nie i-node jak dla normalnych plików)

Numer major - identyfikator sterownika
Numer minor - identyfikator urządzenia w obrębie sterownika

np. dyski to standardowo /dev/sda /dev/sdb ...
a partycje to np. /dev/sda1 /dev/sda2 ...

Można podmienić numery major i minor /dev/null i zbierać informacje, które miały być ukryte

Złożoność systemu operacyjnego to głównie złożoność w obsłudze wejścia/wyjścia

## Cele oprogramowania IO
* Niezależność obsługi ogólnej od specyfiki urządzenia
* Ujednolicenie nazewnictwa
* Obsługa błędów
	* w im niższej warstwie tym lepiej
* Metoda przesyłania
	* blokująca / nieblokująca
	* synchroniczna / asynchroniczna
* Buforowanie
	* Podwójne buforowanie - jak bufor odczytu się zapełni to przełącza się na pusty, a tamten można teraz opróżniać

W praktyce rozwiązania blokujące "na zawsze" się nie sprawdzają, zawsze muszą być timeouty

## Poziomy obsługi urządzeń IO
1. Poziom fizyczny 
2. Poziom procesu
3. Poziom usług

## Komiunikacja z urządzeniami IO
### Porty wejścia / wyjścia
Z rejestrami kontrolnymi są skojarzone porty (odrębna przestrzeń adresowa) o ustalonych numerach, komunikacja przez instrukcje asemblerowe (dostępne tylko z poziomu jądra), które wykorzystuje się w implementacji wywołań systemowych
```
in reg, port
out port, reg
```

Numery portu mogą być wbite na sztywno na płycie głównej, konfigurowane w BIOS/UEFI
Zazwyczaj są po 2 porty na urządzenie - 1 do komunikatów kontrolnych, 1 do danych

### IO odwzorowywane w pamięci
Porty są zmapowane do konkretnych adresów komórek pamięci

* Taki sterownik można zaimplementować w całości w C bez wstawek asemblerowych
* Nie wymaga dedykowanego mechanizmu ochrony
* Komplikuje architekturę, wiele typów szyn
* Wymaga wyłączenia cache dla tego regionu pamięci

## Programowanie urządzeń IO
1. Programowalne IO, polling, busy waiting
2. Programowanie z wykorzystaniem przerwań
3. Z wykorzystaniem DMA

### Busy waiting
Drukowanie tekstu na drukarce znakowej
```c
copy_from_user(buffer, p, count);
for (i=0; i < count; i++) {
	while (*printer_status_reg != READY);  // busy waiting
	*printer_data_register = p[i];
}
return_to_user();
```

Wskaźniki to porty IO zmapowane do pamięci
To jest najszybsza metoda obsługi tej operacji ale zajmuje czas CPU innym procesom
Stosuje się w praktyce do urządzeń o bardzo szybkich transferach albo np. myszek

### Przerwania
Górna połówka - treść wywołania systemowego
```c
copy_from_user(buffer, p, count);
enable_interrupts();  // przygotowuje obsługę przerwania (inicjuje liczniki itd)
while (*printer_status_reg != READY);
*printer_data_register = p[0];
scheduler();  // proces użytkowy jest dalej zawieszony, oddaje CPU innemu procesowi
```

Planista wznowi jakiś inny proces

Dolna połówka - treść funkcji obsługi przerwania
```c
if (count == 0) {
	unblock_user();  // zmień stan procesu na gotowy do uruchomienia
} else {
	*printer_data_register = p[i];
	count--;
	i++;
}

acknowledge_interrupt();  // inne przerwania mogą się dostać do procesora
return_from_interrupt();
```

Kiedy drukarka będzie gotowa na przyjęcie kolejnego znaku to wygeneruje przerwanie, a procesor obsłuży to przerwanie czyli wykona kod dolenj połówki

`acknowledge_interrupt` musi być wykonanye jak najszybciej bo to kończy sekcję krytyczną kiedy procedura obsługi przerwania jest wyłącznym dysponentem systemu

### Programowanie z wykorzystaniem DMA
Górna połówka
```c
copy_from_user(buffer, p, count)
set_up_dma_controller();
scheduler();
```

Procedura obsługi przerwania generowanego przez kontroler DMA (na końcu operacji)
```c
acknowledge_interrupt();
unblock_user();
return_from_interrupt();
```

Za tydzień tworzenie sterownika urządzenia