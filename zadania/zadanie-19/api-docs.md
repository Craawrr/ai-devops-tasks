Dokumentacja API – Lista użytkowników
Endpoint

GET /api/users

Opis

Endpoint służy do pobierania listy użytkowników z systemu. Obsługuje stronicowanie wyników oraz filtrowanie użytkowników według ich roli.

Parametry zapytania (Query Parameters)
Parametr	Typ	Wymagany	Domyślna wartość	Opis
page	integer	Nie	1	Numer strony wyników.
limit	integer	Nie	10	Liczba użytkowników na stronie. Maksymalna wartość: 100.
role	string	Nie	Brak	Filtruje użytkowników według określonej roli.
Przykładowe żądanie

Pobranie pierwszych 10 użytkowników:

http
GET /api/users?page=1&limit=10


Pobranie użytkowników z rolą administratora:

http
GET /api/users?page=1&limit=20&role=admin

Przykładowa odpowiedź

Status HTTP: 200 OK

json
{
  "users": [
    {
      "id": 1,
      "name": "Jan Kowalski",
      "email": "jan@example.com",
      "role": "admin"
    },
    {
      "id": 2,
      "name": "Anna Nowak",
      "email": "anna@example.com",
      "role": "user"
    }
  ],
  "pagination": {
    "page": 1,
    "limit": 10,
    "total": 2
  }
}


Uwaga: powyższy format odpowiedzi jest przykładowy, ponieważ dokładna struktura danych zwracanych przez API nie została określona.

Możliwe kody odpowiedzi
Kod HTTP	Znaczenie
200 OK	Lista użytkowników została pobrana pomyślnie.
400 Bad Request	Nieprawidłowe parametry zapytania.
401 Unauthorized	Brak uwierzytelnienia, jeśli endpoint wymaga autoryzacji.
403 Forbidden	Brak uprawnień do wykonania operacji.
500 Internal Server Error	Wewnętrzny błąd serwera.
Ograniczenia
Domyślny numer strony wynosi 1.
Domyślna liczba wyników wynosi 10.
Maksymalna liczba wyników na stronie wynosi 100.
Parametr role jest opcjonalny.
Niepoprawne wartości parametrów powinny być odpowiednio walidowane.