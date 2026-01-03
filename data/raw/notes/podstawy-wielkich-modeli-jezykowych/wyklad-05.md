# Fazy trenowania modeli językowych c.d. (2025-11-07)

* Na etapie SFT model uczy się sensownego odpowiadania na pytania użytkownika

## Wychowywanie modelu
* Dostosowanie modelu do ludzkich preferencji, wartości zasad etycznych
* Zbiory treningowe zawierają prompt użytkownika i odpowiedzi uszeregowane według preferencji
	* też negatywne przykłady
	* zwykle mniej przykładów niż w fazie nadzorowanego dostrajania


## Uczenie ze wzmocnieniem
* Rzadka nagroda
	* np. co kilka iteracji
* Agentem jest model językowy
	* nagroda po wygenerowaniu całej sekwencji

## RLHF
* Bardzo wrażliwe na ustawienia hiperparametrów
	* trening może nie być zbieżny
* Są gotowe implementacje
* Nie omawiamy szczegółowo
* Typowe podejście
	* nadzorowane dostrajanie modelu do wykonywania poleceń
	* wytrenowanie modelu oceniającego odpowiedzi językowego
		* zbiór treningowy to instrukcje razem z kilkoma odpowiedziami
	* zastosowanie uczenia ze wzmocnieniem do optymalizacji wag modelu językowego
		* model nagrody ocenia wygenerowane sekwencje
		* optymalizacja wag w celu maksymalizacji nagrody
* Kłopotliwe trenowanie modelu nagrody

## DPO
* Direct Preference Optimization
* Dwie kopie modelu - trenowana i referencyjna
* Model trenowany powinien zwracać
	* większe prawdopodobieństwo dla preferowanych odpowiedzi
	* mniejsze prawdopodobieństwa dla odrzuconych odpowiedzi niż model referencyjny
* Przewaga nad RLHF
	* bardziej stabilne
	* nie wymaga trenowania modelu nagrody

## ORPO
* Technika łącząca nadzorowane dostrajanie do wykonywania poleceń (SFT) i dostosowanie do preferencji
* Zbiór danych zawiera
	* pytanie
	* akceptowaną odpowiedź
	* odrzuconą odpowiedź
* Funkcja straty jest sumą składnika odpowiadającego SFT (entropia krzyżowa) i dostosowaniu preferencji - stosunek prawdopodobieństw akceptowanego vs odrzuconego

# Efektywne obliczeniowo dostrajanie modeli (PEFT)
* Dostrajanie LLM w naiwny sposób
	* pamięć GPU potrzebna do dostrajania modelu jest wielokrotnie większa niż pamięć potrzebna na przechowanie wag modelu (12-20x więcej niż wagi)
	* poza wagami trzeba przechowywać stan optymalizatora, gradienty, aktywacje

## Reprezentacje liczb zmiennoprzecinkowych
* Żeby model zajmował mniej pamięci można zmienić reprezentację
	* niższa precyzja
* float16 ma dużo mniejszy zakres niż float 32
	* 5 bitów wykładnika vs 8 bitów wykładnika
* `bfloat16` - Brain Float 16
	* 8 bitów wykładnika
	* 7 bitów mantysy
	* zakres wartości (wykładnik) taki sam jak dla float 32 przy mniejszej precyzji
* blfloat16 wymaga sprzętowego wsparcia przez GPU
	* nie jest wspierany przez T4 dostępne na collabie
	* RTX 30XX wspierają
* Tensor float 32
	* 8 bitów wykładnika - tyle co float 32
	* 10 bitów mantysy - tyle co float 16
	* zajmuje tyle pamięci co float 32
	* wykorzystywany niejawnie w wybranych architekturach GPU (Ampere A100)
	* GPU wykonuje mnożenie macierzy przy zmniejszonej precyzji
	* potem reprezentacja w standardowych f32
	* pozwala na nawet dwukrotne przyspieszenie obliczeń

## PEFT
* Rodzina metod pozwalająca na efektywne dostrajanie relatywnie dużych modeli
	* 2-4B parametrów można trenować na średniej klasy GPU
* Typowe podejścia
	* optymalizacja tylko niektórych parametrów, a pozostałe zostają zamrożone
	* dodatkowe warstwy optymalizowane podczas uczenia, a wszystkie wagi modelu bazowego zamrożone
## Klasy metod PEFT
* Najważniejsze - LoRA i warianty
* Metody klasy soft prompt
	* model zostaje zamrożony
	* wirtualny prompt w przestrzeni embeddingów, dołączany do promptu użytkownika
	* zwykle 20-100 elementów
	* optymalizujemy wirtualny prompt w procesie uczenia
	* działa tym lepiej im bardziej złożony jest sam model
	* może być losowo zainicjowany
	* zoptymalizowany prompt po zdekodowaniu (najbliżsi sąsiedzi w słowniku) raczej będzie bełkotem
* Hard prompting
	* prompt w języku naturalnym
	* jak ręczny prompt engineering
* In-context learning, one-shot / few-shot learning
	* podajemy w prompcie kilka przykładów oczekiwanej odpowiedzi modelu
* Dynamicznie rozwijająca się dziedzina

## LoRA
* Zamrożanie wag oryginalnego
* Dostrajanie wag innych, mniejszych macierzy
* Zamiast jednej dużej macierzy, np. 512x64, dwie mniejsze macierze np. 8xx64 i 512x8
	* po wymnożeniu będzie taki sam wymiar
	* ale do optymalizacji jest znacznie mniej parametrów (4k vs 32k)
* Na koniec treningu scala się iloczyn dwóch mniejszych macierzy z oryginalną i używa bez narzutu

## Optymalizacja treningu na jednym GPU
* Kwantyzacja modelu z fp32 do fp15, bfloat16 lub int8
* Wybór odpowiedniego optymlalizatora
	* standardowy AdamW zużywa 8 bajtów na parametr
	* AdaFactor - 4 bajty na parametr
	* 8-bitowy AdamW (adamw_bnb_8bit) - 2 bajty na parametr