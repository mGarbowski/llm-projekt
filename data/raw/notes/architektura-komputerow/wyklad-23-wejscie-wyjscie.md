# Wejście/wyjście (2023-06-07)

Porty wejściowe i wyjściowe są widoczne w przestrzeni adresowej

## Budowa komórki pamięci
* dekoder adresu
  * 0 jeśli adres na szynie adresowej odpowiada adresowi komórki
  * 1 jeśli odpowiada
* szyna danych
* bufor trójstanowy - łączenie wyjść wielu bramek
  * wejście danych
  * wyjście danych
  * wejście włączające
  * trzeci stan - wysokiej impedancji - tak jakby układu nie było (rozwarcie)

Port wyjściowy z zapisem zwrotnym - można odczytać to co się do niego zapisało

## Podział interfejsów (historyczny)
* interfejs równoległy
  * tyle drutów ile bitów ma dana
* interfejs szeregowy
  * bity przesyłane jeden po drugim po tym samym drucie

## Dualizm programowo-sprzętowy
Decyzja jak dużo robić w sprzęcie a jak dużo w oprogramowaniu to decyzja ekonomiczna, zmienia się z czasem

## Współpraca z urządzeniem IO
Odczytać z komórki pamięci można w każdej chwili ale tylko kiedy jest gotowe wolno zapisywać / odczytywać

* Aktywne oczekiwanie (polling)
* Przerwania
* Bezpośredni dostęp do pamięci (DMA)

## Aktywne oczekiwanie
* Cały protokół zrealizowany w oprogramowaniu
* Procesor kręci się w pustej pętli tak długo jak drukarka nie jest gotowa
* Nie nadaje się do wielozadaniowych systemów

## Obsługa z użyciem przerwań
* Kiedy urządzenie jest gotowe, urządzenie zgłasza przerwanie
* To nie jest takie proste, dane są buforowane przez system operacyjny
* Obsługa jednego przerwania wymaga wykonania kodu rzędu kilkuset linijek C
* Nie jest oczywiste czy obsługa skomplikowanego przerwania czy długie czekanie w prostej pętli jest lepsze
* Nie nadaje się do szybkich urządzeń, jest jakaś krytyczna częstotliwość przerwań
* Współczesny system może obsłużyć rzędu 10k przerwań na sekundę, na mikrokontrolerach rzędu 100k na sekundę


## Bezpośredni dostęp do pamięci
* Obecnie moduł sprzętowy jest tani
* Sterownik sam transmituje dane między pamięcią i urządzeniem IO zgodnie z gotowością urządzenia IO
* Budowa
  * rejestr adresu pamięci - ładowany początkiem bloku danych do przesłania, inkrementowany po przesłaniu
  * licznik transmitowanych danych - długość bloku do przesłania, dekrementowany po przesłaniu
  * odcina procesorowi dostęp do szyny na czas transmmisji - układ arbitrażu
  * na koniec przesłania bloku (wyzerowanie licznika) zgłasza jedno przerwanie (na samym końcu a nie co bajt!)
* Współczesne każde urządzenie ma wbudowany moduł DMA

## Pamięć masowa
Są 2 bardzo różne technologie

* dyski magnetyczne
* pamięci półprzewodnikowe

* Logicznie to wektor bloków stałego rozmiaru (512B, 4KiB)
* Za organizację danych na blokach odpowiada system plików systemu operacyjnego
* Najmniejsza jednostka jaką można pobrać/zapisać to blok

## Sterownik pamięci masowej
* numer bloku
* liczba bloków
* typ polecenia (odczyt / zapis)
* kod stanu / odpowiedzi
* zazwyczaj DMA
* współczesne sterowniki mogą kolejkować polecenia i optymalizować kolejność operacji dla najlepszego całkowitego czasu

## Dyski stałe magnetyczne
* wirujące sztywne talerze pokryte warstwą magnetyczną z (obu stron)
* koncentryczne ścieżki - kilkadziesiąt tysięcy, podzielone na sektory
* przesunięcie głowicy nad ścieżkę zajmuje czas rzędu ms
* po ustawieniu głowicy trzeba poczekać aż sektor wkręci się pod głowicę
* w sumie czas dostępu rzędu 10ms na ~plik
* Zużywają się mechanicznie (napęd głowicy, łożyska itd)
* Nie zużywa się sam nośnik magnetyczny (20 lat), zużywa się mechanika

## Pamięć półprzewodnikowa
* technologia NAND Flash EEPROM
* bardzo szybki odczyt
* wymaga dodatkowym bitów korekcyjnych (pamięć się myli)
* wymaga skasowania przed zapisem
* blok kasowalny jest duzo większy niż zapisywalny
* długie kasowanie i zapis
* Ograniczona liczba cykli kasowania (blok można skasować nie więcej niż n rzędu 10k, 100k razy)
* Flash Translation Layer
  * algorytmy minimalizują liczbę kasowań
  * pamięcią steruje mikrokomputer
  * balansuje zużycie nośnika
* Nie nadaje się do ciągłego zapisywania dużych plików - nie do obrabiania wideo
* Nie nadaje się do pamięci wirtualnej - jest ciągła wymiana danych, lepiej wyłączyć pamięć wirtualną w laptopie z małym RAMem
* Im bardziej zapełniony tym szybciej się zużywa - lepiej zrobić partycję mniejszą niż całkowita dysku