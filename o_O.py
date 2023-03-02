import requests
from bs4 import BeautifulSoup
from time import sleep


# to hide our system`s `info
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }


def load_pics(url):
    resp = requests.get(url, stream=True)
    with open(r'/Users/vf585/Desktop/My_projects/Scraping/Images/'+ url.split('/')[-1], 'wb') as f:
        for value in resp.iter_content(1024*1024):
            f.write(value)


def get_url():
    for count in range(1, 8):
        # don`t be in hurry be like human wait for 2sec
        sleep(1)
        url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'
        # get page 
        response = requests.get(url, headers=headers)
        # convert to text
        soup = BeautifulSoup(response.text, 'lxml')
        # getting cards of skuies
        data = soup.find_all('div', class_="col-lg-4 col-md-6 mb-4")

        for i in data:
            # getting url for card of sku 
            page_url = 'https://scrapingclub.com' + i.find('a').get('href')
            yield page_url
        # get name for sku
        #name = i.find('h4', class_='card-title').text.strip()
        # get price for sku
        #price = i.find('h5').text.strip()
        #cget url for img of sku
        #url_img = 'https://scrapingclub.com' + i.find('img', class_="card-img-top img-fluid").get('src')

def array_goods():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)
        # don`t be in hurry be like human wait for 2sec
        sleep(1)
        # convert to text
        soup = BeautifulSoup(response.text, 'lxml')
        # getting card of sku
        data = soup.find('div', class_="card mt-4 my-4")
        name = data.find('h3', class_='card-title').text.strip()
        price = data.find('h4').text.strip()
        url_img = 'https://scrapingclub.com' + data.find('img', class_="card-img-top img-fluid").get('src')
        description = data.find('p', class_="card-text").text.strip()
        load_pics(url_img)
        print(name, price, url_img, description)
        yield name, price, url_img, description 