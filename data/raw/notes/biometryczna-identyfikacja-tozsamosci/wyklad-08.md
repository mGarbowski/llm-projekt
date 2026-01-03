# Rozpoznawanie mówcy (2025-12-08)

## Przetwarzanie mowy
* Analiza i synteza
* Kodowanie
	* kompresja
	* przekształcenie sygnału na formę cyfrową
* Rozpoznawanie
	* mowy
	* języka
	* emocji
	* wykrywanie patologii (chorób)
	* mówiącego (speaker recognition)
		* detekcja (diaryzacja - kto mówi kiedy)
		* weryfikacja - 1-1
		* identyfikacja - 1-n

## Biometria głosowa
* Determinowana przez czynniki
	* anatomiczne - kształt i rozmiar organów produkujących głos
	* wzorce behawioralne - sposób mówienia
* Korzyści
	* łatwość użycia

## Historia
* The VODER - 1939
* Pierwszy model procesu wytwarzania mowy - 1960
* Uszczegółowienie modeli - 1970

## Warianty rozpoznawania mówców
* Ustalonej treści
	* fixed-text
	* rejestracja i uwierzytelnienie na podstawie tego samego ustalonego tekstu (hasła)
	* łatwość oszustwa
* Zależne od treści
	* text-dependent
	* uwierzytelnienie na podstawie tekstu podanego przez system
	* łatwość oszustwa, np. złożenie całej wypowiedzi z fragmentów
* Niezależne od treści
	* text-independent
	* wybór tekstu pozostawiony użytkownikowi
* Konwersacyjne

## Cechy mówców
* Niskopoziomowe
	* jak brzmi twoje gardło
* Wysokopoziomowe
	* jak brzmi twój mózg

## Fonemy
* Dla języka polskiego system fonologiczny jest złożony

## Formanty
* Częstotliwości charakteryzujące tor akustyczny
* Związane z budową organów

## Cechy audio
* Energia
* Ton
* Spektrogram
* Log-Mel Spektrogram
* Cepstralne współczynniky częstości Mel

## Przebieg czasowy
* Waveform
* Próbkowanie - do dyskretnego czasu
	* kluczowe zakres 300-3500 Hz
	* twierdzenie Nyquista
	* aliasing

## Kwantyzacja amplitudy
* Liniowa
* Logarytmiczna
* Adaptacyjna
	* np. dla mowy o różnej głośności

## Spektrogram
* Do rozpoznawania człowieka raczej wykorzystuje się zakresy 0-4kHZ
* Wyższe częstotliwości wykorzystuje szczególnie dla zabezpieczania systemów biometrycznych na ataki
* Rozkład na obwiednię i strukturę harmoniczną

## Skala melowa
* Nieliniowa
* Lepiej odpowiada ludzkiej percepcji niż skala liniowa

## Log-Mel spektrogram
* Ludzkie ucho ma lepszą rozdzielczość dla niskich zakresów częstotliwości
* Filtry trójkątne, więcej w niskich częstotliwościach
* Wzmacnia składowe sygnału bardziej istotne dla człowieka

## Cepstralne współczynnniki częstotliwości MEL (MFCC)
* Kroki
	* FFT (wyznaczenie widma z próbki audio)
	* Filtry mel (przekształcenie widma na log-mel widmo)
	* analiza cepstralna
	* ...

## Pipeline systemu weryfikacji mówcy
* Przygotowanie modelu
* Faza rejestracji
* Faza testowania - rozpoznawania

## Cechy zbioru treningowego do rozpoznawania mówców
* Wiele mówców
* Zróżnicowany i reprezentatywność
	* akcenty, tonacje, środowiska nagraniowe, płeć, wiek
* Augmentacje danych
	* raczej nie można użyć 1 do 1 augmentacji z obrazów do spektrogramu
	* augmentacja audio i potem wyznaczenie spektrogramu

## Cechy akustyczne
* Spektrogram
* MFCC
* LFCC
* Embeddingi
	* Whisper
	* wav2vec2
	* HuBERT


## Przygotowanie modelu i trening
* Wybór architektury
* Przygotowanie danych
* Augmentacja
* Trening modelu
* walidacja i optymalizacja
* Testowanie

## Cechy osobnicze - metody rozpoznawania mówców
* Metody nieparametryczne
	* minimalne założenia strukturalne dotyczące danych
	* skuteczne gdy jest dużo danych dobrej jakości
* Metody parametryczne
	* np. SVM
* Sieci neuronowe

### Embeddingi
* Problem z próbkami do przetworzenia
	* różna długość
	* można usunąć ciszę

## X-Vectors
* 3 części
* Część kodowania
* Część grupowania
* Warstwa klasyfikacyjna
	* embeddingi wyciągane z pośredniej warstwy
* Strata krzyżowa entropii kategorialnej
	* nie wymaga trudnego negatywnego próbkowania

## TDNN
* 1d rozszerzona konwolucja
* agreguje informacje na większym polu recepcyjnym

## Resnet
* Też używany do audio
* Res2Net

## Wyzwania w automatycznym rozpoznawaniu mówców
* Stany patologiczne
	* problemy medyczne
* Różnica między mową czytaną i swobodną
* Szumy
	* można próbować odszumiać próbki przed modelu rozpoznawania
	* odszumianie może wpływać na zawartość informacyjną
* Zmiana głosu z wiekiem

## Ataki na systemy
* Są głosy bardziej generyczne które łatwiej naśladować
* Bezpośredni dostęp do próbki
* Odtworzenie (replay attack)
* Text to speech (TTS)
* Konwersja głosu (STS)
	* audio na audio

## Text to speech
* Na wejściu tekst i cechy mówcy
* Na wyjściu syntetyczny głos mówcy wypowiadający tekst
* Analiza cech lingwistycznych tekstu
* Model akustyczny przekształca cechy lingwistyczne na akustyczne
* Vocoder - analizuje mowę, wyznacza cechy akustyczne
* Modele end to end łączą cały potok w jednym modelu

## Konwersja głosu
* Źródłowy mówca
* Docelowy mówca
* Nadal występują problemy z przeciekaniem cech mowy docelowego mówcy na wyjście
* Do trenowania
	* dane równoległe - wiele osób mówi to samo
	* dane nierównoległe - bez bezpośrednich odpowiedników