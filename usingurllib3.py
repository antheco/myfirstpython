import urllib3
from bs4 import BeautifulSoup
http = urllib3.PoolManager()
r = http.request('GET', 'https://www.tutorialspoint.com/python_web_scraping/python_modules_for_web_scraping.htm')
soup = BeautifulSoup(r.data, 'xml')
print (soup.title)
print (soup.title.text)
for link in soup.find_all('a'):
    print(link.get('href'))
import builtwith
builtwith.parse('http://wordpress.com')
