# Szyfry symetryczne i asymetryczne

## Pojęcia
* Kryptografia - nauka i sztuka o projektowaniu szyfrów
* Kryptoanaliza - sztuka i nauka łamania szyfrów
* Kryptologia - kryptografia + kryptoanaliza
* Steganografia - sztuka ukrywania informacji
* Tekst jawny - dane przed zaszyfrowaniem (ciąg bitów, niekoniecznie tekst)
* Szyfrogram - zaszyfrowane dane
* Klucz - modyfikuje działania algorytmu
    * algorytm jest jawny a bezpieczeństwo zapewnia tajny klucz
* Celem szyfrowania jest zapewnienie poufności
* Kodowanie to sposób reprezentacji danych w dobrez zdefiniowany sposób
    * kod ASCII
    * kod Morse'a

## Historia
* Szyfry wykorzystujące przestawienie
    * Scytale
* Szyfry wykorzystujące podstawienie
    * szyfr Cezara
    * ogólnie alfabet jest mapowany na dowolną permutację
    * łamanie przez analizę częstotliwości występowania liter
* Szyfr polialfabetyczny
    * szyfr Vigenere'a
    * kilka alfabetów szyfrowych, kolejne znaki szyfrowane kolejnymi alfabetami
    * ustalona liczba i permutacje alfabetów szyfrujących
    * też daje się złamać przez analizę częstotliwościową ale trudniej
* Szyfr Vernama
    * nie da się go złamać (przy zapewnieniu warunku niepowtarzalności klucza)
    * jednorazowy klucz o jednakowej długości jak wiadomość
    * niepraktyczne
* Maszyny rotorowe
    * Enigma
    * Klawiatura do wprowadzania tekstu jawnego
    * Po wciśnięciu zapala się lampka z zakodowanym znakiem
    * Rotory (bębenki) realizujące sprzętowo permutacje
    * Ustawienie rotorów określa szyfr
    * Po wciśnięciu przycisku bębenki się obracają (1. co 1, 2. co 26, 3. co 26^2)
    * Też jest szyfrem podstawieniowym z 26^3 alfabetów

## Podział szyfrów
* Blokowe i strumieniowe
* Symetryczne i asymetryczne

## Szyfry blokowe i strumieniowe

### Szyfr strumieniowy
* Szyfruje nadchodzący znak (bajt) niezależnie
* XOR klucza z wiadomością do zaszyfrowania
	* funkcja generująca ciąg pseudolosowy na podstawie klucza
* Deszyfrowanie to XOR klucza z szyfrogramem
* RC4 stosowane w starych standardach WiFi
* Wymaga dobrego algorytmu pseudolosowego generowania klucza

### Szyfr blokowy
* Szyfruje za jednym razem większą porcję danych niż znak
* Bloki o wielkości rzędu 64, 128 bitów
* Obrona przed atakami częstotliwościowymi
* Wielokrotne zastosowanie prostych operacji (zmieszanie i rozproszenie)
* DES - dalej stosowany ale złamany, nie wykorzystywać w nowych systemach!!!
    * S-box
    * rundy
* 3DES
    * Szyfrator, deszyfrator, szyfrator
    * Reużywanie sprzętu do DES
* AES/Rijandael - preferowany

## Szyfry symetryczne i asymetryczne

### Szyfr symetryczne
* Tego samego klucza używa nadawca i odbiorca
* Jeden klucz do szyfrowania i deszyfrowania
* Odtajnienie klucza po jednej stronie odtajnia całą wymianę
* Klucz tajny / wsymetryczny / wspólny

### Szyfr asymetryczny
* Dwa klucze
* Publiczny klucz dla każdego, kto chce zaszyfrować wiadomość
* Prywatny klucz deszyfrujący znany tylko odbiorcy

#### Wymiana wiadomości
* Alicja chce wysłać wiadomość do Bolka
* Bolek generuje parę kluczy
* Bolek udostępnia swój klucz publiczny
* Alicja odszukuje klucz publiczny Bolka
* Alicja szyfruje wiadomość kluczem publicznym Bolka i ją wysyła
	* nie jest w stanie jej już sama odszyfrować
* Tylko Bolek posiadający swój klucz prywatny może odszyfrować wiadomość od Alicji

### Algorytm Diffiego-Hellmana
* Do uzgadniania klucza na niezaufanym (podsłuchiwanym) kanale
* Pierwiastek pierwotny modulo p (logarytm dyskretny)
    * do złamania tylko przez brute-force, bezpieczne dla dużych liczb
    * liczba której potęgi generują wszystkie niezerowe liczby $mod \quad p$ 
* Idea działania
	* Alicja wysyła list do Bolka w zamkniętej szkatułce z własną kłódką
	* Bolek dokłada swoją kłódkę i odsyła szkatułkę
	* Alicja zdejmuje swoją kłódkę i odsyła szkatułkę
	* Bolek zdejmuje swoją kłódkę i odczytuje list
* Algorytm
	* $g$ i $p$ są znane, $g$ jest pierwiastkiem pierwotnym
	* Alicja losuje wartość $X_A$, która jest jej kluczem prywatnym
	* $Y_A = g^{X_A}$ jest jej kluczem publicznym
	* Bolek postępuje analogicznie analogicznie
	* Alicja chce wysłać wiadomość do Bolka
	* Alicja odszukuje jego klucz publiczny i oblicza $K=(Y_B)^{X_A}$
	* Alicja szyfruje wiadomość za pomocą klucza $K$
	* Bolek odbiera wiadomość i odszukuje klucz publiczny Alicji
	* Bolek oblicza $(Y_A)^{X_B}=(g^{X_A})^{X_B}=(g^{X_B})^{X_A}=(Y_B)^{X_A}=K$
	* Bolek odszyfrowuje wiadomość kluczem K

### Szyfrowanie RSA
* Klucz publiczny
	* $N = p \cdot q$, gdzie $p$ i $q$ to duże liczby pierwsze
	* liczba $e$ bez wspólnych dzielników z $(p-1)$ i $(q-1)$
* Klucz prywatny
	* liczby $p$ i $q$
	* liczba $d$, taka że $d \cdot e = 1 \mod \phi(N)$
	* $\phi(N) = (p-1) \cdot (q-1)$ - funkcja Eulera
* Szyfrowanie $C = M^e \mod N$
	* $M$ - tekst jawny
	* $C$ - szyfrogram
* Odszyfrowanie $M = C^d \mod N$


### Bezpieczeństwo szyfrów asymetrycznych
* RSA - problem faktoryzacji
* Diffie-Hellman - problem logarytmu dyskretnego
* Bezpieczeństwo szyfru zależy od trudności rozwiązania problemów matematycznych


### Porównanie
* Wada szyfrów symetrycznych to problem dystrybucji i tajności klucza
    * jeśli wykorzystujemy jeden tajny klucz to jego ujawnienie osłabia cały system
    * jeśli każda para posiada własny klucz to musi ich być $N(N-1)/2$
* Wadą szyfrów asymetrycznych jest prędkość działania
    * potęgowanie modulo liczb o długości rzędu 4K
    * szyfry symetryczne dają się implementować w sprzęcie i mogą być do 1000 razy szybsze

### Szyfr hybrydowy
* Szybkość działania szyfrów symetrycznych
* Działanie
    * generowanie losowego klucza symetrycznego
    * zaszyfrowanie danych kluczem symetrycznym (AES) - szybkie
    * pobranie klucza publicznego odbiorcy
    * zaszyfrowanie kluczem publicznym odbiorcy klucza symetrycznego i wysłanie razem z danymi
    * odbiorca odszyfrowuje klucz symetryczny swoim kluczem prywatnym
    * odbiorca odszyfrowuje dane kluczem symetrycznym
* Można zaszyfrować dane raz przez AES i wysłac wielu odbiorcom szyfrując asymetrycznie już tylko klucz

## Tryby pracy algorytmów blokowych
* Bloki o długości rzędu 16 bajtów
* ECB - elektroniczna książka kodowa
	* każdy blok danych szyfrowany niezależnie od innych
	* identyczne dane dadzą powtarzalny wzorzec w szyfrogramie
* CBC - wiązanie bloków zaszyfrowanych
	* wiązanie następnego bloku z poprzednim
	* XOR bloku tekstu jawnego z poprzednim blokiem szyfrogramu
	* na początku wektor inicjujący
* OFB - wyjściowe sprzężenie zwrotne
	* szyfr strumieniowy zbudowany w oparciu o wielokrotne szyfrowanie klucza i wiązanie wyniku funkcją XOR z danymi do zaszyfrowania
* CTR - tryb licznikowy
	* daje się zrównoleglać
	* identyczne bloki danych będą różne po zaszyfrowaniu
* CFB - sprzężenie zwrotne szyfrogramu
    * połączenie szyfru blokowego ze strumieniowym
    * szyfr strumieniowy oparty o szyfrowanie rejestru przesuwnego zależnego od wyniku poprzedniego szyfrowania

