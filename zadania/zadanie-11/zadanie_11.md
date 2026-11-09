Pewnie! Pokażę Ci krok po kroku, jak napisać test jednostkowy dla funkcji sum(a, b) przy użyciu Jest.

1. Czym jest Jest?
Jest to framework do testowania kodu JavaScript, stworzony przez Meta.

Pozwala m.in. na:

Pisanie testów jednostkowych (Unit Tests).

Sprawdzanie, czy funkcje zwracają oczekiwane wyniki.

Weryfikowanie wyjątków i błędów.

Generowanie raportów z testów.

Uruchamianie testów automatycznie.

Przykładowo możemy sprawdzić, czy sum(2, 3) zwraca 5.

2. Struktura projektu
Utwórzmy prosty projekt o następującej strukturze:


text
jest-project/
│
├── package.json
│
├── src/
│   └── sum.js
│
└── tests/
    └── sum.test.js
src/sum.js – funkcja, którą chcemy przetestować.

tests/sum.test.js – plik zawierający testy jednostkowe.

package.json – konfiguracja projektu i zależności.

3. Instalacja Jest
Najpierw utwórz katalog projektu:


bash
mkdir jest-project
cd jest-project
Zainicjuj projekt Node.js:


bash
npm init -y
Zainstaluj Jest jako zależność developerską:


bash
npm install --save-dev jest
4. Kod funkcji – sum.js
Utwórz plik src/sum.js:


javascript
function sum(a, b) {
  return a + b;
}

module.exports = sum;
module.exports pozwala udostępnić funkcję innym plikom, np. testom.

5. Napisanie testu jednostkowego
Utwórz plik tests/sum.test.js:


javascript
const sum = require('../src/sum');

test('dodaje dwie liczby', () => {
  expect(sum(2, 3)).toBe(5);
});
Wyjaśnienie poszczególnych elementów
require('../src/sum') – importuje testowaną funkcję.

test() – definiuje pojedynczy test.

expect() – określa wartość, którą chcemy sprawdzić.

toBe(5) – sprawdza, czy wynik jest równy 5.

Możemy również dodać więcej testów:


javascript
const sum = require('../src/sum');

test('dodaje dwie liczby dodatnie', () => {
  expect(sum(2, 3)).toBe(5);
});

test('dodaje liczby ujemne', () => {
  expect(sum(-2, -3)).toBe(-5);
});

test('dodaje zero', () => {
  expect(sum(5, 0)).toBe(5);
});

test('dodaje liczbę dodatnią i ujemną', () => {
  expect(sum(10, -5)).toBe(5);
});
6. Konfiguracja package.json
Otwórz plik package.json i dodaj skrypt test w sekcji scripts:


json
{
  "scripts": {
    "test": "jest"
  }
}
Nie musisz usuwać pozostałych pól wygenerowanych przez npm init.

7. Uruchomienie testów
W terminalu, w głównym katalogu projektu, wpisz:


bash
npm test
Jeżeli wszystko działa poprawnie, zobaczysz wynik podobny do tego:

Wynik testów Jest

PASS

text
PASS tests/sum.test.js

 ✓ dodaje dwie liczby

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Wszystkie testy zakończone sukcesem!

8. Podsumowanie – jak działa test jednostkowy?
Cały proces wygląda następująco:

1. Funkcja sum(a, b)

Kod, który chcemy przetestować

2. Plik sum.test.js

Przekazujemy argumenty 2 i 3

3. expect(sum(2, 3)).toBe(5)

Jest porównuje wynik z oczekiwanym 5

PASS
4. Test zakończony sukcesem

Najważniejsze do zapamiętania:

test() – tworzy test.

expect() – wskazuje, co sprawdzamy.

toBe() – porównuje wynik z oczekiwaną wartością.

npm test – uruchamia testy.

To podstawy testowania jednostkowego w JavaScript. Kolejnym krokiem może być poznanie describe(), beforeEach() oraz testowania sytuacji brzegowych.