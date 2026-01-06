# Polityka bezpieczeństwa

## Bezpieczeństwo
* Bezpieczeństwo jest procesem
* Produkty zapewniają bezpieczeństwo, ale warunki zmieniają się dynamicznie
* W organizacji trzeba wdrożyć cały proces wykrywania, reakcji i wprowadzania zmian

### Polityka bezpieczeństwa
* Dokument w którym jasno i zwięźle wyrażono, co mają osiągnąć mechanizmy zabezpieczeń
* Na początku definiuje się model zagrożeń
	* jakie zagrożenia i ataki bierzemy pod uwagę
* Potem tworzy się *politykę bezpieczeńśtwa*
	* definiuje co należy chronić
	* zarys tego w jaki sposób chronić
* Na końcu wybiera się odpowiednie *mechanizmy zabezpieczeń*
	* żeby spełnić wymagania opisane w polityce bezpieczeństwa

## Szacowanie ryzyka
* Co chronić i ile wydać na ochronę
* Podejścia
	* ilościowe - inwentaryzujemy wszystkie zasoby i oceniamy ile będzie kosztowała nas jego utrata/atak
	* jakościowe - stosowane do dużych organizacji jak miasta czy państwa gdzie nie jest możliwa inwentaryzacja wszystkich zasobów

### Podejście ilościowe
* Single Loss Expectancy (SLE)
	* koszt jednego zdarzenia
	* $SLE = AV \cdot EF$
	* $AV$ - asset value (wartość zasobu)
	* $EF$ - exposure factor (współczynnik zniszczenia)
* Annual Loss Expectancy (ALE)
* roczna oczekiwana strata
	* $ALE = SLE \cdot ARO$
	* $ARO$ - Annualized Rate of Occurence (roczna liczba zdarzeń)
* Podejście typu fuzzy logic

## Bezpieczeństwo na poziomie kraju lub świata

### CERT
* W latach 80 robat zainfekował 10% wszystkich maszyn w internecie
* W efekcie DARPA powołało Computer Emergency Response Team / Coordination Center
	* zespoły reagowania na incydenty bezpieczeństwa
	* założenie CERT wymaga zdobycia licencji itp
* Computer Security Incident response Team (CSIRT)
	* bez potrzeby licencjonowania
	* muszą być oddzielone od administratorów

### W Polsce
* Narodowe Centrum Cyberbezpieczeństwa (NCC) w ramach NASK
	* ma być forum wymiany informacji między instytucjami państwowymi a biznesem
	* umowy o współpracy z telekomami
* Stan aktualny
	* CSIRT NASK
	* CSIRT GOV
	* CSIRT MON
* Warto zgłaszać ataki

## Podejście do ujawniania błędów
* Błędy w aplikacjach zawsze będą
* Już raczej nie ściga się sądowo ludzi zgłaszających błędy
* Poinformowanie producenta
	* producent może zamieść wszystko pod dywan
* Pełne ujawnienie
	* do wiadomości publicznej
	* producent musi zareagować
	* naraża użytkowników końcowych
* Odpowiedzialne ujawnienie
	* poinformować producenta i ujawnić informacje po rozsądnym czasie
* CERTy mogą przyjmować zgłoszenia i działają jako zaufana trzecia strona

### Płacenie za błędy
* Firmy wprowadzają jasną ścieżkę informowania o wykrytych błędach
* Bug Bounty
* HackerOne - firma łączy White Hats z potencjalnymi klientami
* Testowanie cudzego oprogramowania pod kątem bezpieczeństwa bez zgody to nadal próba ataku z punktu widzenia prawa

###  Open Source Intelligence
* Przestępcy otwarcie dzielą się wiedzą
* Firmy, organizacje, rządy niechętnie dzielą się informacjami o atakach
* Istnieją ogólno dostępne zasoby związane z udostępnianiem informacji i analiz cyberbezpieczeństwa
	* warto zgłaszać próbki malware'u do analizy

## Cele mechanizmów bezpieczeństwa
* Odstraszanie
* Wykrycie
* Alarm
* Powstrzymywanie
* Reakcja
* Edukacja
* Żeby system dobrze działał powinien obejmować wszystkie wymienione

## Reakcja na incydenty
* Incident response
* Aktualnie przykłada się dużą uwagę do wykrywania i prewencji ataków
* Najważniejsza jest odpowiednia reakcja
	* wyjaśnienie co się stało, jak do tego doszło
	* jakie są straty
	* czy będą podjęte dalsze kroki prawne
	* co można zrobić żeby zapobiec kolejnym atakom tego typu

## Edukacja użytkowników
* Coraz więcej osób pracuje z wykorzystaniem komputera, poczty elektronicznej, internetu
* Użytkownicy podatni na socjotechnikę - nikt im tego nie wytłumaczył
* W organizacjach powinno prowadzić się Security Awareness Campaign
	* treningi na co zwracać uwagę żeby nie stać się ofiarą socjotechniki
	* szczególnie dla nietechnicznych
