def safe_divide(dividend, divisor):
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError:
        return "Fehler: Division durch Null ist nicht erlaubt!"
    except TypeError:
        return "Fehler: Beide Werte müssen numerisch sein!"
    except Exception as e:
        return f"Fehler: Ein unerwarteter Fehler ist aufgetreten: {e}"

# Test 1: Erfolgreiche Division
print("Test 1 - Erfolgreiche Division:")
ergebnis1 = safe_divide(10, 2)
print(f"safe_divide(10, 2) = {ergebnis1}")
print()

# Test 2: Division durch Null
print("Test 2 - Division durch Null:")
ergebnis2 = safe_divide(10, 0)
print(f"safe_divide(10, 0) = {ergebnis2}")
print()

# Test 3: Nicht-numerische Werte (TypeError)
print("Test 3 - Nicht-numerische Werte:")
ergebnis3 = safe_divide(10, "zwei")
print(f"safe_divide(10, 'zwei') = {ergebnis3}")
print()

# Test 4: Weitere erfolgreiche Division mit Gleitkommazahlen
print("Test 4 - Division mit Gleitkommazahlen:")
ergebnis4 = safe_divide(7.5, 2.5)
print(f"safe_divide(7.5, 2.5) = {ergebnis4}")
print()

# Test 5: Beide Werte nicht-numerisch
print("Test 5 - Beide Werte nicht-numerisch:")
ergebnis5 = safe_divide("zehn", "zwei")
print(f"safe_divide('zehn', 'zwei') = {ergebnis5}")