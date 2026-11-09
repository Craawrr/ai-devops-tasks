Simple Task API
Opis projektu

Simple Task API to proste REST API służące do zarządzania zadaniami. Projekt został napisany w technologii Node.js z wykorzystaniem frameworka Express.js oraz bazy danych MongoDB.

API umożliwia użytkownikom tworzenie, przeglądanie, edytowanie i usuwanie zadań. Dodatkowo udostępnia filtrowanie zadań według statusu i priorytetu oraz podstawową autoryzację użytkowników.

Główne funkcje
Tworzenie nowych zadań.
Pobieranie listy wszystkich zadań.
Pobieranie szczegółów konkretnego zadania.
Aktualizowanie istniejących zadań.
Usuwanie zadań.
Filtrowanie zadań według statusu i priorytetu.
Podstawowa autoryzacja użytkowników.
Instalacja
Wymagania

Przed uruchomieniem projektu należy zainstalować:

Node.js (zalecana wersja LTS).
npm.
MongoDB (lokalnie lub w chmurze).
Kroki instalacji
Sklonuj repozytorium:
bash
git clone <URL_REPOZYTORIUM>

Przejdź do katalogu projektu:
bash
cd simple-task-api

Zainstaluj zależności:
bash
npm install

Utwórz plik .env i skonfiguruj zmienne środowiskowe:
env
PORT=3000
MONGODB_URI=mongodb://localhost:27017/simple-task-api
JWT_SECRET=your_secret_key

Uruchom aplikację:
bash
npm start


API powinno być dostępne pod adresem:

http://localhost:3000

Użycie

API umożliwia zarządzanie zadaniami za pomocą żądań HTTP.

Przykładowe zadanie:

json
{
  "title": "Przygotować dokumentację",
  "description": "Utworzyć plik README.md",
  "status": "pending",
  "priority": "high"
}


Przykładowe wywołanie API za pomocą curl:

bash
curl http://localhost:3000/api/tasks


W przypadku endpointów wymagających autoryzacji należy przekazać token:

http
Authorization: Bearer YOUR_TOKEN

Endpointy API

Wszystkie endpointy dotyczące zadań mają prefiks /api/tasks.

Metoda HTTP	Endpoint	Opis
GET	/api/tasks	Pobieranie wszystkich zadań
GET	/api/tasks/:id	Pobieranie zadania według ID
POST	/api/tasks	Tworzenie nowego zadania
PUT	/api/tasks/:id	Aktualizacja zadania
DELETE	/api/tasks/:id	Usuwanie zadania
Filtrowanie zadań

Możliwe jest filtrowanie zadań za pomocą parametrów zapytania:

http
GET /api/tasks?status=pending
GET /api/tasks?priority=high
GET /api/tasks?status=completed&priority=low

Autoryzacja

Przykładowe endpointy autoryzacyjne:

Metoda HTTP	Endpoint	Opis
POST	/api/auth/register	Rejestracja użytkownika
POST	/api/auth/login	Logowanie użytkownika

Po poprawnym zalogowaniu użytkownik otrzymuje token autoryzacyjny, który należy przekazywać w nagłówku Authorization.

Technologie
Node.js – środowisko uruchomieniowe JavaScript.
Express.js – framework do tworzenia REST API.
MongoDB – nierelacyjna baza danych.
JWT – mechanizm tokenowej autoryzacji użytkowników.
Uwagi

Dokumentacja przedstawia przykładową strukturę i sposób działania Simple Task API. Przed wykorzystaniem jej w rzeczywistym projekcie należy zweryfikować endpointy, nazwy zmiennych środowiskowych oraz sposób autoryzacji z faktyczną implementacją aplikacji.
