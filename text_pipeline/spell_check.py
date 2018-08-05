from text_pipeline import spelling_correction as sc
from text_pipeline import input_check
from text_pipeline import statistic


def spell_check_list(text, static=False, file_name='spell_check'):
    """
    Correct the list of the words
    :param static: if do statistic to record the text change
    :param text: the list of the misspelling words
    :param file_name: input the name of the statistic file
    :return: the list of corrected spelling words
    """
    # Check whether or not input the correct type of data
    input_check.input_check_list(text)
    cor_words = []
    # original words list
    origin_words = []
    # affected words list
    affected_words = []
    for word in text:
        # check if the word spells wrong
        cor_word = sc.correction(word)
        # add it into the list if the word is corrected
        if cor_word != word:
            origin_words.append(word)
            affected_words.append(cor_word)
        # filter the word which length is less than 1 such as the punctuation
        if len(word) > 1:
            cor_words.append(cor_word)
    # do statistic
    if static:
        statistic.do_statistic(origin_words, affected_words, file_name)

    return cor_words
