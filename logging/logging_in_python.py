import logging

# Logger konfigurieren
logger = logging.getLogger('meine_anwendung')
logger.setLevel(logging.DEBUG)  # Globales Log-Level auf DEBUG setzen

# Formatter für Log-Ausgaben
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Konsolen-Handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

# Datei-Handler
file_handler = logging.FileHandler('meine_anwendung.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)

# Handler dem Logger hinzufügen (aber doppelte Einträge vermeiden)
if not logger.handlers:
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

def division(a, b):
    """Führt eine Division durch und protokolliert Fehler bei Division durch Null."""
    logger.debug(f"Starte Division: {a} / {b}")
    try:
        ergebnis = a / b
        logger.info(f"Division erfolgreich: {a} / {b} = {ergebnis}")
        return ergebnis
    except ZeroDivisionError:
        logger.error("Fehler: Division durch Null!", exc_info=True)
        return None
    except Exception as e:
        logger.critical(f"Unerwarteter Fehler bei der Division: {e}", exc_info=True)
        return None

def main():
    logger.info("Anwendung gestartet.")

    # Testfälle
    division(10, 2)
    division(5, 0)
    division(8, 4)
    division('a', 3)  # Fehlerhafter Eingabetyp

    logger.info("Anwendung beendet.")

if __name__ == "__main__":
    main()