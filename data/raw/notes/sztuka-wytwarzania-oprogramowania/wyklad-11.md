# Współbieżność (2024-05-20)

## Aplikacja wielowątkowa
* Pozwala na reakcję na zlecenia użytkownka podczas przeprowadzania obliczeń
* Lepiej wykorzystuje dostępną moc obliczeniową
* Może obsługiwać wiele zleceń równolegle
* Poprawnie zaprojektowana jest szybsza a platformach wieloprocesorowych

Język programowania musi wspierać współbieżność (np. C++, Java)

## Współbieżność w C++
* Należy używać bibliotek przeznaczonych do pracy wielowątkowej
* Dostarcza mechanizmy tworzenia i synchronizacja w bibliotece standardowej
* Współdzielone
	* obiekty globalne
	* obiekty dynamiczne
	* zasoby systemu operacyjnego
	* kod wykonywany
* Niezależne
	* rejestry
	* ciąg wykonywanych instrukcji
	* stos
	* obiekty automatyczne (na stosie)
* Program ma zawsze jeden wątek (funkcja `main`)
	* może tworzyć kolejne wątki
* Trzeba zlinkować odpowiednią wersję biblioteki standardowej (wielowątową)
	* w przeciwnym razie mogą wystąpić wyścigi
	* ustawiane przez flagę kompilatora

### `std::thread`
* Przyjmuje uchwyt na funkcję główną wątku albo na funktor (obiekt z zaimplementowanym operatorem wołania funkcyjnego)
* Metoda `join` zawiesza bieżący wątek do zakończenia wątku


## Wyścig (race conditions)
* Wiele wątków pisze lub czyta ten sam obszar pamięci
* Nie wiadomo jakie jest wzajemne rozłożenie w czasie instrukcji wątków
* Wyścig można wyeliminować tylko na etapie projektu
* Rozwiązania
	* synchronizacja
	* operacje atomowe
## Problemy z tworzeniem aplikacji wielowątkowych
* Błędy są niepowtarzalne - nie można przeprowadzić deterministycznych testów
* Różne zachowanie wersji debug i release


## Blokada (mutex)
* Sekcja krytyczna umieszczona między wywołaniem instrukcji `lock` i `unlock`
* Wzorzec projektowy RAII
	* `lock` wywołane w konstruktorze
	* `unlock` wywołane w destruktorze


```cpp
struct Lock {
	Lock(mutex &m) : m_(m) {m_.lock();}
	~Lock() {m_.unlock();}
	mutex &m_;
};

std::mutex m;
{
	Lock guard(m);
	// Sekcja krytyczna
} // Zwolnienie zasobów
```

## Zakleszczenie
* Każdy z wątków czeka na jakiś inny, żaden nie może dalej pracować
	* 1: a.lock()
	* 2: b.lock()
	* 2: a.lock()
	* 1: b.lock()
* Rozwiązanie
	* zajmowanie blokad zawsze w tej samej kolejności
	* stosowanie innych mechanizmów synchronizacji

## Kończenie wątku
* Błędne jest przerwanie wątku z zewnątrz
	* nieustalony stan aplikacji
	* wątek mógł być wewnątrz sekcji krytycznej i jej nie zwolni
* Wątek musi zakończyć się sam
* Wątek może przyjmować flagę i sprawdzać czy powinien sam się zakończyć
	* flagę można ustawić z zewnątrz
	* wątek zewnętrzny zgłasza prośbę i czeka aż wątek sam się zakończy

```cpp
class Thread {
public:
	thread(): finish_(false) {}
	void finish() {finish_ = true;}
	void operator()() {
		while !finish_) {
		// sekcja krytyczna
		}
	}
private:
	volatile bool finish_;
};
```


## Skalowalność
* Prawo Amdahla - przyspieszenie dla $p$ procesów
* $S(p) = \frac{1}{1-a+a/n}$
	* $a$ część algorytmu, która może podlegać zrównolegleniu
	* większa liczba procesów przyspiesza tylko część która może być zrównoleglona
* Prawo Gustafsona-Barsisa
	* wraz ze wzrostem liczby procesorów można rozwiązywać coraz większe instancje problemu
	* ...

### Wysoka skalowalność
* Ścieżka szybka
	* nie występują blokady
	* odczyt lokalnych lub współdzielonych danych
	* zapis tylko lokalnych danych
* Ścieżka wolna
	* blokady
	* zapis współdzielonych danych

## Podwójna sprawdzanie

### Poprawne ale nieefektywne

```cpp
Singleton& SIngleton::getInstance() {
	std::lock_guard guard(mutex);
	if (!pInstance) {
		pInstance = new Singleton;
	}
	return *pInstance;
}
```
### Efektywne - wzorzec podwójnego sprawdzania

```cpp
Singleton& SIngleton::getInstance() {
	if (!pInstance) {
		std::lock_guard guard(mutex);
		if (!pInstance) {
			pInstance = new Singleton;
		}
	}
	return *pInstance;
}
```

Ścieżka szybka - nie wchodzi w zewnętrzny `if`

Zakłada kolejność wykonania linii - przydział pamięci, konstruktor, przypisanie
Może być niepoprawny jeśli `pInstance` nie jest `volatile`
Sequence point w C++ to linia
W praktyce to i tak działa na wszystkich platformach


## Wyjątki
* Wyjątki mogą być rzucane i wyłapywane w niezależnych wątkach
* Wątek musi być wygenerowany i złapany w obrębie jednego wątku
	* nie może wyjść poza funkcję główną wyjątku


## Wzorzec monitora
* Obiekt sam zapewnia, że metody mogą być wołane przez różne wątki
* Obiekt sam synchronizuje operacje, które tego wymagają

## Przetwarzanie potokowe
* Algorytm składa się z kolejnych etapów, gdzie kolejny na swoje wejście przyjmuje wyjście poprzedniego etapu
* Wątki pozwalają wygodnie implementować taki model przetwarzania
* Dane można podzielić na bloki i kolejne etapy przetwarzania wykonywać współbieżnie
* Wątki mają bufor wejściowy i wyjściowy - muszą je między sobą synchronizować
* Algorytm może sam dobrać wielkość porcji danych którą będzie przetwarzać
* Mechanizm wątków sprawia że kolejne etapy się między sobą równoważą przez zapełnienianie buforów
* Dwa kolejne kroki współdzielą bufor który może np implementować wzorzec monitora
