import requests
from bs4 import BeautifulSoup


ret = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(ret.text, 'html.parser')

posts = soup.find_all('article')


def find_articles_by_keywords(keywords):
    correct_posts = []
    for post in posts:
        # find post's header text
        post_header = post.find(class_="tm-article-snippet__title-link")
        post_header_text = post_header.find('span').text
        # find link to post
        post_link = 'https://habr.com' + post_header.get('href')
        # get post's full text
        req = requests.get(post_link)
        post_soup = BeautifulSoup(req.text, 'html.parser')
        post_text = ' '.join([line.text.strip() for line in post_soup.find(class_="tm-article-body").find_all('p')])
        # check the condition
        if any(post_text.find(word) + 1 for word in keywords):
            # find post's time
            post_time = post.find('time').get('title')
            correct_posts.append(f'{post_time} - {post_header_text} - {post_link}')
    return correct_posts
