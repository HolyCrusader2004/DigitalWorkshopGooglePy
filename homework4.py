import requests
from bs4 import BeautifulSoup

website = "https://f1manager.ro/clasament-formula-1"
r = requests.get(website)

soup = BeautifulSoup(r.content, 'html.parser')


box = soup.find('table', attrs={'class': 'resultsarchive-table'})
teams = []
with open('homework4.txt', 'w') as file:

    for row in box.find_all('tr')[1:]:
        plasament = row.find('td', attrs={'class': 'dark'}).text
        nume = row.find('span', attrs={'class': 'hide-for-tablet'}).text
        prenume = row.find('span', attrs={'class': 'hide-for-mobile'}).text
        nationality = row.find('td', attrs={'class': 'dark semi-bold uppercase'}).text
        car = row.find('a', attrs={'class': 'grey semi-bold uppercase ArchiveLink'}).text
        points = row.find('td', attrs={'class': 'dark bold'}).text
        teams.append({
            'Placement': plasament,
            'First Name': nume,
            'Last Name': prenume,
            'Nationality': nationality,
            'Car': car,
            'Points': points
        })
        file.write(f"{plasament},{nume},{prenume},{nationality},{car},{points}\n")
# print(teams)


def showinfo(nume_fisier):
    with open(nume_fisier, 'r') as file:
        for line in file.readlines():
            print(line)


def modifyinfo(nume_fisier, modificare):
    with open(nume_fisier, 'r') as file:
        line = file.readlines()
    with open(nume_fisier, 'w') as file:
        for linie in line:
            linie = linie.strip() + modificare + '\n'
            file.write(linie)


modifyinfo('homework4.txt', 'modificare')
