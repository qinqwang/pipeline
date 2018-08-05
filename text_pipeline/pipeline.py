from text_pipeline import input_check
from text_pipeline import string_to_function
import threading
import csv
import os

DIR_NAME = os.path.dirname(__file__)

iid = 1
iid_clock = threading.Lock()
OUT_FOLDER = 'output'


def _next_id():
    """
    It is a private counter for version control which used for different files to stemming_static.csv
    :return: The current id
    """
    global iid
    with iid_clock:
        result = iid
        iid = iid + 1
    return result


def Pipeline(functions):
    """
    The frame of the text pipeline. Firstly construct the function it needs and input the data
    :param functions: The functions users want to put into
    :return: trigger
    """
    input_check.input_check_pipeline(functions)
    _static_pipe(functions)

    def trigger(text):
        """
        Inner function that needs input the data
        :type text: object
        """
        result = text
        # extract function data from functions
        for tup in functions:
            # get the function name
            func_name = tup[0]
            # get the module and corresponding name
            func = string_to_function.string_to_function(func_name)
            if tup[1]:
                # concatenate the result into the arguments
                tup[1]['text'] = result
                result = getattr(func[0], func[1])(**tup[1])
            else:
                # no other arguments
                result = getattr(func[0], func[1])(result)
        return result

    return trigger


def _static_pipe(functions):
    """
    Record what function the text pipeline use and write into the .csv file
    :return: True
    """

    formatted_pipe_static = 'pipe_static{}.csv'.format(_next_id())
    relative_pipe_static = os.path.join(DIR_NAME, '..', OUT_FOLDER)

    if not os.path.exists(relative_pipe_static):
        os.makedirs(relative_pipe_static)

    relative_ps_file = os.path.join(relative_pipe_static, formatted_pipe_static)

    with open(str(relative_ps_file), 'w') as pipe_file:
        field_names = ['functions']
        pipe_writer = csv.DictWriter(pipe_file, fieldnames=field_names)
        pipe_writer.writeheader()
        for function in functions:
            pipe_writer.writerow(dict(functions=function[0]))
    pipe_file.close()
    return True
