class Calculator:
    """Einfache Taschenrechner-Klasse mit Grundrechenarten."""

    def add(self, a: float, b: float) -> float:
        """Gibt die Summe von a und b zurück."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Gibt die Differenz von a und b zurück."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Gibt das Produkt von a und b zurück."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Gibt den Quotienten von a und b zurück. 
        Wirft ValueError bei Division durch Null."""
        if b == 0:
            raise ValueError("Division durch Null ist nicht erlaubt.")
        return a / b
