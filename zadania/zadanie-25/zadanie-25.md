
# Zadanie 25: Generowanie prostego Jenkinsfile

## 1. Cel zadania

Celem zadania było utworzenie prostego potoku CI/CD dla aplikacji Node.js
z wykorzystaniem Jenkins i deklaratywnej składni Pipeline.

Pipeline automatyzuje pobieranie kodu, instalowanie zależności,
uruchamianie testów, budowanie aplikacji oraz tworzenie i publikowanie
obrazu Docker.

## 2. Wyjaśnienie poszczególnych etapów

### 2.1. Checkout

```groovy
stage('Checkout') {
    steps {
        checkout scm
    }
}
```

Etap pobiera kod źródłowy z repozytorium Git.
Polecenie `checkout scm` wykorzystuje konfigurację repozytorium
ustawioną w zadaniu Jenkins.

Dzięki temu pipeline pracuje na aktualnej wersji kodu.

### 2.2. Install Dependencies

```groovy
stage('Install Dependencies') {
    steps {
        sh 'npm install'
    }
}
```

Etap instaluje wszystkie zależności aplikacji Node.js
zdefiniowane w pliku package.json.

Pakiety są pobierane i instalowane w środowisku wykonawczym Jenkinsa.

### 2.3. Run Tests

```groovy
stage('Run Tests') {
    steps {
        sh 'npm test'
    }
}
```

Etap uruchamia testy aplikacji.

Jeżeli testy zakończą się niepowodzeniem, Jenkins przerwie
dalsze wykonywanie pipeline'u.

Pozwala to uniknąć budowania i publikowania wadliwej aplikacji.

### 2.4. Build Application

```groovy
stage('Build Application') {
    steps {
        sh 'npm run build'
    }
}
```

Etap buduje aplikację przy użyciu skryptu build
zdefiniowanego w package.json.

W zależności od technologii może wygenerować pliki produkcyjne,
np. w katalogu dist lub build.

### 2.5. Build Docker Image

```groovy
stage('Build Docker Image') {
    steps {
        sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
    }
}
```

Etap tworzy obraz Docker na podstawie Dockerfile
znajdującego się w katalogu projektu.

Obraz otrzymuje nazwę oraz tag odpowiadający numerowi
aktualnego buildu Jenkinsa.

Dzięki temu można identyfikować poszczególne wersje aplikacji.

### 2.6. Push Docker Image

```groovy
stage('Push Docker Image') {
    steps {
        // Logowanie i publikowanie obrazu
    }
}
```

Etap odpowiada za publikowanie obrazu Docker w rejestrze Docker Hub.

Dane logowania pobierane są z bezpiecznego magazynu Jenkins Credentials.

Następnie wykonywane są operacje:

- Logowanie do Docker Hub.
- Oznaczenie obrazu nazwą użytkownika.
- Wysłanie obrazu do rejestru za pomocą docker push.
- Wylogowanie z rejestru.

Dzięki temu obraz jest dostępny do późniejszego wdrożenia.

## 3. Sekcja post

Sekcja post definiuje działania wykonywane po zakończeniu pipeline'u.

- success – wyświetla komunikat o powodzeniu.
- failure – wyświetla komunikat o błędzie.
- always – wykonuje się niezależnie od wyniku pipeline'u.

## 4. Najlepsze praktyki przy tworzeniu pipeline'ów Jenkins

1. **Bezpieczne przechowywanie danych**
   Nie należy umieszczać haseł i tokenów bezpośrednio w Jenkinsfile.
   Należy korzystać z Jenkins Credentials.

2. **Podział na etapy**
   Pipeline powinien składać się z czytelnych etapów,
   z których każdy realizuje konkretne zadanie.

3. **Automatyczne testowanie**
   Testy powinny być wykonywane przed budowaniem i publikowaniem obrazu.

4. **Wersjonowanie obrazów**
   Warto stosować unikalne tagi, np. numer buildu lub identyfikator commita,
   zamiast polegać wyłącznie na tagu latest.

5. **Kontrola błędów**
   Pipeline powinien przerywać wykonywanie po błędzie krytycznego etapu.

6. **Ograniczanie uprawnień**
   Jenkins powinien korzystać tylko z uprawnień niezbędnych do wykonania zadania.

7. **Powtarzalność buildów**
   Warto używać pliku package-lock.json i polecenia npm ci
   zamiast npm install w produkcyjnych pipeline'ach.

8. **Czyszczenie środowiska**
   Warto usuwać tymczasowe pliki i niepotrzebne obrazy po zakończeniu buildów.

## 5. Podsumowanie

W ramach zadania utworzono deklaratywny Jenkinsfile dla aplikacji Node.js.

Pipeline realizuje następujące operacje:

1. Pobranie kodu z repozytorium.
2. Instalację zależności npm.
3. Uruchomienie testów.
4. Budowanie aplikacji.
5. Budowanie obrazu Docker.
6. Publikowanie obrazu w Docker Hub.

Konfiguracja automatyzuje podstawowy proces CI/CD i ułatwia
przygotowanie aplikacji do dalszego wdrażania.
