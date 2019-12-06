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

    letter_container = soup.select('#tab-container-1')[0]
    letter_texts = [div.text for div in letter_container.select('div')]
    letter_text = ' '.join(letter_texts)
    return letter_text


def get_letters(urls):
    letters = []

    for url in urls:
        letters.append(get_letter(url))

    return letters


def save_data(letters):
    with open('vangogh_letters.txt', 'w') as f:
        f.write('\n'.join(letters))


def main():
    # Get URLs to get letter texts from
    url_template = 'http://vangoghletters.org/vg/letters/let{}/letter.html'
    urls = get_urls(url_template, 1, 902)

    # Get letter texts
    letters = get_letters(urls)

    # Save data
    save_data(letters)


if __name__ == '__main__':
    main()
    exit(0)
