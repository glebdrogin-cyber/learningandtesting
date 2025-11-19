import os
from datetime import datetime

def check_and_create_file(filename, default_content):

    # Überprüft, ob eine Datei existiert, und erstellt sie bei Bedarf.
    
    # Args:
    #    filename: Name der zu prüfenden Datei
    #    default_content: Inhalt, der bei Neuerstellung geschrieben wird
    
    # Returns:
    #    bool: True wenn Datei existiert oder erstellt wurde, False bei Fehler

    try:
        if not os.path.exists(filename):
            print(f"Datei '{filename}' existiert nicht. Erstelle neue Datei...")
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(default_content)
            print(f"Datei '{filename}' wurde erfolgreich erstellt.")
            return True
        else:
            print(f"Datei '{filename}' existiert bereits.")
            return True
    except PermissionError:
        print(f"FEHLER: Keine Berechtigung zum Erstellen der Datei '{filename}'.")
        return False
    except Exception as e:
        print(f"FEHLER beim Erstellen der Datei '{filename}': {e}")
        return False

def backup_file(source_file, backup_file):

    #Erstellt ein Backup einer Datei durch Kopieren des Inhalts.
    
    #Args:
    #    source_file: Quelldatei zum Lesen
    #    backup_file: Zieldatei für das Backup
    
    #Returns:
    #    bool: True bei Erfolg, False bei Fehler

    try:
        with open(source_file, 'r', encoding='utf-8') as source:
            content = source.read()
        
        with open(backup_file, 'w', encoding='utf-8') as backup:
            backup.write(content)
        
        print(f"Backup erfolgreich: '{source_file}' → '{backup_file}'")
        return True
    except FileNotFoundError:
        print(f"FEHLER: Datei '{source_file}' nicht gefunden.")
        return False
    except PermissionError:
        print(f"FEHLER: Keine Berechtigung zum Lesen/Schreiben der Dateien.")
        return False
    except Exception as e:
        print(f"FEHLER beim Backup: {e}")
        return False

def log_backup(log_file, source_file, backup_file, success):

    #Protokolliert den Backup-Vorgang mit Zeitstempel.
    
    #Args:
    #    log_file: Name der Log-Datei
    #    source_file: Name der Quelldatei
    #    backup_file: Name der Backup-Datei
    #    success: Boolean, ob Backup erfolgreich war

    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "ERFOLGREICH" if success else "FEHLGESCHLAGEN"
        log_entry = f"[{timestamp}] Backup {status}: '{source_file}' → '{backup_file}'\n"
        
        with open(log_file, 'a', encoding='utf-8') as log:
            log.write(log_entry)
        
        print(f"Log-Eintrag wurde zu '{log_file}' hinzugefügt.")
    except PermissionError:
        print(f"FEHLER: Keine Berechtigung zum Schreiben in '{log_file}'.")
    except Exception as e:
        print(f"FEHLER beim Logging: {e}")

def main():
    #"""
    #Hauptfunktion: Führt alle Schritte des Backup-Prozesses aus.
    #"""
    
    # Dateinamen definieren
    data_file = "daten.txt"
    backup_filename = "backup.txt"
    log_filename = "log.txt"
    
    # Beispieltext für neue daten.txt
    default_content = """Dies ist ein Beispieltext für die Datendatei.
Hier können verschiedene Informationen gespeichert werden.
Datum: """ + datetime.now().strftime("%Y-%m-%d") + """
Status: Aktiv

Weitere Beispieldaten:
- Zeile 1
- Zeile 2
- Zeile 3
"""
    
    # Schritt 1: Datei prüfen und ggf. erstellen
    print("\n[Schritt 1] Überprüfe Existenz von 'daten.txt'...")
    if not check_and_create_file(data_file, default_content):
        print("\nProgramm wird aufgrund von Fehlern beendet.")
        return
    
    # Schritt 2: Backup erstellen
    print("\n[Schritt 2] Erstelle Backup...")
    backup_success = backup_file(data_file, backup_filename)
    
    # Schritt 3: Logging
    print("\n[Schritt 3] Protokolliere Backup-Vorgang...")
    log_backup(log_filename, data_file, backup_filename, backup_success)

if __name__ == "__main__":
    main()