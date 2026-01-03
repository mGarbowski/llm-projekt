# Kolokwium 2

## Analiza, metryki

### Czym różni się analiza statyczna od dynamicznej
Analiza dynamiczna wymaga uruchomienia programu (np. w zwirtualizowanym środowisku), a analiza statyczna dotyczy *martwego* programu (bez uruchamiania)

### Czym się różni metryka statyczna od dynamicznej
Metryka dynamiczna wymaga uruchomienia programu (np. zużycie pamięci), a statyczna nie (np. procent linii komentarzy)

### Przykłady analizy dynamicznej
* Użycie pamięci i wycieki
* Użycie cache
* Użycie procesora
* Wykorzystanie sieci
* Wykorzystanie dysku

### Jakie aspekty oprogramowania można mierzyć (jakie grupy metryk oprogramownia można wyznaczyć)?
* Metryki kodu
	* liczba linijek
	* procent linii komentarzy
	* średnia liczba linijek w funkcji
	* maksymalna liczba parametrów funkcji
* Metryki procesu wytwarzania oprogramowania
	* liczba zgłoszonych błędów
	* średnie przekroczenia szacowanego czasu
* Metryki testów
	* pokrycie linii
	* pokrycie gałęzi

### Przykłady metryk dynamicznych
* Czas wykonania programu
* Czas ładowania programu
* Zużycie CPU/pamięci/dysku

### Przykłady metryk statycznych
* Liczba linii kodu
* Złożoność cyklometryczna
* Liczba linii w funkcji
* Procent linii komentarzy

### Czy (i ewentualnie jak) można mierzyć "utrzymywalność" kodu?
* Każda metoda wyliczania utzrymywalności jest obarczona wadami
* Można wykorzystać różne metryki, które mogą być pomocne w ocenianiu utrzymywalności
* Przykładowe metryki
	* złożoność cyklometryczna
	* średnia długość funkcji
	* liczba linijek kodu
	* itp.

### Czy (i ewentualnie jak) można mierzyć jakość testu
* Można wykorzystać metryki takie jak do zwykłego kodu
* Można wykorzystać metryki specyficzne dla testów
	* pokrycie linii
	* pokrycie decyzji
* Pokrycie (i inne metryki) nie gwarantują że test jest dobry
	* scenariusze mogą nie być reprezentatywne
	* asercje mogą być nie takie jak trzeba
	* wymagania klienta mogą nie być weryfikowane przez test

### Czy analiza dynamiczna ma przewagę nad statyczną?
* Generalnie nie
	* analiza dynamiczna i statyczna służą do różnych rzeczy
	* są rzeczy, które da się sprawdzić tylko przez analizę dynamiczną (np. wykorzystanie zasobów, IO, wycieki pamięci)

### Co pokrycie kodu mówi o jakości testu?
* Mówi jaka część kodu (linijki / gałęzie) jest wykonywana przez testy
* Pokrycie powinno być wysokie, ale to nie znaczy że przy 100% gwarantuje poprawne działanie
* Zgodność testu z wymaganiami jest niemierzalna

### Jak ocenić jakość testu? Na ile ocena będzie obiektywna?
* Ocena na podstawie metryki (np. pokrycie gałęzi) jest obiektywna
	* to że jest obiektywna nie znaczy, że jeśli jest odpowiednio wysoka to test jest dobry
* Właściwa ocena jakości testu (czy faktycznie testuje to co ma testować) nie jest mierzalna przez metryki
	* ocena przez człowieka będzie subiektywna
	* poddanie testu pod code review da lepszą subiektywną (intersubiektywną?) ocenę niż pojedyncza osoba

### W jakim celu prowadzi się analizę aplikacji
* W celu poprawienia jakości
	* wykrycia błędów
	* wykrycia niezgodności ze standardem kodowania
	* profilowanie w celu poprawy wydajności

## Pokrycie

### 1
```cpp
std::shared_ptr<Item> Service::method(const Other* obj, int x) {
	if (obj != nullptr && obj->hasSomeProperty())
		return nullptr;
	if (x < -10)
		throw InvalidArgument(x);
	return x > 5 ? Item::Default : std::make_shared<Item>(x);
}
```


* 100% pokrycia linii
	* `obj != nullptr && obj->hasSomeProperty()`
	* `obj == nullptr && x == -11`
	* `obj == nullptr && x == 0`
* 100% pokrycia gałęzi
	* `obj != nullptr && obj->hasSomeProperty()`
	* `obj != nullptr && !obj->hasSomeProperty()`
	* `obj == nullptr && x == -11`
	* `obj == nullptr && x == 6`
	* `obj == nullptr && x == 4`

### 2
```cpp
std::shared_ptr<Item> Service::method(const Other* obj, int x) {
	if (x < this->range().lowerBound)
		throw InvalidArgument(x);
	if ((obj == nullptr) || (obj->isExcluded()))
		return nullptr;
	return (x >= this->range().upperBound) ? Item::Default : std::make_shared<Item>(x);
}
```

* 100% pokrycia linii
	* `x < this->range().lowerBound`, `obj` dowolnie
	* `x >= this->range().lowerBound && obj == nullptr`
	* `x >= this->range().lowerBound && obj != nullptr && !obj->isExcluded()`
* 100% pokrycia gałęzi
	* `x < this->range().lowerBound`, `obj` dowolnie
	* `x >= this->range().lowerBound && obj == nullptr`
	* `x >= this->range().lowerBound && obj != nullptr && obj->isExcluded()`
	* `x >= this->range().lowerBound && obj != nullptr && !obj->isExcluded() && x >= this->range().upperBound`
	* `x >= this->range().lowerBound && obj != nullptr && !obj->isExcluded() && x < this->range().upperBound`

### 3
```cpp
std::unique_ptr<Event> Service::method(double d, const Other* obj) {
	if ((obj == nullptr) || !obj->isEnabled())
		return std::make_unique<IgnoredValueEvent>(d);
	if (d < obj->minimumSupportedValue())
		throw InvalidArgument(d);
	return (obj->threshold() < d) ? std::make_unique<LimitReachedEvent>(d) : nullptr;
}
```

* 100% pokrycia linii
	* `obj == nullptr`
	* `obj != nullptr && obj->isEnabled() && d < obj->minimumSupportedValue()`
	* `obj != nullptr && obj->isEnabled() && d >= obj->minimumSupportedValue()`
* 100% pokrycia gałęzi
	* `obj == nullptr`
	* `obj != nullptr && !obj->isEnabled()`
	* `obj != nullptr && obj->isEnabled() && d < obj->minimumSupportedValue()`
	* `obj != nullptr && obj->isEnabled() && d >= obj->minimumSupportedValue() && obj->threshold() < d`
	* `obj != nullptr && obj->isEnabled() && d >= obj->minimumSupportedValue() && obj->threshold() >= d`

## Co jest nie tak z poniższym kodem

### 1
```cpp
int Service::process(const Request& r, bool ignored) {  
// sprawdzamy, czy usługa działa  
    if (isConfigured() && registry->isEnabled(this) && subservice != nullptr && subservice->isConfigured()  
        && subservice->isActive() && registry->isEnabled(subservice))  
    {  
        if (!r.header.topic.items.contain(Request::Header::Type::Active))  
            return -2;  
        auto tmp = r.body.items[3].data;  
        if (tmp > 5) {  
            tmp = 15 * itemCount();  
            if (ignored)  
                throw IncorrectRequest(r);  
            tmp = sendResponse(r, tmp);  
            if (tmp != 0)  
                return tmp;  
            else  
                return 0;  
        } else {  
            if (ignored)  
                throw IncorrectRequest(r);  
            tmp = sendResponse(r, 15 * itemCount() - 2);  
            if (tmp != 0)  
                return tmp;  
            return 0;  
        }  
    }  
    else  
    {  
        return -4;  
    }  
    return -5;  
}
```

* Argument typu `bool` - lepiej użyć `enum`
* Pierwszy `if` można uprościć
	* to samo jest robione na `this` i `subservice`
	* można to wydzielić jako oddzielną metodę
* Zmienna o nazwie `tmp`
	* nazwa powinna być deskryptywna, tu nie wiadomo o co chodzi
* Drugi `if`
	* sprawdzany warunek mógłby być metodą `Request::isActive`
* Użycie *magic numbers*
	* lepiej użyć stałych / `#define`
	* z deskryptywnymi nazwami
* Głębokie zagnieżdżenia
	* zewnętrzny `if` można odwrócić i spłaszczyć


### 2
```cpp
int Service::process(const Request& r, bool ignored, Type t) {  
// sprawdzamy, czy usªuga dziaªa  
    if (isConfigured() && registry->isEnabled(this) && subservice != nullptr && subservice->isConfigured()  
        && subservice->isActive() && registry->isEnabled(subservice))  
    {  
        if (!r.header.topic.items.contain(Request::Header::Type::Active))  
            return -2;  
        auto tmp = r.body.items[3].data;  
        if (tmp > 5) {  
            tmp = 1685 * itemCount();  
            if (ignored)  
                throw IncorrectRequest(r);  
            switch (t) {  
                case Type::Responding: return sendResponse(r, tmp);  
                case Type::Blocked: return -3;  
                default: return 0;  
            }  
        } else {  
            if (ignored)  
                throw IncorrectRequest(r);  
            switch (t) {  
                case Type::Responding: sendResponse(r, 15 * itemCount() - 2);  
                case Type::Blocked: return -3;  
                default: return 0;  
            }  
        }  
    }  
    else  
    {  
        return -4;  
    }  
    return -5;  
}
```

* Użycie *magic numbers*
	* powinny być deskryptywnie nazwane stałe
* Użycie parametry `Type t` i instrukcji `switch` zamiast polimorfizmu
* Użycie parametru `bool ignored`
	* lepiej użyć deskryptywnie nazwany `enum`
* Nazwa zmiennej `tmp`
	* powinna być nazwana deskryptywnie
* Pierwszy `if`
	* jest duplikacja kodu
	* jest zbyt długi i skomplikowany
* Drugi `if`
	* powinien być wywołaniem metody na `r`
* Zduplikowany `throw IncorrectRequest(r)`
	* można wyjąć przed instrukcję `if`
* Instrukcja `case` bez `break` albo `return`
* Mocno zagłębione `if`y
	* można odwrócić warunki i spłaszczyć  zagłebienie (`return` bez `else`)
* Ostatni `return` jest nieosiągalny

### 3
```cpp
int Client::download(const Item& i, Processing p, bool confirmed)  
{  
// sprawdzamy połączenie  
    if (isConnected() && isActive() && (requests.size() == 0) && ((security == nullptr) || security->isAdmin() || security->allowsDownloads()))  
    {  
        auto tmp = i.options.flags[3].value;  
        if (tmp < 15) {  
            tmp = 2 * i.size();  
            switch (p) {  
                case Processing::Async: return confirmed ? startDownload(i, tmp) : - 5;  
                case Processing::Sync: return confirmed ? downloadNow(i) : -3;  
                default: return 0;  
            }  
        } else {  
            switch (p) {  
                case Processing::Sync: return confirmed ? downloadNow(i) : -3;  
                case Processing::Async: return confirmed ? startDownload(i, tmp - 2) : - 5;  
                default: return 1;  
            }  
        }  
    }  
    else  
    {  
        if (parent.mainProvider.registry.items.cache.contains(i))  
            return 2;  
        return -4;  
    }  
    return -5;  
}
```

* Argument `p` i `switch` zamiast polimorfizmu
* *Magic numbers*
* Argument boolowski zamiast enum
* Nieosiągalny kod
* Zmienna `tmp`
* Długi warunek w pierwszym `if`ie
* Odwołania głęboko w hierarchię w ostatnim `if`ie i w definicji `tmp`
* Głęboko zagnieżdżone `if`y
