# Tokenizacja

## Reprezentacja tekstu w języku naturalnym
* Tekst jest dzielony na tokeny
* Tokeny na ich numery w słowniku
* Numery w słowniku na reprezentację wektorową (embedding)
	* reprezentacja jest gęsta
	* to jest element modelu językowego
	* inicjowany losowo, trenowany

## Tokenizacja
* Podzielenie tekstu na mniejsze jednostki - tokeny
* Słownik tokenów jest tworzony przez analizę korpusu tekstowego
* Słownik tworzy się niezależnie od treningu modelu językowego

### Podejście klasyczne
* Tokenizacja na poziomie słów
* Wstępna normalizacja - usunięcie znaków przestankowych itp.
* Stemming - sprowadzanie wyrazów do ich podstawowej formy przez usuwanie końcówek fleksyjnych
* Rzadkie lub błędnie zapisane słowa kodowane przez specjalny token `<UNK>`

### Tokenizacja na poziomie części słów
* Tokeny reprezentują
	* często występujące słowa
	* często występujące morfemy / części słów
	* pojedyncze symbole z alfabetu lub bajty składające się na symbol w UTF-8
* Redukuje problem słów błędnie zapisanych lub słów spoza słownika
* Byte Pair Encoding (BPE)
	* tak naprawdę działa na znakach, a nie bajtach
	* dzieli wejściowy tekst na najmniejsze jednostki (znaki)
	* iteracyjnie łączy pary sąsiednich symboli korzystając z ustalonych reguł
* Byte-level BPE
	* najpopularniejsze podejście
	* dowolne znaki unicode
	* koduje tekst w formacie UTF-8 i traktuje jako strumień bajtów
	* GPT, LLaMA, Claude...
	* słowo i to samo słowo z doklejoną spacją do mogą być 2 różne tokeny
	* tokenizacja liczb - nie ma narzuconego żadnego porządku
* Unigram Language Model
	* probabilistyczny model tworzenia słownika
	* lepszy dla języków o złożonej morfologii
	* bardziej złożony obliczeniowo
	* mniej popularny
* W GPT4 token odpowiada średnio 3/4 słowa

### Tokeny specjalne
* Oprócz tokenów reprezentujących słowa / części słów, do słownika dodaje się specjalne tokeny
	* zależnie od modelu
* Przykładowo
	* `<|unkn|>` - nieznane słowo (tokenizoatory oparte na całych słowach)
	* `<|endoftext|>` - koniec tekstu
	* `[BOS]` - początek sekwencji
	* `[EOS]` - koniec sekwencji
	* `[PAD]` - padding (dopełnienie wsadu do określonej długości)
	* `[CLS]` - klasyfikacja (dla modeli z dwukierunkową atencją)
	* `[MASK]` - zamaskowany token (dla modeli z dwukierunkową atencją)
	* tokeny wywołania zewnętrznych narzędzi - integracje systemu dialogowego

## Uczenie tokenizatora
* Zaczynamy od małego słownika
	* pojedyncze znaki lub bajty w kodowaniu Unicode
* Iteracyjne wyznaczanie reguł łączenia

### Algorytm uczenia DPE
* Przygotowanie korpusu tekstowego
* Normalizacja i pre-tokenizacja tekstu
	* zależnie od zastasowania
	* np. usuwanie nadmiarowych spacji
* Zaczynamy ze słownikiem ze wszystkimi znakami albo bajtami UTF-8
* Wybierz najczęśniej występujące obok siebie tokeny
* Połącz w nowy token i dodaj do słownika
	* połączone tokeny też zostają w słowniku
* Zastąp wszystkie wystąpienia nowym tokenem
* Powtarzamy do osiągnięcia założonego rozmiaru słownika
* Wynikiem treningu są
	* słownik - zbiór wyznaczonych tokenów
	* reguły łączenia tokenów - zapisane w kolejności (tokenizacja jest jednoznaczna)

### Algorytm tokenizacji
* Normalizacja i pre-tokenizacja tekstu
* Podziel tekst na najmniejsze jednostki
	* znaki lub bajty unicode
* Stosuj kolejno reguły łączenia tokenów
	* jeśli można zastosować regułę to zastosuj i wróć na początek
	* jeśli nie można zastosować żadnej reguły - zakończ
* Można wykonać w czasie $n \log n$
	* jak?

## Słownik osadzeń
* Embedding layer
* Część modelu językowego
* Lookup table
	* wagi inicjowane losowo
	* optymalizowane podczas treningu

# Transformator cech głębokich z atencją (Transformer)


## Typy architektur Transformer
Będzie z tego pytanie na kolokwium

### Tylko koder
* Inne maskowanie atencji niż w tylko-dekoder
* BERT, RoBERTa
* Rzadziej stosowane ale nadal użyteczne
* Wyznaczanie kontekstowych reprezentacji sekwencji
	* np. na potrzeby RAG
	* klasyfikacja tekstu
	* analiza sentymentu
	* klasyfikacja tematu
	* detekcja spamu

### Tylko dekoder
* Architektura wielkich modeli językowych
* GPT i podobne

### Koder-dekoder
* W oryginalnym artykule Attention is all you need
* Obecnie rzadko wykorzystywana
* Zaproponowana do zadania tłumaczenia maszynowego
* Obecnie stosowana w przekształceniach multimodalnych
	* np. audio na tekst

## Architektura tylko-dekoder
* Warstwa osadzeń (słownik)
	* macierz (rozmiar słownika, rozmiar zanurzenia)
* Kodowanie pozycyjne
	* dalsza część modelu nie bierze pod uwagę kolejności tokenów w sekwencji
	* kolejność słów w zdaniu jest istotna
* Bloki dekodera
	* kontekstowe reprezentacje tokenów na wyjściu z bloków dekodera
	* wielogłowicowa atencja
	* warstwa w pełni połączona
	* połączenia rezydualne - współcześnie inaczej niż na rysunku
* Warstwa liniowa i softmax
	* zwraca rozkład prawdopodobieństwa
	* w trybie inferencji tylko dla ostatniego zanurzenia w sekwencji
	* w trybie treningu liczymy stratę dla każdego zanurzenia w sekwencji

## Blok kodera i dekodera
* W koderze i dekoderze różni się tylko maską atencji
	* w dekoderze brane są tylko tokeny występujące wcześniej w sekwencji
	* w koderze brana jest cała sekwencja
* Przekształca wejściową sekwencję wektorów cech w wyjściową sekwencję wektorów cech o tej samej długości biorąc pod uwagę kontekst

## Atencja QKV
* Mechanizm atencji tworzy kontekstową reprezentację wektorów w sekwencji wejściowej poprzez skupienie uwagi i uwzględnienie informacji z innych elementów
* Wektor zapytania
* Wektor klucza
* Wektor wartości
* Wagi optymalizowane w procesie uczenia
* Wektory tworzone przez pomnożenie wektora zanurzenia przez macierz wag
* Współczynniki atencji wyznaczane jako iloczyn skalarny wektorów klucza i zapytania (znormalizowany)
	* tworzy się macierz współczynników atencji dla wszystkich par klucz-wartość
	* wektory i iloczyn nie są znormalizowane! - zakres wartości $(-\infty, +\infty)$
* Maska atencji przyczynowej - współczynniki atencji odpowiadające wpływowi późniejszego tokenu na wcześniejszy są maskowane
	* powyżej diagonali zamienia się wszystkie elementy na $-\infty$
* Softmax po wierszach macierzy współczynników atencji
	* $-\infty$ z maski odpowiada prawdopodobieństwu $0$
	* wiersz macierzy zamienia się na rozkład prawdopodobieństwa - sumuje się do 1
* Macierz wektorów wartości
	* i-ty wektor wyjściowy to suma ważona wektorów wartości, ważona współczynnikami atencji
* Całość wyraża się wzorem $H = softmax(\frac{QK^T}{\sqrt{d}} + M)V$
	* $M$ - maska atencji przyczynowej
	* $Q, K, V$ - wiersze to wektory zapytań/kluczy/wartości