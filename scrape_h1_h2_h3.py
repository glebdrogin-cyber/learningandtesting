import requests
from bs4 import BeautifulSoup
import pandas as pd

def extract_headings(url):
    # Webseite abrufen
    response = requests.get(url)
    response.raise_for_status()  # Fehler werfen, falls Request fehlschlägt

    # HTML parsen
    soup = BeautifulSoup(response.text, "html.parser")

    # Überschriften sammeln
    headings_data = []
    for tag in ["h1", "h2", "h3"]:
        for heading in soup.find_all(tag):
            headings_data.append({
                "tag": tag,
                "text": heading.get_text(strip=True)
            })

    # DataFrame erstellen
    df = pd.DataFrame(headings_data)
    return df


if __name__ == "__main__":
    url = "https://www.berliner-zeitung.de"
    df_headings = extract_headings(url)

    # DataFrame auf der Konsole ausgeben
    print(df_headings)