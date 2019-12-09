"""
Build a corpus consisting of the letters of Vincent Van Gogh from the website
http://vangoghletters.org.
Heikal Badrulhisham 2019, <heikal93@gmail.com>
"""
import requests
from bs4 import BeautifulSoup


def get_urls(url_template, first, last):
    """
    Get URLs of webpages containing letters. Helper method for main().
    :param url_template: string template of letter webpage URLs
    :param first: first index that goes into URL template
    :param last: last index that goes into URL template
    :return: list of URLs containing indices of letters
    """
    urls = []

    for i in range(first, last+1):
        index = f'00{i}'[-3:]
        url = url_template.format(index)
        urls.append(url)

    return urls


def get_letter(url):
    """
    Get the letter text from the webpage of the given URL. Helper method for
    get_letters().
    :param url: URL of the webpage containing the letter
    :return: the text content of the letter
    """
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    # Element containing the letter
    letter_container = soup.select('#tab-container-1')[0]

    # Delete unneeded elements on the website
    to_delete = ['span.anchor', 'span.pagebreak']
    delete_elements(letter_container, to_delete)

    # Combine texts from different elements
    letter_texts = [div.text for div in letter_container.select('div')]
    letter_texts = [' '.join(t.split()) for t in letter_texts]
    letter_text = ' '.join(letter_texts)

    return letter_text


def delete_elements(soup, selectors):
    """
    Delete specified webpage elements from another webpage element.
    :param soup: BeautifulSoup object of the webpage element to delete from.
    :param selectors: selectors of elements to delete.
    """
    for selector in selectors:
        elements = soup.select(selector)

        if elements:
            for element in elements:
                element.decompose()


def get_letters(urls):
    """
    Get a list of letters from a list of URLs. Helper method for main().
    :param urls: list of URLs of webpages containing letters.
    :return: list of letters
    """
    return [get_letter(url) for url in urls]


def save_data(letters, filename):
    """
    Save corpus data to a file. Helper method for main()
    :param letters: list of letters (string)
    :param filename: name of the file to be saved
    """
    with open(filename, 'w') as f:
        f.write('\n'.join(letters))


def main():
    """
    Get URLs of webpages containing letters. Get text content of letters from
    said webpages. Save corpus data to a file.
    """
    # Get URLs to get letter texts from
    url_template = 'http://vangoghletters.org/vg/letters/let{}/letter.html'
    urls = get_urls(url_template, 1, 902)

    # Account for quirk of the website's listing
    urls.insert(1, url_template.format('001a'))

    # Get letter texts
    letters = get_letters(urls[:5])

    # Save data
    save_data(letters, 'vangogh_letters.txt')


if __name__ == '__main__':
    main()
    exit(0)
