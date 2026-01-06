# Sygnały akustyczne

## Sygnał akustyczny a foniczny
* Źródło dźwięku generuje falę akustyczną (sygnał akustyczny, zmiana ciśnienia w czasie)
* Mikrofon (przetwornik) przetwarza sygnał akustyczny na sygnał foniczny (zmiana napięcia w czasie)
* Transmisja, przetwarzanie na sygnał cyfrowy, zapis
* Głośnik z sygnału fonicznego generuje sygnał akustyczny, który dociera do odbiorcy dźwięku

## Dźwięk
Fala dźwiękowa to rozchodzące się zagęszczenia i rozrzedzenia ośrodka wiążące się z lokalną zmianą ciśnienia. Fala dźwiękowa jest falą podłużną. Wartość zmiany (od bazowego ciśnienia, atmosferycznego) nazywamy ciśnieniem akustycznym.

## Analiza częstotliwościowa dźwięku
* Transformata fouriera
* Przejście z dziedziny czasu do dziedziny częstotliwości
* Większość sygnałów akustycznych jest złożona
* W widmie widocznych jest wiele częstotliwości składowych sygnału

## Przebieg czasowy sygnału akustycznego
* Przebieg chwilowych zmian ciśnienia względem średniego ciśnienia atmosferycznego
* Sinusoidalny przebieg nazywamy tonem

## Poziom ciśnienia akustycznego
$$L_p = 20 \cdot \log \frac{p}{p_{ref}}dB \quad p_{ref} = 20 \mu Pa$$
* Wygodna skala do opisywania dźwięków postrzeganych przez człowieka
* Dynamika słuchu do $120dB$

## Składowe harmoniczne dźwięku
* Częstotliwość podstawowa - pół sinusoidy
* Częstotliwości harmoniczne - wielokrotności częstotliwości podstawowej
* Przy generowaniu rzeczywistych dźwięków (np. instrumenty muzyczne) częstotliwości podstawowej towarzyszą jej harmoniczne

## Zakres słyszanych częstotliwości
* Zależy od poziomu ciśnienia akustycznego (SPL) i częstotliwości
* Zakres słyszalności mieści się w
	* od $0dB$ do $120dB$
	* od $20Hz$ do $20kHz$
* Ucho jest mniej czułe na skrajne częstotliwości

## Percepcja dźwięku przez człowieka
* Małżowina uszna
	* odpowieda za zdolność do lokalizacji dźwięku
	* można sztucznie wywoływać ten efekt
* Ucho środkowe
	* błona bębenkowa drgając porusza młoteczek, kowadełko i strzemiączko
	* trąbka słuchowa odpowiada za regulowanie ciśnienia
* Ucho wewnętrzne
	* strzemiączko wywołuje drgania płynu w ślimaku
	* komórki słuchowe poruszane falą w płynie odbierają określone częstotliwości
	* neuroprzekaźniki zamieniają ruch komórek słuchowych na sygnały elektryczne do mózgu

## Wrażeniowe cechy dźwięku
* Cechy, które odbiera aparat słuchowy obserwatora
* Z nich składa się obraz akustyczny w głowie obserwatora
* Wrażenia, a cechy fizyczne dźwięku
	* głośność - poziom ciśnienia akustycznego
	* wysokość - częstotliwość
	* barwa - widmo
	* czas trwania - czas trwania
* Te pojęcia nie są równoważne
* Wrażenie głośności zależy nie tylko od poziomu ciśnienia akustycznego
* Dwa dźwięki o jednakowej częstotliwości mogą dawać wrażenie różnych wysokości
* Subiektywny czas trwania i obiektywny czas trwania nie są tożsame
* Wykorzystuje się te nieoczywiste zależności przy manipulowaniu wrażeniem

### Skale wielkości wrażeniowych
* Skale głośności dźwięku
	* skala fonów
	* skala sonów
* Skale wysokości dźwięku
	* skala melowa

### Zależność głośności od częstotliwości
* Zależność została zbadana eksperymentalnie
* Krzywe izofoniczne
* Głośność mierzona w fonach
* Izofona łączy punkty, które są równo głośne jak ton 1000Hz w 40dB
* Ucho jest bardziej wrażliwe na częstotliwości odpowiadające ludzkiej mowie
* Niskie częstotliwości, na które ucho jest mniej wrażliwe można kodować z mniejszą dokładnością

## Percepcja wysokości dźwięku
* Błona podstawna w ślimaku drga w różnych miejscach dla różnych częstotliwości
* Jeszcze nie do końca wiadomo jak to dokładnie działa
* Teoria miejsca - komórki słuchowe o częstotliwości charakterystycznej odpowiadają za percepcję wysokości konkrentych częstotliwości
* Teoria czasowa - za percepcję wysokości dźwięku odpowiada czasowy przebieg impulsów neuronowych
* Toria filtrów słuchowych - ucho działa jak FFT zamieniając falę na widmo

## Maskowanie dźwięku
* Zjawisko związane z percepcją
* Jedne dźwięki maskują drugie
* Maskowanie częściowe
	* w obecności innego dźwięku (maskera) dźwięki maskowane stają się słyszalne słabiej
* Maskowanie całkowite
	* w obecności maskera dźwięki maskowane przestają być słyszalne
* Zastosowanie np. w open space do maskowania mowy
	* szum babble - wielokrotnie nałożona na siebie mowa
* Wykorzystywane w kompresji dźwięku
	* skoro dźwięk zostanie zamaskowany to nie trzeba marnować na niego bitów
* Eksperymentalnie wyznaczono krzywe maskowania
	* dla dźwięku o podanej częstotliwości i SPL całkowicie zamaskowane zostaną dźwięki pod krzywą
	* można je odrzucić przy kompresji

## Dźwięki szkodliwe dla słuchu
* Pogarsza się z wiekiem
* Długie nastawienie na dźwięk powyżej 85dB może powodować uszkodzenie układu słuchowego
	* przyjmuje się próg 85dB przez 8h
	* przy skróceniu czasu o połowę próg zwiększa się o 3dB
