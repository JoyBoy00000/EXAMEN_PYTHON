import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5500/index.html"

reponse = requests.get(url)

if reponse.status_code != 200:
    print("Erreur lors de la récupération de la page")
    exit()
    
soup = BeautifulSoup(reponse.text, 'html.parser')

# 1. scraper les images
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Liste des images :")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
images = soup.find_all('img')
for image in images:
    print(image)

# 2. scaper les titres
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Liste des titres :")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
services = soup.select('.card-service')
for idx, service in enumerate(services, start=1):
    title = service.find('h3').text.strip()
    print(f"Service {idx}: {title} ")

#3. scraper les paragraph
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Liste des paragraph :")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
paragraph = soup.select('.card-service')
for idx, service in enumerate(paragraph, start=1):
    description = service.find('p').text.strip()
    print(f"service {idx}: {description} ")
    

# 4. scraper le formulaire
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Liste des formulaires :")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
from bs4 import BeautifulSoup

 # Charger le fichier HTML local
reponse = requests.get(url)
soup = BeautifulSoup(reponse.text, "html.parser")

 # Trouver le formulaire
form = soup.find("form")

# Trouver tous les champs
inputs = form.find_all(["input", "textarea"])

print("Champs du formulaire :\n")

for champ in inputs:
    placeholder = champ.get("placeholder")

    print(f"Placeholder : {placeholder}")
    print("----")

# 5. scraper les liens
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Liste des liens :")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++")
header_links = [a.get('href') for a in soup.select('header nav a')]
print("Liens de navigation :", header_links)
