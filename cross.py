import re
import itertools
import random


DICT = 'british-english'


def get_words(filename, limit=None):
    with open(filename) as f:
        words =  f.readlines()
        random.shuffle(words)
        if limit:
            words = words[:limit]
        words = map(lambda x: x.replace('\n', ''), words)
        return words

def get_word_like(pat):
    words = get_words(DICT)
    for word in words:
        if re.match(pat, word):
            yield word


class Grid(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.grid = []
        for i in range(x):
            self.grid.append(['.']* y)

    def __repr__(self):
        lines = []
        for line in self.grid:
            lines.append(''.join(line))
        return '\n'.join(lines)

    def is_empty(self):
        return ''.join(itertools.chain(*self.grid)).strip('.') == ''

    def add_word(self, word, direction='across'):
        print "Word:",word
        if direction == 'across':
            r = random.randint(0, self.x)
            for i, c in enumerate(word):
                if self.grid[r][i] in ('.', c):
                    self.grid[r][i] = c
                    continue
                raise ValueError
        else:
            r = random.randint(0, self.y)
            for i, c in enumerate(word):
                if self.grid[i][r] in ('.', c):
                    self.grid[i][r] = c
                    continue
                raise ValueError

    def add_random(self, col):
        pattern = ''

        row = 0
        for j in range(self.x):
            if self.grid[j][col] != '.' and row == 0:
                row = j

            pattern += self.grid[j][col]

        pattern = pattern.strip('.')
        print "Pattern:",pattern
        print
        print
        for word in get_word_like(pattern):
            if not word:
                return
            print "word: ", word
            """ adds the word"""
            try:
                for i, c in enumerate(word):
                    self.grid[i+row][col] = c
            except IndexError:
                continue



if __name__ == '__main__':
    words = get_words('british-english', 10)
    grid = Grid(20, 20)
    grid.add_word(words[0])
    grid.add_word(words[1])
    for c in range(20):
        grid.add_random(c)
    print(grid)
