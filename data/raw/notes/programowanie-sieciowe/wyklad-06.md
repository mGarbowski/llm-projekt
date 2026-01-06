# Protokół HTTP (2024-11-28)
* Nie wymaga przechowania informacji o stanie sesji przez komunikujące się strony
	* bezstanowy
	* łatwiejszy w implementacji
	* bardziej niezawodny
* Uproszczony schemat korzystania przez przeglądarkę
	* Użytkownik wpisuje adres URL
	* Klient - DNS lookup, określa IP
	* K - wysłanie `GET / HTTP/1.1 \r\n\r\n`
	* Serwer - decyduje jak obsłużyć żądanie
	* S - wysyła nagłówek odpowiedzi i opcjonalnie dane
	* K, S - sesja TCP jest zamykana (jest możliwość nie zamykać od razu)

```
mgarbowski@yoga:~$ telnet www.elka.pw.edu.pl 80
Trying 194.29.160.96...
Connected to www.elka.pw.edu.pl.
Escape character is '^]'.
GET / HTTP/1.1

HTTP/1.1 400 Bad Request
Server: nginx/1.20.1
Date: Thu, 28 Nov 2024 07:38:28 GMT
Content-Type: text/html
Content-Length: 157
Connection: close

<html>
<head><title>400 Bad Request</title></head>
<body>
<center><h1>400 Bad Request</h1></center>
<hr><center>nginx/1.20.1</center>
</body>
</html>
Connection closed by foreign host.
```

## Budowa

```
Full-Request = 
	Request-Line
	* (General-Header | Request-Header | Entity-Header)
	CRLF
	[Entity-Body]

Full-Response = 
	Status-Line
	* (General-Header | Response-Header | Entity-Header)
	CRLF
	[Entity-Body]

```

* Entity-Body - przesyłany dokument
	* opcjonalny
	* tekstowy lub binarny
* Entity-Header
	* odnosi się do przesyłanych danych
	* ContentType
	* ContentLength

## URL, URI, URN
* Uniform Resource Identifier
	* różne typy zasobów
	* dowolny schemat
	* dokument, usługa, ...
	* identyfikator - napis ASCII
* Uniform Resource Locator
	* podzbiór URI
	* identyfikuje i lokalizuje zasób
	* określa zasób przez sposób dostępu (np. http)
	* używa schematu opisującego protokół dostępu
	* np. `https://www.w3.org/index.html`
	* `schemat domena[:port] ścieżka parametry[#kotwica]`
* Uniform Resource Name
	* podzbiór URN
	* identyfikuje zasób
	* nie opisuje lokalizacji i sposobu dostępu
	* trwała i unikalna nazwa
	* niezależna od lokalizacji
	* np. `isbn:`

### URL w HTTP i HTTPS
* Opcjonalny login
	* username i hasło, `@`
* Opcjonalne query
* Wybrane znaki ASCII
	* znaki bezpieczne
	* znaki specjalne
### URL escape
* `escape = "%" HEX HEX`
* żeby zawrzeć znak, który ma specjalne znaczenie
* spacje, nie ASCII

### Przykładowy URL phishingowy
* Wtkorzystanie logowanie z hasłem w URLu

## Polecenia HTTP (method)
* `GET` - pobierz dane
* `HEAD` - jak `GET` ale zwracany tylko nagłówek
	* przydatne jeśli dokument jest duży
	* zamiast pobierać można użyć dokumentu z cache
* `POST` - zgłoś dane do przetworzenia przez URL
	* pozwala na przesłanie większej ilości danych
	* wysyłanie danych do aplikacji
	* mniejsze dane można przesłać prez `GET` jako query
* `PUT` - zmień zawartość URL
* `DELETE` - usuń dane
* `CONNECT` - przełącz proxy w inny tryb
	* przełączenie na protokół FTP
	* zmiana wersji protokołu z 1.1 na 2
	* zmiana na sesję szyfrowaną (TLS)
* `TRACE` - nieużywany, zwróć otrzymane żądanie jako entity
* `OPTIONS` - nieużywany - zwróć dostępne opcje

## Protokół WEBDav
* Podobne metody do HTTP
* Do modyfikowania dokumentów
	* HTTP pierwotnie miał służyć do edytowania dokumentów
	* obecnie nieużywane, robi się to pośrednio przez aplikacje webowe używające HTTP

## Wersje
* 0.9
* 1.0
* 1.1
* 2
* 3 - wersja 2 z transportem QUIC
* Ruch głównie w 1.1 i 2

## Kody odpowiedzi
* `1xx` - Informational
	* rzadko używane
	* np. zmiana protokołu
* `2xx` - Success
	* polecenie zrozumiane, wykonanie poprawnie
	* 200 - OK
	* 201 - Created
	* 202 - Accepted
	* 204 - No content
	* 206 - Partial Content
* `3xx` - Redirection
	* należy podjąć dodatkowe czynności w celu realizacji polecenia
	* ...
* `4xx` - Client Error
	* błąd polecenia, prawdopodobnie błąd składni po stronie klienta
	* 400 - Bad request
	* 401 - Unauthorized
	* 403 -Forbidden
	* 404 - Not found
* `5xx` - Server Error
	* serwer nie jest w stanie obsłużyć połączenia
	* jeśli proces serwera padnie to nie odpowie, system operacyjny odeśle TCP RST
	* w przypadku jeśli inny proces obsługuje żądanie, serwer HTTP może wykryć że coś jest nie tak i odesłać `5xx`
	* 500 - Internal server error
	* 501 - Not implemented - możliwe że klient wysłał źle sformatowane żądanie
	* 503 - Service unavailable

## Wybrane nagłówki

### Ogólnego przeznaczenia
* Date
	* znacznik czasowy z dokładnością do sekundy i strefą czasową
	* używany do określenia wazności dokumentów
	* istotne dla cache i cookies
* Transfer-Encoding
	* chunked
	* nie mylić z Content-Encoding
	* serwer odpowiada, że odsyłane dane będą podzielone na części
	* długość części zapisana szestnastkowo, porcja danych, CRLF
	* na końcu 0
	* browser comforting - np. przy długim przetwarzaniu najpierw odeśle dane do wygenerowania paska ładowania
	* teraz powszechnie używany do streamingu
* Cache-control
	* zarządzanie
* `Connection: Keep-alive`
	* zestawianie jednego połączenia dla każdego polecenia HTTP jest bardzo niewydajne
	* można przesyłać wiele poleceń HTTP jednym połączeniem TCP
	* dalej protokół jest bezstanowy, zapytania są niezależne od siebie tylko korzystają z tego samego połączenia
	* koniec połączenia przez `Connection: close`

### Nagłówki żądania
* Accept - przyjmowane typy danych
	* serwer powinien to weryfikować
	* `Accept: text/*, image/gif, image/jpg`
* Accept-Charset
* Accept-Encoding
	* algorytmu kompresji
	* dozwolone gzip, compress, deflate
* Kodowanie znaków
	* zgodne z mime
	* np. UTF-8
* Accept-Language
	* zgodne z kodami ISO639
	* wzięte np z ustawień przeglądarki
	* np. en, pl
* Host
	* wymagane
	* określenie serwera w przypadku gdy do jednego adresu IP przypisano wiele serwerów wirtualnych
	* `Host: www.w3.org`
	* jeśli nie zostanie podane, a serwer obsługuje wiele adresów domenowych to serwer odpowie błędem
* User-Agent
	* nazwa i wersja przeglądarki
	* pozwala na dynamiczne dostosowanie zwracanej zawartości do przeglądarki
* Referer
	* poprzedni URL
	* przydatne w statystykach
	* pozwala na określenie ścieżki klienta
	* kluczowe dla e-commerce - jakie hasło googlował użytkownik który wszedł na stronę sklepu

### Nagłówki odpowiedzi
* Server
	* serwer się przedstawia
	* często nie chcemy podawać
* Location
	* przekierowanie
	* np. w parze z kodem `301`
	* po reorganizacji serwisów
	* federacja - wiele serwisów nie w pełni zintegrowanych, użytkownika na raz uwierzytelnia się na wielu serwerach

### Nagłówki zawartości
* Content-Type
	* typ zwracanej treści
	* zgodny z MIME
	* np. `text/html`
* Content-Length
	* długość Entity-Body w bajtach
	* szczególnie ważne przy keep-alive - klient musi przeczytać dokładnie tyle
	* bez keep-alive nie ma problemu, klient czyta do skutku
	* dla `HEAD` zwraca to samo co dla `GET`
	* serwer musi z góry wiedzieć ile będzie danych - problematyczne przy dynamicznie generowanej treści - musi najpierw zbuforować wszystko
* Content-Encoding
* Content-Disposition
	* np. dla Attachment przeglądarka nie wyświetla go, tylko otwiera dialog do pobrania
* Content-Language
* Content-MD5
* Expires
* Last-Modified
	* dla optymalizacji cache'owania