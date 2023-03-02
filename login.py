from requests import Session
from bs4 import BeautifulSoup
from time import sleep

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }

work = Session()

# make coockies
work.get('http://quotes.toscrape.com/', headers=headers)
# go for login
response = work.get('http://quotes.toscrape.com/login', headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
token = soup.find('form').find('input').get('value')

data_for_login = {
'csrf_token': token,
'username' : '123',
'password' : '456'
}
print(token)