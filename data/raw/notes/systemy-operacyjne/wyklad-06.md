# Wykład 06 (2023-11-07)
Kolokwium będzie na ostatnim wykładzie przed świętami.
Będzie podany zakres pytań
Obejmuje te slajdy, które zostały omówione

`fork` i `exec` są oddzielnymi wywołaniami, żeby móc ustawić pewne parametry 
dla nowego procesu przed jego uruchomieniem.

`$1`, `$2` itd zawsze dotyczą najwęższego kontekstu (czyli np funkcji jeśli jesteśmy w ciele funkcji)

## Metaznaki
* `*` - każdy znak poza `/`
* `?` - jeden dowolny znak
* `\` - traktuj literalnie następny metaznak

Każdy plik identyfukuje jego i-node (tak np można usunąć plik o krzakowatej nazwie)

Metaznaki jak `*` są rozwijane przez shella jeszcze przed uruhchomieniem programu

kolejność substytucji ...

Nie ma tablic w shellu, można je emulować przez odpowiednie, dynamicznie wyliczane nazwy zmiennych

Argumenty które nie są nazwami plików powinny być poprzedzone znakiem `-`

Nawiasy okrągłe grupują komendy, które będą wykonywane jako samodzielny proces

Końcem komendy są znaki `<NL>` `;` `&`

Shell może wykonywać procesy w tle lub w pierwszym planie (bash pozwala, shell minixa nie)

`nohup polecenie &` - odpali proces w tle, nie przerwie się po przerwaniu sesji ssh
W praktyce przydaje się serwer terminala jak `screen` albo `tmux`

operatory `&&` i `||`
