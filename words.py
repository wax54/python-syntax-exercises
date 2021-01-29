words = ["hello", "hey", "goodbye", "yo", "eyes"]


def print_upper_words(word_list, must_start_with=False):
    """ Prints an uppercase version of each word in word list
    if must_start_with is specified(as a set of letters ex: {'a','b'}) 
       only words starting with those letters(non-case-sensitive) will be printed 
    """

    if(must_start_with):
        for word in word_list:
            word = word.upper()
            for req in must_start_with:
                if word[0] == req.upper():
                    print(word)
    else:
        for word in word_list:
            print(word.upper())
