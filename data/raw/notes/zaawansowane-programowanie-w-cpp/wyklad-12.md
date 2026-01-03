# C++ zorientowany na wartość  (ZPR- W13 -2021 01 12)

Java jest oparta o wskaźniki
Python jest oparty o referencje
C i C++ mają wskaźniki ale są oparte o wartości

Typy algebraiczne - sumowanie istniejących typów
para - typ mnożący `std::pair<bool, unsigned char>` może mieć 2 * 256 różnych wartości
wariant - typ dodający `std::variant<bool, unsigned char>` może mieć 2 + 256 różnych wartości

użycie wariantu zamiast polimorfizmu - nie ma funkcji wirtualnych ale trzeba się narobić
zamiast wołania funkcji wirtualnych - wzorzec wizytatora

`std::visit(visitor, variant)` - przyjemna obsługa
zachowanie definiowane w wizytatorze dla odpowiednich typów wariantu

lambde implementuje się tak samo jak taki wizytator
użycie `auto` - jednakowa obsługa wielu typów

`std::variant` świetny do parsowania/tokenizacji -> TKOM

`std::optional` do reprezentowania wartości pustych, dobre semantycznie
do konfiguracja
czym innym jest pusty string (bezargumentowy konstruktor) a brak stringa
optional nie wymaga np. utworzenia obiektu tymczasowego (wołania konstruktora) kiedy jest pusty

nie powinno się używać domniemanego rzutowania optional na bool
szczególnie w przypadku `std::optional<bool>` - traci się semantykę