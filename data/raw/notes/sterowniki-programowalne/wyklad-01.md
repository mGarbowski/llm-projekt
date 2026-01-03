# 2025-02-27

## Siemens
* PROFINET
	* złącze jak ethernet
	* konkretne protokoły specyficzne do zastosowań przemysłowych
	* zielone kable

### Adresowanie modułów
* TB.b
	* T - typ zmiennej
	* B - adres bitu
	* b - adres bitu
* Wejście np. `I0.2`,` I4.6`
* Wyjście np. `Q4.2`, `Q29.6`
* Znacznik (Memory) np. `M0.0`, `M23.4`

## Mitsubishi
* Kompaktowy
* Binarne IO
* Stanowisko na lab ma dołożone moduły analogowych IO

## Przekaźnik elektromagnetyczny
* Obwód prądu stałego z niskim napięciem i cewką
* Obwód załączanego urządzenia z prądem zmiennym o wysokim napięciu (230V)
* Cewka oddziałuje magnetycznie na kotwicę, która zwiera obwód z sygnałem o dużej mocy
* Izolacja galwaniczna
	* nie ma połączenia między obwodami
* Sygnał małej mocy przełącza sygnał o dużo większej mocy
* Sygnał o dużej mocy może usmażyć elementy sterujące gdyby zewrzeć te obwody
* Przekaźnik z wieloma stykami
	* Normalnie Otwarte i Normalnie Zamknięte
	* 2 pozycje
	* przeniesienie sygnału albo negacja sygnału
	* można z tego złożyć układy logiczne

## Język drabinkowy
* Po lewej jest zasilanie, po prawej masa
* Oznaczenie jak kondensator to styk normalnie otwarty
* Oznaczenie z kreską pod skosem - normalnie zamknięty
* Oznaczenie z okrągłymi nawiasami - wyjście na port wyjściowy albo do pamięci
* Translowany na język instrukcji (*prawie* asembler)
* Są pewne *chytrości* w języku - omówimy potem
	* program jest wykonywany szeregowo
	* sterownik steruje obiektem, który może wysyłać do pewnego stopnia nieprzewidywalne sygnały

## Wykonywanie programu
* Program chodzi w pętli
	* mechanizm wbudowany w system operacyjny sterownika
* Trzeba mieć świadomość ile trwa pętla (rzędu 1ms)
	* ważny jest stosunek do minimalnych czasów w obiektach
	* sterownik musi być dużo szybszy
* Może być w ramach jednego przebiegu wiele odwołań do tej samej zmiennej
	* co jeśli sygnał wejściowy zmieni się w trakcie cyklu
* Najpierw wejścia są czytane do tablicy obrazów wejść
	* obraz rzeczywistości obowiązujący na czas przebiegu
	* potem program odczytuje wejścia z tablicy
	* snapshot
* Wyjścia są zapisywane do tablicy obrazów wyjść i dopiero po całym cyklu następuje sterowanie
	* jednocześnie zostaną udostępnione do świata zewnętrznego (do obiektów)
* Zapis do zmiennej wyjściowej nadpisuje poprzednią wartość
	* jeśli w jednym cyklu są 2 zapisy do tego samego wyjścia to jest błąd w programie
* Instrukcja `IF` nie działa tak jak się myśli że działa - o tym później

## Opóźnienie reakcji sterownika
* Na rysunku najbardziej złośliwy przypadek
* Maksymalne opóźnienie jest jeśli sygnał na wejściu zmieni się tuż po odczycie do tablicy na początku cyklu
