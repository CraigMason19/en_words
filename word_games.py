from en_words import (words_from_letters, potential_words, word_count, 
    words_of_length)

def spelling_bee(inner_letter, outer_letters):
    ''' https://spellingbeegame.org '''
    def contains_central_letter(word):
        # return word.find(inner_letter.lower()) == 1
        return (inner_letter.lower() in word)

    letters = outer_letters.lower() + inner_letter.lower()
    
    sb = words_from_letters(letters, min_len=4, max_len=None, remove_doubles=False)
    sb = [word for word in sb if contains_central_letter(word)]

    print(f'Spelling Bee: ({inner_letter.lower()}, {outer_letters.lower()}), count: {len(sb)}')
    print(sb)
    print("")

def wordle(word, ignore, include):
    ''' https://www.nytimes.com/games/wordle/index.html '''
    words = potential_words(word, ignore, include)
    print(f'Wordle: {word}, count: {len(words)}')
    print(words)
    print()

def polygon(inner_letter, outer_letters):
    ''' Game from The Times newspaper'''

    def contains_central_letter(word):
        return (inner_letter.lower() in word)

    letters = outer_letters.lower() + inner_letter.lower()
    
    p = words_from_letters(letters, min_len=4, max_len=9, remove_doubles=False)
    p = [word for word in p if contains_central_letter(word)]

    print(f'Polygon: ({inner_letter.lower()}, {outer_letters.lower()})')
    print(p)
    print("")


def cash_square(word_list):
    ''' From take a break magazine '''

    # E.g.
    #
    # Given words
    # a v e r
    # f l a p
    # g e n t
    # l i m e
    # n e w t
    #
    # Answer
    # f l a p
    # l i m e
    # a v e r
    # g e n t

    rows = [w.lower() for w in word_list]
    cols = [''.join(zipped) for zipped in zip(*rows)]

    # Precompute words that might be a soultion to a column
    potentials_col_1 = words_from_letters(cols[0], 4, 4)
    potentials_col_2 = words_from_letters(cols[1], 4, 4)
    potentials_col_3 = words_from_letters(cols[2], 4, 4)
    potentials_col_4 = words_from_letters(cols[3], 4, 4)

    for a in potentials_col_1:
        for b in potentials_col_2:
            for c in potentials_col_3:
                for d in potentials_col_4:
                    # recreate the rows
                    row_1 = ''.join([a[0], b[0], c[0], d[0]])
                    row_2 = ''.join([a[1], b[1], c[1], d[1]])
                    row_3 = ''.join([a[2], b[2], c[2], d[2]])
                    row_4 = ''.join([a[3], b[3], c[3], d[3]])

                    grid_set = set([row_1, row_2, row_3, row_4])

                    if grid_set.issubset(word_list):
                        answer = set(word_list).difference(grid_set)

                        print(f'Cash Grid: ({rows})')
                        
                        for r in [row_1, row_2, row_3, row_4]:
                            print(f'\t{" ".join(r).upper()}')

                        print(f'{answer.pop()}')

def main():
    spelling_bee('i', 'xlpevt')
    wordle('???N?', 'steaiy', 'r') # -> wrong was the answer
    polygon('F', 'lretgure')
    cash_square(['aver', 'flap', 'gent', 'lime', 'newt'])

if __name__ == '__main__':
    main()