import requests
from bs4 import BeautifulSoup

url = "https://www.arise.tv/category/tech/"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup.prettify())
    for data in soup.find_all('article'):
        # print(data)
        title = data.find('h3')
        if title:
            print(title.text.strip())
        link = data.find('a')
        if link:
            print(link.get('href'))
        img = data.find('img')
        if img:
            print(img.get('src'))
            
        print("\n")
