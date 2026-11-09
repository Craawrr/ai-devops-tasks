
# Zadanie 27 – Wyjaśnienie zależności między etapami pipeline Jenkins

## 1. Wprowadzenie

Pipeline CI/CD w Jenkinsie automatyzuje proces budowania, testowania i wdrażania aplikacji webowej.

Każdy etap jest zależny od poprawnego zakończenia poprzednich etapów. Dzięki temu błędny kod nie trafia na środowisko produkcyjne.

## 2. Opis poszczególnych etapów

### 1. Checkout kodu

Jenkins pobiera najnowszą wersję kodu źródłowego z repozytorium Git.

Jest to pierwszy etap pipeline'u. Wszystkie kolejne operacje wykonywane są na pobranym kodzie.

### 2. Budowanie aplikacji

Następuje kompilacja kodu oraz pobranie wymaganych zależności.

Jeśli budowanie zakończy się błędem, pipeline zostaje przerwany.

### 3. Testy jednostkowe

Sprawdzane są pojedyncze komponenty aplikacji.

Testy pozwalają wykryć błędy w logice programu jeszcze przed dalszym przetwarzaniem.

### 4. Analiza statyczna kodu

Kod jest analizowany bez jego uruchamiania.

Celem jest wykrycie potencjalnych błędów, niezgodności ze standardami programowania oraz problemów z jakością kodu.

Przykładowe narzędzia:
- SonarQube
- ESLint
- Checkstyle

### 5. Skanowanie bezpieczeństwa

Sprawdzane są zależności aplikacji oraz kod pod kątem znanych podatności.

Przykładowe narzędzia:
- OWASP Dependency-Check
- Snyk
- Trivy

W przypadku wykrycia krytycznych problemów pipeline może zostać zatrzymany.

### 6. Budowanie obrazu Docker

Po pomyślnym przejściu wcześniejszych etapów Jenkins buduje obraz Docker.

Obraz zawiera aplikację oraz jej wymagane środowisko uruchomieniowe.

Dzięki temu aplikacja może działać w spójnym środowisku.

### 7. Testy integracyjne

Sprawdzana jest współpraca poszczególnych komponentów aplikacji, np. komunikacja z bazą danych i zewnętrznymi usługami.

Testy wykonywane są na przygotowanym środowisku testowym z wykorzystaniem obrazu Docker.

### 8. Wdrożenie na środowisko Staging

Jeżeli testy integracyjne zakończą się sukcesem, aplikacja zostaje wdrożona na środowisko staging.

Środowisko to odwzorowuje konfigurację produkcyjną i umożliwia przeprowadzenie dodatkowych testów.

### 9. Testy akceptacyjne

Na środowisku staging wykonywane są testy sprawdzające, czy aplikacja spełnia wymagania biznesowe i działa prawidłowo.

Negatywny wynik testów blokuje wdrożenie produkcyjne.

### 10. Wdrożenie na środowisko Production

Po pozytywnej akceptacji aplikacja zostaje wdrożona na środowisko produkcyjne.

Na tym etapie aplikacja staje się dostępna dla użytkowników końcowych.

### 11. Weryfikacja wdrożenia

Ostatni etap polega na sprawdzeniu poprawności działania aplikacji po wdrożeniu.

Może obejmować:
- testy dostępności aplikacji,
- sprawdzenie endpointów API,
- analizę logów,
- monitorowanie błędów.

## 3. Zależności między etapami

Pipeline działa w określonej kolejności:

1. Checkout dostarcza kod źródłowy.
2. Budowanie przygotowuje aplikację do testowania.
3. Testy jednostkowe sprawdzają poprawność poszczególnych komponentów.
4. Analiza statyczna ocenia jakość kodu.
5. Skanowanie bezpieczeństwa wykrywa potencjalne zagrożenia.
6. Budowanie obrazu Docker przygotowuje artefakt wdrożeniowy.
7. Testy integracyjne sprawdzają współpracę komponentów.
8. Staging umożliwia sprawdzenie aplikacji w warunkach zbliżonych do produkcyjnych.
9. Testy akceptacyjne weryfikują wymagania biznesowe.
10. Production udostępnia aplikację użytkownikom.
11. Weryfikacja wdrożenia potwierdza poprawność działania aplikacji.

Każdy etap stanowi warunek przejścia do kolejnego. W przypadku błędu pipeline zostaje zatrzymany, co zapobiega wdrażaniu niepoprawnej wersji aplikacji.

## 4. Korzyści z wykorzystania Jenkins CI/CD

- Automatyzacja procesu wdrażania.
- Szybsze wykrywanie błędów.
- Poprawa jakości kodu.
- Zwiększenie bezpieczeństwa aplikacji.
- Powtarzalność procesu budowania i wdrażania.
- Ograniczenie ryzyka błędów podczas wdrożeń produkcyjnych.

## 5. Podsumowanie

Jenkins CI/CD umożliwia automatyzację całego procesu dostarczania aplikacji webowej.

Zastosowanie kolejnych etapów kontroli jakości, testowania i bezpieczeństwa sprawia, że na środowisko produkcyjne trafia wyłącznie wersja aplikacji, która przeszła wymagane kontrole.
