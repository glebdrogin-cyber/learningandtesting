def calculate_discounted_price(price, discount):
    if price < 0:
        raise ValueError("Der Preis darf nicht negativ sein.")
    if discount < 0 or discount > 100:
        raise ValueError("Der Rabatt muss zwischen 0 und 100 Prozent liegen.")
    return price * (1 - discount / 100)


def apply_tax(price, tax_rate):
    if price < 0:
        raise ValueError("Der Preis darf nicht negativ sein.")
    if tax_rate < 0:
        raise ValueError("Der Steuersatz darf nicht negativ sein.")

    return price * (1 + tax_rate / 100)
