from collections import Counter
import re
import os

DIR_NAME = os.path.dirname(__file__)
PATH_SPELLING_CORPUS = os.path.join(DIR_NAME, '..', 'data', 'big.txt')


def words(text):
    """
        :param word: the spelling corpus
        :return: the corpus with all words in lower case
       """
    return re.findall(r'\w+', text.lower())

"""
    Input data for path should be text data (.txt) 
    This file should be file with correct spelling words or dictionary
"""

spelling_corpus = Counter(words(open(PATH_SPELLING_CORPUS).read()))


def correction(word):
    """
       This is the function to call for spelling correction
        :param word: the correct spelling words
        :return: return the most likely word to replace the wrong spelling word
    """

    return max(candidates(word), key = word_probability) if candidates(word) else None

def word_probability(word, word_sum =sum(spelling_corpus.values())):

    """
    :param word: corrected spelling word
    :return: return the probability of a word occured in the spelling_corpus
     """
    return spelling_corpus[word] / word_sum



def candidates(word):
    """
    :param word: wrong spelling word
    :return: return the possible correct spelling words after being edited
    """
    return(get_known_word([word]) or get_known_word(edit_word(word)) or get_known_word(edit_word_twice(word)  or [word]))

def get_known_word(words):
    """
        :param word: the edited words
        :return: return set of edited words that match the words in spelling corpus
    """

    return set(w for w in words if w in spelling_corpus)


def edit_word(word):
    """
        this function edit the wrong words using edit operations:
        deletes, transpose, replace, insert
        :param word: are the words that are in the corpus
        :return: return a set of correct spelling words
    """

    letters = 'abcdefghijklmnopqrstuvwxyz'
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    tranposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R) > 1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in letters]
    inserts = [L + c + R for L, R in splits for c in letters]
    return set(deletes + tranposes + replaces + inserts)


def edit_word_twice(word):
    """
        :param word: is the set of correct spelling word that was return by edits1 function
        :return: return words that require two edit distance
    """

    return(twice_edited_word for one_edited_word in edit_word(word) for twice_edited_word in edit_word(one_edited_word))