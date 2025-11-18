# Variablen definieren
name = "John Doe"
alter = 28
groesse = 1.82
ist_student = False
lieblingszahl = 7
geburtsjahr = 1995
wohnort = "Berlin"
durchschnittsnote = 2.5
hat_fuehrerschein = True
telefonnummer = "123-456-7890"

# Werte und Datentypen ausgeben
print("Name:", name, "| Datentyp:", type(name))
print("Alter:", alter, "| Datentyp:", type(alter))
print("Größe:", groesse, "| Datentyp:", type(groesse))
print("Ist Student:", ist_student, "| Datentyp:", type(ist_student))
print("Lieblingszahl:", lieblingszahl, "| Datentyp:", type(lieblingszahl))
print("Geburtsjahr:", geburtsjahr, "| Datentyp:", type(geburtsjahr))
print("Wohnort:", wohnort, "| Datentyp:", type(wohnort))
print("Durchschnittsnote:", durchschnittsnote, "| Datentyp:", type(durchschnittsnote))
print("Hat Führerschein:", hat_fuehrerschein, "| Datentyp:", type(hat_fuehrerschein))
print("Telefonnummer:", telefonnummer, "| Datentyp:", type(telefonnummer))

# --- Teil 1: Berechnungen ---
# a) Alter in 5 Jahren
alter_in_5_jahren = alter + 5

# b) Angepasste Größe (um 10 % erhöht)
angepasste_groesse = groesse * 1.1

print("\n--- Berechnungen ---")
print("In 5 Jahren ist die Person", alter_in_5_jahren, "Jahre alt.")
print("Die angepasste Größe beträgt:", round(angepasste_groesse, 2), "Meter.")

# --- Teil 2: String-Slicing ---
erster_buchstabe = name[0]

print("\n--- String-Slicing ---")
print("Der erste Buchstabe des Namens ist:", erster_buchstabe)
