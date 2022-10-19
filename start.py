import requests
import bs4

r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
 
print(r)

soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())