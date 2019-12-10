from collections import defaultdict
import random
import spacy


def make_markov_chain(texts):
    words = []

    for text in texts:
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(text)
        words += [token.text for token in doc]

    markov_chain = defaultdict(list)
    prevs, nexts = words[:-1], words[1:]

    for prev, next in zip(prevs, nexts):
        markov_chain[prev].append(next)

    return markov_chain


def generate_text(markov_chain):
    sentence = []

    word_1 = random.choice([k for k in markov_chain])
    sentence.append(word_1)

    while word_1 != '.':
        word_2 = random.choice(markov_chain[word_1])
        sentence.append(word_2)
        word_1 = word_2

    return ' '.join(sentence)


def main():
    # Get corpus of letters
    with open('vangogh_letters.txt', 'r') as f:
        letters = f.read().split('\n')

    # Build Markov chain
    markov_chain = make_markov_chain(letters)

    # Generate text based on said Markov chain
    sent = generate_text(markov_chain)
    print(sent)


if __name__ == '__main__':
    main()
    exit(0)
