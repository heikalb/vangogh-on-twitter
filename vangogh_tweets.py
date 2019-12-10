import re
from collections import defaultdict
import random
from nltk import bigrams


def get_sentence_lengths(texts):
    lengths = []

    for text in texts:
        sentences = re.split('[!?.]+\s*', text)

        for sentence in sentences:
            words = sentence.split(' ')

            if len(words):
                lengths.append(len(words))

    random.shuffle(lengths)
    return lengths


def make_markov_chain(texts):
    words = []

    for text in texts:
        words += text.split()

    markov_chain = defaultdict(list)
    prevs, nexts = words[:-2], bigrams(words[1:])

    for prev, next in zip(prevs, nexts):
        markov_chain[prev].append(next)

    return markov_chain


def generate_text(markov_chain, lengths):
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
            print(' '.join(sentence))
            if len(sentence) == length:
                break
            else:
                word_1 = sentence[0]
                sentence = sentence[:1]

    return ' '.join(sentence)


def main():
    # Get corpus of letters
    with open('vangogh_letters.txt', 'r') as f:
        letters = f.read().split('\n')

    # Get possible sentence lengths
    lengths = get_sentence_lengths(letters)

    # Build Markov chain
    markov_chain = make_markov_chain(letters)

    # Generate text based on said Markov chain
    sent = generate_text(markov_chain, lengths)
    print(sent)


if __name__ == '__main__':
    main()
    exit(0)
