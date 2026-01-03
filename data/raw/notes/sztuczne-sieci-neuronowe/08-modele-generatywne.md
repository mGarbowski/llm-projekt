# Modele generatywne

## Uczenie nadzorowane vs generatywne

* Klasyfikator uczy się rozkładu prawdopodobieństwa $p(y|x)$
	* $y$ to klasa
	* $x$ to wejście

## Adwersarialne przykłady
* Klasyfikator uczył się na podstawie skończonej liczby zdjęć
	* może nauczyć się konkretnego zbitka pikseli jeśli tak się ułożyło w zbiorze
* Dodanie odpowiedniego szumu do obrazu może zupełnie zaburzyć wyjściowe prawdopodobieństwo
	* szum może być nieistotny dla ludzkiego oka
	* bardzo łatwo znaleźć taki szum jeśli mamy dostęp do klasyfikatora
* Dla klasyfikatora cały świat to jego zbiór treningowy

## Po co modele generatywne
* Pozwala modelować brakujące prawdopodobieństwo $p(x)$
* Znajomość $p(x)$ pozwala na
	* ustalenie czy przykład był obserwowany w przeszłości
	* ważenie decyzji
	* ustalanie niepewności decyzji
	* aktywne poznawanie środowiska - np. dopytywanie o przykłady o niskim $p(x)$
	* generowanie nowych przykładów
* Przykład
	* $p(y=kon|x)$ jest wysokie ale $p(x)$ jest niskie - niepewna decyzja
	* przykład odstaje od znanego rozkładu
* Tych samych architektur używa się do dźwięku, obrazów i wideo

## Różne modele generatywne
* Wariacyjny autoenkoder (VAE)
* Sieci neuronowe typu GAN
* Modele autoregresywne
* Modele przepływu
* Modele dyfuzyjne / modele funkcji wynikowej

## Autoenkoder generatywny
* Ze zwykłego autoenkodera nie możemy próbkować, bo przestrzeń ukryta jest rzadka
* Dokonujemy regularyzacji przestrzeni ukrytej, żeby wymusić kodowanie zgodnie z jakimś rozkładem
* Z tego rozkładu można losować próbki i dekodować
* Trik reparametryzacji - na ćwiczeniach
* Rozszerzone architektury
	* inne metody regularyzacji
	* hierarchiczne VAE - wiele przestrzeni ukrytych, różne cechy w różnych przestrzeniach
	* Conditional VAE - generując wynik z prompta szukamy rozkładu prawdopodobieństwo pod warunkiem prompta
	* $\beta$-VAE - dodatkowa normalizacja na przestrzeni ukrytej, każdy wymiar Gaussa jest niezależny, można zdekomponować obraz do niezależnych cech, potencjalnie cechy mogą być interpretowalne

## Sieci neuronowe typu GAN
* GAN
	* mamy małowymiarową przestrzeń o znanym rozkładzie
	* losujemy wartości z przestrzeni
	* model generator przetwarza te wartości do przestrzeni o wymiarowości obrazka
	* bierzemy zbiór treningowy z prawdziwymi danymi
	* kolejny model dyskryminator uczy się rozróżniać czy obrazek jest prawdziwy czy fałszywy
	* trenujemy na zmianę generator i dyskryminator
	* analogia do fałszerza i policjanta
* Model matematyczny
	* dyskryminator jest klasyfikatorem
	* dyskryminator maksymalizuje stratę (np. entropia krzyżowa klasyfikacji)
	* generator minimalizuje stratę
	* przy propagacji wstecznej zamrażamy wagi albo jednego albo drugiego
* Generalnie generator będzie dawać zróżnicowane generacje zamiast małpować zawsze jakieś jedno zdjęcie ze zbioru uczącego
	* nie ma bezpośredniego dostępu do tych zdjęć tylko ma odpowiedź od dyskryminatora
	* jest losowość przy generacji - próbkuje się wektor z jakiejś przestrzeni
	* uda się oszukać dyskryminator jeśli rozkład fałszywych obrazów będzie zbliżony do prawdziwych
	* i tak może się zdarzyć mode collapse
* Problemy
	* mode collapse
	* trening jest bardzo niestabilny - kiedy jedna sieć stanie się dużo lepsza od drugiej
	* nie wiadomo kiedy przerwać trening - czy generator jest tak dobry czy dyskryminator tak głupi?
* Zalety
	* nie ma funkcji straty MSE (ona sobie nie radzi z przesunięciem o 1 piksel)
	* dobrej jakości generacje
	* lepsze dopasowanie do złożonych dystrybucji danych
* Rozszerzenia GANów
	* VAEGAN
	* StyleGAN - tłumaczenie z jednego stylu w drugi
	* generalnie modele dyfuzyjne są dużo lepsze

## Modele autoregresywne
* Dzielimy przestrzeń na fragmenty, generujemy obraz po fragmencie biorąc pod uwagę to co generowaliśmy wcześniej
* Problemy
	* przetwarzanie obrazka piksel po pikselu - nie tak postrzegamy obrazy
* Obiecujący wariant
	* vq vae
	* autoenkoder
	* uczymy się słownika cech z których składają się obrazki
	* model autoregresywny działa na przestrzeni ukrytej vae, ten wektor cech jest dekodowany na właściwy obrazek
* Popularne w syntezie mowy, generowaniu tekstu

## Modele przepływu (Flow)
* Schemat
	* na wejściu obrazek
	* model przyjmuje obrazek i koduje go do wektora
	* model to mnożenie macierzy
	* macierz można odwrócić
	* możemy wylosować wektor i macierzami odwrotnymi przejść z powrotem nawet przez ten sam model
* Problemy
	* nie wszystkie macierze da się odwrócić
	* im większy błąd tym gorsza rekonstrukcja
	* psują to funkcje aktywacji (ReLU gubi informacje)

## Modele dyfuzyjne
* Szum zamieniany za pomocą jednego przejścia przez sieć na obrazek
* Obrazek generowany w kilku krokach, iteracyjnie poprawiany
* Dyfuzja
	* mając obrazek $x_0$
	* zaszumiamy go dodając np. Gaussa
	* jeśli zrobimy bardzo dużo takich kroków to szum całkowicie przykryje obrazek
	* proces dyfuzji do przodu
* Można tak dobrać parametry żeby np. po 100 krokach dostać szum o rozkładzie normalnym standardowym
* Model uczy się procesu odwrotnego
	* jak usunąć trochę szumu z zaszumionego obrazka
	* przejście od $x_t$ do $x_{t-1}$
* Obojętnie jaki model nauczymy
	* np. autoenkoder
	* uczymy jeden model i aplikujemy go np. 100 razy
* Trening modelu dyfuzyjnego (intuicyjnie)
	* chcemy jednego modelu który działa na różnych poziomach zaszumienia
	* aplikujemy dekoder T razy w celu wygenerowania obrazu z szumu
	* obliczamy funkcję straty dla każdego kroku osobno
	* trenujemy model na podstawie sumarycznej straty dla każdego kroku
	* bardzo kosztowne obliczeniowo - 1 update modelu wymaga 100 przejść przez model
* Żeby przejść z kroku 0 do 47 to nie musimy dodawać 47 razy szumu, tylko raz dodać szum o 47 razy większej wariancji
	* możemy bez problemu przeskoczyć z $0$ do dowolnego kroku $t$
	* zamiast na raz trenować na wszystkich poziomach zaszumienia, możemy wylosować jeden
	* losujemy $t$ z którego uczymy autoenkoder przejścia do $t-1$
* Funkcja straty - błąd rekonstrukcji
	* Dywergencja Kullbacka-Leiblera
	* można też najprostszy MSE
* Inferencja
	* bardzo wolna dla modeli o dużej liczbie kroków dyfuzji
	* na wejściu dajemy losowy szum, przepuszczamy T razy przez model i dostajemy obrazek
* Prompt
	* architektura UNet
	* prompt jest doklejany jako embedding w każdym poziomie zaszumienia
* Modele latent diffusion
	* VAE
	* obrazki najpierw kodujemy do mniejszej przestrzeni
	* z tej przestrzeni dekodujemy
	* wszystkie dane treningowe najpierw kodujemy do tej przestrzeni
	* z tego trenujemy model dyfuzyjny
	* zysk wydajności obliczeń
* Możemy trenować model tak żeby przewidywał oryginalny obrazek a nie t-1
	* stabilizuje wyjście z UNet'a
	* i potem iteracyjnie słaba predykcja, zaszumienie słabej predykcji i ponownie predykcja
	* łatwiej uczyć UNet jeśli wyjście jest zawsze takie same
