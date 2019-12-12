"""
Generate texts using a Markov chain based on a corpus of letters by Vincent
Van Gogh.
Heikal Badrulhisham, 2019 <heikal93@gmail.com>
"""

import re
from collections import defaultdict
import random
from nltk import bigrams


def preprocess_corpus(texts):
    """
    Insert sentence boundary indicators between sentences in a corpus. Helper
    method for main().
    :param texts: List of texts (string)
    :return: corpus with sentence boundary indicators inserted between
    sentences.
    """
    new_corpus = []

    for text in texts:
        for symbol in ['\.', '\?', '!', ':', ';']:
            text = re.sub(f'{symbol}+\s+', '. <b> ', text)

        text = f'<b> {text} <b>'
        new_corpus.append(text)

    return new_corpus


def get_sentence_lengths(texts):
    """
    Get possible sentence lengths from a corpus. Helper method for main().
    :param texts: list of texts (string)
    :return: list of sentence lengths in the corpus
    """
    lengths = []

    for text in texts:
        sentences = re.split('[!?.]+\s*', text)

        for sentence in sentences:
            words = sentence.split(' ')

            if len(words):
                lengths.append(len(words))

    return lengths


def make_markov_chain(texts):
    """
    Create a Markov chain for word transitions in a corpus. Helper method for
    main().
    :param texts: list of texts (string)
    :return: Markov chain in the form of a dictionary where the key are words
    and the values are lists of word bigrams that can follow key words.
    """
    # Break corpus into words
    words = [word for text in texts for word in text.split()]

    # Get current words and their following word bigrams
    prevs, nexts = words[:-2], bigrams(words[1:])

    # Create dictionary of word transitions
    markov_chain = defaultdict(list)

    for prev, next in zip(prevs, nexts):
        markov_chain[prev].append(next)

    return markov_chain


def generate_text(markov_chain, lengths):
    """
    Generate a sentence based on a given Markov chain. Helper method for main()
    :param markov_chain: dictionary of word transitions where the keys are
    words and the values are lists of word bigrams that can follow key words
    :param lengths: list of possible sentence lengths in a corpus. This is to
    limit generated sentences to more reasonable lengths.
    :return: generated sentence (string)
    """
    # Get the number of words of the sentence to generate
    length = random.choice(lengths)

    # Start with sentence boundary
    curr = '<b>'
    sentence = []

    # Get next words using the Markov chain
    while True:
        next = random.choice(markov_chain[curr])
        sentence.append(next[0])
        sentence.append(next[1])
        curr = next[1]

        # Stop when the sentence boundary is encountered again
        if '<b>' in next:
            # Remove sentence boundary
            if next[0] == '<b>':
                sentence.pop()
                sentence.pop()
            else:
                sentence.pop()

            # Done if the sentence is near the specified word count
            if length - 2 <= len(sentence) <= length + 2:
                break
            # If the sentence is too short/too long, start again
            else:
                sentence.clear()

    return ' '.join(sentence).capitalize()


def main():
    # Get corpus of letters
    with open('vangogh_letters.txt', 'r') as f:
        letters = f.read().split('\n')

    # Insert sentence boundaries between sentences in the corpus
    letters = preprocess_corpus(letters)

    # Get possible sentence lengths
    lengths = get_sentence_lengths(letters)

    # Build Markov chain
    markov_chain = make_markov_chain(letters)

    # Generate texts based on said Markov chain
    for i in range(20):
        sent = generate_text(markov_chain, lengths)
        print(sent, '\n')


if __name__ == '__main__':
    main()
    exit(0)
