
```python
# kod oryginalny
def find_duplicates(list_of_items):
    duplicates = []
    for i in range(len(list_of_items)):
        for j in range(i+1, len(list_of_items)):
            if list_of_items[i] == list_of_items[j] and list_of_items[i] not in duplicates:
                duplicates.append(list_of_items[i])
    return duplicates

# kod zoptymalizowany
def find_duplicates(list_of_items):
    seen = set()
    duplicates = set()

    for item in list_of_items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)

```
# Porównanie wydajności
Tak\! Twój kod można znacząco zoptymalizować. Obecna implementacja wykorzystuje dwie zagnieżdżone pętle, przez co jej złożoność czasowa wynosi O(n²). Dodatkowo sprawdzanie `not in duplicates` wymaga kolejnego przeszukiwania listy.

Można to rozwiązać znacznie wydajniej, wykorzystując strukturę danych `set` (zbiór).

## 1. Zoptymalizowana wersja

python

```python
def find_duplicates(list_of_items):
    seen = set()
    duplicates = set()

    for item in list_of_items:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)
```

Złożoność czasowa: O(n) średnio.

Złożoność pamięciowa: O(n).

## 2. Jak działa rozwiązanie?

- `seen` przechowuje elementy, które już napotkaliśmy.
- `duplicates` przechowuje elementy, które wystąpiły więcej niż jeden raz.
- Dla każdego elementu sprawdzamy, czy znajduje się już w `seen`.
- Jeśli tak, dodajemy go do `duplicates`.
- Jeśli nie, zapisujemy go w `seen`.

Przykład:

python

```python
items = [1, 2, 3, 2, 4, 5, 1, 3]

print(find_duplicates(items))
```

Wynik:

python

```python
[1, 2, 3]
```

Kolejność elementów w wyniku nie jest gwarantowana, ponieważ używamy zbioru.

## 3. Wersja zachowująca kolejność występowania

Jeżeli zależy Ci na zachowaniu kolejności duplikatów zgodnej z oryginalną listą, proponuję następującą implementację:

python

```python
def find_duplicates(list_of_items):
    seen = set()
    duplicates = []
    duplicates_set = set()

    for item in list_of_items:
        if item in seen:
            if item not in duplicates_set:
                duplicates.append(item)
                duplicates_set.add(item)
        else:
            seen.add(item)

    return duplicates
```

Przykład:

python

```python
items = [3, 1, 2, 3, 2, 1, 4]

print(find_duplicates(items))
```

Wynik:

python

```python
[3, 1, 2]
```

## 4. Porównanie wydajności

| Właściwość | Oryginalny kod | Zoptymalizowany kod |
| --- | --- | --- |
| Złożoność czasowa | O(n²) | O(n) średnio |
| Złożoność pamięciowa | O(n) | O(n) |
| Zagnieżdżone pętle | Tak | Nie |
| Zachowanie kolejności | Tak | Zależnie od wersji |

Moja rekomendacja: Wersja nr 3 jest najlepszym kompromisem, ponieważ zapewnia średnią złożoność czasową O(n), eliminuje zbędne przeszukiwanie listy i zachowuje kolejność duplikatów.

Uwaga: Obie zoptymalizowane wersje zakładają, że elementy listy są hashowalne (np. liczby, napisy lub krotki zawierające hashowalne elementy). Jeśli lista zawiera słowniki lub inne listy, potrzebne będzie inne rozwiązanie.