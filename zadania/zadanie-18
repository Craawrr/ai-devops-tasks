Zadanie 18: Analiza wymagań bezpieczeństwa dla aplikacji Dockerowych

Pytanie 1: Jakie są 5 kluczowych praktyk bezpieczeństwa dla aplikacji Dockerowych w środowisku produkcyjnym?

1. Uruchamianie kontenerów z uprawnieniami nieuprzywilejowanymi (Non-root user)

Domyślnie kontenery Docker uruchamiają procesy jako użytkownik root. Jeśli napastnik zdoła uciec z kontenera, uzyskuje uprawnienia roota na hoście. Zastosowanie dedykowanego użytkownika o ograniczonych uprawnieniach znacząco ogranicza promień rażenia ewentualnego ataku.

2. Skanowanie obrazów i używanie zaufanych, minimalnych obrazów bazowych

Korzystaj wyłącznie z oficjalnych lub zweryfikowanych obrazów bazowych (np. obracających się wokół dystrybucji Alpine lub obrazów distroless). Regularnie skanuj obrazy w poszukiwaniu znanych podatności (CVE) za pomocą narzędzi takich jak Trivy, Docker Scout czy Clair.

3. Zapewnienie niezmienności i zasada minimalnych uprawnień systemowych (Read-only root filesystem & Capabilities)

Ogranicz uprawnienia jądra Linux dostarczane do kontenera (cap_drop: - ALL) i przyznawaj tylko te absolutnie niezbędne. W miarę możliwości uruchamiaj system plików kontenera w trybie tylko do odczytu (read_only: true), montując jako zapisywalne tylko katalogi tymczasowe (tmpfs).

4. Bezpieczne zarządzanie sekretami (Secrets Management)

Nigdy nie przechowuj haseł, kluczy API ani certyfikatów bezpośrednio w kodzie, plikach Dockerfile czy jako stałe zmienne środowiskowe w obrazie. Używaj dedykowanych mechanizmów zarządzania sekretami, takich jak Docker Secrets, HashiCorp Vault, AWS Secrets Manager lub zmiennych wstrzykiwanych w czasie uruchamiania.

5. Ograniczanie zasobów i izolacja sieciowa

Definiuj limity pamięci RAM oraz CPU dla każdego kontenera, aby zapobiec atakom typu Denial of Service (DoS) lub wyczerpaniu zasobów hosta. Twórz odizolowane, dedykowane sieci Dockerowe (nie używaj domyślnej sieci bridge), aby ograniczyć ruch sieciowy wyłącznie do kontenerów, które muszą ze sobą się komunikować.

Pytanie 2: Jak mogę zaimplementować pierwszą z tych praktyk (Non-root user) w moim Dockerfile i docker-compose.yml?

Poniżej znajdują się przykłady implementacji zasady użytkownika nieuprzywilejowanego (Non-root user).

Implementacja w Dockerfile

W Dockerfile należy utworzyć dedykowaną grupę i użytkownika, nadaj im odpowiednie uprawnienia do katalogu aplikacji, a następnie przełączyć kontekst za pomocą instrukcji USER.

# Obraz bazowy
FROM node:18-alpine

# Utworzenie nieuprzywilejowanej grupy i użytkownika
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

# Ustawienie katalogu roboczego
WORKDIR /app

# Skopiowanie plików zalezności i instalacja
COPY package*.json ./
RUN npm ci --only=production

# Skopiowanie reszty kodu aplikacji
COPY . .

# Zmiana właściciela katalogu aplikacji na utworzonego użytkownika
RUN chown -R appuser:appgroup /app

# Przełączenie się na użytkownika nieuprzywilejowanego
USER appuser

# Wystawienie portu i uruchomienie aplikacji
EXPOSE 3000
CMD ["node", "server.js"]


Implementacja w docker-compose.yml

W pliku docker-compose.yml można wymusić uruchomienie kontenera jako określony UID i GID (np. użytkownik z hosta lub wcześniej przygotowany użytkownik w obrazie) za pomocą pola user.

version: '3.8'

services:
  web-app:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "3000:3000"
    # Uruchomienie kontenera jako użytkownik nieuprzywilejowany (UID:GID)
    # 10001:10001 to przykładowe UID i GID użytkownika bez uprawnień root
    user: "10001:10001"
    
    # Dodatkowe zabezpieczenia wspierające:
    read_only: true # System plików w trybie tylko do odczytu
    tmpfs:
      - /tmp # Katalog tymczasowy dostępny do zapisu
    security_opt:
      - no-new-privileges:true # Blokuje podnoszenie uprawnień wewnątrz kontenera
    restart: unless-stopped