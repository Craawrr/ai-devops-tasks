# 1
+----------+          +-------------------+          +-------------+
|  Klient  | -------> | Serwer aplikacji  | -------> | Baza danych |
|  (Client)|          | (App Server)      |          | (Database)  |
+----------+          +-------------------+          +-------------+

# 2

+--------------------+                     +----------------------+                     +--------------------+
|       Klient       |                     |   Serwer aplikacji   |                     |    Baza danych     |
|  (Przeglądarka /   | -- Żądanie HTTP ---> |  (Logika biznesowa,  | -- Zapytanie SQL --> | (Przechowywanie    |
| Aplikacja mobilna) | <--- Dane JSON/HTML - |   API, Kontrolery)   | <-- Wyniki danych - |     rekordów)      |
+--------------------+                     +----------------------+                     +--------------------+