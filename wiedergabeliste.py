# 1. Erstelle eine Liste mit Seriennamen
wiedergabeliste = ['Breaking Bad', 'Stranger Things', 'The Crown']

# 2. Funktion zur formatierten Ausgabe der Wiedergabeliste
def zeige_wiedergabeliste():
    print("\nAktuelle Netflix-Wiedergabeliste:")
    for index, serie in enumerate(wiedergabeliste, start=1):
        print(f"{index}. {serie}")
    print("-" * 40)

# Ausgabe der initialen Wiedergabeliste
zeige_wiedergabeliste()

# 3. Neue Serie hinzufügen
print("Füge 'The Witcher' zur Wiedergabeliste hinzu...")
wiedergabeliste.append('The Witcher')
zeige_wiedergabeliste()

# 4. Eine Serie entfernen
print("Entferne 'Breaking Bad' aus der Wiedergabeliste...")
if 'Breaking Bad' in wiedergabeliste:
    wiedergabeliste.remove('Breaking Bad')
else:
    print("'Breaking Bad' wurde nicht in der Wiedergabeliste gefunden.")
zeige_wiedergabeliste()
