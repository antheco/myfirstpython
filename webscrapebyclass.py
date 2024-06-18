from bs4 import BeautifulSoup
import requests
website = requests.get('https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/')
soup = BeautifulSoup(website.content, 'html.parser')
my_classes = soup.find_all(class_ = 'menuitm')
for soups in my_classes:
 	print(soups.string)