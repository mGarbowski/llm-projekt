# Spring Framework

Dependency injection, inversion of control

time to market i koszty utrzymania - czynniki brane pod uwagę przy wyborze technologii do zbudowania nowej funkcji systemu

Wysiłki standaryzacyjne w Javie dla aplikacji biznesowych (standardy połączenia z bazą danych, kolejkami, współbieżność) - J2EE, JEE, Jakarte EE, Enterprise Java Beans

dążenie do tego, żeby deweloperzy pisali tylko logikę biznesową, a możliwie wiele rzeczy miało dostarczone implementacje standardowych api

Spring powstał w odpowiedzi na drogie licencje na serwery aplikacyjne J2EE
Spring jest Open Source


## Odwrócenie sterowania i wstrzykiwanie zależności
* Na w pełni skonfigurowany, gotowy do użycia system składają się
	* kontener Springa
	* metadane konfiguracyjne
	* obiekty biznesowe dostarczone przez programistę aplikacji (POJO)
* Odwrócenie sterowania
	* to nie programista aplikacji zarządza cyklem życia obiektów (nie pisze funkcji main itd)
	* framework wykonuje kod programisty w odpowiedzi na jakieś zdarzenia w systemie
	* programista dostarcza kodu logiki biznesowej, który obsługuje zdarzenia
* Wstrzykiwanie zależności
	* moduły zależą od siebie
	* wzorzec projektowy do definiowania zależności między modułami
	* zapewnia wymienialność modułów
* POJO
	* plain old java object
	* elastyczne, framework nie narzuca struktury klas
* Metadane
	* np. dotyczące cyklu życia obieków

## Moduły Springa
* Ma architekturę modułową
* Nie trzeba używać wszystkich
	* tylko te których potrzebujemy
* Core Container
	* bazowe funkcjonalności
	* Beans - zarządzanie obiektami
	* Core, Context - logika odpalania aplikacji
* Wsparcie testów
* Dostęp do danych
* Web
* Aspect Oriented Programming

## Demo
* gradle.lockfile
	* wszystkie zależności i ich wersje
* `SpringApplication.run()`
	* zwraca kontekst aplikacji
	* kontekst zawiera wszystkie beany w aplikacji
* Anotacja `@Slf4j` z lomboka
* Warto korzystać z biblioteki standardowej wszędzie gdzie się da zamiast dodawać więcej zależności
	* łatwiejszy w utrzymaniu kod
* Dwa podejścia do zarejestrowania Beanów
	* anotacje na samej klasie `@Service`
	* klasa z anotacją `@Configuration` (fabryka) z metodą zwracającą bean z anotacją `@Bean`
* Kod korzystający z wzorca wstrzykiwania zależności daje się łatwo testować jednostkowo
* Zaleta wstrzykiwania zależności
	* można zmienić wstrzykiwany obiekt np. w trakcie testów
* Anotacja `@SneakyThrows` z lomboka
	* do pominięcia checked exceptions
* Wzorzec z przerywaniem wątku z zewnątrz
* `jps`
	* `ps` ale dla wystartowanych instancji JVM w systemie
* Przy programowaniu wielowątkowym
	* poprawna obsługa sygnału SIGTERM (15)
	* graceful shutdown
* Realizacja feature flags w springu
	* `@ConfigurationProperties`
	* `@ConditionalOnProperty`
	* rejestruje beana tylko jeśli jest ustawiona flaga w application.yml
	* np. inna konfiuracja dla produkcji, inna dla testów

## Dostęp do danych
* Zarządzanie transakcjami
	* Java Transactions Api i inne możliwości
	* zarządzanie przez anotacje
	* która metoda ma się wykonywać jako transakcja
* Wsparcie dla DAO
* JDBC
* Spring Data

### Dwufazowy commit
* Kolejki JMS też mogą być transakcyjne
* Przykładowo
	* aplikacja odczytuje zdarzenie z kolejki
	* przetwarza zdarzenie
	* zapisuje coś do bazy
* Dwufazowy commit
	* nie chcemy żeby zdarzenie zostało zdjęte z kolejki jeśli nie uda się zapis do bazy
	* obie transakcje muszą się udać
	* skomplikowany rollback
	* spring tym zarządza

### DAO
* Transalcja między językiem źródła danych a modelem obiektowym
* np rekordy z SQLa na obiekty w Javie
* w testach zastępuje się mockiem
* Implementacja np. korzystając ze sterowników JDBC

### Dostęp przez JDBC
* Bezpośrednie użycie JDBC wymaga pisania dużo boilerplate
* jdbc tempates bardzo skracają zapis
* podaje się SQL w stringach
* toole od springa
* tabelka co musi programista a co robi spring przy spring-jdbc

### Dostęp za pomocą ORM
* JPA
* Integracja springa z JPA
* Entity Manager oznaczony jako Persistence Context

### Spring Data
* Nie tylko do SQLa
	* Mongo
	* ldap
* pod spodem JDBC, JPA, ...
* Dostarcza wielu gotowych rozwiązań
	* CrudRepository
	* wszystkie standardowe operacje CRUD

## Serwlet
* Interfejs HttpServlet z czystej Javy
	* metoda inicjalizująca
	* metody do obsługi get i post
	* argumenty request i response
* deployowany do serwera aplikacyjnego, kontenera serwletów
	* np. tomcat
* spring opakowuje serwlety

## Wzorzec MVC
* Model
	* model domenowy danych
* View
	* wyświetlany użytkownikowi
* Controller
	* manipuluje danymi opartymi o model
* wzorzec do tworzenia aplikacji z interfejsem użytkownika
* użytkownik używa kontrolera
* kontroler modyfikuje model
* model uaktualnia widok

### Spring web mvc
* Do aplikacji webowych lub rest api
* do sever side rendering (np z użyciem thymeleaf) są devtoole z wsparciem hot module reload
* spring actuator - monitoring
* biblioteka która z automatu generuje strone ze specyfikacją api
	* swagger, openapi
