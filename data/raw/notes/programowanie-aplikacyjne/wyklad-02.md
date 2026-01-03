# Wykład 02
ciąg dalszy

stare WinAPI miało jawną kolejkę zdarzeń
aplikacja pobiera zdarzenia z kolejki i je obsługuje

w większości współczesnych frameworków kolejka zdarzeń jest jakoś ukryta
zdarzenia mają różne priorytety, fragment okna można (było) oznaczyć jako nieświeży, rysowanie miało najniższy priorytet

Rapid Application Development - przeciąganie kontrolek z palety na okno, oryginalnie w Visual Basic


## Zdarzenia w Javie
Wykorzystuje się wzorzec observer
obiekty trzymają listę słuchaczy i po zdarzeniu wywołują na nich odpowiednie metody
okno jest reprezentowane przez obiekt
parametrem zdarzenia jest okno, którego dotyczy


## Wstęp do Javy
* jest kompilowana do kodu pośredniego, który jest później kompilowany na maszynie na której jest wykonywany (runtime environment)
* runtime Javy może być lepiej dostosowany do możliwości procesora niż np. program w C++ skompilowany z domyślnymi flagami
* szeroko wykorzystywany przez korporacje
* maszyna wirtualna na urządzenia mobilne różni się budową od JVM na komputery
* javax.* należy do Oracle, lepiej używać jakarta.*
