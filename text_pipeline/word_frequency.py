from text_pipeline import pipe_token
from text_pipeline import statistic
from collections import Counter


def count_word_frequency(text, file_name='word_frequency', static=False):
    """
    count the word frequency and return the dictionary of tokens and their corresponding frequency
    :param text: the list of tokens
    :param file_name: The default file name is word frequency
    :param static: if do statistic
    :return: The dictionary of tokens and each word corresponding frequency
    """
    # Do tokenization
    tokens = []
    for data in text:
        tokens = tokens + pipe_token.tokenize_words([data])
    # remove the punctuations
    print(tokens)
    tokens = pipe_token.remove_punct(tokens)
    if static:
        word_freq = statistic.do_statistic_single(tokens, file_name)
    else:
        word_freq = dict(Counter(tokens))
    return word_freq
