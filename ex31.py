# even more practice
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """Sort the words."""
    return sorted(words)

def print_first_word(words):
    """Print the first word after popping it off."""
    word = words.pop(0)
    print word

def print_last_word(words):
    """Print the last word after popping it off."""
    word = words.pop(-1) 
    print word 
    # I thought that it would be pop(len(words))
    # what about try that when we finish it. 
 
def sort_sentence(sentence):
    """Taking a full sentence and return the sorted words."""
    return sort_words(break_words(sentence))

def print_first_and_last(sentence):
    """Print the first word, and last word after popping them off."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sort the words then print the first and last one."""
    words = sort_sentenc