# Strumieniowanie multimediów
Problem przy oddzielnych sturmieniach (np. audio i video) jest taki, że potrzebujemy je równocześnie odczytywać i odtwarzać (pojawia się np. problem przy odczytywaniu z płyty CD, odpowiednio indeksować i buforować pakiety przesłane siecią)

## Kontenery multimedialne
* Opakowanie danych multimedialnych w ten sposób, żeby móc je odtwarzać z mniejszą liczbą operacji
* Odpowiednio wymieszane dane i metadane w nagłówkach
* Metadane zawierają informacje kontrolne
* Dane audio i video dzieli się na mniejsze pakiety i przeplata

### Przykłady kontenerów multimedialnych
* Wideo
	* MPEG-2 PS
	* MPEG-2 TS
	* MP4
	* Ogg
	* WebM
	* AVI
* Audio
	* WAV
	* AIFF
	* XMF
* Obrazy
	* TIFF
	* JFIF

## Kontener MP4
* Format łącznego zapisu ścieżek audio i video
	* można też dodawać teksty, obrazy
* Hierarchiczne obiekty - boxy
* Box
	* nagłówek określający rozmiar
	* nagłówek określający typ
* Różne warianty
	* podział na fragmenty o różnym czasie prezentacji
* Metadane nagłówkowe do prezentacji
	* moov - movie box - metadane do wszystkich mediów / ścieżek
	* moof - movie fragment - metadane do fragmentów
	* mfra - moovie random access - wskaźniki do wybranych punktów czasowych w ścieżkach
* Nagłówek mediów mdhd
	* daty/czasy wytworzenia i modyfikacji
	* jednostka czasu (time scale) - ile w 1 sekundzie
	* czas trwania (duration)
	* szybkość odtwarzania
	* macierz 3x3 transformacji kolorów wideo
* Nagłówek ścieżki tkhd
	* daty/czasy wytworzenia i modyfikacji
	* identyfikator (track_ID)
	* czas trwania (duration)
* Metadane zawierają
	* deklaracje ścieżek audio lub video (track)
	* znaczniki czasu
	* przyporządkowanie jednostek audio/video (sample) do kawałków (chunk)
	* deklaracje rozmiaru tablicy jednostek
	* wskaźniki do danych dla kolejnych jednostek w boksie mdat
* Kawałki
	* zasadnicze dane
	* tworzą ciągły zbiór jednostek w pliku
	* mogą zawierać jedną lub wiele jednostek
	* przypisane do różnych ścieżek przeplatają się
	* tablica w nagłówku określa początki/końce
* Format MP4 bazuje na QuickTime
	* w nagłówku pliku jest określony typ, podtyp

## Multipleksowanie strumieni elementarnych
* MPEG-2 określa 2 metody multipleksowania sturmieni elementarnych
* Strumień programowy (PS)
	* DVD
* Strumień transportowy (TS)
	* DVB
	* ATSC
	* IPTV
	* Blu-ray

### Pakietowy strumień elementarny
* Strumień elementarny (ES) dzielony jest na pakiety PES
* Konwersja ES-PES wymagana do tworzenia strumienia programowego (PS) i transportowego (TS)
* Konwersja między TS i PS poprzez PES
* Nie musi być zgodności z jednostkami dostępu ES (np. ramkami) ale w praktyce się zachowuje
* Jednostka dostępu ES - np. klatka filmu - może być dzielony na pakiety PES
* PES mają własne nagłówki, nie muszą pokrywać się w czasie ani miejscu z nagłówkami ES
* PTS / DTS - umożliwiają inny porządek przy prezentacji i dekodowaniu
	* np. ramki B w video
	* Presentation / Decoding Time Stamp

### Multipleksacja MPEG-2 PS
* Strumień programowy (PS) zawiera przeplecione pakiety PES audio i wideo
* Demultipleksacja na podstawie numerów identyfikujących ES z nagłówków PES
* Nagłówek pakietu PS
	* zegar jako licznik o ustalonej podstawie czasu
	* sygnalizacja przepływności
	* bity o stałej wartości (marker bit)
	* nagłówek systemowy
* Strumień PS zapisuje się w plikach z rozszerzeniem
	* mpg, mpeg (audio-video)
	* mpa, mp2, mp3 (audio)
	* pliki vob opracowane na bazie PS
* Multipleksacja
	* strumienie audio i wideo enkodowane i pakietyzowane oddzielnie
	* wspólny sygnał zegarowy
	* oba strumienie trafiają do multipleksera PS
	* na wyjściu strumień programowy
* Demultipleksacja
	* z cyfrowego nośnika danych
	* strumień programowy trafia do dekodera programowego
	* rozdziela strumienie audio i video
	* oddzielnie dekodowane strumienie audio i wideo trafiają na wyjście
	* dekodery sterowane wspólnym zegarem

### Emisja programów TV
* Zaszłości historyczne dotyczące pasm
* Transmisja każdego programu w oddzielnym pasmie jest nieefektywna
	* odstępy międzypasmowe
* Lepiej na danym pasmie multipleksować wiele programów

### Multipleksacja MPEG-TS
* Strumień transportowy TS
	* wiele programów
	* każdy program ma swoje strumienie elementarne i zegar
	* pliki mają rozszerzenie ts lub m2t
* Multipleksacja
	* powielone to co dla strumienia programowego
	* wszystkie trafiają do multipleksera TS
	* każdy z własnym zegarem
* Nagłówek pakietu TS
	* sygnalizacja początku PS (payload_unit_start)
	* identyfikator PID
	* licznik (continuity_counter)
	* sekcja adaptacyjna (adapt_field_ctrl=1)
		* sygnalizacja mniejszej liczby bajtów w pakiecie (adaptation_field_length)
		* PCR - zegar/licznik
* Pakiety TS tworzone z PES
	* pakiet TS trafia w całości tylko do jednego PES
	* na granicy pakietu PES, TS jest padowane zerami
* Pakiety TS mają 188 bajtów
	* nagłówek wydłużany przez opcję adaptacji
	* np. do sygnalizacji ważnych bajtów
	* to że pakiety są małe zapewnia odporność na błędy - błąd w jednym pakiecie nie propaguje się na inne

### Demultipleksacja MPEG-TS
* Strumień transportowy trafia do demultipleksera
* Hierarchiczna identyfikacja ES za pomocą tablic PAT i PMT
* Zegar (licznik) w nagłówkach pakietów o wybranym PID
	* w polu adaptacyjnym
	* nie rzadziej niż co 100ms
* Tablica PAT mapuje programy na identyfikatory PID
* Tablica PMT mapuje strumienie (zegar, video, ściezki audio) na identyfikatory PID

### Multipleksowanie
* Statyczne
	* proste
	* nieefektywne wykorzystanie pasma
	* każdy program dostaje określone pasmo, w którym ma się zmieścić
* Statystyczne
	* pozwala efektywnie wykorzystać pasmo
	* zwiększa jakość
	* wymaga łącznej regulacji przepływności strumieni elementarnych audio-video
	* tam gdzie jest większa złożoność przeznacza się większą część strumienia
* Silne wahania przepływności wpływają na opóźnienie transmisji w kanale
	* niestabilność czasowa
	* konieczne bufory
* Regulacja
	* czas występowania ramek Intra
	* lepiej żeby nie w każdym programie występowały na raz ramki I bo mają większy budżet bitowy
	* siła kwantyzacji - parametr QP

## DVB
* DVB - standard dla transmisji satelitarnej, naziemnej, kablowej
* Moduły DVB przyjmują i odtwarzają strumień transportowy MPEG-2 TS
* Warianty DVB (T/C/S) różnią się sposobem modulacji fali nośnej
* Transmisja odbywa się w ograniczonym pasmie
* Kodowanie kanałowe
	* wspólne dla wariantów T/S/C
	* jest nadmiarowe i ma na celu detekcję i korekcję błędów transmisji
	* kody Reed-Solomon'a (RS)
	* kody splotowe
* Modulator OFDM - charakterystyczny dla DVB-T
* Modulacja fazowa (np. QPSK)
	* pozwala na zwiększenie przepływności bitowej
	* przesyłanie wielu bitów w tym samym momencie
	* dla modulacji fazowej przez odpowiednie przesunięcia fazy

### Modulator OFDM
* Orthogonal Frequency Division Multiplexing
* Wykorzystuje nośne ortogonalne
* Okres ochronny - wydłuża czas trwania
* Dane dzieli się między wiele częstotliwości nośnych w paśmie
	* częstotliwości są ortogonalne i nie wpływają na siebie nawzajem
	* wiele strumieni danych można transmitować jendocześnie
* Wykorzystywana m. in. w standardzie LTE

### DVB-T2
* Większa elastyczność w doborze parametrów
* Większa przepływność
* Lepsza odporność na błędy
* Większe zasięgi przy tej samej mocy
* Większa przepływność kosztem
	* mniejszej ochrony przed błędami
	* większej mocy sygnału
	* mniejszych odległości

## Transmisja multimediów w sieci
* IPTV - po UDP, rzadziej stosowane
* WebTV - telewizja internetowa po HTTP (YouTube, Netflix)
* Usługi
	* telewizja liniowa
	* telewizja nieliniowa (VOD, personal video recorder)
* Problem przepustowość vs jakość, dobór parametrów
	* pasmo
	* stabilność
	* rozdzielczość
	* adaptacja

### Pobieranie multimediów
* Dwie fazy
* Najpierw pobrać, potem odpalić
* Duże opóźnienie
* Nieefektywne
* Dużo danych do buforowania
* Reszta danych może nie być potrzebna

### Transmisja progresywna
* Rozpoczęcie odtwarzania pliku multimedialnego po pobraniu fragmentu pliku
* Efektywna
	* małe opóźnienie - rozpoczęcie odtwarzania pliku mmultimedialnego po pobraniu fragmentu pliku
	* buforowanie małej ilości danych
	* nieodtwarzane treści nie są transmitowane
* O użyciu progresywnej transmisji decyduje odtwarzacz
* Implementacje HTTP z progresją
	* Macromedia - Adobe Flash Player
	* Windows Media Player
	* Quick Time
	* Real Player

### Strumieniowanie przez UDP
* Może gubić pakiety
* Pakiety mogą przyjść w złej kolejności
* Unicast / multicast
	* unicast wysyła wielokrotnie te same dane
* Ok. 7 pakietów sturmienia transportowego pakuje się do jednej ramki UDP
	* im większy tym większe prawdopodobieństwo utraty pakietu
* Transmisja UDP bywa blokowana na routerach, HTTP jest zawsze przepuszczane

### Odporność na błędy
* Dzielenie ramek wideo na plastry (slices)
	* tworzy oddzielne strumienie
	* zmniejsza efektywność kompresji
	* ogranicza zasięg błędów

### Transmisja RTP/RTCP
* Real Time Protocol (RTP)
	* przesyłanie danych mutlimedialnych od nadawcy do odbiorcy
	* może opakowywać
		* strumień transportowy (TS)
		* strumień elementarny wideo (ES)
		* strumień elementarny audio (ES)
	* jeden pakiet RTP zwykle zawiera kilka pakietów TS
* Real Time Control Protocol (RTCP)
	* nadawca i odbiorca wymieniają się warunkami transmisji
	* identyfikacja nadawcy
	* zakończenie sesji
	* raport nadawcy i odbiorcy
		* sparowane
		* czasy
		* opóźnienia
		* liczba pakietów nadanych/utraconych
		* liczba bajtów od początku transmisji
* Oba w UDP

### RTSP
* Real Time Streaming Protocol
* Wykorzystuje TCP
* Podstawowy protokół dla systemów VoD w IPTV
* Steruje dostarczaniem danych multimedialnych rozsyłanych przy pomocy odrębnego protokołu (np. RTP/RTCP)
	* inicjalizacja sesji
	* setup
	* start
	* pauza
	* nagrywanie

## Adaptacyjne strumieniowanie
* Serwer dysponuje wieloma wariantami tego samego wideo o różnych parametrach (jakości)
* W zależności od przepływności bitowej kanału wybierany jest odpowiedni wariant
* Implementacje
	* HTTP Live Streaming
	* HTTP Smooth Streaming
	* HTTP Dynamic Streaming
	* Dynamic Adaptive Streaming over HTTP - MPEG-DASH

### MPEG DASH
* Dostarczanie treścji multimedialnej ze zwykłych serwerów HTTP
* Obsługa różnych rodzajów mediów i różnych kodeków
* Dzielenie treści multimedialnej na segmenty o krótkim czasie trwania i kilku wariantach jakość-przepływność
* Algorytm adaptacji pzrepływności po stronie klienta (inaczej niż w RTP/RTCP)
* Dostępna gotowa biblioteka dla klienta
* Fragmenty multimedialne w pojedynczych plikach lub wielu plikach
* Serwer przesyła klientowi plik MPD
	* opisuje warianty przepływności, kodeki, URL
	* hierarchiczna budowa zapisywana w XML
	* mpd -> period -> adaptation set -> presentation -> segment
	* strumienie multimedialne jako fragmenty w pojedynczych lub w wielu plikach

### Deskryptor MPD
* Media Presentation Descriptor
* Opisuje dostępne ścieżki z podziałem na krótkie segmenty czasowe
	* czasy trwania
	* URL
	* warianty przepływności
	* kodeki
	* charakterystyki
* Struktura hierarchiczna/obiektowa zapisywana w XML
* Segmenty
	* adresowane pozycją bajtową w pliku
	* wylistowane jako oddzielne pliki
	* z generycznymi nazwami do oddzielnych plików

### Wyświetlanie wideo w dokumentach HTML
* Znacznik `<video></video>`
* Pobieranie filmu przez HTTP GET
* Formaty MP3, MP4, WAV
