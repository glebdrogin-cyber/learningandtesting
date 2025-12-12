import asyncio
import random
import os

# -------------------------------------------------------
# Teil 1: Asynchrone Datenabfrage
# -------------------------------------------------------

async def fetch_weather_data(city: str) -> dict:
    """
    Simuliert eine asynchrone Wetterdatenabfrage für eine Stadt.
    """
    await asyncio.sleep(random.uniform(0.5, 1.5))  # simuliert Netzwerkwartezeit
    temperature = round(random.uniform(-10, 35), 1)  # zufällige Temperatur
    return {"city": city, "temperature": temperature}


async def process_weather_data(cities: list[str]):
    """
    Ruft fetch_weather_data für jede Stadt parallel auf und sammelt die Ergebnisse.
    """
    tasks = [fetch_weather_data(city) for city in cities]
    results = await asyncio.gather(*tasks)

    print("\n=== Wetterdaten ===")
    for item in results:
        print(f"{item['city']}: {item['temperature']}°C")


# -------------------------------------------------------
# Teil 2: Rekursive Dateisuche
# -------------------------------------------------------

def list_files(directory: str) -> list[str]:
    """
    Listet alle Dateien in einem Verzeichnis und dessen Unterverzeichnissen auf.
    Nutzt Rekursion.
    """
    files = []

    for entry in os.listdir(directory):
        path = os.path.join(directory, entry)

        if os.path.isfile(path):
            files.append(path)
        elif os.path.isdir(path):
            # Rekursion in Unterverzeichnis
            files.extend(list_files(path))

    return files


# -------------------------------------------------------
# Hauptprogramm
# -------------------------------------------------------

if __name__ == "__main__":
    # Teil 1 ausführen
    cities = ["Berlin", "Hamburg", "München", "Köln", "Frankfurt"]
    asyncio.run(process_weather_data(cities))

    # Teil 2 ausführen
    print("\n=== Gefundene Dateien ===")
    directory_to_search = "."  # aktuelles Verzeichnis
    all_files = list_files(directory_to_search)

    for f in all_files:
        print(f)
