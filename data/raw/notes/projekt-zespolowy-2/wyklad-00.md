# Organizacja

* Materiały na leonie
* Obowiązkowe ćwiczenia
* W następnym tygodniu pierwsze ćwiczenie
* Harmonogram jest na leonie
* Przed świętami zaczynamy robić prototypy
* Spotkania feedbackowe z mentorem
* Pierwszym zadaniem będzie złożenie dokumentu z zatwierdzonymi przez (kogoś?) wymaganiami
	* proces uzgadniania wymagań jest iteracyjny i długo trwa
* Pierwsze spotkanie z właścicielem umawia mentor
* Eksperci będą oceniać czy projekt jest wykonany zgodnie ze sztuką i dobrymi praktykami
	* 2 razy, przed prezentacją śródsemestralną (1.12 i 10.01)
* Punktacja indywidualna i zespołowa
	* mentor decyduje o dystrybucji punktów w zespole
	* ankiety o współpracy w zespole
	* ocena jakościowa mentora
* Na leonie będą spisane wymagania ekspertów z każdej dziedziny
* Wytyczne i szkielet dokumentacji
	* składa się w leonie zatwierdzone wymagania, dokumentację wstępną i dokumentację finalną
* Prezentacja też jest oceniana jako osobny produkt
* Do przygotowania wizytówka zespołu
* Instrukcja na filmiku jak się wybiera temat projektu
* Do piątku wybór(?)
* Teams do bieżącej komunikacji
* Każdy zespół będzie miał założony prywatny kanał
* Na teams będzie excel ze składami zespołów
* Mentor doradza i ocenia (przyznaje najwięcej punktów)

## Architektura
* Najlepiej zacząć rozważania o projekcie od architektury
* Można na tej podstawie podzielić się pracą
* Oceniane jak czytelnie komunikujemy to co chcemy zrobić bardziej niż to jak Odpowiednia jest sama architektura
* Można opisać w UML, modelu C4
* Przy modelu C4 raczej tylko 3 pierwsze poziomy
* Kontakt przez mail albo teams z ekspertem żeby omówić projekt architektury

## Trwałość danych
* Piotr Salata
* Bazy danych nie są jedyną możliwością
	* SQL
	* noSQL
	* pliki
* Wybór metody ma duży wpływ na całą architekturę rozwiązania
	* warto opracować ją wcześnie
* Mogą być projekty bez trwałości danych
* Sposób reprezentacji trzeba opracować i opisać
* Model pojęciowy
	* diagram ER, diagram klas UML
* Model logiczny
	* struktura sposobu reprezentacji danych właściwego dla technologii
	* jakiś diagram który zapewnia czytelną prezentację
	* inne obiekty (np. triggery w bazie SQL) też należy opisać
* Udokumentować sposób komunikacji między aplikacją a bazą danych
	* np. czy używa się ORM
* Warto skonsultować trwałość danych wcześniej
* Komunikacja tylko przez teams i spotkania tylko na teams
* Do wypełnienia test na drugie ćwiczenia
	* 10 minut

## Oprogramowanie
* Robert Nowak
* Ważne są wykorzystywane narzędzia
	* oceniane repozytorium kodu
* Wszystko opisane w dokumencie