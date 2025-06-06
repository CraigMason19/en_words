
# en_words
A package for working with English dictionaries and finding words and anagrams.

Also contains soultions and potential solutions to various word games including Wordle and Countdown.

## Requirements
None.

## Usage
By default the methods use the dictionary included in the directory but other text files can be passed in. Makes use of a dictionary sorted by length and then alphabetically. This can be created using the create_sorted_dict() method on a normal dictionary.

```python
import en_words as ew
```

### Words of a certain length
```Python
words = ew.words_of_length(4)
```
###  Potential words
```Python
words = ew.potential_words('_?tt-e')
```
See main.py for more usage examples.

# Word games

A collection of wrappers for fun word games.

## Spelling Bee
https://www.nytimes.com/puzzles/spelling-bee
With a central letter and 6 other letters around it. Find words (of 4 or more) that contain the central letter.
```Python
from en_words.word_games import spelling_bee

spelling_bee('f', 'eltbad')

[..., 'peelite', 'pipette', 'pittite', 'textile', 'tillite', 'tippett', 'vitelli', 'villette', 'expletive']
```

## Wordle
https://www.nytimes.com/games/wordle/index.html
```Python
from en_words.word_games import wordle

wordle('???N?', 'steaiy', 'r')

['bronx', 'bruno', 'corno', 'cornu', 'cronk', 'drunk', 'frond', 'porno', 'prong', 'pronk', 'round', 'wrong', 'wrung']
```

## Polygon
With a central letter and 8 other letters around it. Find words (of 4 or more) that contain the central letter.
```Python
from en_words.word_games import polygon

polygon('F', 'lretgure')

[..., 'gruffer', 'referee', 'refugee', 'refuter', 'ruffler', 'truffle', 'ferreter', 'gefullte', 'fleurette', 'regretful']
```

## Cash Grid
By putting 4 words on top of each other 4 more words can be formed reading downwards aswell.
```Python
from en_words.word_games import cash_square

cash_square(['aver', 'flap', 'gent', 'lime', 'newt'])

F L A P
L I M E
A V E R
G E N T
```

## Countdown
A solver for the TV show Countdown
```Python
from en_words.word_games import countdown

countdown('ljsoeitwo')

...

6 letters:
        ['jolies', 'joliot', 'jostle', 'lowest', 'oolite', 'otiose', 'owlets', 'soweto', 'toiles', 'towels']

7 letters:
        ['oolites', 'ostiole', 'stoolie', 'woolies']

8 letters:
        ['jowliest']

9 letters:
        []
```