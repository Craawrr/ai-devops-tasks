Oczywiście! Przejdźmy przez ten skrypt spokojnie, linia po linii, zakładając, że dopiero zaczynasz naukę Bash i Linuksa.

Na początek warto wiedzieć, że skrypt służy do sprawdzenia, czy usługa Docker jest uruchomiona, a jeśli nie jest – próbuje ją uruchomić. Następnie sprawdza, czy operacja się powiodła.

1. Cały skrypt – co robi?
W uproszczeniu jego działanie wygląda tak:

Sprawdza, czy Docker działa.

Jeśli działa – wyświetla odpowiedni komunikat.

Jeśli nie działa – próbuje go uruchomić.

Ponownie sprawdza, czy Docker działa.

Jeśli uruchomienie się nie powiodło – wyświetla błąd i kończy działanie skryptu.

2. Wyjaśnienie linia po linii
Linia 1

bash
#!/bin/bash
To tak zwany shebang (czytamy mniej więcej: szebang).

Informuje system operacyjny, że ten skrypt powinien zostać wykonany przy użyciu interpretera Bash.

#! – specjalny zapis informujący system, jaki program ma wykonać skrypt.

/bin/bash – ścieżka do interpretera Bash.

Można to porównać do instrukcji: „Uruchom ten plik za pomocą Bash”.

Linia 2

bash
# Sprawdzenie, czy usługa Docker jest aktywna
To komentarz.

W Bash wszystko, co znajduje się po znaku # (poza szczególnymi przypadkami, np. shebangiem), jest traktowane jako komentarz.

Oznacza to, że:

komentarz jest przeznaczony dla człowieka;

Bash go nie wykonuje;

pomaga zrozumieć, co robi dana część kodu.

Linia 3

bash
if systemctl is-active --quiet docker; then
To jedna z najważniejszych linii całego skryptu.

Rozłóżmy ją na części:

if – oznacza „jeżeli”. Rozpoczyna instrukcję warunkową.

systemctl – narzędzie systemowe służące do zarządzania usługami w Linuksie.

is-active – sprawdza, czy dana usługa jest aktywna.

--quiet – powoduje, że polecenie nie wyświetla standardowego komunikatu o stanie usługi.

docker – nazwa usługi, którą sprawdzamy.

then – oznacza „to wykonaj”. Rozpoczyna blok poleceń wykonywanych, jeśli warunek jest spełniony.

Czyli cała linia oznacza:

Jeżeli usługa Docker jest aktywna, wykonaj polecenia znajdujące się po słowie then.

Ważna rzecz dla początkującego: Bash nie sprawdza tutaj, czy polecenie zwróciło tekst „active”. Sprawdza jego kod zakończenia:

0 – polecenie zakończyło się sukcesem (Docker jest aktywny).

wartość różna od 0 – polecenie zakończyło się niepowodzeniem (Docker nie jest aktywny).

Linia 4

bash
echo "Usługa Docker już działa."
Polecenie echo służy do wyświetlania tekstu w terminalu.

W tym przypadku użytkownik zobaczy:


text
Usługa Docker już działa.
Ta linia wykona się tylko wtedy, gdy Docker był już aktywny.

Linia 5

bash
else
Słowo else oznacza „w przeciwnym razie”.

Czyli jeśli warunek z linii 3 nie został spełniony, Bash przechodzi do części znajdującej się po else.

W naszym przypadku oznacza to, że Docker nie jest aktywny.

Linia 6

bash
echo "Usługa Docker jest wyłączona. Próbuję ją uruchomić..."
Ponownie używamy echo, aby wyświetlić komunikat.

W terminalu pojawi się:


text
Usługa Docker jest wyłączona. Próbuję ją uruchomić...
To informacja dla użytkownika, że skrypt wykrył nieaktywną usługę i zamierza ją uruchomić.

Linia 7

bash
sudo systemctl start docker
To polecenie odpowiada za uruchomienie usługi Docker.

Rozbijmy je:

sudo – uruchamia polecenie z uprawnieniami administratora (root), zwykle po potwierdzeniu hasłem.

systemctl – narzędzie do zarządzania usługami systemowymi.

start – oznacza „uruchom”.

docker – wskazuje usługę, którą chcemy uruchomić.

Całość oznacza:

Uruchom usługę Docker z uprawnieniami administratora.

Dlaczego używamy sudo?

Ponieważ zwykły użytkownik zazwyczaj nie ma uprawnień do uruchamiania i zatrzymywania usług systemowych.

Warto też wiedzieć, że samo start nie oznacza automatycznego uruchamiania Dockera przy każdym starcie komputera. Do tego służy między innymi systemctl enable.

Linia 8

bash
# Weryfikacja, czy uruchomienie się powiodło
To kolejny komentarz.

Informuje nas, że teraz skrypt będzie sprawdzał, czy próba uruchomienia Dockera zakończyła się sukcesem.

Linia 9

bash
if systemctl is-active --quiet docker; then
To ponowne sprawdzenie stanu usługi Docker.

Dlaczego robimy to drugi raz?

Ponieważ samo wydanie polecenia:


bash
sudo systemctl start docker
nie gwarantuje, że usługa rzeczywiście została uruchomiona.

Mogło wystąpić na przykład:

uszkodzenie konfiguracji Dockera;

problem z zależnościami;

błąd podczas uruchamiania usługi;

brak odpowiednich uprawnień.

Dlatego skrypt ponownie sprawdza, czy Docker jest aktywny.

Jeżeli tak – przechodzi do kolejnej linii.

Linia 10

bash
echo "Usługa Docker została pomyślnie uruchomiona."
Jeżeli ponowne sprawdzenie wykazało, że Docker działa, zostanie wyświetlony komunikat:


text
Usługa Docker została pomyślnie uruchomiona.
To informacja, że operacja zakończyła się powodzeniem.

Linia 11

bash
else
Ponownie mamy else.

Tym razem odnosi się ono do drugiego warunku if.

Oznacza to, że jeśli po wykonaniu polecenia uruchamiającego Docker usługa nadal nie jest aktywna, wykonaj instrukcje znajdujące się poniżej.

Linia 12

bash
echo "Błąd: Nie udało się uruchomić usługi Docker." >&2
Ta linia wyświetla komunikat o błędzie.

Nowym elementem jest tutaj:


bash
>&2
Co to oznacza?

W systemach Linux istnieją trzy podstawowe strumienie:

Numer

Nazwa

Znaczenie

0

stdin

Dane wejściowe

1

stdout

Standardowe wyjście

2

stderr

Wyjście błędów

Domyślnie echo wyświetla tekst na standardowym wyjściu (stdout).

Natomiast zapis:


bash
>&2
przekierowuje tekst na standardowe wyjście błędów (stderr).

Dlaczego to przydatne?

Ponieważ komunikaty informacyjne i komunikaty o błędach można dzięki temu rozdzielić.

Na przykład można zapisać zwykłe komunikaty do jednego pliku, a błędy do innego.

Linia 13

bash
exit 1
To polecenie kończy działanie skryptu.

Liczba 1 oznacza, że skrypt zakończył się błędem.

Warto zapamiętać:

exit 0 – zakończenie poprawne;

exit 1 – zakończenie z błędem;

inne wartości od 1 do 255 również mogą oznaczać różne rodzaje błędów.

Dlaczego nie używamy tutaj exit 0?

Ponieważ Docker nie został uruchomiony, więc skrypt nie wykonał swojego zadania.

Linia 14

bash
fi
Słowo fi kończy instrukcję warunkową if.

Ciekawostka: fi to po prostu if zapisane od tyłu.

W tym miejscu zamykamy drugi warunek if.

Linia 15

bash
fi
To drugie fi zamyka pierwszy, zewnętrzny warunek if.

Dlaczego mamy dwa razy fi?

Ponieważ mamy dwie instrukcje warunkowe:

Pierwsza sprawdza, czy Docker działa przed próbą uruchomienia.

Druga sprawdza, czy Docker działa po próbie uruchomienia.

Każdy blok if musi mieć swoje własne fi.

3. Schemat działania całego skryptu
Poniżej przedstawiam uproszczony schemat logiczny:

START

Rozpoczęcie wykonywania skryptu

Sprawdź: czy Docker działa?

systemctl is-active --quiet docker

TAK
Wyświetl komunikat

Docker już działa.

KONIEC

NIE
Uruchom Docker

sudo systemctl start docker

Sprawdź ponownie

Czy Docker działa?

TAK

Sukces

NIE

Błąd + exit 1

4. Jak skrypt zachowa się w praktyce?
Przeanalizujmy trzy możliwe sytuacje.

Sytuacja 1: Docker już działa

Wynik w terminalu:


text
Usługa Docker już działa.
Skrypt niczego nie uruchamia, ponieważ Docker jest już aktywny.

Sytuacja 2: Docker nie działa, ale udaje się go uruchomić

Wynik:


text
Usługa Docker jest wyłączona. Próbuję ją uruchomić...
Usługa Docker została pomyślnie uruchomiona.
Skrypt wykrył problem, uruchomił usługę i potwierdził sukces.

Sytuacja 3: Docker nie działa i nie udaje się go uruchomić

Wynik:


text
Usługa Docker jest wyłączona. Próbuję ją uruchomić...
Błąd: Nie udało się uruchomić usługi Docker.
Skrypt kończy działanie kodem błędu 1.

5. Najważniejsze polecenia do zapamiętania
Polecenie

Co robi?

echo

Wyświetla tekst

if

Rozpoczyna warunek

then

Rozpoczyna blok wykonywany po spełnieniu warunku

else

Wykonuje alternatywny blok

fi

Kończy warunek

systemctl is-active

Sprawdza stan usługi

systemctl start

Uruchamia usługę

sudo

Wykonuje polecenie z uprawnieniami administratora

exit 1

Kończy skrypt z kodem błędu

>&2

Przekierowuje komunikat na wyjście błędów

6. Jak samodzielnie przetestować ten skrypt?
Zapisz go na przykład w pliku docker_check.sh.

Następnie w terminalu wykonaj:


bash
chmod +x docker_check.sh
To nada plikowi uprawnienia do wykonywania.

Uruchom skrypt:


bash
./docker_check.sh
Możesz też ręcznie sprawdzić stan Dockera:


bash
systemctl status docker
Aby sprawdzić sam kod zakończenia ostatniego polecenia, wpisz:


bash
echo $?
Wynik 0 oznacza sukces, a 1 oznacza błąd.

Moja rada na początek nauki Bash: postaraj się zapamiętać przede wszystkim konstrukcję if → then → else → fi. To fundament, który będzie pojawiał się w wielu skryptach automatyzujących pracę w Linuksie.

Następnym dobrym ćwiczeniem byłoby napisanie własnego skryptu, który sprawdza, czy usługa SSH działa, i w razie potrzeby próbuje ją uruchomić.