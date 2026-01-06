# Optymalizacja (ZPR- W14 -2021 01 19)
Nie ma narzutu w wektorze względem tablicy (tylko przez wyciągnięcie długości ale i tak należy grupować tablicę z rozmiarem)

-O3 może wygenerować więcej kodu niż -O2 stosując dzikie optymalizacje
ma znaczenie czy cały program mieści się w cache'u instrukcji na procesroze

`int[][]` vs `vector<vector<int>>`

Kompilator zamieni mnożenie przez stałą na shift - należy pisać normalne semantycznie wyrażenia matematyczne
Kompilator i tak zamienia te operacje na najbadziej wydajne

`const` umożliwia potężne optymalizacje
lokalna zmienna nie jest zmienną