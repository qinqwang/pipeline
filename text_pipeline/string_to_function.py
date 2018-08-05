from text_pipeline import pipe_token
from text_pipeline import lang_detect
from text_pipeline import spell_check
from text_pipeline import stemming
from text_pipeline import input_check
from text_pipeline import word_frequency
from text_pipeline import lemmatization_pos


def string_to_function(func_name):
    """
    convert function name to the function
    :param func_name: string of function name
    :return: function and its corresponding name use for call function with
    a dynamic list of arguments
    """
    # check input type
    input_check.input_check_str(func_name)

    dispatch = {
        "tokenize_words": pipe_token,
        "stop_words_removal": pipe_token,
        "remove_punct": pipe_token,
        "detect_language": lang_detect,
        "spell_check_list": spell_check,
        "stemming_list": stemming,
        "count_word_frequency": word_frequency,
        "lemma": lemmatization_pos
    }
    # check if function name in the dictionary
    if func_name not in dispatch.keys():
        raise Exception('Do not have the function!')

    return dispatch[func_name], func_name
