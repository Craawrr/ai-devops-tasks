
# Zadanie 29 – Generowanie szablonu konfiguracji Jenkins

## 1. Cel zadania

Celem zadania jest przygotowanie automatycznej konfiguracji
Jenkins za pomocą mechanizmu Jenkins Configuration as Code (JCasC).

Konfiguracja znajduje się w pliku `jenkins-casc.yaml`.

## 2. Wymagania

Przed rozpoczęciem należy zainstalować:

- Docker i Docker Compose
- Git
- Jenkins z obsługą Jenkins Configuration as Code
- Dostęp do repozytorium projektu

## 3. Zawartość konfiguracji

Plik `jenkins-casc.yaml` zawiera:

- podstawową konfigurację Jenkinsa;
- ustawienie liczby executorów na 2;
- konfigurację użytkownika administratora;
- katalog narzędzi Maven 3.9.9;
- katalog narzędzi Node.js 22;
- przykładową konfigurację Docker;
- automatyczne utworzenie zadania Pipeline;
- timeout zadania wynoszący 30 minut.

## 4. Instalacja Jenkinsa

Najprostszy sposób uruchomienia Jenkinsa to wykorzystanie Dockera.

Utwórz plik `plugins.txt`:

```text
configuration-as-code
workflow-aggregator
job-dsl
git
maven-plugin
nodejs
docker-plugin
```

Utwórz plik `Dockerfile`:

```dockerfile
FROM jenkins/jenkins:lts-jdk21

COPY plugins.txt /usr/share/jenkins/ref/plugins.txt

RUN jenkins-plugin-cli -f /usr/share/jenkins/ref/plugins.txt
```

Zbuduj obraz:

```bash
docker build -t jenkins-jcasc .
```

## 5. Uruchomienie Jenkinsa z JCasC

Umieść plik `jenkins-casc.yaml` w katalogu projektu.

Utwórz zmienne środowiskowe:

```bash
export JENKINS_ADMIN_ID=admin
export JENKINS_ADMIN_PASSWORD='ChangeThisPassword123!'
```

Uruchom kontener:

```bash
docker run -d \
  --name jenkins \
  -p 8080:8080 \
  -p 50000:50000 \
  -e CASC_JENKINS_CONFIG=/var/jenkins_home/casc/jenkins-casc.yaml \
  -e JENKINS_ADMIN_ID="$JENKINS_ADMIN_ID" \
  -e JENKINS_ADMIN_PASSWORD="$JENKINS_ADMIN_PASSWORD" \
  -v jenkins_home:/var/jenkins_home \
  -v "$(pwd)/jenkins-casc.yaml:/var/jenkins_home/casc/jenkins-casc.yaml:ro" \
  jenkins-jcasc
```

## 6. Dostęp do panelu Jenkins

Po uruchomieniu kontenera otwórz przeglądarkę:

http://localhost:8080

Zaloguj się za pomocą danych administratora skonfigurowanych
w zmiennych środowiskowych.

## 7. Weryfikacja konfiguracji

Po uruchomieniu Jenkinsa sprawdź:

1. Czy Jenkins uruchomił się poprawnie.
2. Czy konfiguracja JCasC została załadowana.
3. Czy skonfigurowano 2 executory.
4. Czy dostępne są narzędzia Maven i Node.js.
5. Czy konfiguracja Docker została poprawnie rozpoznana.
6. Czy automatycznie utworzono zadanie `example-pipeline`.
7. Czy Pipeline można uruchomić.

W razie problemów sprawdź logi:

```bash
docker logs jenkins
```

Możesz również sprawdzić status kontenera:

```bash
docker ps
```

## 8. Ponowne zastosowanie konfiguracji

Po zmianie pliku YAML można ponownie załadować konfigurację
z poziomu panelu Jenkins:

Manage Jenkins → Configuration as Code → Reload existing configuration.

Przed przeładowaniem należy upewnić się, że zmiany w YAML
są poprawne.

## 9. Zatrzymanie Jenkinsa

```bash
docker stop jenkins
```

Ponowne uruchomienie:

```bash
docker start jenkins
```

## 10. Podsumowanie

W ramach zadania przygotowano szablon Jenkins Configuration
as Code, który umożliwia automatyzację podstawowej konfiguracji
serwera Jenkins.

Dzięki JCasC konfiguracja jest przechowywana jako kod,
co ułatwia jej wersjonowanie, odtwarzanie i przenoszenie
pomiędzy środowiskami.
