def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        raise ValueError(f"Fehler: Division durch Null ist nicht erlaubt! "
                        f"Es wurde versucht, {a} durch {b} zu teilen.")