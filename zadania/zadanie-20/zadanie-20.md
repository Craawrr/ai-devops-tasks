
# Zadanie 20 – Generowanie wyrażeń regularnych

## 1. Opis problemu

Celem zadania jest stworzenie wyrażenia regularnego
(Regex), które sprawdza poprawność adresów IPv4.

Prawidłowy adres IPv4:
- Składa się z czterech liczb (oktetów).
- Każdy oktet jest oddzielony kropką.
- Każdy oktet mieści się w zakresie 0–255.
- Nie zawiera niepotrzebnych zer na początku liczby.

## 2. Wyrażenie regularne

```regex
^(?:(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$
```

## 3. Wyjaśnienie działania regex

### Początek i koniec adresu

- `^` – oznacza początek tekstu.
- `$` – oznacza koniec tekstu.

Dzięki temu cały tekst musi być poprawnym adresem IPv4.

### Zakres pojedynczego oktetu

`25[0-5]` – dopasowuje liczby od 250 do 255.

`2[0-4]\d` – dopasowuje liczby od 200 do 249.

`1\d{2}` – dopasowuje liczby od 100 do 199.

`[1-9]?\d` – dopasowuje liczby od 0 do 99.

Znak `|` oznacza alternatywę (LUB).

### Kropka

`\.` – oznacza dosłowną kropkę oddzielającą oktety.

### Powtarzanie

`(?:(?:...)\.){3}` – dopasowuje trzy pierwsze oktety wraz z kropkami.

Ostatni oktet jest dopasowywany osobno.

W rezultacie otrzymujemy dokładnie cztery oktety.

## 4. Przykłady testów

| Adres IPv4 | Wynik | Uzasadnienie |
|---|---|---|
| 192.168.1.1 | TRUE | Poprawny adres |
| 127.0.0.1 | TRUE | Poprawny adres |
| 255.255.255.255 | TRUE | Maksymalne wartości |
| 0.0.0.0 | TRUE | Minimalne wartości |
| 256.1.1.1 | FALSE | Oktet przekracza 255 |
| 192.168.1 | FALSE | Tylko trzy oktety |
| 192.168.1.999 | FALSE | Oktet przekracza 255 |
| 192.168.01.1 | FALSE | Zero na początku oktetu |
| abc.def.ghi.jkl | FALSE | Niepoprawne znaki |
| 192.168.1.1.1 | FALSE | Pięć oktetów |

## 5. Implementacja

Funkcja `isValidIPv4(ip)` wykorzystuje metodę
`.test()` do sprawdzenia, czy przekazany tekst
pasuje do wyrażenia regularnego.

Zwraca:
- `true` – jeżeli adres jest poprawny.
- `false` – jeżeli adres jest niepoprawny.

## 6. Uruchomienie

W terminalu należy wykonać:

```bash
node ipv4-validator.js
```

## 7. Podsumowanie

Zadanie pozwoliło przećwiczyć:
- Tworzenie wyrażeń regularnych.
- Alternatywy i grupy w regex.
- Zakresy znaków i kwantyfikatory.
- Walidację danych w JavaScript.
- Testowanie poprawności adresów IPv4.
