import csv
import threading
import os
from collections import Counter

DIR_NAME = os.path.dirname(__file__)
OUT_FOLDER = 'output'

iid = 1
iid_clock = threading.Lock()


def _next_id():
    """
    It is a private counter for version control which used for different files to static.csv
    :return: The current id
    """
    global iid
    with iid_clock:
        result = iid
        iid = iid + 1
    return result


def _build_relative_file_path(fun_name):
    """
    build the relative file path
    :param fun_name: function name you use
    :return: the full path
    """
    file_name = '{}_{}.csv'.format(fun_name, _next_id())
    relative_folder_path = os.path.join(DIR_NAME, '..', OUT_FOLDER)
    if not os.path.exists(relative_folder_path):
        os.makedirs(relative_folder_path)
    # Build the relative file path
    relative_path = os.path.join(relative_folder_path, file_name)
    return relative_path


def do_statistic(original_words_list, affected_words_list, func_name):
    """
    Record the words change and word frequency in the list and write into a .csv file
    :param original_words_list: The list of original words
    :param affected_words_list: The list of the changed words
    :param func_name: function name
    :return: True
    """

    relative_file_path = _build_relative_file_path(func_name)
    # reconstruct the data into a dictionary
    tem_dic = reconstruct_dic(original_words_list, affected_words_list)

    try:
        with open(str(relative_file_path), 'w') as file:
            fieldnames = ['original_words', 'affected_words', 'frequency']
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for key in tem_dic.keys():
                csv_writer.writerow(
                    dict(original_words=key, affected_words=tem_dic[key][1], frequency=tem_dic[key][0]))
        file.close()
    except IOError:
        print('Could not write file', func_name)

    return True


def reconstruct_dic(origin_list, affected_list):
    """
    reconstruct the affected words list into a dictionary
    :param origin_list:
    :param affected_list:
    :return:
    """
    re_dic = {}
    n = 0
    for origin_word in origin_list:
        if origin_word in re_dic.keys():
            re_dic[origin_word][0] += 1
        else:
            re_dic[origin_word] = [1, affected_list[n]]
        n += 1
    return re_dic


def do_statistic_single(affected_word_list, function_name):
    """
    This function is to deal with the record that only one elements affected, e.g. the stop_words removal,
    we only need to record how many stopwords removed
    :param affected_word_list: the list of affected words
    :param function_name: the function you use
    :return: Ture
    """

    # build relative file path
    relative_file_path = _build_relative_file_path(function_name)
    # construct the dictionary
    single_dic = dict(Counter(affected_word_list))
    try:
        with open(str(relative_file_path), 'w') as file:
            fieldnames = ['affected_words', 'word_frequency']
            csv_writer = csv.DictWriter(file, fieldnames=fieldnames)
            csv_writer.writeheader()
            for key in single_dic.keys():
                csv_writer.writerow(dict(affected_words=key, word_frequency=single_dic[key]))
        file.close()
    except IOError:
        print('Could not write the file', function_name)

    return single_dic


