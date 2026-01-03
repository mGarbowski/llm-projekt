# Kolokwium 01

## Cykl życia wytwarzania oprogramowania

### W którym momencie procesu wytwarzania oprogramowania uzyskujemy gwarancję poprawności programu? Kiedy możemy go dostarczyć klientowi?

* Nigdy nie ma 100% gwarancji poprawności (może być przy metodach weryfikacji formalnej), bo testy wykrywają tylko znane błędy
* Rzetelne przetestowanie programu zwiększa pewność co do jego poprawności
* Program można dostarczyć klientowi jeśli przechodzi testy akceptacyjne
	* mogą być opisane w zawartej umowie

### Dlaczego warto oczekiwać, by wymaganie było, między innymi, weryfikowalne i jednoznaczne?
* Weryfikowalne - możemy określić czy zostało spełnione
* Jednoznaczne - zrozumiałe dla każdego odbiorcy, nie daje pola do interpretacji
* Warto tego oczekiwać, ponieważ pozwala na jasne określenie czy wymagania są spełnione czy nie, np. na potrzeby zaakceptowania produkut przez klienta, zapłacenie za wykonany produkt

### Kiedy można powiedzieć o wymaganiu, że jest jednoznaczne? Podaj przykład - własny, wskazujący na zrozumienie tematu.
Wymaganie jest jednoznaczne, kiedy wszystkie używane w nim pojęcia są zrozumiałe dla każdego odbiorcy

Np. "Program umożliwia zapisanie danych o procesie do bazy danych" - proces może odnosić się do procesu w systemie operacyjnym, procesu produkcyjnego w fabryce, procesu sądowego, należy doprecyzować o jaki dokładnie proces chodzi (np. w słowniku pojęć)

### Dlaczego przyjmuje się, że dobry test powinien być deterministyczny? Podaj przykład problemu i jego rozwiązania
Jeśli test jest deterministyczny, to mamy pewność że dla tych samych danych wejściowych, rezultat testu będzie zawsze taki sam.

Funkcja wykorzystująca generator liczb pseudolosowych może być niemożliwa do przetestowania, kiedy za każdym razem wynik zależy od psudolosowej liczby.

Można to rozwiązać przez przekazanie jako argument funkcji ziarna generatora / całego generatora, który da się zamockować.

### Kiedy można powiedzieć o wymaganiu, że jest atomowe? Podaj przykład własny, wskazujący na zrozumienie tematu.
Atomowe wymaganie jest niepodzielne, nie składa się z wielu części, bez spójnika "i"

Np. nie jest atomowe "Aplikacja wysyła powiadomienie przez email i SMS"
Lepsze są 2 atomowe wymagania "Aplikacja wysyła powiadomienie email. Aplikacja wysyła powiadomienie SMS"

## SOLID

### Przykład 1
* Łamie zasadę pojedynczej odpowiedzialności
	* przechowywanie zawartości dokumentu
	* łączenie dokumentów
	* sprawdzanie pisowni
	* renderowanie
* Łamie zasadę open-closed
	* `HiddenContent` musi nadpisać metodę `render` nawet gdy nie ma to sensu
* Łamie zasadę Liskov
	* `HiddenContent*` nie może być traktowany jak `Content*`, ponieważ wywołanie `render` zawsze rzuci błąd
* Łamie zasadę segregacji interfejsów
	* ten sam interfejs do scalania, sprawdzania pisowni i renderowania
* Łamie zasadę inwersji zależności
	* `isSpellingCorrect` zależy od konkretnego `EnglishDictionary`
	* powinien zależeć od abstrakcyjnego słownika
	* umożliwiłoby internacjonalizację
* Jak można poprawić
	* oddzielna klasa do sprawdzania pisowni, przyjmuje dokument jako argument, słownik da się sparametryzować
	* daje się lepiej rozszerzać, np. na inne języki
	* oddzielny interfejs do renderowania
```cpp
class Content
{
public:
	const std::vector<std::string>& words() const;
	void mergeWith(const Content& other)
	{
		words_.insert(std::end(words_),
		std::cbegin(other.words()), std::cend(other.words()));
	}
	
	bool isSpellingCorrect() const
	{
		EnglishDictionary dictionary;
		return std::ranges::all_of(words(),
			[&dictionary](const auto& w) {
				return dictionary.hasElement(w);
			}
		);
	}

	virtual void render(Screen& screen)
	{
		// ...
	}
protected:
	std::vector<std::string> words_;
};

class HiddenContent : public Content
{
public:
	explicit HiddenContent()
	{
		words_.emplace_back("Hide!");
	}
	
	void render(Screen& screen) override
	{
		throw std::runtime_error("Content hidden");
	}
};
```

### Przykład 2
*  Łamie zasadę pojedynczej odpowiedzialności
	* `Button` odpowiada i za obsługę kliknięcia guzika i za jego wyświetlanie
* Łamie zasadę open-close
	* `HiddenButton` musi nadpisać metodę `render` kiedy nie ma to sensu
* Łamie zasadę Liskov
	* klasa dziedzicząca `HiddenButton` nie może być traktowana jednakowo jak `Button` przy wywołaniu `render`
* Łamie zasadę segregacji interfejsów
	* `render` powinno być objęte w oddzielnym dla obiektów, które można wyświetlać
* Łamie zasadę inwersji zależności
	* `Button` zależy od konkretnej sesji `chrome::Session` zamiast od abstrakcyjnej sesji przeglądarki
* Jak poprawić
	* Oddzielna klasa, która przyjmuje `Button` i go wyświetla
	* Sesja Chrome zastąpiona abstrakcyjną sesją przeglądarki
```cpp
class Button  
{  
public:  
    Button(chrome::Session& session_, std::string_view url_)  
            : session(session_), url(url_)  
    {}  
    virtual ~Button() {}  
    virtual void render(Screen& screen)  
    {  
// ...  
    }  
    void onClick()  
    {  
        session.request(url + "/pressed");  
    }  
private:  
    chrome::Session& session;  
    std::string url;  
};  
class HiddenButton : public Button  
{  
public:  
    HiddenButton(chrome::Session& session, std::string_view url)  
            : Button(session, url) {}  
    void render(Screen& screen) override  
    {  
        throw std::runtime_error("Button hidden");  
    }  
};
```

### Przykład 3
* Złamana zasada SRP
	* klasa odpowiedzialna za trzymanie danych, sprawdzanie pisowni i zapisywanie do pliku
* Złamana zasada ISP
	* jeden interfejs zapisuje do pliku i sprawdza pisownię
* Złamana zasada DIP
	* zależy od konkretnego `EnglishDictionary`
	* zapis konkretnie do pliku, można do strumienia wyjściowego

```cpp
class Page  
{  
public:  
    const std::vector<std::string>& words() const;  
    bool isSpellingCorrect() const  
    {  
        EnglishDictionary dictionary;  
        return std::ranges::all_of(words(), [&dictionary](const auto& w) { return dictionary.hasElement(w); });  
    }  
    void save(const std::string& fileName)  
    {  
        std::ofstream out(fileName);  
        std::ranges::copy(words(), std::ostream_iterator<std::string>(out, " "));  
    }  
};
```

Poprawiony kod
```cpp
#include <string>  
#include <algorithm>  
#include <vector>  
  
class Page {  
public:  
    const std::vector<std::string>& words() const;  
};  
  
class Dictionary {  
public:  
    virtual bool hasElement(const std::string &w) = 0;  
};  
  
class EnglishDictionary : public Dictionary {  
    // ...  
};  
  
class SpellChecker {  
public:  
    SpellChecker(Dictionary *dict) : dictionary(dict) {}  
  
    bool isSpellingCorrect(Page &page) {  
        return std::ranges::all_of(page.words(), [this](const auto& w) { return dictionary->hasElement(w); });  
    }  
private:  
    Dictionary *dictionary;  
};  
  
class PagePersister {  
public:  
    void save(Page &page, std::ostream &outputStream) {  
        std::ranges::copy(page.words(), std::ostream_iterator<std::string>(outputStream, " "));  
    }  
};
```

### Przykład 4
* Złamana zasada SRP i ISP
	* ta sama klasa przechowuje dane, łączy dokumenty i zapisuje do pliku
* Złamana zasada DIP
	* zapis może być tylko do pliku (konkretne) zamiast bardziej ogólnie np do strumienia wyjściowego
* Jak naprawić
	* oddzielna klasa, która przyjmuje dokument, strumień wyjściowy i go zapisuje
```cpp
class Document  
{  
public:  
    void save(std::string_view fileName)  
    {  
        std::ofstream out(fileName);  
        out << title();  
        out << "\n";  
        out << data(); // typ Data poprawnie obsªu»y t¦ operacj¦  
        out << "\n.\n";  
    }  
    std::string title() const;  
    Data data() const; // implementacja typu Data jest nieistotna  
    void combine(const Data& other)  
    {  
// szczegóªy implementacji nie maj¡ znaczenia  
    }  
};
```

### Przykład 5
Złamana zasada pojedynczej odpowiedzialności - obliczanie wyniku i wypisywanie na STDOUT.

Należałoby ewentualne wypisywanie wyniku obsłużyć tam, gdzie jest wołane `execute`
```cpp
struct Example  
{  
    int execute(int a)  
    {  
        const int result = a * a;  
        std::cout << "result is:" << result;  
        return result;  
    }  
};
```


### Przykład 6
* Kod łamie zasadę LSP
* Dla `DocumentFileWriter` write wykonuje pełną operację zapisu
* Dla `DocumentDatabaseWriter` write, żeby zapisać dokument wymaga wywołania później `commit`
* Wskaźnik na `DocumentWriter` nie może być traktowany jednakowo dla każdej podklasy
* Zatwierdzenie transakcji powinno być wołane wewnątrz `DocumentDatabaseWriter::write`

```cpp
class DocumentWriter  
{  
public:  
  virtual void write(const Document& doc) = 0;  
};

class DocumentFileWriter : public DocumentWriter  
{  
public:  
  void write(const Document& doc) override  
  {  
    out << doc.header() << "\n" << doc.data() << "\n.\n";  
    out.flush();  
  }  
  
  // ... szczegóły implementacji są nieistotne  
};  
  
class DocumentDatabaseWriter : public DocumentWriter  
{  
public:  
  void write(const Document& doc) override  
  {  
    db.insertRow(doc.header(), doc.data());  
  }  
  
  void commit()  
  {  
     db.commit();  
  }  
  
  // ... szczegóły implementacji są nieistotne  
};  
  
void userCode()  
{  
  Document doc;  
  // ...  
  DocumentWriter* writer = factory.createWriter();  
  writer->write(doc);  
}
```

### Przykład 7
* Złamane zasady SRP i ISP
	* ta sama klasa trzyma dane, obsługuje zapis do pliku i scalanie dokumentów
	* do zapisu i scalania powinny być oddzielne interfejsy
	* zapis powinna obsługiwać oddzielna klasa przyjmująca dokument jako argument metody
* Złamana zasada DIP
	* zapis konkretnie do pliku zamiast ogólnie do strumienia wyjściowego
	* lepiej byłoby przekazać otwarty strumień wyjściowy
```cpp
class Document  
{  
public:  
  void save(std::string_view fileName)  
  {  
    std::ofstream out(fileName);  
    out << title();  
    out << "\n";  
    out << data(); // typ Data poprawnie zachowa swoje dane w tej operacji  
    out << "\n.\n";  
  }  
  
  std::string title() const;  
  Data data() const; // typ Data nieistotny dla reszty problemu

  void combine(const Data& other)  
  {  
    // szczegóły implementacji nie mają znaczenia  
  }  
};
```

### Przykład 8
* Złamane zasady SRP i ISP
	* ta sama klasa trzyma dane, drukuje i scala dokumenty
	* drukowanie powinna obsługiwać oddzielna klasa, która przyjmuje dokument jako argument metody
	* scalanie i drukowanie powinny być widoczne przez różne interfejsy
* Złamana zasada DIP
	* `Document` zależy od konkretnego `ColorPrinter`
	* moduł odpowiedzialny za drukowanie dokumentu i obsługujący kolorową drukarkę powinien zależeć od wspólnego interfejsu 
```cpp
class Document  
{  
public:  
  void print()  
  {  
    ColorPrinter p;  
    //  szczegóły implementacji nie mają znaczenia  
    p.print();  
  }  
  
  std::string title() const;  
  Data data() const; // typ Data umie się zapisywać  
  
  void combine(const Data& other)  
  {  
    // szczegóły implementacji nie mają znaczenia  
  }  
};
```