# logi
May 19 10:15:32 server dockerd[1234]: time="2025-05-19T10:15:32.123456789Z" level=info msg="Container 78a2b3c4 health status changed from starting to healthy"
May 19 10:16:45 server dockerd[1234]: time="2025-05-19T10:16:45.987654321Z" level=info msg="Container 78a2b3c4 failed to connect to 172.17.0.3:5432: connection refused"
May 19 10:16:47 server dockerd[1234]: time="2025-05-19T10:16:47.246813579Z" level=warning msg="Container 78a2b3c4 health status changed from healthy to unhealthy"

# analiza

Logi przedstawiają problem z kontenerem Docker o identyfikatorze 78a2b3c4. Początkowo kontener działał poprawnie, ale po pewnym czasie utracił możliwość połączenia z inną usługą (najprawdopodobniej bazą danych PostgreSQL).

Przeanalizujmy poszczególne wpisy.

1. Analiza logów
Log 1 – kontener uzyskał status Healthy

text
May 19 10:15:32 server dockerd[1234]: 
Container 78a2b3c4 health status changed from starting to healthy
Kontener zakończył fazę uruchamiania.

Mechanizm Docker Healthcheck wykonał test kontrolny.

Test zakończył się powodzeniem.

Kontener otrzymał status healthy.

Healthy
 Kontener w tym momencie działał poprawnie według skonfigurowanego testu zdrowia.

Log 2 – problem z połączeniem

text
May 19 10:16:45 server dockerd[1234]:
Container 78a2b3c4 failed to connect to 172.17.0.3:5432: connection refused
To najważniejszy wpis wskazujący na problem.

Kontener próbował nawiązać połączenie z adresem:

IP: 172.17.0.3

Port: 5432

Protokół: najprawdopodobniej TCP.

Usługa: prawdopodobnie PostgreSQL.

Komunikat connection refused oznacza, że próba nawiązania połączenia została odrzucona.

Możliwe przyczyny:

PostgreSQL nie jest uruchomiony.

PostgreSQL zakończył działanie lub uległ awarii.

Baza danych nie nasłuchuje na porcie 5432.

Usługa nasłuchuje tylko na localhost zamiast na interfejsie sieciowym kontenera.

Występuje problem z konfiguracją sieci Docker lub mapowaniem portów.

Ważne: connection refused zwykle oznacza, że adres docelowy jest osiągalny, ale połączenie TCP nie może zostać zaakceptowane na wskazanym porcie.

Log 3 – kontener stał się Unhealthy

text
May 19 10:16:47 server dockerd[1234]:
Container 78a2b3c4 health status changed from healthy to unhealthy
Docker wykonał kolejny test Healthcheck.

Test zakończył się niepowodzeniem.

Status kontenera zmienił się z healthy na unhealthy.

Unhealthy
 Kontener nie spełnia już warunków określonych w skonfigurowanym Healthcheck.

2. Jakie problemy można zidentyfikować?
Na podstawie logów można wskazać następujące problemy:

Problem

Prawdopodobna przyczyna

Brak połączenia z PostgreSQL

Baza nie działa lub nie nasłuchuje

Connection refused

Port 5432 odrzuca połączenie

Zmiana statusu na unhealthy

Nieudany Healthcheck

Niestabilność komunikacji

Możliwa awaria lub restart usługi bazodanowej

Warto zauważyć, że status healthy nie oznacza, że wszystkie funkcjonalności aplikacji działają poprawnie. Oznacza jedynie, że skonfigurowany test zdrowia zakończył się sukcesem.

3. Jak zdiagnozować problem?
Proponuję wykonać następujące kroki.

Krok 1. Sprawdź status kontenerów


bash
docker ps -a
Zwróć uwagę na status kontenera PostgreSQL oraz kontenera aplikacji.

Krok 2. Sprawdź logi bazy danych


bash
docker logs <postgres_container>
Poszukaj komunikatów dotyczących:

błędów uruchamiania PostgreSQL,

problemów z konfiguracją,

restartów,

błędów związanych z dostępnością zasobów.

Krok 3. Sprawdź, czy PostgreSQL nasłuchuje na porcie 5432

W kontenerze bazy danych:


bash
ss -lntp | grep 5432
Krok 4. Sprawdź konfigurację sieci Docker


bash
docker network inspect bridge
Zweryfikuj, czy oba kontenery znajdują się w odpowiedniej sieci i czy adres 172.17.0.3 należy do oczekiwanego kontenera.

Krok 5. Sprawdź szczegóły Healthcheck


bash
docker inspect 78a2b3c4
Szczególnie interesujące są pola:

State.Health.Status

State.Health.Log

Config.Healthcheck

Pozwolą ustalić, jaki test wykonywał Docker i dlaczego zakończył się niepowodzeniem.

4. Wniosek końcowy
Najbardziej prawdopodobny scenariusz wygląda następująco:

10:15:32 – uruchomienie kontenera

Kontener przechodzi do statusu healthy.

Healthy
10:16:45 – utrata połączenia

Aplikacja nie może połączyć się z usługą PostgreSQL pod adresem 172.17.0.3:5432.

Connection refused
10:16:47 – wykrycie problemu

Healthcheck wykrywa nieprawidłowość i Docker zmienia status kontenera na unhealthy.

Unhealthy
Moja diagnoza: najbardziej prawdopodobnym źródłem problemu jest niedostępność usługi PostgreSQL lub nieprawidłowa konfiguracja komunikacji między kontenerami.

Nie można jednak jednoznacznie stwierdzić, czy awaria dotyczy samej bazy danych, czy konfiguracji sieciowej, wyłącznie na podstawie tych trzech wpisów.

Warto też pamiętać, że Docker samoczynnie nie restartuje kontenera tylko dlatego, że jego status zmienił się na unhealthy. Do automatycznego restartu potrzebne są dodatkowe mechanizmy, np. zewnętrzny monitoring lub orkiestrator.