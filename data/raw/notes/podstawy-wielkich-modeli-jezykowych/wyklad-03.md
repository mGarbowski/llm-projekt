# Transformer c.d.

## Atencja wielogłowicowa
* Równoległe, niezależne bloki
* Ogranicza się wymiar wyjść z pojedynczej głowicy do $d/h$
	* $d$ - rozmiar embeddingu
	* $h$ - liczba głowic
* Potem wektory wyjściowe są konkatenowane
	* do wejściowego wymiaru
* Połączone embeddingi są wymnożone przez macierz projekcyjną $W_O$
* W jednogłowicowej atencji
	* $W_K$ ma wymiar $(d,d)$
* Tutaj $W_K^i, W_Q^i, W_V^i$ mają wymiar $(d, d/h)$
* $SA_I(X) = softmax(\frac{Q_iK_i^T}{\sqrt{d}} + M)V_i$
* $MHA(X) = [SA_1(X)|\ldots|SA_h(X)]W_O$
	* konkatenacja i mnożenie macierzy

### Liczba trenowalnych parametrów
* Najczęściej wymiar Q, K i wymiar V są równe
	* $d \cdot d/h$
* Liczba parametrów warstwy atencji wielogłowicowej nie zależy od długości przetwarzanych sekwencji
* Liczba parametrów zwykle nie zależy od liczby głowic
	* macierze QKV są dla każdej głowicy skalowane przez liczbę głowic
* Rozmiar macierzy $W_O$ ...
* W sumie $4d^2$

### Warstwa MH w torch
* Na wejściu oddzielnie podawany X do query, key i value
	* w architekturze tylko dekoder podaje się to samo
	* w innych niekoniecznie

## Elementy składowe bloku transformera
* Atencja wielogłowicowa
* Blok w pełni połączony
	* dwuwarstwowy perceptron
	* GELU
	* pierwsza warstwa ma zwykle większy wymiar wyjścia (np $4d$)
* Połączenie rezydualne i normalizacja warstwy
	* normalizacja po wymiarze embeddingu
	* połączenie rezydualne obok bloku MHA
	* połączenie rezydualne obok bloku FF
* Opcjonalnie dropout

### Liczba trenowalnych parametrów bloku liniowego
* Zwykle więcej wag niż w bloku atencji
* Rozmiar warstwy ukrytej zwykle $H=4d$
* $(d \cdot H + H) + (H \cdot d + d)$
* Dla $d=4096$ jest ponad $130$ mln parametrów

## Warianty architektury
* W oryginalnym artykule o transformerze normalizacja warstwy była po połączeniu rezydualnym
* W najczęściej obecnie stosowanej architekturze normalizacja jest robione bezpośrednio przed warstwami MHA i FF
	* oryginalny $x$ bez normalizacji też przepływa przez strumień połączeń rezydualnych

## Kodowanie pozycyjne
* Wielogłowicowa atencja nie bierze pod uwagę kolejności zanurzeń
* Kolejność trzeba wstrzyknąć do samych zanurzeń
* Bezwzględne kodowanie pozycyjne
	* stosowane raz
	* do zanurzenia każdego tokenu dodawany jest wektor kodujący jego pozycję w sekwencji
	* ten sam token w różnych pozycjach w sekwencji dostanie inny wektor zanurzenia
* Względne kodowanie pozycyjne
	* w każdej warstwie atencji
	* przekształcenie wektorów zapytań i kluczy
	* wynikowe wartości atencji zależne od względnej pozycji elementów w sekwencji
	* obecnie to jest standard

### Bezwzględne kodowanie pozycyjne
* Uczona warstwa słownikowa
	* Ogranicza maksymalny rozmiar okna kontekstu podczas inferencji
* Deterministyczna funkcja, np. sinusowe kodowanie
	* dla $k$-tego elementu w sekwencji
	* $i$-ty element wektora pozycyjnego $sin(k/...)$ albo $cos(...)$
* To samo słowo na różnych pozycjach jest różnie reprezentowane

### Względne kodowanie pozycyjne
* Rotacyjne kodowanie pozycyjne (RoPE)
	* Llama, Mistral, ...
* W każdej warstwie atencji
* Żeby iloczyn skalarny wektora q i k zależał dodatkowo od odległości tokenów w sekwencji wejściowej
* Wyznaczenie q i k
	* $q_m = R_mW_Qx_m$
	* $k_n=R_nW_Kx_n$
* $R_i$ - macierz rotacji zależna od pozycji $i$
	* własność $R_m^TR_n = R_{n-m}$

# ??

## Autoregresyjne generowanie tekstu
* Długi tekst generuje się token po tokenie
* Bierze się reprezentację ostatniego tokenu na wyjściu
* Przepuszcza się przez macierz projekcji i softmax
* Z otrzymanego rozkładu próbkuje się token i dokłada na koniec wejścia
* Znowu przepuszcza się całą sekwencję wejściową przez cały model
* Dla przyspieszenia generacji stosuje się KV cache

### Kompromis między jakością a różnorodnością
* Wybieranie najbardziej prawdopodobnego tokenu będzie generować bardziej spójny i zgodny z faktami tekst ale bardziej powtarzalny
	* często się zapętla i generuje wiele razy to samo zdanie
* Próbkowanie losowe
	* losuj token zgodnie z rozkładem określonym przez model
	* w praktyce często generowane są rzadkie tokeny i tekst nie ma sensu
	* problem długiego ogona - jest bardzo wiele tokenów, wiele ma małe prawdopodobieństwo ale ich suma już jest duża
* Top-k sampling
	* $k$ najbardziej prawdopodobnych słów
	* znormalizowany rozkład dla tych k
	* próbkowanie losowe z tego rozkładu
* Top-p sampling
	* najbardziej prawdopodobne tokeny o łącznej masie prawdopodobieństwa $p$
* Temperature sampling
	* zmienia kształt rozkładu prawdopodobieństwa
	* przy dużej temperaturze rozkład prawdopodobieństwa się spłaszcza
	* przy niskiej temperaturze rozkład się wyostrza

## Fazy trenowania generatywnych modeli językowych
* na kolokwium
* Wstępne trenowanie
	* najbardziej wymagające
	* rzędu milionów godzin GPU
	* modele udostępniane z tagiem BASE
* Nadzorowane dostrajanie do wykonywania poleceń
	* wersja INSTRUCT
* Dostosowanie do preferencji
	* Reinforcement Learning from Human Feedback
	* Direct Preference Optimization
	* Odds Ratio Preference Optimization
* Fazy 2 i 3 - "wychowywanie modelu"
	* zgodność z oczekiwaniami użytkowników
	* minimalizacja ryzyka generowania treści szkodliwych
* Fazy 1 i 2
	* uczenie samonadzorowane
	* predykcja następnego tokenu

## Wstępne trenowanie
* Przepuszczenie sekwencji  przez transformer
* Wyjście dla każdego tokenu (inaczej niż przy inferencji)
* Średnia entropii krzyżowej dla każdego elementu sekwencji
* Cel - dopasowanie dokładnie następnego tokenu