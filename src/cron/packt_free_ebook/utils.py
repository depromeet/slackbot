import os
from bs4 import BeautifulSoup

PACKT_URL = 'https://www.packtpub.com/packt/offers/free-learning'


def _get_today_free_ebook_title():
    os.system('curl -sS {} > /tmp/packt.txt'.format(PACKT_URL))
    page_content = open('/tmp/packt.txt', 'r', encoding='utf8')
    html = BeautifulSoup(page_content, 'html.parser')

    page_content.close()
    os.remove('/tmp/packt.txt')

    title = html.find(
        'div',
        attrs={
            'class': 'dotd-title'
        }
    )

    return title.text.strip()


def get_today_free_ebook():
    title = _get_today_free_ebook_title()
    return ':star: 오늘의 무료책 :star:\n*{}*\n{}'.format(title, PACKT_URL)


def main():
    print(_get_today_free_ebook_title())
    print(get_today_free_ebook())


if __name__ == '__main__':
    main()
