# error
ERROR: for app  Cannot start service app: driver failed programming external connectivity on endpoint app (172.18.0.2): Error starting userland proxy: listen tcp4 0.0.0.0:3000: bind: address already in use
# odpowiedź

Ten błąd oznacza, że port 3000 jest już zajęty przez inny proces lub kontener, a Docker nie może uruchomić kolejnego kontenera app, który próbuje korzystać z tego samego portu.

Najważniejszy fragment komunikatu to:


text
listen tcp4 0.0.0.0:3000: bind: address already in use
Docker próbuje przypisać port 3000 na Twoim komputerze do portu kontenera, ale system informuje, że ten port jest już używany.

1. Sprawdź, co zajmuje port 3000
Jeśli korzystasz z Linuxa, wpisz w terminalu:


bash
sudo lsof -i :3000
Alternatywnie:


bash
sudo ss -ltnp | grep :3000
Zobaczysz proces, który nasłuchuje na porcie 3000.

Przykładowy wynik:


text
COMMAND   PID   USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
node     1234   user   20u  IPv4  ...    TCP *:3000 (LISTEN)
W tym przypadku port zajmuje proces Node.js o PID 1234.

2. Sprawdź, czy port zajmuje inny kontener Dockera
Wpisz:


bash
docker ps
Zwróć uwagę na kolumnę PORTS.

Przykład:


text
CONTAINER ID   IMAGE       PORTS
abc123         my-app      0.0.0.0:3000->3000/tcp
Jeśli znajdziesz kontener zajmujący port 3000, możesz go zatrzymać:


bash
docker stop abc123
Zamiast abc123 podaj ID swojego kontenera.

3. Zatrzymaj proces zajmujący port
Jeśli port zajmuje zwykły proces, np. Node.js, możesz go zatrzymać:


bash
sudo kill 1234
Zastąp 1234 rzeczywistym PID procesu.

Jeśli proces nie chce się zatrzymać, możesz użyć:


bash
sudo kill -9 1234
Uwaga: używaj tej opcji tylko wtedy, gdy wiesz, że możesz bezpiecznie zakończyć dany proces.

4. Alternatywnie zmień port w Dockerze
Jeżeli chcesz uruchomić dwie aplikacje jednocześnie, możesz zmienić port zewnętrzny.

W pliku docker-compose.yml prawdopodobnie masz:


yaml
services:
  app:
    ports:
      - "3000:3000"
Zmień na:


yaml
services:
  app:
    ports:
      - "3001:3000"
Oznacza to:

3001 – port dostępny na Twoim komputerze.

3000 – port wewnątrz kontenera.

Aplikacja będzie wtedy dostępna pod adresem:


text
http://localhost:3001
5. Uruchom ponownie aplikację
Po rozwiązaniu konfliktu wykonaj:


bash
docker compose down
docker compose up -d
Jeśli chcesz przebudować aplikację:


bash
docker compose up -d --build
Moja rekomendacja
Zacznij od tych dwóch poleceń:


bash
sudo lsof -i :3000
docker ps
Pozwolą Ci ustalić, czy port 3000 zajmuje lokalny proces, czy inny kontener Dockera.

Mam jeszcze jedno pytanie: Czy uruchamiasz aplikację przez Docker Compose (docker compose up), czy bezpośrednio przez Docker (docker run)?

Dzięki temu mogę wskazać Ci dokładnie, co zmienić, żeby rozwiązać problem bez niepotrzebnego zatrzymywania innych aplikacji.