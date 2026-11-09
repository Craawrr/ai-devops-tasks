Najważniejsze różnice między Bash a PowerShell
Bash

PowerShell

Opis

#!/bin/bash

Brak odpowiednika

PowerShell używa rozszerzenia .ps1

date +%Y%m%d_%H%M%S

Get-Date -Format

Pobieranie daty

mkdir -p

New-Item -Force

Tworzenie katalogu

[ ! -d ... ]

-not (Test-Path ...)

Sprawdzanie katalogu

echo

Write-Host

Wyświetlanie komunikatów

gzip

gzip.exe

Kompresja pliku

Wymagania
Przed uruchomieniem upewnij się, że:

Masz zainstalowany MySQL Client (mysqldump.exe).

Masz dostępne narzędzie gzip.exe (np. z Git for Windows).

Katalog z programami MySQL i gzip znajduje się w zmiennej środowiskowej PATH.

Uruchomienie skryptu
Otwórz PowerShell i wykonaj:


powershell
.\backup.ps1
Uwaga: Warto sprawdzać osobno kod zakończenia mysqldump i gzip, ponieważ samo sprawdzenie $LASTEXITCODE po potoku może nie wykryć błędu pierwszego polecenia. W wersji produkcyjnej zalecam również użycie tymczasowego pliku i przeniesienie go do docelowej lokalizacji dopiero po udanym backupie.


