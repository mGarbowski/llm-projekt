# Shell cd (2023-10-31)

Laboratorium z kompilacji jądra i wywołań systemowych będzie na 2 laby za 8 pkt
Wymogi czasowe określają prowadzący

`cat<<EOT` pozwala wbudować plik tekstowy do skryptu shellowego

`1>&2` przekierowanie stdout na stderr

Generalnie kolejność zadawania przekierowań nie ma znaczenia

`a <b >c` - uruchamia proces `a`, pobiera standardowe wejście z pliku `b` 
i zapisuje standardowe wyjście do pliku `c`
`a > c < b` działa tak samo

`a 2>/dev/null` - chowa wyjście diagnostyczne

`find . 2>&1 >/dev/null` - tylko strumień diagnostyczny pójdzie na wyjście
`find . >/dev/null 2>&1` - oba strumienie pójdą do /dev/null 
`cat >> x.txt` - append

Można podać wartości zmiennych środowiskowych które będą dostępne dla programu
`VAR=value command arg1 arg2`

Przykład `env-example.sh`
`GREETING="hello" ./env-example`

export - zmianna środowiskowa będzie dostepna dla podprocesów
