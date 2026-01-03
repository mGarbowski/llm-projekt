# Wykład 03 (2023-10-17)


## Przerwania
Przerwanie nie jest sytuacją wyjątkową, jest jego normalnym elementem
Jest mechanizmem, a nie sygnalizacją błędu

Próby dzielenia przez 0, niedozwolonego odwołania do pamięci kończą się wyjątkiem (które mogą być realizowane jako przerwania)
Operacje IO są o wiele rzędów wielkości wolniejsze od operacji procesora
proces oddaje czas procesora do innych procesów i przejmuje kontrolę ponownie, po zgłoszeniu przerwania przez urządzenie IO (sygnalizujące gotowość)

procedura obsługi przerwania może zmienić stan procesu z oczekiwania na gotowość do wykonania

Nietypowe przerwania to np przerwania zegarowe


## Koncepcje związane z systemem operacyjnym
* proces
    * przestrzeń adresowa procesów
    * tablica procesów
    * obraz procesu
    * procesy potomne
    * komunikacja międzyprocesowa
    * sygnały
    * identyfikatory procesu, grupy, właściciela
* blokady
* zarządzanie pamięcią
* I/O
* pliki
    * katalogi
    * ścieżki dostępu
    * katalog główny
    * katalog bieżący
    * deskryptor pliku
    * system plików
    * pliki specjalne
    * urządzenia blokowe i znakowe
    * potoki
* bezpieczeństwo
    * bity rwx
    * listy kontroli dostępu
* interpreter poleceń

cd nie może być oddzielnym procesem, bo nie może ingerować w aktywny katalog innego procesu (jest wewnętrznym poleceniem shella)
