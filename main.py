import requests
from bs4 import BeautifulSoup


url = "https://www.ebay.com/sch/i.html?_nkw=mac%20book%202019%20&_sacat=0&_from=R40&rt=nc&_udlo=100&_udhi=120"
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    for data in soup.find_all('div', {"class": "s-item__wrapper clearfix"}):
        name = data.find('span', {"role": "heading"})
        print(f"PRODUCT NAME: {name.text.strip()}")
        price = data.find("span", {"class": "s-item__price"})
        print(f"PRODUCT PRICE: {price.text.strip()}")
        img = data.find('img')
        if img:
            image = img.get("src")
            print(f"PRODUCT IMAGE: {image.strip()}")
        url = data.find('a')
        if url:
            link = url.get('href')
            print(f"PRODUCT LINK: {link.strip()}")
            
        print("\n")
