import requests
from bs4 import BeautifulSoup


response = requests.get('https://habr.com/')
# print(response.status_code)

KEYWORDS = {'дизайн', 'фото', 'web', 'Python', 'C++'}
soup = BeautifulSoup(response.text, features='html.parser')

articles = soup.find_all('article')
# print(articles)
for article in articles:
    hubs = article.find_all('span', class_="tm-article-snippet__hubs-item")
    hubs = set([hub.find('span').text for hub in hubs])
    if KEYWORDS & hubs:
        print('---')
        header = article.find('h2').text
        # print(header)
        link = article.find('a', class_="tm-article-snippet__title-link")
        # print(link.get('href'))
        published = article.find('span', class_="tm-article-snippet__datetime-published")
        published = (pub.get('time').text for pub in published)
        # print(published)
        print(f'Дата:{published} - Заголовок:{header} - Ссылка:{link.get("href")}')












