import requests
from bs4 import BeautifulSoup


URL = 'https://habr.com'
response = requests.get(URL)


KEYWORDS = {'дизайн', 'фото', 'web', 'Python', 'C++'}
soup = BeautifulSoup(response.text, features='html.parser')

articles = soup.find_all('article')

for article in articles:
    hubs = article.find_all('span', class_="tm-article-snippet__hubs-item")
    hubs = set([hub.find('span').text for hub in hubs])
    link = article.find('a', class_="tm-article-snippet__title-link")
    new_link = f"{URL}{link.get('href')}"
    res = requests.get(new_link)
    s = BeautifulSoup(res.text, features='html.parser')
    text = s.find_all('div', class_="tm-article-presenter__body")

    for a in text:
        if KEYWORDS & hubs:
            published = a.find('span', class_="tm-article-snippet__datetime-published")
            published = published.find('time')['title']
            header = a.find('h1', class_="tm-article-snippet__title tm-article-snippet__title_h1")
            header = header.find('span').text
            print(f'Дата:{published} - Заголовок:{header} - Ссылка:{new_link}')
