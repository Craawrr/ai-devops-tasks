Zadanie 24: Interpretacja danych wydajnościowych
1. Dane wydajnościowe serwera API

Analizie poddano metryki serwera API z ostatnich 24 godzin.

Metryka	Wartość
Średni czas odpowiedzi	230 ms
95. percentyl czasu odpowiedzi	450 ms
99. percentyl czasu odpowiedzi	1200 ms
Liczba zapytań	15 000
Liczba błędów HTTP 5xx	120
Średnie użycie CPU	45%
Maksymalne użycie CPU	80%
Średnie użycie pamięci	2,1 GB
Maksymalne użycie pamięci	3,5 GB
Dostępna pamięć	4 GB
2. Interpretacja danych
Czas odpowiedzi API

Średni czas odpowiedzi wynosi 230 ms, co można uznać za dobry wynik dla typowego API.

Jednak wartości percentyli wskazują na problemy z wydajnością części zapytań:

P95 = 450 ms oznacza, że 95% zapytań otrzymuje odpowiedź w czasie nieprzekraczającym 450 ms.
P99 = 1200 ms oznacza, że 1% zapytań trwa dłużej niż 1200 ms.

Wskazuje to na występowanie pojedynczych wolnych operacji, które mogą negatywnie wpływać na doświadczenie użytkowników.

Potencjalny problem: Niektóre endpointy mogą wykonywać zbyt kosztowne zapytania do bazy danych lub korzystać z wolnych usług zewnętrznych.

Liczba zapytań i błędy 5xx

Serwer obsłużył 15 000 zapytań w ciągu 24 godzin.

Liczba błędów 5xx wynosi 120.

Współczynnik błędów:

120 / 15 000 × 100% = 0,8%

Oznacza to, że około 0,8% wszystkich zapytań zakończyło się błędem serwera.

Potencjalny problem: Błędy 5xx mogą wskazywać na:

Przeciążenie serwera.
Problemy z bazą danych.
Przekroczenie limitów czasu odpowiedzi.
Nieprawidłową obsługę wyjątków.
Problemy z usługami zewnętrznymi.

Warto przeanalizować logi błędów i ustalić, które endpointy generują najwięcej niepowodzeń.

Wykorzystanie procesora CPU

Średnie wykorzystanie CPU wynosi 45%, natomiast maksymalne 80%.

Średnie obciążenie jest umiarkowane i nie wskazuje na stałe przeciążenie procesora.

Maksymalna wartość 80% sugeruje jednak, że w określonych momentach serwer może doświadczać zwiększonego obciążenia.

Potencjalny problem: Nagłe wzrosty liczby zapytań lub kosztowne operacje mogą powodować chwilowe spowolnienia.

Wykorzystanie pamięci RAM

Średnie zużycie pamięci wynosi 2,1 GB z dostępnych 4 GB.

Maksymalne zużycie wynosi 3,5 GB, czyli 87,5% dostępnej pamięci.

Jest to jeden z najbardziej niepokojących wyników w analizowanych metrykach.

Potencjalne problemy:

Ryzyko wyczerpania dostępnej pamięci RAM.
Wycieki pamięci w aplikacji.
Zbyt duża liczba przechowywanych obiektów w pamięci.
Nadmierne buforowanie danych.
Spadek wydajności związany z intensywnym zarządzaniem pamięcią.

Należy monitorować zużycie pamięci w czasie i sprawdzić, czy rośnie ono stopniowo podczas działania aplikacji.

3. Zidentyfikowane problemy

Na podstawie przedstawionych danych można wskazać następujące potencjalne problemy:

Wysoki P99 czasu odpowiedzi – część użytkowników doświadcza odpowiedzi trwających ponad 1,2 sekundy.
Błędy serwera 5xx – współczynnik błędów wynosi 0,8%, co wymaga dalszej analizy.
Wysokie maksymalne zużycie pamięci – 87,5% dostępnej pamięci może prowadzić do problemów ze stabilnością.
Okresowe wzrosty użycia CPU – maksymalne obciążenie 80% wskazuje na możliwe chwilowe przeciążenia.
4. Rekomendacje dotyczące poprawy wydajności
Optymalizacja zapytań do bazy danych
Przeanalizować najwolniejsze zapytania SQL.
Dodać indeksy do często wyszukiwanych kolumn.
Unikać pobierania niepotrzebnych danych.
Ograniczyć liczbę zapytań wykonywanych podczas pojedynczej operacji API.
Zastosować paginację przy pobieraniu dużych zbiorów danych.
Optymalizacja pamięci
Przeprowadzić analizę zużycia pamięci.
Sprawdzić aplikację pod kątem wycieków pamięci.
Ograniczyć przechowywanie dużych obiektów w pamięci.
Zoptymalizować mechanizmy cache.
Rozważyć zwiększenie dostępnej pamięci RAM, jeśli obciążenie stale rośnie.
Poprawa czasu odpowiedzi API
Zidentyfikować endpointy o najwyższym czasie odpowiedzi.
Zastosować cache dla często wykorzystywanych danych.
Ograniczyć zbędne operacje wykonywane synchronicznie.
Rozważyć wykonywanie czasochłonnych zadań asynchronicznie.
Zoptymalizować komunikację z usługami zewnętrznymi.
Ograniczenie liczby błędów 5xx
Przeanalizować logi serwera.
Dodać szczegółowe logowanie wyjątków.
Zastosować odpowiednią obsługę błędów.
Skonfigurować timeouty i kontrolowane ponawianie nieudanych operacji.
Monitorować dostępność bazy danych i usług zewnętrznych.
Monitoring i skalowanie
Wprowadzić monitoring CPU, RAM i czasu odpowiedzi.
Skonfigurować alerty dla wysokiego zużycia pamięci.
Monitorować P95 i P99 zamiast analizować wyłącznie średni czas odpowiedzi.
Rozważyć skalowanie infrastruktury, jeśli obciążenie regularnie przekracza dostępne zasoby.
5. Priorytety działań
Priorytet	Działanie	Uzasadnienie
Wysoki	Analiza zużycia pamięci	Maksymalnie wykorzystane 87,5% RAM
Wysoki	Analiza błędów 5xx	120 błędów w ciągu 24 godzin
Wysoki	Analiza wolnych endpointów	P99 wynosi 1200 ms
Średni	Optymalizacja zapytań SQL	Możliwe ograniczenie opóźnień
Średni	Wdrożenie cache	Zmniejszenie liczby kosztownych operacji
Średni	Monitoring i alerty	Szybsze wykrywanie problemów
Niski	Analiza możliwości skalowania	Dalsza poprawa wydajności w miarę wzrostu ruchu
6. Podsumowanie

Serwer API ogólnie działa na akceptowalnym poziomie. Średni czas odpowiedzi wynoszący 230 ms oraz średnie użycie CPU na poziomie 45% nie wskazują na stałe przeciążenie infrastruktury.

Występują jednak obszary wymagające poprawy:

Wysoki 99. percentyl czasu odpowiedzi wskazuje na wolne zapytania.
Współczynnik błędów 5xx wynoszący 0,8% wymaga zbadania.
Maksymalne wykorzystanie pamięci na poziomie 87,5% stanowi potencjalne zagrożenie dla stabilności serwera.

Wniosek: W pierwszej kolejności należy przeanalizować zużycie pamięci, błędy serwera oraz najwolniejsze endpointy API. Następnie warto zoptymalizować zapytania do bazy danych, wdrożyć cache i rozszerzyć monitoring.

Działania te powinny poprawić stabilność serwera, skrócić czas odpowiedzi i ograniczyć liczbę błędów.