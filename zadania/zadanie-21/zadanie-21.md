Zadanie 21: Transformacja danych JSON do CSV
1. Cel zadania

Celem zadania było przekształcenie danych użytkowników z formatu JSON do formatu CSV oraz przygotowanie dokumentacji opisującej proces konwersji.

2. Wykorzystane pliki
users.json – oryginalne dane w formacie JSON.
users.csv – dane przekonwertowane do formatu CSV.
zadanie-21.md – dokumentacja procesu transformacji.
3. Proces konwersji
Przygotowano dane użytkowników w formacie JSON.
Odczytano tablicę users.
Dla każdego użytkownika pobrano pola: id, name, email oraz roles.
Nagłówki CSV ustawiono zgodnie z wymaganiami.
Tablicę roles przekształcono w tekst, łącząc jej elementy przecinkami.
Wygenerowano plik users.csv.
4. Przykład wyniku CSV
csv
id,name,email,roles
1,Jan Kowalski,jan@example.com,"admin,user"
2,Anna Nowak,anna@example.com,user

5. Potencjalne wyzwania
Tablice w JSON

JSON obsługuje tablice, natomiast CSV jest formatem tabelarycznym. Dlatego tablicę roles trzeba odpowiednio przedstawić w jednej komórce.

W tym zadaniu zastosowano połączenie elementów tablicy przecinkami, np. admin,user.

Znaki specjalne

Nazwy lub inne wartości mogą zawierać przecinki, cudzysłowy albo znaki nowej linii. W takich przypadkach należy stosować odpowiednie reguły cytowania CSV.

Brakujące wartości

Jeżeli niektóre obiekty nie zawierają określonych pól, należy zdecydować, czy pozostawić puste komórki, czy zastosować wartości domyślne.

Utrata struktury danych

CSV nie przechowuje typów danych ani zagnieżdżonych struktur JSON. Konwersja może więc powodować utratę części informacji.

6. Podsumowanie

Dane zostały przekształcone z JSON do CSV. Zachowano wszystkie wymagane kolumny: id, name, email i roles.

Przyjęta metoda pozwala na łatwe otwieranie danych w arkuszach kalkulacyjnych, takich jak Microsoft Excel lub Google Sheets.