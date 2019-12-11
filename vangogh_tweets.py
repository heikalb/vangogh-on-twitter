import re
from collections import defaultdict
import random
from nltk import bigrams


def preprocess_corpus(texts):
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
    Create a Markov chain for word transitions in a corpus. Helper methdd for
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
    length = random.choice(lengths)
    curr = '<b>'
    sentence = []

    while True:
        next = random.choice(markov_chain[curr])
        sentence.append(next[0])
        sentence.append(next[1])
        curr = next[1]

        if '<b>' in next:
            if next[0] == '<b>':
                sentence.pop()
                sentence.pop()
            else:
                sentence.pop()

            if length - 2 <= len(sentence) <= length + 2:
                break
            else:
                sentence.clear()

    return ' '.join(sentence).capitalize()


def generate_text_(markov_chain, lengths):
    """
    Generate a sentence based on a given Markov chain. Helper method for main()
    :param markov_chain: dictionary of word transitions where the keys are
    words and the values are lists of word bigrams that can follow key words
    :param lengths: list of possible sentence lengths in a corpus. This is to
    limit generated sentences to more reasonable lengths.
    :return: generated sentence (string)
    """
    length = random.choice(lengths)
    word_1 = ' '

    while not word_1[0].isupper():
        word_1 = random.choice([k for k in markov_chain])

    sentence = [word_1]
    while True:
        word_2 = random.choice(markov_chain[word_1])
        sentence.append(word_2[0])
        sentence.append(word_2[1])
        word_1 = word_2[1]

        if word_1.endswith('.') or word_1.endswith('?'):
            if length -2 <= len(sentence) <= length + 2:
                break
            else:
                sentence.clear()

                while not word_1[0].isupper():
                    word_1 = random.choice([k for k in markov_chain])

    return ' '.join(sentence)


def main():
    # Get corpus of letters
    with open('vangogh_letters.txt', 'r') as f:
        letters = f.read().split('\n')

    letters = preprocess_corpus(letters)

    # Get possible sentence lengths
    lengths = get_sentence_lengths(letters)

    # Build Markov chain
    markov_chain = make_markov_chain(letters)

    # Generate text based on said Markov chain
    for i in range(100):
        sent = generate_text(markov_chain, lengths)
        print(sent, '\n')


if __name__ == '__main__':
    main()
    exit(0)
