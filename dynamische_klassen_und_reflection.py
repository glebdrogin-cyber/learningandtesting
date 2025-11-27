import inspect
from types import MethodType

# ===========================================
# Teil 1: Dynamische Klassenerzeugung & Reflection
# ===========================================

def create_class(class_name, attributes):
    """
    Erzeugt zur Laufzeit eine Klasse mit dem gegebenen Namen und Attributen.
    attributes ist ein Dictionary mit Attributnamen und -werten oder -methoden.
    """
    # Dynamische Klassenerzeugung mit type()
    return type(class_name, (object,), attributes)

# Beispielattribut und Methode für die neue Klasse
def print_msg(self):
    print(f"Nachricht: {self.msg}")

# Klasse dynamisch erzeugen
MyDynamicClass = create_class("MyDynamicClass", {
    "msg": "Hallo, ich bin eine dynamisch erzeugte Klasse!",
    "print_msg": print_msg
})

# Instanz erstellen
instance = MyDynamicClass()

# Methode aufrufen
instance.print_msg()

# Reflection: Alle Attribute und Methoden auflisten
print("\n--- Mitglieder der Instanz (Reflection) ---")
for name, member in inspect.getmembers(instance):
    if not name.startswith("__"):
        print(f"{name}: {member}")

# Neues Attribut und neue Methode dynamisch hinzufügen
setattr(instance, "new_attr", "Ich wurde nachträglich hinzugefügt!")

def new_method(self):
    print("Dies ist eine neue Methode, die nachträglich hinzugefügt wurde!")

# Methode dynamisch binden (MethodType nötig, damit self korrekt übergeben wird)
setattr(instance, "new_method", MethodType(new_method, instance))

# Überprüfung
print("\n--- Nachträglich hinzugefügte Elemente ---")
print("new_attr:", instance.new_attr)
instance.new_method()

# ===========================================
# Teil 2: Einfaches Plugin-System
# ===========================================

class Plugin:
    def run(self):
        print("Running plugin")

def load_plugin(plugin):
    """
    Modifiziert das Verhalten der run()-Methode eines Plugin-Objekts zur Laufzeit.
    """
    def modified_run(self):
        print("Running modified plugin")
    
    # Methode überschreiben
    plugin.run = MethodType(modified_run, plugin)

# Plugin-System testen
print("\n--- Plugin-System-Test ---")
plugin = Plugin()
plugin.run()            # Original
load_plugin(plugin)
plugin.run()            # Modifiziert
