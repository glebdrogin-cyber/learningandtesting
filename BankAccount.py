class BankAccount:
    def __init__(self, inhaber, anfangs_kontostand):
        self.inhaber = inhaber
        self.kontostand = anfangs_kontostand
        print(f"Konto für {self.inhaber} wurde mit {self.kontostand:.2f}€ erstellt.")
    def deposit(self, betrag):
        if betrag > 0:
            self.kontostand += betrag
            print(f"{betrag:.2f}€ eingezahlt. Neuer Kontostand: {self.kontostand:.2f}€")
        else:
            print("Der Einzahlungsbetrag muss positiv sein.")
    def withdraw(self, betrag):
        if betrag <= 0:
            print("Der Auszahlungsbetrag muss positiv sein.")
        elif betrag > self.kontostand:
            print("Fehler: Nicht genügend Guthaben.")
        else:
            self.kontostand -= betrag
            print(f"{betrag:.2f}€ abgehoben. Neuer Kontostand: {self.kontostand:.2f}€")
    def display_balance(self):
        print(f"Aktueller Kontostand von {self.inhaber}: {self.kontostand:.2f}€")
# Beispielverwendung
konto1 = BankAccount("Max Mustermann", 1000)
konto1.deposit(250)
konto1.withdraw(100)
konto1.withdraw(2000)  # sollte Fehlermeldung geben
konto1.display_balance()