from habr_scraping import find_articles_by_keywords

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

if __name__ == '__main__':
    print(*find_articles_by_keywords(KEYWORDS), sep='\n')
