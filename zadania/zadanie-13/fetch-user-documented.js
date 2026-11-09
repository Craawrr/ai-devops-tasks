/**
 * Pobiera dane użytkownika z zewnętrznego API.
 *
 * Wysyła żądanie HTTP GET do API, a następnie przetwarza otrzymane dane.
 * Zwraca obiekt zawierający imię, adres e-mail oraz datę ostatniego logowania.
 *
 * @async
 * @function fetchUserData
 * @param {string|number} userId - Unikalny identyfikator użytkownika.
 * @returns {Promise<{
 *   name: string,
 *   email: string,
 *   lastLogin: Date
 * }|null>} Promise zwracający obiekt z danymi użytkownika
 * lub null w przypadku wystąpienia błędu.
 *
 * @throws {Error} Błąd HTTP, jeśli odpowiedź serwera nie jest poprawna.
 *
 * @example
 * fetchUserData(123).then(user => {
 *   if (user) {
 *     console.log(user.name);
 *     console.log(user.email);
 *     console.log(user.lastLogin);
 *   }
 * });
 */
function fetchUserData(userId) {
  return fetch(`https://api.example.com/users/${userId}`)
    .then(response => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then(data => {
      return {
        name: data.name,
        email: data.email,
        lastLogin: new Date(data.lastLoginTimestamp)
      };
    })
    .catch(error => {
      console.error('Fetch error:', error);
      return null;
    });
}