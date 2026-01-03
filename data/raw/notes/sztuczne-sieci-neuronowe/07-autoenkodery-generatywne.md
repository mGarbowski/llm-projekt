# Autoenkodery generatywne
* Co jakby wziąć punkt z przestrzeni ukrytej w otoczeniu innych reprezentujących jakieś pojęcie (np. konia)
	* możemy wylosować taki punkt i go zdekodować dekoderem
	* z każdym kolejnym wymiarem dokłada się więcej pustej przestrzeni niewypełnionej przykładami treningowymi
	* z wymiarowością rośnie prawdopodobieństwo, że wylosujemy punkt bardzo daleko od czegoś sensownego
	* klątwa wymiarowości
* Można dokonać regularyzacji przestrzeni ukrytej
	* niech wszystkie przykłady będą zakodowane wg znanego rozkładu prawdopodobieństwa (najlepiej Gauss)
	* sprzeczne zadania z zachowaniem zdolności rozróżniania reprezentacji ukrytych od siebie
* Autoenkoder generatywny może generować nowe przykłady z losowych wartości o rozkładzie normalnym podawanym przez warstwę ukrytą

## Model probabilistyczny z przestrzenią ukrytą
* Mamy próbki z rzeczywistego rozkładu
* Wprowadzamy model w ramach którego uczymy się przestrzeni ukrytej, z której można losować reprezentację przykładu - $z$
* Na podstawie $z$ można losować przykład $x$ z warunkowego prawdopodobieństwa $p(x|z)$
* Szukamy mapowania do przestrzeni ukrytej $z$ opisanej znanym rozkładem (gaussem)

### Aproksymacja rozkładu
* Teoretycznie można metodą Monte Carlo
	* dla wielowymiarowego problemu - klątwa wymiarowości
* Aproksymacja rozkładu metodą variational inference - alternatywa

### Evidence Lower Bound (ELBO)
* Enkoder jest siecią neuronową z parametrami $\phi$
	* przyjmuje x
	* stochastycznie zwraca z
* Minimalizowany błąd rekonstrukcji
	* zakładamy że przykłady treningowe dobrze odzwierciedlają rozkład
* Regularyzacja - kara za odejście od znanego rozkładu (np. Gaussa)
