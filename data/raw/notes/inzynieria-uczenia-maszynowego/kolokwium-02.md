## Kolokwium 2

Wykłady 8-14

## Pytania ze slajdów

### Czy tworząc model w “środowisku statycznym” zakładamy, że projekt nie jest realizowany iteracyjnie? 

Niekoniecznie, nadal możemy pracować w sposób iteracyjny aż do np. wykonania finalnej predykcji (jednorazowego) opracowanym modelem. Wcześniej powtarzamy iteracyjnie np. analizę domeny biznesowej, analizę danych i konstrukcję modelu.

### O czym powinniśmy pamiętać, gdy chcemy korzystać z predykcji generowanych przez inny zespół do realizacji naszego modelu?

* O rozkładzie danych wyjściowych z tego modelu
* O komunikacji z zespołem co do zmian w modelu, wdrożeń itd.
	* komunikacji że w ogóle korzystamy z tego modelu

### Czy problem zanikających korelacji może dotyczyć również atrybutów dyskretnych?

* Współczynnik korelacji (Pearsona) jest zdefiniowany dla zmiennych ciągłych, a nie dyskretnych
* Ale może być analogiczny problem dla zmiennych dyskretnych
	* przyjmując odpowiednią miarę *korelacji*
* Np.
	* $x_1$ - pora dnia
	* $x_2$ - typ urządzenia
	* $y$ - czy klient dokona zakupu

### Czy przygotowując system rekomendacji jesteśmy w stanie ocenić jego skuteczność na podstawie danych “offline”?

* Jak rozumiemy skuteczność
* Na danych offline możemy obliczyć analityczne miary jakości
* Jako skuteczność może interesować nas cel biznesowy np. wzrost czasu spędzonego przez użytkowników na platformie streamingowej
	* biznesowa miara jakości
	* nie możemy obliczyć wpływu na zachowanie użytkowników mając tylko dane offline
* Chcemy dobrać takie miary analityczne, które będą jak najlepiej przekładać się na miary biznesowe (a te na spełnienie celów biznesowych)

### Przeprowadzamy eksperyment RCT i informujemy uczestników, do których grup należą – jakie będą tego konsekwencje?

* Może zaburzyć wyniki eksperymentu - efekt placebo/nocebo
* Świadomość przynależności do grupy może wpłynąć na efekt
	* np. kiedy osoba wie, że przyjmuje placebo, a nie prawdziwy lek

### Dlaczego podczas przeprowadzania eksperymentu musimy znać dokładny moment wystąpienia interwencji?

* Jeśli mówimy o eksperymencie A/B w kontekście uczenia maszynowego
* Musimy wiedzieć kiedy zbierać logi
* Musimy znać moment żeby eksperymenty się nie pokrywały
	* 2 eksperymenty jednocześnie wpływają na to samo mierzone zjawisko
	* nie wiemy która zmiana przyczyniła się do poprawy / pogorszenia metryk
### Jaki rozkład w przybliżeniu opisuje zachowanie wartości statystyki w teście z?

Normalny standardowy

### Jakie będą konsekwencje pozwolenia użytkownikom na wybór, do której z grup chcieliby należeć?

* To zaburza wyniki eksperymentu
* W eksperymencie chcemy badać jaki wpływ ma zmiana jednej zmiennej
	* np. wykorzystany model predykcyjny
* Na decyzję użytkownika mogą mieć wpływ inne czynniki i to od nich może zależeć wynik eksperymentu
	* nie zmierzymy wtedy wpływu podmiany modelu
### Czy na ataki z użyciem złośliwych danych podatne są również modele drzewiaste?

* Co do zasady tak, np. boundary attack - metoda dla czarnych skrzynek, nie korzysta z gradientu
	* da radę zastosować na drzewie
* Ze względu na nieliniowy charakter modeli drzewiastych są mniej podatne

### W jaki sposób złośliwie wygenerowane przykłady dałoby się zastosować do diagnostyki modelu?

* Jak w przykładzie z wnioskami kredytowymi
* Chodzi o znalezienie najmniejszej modyfikacji przykładu wejściowego, która zmieni wynik klasyfikacji
* To tak samo postawione zadanie optymalizacyjne
* Do zastosowań XAI możemy mieć dodatkowe ograniczenia na perturbacje
	* powinny być możliwe do zrealizowania (zmniejszenie wieku)
### Jakie konsekwencje będzie miało stosowanie w prywatności różnicowej rozkładów “z grubymi ogonami”?

* Dodawanie do danych szumu z rozkładu z grubym ogonem
* Mocniej maskuje przykłady, nawet odstające
	* większa ochrona prywatności
* Mocno zaburza dane
	* bardzo mocne szumy są nadal całkiem prawdopodobne
	* tak zaburzone dane mogą być mało użyteczne

### Jaki będzie koszt obliczeniowy trenowania odpornego (robust learning) w porównaniu do “klasycznego” podejścia?

* Dużo większy, bo wplatamy w trening zaburzone przykłady
* Przykładów jest więcej
	* np. wiele zaburzeń dla jednego przykładu
### W jakiej przestrzeni rozwiązywane jest zadanie optymalizacji podczas generowania przykładu złośliwego? Czy definiuje się w niej jakieś ograniczenia?

* W przestrzeni danych wejściowych modelu
	* szukamy modyfikacji tych atrybutów
	* opcjonalnie podzbiór atrybutów, ale to bardziej do zastosowań XAI niż do ataku
* Ograniczenie w boundary attack - przykład znajduje się po właściwej stronie granicy decyzyjnej
* Minimalizacja wielkości perturbacji (np. norma L2) przy ograniczeniu - dodanie perturbacji zmienia odpowiedź modelu
