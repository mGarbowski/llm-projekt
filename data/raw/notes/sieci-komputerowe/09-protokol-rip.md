# Protokół RIP
Routing Information Protocol - najprostszy protokół routingu dynamicznego

* Oparty o algorytm Bellmana-Forda
* Distance vector algorithm
* Wpisy w tabeli mają ustalony czas życia

### Działanie
* Router co określony czas rozgłasza swoją tabele routingu do sąsiednich routerów
* Routery nasłuchują na rozgłoszenia i zapisują zawartość
    * zwiększają metrykę o 1
    * nie zapisują ścieżek, którę są gorsze od już zapisanych

### Nagłówek
* command
* version
* address family
* IP address
* metric - liczba skoków (distance vector)

Nie zawiera maski sieci - tylko routing klasowy

### Zliczanie do nieskończoności
Przy usunięciu wpisu w tabeli pojawia się problem z zapętleniem

* router usuwa wpis w swojej tabeli
* dostaje błędny wiersz od sąsiedniego routera (odpowiednik tego usuniętego ale ze zwiększoną metryką)
* router zapisuje błędny wiersz i zwiększa metrykę
* po upłynięciu czasu życia wpisu proces się powtarza

Ustala się maksymalną metrykę jako 16, po osiągnięciu 16 wpis jest usuwany - to dalej zajmuje dużo czasu

### Split horizon
Router nie odsyła w dany kierunek (przez interfejs) tych wierszy, które otrzymał z tamtego kierunku (interfejsu).

Eliminuje problem z zapętleniem się wpisu po usunięciu i zliczania do nieskończoności (chyba że w sieci są cykle)

### Poisoned reverse
Przy usunięciu wpisu w tabeli, router rozgłasza ten sam wpis ale z metryką ustwaioną na 16 (maksymalną) - propaguje usunięcie informacji o ścieżce do pozostałych routerów


### Triggered updates
W przypadku zmian w tabeli routingu, tabela jest rozgłaszana natychmiast, poza normalną kolejnością - zliczanie do nieskończoności zajmuje maksymalnie kilka sekund, w połączeniu z poprawkami (split horizon, poisoned reverse) - jeszcze szybciej

## RIP v.2
Wspiera routing bezklasowy (zawiera maski) i uwierzytelnianie

### Nagłówek
* command
* version
* address family
* route tag - identyfikator routera, nadawca rozpoznaje kiedy informacje do niego wracają
* IP address
* subnet mask - routing bezklasowy
* next hop - przydatne w sieci dostawcy internetu
* metric

## Problem z metryką
Liczba routerów w ścieżce nie określa w wymierny sposób czasu potrzebnego do przejścia śieżki ze względu na różnice w fizycznych łączach (modem vs gigabit ethernet) - czym innym jest najkrótsza i najszybsza droga. Patrząc tylko na metrykę, router może wybierać ścieżki, które mają mniej skoków ale te skoki są wolniejsze

## Koszt
* Liczba odwrotnie proporcjonalna do szybkości łącza
* Koszt ścieżki - suma kosztów poszczególnych odcinków
* Lepszy od metryki - bezpośrednio przekłada się na czas

## Równoważenie obciążeń
Kiedy istnieje wiele jednakowo dobrych tras, router wybiera ścieżkę związaną z interfejsem o najmniejszym obciążeniu, pozwala na zwiększenie przepustowości
