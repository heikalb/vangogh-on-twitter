import requests
from bs4 import BeautifulSoup

def get_urls(url_template, first, last):
    urls = []

    for i in range(first, last+1):
        index = f'00{i}'[-3:]
        url = url_template.format(index)
        urls.append(url)

    return urls


def get_letter(url):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    letter_container = soup.select('#tab-container-1')
    print(letter_container)




def get_letters(urls):
    letters = []

    for url in urls:
        letters.append(get_letter(url))

    return letters


def main():
    # Get URLs to get letter texts from
    url_template = 'http://vangoghletters.org/vg/letters/let{}/letter.html'
    urls = get_urls(url_template, 1, 902)

    letters = get_letters(urls)
    return


if __name__ == '__main__':
    main()
    exit(0)
