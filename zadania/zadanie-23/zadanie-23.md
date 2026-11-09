
# Zadanie 23 – Analiza złożoności algorytmu

## 1. Cel zadania

Celem zadania było przeanalizowanie algorytmu
wyszukującego pary liczb w tablicy, których suma
jest równa podanej wartości `targetSum`.

## 2. Oryginalny algorytm

Oryginalny algorytm wykorzystuje dwie zagnieżdżone
pętle `for`, aby sprawdzić wszystkie możliwe pary
elementów tablicy.

### Złożoność czasowa

O(n²) – algorytm sprawdza wszystkie możliwe pary
elementów tablicy.

### Złożoność pamięciowa

O(1) pamięci pomocniczej oraz O(k) na przechowywanie
wynikowych par.

## 3. Zoptymalizowany algorytm

W zoptymalizowanej wersji zastosowano strukturę Map.

Algorytm zapamiętuje odwiedzone liczby i liczbę ich
wystąpień. Dla każdej kolejnej liczby oblicza
dopełnienie:

complement = targetSum - num

Następnie sprawdza, ile razy dopełnienie wystąpiło
wcześniej. Pozwala to znaleźć wszystkie pasujące
pary bez sprawdzania każdej kombinacji.

### Złożoność czasowa

O(n + k) średnio, gdzie:
- n – liczba elementów tablicy,
- k – liczba znalezionych par.

### Złożoność pamięciowa

O(n) pamięci pomocniczej na strukturę Map oraz
O(k) na przechowywanie wyników.

## 4. Porównanie algorytmów

| Właściwość | Oryginalny | Zoptymalizowany |
|---|---|---|
| Czasowa | O(n²) | O(n + k) |
| Pamięć pomocnicza | O(1) | O(n) |
| Struktura danych | Tablica | Map |

## 5. Zalety optymalizacji

- Znacznie szybsze działanie dla dużych tablic.
- Brak konieczności sprawdzania wszystkich kombinacji.
- Wykorzystanie szybkiego wyszukiwania w Map.
- Poprawna obsługa powtarzających się liczb.
- Zachowanie wszystkich par, również tych
  zawierających identyczne wartości.

## 6. Wnioski

Zoptymalizowany algorytm jest wydajniejszy czasowo
od wersji oryginalnej.

Oryginalna wersja ma złożoność kwadratową O(n²),
natomiast zoptymalizowana osiąga średnio O(n + k).

Optymalizacja wymaga dodatkowej pamięci na strukturę
Map, ale pozwala znacząco ograniczyć liczbę operacji.

W przypadku dużych tablic jest to korzystna
wymiana pamięci na szybkość działania.
