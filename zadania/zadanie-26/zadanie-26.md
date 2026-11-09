
# Zadanie 26 – Analiza i poprawa Jenkinsfile

## Cel zadania

Celem zadania była analiza istniejącego pliku Jenkinsfile,
znalezienie błędów oraz przygotowanie poprawionej konfiguracji
potoku CI/CD w Jenkinsie.

## Znalezione błędy

### 1. Niepoprawna nazwa sekcji steps

Oryginalny zapis:
`stesp {`

Problem:
Niepoprawna nazwa sekcji powoduje błąd składniowy
w deklaratywnym potoku Jenkins.

Rozwiązanie:
Zmieniono `stesp` na `steps`.

### 2. Niepoprawna komenda npm build

Oryginalny zapis:
`npm build`

Problem:
Komenda nie uruchamia standardowo skryptu budowania
zdefiniowanego w package.json.

Rozwiązanie:
Zmieniono na:
`npm run build`

### 3. Nieprawidłowe umiejscowienie when

Oryginalny zapis:
Sekcja `when` znajdowała się po sekcji `steps`
w etapie Deploy.

Problem:
W deklaratywnym Jenkins Pipeline dyrektywę `when`
należy umieścić przed `steps`.

Rozwiązanie:
Przeniesiono `when` przed `steps`.

## Pozostałe elementy

- `npm install` – instaluje zależności projektu.
- `npm test` – uruchamia testy.
- `docker build -t myapp .` – buduje obraz Docker.
- `docker push myapp:latest` – wysyła obraz do rejestru.
- `branch 'master'` – ogranicza etap Deploy do gałęzi master.

## Rezultat

Przygotowano poprawioną konfigurację Jenkinsfile.
Pipeline zawiera trzy etapy:

1. Build – instalacja zależności i budowanie aplikacji.
2. Test – uruchamianie testów.
3. Deploy – budowanie i publikowanie obrazu Docker.

Poprawki usuwają zidentyfikowane błędy składniowe
i konfiguracyjne.
