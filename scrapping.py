import requests
from bs4 import BeautifulSoup
import csv


url = "https://sleyter.fr/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

projects = []
for project in soup.find_all('div', class_='col-md-4'):
    name = project.find('h2', class_='w-title').get_text()
    subtitle = project.find('span', class_='w-ctegory').get_text()
    date = project.find('span', class_='w-date').get_text()
    projects.append({'name': name, 'subtitle': subtitle, 'date': date})


# Écriture des informations des projets dans un fichier CSV
with open('projects.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name :', 'Subtitle :', 'Date :'])
    for project in projects:
        writer.writerow([project['name'], project['subtitle'], project['date']])

