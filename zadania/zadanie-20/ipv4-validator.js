
/**
 * Walidator adresów IPv4.
 */

const ipv4Regex =
  /^(?:(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)$/;

/**
 * Sprawdza, czy podany ciąg znaków jest poprawnym adresem IPv4.
 *
 * @param {string} ip - Adres IP do sprawdzenia.
 * @returns {boolean} - Informacja o poprawności adresu.
 */
function isValidIPv4(ip) {
    return typeof ip === "string" && ipv4Regex.test(ip);
}

// Przykłady testów
const testCases = [
    "192.168.1.1",
    "127.0.0.1",
    "255.255.255.255",
    "0.0.0.0",
    "256.1.1.1",
    "192.168.1",
    "192.168.1.999",
    "192.168.01.1",
    "abc.def.ghi.jkl",
    "192.168.1.1.1"
];

testCases.forEach(ip => {
    console.log(`${ip}: ${isValidIPv4(ip)}`);
});

// Eksport funkcji
module.exports = { isValidIPv4 };
