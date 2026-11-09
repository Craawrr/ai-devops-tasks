Przykład użycia

javascript
const tasks = [
    { id: 3, title: "Zadanie C", status: "completed" },
    { id: 1, title: "Zadanie A", status: "completed" },
    { id: 2, title: "Zadanie B", status: "pending" },
    { id: 4, title: "Zadanie D", status: "completed" }
];

const result = getCompletedTaskTitles(tasks);

console.log(result);
Wynik:


javascript
["Zadanie A", "Zadanie C", "Zadanie D"]
Jak to działa?
filter() – wybiera tylko zadania ze statusem "completed".

sort() – sortuje zadania rosnąco według id.

map() – tworzy nową tablicę zawierającą wyłącznie tytuły zadań.

Zaleta: Funkcja nie modyfikuje oryginalnej tablicy tasks, ponieważ filter() tworzy nową tablicę przed sortowaniem.


