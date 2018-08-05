import string
import json
import re
from nltk.corpus import stopwords
from nltk import wordpunct_tokenize
from text_pipeline import input_check
import os
from text_pipeline import statistic

DIR_NAME = os.path.dirname(__file__)
PATH_ISO_CODE = os.path.join(DIR_NAME, '..', 'data', 'ISO639-1_Code.json')


def tokenize_words(text, keep_date=False):
    """
    Use nltk to do tokenization. If the raw_data has the date information, the tokenizer won't split them up and it
    will keep it in the original form. (['I have a meeting in Jan 1st 1995-01-13']--->['I', 'have', 'a', 'meeting',
    'in', 'Jan 1st', '1995-01-13'])
    :param keep_date: Decide if token need to keep date information
    :param text: List of plaintext
    :return: the list of tokenized word
    """

    input_check.input_check_list(text)
    token_words = wordpunct_tokenize(text[0])
    if keep_date:
        return _keep_date(token_words)
    else:
        return token_words


def _keep_date(text):
    """
        Input the list of tokens and return the list of tokens with date information
        :param text: the list of tokens
        :return: the list of tokens with date information
        """
    # check if the list has the time element
    if '-' in text:
        # find all indices which contain - in the list
        indices = _find_all_indices('-', text)
        count = 0
        valid_pair_index = []
        # find all validate indices
        while count < len(indices) - 1:
            if (indices[count] + 2) == indices[count + 1]:
                valid_pair_index.append([indices[count], indices[count + 1]])
            count = count + 1
        # joint time string in the list
        # loop_num records the time of merging to adjust the merge position
        loop_num = 0
        for valid_pair in valid_pair_index:
            # The reange of the list is [)
            text[(valid_pair[0] - 1 - loop_num): (valid_pair[1] + 2 - loop_num)] = [
                ''.join(text[(valid_pair[0] - 1 - loop_num): (valid_pair[1] + 2 - loop_num)])]
            # each merge decrese the list size by 4
            loop_num = loop_num + 4

    # check if the list contains month information
    Month_list = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    # convert the list of token words into lower case
    l_tokens = [word.lower() for word in text]
    pattern = re.compile(r'\d.+')
    for mon in Month_list:
        if mon in l_tokens:
            in_dex = _find_all_indices(mon, l_tokens)
            # loop_num records the time of merging to adjust the merge position
            loop_num = 0
            for idx in in_dex:
                idx = idx - loop_num
                if pattern.match(text[idx + 1]):
                    text[idx: idx + 2] = [' '.join(text[idx: idx + 2])]
                    l_tokens[idx: idx + 2] = [' '.join(l_tokens[idx: idx + 2])]
                    loop_num = loop_num + 1
    return text


def _find_all_indices(value, qlist):
    """
    Finding the index of an item given a list containing it
    :param value: The item want to find in the list
    :param qlist: The list
    :return: The list of indices
    """
    indices = []
    idx = -1
    while True:
        try:
            # index() returns the first index of value
            idx = qlist.index(value, idx + 1)
            indices.append(idx)
        except ValueError:
            break
    return indices


def stop_words_removal(text, language='en', static=False, file_name='stopwords'):
    """
    Filter out the stop words in the text according to the language it uses
    :param file_name: name the file for statistic file
    :param static: Check if user wants to do statistic
    :param text: The list of tokenized text
    :param language: Detected language which is the IOS639-1 format
    :return: The list of the tokenized text without stopwords
    """
    # convert language code
    lang = code_convert(language).lower()
    # simplify which language used on stopwords
    stop_words = stopwords.words(lang)
    words_filter = []
    # records the affected words
    affected_words_list = []
    for word in text:
        if word not in stop_words:
            words_filter.append(word)
        else:
            affected_words_list.append(word)
    # check if it needs recording
    if static:
        statistic.do_statistic_single(affected_words_list, file_name)
    return words_filter


def remove_punct(text):
    """
    Filter out the punctuation in the tokenized data
    :return:
    :param text: The list of tokenized data
    :return: The list of tokenized data without punctuations
    """
    words = [''.join(word for word in word_list if word not in string.punctuation) for word_list in text]
    return [word for word in words if word]


def code_convert(lang):
    """
    Covert IOS639-1 format to the original readable language
    :param lang: IOS639-1 code
    :return: language
    """
    input_check.input_check_str(lang)

    file = open(str(PATH_ISO_CODE))

    data = json.load(file)

    language = data[lang]

    file.close()

    return language
