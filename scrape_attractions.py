import requests
from bs4 import BeautifulSoup

url = "https://disneyworld.disney.go.com/attractions/#/magic-kingdom,epcot,hollywood-studios,animal-kingdom/sort=alpha/"

# Make HTTP GET request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Find all finder-list-card elements
finder_cards = soup.find_all('finder-list-card')

# Iterate over each finder-list-card and extract relevant information
for card in finder_cards:
    name = card.find(class_='name').text.strip()
    park = card.find(class_='location').text.strip()
    hours = card.find(class_='time-range').text.strip()
    height_restrictions = card.find(class_='facets').text.strip()
    
    # Print extracted information
    print("Name:", name)
    print("Park:", park)
    print("Hours:", hours)
    print("Height Restrictions:", height_restrictions)
    print("-------------")
