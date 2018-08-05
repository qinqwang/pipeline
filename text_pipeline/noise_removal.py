import os
from os import walk
import re

# regrex match(Nº|©, The prefix, id? end of the page, the catalog, (1), 1.2.3, 1. , ...., - 12 -)

rgx_list = ['(©|Nº)', '(\([i|v][i|v]*\))', 'AMSDAM(-(\d|v)*)*(.(\d)*)?', '[\b\w+\b ]*\.+ \d*$', '-?(\d+-)+(\w*)', '\(\w\)',
            '(\d{1,2}\.)+(\d{1,2})*', '^(\d{1,2}\.)', '\.{3,}', '- \d+ -']


def noise_removal(folder_path):
    """
    Get rid of the noisy data. Only input the path of the folder and it will automatically
    get txt file and get rid of the noisy from the file and rewrite into the output folder
    as the same name
    :param folder_path: The absolute path of the data folder
    """
    # create a output folder if not exist
    out_put_folder = os.path.join(folder_path, 'output')
    if not os.path.exists(out_put_folder):
        os.makedirs(out_put_folder)
    # get the file list
    file_list = _get_txt_files(folder_path)
    for file in file_list:
        # join the path
        path_r = os.path.join(folder_path, file)
        path_w = os.path.join(out_put_folder, file)
        file_r = open(path_r, 'rU', encoding='UTF-8')
        file_w = open(path_w, 'w', encoding='UTF-8')
        # data cleaning
        try:
            for line in file_r:
                # get rid of the white spaces and while lines
                line = line.lstrip().rstrip().strip('\n')
                if line:
                    # clean the string
                    line = _clean_data(rgx_list, line)
                    if line:
                        # write out
                        file_w.write(line + '\n')

        finally:
            file_r.close()
            file_w.close()


def _get_txt_files(path):
    """
    get all the txt file's name
    :param path: the path of the folder
    :return: the list of the txt file name
    """
    file_names = []
    # walk through the folder's files which are txt
    for (dirpath, dirnames, filenames) in walk(path):
        file_names.extend(filenames)
        break
    # only get the txt files
    return [txt for txt in file_names if '.txt' in txt]


def _clean_data(rgx_list, text):
    """
    mainly use regular expression to get rid of the noisy
    :param rgx_list: the list if the rgx pattern
    :param text: string text
    :return: the clean text of string
    """
    new_text = text
    for rgx_match in rgx_list:
        new_text = re.sub(rgx_match, '', new_text)
    return new_text


