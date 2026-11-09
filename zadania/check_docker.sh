Bash
#!/bin/bash

# Sprawdzenie, czy usługa Docker jest aktywna
if systemctl is-active --quiet docker; then
    echo "Usługa Docker już działa."
else
    echo "Usługa Docker jest wyłączona. Próbuję ją uruchomić..."
    sudo systemctl start docker
    
    # Weryfikacja, czy uruchomienie się powiodło
    if systemctl is-active --quiet docker; then
        echo "Usługa Docker została pomyślnie uruchomiona."
    else
        echo "Błąd: Nie udało się uruchomić usługi Docker." >&2
        exit 1
    fi
fi