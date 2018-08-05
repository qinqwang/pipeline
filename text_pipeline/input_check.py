def input_check_str(in_str):
    """
    Check input string whether or not qualified
    :param in_str: String of text
    :return: True
    """
    if in_str == '':
        raise ValueError('Empty string!')
    elif not isinstance(in_str, str):
        raise ValueError('Wrong type of input')
    elif in_str is None:
        raise ValueError('Input None')
    return True


def input_check_list(in_list):
    """
    Check input list whether or not qualified
    :param in_list: list of text
    :return: True
    """
    if not in_list:
        raise ValueError('Empty list!')
    elif not isinstance(in_list, list):
        raise ValueError('Wrong type of input')
    elif in_list is None:
        raise ValueError('Input None')
    return True


def input_check_pipeline(in_list):
    """
    Check input list whether or not satisfy pipeline format: [(string, dic), (string, dic)...]
    :param in_list: list
    :return: True
    """
    input_check_list(in_list)

    for tup in in_list:
        input_check_str(tup[0])
        if not isinstance(tup[1], dict):
            raise ValueError('Please input dic as the arguments!')
