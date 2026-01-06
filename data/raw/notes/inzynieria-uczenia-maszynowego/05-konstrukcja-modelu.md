# Konstrukcja modelu

## Modelowanie
* Często nie można mieć modelu który jednocześnie
	* jest niezawodny
	* daje najlepsze wyniki
	* chcemy z nim pracować (np. dobrze go rozumiemy)
* Modelowanie jest procesem iteracyjnym
* Składniki modelu
	* struktura modelu
	* funkcja celu
	* metoda optymalizacji

## Strojenie hiperparametrów
* Czemu nie ma uniwersalnego zestawu hiperparametrów dla ustalonego modelu
* No free lunch
	* dotyczy optymalizatorów
	* dowolne dwa algorytmy jeśli porównujemy je po wszystkich możliwych problemach optymalizacji to żaden z nich nie będzie lepszy od drugiego ani od błądzenia przypadkowego
* Jeśli nie założymy nic o strukturze problemu optymalizacyjnego to będziemy w błędzie
	* dany algorytm jest dobry tylko dla grupy problemów
* Hiperparametry - sterują architekturą i procesem uczenia
	* krok uczenia
	* liczba warstw w sieci neuronowej
	* itp.
* Nawet jeśli domyślne wartości hiperparametrów są dobre do i tak pewnie da się poprawić działanie modelu bo dostrojeniu
* Jeśli nie ma co więcej zrobić z danymi to zostaje strojenie

### Metody strojenia
* Przeszukiwanie po hipersiatce
	* wszystkie kombinacje wartości hiperparametrów
	* najprostsza możliwa strategia
	* kosztowna obliczeniowo
* Przeszukiwanie losowe
	* zaskakująco skuteczne
	* definiujemy zakresy wartości dla każdego parametru
	* w praktyce nie każde parametry mają równie duży wpływ
	* hipersiatka marnuje dużo budżetu na testowanie nieistotnych parametrów, a dla istotnych testuje mało wartości
* Podejścia bayesowskie
	* w praktyce rzadko się stosuje
	* np. SMBO
	* wprowadza się model zastępczy (model regresji)
	* obliczamy błąd dla kilku punktów
	* dopasowujemy do nich model zastępczy
	* optymalizujemy model zastępczy
	* powtarzamy
	* można szybko przewidywać na podstawie modelu zastępczego bez odpalania właściwego modelu
* Hyperband
	* jak możliwie najszybciej zidentyfikować zestawy złych hiperparametrów żeby nie tracić na nie czasu
	* na wszystkie zestawy jest określony budżet
	* sprawdza się poziom błędu
	* odrzuca się połowę najgorszych
	* zwiększa się budżet i powtarza
* Metaheurystyki
	* algorytmy ewolucyjne itp
* W praktyce najczęściej hipersiatka i losowe

### Kryterium zatrzymania
* Skąd wiedzieć kiedy skończyć strojenie
* Np. przetestowałem 1000 zestawów parametrów, czy to wystarczy?
	* ile trzeba by dorzucić żeby spodziewać się wyraźnie lepszego wyniku
* Rysujemy wykres pudełkowy
	* losujemy n zestawów parametrów spośród zbadanych
	* szacujemy wariancję wyników w zależności od wielkości próby losowej (n)
	* im więcej tym mniejsza wariancja
	* na slajdzie - patrzymy czy już jest wypłaszczenie czy dalej jest ostra poprawa
	* tak jak na slajdzie - trzeba by dołożyć tysiące prób żeby coś dalej poprawić

## Funkcje celu / Miary jakości

### Podstawowe funkcje celu
* Do regresji, klasyfikacji, uczenia nadzorowanego
* MSE, RMSE, MAE, MSLE
* Entropia krzyżowa
* Nie mają żadnych parametrów

### Zaawansowane przypadki
* Do nietypowych zadań, niesymetrycznych kosztów pomyłek
* Metric learning - funkcja straty triplet loss
	* punkty rozważane trójkami - kotwica, pozytywny, negatywny
	* parametryzowany margines
	* jak definiowana odległość
* Przykład z wykładu 2 - edytor tekstu i generowanie dobrej parafrazy zdania
	* potrzebna ocena ekspertów czy wynik jest *dobry* - drogie i czasochłonne
	* ekspertów nie można wpiąć do optymalizacji gradientowej
	* przed oddaniem ekspertom korzystamy z modelu pomocniczego / analitycznego kryterium
	* często modele pomocnicze też się nie nadają do wpięcia do algorytmu uczenia
	* trenujemy model tak żeby np. minimalizował entropię krzyżową, potem model pomocniczy, potem eksperci
* Zachowanie modelu - funkcja celu - analityczna miara jakości - biznesowa miara jakości - spełnienie celu biznesowego
	* liczymy że kolejne miary są do siebie proporcjonalne
	* dobrze ze sobą korelują
	* od lewej - tanie do wyliczenia i wygodne
	* od prawej - istotne dla klienta, długotrwałe i kosztowne
* Wnioski z przykładu
	* jakość modelu to coś innego dla użytkownika, osoby trenującej model i zespołu utrzymującego model online
	* różne miary jakości mierzą różne rzeczy

### Informacje zwrotne
* Bezpośrednie - dla predykcji wiemy czy mieliśmy rację czy nie
	* może od razu, może trzeba poczekać
	* np. przewidujemy przyszłość i możemy poczekać - notowania giełdowe, temperatura
	* np. filtr spamowy - użytkownik oznaczy wiadomość jako spam / zwykłą pocztę - nie zawsze użytkownik zaznaczy
	* np. użytkownicy odrzucają nietrafione rekomendacje
* Pośrednie - nigdy nie wiemy jaka była poprawna wartość
	* możemy tylko szukać w skorelowanych informacjach
	* np. medycyna - monitorowanie działania leku mierząc temperaturę, ciśnienie itp.
	* np. metody uczenia nienadzorowanego
* Brak informacji zwrotnych
	* systemy szacujące koszty awarii
	* nie wiadomo ile firma by zarobiła gdyby serwerownia nie padła

### Modele bazowe
* Względem czego oceniamy model
	* MSE=0.7 nic nie znaczy jeśli nie mamy z czym tego porównać
* Model bazowy - nie musi być związany z uczeniem maszynowym (spytać górala jaka będzie temperatura)
* Nasze rozwiązanie ma być lepsze od modelu bazowego
* Jeśli nie ma nic lepszego to zawsze można odnieść się do modelu losowego
	* np. przy grupowaniu - raz wysyłamy zniżki do losowych klientów, a raz do pogrupowanych algorytmem i patrzymy kiedy był większy zysk
* Ważne na projekt!
* Nie musi być skomplikowany

## Analiza wyników

### Paradoks Simpsona
* Mamy kilka podgrup w danych
* W każdej grupie jest wyraźny trend
* Uśrednienie po grupach odwraca trend
* Widać na przykładach
* Żeby się obronić
	* analizować miary jakości nie tylko w formie zagregowanej ale też z podziałem na kluczowe podgrupy
* Na kolosie!

### Analizowanie monitorowanych miar
* Szeregi czasowe
* W szeregu wyróżnia się składowe szeregu
	* trend
	* wahania okresowe
	* szum losowy
* Wpływ zdarzeń wewnętrznych
	* kalendarz, ważne wydarzenia
* Wykres różnicowy
	* od metryki dzisiaj odejmujemy wartość tydzień temu
	* eliminuje wpływ okresowości tygodniowej
	* dobra sztuczka przy analizowaniu szeregów czasowych żeby lepiej zrozumieć trendy
* Warto oznaczać w narzędziach punkty w czasie
	* np. kiedy zaczyna się kampania marketingowa
	* w Grafanie można oznaczać punkty
