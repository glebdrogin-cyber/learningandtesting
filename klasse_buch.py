class Buch:
    def __init__(self, titel, autor, isbn, verfuegbar=True):
        self.titel = titel
        self.autor = autor
        self.isbn = isbn
        self.verfuegbar = verfuegbar

    def ausleihen(self):
        if self.verfuegbar:
            self.verfuegbar = False
            print(f"Das Buch '{self.titel}' wurde ausgeliehen.")
        else:
            print(f"Das Buch '{self.titel}' ist derzeit nicht verfügbar.")

    def zurueckgeben(self):
        if not self.verfuegbar:
            self.verfuegbar = True
            print(f"Das Buch '{self.titel}' wurde zurückgegeben.")
        else:
            print(f"Das Buch '{self.titel}' war bereits verfügbar.")


# Erstellen von mindestens drei Buchobjekten
buch1 = Buch("Der kleine Prinz", "Antoine de Saint-Exupéry", "978-3-551-20000-0")
buch2 = Buch("1984", "George Orwell", "978-3-453-45123-0")
buch3 = Buch("Harry Potter und der Stein der Weisen", "J.K. Rowling", "978-3-551-35401-7")

# Demonstration des Funktionswechsels
buch1.ausleihen()       # sollte verfügbar -> ausgeliehen
buch1.ausleihen()       # nochmal ausleihen -> nicht verfügbar
buch1.zurueckgeben()    # wieder verfügbar

print()  # Leerzeile für bessere Lesbarkeit

buch2.ausleihen()
buch2.zurueckgeben()

print()

buch3.ausleihen()
buch3.zurueckgeben()
