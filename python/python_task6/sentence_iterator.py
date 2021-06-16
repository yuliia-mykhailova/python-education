"""Module for implementing sentence iterator"""
import re


class SentenceIterator:
    """SentenceIterator class for iterating Sentence"""
    def __init__(self, words):
        """Constructor"""
        self.words = words
        self.counter = 0

    def __iter__(self):
        """Returns iterator obj"""
        return self

    def __next__(self):
        """Returns next element from iterator"""
        if self.counter < len(self.words):
            result = self.words[self.counter]
            self.counter += 1
            return result
        raise StopIteration


class Sentence:
    """Sentence class for manipulating with sentences"""

    def __init__(self, text: str):
        """Constructor"""
        terminal_symbols = '.?!'
        if not isinstance(text, str):
            raise TypeError('Wrong type of input text')
        if text[-1] not in terminal_symbols:
            raise ValueError('Not ended sentence')
        self.text = text

    def __repr__(self):
        """String presentation of object"""
        return f"<Sentence(words={len(self.words)}, other_chars={len(self.other_chars)})>"

    def __iter__(self):
        """Returns iterator object"""
        return SentenceIterator(self.words)

    def __getitem__(self, item):
        """getitem delegation to list words"""
        return self.words[item]

    def _words(self):
        """Lazy iterator"""
        i = 0
        while i < len(self.words):
            yield self.words[i]
            i += 1

    @property
    def words(self):
        """Returns a list of words from text"""
        return re.findall(r'\w+', self.text)

    @property
    def other_chars(self):
        """Returns a list of special symbols"""
        return re.findall(r'\W+', self.text)


if __name__ == '__main__':
    # testing

    test = Sentence('Hello world!')
    print(test)

    print(Sentence('Hello world!')._words())
    print(next(Sentence('Hello world!')._words()))
    test = test._words()
    print(next(test), next(test))

    print(Sentence('Hello world!')[0])
    print(Sentence('Hello world!')[:])

    for word in Sentence('Hello world!'):
        print(word)

    print(iter(Sentence('Hello world!')))
