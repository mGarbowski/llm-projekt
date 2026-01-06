# Bezpieczeństwo systemu biometrycznego (2025-11-17)

## Budowa systemu biometrycznego
* Podsystem pomiarowy
	* sensor
	* sensor mierzy obiekt
* Podsystem przetwarzania sygnałów
	* sfera algorytmiczna
	* segmentacja
	* wyznaczanie cech
	* kontrola autentyczności
* Podsystem przechowywania danych
* Podsystem dopasowania danych
* Podejmowanie decyzji
* Podsystem administracyjny
	* ustalanie progów akceptacji próbek i kryteriów
	* inne rzeczy wynikające z tego że to system informatyczny, niekoniecznie związane z biometrią
	* kontrolowanie środowisko
	* logowanie, monitorowanie
	* zapewnienie prywatności
* Interfejs
	* programistyczny i sprzętowy
	* umożliwia komunikację między systemami

### Przepływ danych
* Rejestracja
	* pomiar obiektu sensorem
	* przetworzenie próbki biometrycznej - utworzenie wzorca
	* zapis wzorca na nośniku lub w bazie danych
* Uwierzytelnienie
	* deklaracja tożsamości
	* wyszukanie wzorca w bazie
	* równolegle pomiar i wyznaczenie wzorca
	* dopasowanie utworzonego wzorca ze wzorcem z bazy
	* wyznaczenie współczynnika podobieństwa
	* podejmowanie decyzji
* Identyfikacja
	* pomiar i wyznaczenie wzorca
	* porównanie z każdym wzorcem z bazy
	* znalezienie najbliższego dopasowania
	* podjęcie decyzji

## Podatności
* Wszystkie elementy są punktami wrażliwymi

## Bezpieczeństwo sensora
### Testowanie żywotności
* Przetwarzane dane muszą być wynikiem pomiaru cech żywej osoby
* Muszą być dostarczane właściwe próbki biometryczne
* Badanie żywotności jest niezbędne aby system można było nazwać symetrycznym

### Ochrona urządzeń i danych
* Obudowy odporne na ingerencję
	* nie da się otworzyć śrubokrętem
* Kasowanie i zamazywanie pamięci w przypadku ingerencji
* Uwierzytelnienie i certyfikacja urządzeń
	* nawzajem przez komunikujące się urządzenia
	* poddanie testom przez akredytowaną instytucję
* Szyfrowanie i podpisywanie danych do dalszych komponentów systemu

## Bezpieczeństwo transferu danych
* Podsłuchiwanie transmisji
	* dane biometryczne - próbki, dane wstępnie przetworzone, wzorce
	* parametry kodowania
	* wyniki testów żywotności
	* parametry jakościowe
	* wyniki dopasowania
	* decyzje
* Ingerencja w transmisję
	* modyfikacja danych
	* wstrzykiwanie danych

## Przykład ataku - hill climbing
* Atakujący zyskuje dostęp do kanału transmisji, może wstrzykiwać syntetyczne dane biometryczne
* Próbuje dopasować sztuczny zbiór minucji do wzorca
* Atakujący generuje losowy zbiór minucji
	* porównuje ze wzorcem
	* generuje kolejny, zmieniony zbiór minucji
	* optymalizacja współczynnika dopasowania
* Wiele iteracji
* Obrona przed atakiem
	* spowolnienie, ograniczenie liczby zapytań do systemu
	* nie udostępniać współczynnika dopasowania, tylko decyzję
	* załatać dziurę, która umożliwiła dostęp do kanału komunikacji

## Syntetyczne dane biometryczne
* Generowanie danych na podstawie których można uzyskać wymagane podobieństwo wzorca biometrycznego wyznaczonego dla tych danych z wzorcem referencyjnym
* Biometria odwrotna
	* odtworzenie surowych danych na podstawie wzorców
	* zabezpieczenie - stosowanie operacji jednokierunkowych przy wyznaczaniu wzorców

## Problem biometrii odwrotnej na przykładzie biometrii tęczówki
* Jednoznaczne przekształcenie z przestrzeni zdjęć tęczówki do przestrzeni kodów
* Niemożliwość jednoznacznego odwzorowania w drugą stronę

## Możliwości zabezpieczeń
* Kryptografia
* Steganografia
	* osadzanie tajnej informacji niezaburzającej informacji biometrycznej
	* stosowana do uwierzytelniania urządzeń i wzorców
	* np. odłożenie tajnego klucza na najmniej znaczących bitach
* Bio-kryptografia
	* tworzenie klucza kryptograficznego na podstawie danych biometrycznych
	* klucz potem używany np. do kontroli dostępu
* Wykorzystanie właściwości biometrii
	* naturalna zmienność wzorców biometrycznych - realistycznie nie będzie dwóch identycznych pomiarów
	* można wprowadzić górny próg podobieństwa
	* parametryzacja i interaktywność metod porównywania - biometria wielokrotna
	* zaszumienie / kwantyzacja wyników porównań - przeciwdziałanie atakom hill climbing, brute force
	* jednokierunkowość przekształceń

### Przykład jednokierunkowych przekształceń
* W biometrii tęczówki
* Segmentacja obrazu tęczówki
	* podział na nierówne prostokąty
* Permutacja segmentów - przemieszanie

## Bezpieczeństwo nośników i przechowywania danych

### Karta mikroprocesorowa
* Np. dowód osobisty
* Urządzenie wyposażone w procesor, pamięć, często koprocesor kryptograficzny
* Zasilanie indykcyjne
	* przytknięcie do sensora z pętlą indukcyjną
* Wysokie bezpieczeństwo, ograniczone zasoby

### Technologia match-off-card
* Wzorzec jest przechowywany na karcie mikroprocesorowej
* Nie ma centralnej bazy
* Np. kontrola paszportu
* Nie można wykraść danych z centralnej bazy bo nie istnieje centralna baza
* Trzymanie danych po stronie użytkownika wymusza interoperacyjność
	* wzorce ustandaryzowane przez ISO

### Technologia match-on-card
* Podejmowanie decyzji wykonywane po stronie karty inteligentnej
* Przetwarzanie sygnałów nie może być robione na karcie, bo to za dużo obliczeń dla tak małych zasobów
* Rzadki schemat

### Technologia measure-and-match-on-token
* W jednym urządzeniu wszystkie elementy przetwarzania
* Np. biometria w telefonie
* Tokeny biometryczne

## Podsumowanie
* Dwa aspekty w kontekście biometrii
	* ....

## Przykładowe pytania egzaminacyjne
* Które z poniższych technik zapobiegają akceptacji nielegalnie pozyskanego wzorca przesłanego ponownie w niezmienionej formie w celu uwierzytelnienia
	* zaszumianie wzorców przed transmisją - nie, to samo zostanie zaszumione i porównywane
	* permutacja elementów wzorca na etapie wyznaczanie - nie, to samo będzie permutowane
	* ustalenie progu maksymalnej dozwolonej zgodności - tak, będzie identyczny wynik dla tego samego wejścia
	* brak możliwości odtworzenia oryginalnej próbki na podstawie wzorca - nie rozwiąże tego problemu
	* kwantyzacja wyniku dopasowania wzorców do trzech wartości (tak, nie, niepewne) - tutaj nie pomoże
* Analogiczne pytanie o hill climbing

Dystans Hamminga - zapamiętać na egzamin

# Biometrie dłoni
* Modalności związane z dłonią
* Odciski
	* placów
	* dłoni
* Geometria
	* dłoni 2D/3D
	* palców (2D/3D)
* Tekstura kostek dłoni
* Układ żył
	* wewnętrznej części dłoni
	* zewnętrznej części dłoni
	* nadgarstka

## Odcisk dłoni
* Linie główne dłoni
	* kierunki
	* rozwidlenia
	* zakończenia
	* przecięcie
* Tekstura dłoni
	* cechy wycinka obrazu dłoni
* Linie papilarne
	* tożsame z biometrią odcisku palca

## Geometria dłoni
* Cechy 2D
	* szerokość palców i dłoni
	* długości palców
* Cechy 3D, 2.5D
	* rozszerzenie cech 2D o wysokości
* Pozyskiwanie obrazu
	* kołki pozycjonujące
	* dłoń ułożona na powierzchni refleksyjnej
	* lustra po bokach
	* prosty do obróbki obraz, mała zmienność
* Klasyfikacja liniowa
	* błędy na poziomie EER<1% dla starych metod
* Już nie jest rozwijana

## Układ żył dłoni i palców
* Amazon One - czytnik
* Krzywe absorpcji światła przez różne składniki krwi
	* krew pochłania część światła podczerwonego
* Realizacja techniczna
	* oświetlanie z góry
	* oświetlanie z dołu
	* prześwietlanie
* Analogiczne kroki przetwarzania do odcisków palca
	* obraz szkieletowy na końcu

## Układ żył palca
* Tak samo jak dla układu żył dłoni
* Współczynnik niedopasowania
* Klasy elementów obrazy - żyła, tło, niepewny

## Termika dłoni
* Temperatura powierzchni skóry
	* matryca czujników temperatury
	* kamera termowizyjna
* Słabe do rozpoznawania ludzi ale całkiem dobry test żywotności


# Egzotyczne biometrie
## Biometria siatkówki
* Ta część przyczepiona do nerwu wzrokowego
* Właściwie to biometria naczyniówki - ukrwiona część pod siatkówką
	* jest ukrwiona - sieć naczyń krwionośnych
* Układy pomiarowe są skomplikowane technicznie i wymagają ścisłej współpracy mierzonej osoby
* Historycznie starsze niż biometria tęczówki

### Pozyskiwanie obrazu
* Obserwajca układu naczyń w naczyniówce
* Bardzo mała moc światła (7mW)
* Pomiar aktywny w podczerwieni
* Odległość oka od obiektywu ok. 2 cm
* Obrazy niskiej rozdzielczości
* Wymaga współpracy użytkownika
	* bardziej jak badanie u okulisty niż FaceID

### Porównywanie danych
* Filtracja nisko-częstotliwościowa
	* np. falki Gabora
* Uwydatnianie kontrastu
* Normalizacja
* Porównywanie korelacyjne
	* z korekcją obrotu oka

## Biometria ucha
* Ślady ucha są często znajdowane na miejscach przestępstw
* Eksperymentalnie potwierdzone, że odcisk ucha umożliwia identyfikację
	* u bliźniąt jednojajowych są podobne ale nie identyczne

### System Iannarellego
* Cechy Iannarellego
	* 12 cech
	* dyskretyzacja pomiaru do wielokrotności 3mm

## Zapach
* Do testów żywotności
* Słabe do samej biometrii
* Działanie narządu węchu - bardzo skomplikowane do zamodelowania
	* jest 100mln receptorów, 1000 typów
	* receptory tworzą sygnały elektryczne
	* przetwarzanie wstępne w korze mózgowej

### Elektroniczny nos
* Bardziej do kontroli na lotniskach niż do biometrii
* Zbiór czujników chemicznych
* Sygnał elektryczny do przetwornika
* Informacja przepuszczona przez neuronowy klasyfikator

### Typy czujników
* Rezystancyjne
* Piezoelektryczne
* Spektrometryczne
* MOSFET
* Optyczne

## Do zapamiętania
* Jakie własności dłoni nas wyróżniają
	* wymienić i opisać modalności
* Czym różni się biometria tęczówki od siatkówki
	* przynajmniej nie mylić