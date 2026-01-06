# Lokalizacja źródła dźwięku

## Lokalizacja dźwięków
* Istotne dla dźwięku w wirtualnej rzeczywistości
* Chcemy przez słuchawki dać wrażenie przestrzenne
* Zdolność oceny odległości od źródła dźwięku i kierunku z jakiego dociera

### Lokalizacja w płaszczyźnie poziomej
* Fala dochodząca z prawej wcześniej dochodzi do prawego ucha
* Przed dojściem do lewego ucha mija czas i fala się ugina
* ITD - interaural time difference
	* ścieżki na lewy/prawy kanał są względem siebie przesunięte
	* dominuje dla niskich częstotliwości
* Dla wysokich częstotliwości nie ma ugięcia
	* głowa tworzy cień akustyczny
	* jedno ucho odbiera niższy poziom (amplitudę)
* ILD - Interaural Level Difference
	* dominuje dla wysokich częstotliwości

### Lokalizacja w płaszczyźnie pionowej
* Człowiek określa położenie góra/dół na podstawie częstotliwościowych cech dźwięku związanych z odbiciami od małżowiny usznej
	* dźwięki z różnych kierunków odbijają się inaczej
	* rozdzielczość jest gorsza niż dla płaszczyzny poziomej
* Problematyczne do syntezy
	* różnice w widmie są bardzo subtelne
	* słuchawki zawsze mają swoje błędy

### Czynniki lokalizacyjne
* ITD
* ILD (IID)
* Efekt precedensu
	* różnice czasowe dominują
	* mózg zwróci większą uwagę na różnicę w czasie nawet jeśli poziomy się nie zgadzają
* Efekt cocktail-party
	* przy niesprzyjającym stosunku sygnału do szumu (rozmowa na imprezie)
	* zdolność do oddzielenia istotnej informacji od szumu
	* tym lepsze jeśli znamy barwę istotnego sygnału
* MAA (minimum audible angle) / MAMA
* Lokalizacja odległości
	* człowiek jest słaby w bezwzględnym wskazywaniu odległości
	* człowiek jest dobry w porównywaniu względnym (co bliżej, co dalej)
	* powietrze szybciej tłumi wysokie częstotliwości
	* przy sztucznym dźwięku trzeba odpowiednio obcinać wysokie częstotliwości (poza zmniejszaniem poziomu)
* Rola ruchów głową
	* istotne przy testach śledzenia czy osoba może ruszać głową
* HRTF - head related transfer function
* Doświadczenie słuchowe i wiązanie zjawisk akustycznych z obserwacjami wzrokowymi
	* człowiek bardziej zwraca uwagę na obraz (czy widzi skąd dobiega dźwięk)

Człowiek naturalnie skleja "strumienie danych" z lewego i prawego ucha w pojedyncze zdarzenia na poziomie milisekund.


## Dźwięk przestrzenny
* Mono
	* już praktycznie nigdzie nieużywany
* Stereo
	* standard mimo rozwoju dźwięku przestrzennego
	* 2 źródła
	* określony przedni kierunek
* 5.1
	* transmisja musi być zakodowana w 5.1
	* wyróżniony kierunek przedni
	* 3 przednie i 2 tylne
	* tylne głośniki niczego nie odtwarzają jeśli transmisja nie jest zakodowana w 5.1
	* trzeba dostarczyć oddzielny mix do stereo i 5.1
* Ambisonia
	* rejestracja dźwięku w wielu płaszczyznach
	* nie rejestruje się dźwięku dla określonego ustawienia głośnika
	* rejestruje się dźwięk dla sfery wokół punktu i dekoduje dla określonego zestawu głośników
	* bez wyróżnionego kierunku przedniego
* Auralizacja
	* "wizualizacja" dla dźwięku
	* sztuczne tworzenie wrażeń akustycznych
	* dźwięk w zwirtualizowanej przestrzeni

### Lateralizacja
* Przy odsłuchu słuchawkowym stereo
* Wrażenie jest, że źródła są w środku głowy
* Nie ma wrażenia dźwięku poza głową
* Można łatwo uzyskać przez wprowadzenie przesunięcia czasowego (ITD i ILD)

### Eksternalizacja
* Wrażenie dźwięku przestrzennego, źródło poza głową
* Mamy słuchawki na uszach
* Jest wrażenie, że dźwięk dobiega z zewnątrz
* Korzystając ze słuchawek małżowina nie pracuje
* Nagrania binauralne - manekin ze sztucznymi małżowinami i 2 mikrofonami w środku
* Kształt małżowiny jest indywidualne więc nagrania nie działają idealnie

### Head related transfer function
* Funkcja przenoszenia głowy
* Określa wpływ głowy i ciała na dźwięk o danej częstotliwości docierające do ucha z poszczególnych kierunków
* Dla każdego kąta bada się zależność poziomu od częstotliwości
* Wymaga komory bezechowej do wyznaczenia
* Popularny temat badań
	* gracz dla dobrego doświadczenia VR powinien mieć spersonalizowaną funkcję żeby wyeliminować błędy z lokalizacją
	* problem z wyznaczeniem bez komory bezechowej
	* można dobrać funkcję dla najbardziej zbliżonego ucha z bazy na podstawie zdjęcia ucha (hrtf fitting)

## Beamforming
* Kształtowanie wiązki
* Wykorzystanie matrycy mikrofonowej
* Przetwarzanie sygnałów z poszczególnych mikrofonów
* Kształtowanie charakterystyki kierunkowej matrycy
* Możliwość uzyskania silnie kierunkowej charakterystyki
* Zastosowania
	* usuwanie wpływów zakłóceń na sygnał użyteczny
	* filtracja adaptacyjna w celu usunięcia niepożądanych sygnałów
	* neurobeamforming - wykorzystanie sieci neuronowych i uczenia maszynowego do znalezienia wag
