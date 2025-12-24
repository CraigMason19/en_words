from en_words import en_words as w
from en_words import word_games as wg

def main():
    """
    Example usage
    """
    sd = w.create_sorted_dict()

    print(f"\nWord count:") # 194433
    print(f"\t{w.word_count()}")

    largest = w.find_largest_word()
    print(f"\nLargest word ({len(largest)}):")
    print(f"\t{largest}")

    wol = w.words_of_length(4)
    print(f"\nWords of len(4):") # 5368
    print(f"\t{len(wol)}")  

    word = '_?tt-e'
    pw = w.potential_words(word)
    print(f"\nPotential words of {word}: {len(pw)}") 
    print(f"\t{pw}")  

    letters = "beetles"
    words = w.words_from_letters(letters, min_len=3, max_len=5)
    print(f"\nWords from letters '{letters}' between 3 & 5 letters: {len(words)}") 
    print(f"\t{words[:20]}...")
    # print(f"\t{words}")  

    letters = "beetles"
    words = w.words_from_letters(letters, min_len=5, max_len=None, remove_doubles=False) 
    print(f"\nWords from letters '{letters}' between 5 & NONE letters: {len(words)}") 
    print(f"\t{words[:20]}...")
    # print(f"\t{words}")  

    word = "Skate"
    a = w.anagrams(word)
    print(f"\nAnagrams of '{word}'") 
    print(f"\t{a}")

def word_games():
    wg.spelling_bee('t', 'wnidal')
    wg.wordle("?a?e?", "STMLkdBY", "n") 
    wg.polygon('F', 'lretgure')
    wg.cash_square(['aver', 'flap', 'gent', 'lime', 'newt']) 
    wg.countdown('ljsoeitwo') # 'jowliest', 8 letters, best answer

if __name__ == '__main__':
    # main()
    word_games()