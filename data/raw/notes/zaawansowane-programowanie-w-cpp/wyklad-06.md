# ZPR- W07 -2020 11 17 Optymalizacja kodu
* Intuicja programisty nie działa
* Wszystkie rozważania co do wydajności należy opierać na pomiarach
* Żeby robić mikro-optymalizacje trzeba czytać wygenerowany kod asemblera
* `mov eax, ebx` - `eax = ebx`
* `mov eax, [rdi]` - `eax = *rdi`
* `mov eax, [rdi+rsi*4]`  - `eax = rdi[rsi*4]`
* http://godbolt.org
* Koszt `unique_ptr` nad użyciem gołego pointera jest żaden albo znikomy
* `shared_ptr` faktycznie ma narzut
	* generuje dużo kodu asemblerowego
	* mechanizmy synchronizacji
	* ma implikacje dla architektury aplikacji - rozmyta odpowiedzialność
	* nie należy go nadużywać