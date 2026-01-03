# Kwestie społeczne

* Metody sztucznej inteligencji są coraz szerzej stosowane
* Im szersze grono odbiorców, tym więcej potencjalnych problemów i zagrożeń
* Z perspektywy fairness za *bezpieczne* można uznać atrybuty dla których możemy uzasadnić istnienie związku przyczynowo-skutkowego z modelowanym zjawiskiem

## Źródła obciążenia
* Historyczne - to jak wyglądał / wygląda świat jest odzwierciedlone w danych
* Niedostateczna reprezentacja niektórych grup społecznych w danych
* Dobór atrybutów stosowanych podczas modelowania
	* łatwe do zdobycia sygnały często mogą korelować z modelowanym zjawiskiem ale nie mieć relacji przyczynowo-skutkowej
* Stosowanie niereprezentatywnych benchmarków do oceny modeli
* Spojrzenie jedynie na zagregowane statystyki podczas oceny modelu
	* paradoks Simpsona

## Definicja fairness
* Bardzo wiele różnych
* Dają się przybliżać przez 3 pojęcia dot. klasyfikatorów binarnych
* Oznaczenia
	* $R$ - odpowiedź klasyfikatora
	* $Y$ - prawdziwa etykieta
	* $A$ - wrażliwy / chroniony atrybut
* Niezależność
	* odpowiedź modelu nie zależy od wrażliwego atrybutu
	* $P(R=1|A=a)=P(R=1|A=b)$
	* taka sama odpowiedź modelu we wszystkich chronionych podgrupach
* Separacja
	* jeżeli dwie osoby mają tą samą prawdziwą etykietę, to wrażliwy atrybut nie wpływa na predykcję
	* $P(R=1|Y=1,A=a) = P(R=1|Y=1,A=b)$
	* $P(R=1|Y=0,A=a) = P(R=1|Y=0,A=b)$
	* dopuszczalna jest korelacja między A oraz R, którą uzasadniają różnice w zmiennej celu
	* dla wszystkich grup jest ten sam poziom fałszywych pozytywów FP i FN
* Wystarczalność
	* osoby o różnych wartościach chronionego atrybutu, a takiej samej odpowiedzi mają takie same prawdopodobieństwo wystąpienia etykiety $Y=1$
	* $P(Y=1|R=r,A=a)=P(Y=1|R=r,A=b)$
	* można interpretować jako kalibrację modelu wewnątrz grup
* Kalibracja
	* np. przez dołożenie elementu na końcu sieci
	* raczej postprocessing - zwłaszcza przy uczeniu transferowym
	* skalowanie Platta

## Kluczowe założenia fairness
* Istnieją atrybuty szczególnie wrażliwe społecznie, które mogą być w pewnym sensie chronione
	* np. płeć, kolor skóry, orientacja seksualna, niepełnosprawność
* Dostępne do trenowania modeli czy analiz dane zawierają
	* większą reprezentację niektórych podgrup wydzielonych przez atrybuty chronione - może zaburzać występujące korelacje
	* informacje zbierane historycznie, w dłuższych okresach - proces generujący dane mógł ulec zmianom

## Konsekwencje
* Wszystkie zbiory danych będą mniej lub bardziej obciążone
	* zawsze występują różnice między grupami
* Nie wystarczy pominąć atrybutów wrażliwych w danych do modelowania
	* występują atrybuty skorelowane
	* problematyczne są wszystkie atrybuty korelujące, ale nie mające relacji przyczynowo-skutkowej
* Korygowanie tego zjawiska musi się odbywać aktywnie
	* na etapie tworzenia modelu

## Narzędzia, przykłady

### Fairlearn
* Szkody alokacyjne - nierówne dystrybuowanie szans
	* np. na zatrudnienie, udzielenie kredytu
* Gorsza jakość usług
	* różnice w skuteczności systemu między grupami
	* np. rozpoznawanie twarzy, mowy
* Pakiet dostarcza dwa typy narzędzi
	* miary do oceny, które grupy są negatywnie dotknięte przez model
	* algorytmy wprowadzające korektę do istniejącego modelu
* Metoda
	* w jaki sposób mogą być poszkodowane grupy wrażliwe
	* jakie mamy grupy wrażliwe - cechy demograficzne i analiza ich kombinacji
	* identyfikacja miar jakości i ich analiza w podgrupach
	* porównanie wyników między grupami i ewentualnie zastosowanie algorytmów poprawiających

### AI Fairness 360
* Projekt Linux Foundation
* Grupy metod korekty
	* pre-processing na poziomie danych trenujących (np. ważenie)
	* in-processing - analogiczne techniki jak do generowania danych złośliwych
	* post-processing - dołożenie czegoś do wytrenowanego modelu

### Adversarial debiasing
* Zapewnienie niezależności predykcji $\hat{y}$ od zmiennej chronionej $z$
	* nie wystarczy usunąć atrybutu bo mogą być atrybuty skorelowane
* Intuicja
	* jeśli na podstawie wartości $\hat{y}$ nie da się przewidzieć wartości $z$ to zmienne muszą być niezależne
* Modyfikacja funkcji straty
	* mamy dwa modele - ten właściwy i drugi model zgadujący $z$
	* ten pierwszy ma się stawać coraz lepszy
	* ten drugi ma się stawać coraz gorszy
	* podobnie do treningu GAN
* Atrybutu $z$ może w ogóle nie być w $x$
	* chcemy się upewnić że nie przecieka do żadnych innych atrybutów

## Otwarte pytania dotyczące fairness
* Arbitralne, zależą od przypadku użycia modelu
* Jakie atrybuty powinny być chronione
* Które miary / kryteria stosować

## Ograniczenia prawne

### AI-Act
* Przewiduje bardzo wysokie kary za naruszenia
* Ryzyko niedopuszczalne
	* zakazane ze względu na sprzeczność z prawami człowieka
* Ryzyko wysokie
	* muszą spełniać rygorystyczne wymogi
	* np. diagnostyka medyczna, narzędzia rekrutacyjne
* Ryzyko ograniczone
	* systemy wymagające transparentności
	* np. chatboty, automatyczne podpowiedzi
* Ryzyko minimalne
	* bez dodatkowych regulacji, obowiązują ogólne zasady etyczne
	* np. filtry antyspamowe
* Modele ogólnego przeznaczenia (GPAI)
	* np. LLM
	* podlegają dodatkowym wymogom
	* szczególnie gdy stają się komponentami systemów wysokiego ryzyka

## Bańki filtrujące z perspektywy UM
* Brak eksploracji
	* model serwuje nam tylko najbardziej trafione dane
* Pętla sprzężenia zwrotnego przy zbieraniu danych
* Użytkownicy widzą coraz mniejszy wycinek świata
