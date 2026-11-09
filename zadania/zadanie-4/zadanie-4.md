# Zwykły prompt

Jak rozwiązać problem z dużym zużyciem pamięci przez kontener Docker?

Rozwiązanie problemu dużego zużycia pamięci przez kontener Docker wymaga zidentyfikowania źródła wycieku lub nadmiernego zapotrzebowania, a następnie nałożenia odpowiednich limitów.

Oto sprawdzony, krok po kroku proces diagnozy i optymalizacji.

Krok 1: Identyfikacja kontenera i bieżącego zużycia
Sprawdź, które kontenery zużywają najwięcej pamięci RAM, uruchamiając w terminalu:

Bash
docker stats
Polecenie to wyświetli w czasie rzeczywistym zużycie zasobów (CPU, pamięć RAM, sieć, I/O dyskowe) dla wszystkich uruchomionych kontenerów.

Krok 2: Diagnoza wnętrza kontenera
Jeśli nie masz pewności, co dokładnie w kontenerze generuje obciążenie, możesz sprawdzić zużycie pamięci przez poszczególne procesy wewnątrz niego:

Bash
docker top <nazwa_lub_id_kontenera>
Możesz też wejść do wnętrza kontenera, aby przeprowadzić dokładniejszą inspekcję (np. za pomocą htop lub polecenia ps):

Bash
docker exec -it <nazwa_lub_id_kontenera> sh
# wewnątrz kontenera:
free -m
ps aux --sort=-%mem
Krok 3: Nałożenie limitów pamięci (Ochrona systemu hosta)
Aby zapobiec sytuacji, w której jeden kontener zjada całą pamięć RAM i doprowadza do awarii całego hosta (lub zatrzymania systemu przez mechanizm OOM Killer), ustaw twarde limity zasobów.

Przy uruchamianiu przez CLI (docker run):
Użyj flagi -m lub --memory oraz opcjonalnie --memory-swap:

Bash
docker run -d --name moj-kontener -m 512m --memory-swap 512m moja-aplikacja
(Ustawienie --memory-swap na taką samą wartość jak --memory wyłącza korzystanie z pamięci swap, co zmusza kontener do działania wyłącznie w ramach limitu RAM).

W pliku docker-compose.yml:
Dodaj sekcję deploy.resources.limits lub starszą mem_limit:

YAML
version: '3.8'
services:
  app:
    image: moja-aplikacja
    deploy:
      resources:
        limits:
          memory: 512M
        reservations:
          memory: 256M
Krok 4: Optymalizacja i typowe przyczyny
Konfiguracja środowiska uruchomieniowego (np. Node.js, JVM, Python):
Wiele języków i środowisk domyślnie próbuje zaalokować dużą część pamięci dostępnej na hoście.

Node.js: Domyślny limit pamięci Heap dla V8 bywa za mały lub za duży w kontenerach. Możesz go ograniczyć flagą: --max-old-space-size=384.

Java (JVM): Tradycyjne aplikacje Java słabo radzą sobie z ograniczeniami Dockera, chyba że włączysz obsługę kontenerów flagą -XX:+UseContainerSupport i odpowiednio ustawisz -XX:MaxRAMPercentage.

Czyszczenie niewykorzystanych zasobów Dockera:
Czasami problem nie wynika z działania samego kontenera, ale z narastania nieużywanych danych (obrazów, wolumenów, warstw buildera), które zapychają przestrzeń i pamięć podręczną systemu:

Bash
docker system prune -a --volumes
Optymalizacja warstw obrazu (Dockerfile):
Upewnij się, że nie przechowujesz wewnątrz obrazu zbędnych plików tymczasowych i budujesz aplikację w trybie wieloetapowym (Multi-stage builds), pozostawiając w ostatecznym obrazie wyłącznie pliki produkcyjne.

# Prompt "Jesteś doświadczonym..."

Wysokie zużycie pamięci (RAM) w kontenerze Docker to jeden z najczęstszych problemów wydajnościowych, z jakimimierzymy się w codziennej pracy DevOps. Aby podejść do tematu metodycznie, proces diagnostyki i rozwiązywania problemu podzieliłem na konkretne kroki.1. Diagnoza – Identyfikacja źródła problemuZanim cokolwiek zmienisz, musisz dowiedzieć się, co dokładnie konsumuje pamięć.Sprawdź bieżące użycie: Użyj polecenia docker stats, aby zobaczyć, który kontener przekracza limity i jakie jest jego faktyczne zużycie względem alokacji.Przeanalizuj wnętrze kontenera: Wejdź do środka kontenera za pomocą docker exec -it <container_id> sh (lub bash) i sprawdź procesy:Jeśli to aplikacja oparta na Linuksie, użyj top lub htop.W przypadku procesów Node.js, Java (JVM), Python czy Go warto sprawdzić specyficzne narzędzia diagnostyczne dla danej technologii (np. profilowanie pamięci heap).2. Najczęstsze przyczyny i rozwiązaniaA. Brak limitów zasobów (Resource Limits)Domyślnie kontener Docker ma dostęp do całej pamięci RAM hosta. Jeśli aplikacja ma wyciek pamięci (memory leak), będzie rosła w nieskończoność, aż kernel zepsuje system lub zabije proces za pomocą OOM Killer (Out-Of-Memory).Rozwiązanie: Zdefiniuj twarde limity w pliku docker-compose.yml lub przy starcie kontenera:YAMLservices:
  app:
    image: my-app:latest
    deploy:
      resources:
        limits:
          memory: 512M
        reservations:
          memory: 256M
Uwaga: Ustawienie limitu sprawi, że kontener zostanie zamknięty zamiast przeciążać cały węzeł, co wymusza dodanie polityki restartu (np. restart: unless-stopped).B. Konfiguracja maszyn wirtualnych / środowisk uruchomieniowych (JVM, Node.js)Aplikacje uruchamiane w środowiskach takich jak Java (JVM) czy Node.js często domyślnie rezerwują określoną pulę pamięci opartą na zasobach hosta, a nie kontenera.Rozwiązanie dla Javy: Starsze wersje Javy (przed Java 10) nie potrafiły poprawnie odczytać limitów Dockera. Upewnij się, że używasz nowszej Javy i jawnie kontrolujesz flagi sterty, np.:-XX:+UseContainerSupport -Xmx256m -Xms128m.Rozwiązanie dla Node.js: Domyślny limit pamięci V8 dla heapu może być za wysoki dla małych kontenerów. Ogranicz go flagą:node --max-old-space-size=384 server.js.C. Wycieki pamięci (Memory Leaks)Jeśli zużycie pamięci stale rośnie w czasie bez wyraźnego wzrostu ruchu, masz do czynienia z wyciekiem w kodzie aplikacji.Rozwiązanie:Wprowadź automatyczne healthchecki i restarty kontenera jako tymczasowe obejście (Workaround).Wykonaj profilowanie pamięci (np. pprof dla Go, Valgrind dla C/C++, Heapdump dla Node.js/Java) i przekaż raport deweloperom.D. Nadmierne buforowanie, logi i pliki tymczasoweLogi Dockera: Domyślnie Docker trzyma logi kontenera w formacie JSON bez limitu rotacji (json-file), co potrafi zjeść gigabajty pamięci/dyskowej przestrzeni wymiany.Rozwiązanie: Skonfiguruj rotację logów globalnie w /etc/docker/daemon.json:JSON{
  "log-driver": "json-file",
  "log-opts": {
    "max-size": "10m",
    "max-file": "3"
  }
}
Warstwy obrazu i tmpfs: Upewnij się, że aplikacja nie zapisuje dużych plików tymczasowych bezpośrednio w warstwie zapisu kontenera (CoW – Copy-on-Write), lecz używa dedykowanych wolumenów lub montowań typu tmpfs.3. Automatyzacja i Monitoring (Najlepsze praktyki)Jako DevOps nie polegaj tylko na ręcznej reakcji:System monitoringu: Wdróż Prometheus + cAdvisor + Grafana, aby śledzić metryki container_memory_usage_bytes w czasie rzeczywistym.Alerty: Skonfiguruj alerty w Alertmanagerze (np. gdy zużycie pamięci kontenera przekracza 85% limitu przez ponad 5 minut).Testy obciążeniowe: Przed wypuszczeniem na produkcję przetestuj aplikację narzędziami takimi jak k6 lub Locust, obserwując zachowanie pamięci pod obciążeniem.


Uwagi: Pierwszy prompt jest trochę prostszy do zrozumienia, drugi jest bardziej rozpisany