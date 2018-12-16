import re
import collections
import numpy as np
from string import *


def caesar1(str_ascii: str, shift: int) -> str:
    """
    :param str_ascii: (str)
    :param shift: (int)
    :return: (str)
    """
    alpha = ascii_letters
    shift_alpha = alpha[shift:] + alpha[:shift]
    table = str.maketrans(alpha, shift_alpha)
    print(str_ascii.translate(table))
    return str_ascii.translate(table)


def caesar2(str_ascii: str, shift: int) -> str:
    """
    :param str_ascii: (str)
    :param shift: (int)
    :return: (str)
    """
    alpha = dict(enumerate(ascii_letters))
    alpha_r = {val: key for (key, val) in alpha.items()}
    shift_alpha = {key: val + shift for (key, val) in alpha_r.items()}
    for key, val in shift_alpha.items():
        if val > 51:
            shift_alpha[key] = val - 52
        if val < 0:
            shift_alpha[key] = val + 52
    res = "".join([alpha[shift_alpha[i]] for i in str_ascii])
    print(res)
    return res


def word_frequency(str_data: str) -> dict:
    """
    :param str_data: (str)
    :return: (dict)
    """

    res = re.sub(r"\W", " ", str_data, flags=re.I).lower().split()
    res = dict(collections.Counter(np.array(res)).most_common())
    for key, value in res.items():
        print("Word '{}':{}".format(key, value))
    return res


if __name__ == "__main__":
    str_data = ("Beautiful is better than ugly. "
                "Explicit is better than implicit. "
                "Simple is better than complex. "
                "Complex is better than complicated. "
                "Flat is better than nested. "
                "Sparse is better than dense. "
                "Readability counts. "
                "Special cases aren't special enough to break the rules. "
                "Although practicality beats purity. "
                "Errors should never pass silently. "
                "Unless explicitly silenced. "
                "In the face of ambiguity, refuse the temptation to guess. "
                "There should be one-- and preferably only one --obvious way to do it. "
                "Although that way may not be obvious at first unless you're Dutch. "
                "Now is better than never. "
                "Although never is often better than *right* now. "
                "If the implementation is hard to explain, it's a bad idea. "
                "If the implementation is easy to explain, it may be a good idea. "
                "Namespaces are one honking great idea -- let's do more of those!")

    text = input('Input here asci symbols without punctuation and spaces:')
    shift = int(input('Input here shift in the range from -51 to 51 inclusive:'))

    caesar1(text, shift)
    caesar2(text, shift)

    word_frequency(str_data)
