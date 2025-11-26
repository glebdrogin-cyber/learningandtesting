import time
import functools

# -----------------------------------------
# Dekorator 1: error_handler
# -----------------------------------------
def error_handler(func):
    """Fängt Fehler in der Funktion ab und gibt eine Fehlermeldung aus."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"⚠️ Fehler in '{func.__name__}': {e}")
            return None
    return wrapper


# -----------------------------------------
# Dekorator 2: performance_monitor
# -----------------------------------------
def performance_monitor(func):
    """Misst und gibt die Ausführungszeit der Funktion in Sekunden aus."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"⏱️ Ausführungszeit von '{func.__name__}': {end_time - start_time:.2f} Sekunden")
        return result
    return wrapper


# -----------------------------------------
# Beispiel 1: divide – nutzt error_handler
# -----------------------------------------
@error_handler
def divide(x, y):
    """Teilt zwei Zahlen."""
    return x / y


# -----------------------------------------
# Beispiel 2: slow_function – nutzt performance_monitor
# -----------------------------------------
@performance_monitor
def slow_function():
    """Simuliert eine langsame Funktion."""
    time.sleep(2)
    return "Fertig!"


# -----------------------------------------
# Test der beiden Dekoratoren
# -----------------------------------------
if __name__ == "__main__":
    print("=== Test: divide ===")
    print("10 / 2 =", divide(10, 2))
    print("10 / 0 =", divide(10, 0))  # Sollte Fehler abfangen

    print("\n=== Test: slow_function ===")
    result = slow_function()
    print("Ergebnis:", result)
