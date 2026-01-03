# Organizacja

* Egzamin
	* do przepołowienia
	* 3 terminy
	* zerówka dla osób aktywnie uczestniczących w przedmiocie (np. chodzenie na wykład)
	* 60 pkt
* Laboratoria
	* 5 spotkań
	* 8 pkt na spotkanie (40 w sumie)
	* 4 z 5 trzeba zaliczyć
	* pierwsze zajęcia 14 X
* Wysłać maila z preferowanym terminem laboratorium jak ktoś nie jest zadowolony
	* znaleźć grupę docelową w której są miejsca
* W regulaminie na usosie są błędy
* http://zbum.ia.pw.edu.pl/PL/node/64

# Wstęp

## Znaczenie pojęcia
* Bios - życie, metros - pomiar
	* niesprecyzowany cel - np. diagnostyka medyczna, ekologia
* Biometria jako dział informatyki
	* pomiar własności anatomicznych lub własności zachowania człowieka
	* określony cel - automatyczne rozpoznanie tożsamości
* Definicja - zastosowanie własności anatomicznych lub własności zachowania człowieka do automatycznego rozpoznania tożsamości
	* automatyczne - bez udziału eksperta
	* może częściowo wykorzystywać doświadczenie ekspertów (np. daktyloskopii)
	* możliwość braku nadzoru, konieczna duża szybkość, powtarzalność działania
* Własności anatonomiczne lub zachowania
	* w odróżnieniu od innych składników uwierzytelniania (coś co mam, coś co wiem)
* Człowieka
	* odporność na fałszerstwo - np. pokazanie zdjęcia itp
	* testowanie żywotności, autentyczności - niezbędne do nazywania systemu biometrycznym

## Rozpoznanie biometryczne
* Pozytywne
* Negatywne
* Weryfikacja hipotezy - próbka pochodzi od osoby znanej/nieznanej systemowi (wcześniej zarejestrowanej/niezarejestrowanej)

## Schematy uwierzytelniania
* Klasyczne
	* ustalenie tożsamości (identyfikacja) - porównanie 1:n
	* potwierdzenie (weryfikacja) - porównanie 1:1
* Nowe (wynikające z biometrii)
	* negatywne uwierzytelnienie
		* identyfikacja - nie należę do grupy X
		* weryfikacja - nie jestem osobnikiem X
	* eliminacja "wielokrotnych tożsamości"

## Pomiar
* Obiekt - człowiek
* Obserwacja - pomiar
	* np. fotografia
* Charakterystyka lub właściwość biometryczna
	* dziedzina obserwacji
	* wygląd twarzy, kształt dłoni itp. 
* Modalność biometryczna
	* kombinacja charakterystyki i sposobu pomiaru i przetwarzania
	* np. zdjęcie RGB, zdjęcia w podczerwieni, zdjęcie 3D
* Próbka biometryczna - wynik obserwacji
	* wynik obserwacji - surowe lub wstępnie przetworzone dane pomiarowe
	* np. obraz twarzy 3D
* Cecha biometryczna
	* reprezentacja (zwykle skrócona) próbki biometrycznej
	* np. odległości między punktami charakterystycznymi twarzy
	* wyizolowanie trwałych i wyjątkowych elementów z obrazu - te które niosą dużo informacji
	* nieodwracalne przekształcenie - zaleta bezpieczeństwa, mniej boli jak wycieknie wektor cech niż obraz twarzy
* Wzorzec biometryczny
	* dane referencyjne, które zachowujemy w bazie danych na potrzeby rozpoznawania biometrycznego
	* częściowo zazębia się z cechą biometryczną +metadane

## Historia automatycznych systemów biometrycznych
* Lata 60-te
	* automatyczna identyfikacji na podstawie odcisku palca i rozpoznawania głosu
* Lata 70-te
	* geometria dłoni
* Lata 80-te
	* obraz siatkówki i podpis odręczny
* Lata 90-te
	* obraz tęczówki
* XXI wiek
	* zastosowanie na masową skalę
	* biometryczne urządzenia przenośne
	* brak wymagania kooperacji z użytkownikiem

## Podział modalności
* Anatomiczne
	* obraz twarzy
	* tęczówka
	* odcisk palca
	* dłoń
	* głos
	* układ żył
	* termika dłoni, twarzy - raczej jako test żywotności
	* DNA, zapach
	* geometria i termika ucha
* Behawioralne
	* kluczowe są zależności czasowe
	* styl chodzenia
	* podpis
	* charakter pisma
	* fale mózgowe EEG
	* rytm uderzania w klawisze
	* rytm klikania elementów interfejsu scrollowania
	* ruch warg
	* rezonans opuszków palców

## Pożądane własności biometrii
* Unikalność - wysoka zawartość informacyjna
	* niezależne od genotypu, penetracji genetycznej
	* bliźniąt jednojajowych jest zaskakująco dużo!
	* hipoteza o unikalności cech jest uzasadniona tylko eksperymentalnie - nie ma matematycznego dowodu że bliźnięta jednojajowe będą miały różne tęczówki
	* tęczówka jest uważana za najmniej zależną od genotypu, twarz bardziej, DNA całkiem ofc
* Niezmienność w czasie
	* dowód osobisty i paszport jest ważny przez 10 lat
	* odporność na zmiany powodowane chorobami
	* problem starzenia się wzorców - spadająca jakość dopasowania pomiędzy próbkami, których pobranie jest oddalone w czasie (norma ISO)
		* aktualne badania dają sprzeczne wnioski
		* badania muszą być rozciągnięte na wiele lat
		* sprzęt się zmienia w ciągu dekady
* Akceptacja użytkowników
	* DNA - słabe pod tym kątem
	* w celu zwiększenia wiarygodności, dla wygody użytkownika
	* brak wymogu współpracy - możliwe nadużycia
	* obawy społeczne, kulturowe, o prywatność
	* obawy zdrowotne (czy kamera nie uszkodzi wzroku)
	* ochrona danych osobowych
	* dane biometryczne wg. RODO są szczególnie wrażliwe
	* minimalna iwazyjność
	* nieufność do decyzji systemów opartych o UM
* Odporność na fałszerstwa
* Możliwość realizacji technicznej
	* łatwość obserwacji i pomiaru
	* powtarzalność obserwacji i pomiaru
	* powszechność własności biometrycznych
	* niski koszt budowy urządzeń

## System biometryczny i jego decyzje

### Tryby pracy
* Rejestracja
	* wygenerowanie i zapamiętanie wzorca biometrycznego
	* np. wizyta w urzędzie w celu wyrobienia paszportu
* Uwierzytelnienie
	* wykorzystanie zachowanego wzorca do potwierdzenia lub ustalenia tożsamości
	* np. bramka na lotnisku

### Rejestracja
* Trwa dłużej i jest bardziej skomplikowana
* Nadzorowana przez człowieka
	* albo interfejs z instrukcjami
* Wielokrotny pomiar
	* zaostrzona kontrola jakości próbek w celu uzyskania reprezentatywnych danych
	* robi się raz na dłuższy czas, trzeba zadbać o jakość
* Przetwarzanie surowych danych i utworzenie wzorca
	* kontrola spójności cech biometrycznych
* Powiązanie danych biometrycznych z pozostałymi danymi osobowymi
* Zapis wzorców biometrycznych w bazie danych lub na indywidualnym nośniku danych

### Uwierzytelnienie
* Bez nadzoru człowieka
* Odczytanie wzorca biometrycznego z bazy danych (innego nośnika)
* Najczęściej jednokrotny pomiar
	* ma być szybciej
	* test żywotności / autentyczności
	* kontrola jakości
* Przetwarzanie surowych danych, wyznaczenie cech
* Wyznaczenie dopasowania
* Decyzja

### Błędy metod biometrycznych
* Błędne niedopasowanie
* Błędne dopasowanie

### Stopień dopasowania podobieństwa
* Miara podobieństwa weryfikowanej próbki ze wzorcem

### Decyzja
* Dopasowanie lub niedopasowanie
* Podobieństwo musi przekraczać próg decyzyjny
	* ustalony wcześniej

...obrazek z gaussem - **gęstość prawdopodobieństwa**
na egzaminie będą do narysowania wykresy - dobrze go nazwać

### Aproksymacja prawdopodobieństw błędów

False non-match rate
* niebieskie na obrazku
* Jeśli znamy g - całka gęstości
* Jeśli nie znamy - proporcja - prawy gauss z obrazka w mianowniku (wewnątrz klasy)

False match rate
* czerwone na obrazku

Estymator błędu jako funkcja progu decyzyjnego
...obrazek z krzywymi i EER


* FTA
* FTE
* FMR/FNMR
* EER
* zeroFMR
* zeroFNMR

Przykładowe pytanie na egzamin

Czy DNA byłoby dobrym identyfikatorem biometrycznym w zastosowaniu na bardzo dużą skalę, np. do identyfikacji podróżnych na lotniskach? Uzasadnij odpowiedź.

Nie bo jest niewygodne dla użytkowników, istnieją bliźnięta jednojajowe, jest kosztowne i czasochłonne


Terminy

czw 8-11
wt 8-11
wt 14-16

zajęte 12-14