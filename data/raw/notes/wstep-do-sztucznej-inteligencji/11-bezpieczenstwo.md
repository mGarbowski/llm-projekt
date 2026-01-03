# Bezpieczeństwo systemów AI
Bezpieczeństwo w sensie _safety_ nie w sensie cybersecurity, tylko w kontekście krzywdy wyrządzanej człowiekowi przez system AI.

System krytyczny pod względem bezpieczeństwa to taki, którego nieprawidłowe działanie może podować śmierć, szkody dla zdrowia lub środowiska.

Standard dla motoryzacji przewiduje 5-stopniową skalę autonomii pojazdu

* Bezpieczeństwo funkcjonalne (FuSa)
	* Zwykłe błędy software'u
	* Losowe błędy hardware'u
* Safety of Intended Functionality (SOTIF)

Wymagany poziom niezawodności dla klasyczynch systemów to błąd nie częściej niż co 100mln godzin

* Standard ISO 26262
	* Nie dotyczy i nie był pisany z myślą o systemach AI
	* Niektóre wymagania, np. statyczną analizę można zastosować do wyuczonych modeli
	* Systematyczne błędy w softwarze
* Standard ASIL - Automotive Safety Integrity Level
	* Dla różnych poziomów są określone wymagania do testowania funkcjonalności
* SOTIF
	* jakość, kompletność danych treningowych


Kompilatory do C i C++ są odpowiednio certyfikowane i są standardowo wykorzystywane (z odpowiednimi ograniczeniami). Wszystkie narzędzia też muszą być poddane certyfikacji (programy to zarządzania testami, statycznej analizy kodu itd.), często trzeba zabulić.

Istotne jest pojęcie wyjaśnialnej sztucznej inteligencji

Anegdota o systemie wykrywania czołgów