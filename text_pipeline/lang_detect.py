from langdetect import detect_langs
from text_pipeline import input_check


def detect_language(text):
    """
    Detect the which language of the text using and pick up the most likely language
    :param text: The string of plaintext
    :return:  The most likely language which is the IOS639-1 form(english-->en)
    """
    input_check.input_check_str(text)

    lang_ratios = _calculate_languages_ratios(text)

    lang = str(lang_ratios[0]).split(":")

    return lang[0]


def _calculate_languages_ratios(text):
    """
    Calculate the possibilities of each language
    :param text: The string of plaintext
    :return: The list of the possible language with their possibility
    """
    languages_ratios = detect_langs(text)

    sorted_language_list = sorted(languages_ratios, reverse=True)

    return sorted_language_list
