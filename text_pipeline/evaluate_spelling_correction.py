from text_pipeline import spelling_correction
import csv
import os




edited_words_ls = []
mispelled_words_ls = []
correct_words_ls = []

DIR_NAME = os.path.dirname(__file__)
OUT_FOLDER = 'output'
DATA_FOLDER = 'data'

relative_out_path = os.path.join(DIR_NAME, '..', OUT_FOLDER)
relative_data_path = os.path.join(DIR_NAME, '..', DATA_FOLDER)
if not os.path.exists(relative_out_path):
        os.makedirs(relative_out_path)

if not os.path.exists(relative_data_path):
        os.makedirs(relative_data_path)

relative_data = os.path.join(relative_data_path, 'mispelled_word.txt')
relative_output = os.path.join(relative_out_path, 'output.csv')
"""
    This function is to evaluate the accuracy of the spelling_correction module
    :param file is text file contain mispelled words and the correct word 
    :return: the count of number of mispelled word 
    and number of words that were edited correctly by spelling correction module 
"""
def count_words(file):
    count_mispelled = 0
    count_correct_word = 0

    for line in file:
        words = line.lower().split()
        count_mispelled += 1
        mispelled_words_ls.append(words[1])
        edited_word = spelling_correction.correction(words[1])
        edited_words_ls.append(edited_word)
        correct_words_ls.append(words[0])
        if edited_word == words[0]:
            count_correct_word += 1

    return {'mispelled': count_mispelled, 'correct word': count_correct_word}



file = open(relative_data)
count_result = count_words(file)
file.close()

"""
Writing list of mispelled word, edited word, and correct word to csv for analysing
"""

rows = zip(mispelled_words_ls,edited_words_ls,correct_words_ls)

with open(relative_output, "w") as output_file:
    writer = csv.writer(output_file)
    writer.writerow(('mispelled_words', 'edited_words', 'correct_words'))
    for row in rows:
        writer.writerow(row)

output_file.close()