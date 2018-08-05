from text_pipeline import input_check
from text_pipeline import pipe_token
from nltk.stem.snowball import SnowballStemmer
from text_pipeline import statistic


def stemming_list(text, lang='en', static=False, file_name='stemming'):
    """
    Stemming removes morphological affixes from words, leaving only the word stem.
    :param file_name: name the file for statistic
    :param static: Check if user wants to do statistic
    :param text: the list of tokenized words
    :param lang: the language use. Default is english
    :return: the list of words stem
    """
    input_check.input_check_list(text)
    # stemmed word list
    stem_words = []
    # original word list which is affected
    org_words = []
    # affected word list
    aff_words = []
    language = pipe_token.code_convert(lang).lower()
    stemmer = SnowballStemmer(language)
    for word in text:
        stem_word = stemmer.stem(word)
        stem_words.append(stem_word)
        # check if the word changed
        if word != stem_word:
            org_words.append(word)
            aff_words.append(stem_word)
    # check whether or not need statistic
    if static:
        statistic.do_statistic(org_words, aff_words, file_name)
    return stem_words
