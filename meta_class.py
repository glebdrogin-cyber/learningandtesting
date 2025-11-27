# ==========================================
# 1. Aufgabe: EnsureMethodMeta
# ==========================================

# Metaklasse, die überprüft, ob eine Methode 'required_method' vorhanden ist
class EnsureMethodMeta(type):
    def __new__(mcls, name, bases, namespace):
        # Prüfen, ob die Methode 'required_method' definiert ist
        if 'required_method' not in namespace:
            raise TypeError(f"Klasse '{name}' muss eine Methode 'required_method' implementieren.")
        return super().__new__(mcls, name, bases, namespace)


# Klasse, die die Metaklasse verwendet und korrekt 'required_method' implementiert
class MyClass(metaclass=EnsureMethodMeta):
    def required_method(self):
        return "Methode erfolgreich implementiert!"

# Test
obj = MyClass()
print(obj.required_method())  # Ausgabe: Methode erfolgreich implementiert!


# Optional: Eine Klasse, die absichtlich KEINE required_method implementiert
# (Dieser Code sollte auskommentiert bleiben, um keinen Fehler auszulösen.)
#
# class InvalidClass(metaclass=EnsureMethodMeta):
#     pass
#
# Wenn aktiviert, würde folgender Fehler auftreten:
# TypeError: Klasse 'InvalidClass' muss eine Methode 'required_method' implementieren.


# ==========================================
# 2. Aufgabe: SingletonMeta
# ==========================================

# Metaklasse, die sicherstellt, dass nur eine Instanz existiert
class SingletonMeta(type):
    _instances = {}  # Dictionary, um Instanzen zu speichern

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            # Falls noch keine Instanz existiert, wird sie erzeugt
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


# Klasse, die SingletonMeta verwendet
class SingletonClass(metaclass=SingletonMeta):
    def __init__(self):
        self._id = id(self)

    def get_instance_id(self):
        return self._id


# Test: Mehrfaches Erzeugen führt zur selben Instanz
a = SingletonClass()
b = SingletonClass()

print(f"ID von a: {a.get_instance_id()}")
print(f"ID von b: {b.get_instance_id()}")

# Überprüfung: beide sollten identisch sein
print("Beide sind dieselbe Instanz:", a is b)

