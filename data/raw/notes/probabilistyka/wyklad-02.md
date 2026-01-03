# Prawdopodobieństwo warunkowe, niezależność zdarzeń

## Przykład 1
Rzucamy raz kostką sześcienną

a) Jaka jest szansa że wypadnie 4?
$$\Omega = \{1, 2, 3, 4, 5, 6\}$$
$$A = \{4\}$$
$$P(A) = \frac{|A|}{|\Omega|} = \frac{1}{6}$$
b) Wypadła parzysta liczba oczek, jaka jest szansa że jest to 4?
$$B = \{2, 4, 6 \}$$
$$
P(A|B) = \frac{P(A \cap B)}{P(B)} = 
\frac{\frac{1}{6}}{\frac{1}{2}} = 
\frac{1}{3}
$$

c) Wypadła liczba oczek większa od 2. Jaka jest szansa że wypadło 4?

$$
C = \{3, 4, 5, 6\}
$$
$$
P(A|C) = \frac{P(A \cap C)}{P(C)} = \frac{\frac{1}{6}}{\frac{4}{6}} = \frac{1}{4}
$$
## Prawdopodobieństwo warunkowe
Prawdopodobieństwo warunkowe zdarzenia $A \subset \Omega$ pod warunkiem zdarzenia $B \subset \Omega$ takiego, że $P(B) > 0$, definiujemy jako

$$
P(A|B) = \frac{P(A \cap B)}{P(B)}
$$
$$
P(A \cap B) = P(A|B) \cdot P(B)
$$
## Przykład 2
W urnie jest 5 białych i 7 czarnych kul. Wyjmujemy losowo jedną kulę po drugiej, bez zwracania, Obliczyć $P(C_1 \cap B_2 \cap C_3)$, gdzie:
* $B_i$ - w i-tym losowaniu wyjmujemy kulę białą
* $C_i$ - w i-tym losowaniu wyjmujemy kulę czarną

...drzewko...

$$
P(C_1 \cap B_2 \cap C_3) = 
P(C_1) \cdot P(B_2 | C_1) \cdot P(C_3 | B_2 \cap C_1) =
\frac{7}{12} \cdot \frac{5}{11} \cdot \frac{6}{10}
$$
## Twierdzenie
Jeśli zdarzenia A_1, A_2 ...

Wzór łańcuchowy
$$
P(A_1 \cap \ldots \cap A_n) =
P(A_1) \cdot P(A_2 | A_1) \cdot P(A_3 | A_1 \cap A_2) \cdot \ldots \cdot 
P(A_n | A_1 \cap \ldots \cap A_{n-1})
$$

Jeśli $P(B) > 0$, to dla dowolnego zdarzenia $A$
$$P(A|B) + P(A'|B) = 1$$
## Przykład 3
Ta sama urna, jakie jest prawdopodobieństwo, że w drugim losowaniu wyciągniemy białą kulę?

$$
P(B_2) = P(B_2 | B_1) \cdot P(B_1) +  P(B_2 | C_1) \cdot P(C_1)
$$
$$B_1 \cap C_1 = \varnothing$$
$$B_1 \cup C_1 = \Omega$$
## Prawdopodobieństwo całkowite

Przeliczalna rodzina zdarzeń $(A_n)_{n \in I}, I \subset \mathbb{N}$, takich, że $A_n \subset \Omega$ dla każdego $n \in I$, nazywamy rozbiciem $\Omega$, jeśli

$A_i \cap A_j = \varnothing$ dla $i \ne j$ 

$$
\bigcup_{n \in I} A_n = \Omega
$$
Dla dowolnego zdarzenia $A \subset \Omega$
$$
P(A) = \sum_{n \in I} P(A | A_n) \cdot P(A_n)
$$

## Przykład 4
Ile wynosi prawdopodobieństwo, że w pierwszym losowaniu wyciągnęliśmy kulę czarną, jeśli wiadomo, że w drugim losowaniu wyciągnęliśmy kulę białą?

$$
P(C_1 | B_2) = \frac{P(C_1 \cap B_2)}{P(B_2)}
= \frac
{P(C_1) \cdot P(B_2 | C_1)}
{P(B_2 | B_1) \cdot P(B_1) +  P(B_2 | C_1) \cdot P(C_1)}
$$

## Wzór Bayesa
Jeżeli ...

$$
P(A_k | A) = \frac{P(A|A_k) \cdot P(A_k)}{P(A)}
$$
$$
P(A) = \sum_{n \in I} P(A | A_n) \cdot P(A_n)
$$
## Niezależność zdarzeń
Zdarzenia $A \subset \Omega$ i $B \subset \Omega$ nazywamy niezależnymi jeśli
$$
P(A \cap B) = P(A) \cdot P(B)
$$
w przeciwnym wypadku $A$ i $B$ są zależne

Jeśli $P(B) > 0$, zdarzenia $A$ i $B$ są niezależne wtedy i tylko wtedy, gdy

$$
P(A | B) = P(A)
$$
Zdarzenia $A_1, A_2, \ldots, A_n$ są niezależne zespołowo ...

$$
P(A_{i_1} \cap \ldots \cap A_{i_k}) = P(A_{i_1}) \cdot \ldots \cdot P(A_{i_k})
$$

Zdarzenia są niezależne parami, jeśli każde dwa z nich są niezależne

Np. zdarzenia $A$, $B$, $C$ są niezależne zespołowo jeśli
* Zdarzenia $A$, $B$, $C$ są niezależne parami
	* $P(A \cap B) = P(A) \cdot P(B)$
	* $P(A \cap C) = P(A) \cdot P(C)$
	* $P(B \cap C) = P(B) \cdot P(C)$
* $P(A \cap B \cap C) = P(A) \cdot P(B) \cdot P(C)$

## Schemat Bernouliego
Ciąg niezależnych powtórzeń tego samego doświadczenia o dwóch możliwych wynikach nazywanych umownie sukcesem i porażką. Poszczególne doświadczenia nazywamy próbami.

### Twierdzenie
Rozważmy schemat Bernouliego z prawdopodobieństwem sukcesu w jednej próbie równym $p$. Wtedy:
1. Prawdopodobieństwo, że w $n$ próbach zajdzie dokładnie $k$ sukcesów jest równe $\binom{n}{k} \cdot p^k \cdot (1-p)^{n-k}$
2. Prawdopodobieństwo, że pierwszy sukces pojawi się w k-tej próbie jest równe $(1-p)^{k-1} \cdot p$

## Przykład 5
Rzucamy wiele razy niesymetryczną monetą $(P(O) = 1/3)$
1. Ile wynosi prawdopodobieństwo, że w 10 rzutach dokładnie 3 razy wypadnie orzeł?
2. Ile wynosi prawdopodobieństwo, że pierwszy orzeł wypadnie w 10. rzucie?

$$
P(A) = \binom{10}{3} \cdot (\frac{2}{3})^7 \cdot (\frac{1}{3})^3
$$
$$
P(B) = (\frac{2}{3})^9 \cdot \frac{1}{3}
$$
Uwaga: z niezależności parami nie wynika niezależność zespołowa

