class ResourceManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        # Datei im Schreibmodus öffnen
        self.file = open(self.filename, 'w', encoding='utf-8')
        print(f"Ressource '{self.filename}' wurde geöffnet.")
        return self.file  # gibt die geöffnete Datei zurück

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Datei schließen, auch wenn ein Fehler auftritt
        if self.file:
            self.file.close()
            print(f"Ressource '{self.filename}' wurde freigegeben.")
        # Fehler, falls vorhanden, nicht unterdrücken
        return False


# Verwendung des Kontextmanagers zum Schreiben in die Datei
with ResourceManager('output.txt') as f:
    f.write("Hallo, dies ist ein Testeintrag in die Datei.\n")

# Nun Datei im Lesemodus öffnen und den Inhalt ausgeben
with open('output.txt', 'r', encoding='utf-8') as f:
    print("Dateiinhalt:")
    print(f.read())