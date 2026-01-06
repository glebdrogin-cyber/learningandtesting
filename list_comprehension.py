farben = ["rot", "grün", "blau"]
gegenstaende = ["Auto", "Haus", "Baum"]

produkt = [(farbe, gegenstand) for farbe in farben for gegenstand in gegenstaende]
print(produkt)