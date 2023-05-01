from bs4 import BeautifulSoup
from pprint import pprint
import requests
import csv

# URL de la page à scraper
url = "https://example.com"

# Obtenir le contenu HTML de la page
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Rechercher les éléments souhaités à partir de la page
data = []
rows = soup.select("div.row")
for row in rows:
    title = row.select_one("h2").text.strip()
    description = row.select_one("p").text.strip()
    data.append([title, description])

# Écrire les données extraites dans un fichier CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Titre", "Description"])
    writer.writerows(data)


import requests
from bs4 import BeautifulSoup
import csv

# URL de la première page à scraper
base_url = "https://example.com/page={}"

# Initialisation de la liste des données extraites
data = []

# Boucle pour scraper les dix pages
for i in range(1, 11):
    # Construire l'URL de la page courante
    url = base_url.format(i)

    # Obtenir le contenu HTML de la page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Rechercher les éléments souhaités à partir de la page
    rows = soup.select("div.row")
    for row in rows:
        title = row.select_one("h2").text.strip()
        description = row.select_one("p").text.strip()
        data.append([title, description])

# Écrire les données extraites dans un fichier CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Titre", "Description"])
    writer.writerows(data)


