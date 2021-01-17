import requests
r = requests.get('https://www.tutorialspoint.com/python_web_scraping/python_modules_for_web_scraping.htm')
print(r.text[:200])