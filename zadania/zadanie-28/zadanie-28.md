Zadanie 28: Skrypt do zarządzania zadaniami Jenkins
1. Cel zadania

Celem zadania było stworzenie skryptu w języku Python, który umożliwia automatyczne zarządzanie zadaniami (jobs) w Jenkins za pomocą REST API.

Skrypt jenkins-manager.py realizuje trzy podstawowe funkcje:

Listowanie wszystkich zadań Jenkins.
Sprawdzanie statusu ostatniego builda wybranego zadania.
Uruchamianie wybranego zadania.
2. Wykorzystane biblioteki
requests

Biblioteka requests służy do wykonywania zapytań HTTP do Jenkins REST API.

Wykorzystujemy:

GET – pobieranie informacji o zadaniach i buildach.
POST – uruchamianie wybranego zadania.
raise_for_status() – wykrywanie błędów HTTP.
Session() – zarządzanie sesją HTTP.
requests.auth.HTTPBasicAuth

Odpowiada za uwierzytelnianie użytkownika Jenkins za pomocą nazwy użytkownika i tokenu API.

os

Biblioteka systemowa wykorzystywana do pobierania konfiguracji ze zmiennych środowiskowych.

sys

Umożliwia obsługę argumentów przekazywanych podczas uruchamiania skryptu.

3. Konfiguracja połączenia

Przed uruchomieniem należy ustawić zmienne środowiskowe:

bash
export JENKINS_URL="http://localhost:8080"
export JENKINS_USER="admin"
export JENKINS_TOKEN="twoj_token_api"


Token API można wygenerować w ustawieniach użytkownika Jenkins.

Instalacja wymaganej biblioteki:

bash
pip install requests

4. Jak działa skrypt?
Listowanie zadań

Polecenie:

bash
python jenkins-manager.py list


Wysyła zapytanie GET do:

/api/json

Pobiera nazwy zadań, ich status oraz adresy URL.

Sprawdzanie statusu builda

Polecenie:

bash
python jenkins-manager.py status nazwa-zadania


Wysyła zapytanie GET do:

/job/NAZWA_ZADANIA/lastBuild/api/json

Pobiera numer ostatniego builda, jego wynik, informację o tym, czy nadal trwa, oraz adres URL.

Uruchamianie zadania

Polecenie:

bash
python jenkins-manager.py run nazwa-zadania


Wysyła zapytanie POST do:

/job/NAZWA_ZADANIA/build

Jenkins otrzymuje polecenie uruchomienia nowego builda.

5. Obsługa błędów i bezpieczeństwo

Skrypt uwzględnia:

Błędy HTTP.
Problemy z połączeniem z serwerem.
Przekroczenie czasu oczekiwania.
Brak wymaganych zmiennych środowiskowych.
Nieprawidłowe argumenty polecenia.

Dane uwierzytelniające nie są zapisane bezpośrednio w kodzie. Wykorzystywane są zmienne środowiskowe i token API Jenkins.

Do uruchamiania zadań wymagane są odpowiednie uprawnienia użytkownika Jenkins.

6. Przykładowe użycie
bash
# Wyświetlenie wszystkich zadań
python jenkins-manager.py list

# Sprawdzenie statusu zadania
python jenkins-manager.py status build-project

# Uruchomienie zadania
python jenkins-manager.py run build-project

7. Podsumowanie

W ramach zadania utworzono skrypt Python integrujący się z Jenkins REST API.

Skrypt pozwala automatyzować podstawowe operacje związane z zarządzaniem zadaniami Jenkins bez konieczności korzystania z interfejsu graficznego.

Wykorzystanie biblioteki requests upraszcza komunikację HTTP, a zastosowanie tokenu API i zmiennych środowiskowych zapewnia bezpieczniejsze przechowywanie danych uwierzytelniających.