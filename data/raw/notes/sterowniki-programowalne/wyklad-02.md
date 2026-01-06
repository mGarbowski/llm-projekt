# Języki programowania PLC (2025-03-06)

## Języki OT
* Operational Technology (automatyka)
* Działalność OT dotyczy
	* obsługi procesów przemysłowych
	* zarządzanie pracą maszyn i systemów automatyki
	* prezentacja informacji
	* bezpieczeństwa (safety) procesu i kadry technicznej
* Przetwarzane dane
	* dane procesowe
	* dane różnorodne w jednym procesie
	* dane unikalne w każdym procesie
	* ilość danych mniejsza niż w IT
	* gwarantowany czas reakcji
* Unikalność danych - nie da się napisać uniwersalnego programu np. do cukrowni
	* nie ma gotowych framework'ów
* Nacisk na ciągłość działania procesów wpływa na dłuższy cykl życia rozwiązań OT (20-25 lat)

## Bezpieczeństwo (safety)
* Kluczowe w OT
* Bezpieczeństwo procesu i pracujących ludzi
	* system nie stwarza zagrożenia
* Fail-safe controller
	* osobne urządzenia które niczym nie sterują, tylko pilnują bezpieczeństwa

## Różnica między językami w OT i IT
* IT
	* paradygmat obiektowy
	* możliwie ogólne oprogramowanie
	* parametryzacja, modułowość
	* skalowalność, przenoszalność
	* wymaga myślenia abstrakcyjnego
* OT
	* realizacja liniowych algorytmów wykonywanych cyklicznie
	* programy dedykowane konkretnym, często niepowtarzalnym systemom
	* wymaga dobrego zrozumienia wymagań stawianych przez technologię produkcji i sposób pracy urządzeń
	* programy powinny być możliwe do napisania i zrozumienia przez osoby nieprzyzwyczajone do myślenia abstrakcyjnego

## Norma IEC 61131-3
* Norma opisująca graficzne i tekstowe języki programowania dla sterowników PLC
* Konkretne rozwiązania
	* CoDeSys
	* ISaGRAF
	* SIMATIC STEP 7
	* SIMATIC TIA Portal
	* GX Works
* CoDeSys
	* do pewnego stopnia abstrakcyjne względem konkretnego sterownika
* Norma definiuje języki
	* drabinkowy (graficzny)
	* język bloków funkcyjnych (graficzny) - podobny do bramek logicznych
	* lista instrukcji (tekstowy) - niskiego poziomu, podobny do asemblera
	* tekst strukturalny (tekstowy) - wysokiego poziomu wzorowany na Pascalu
	* schemat funkcji sekwencyjnych, SFC (graficzny) - jak schematy blokowe albo diagram stanów, opis algorytmów sekwencyjnych i równoległych, dobre debugowanie - wizualna prezentacja stanów

Na pierwszym labie układy kombinacyjne w języku drabinkowym (LAD) i strukturalnym (ST)
Lepiej zacząć od drabinki i to przenieść na ST niż na odwrót