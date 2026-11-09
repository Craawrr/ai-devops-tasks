# 1. prosty prompt

Here is a production-ready, multi-stage Dockerfile for a Node.js application.Multi-stage builds keep your final image lean by separating the build environment (which needs dev dependencies) from the runtime environment (which only needs production dependencies and compiled code).Dockerfile# Stage 1: Build the application
FROM node:20-alpine AS builder

WORKDIR /app

# Install dependencies first (better layer caching)
COPY package*.json ./
RUN npm ci

# Copy source code and build
COPY . .
# Uncomment if you have a build step (e.g., TypeScript or a bundler)
# RUN npm run build

# Stage 2: Run the application
FROM node:20-alpine AS runner

WORKDIR /app

# Set to production environment
ENV NODE_ENV=production

# Create a non-privileged user for security
USER node

# Copy package files and install only production dependencies
COPY package*.json ./
RUN npm ci --only=production

# Copy built artifacts from the builder stage
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/src ./src
COPY --from=builder /app/package.json ./package.json

EXPOSE 3000

CMD ["npm", "start"]
Best Practices Used Here:Alpine Linux Base Image (node:20-alpine): Keeps the image size extremely small and reduces security vulnerabilities.Multi-Stage Build: Keeps dev tools and build caches out of the production image.Non-Root User (USER node): Runs the container with a restricted user rather than root to improve security.Layer Caching: Copies package*.json and runs npm ci before copying source code, ensuring dependencies aren't re-installed every time you change a code file.


# 2. Rozbudowany prompt

Oto prosty i poprawnie skonfigurowany Dockerfile dla aplikacji Node.js, spełniający wszystkie Twoje wymagania:

Dockerfile
# Użycie oficjalnego obrazu Node.js w wersji 18
FROM node:18

# Ustawienie katalogu roboczego wewnątrz kontenera
WORKDIR /app

# Kopiowanie plików definicji zależności
COPY package*.json ./

# Instalacja zależności
RUN npm install

# Kopiowanie pozostałych plików źródłowych aplikacji
COPY . .

# Wystawienie portu, na którym nasłuchuje aplikacja
EXPOSE 3000

# Komenda uruchamiająca aplikację
CMD ["npm", "start"]

Wskazówka dotycząca optymalizacji (opcjonalnie)
Jeśli aplikacja ma być uruchamiana w środowisku produkcyjnym, zamiast npm install często stosuje się npm ci (zainstaluje zależności dokładnie według pliku package-lock.json, co jest szybsze i bezpieczniejsze dla CI/CD).