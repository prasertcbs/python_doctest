'''
intro to doctest
ref: https://docs.python.org/3/library/doctest.html
python file_name.py
python file_name.py -v
'''

import numpy as np
import re
import math


def rectangle_area(w, h):
    """calculate rectangle area

    Args:
        w ([type]): width
        h ([type]): height

    Raises:
        ValueError: w, h > 0

    Returns:
        [type]: rectangle area

    Test:
    >>> rectangle_area(5, 2)
    10
    >>> rectangle_area(5, -2)
    Traceback (most recent call last):
    ...
    ValueError: w and h must be > 0
    """
    if w < 0 or h < 0:
        raise ValueError('w and h must be > 0')
    return w * h


def c2f(c: float) -> float:
    '''
    >>> c2f(100)
    212.0
    >>> c2f(36)
    96.8
    >>> [c2f(celsius) for celsius in range(0,5)]
    [32.0, 33.8, 35.6, 37.4, 39.2]
    >>> [c2f(celsius) for celsius in [0, 10, 15, 30, 100]]
    [32.0, 50.0, 59.0, 86.0, 212.0]
    '''
    return float(c)/5*9+32


def circle_area(r: float) -> float:
    '''
    >>> circle_area(1)
    3.141592653589793
    >>> round(circle_area(1), 4)
    3.1416
    >>> f'{circle_area(1):.4f}'
    '3.1416'
    >>> circle_area(-1)
    Traceback (most recent call last):
        ...
    ValueError: r must be greater than 0
    '''
    if r < 0:
        raise ValueError('r must be greater than 0')
    return math.pi * float(r) ** 2


def split_fullname(fullname: str) -> tuple:
    """extract first and last name

    Args:
        fullname (str): [description]

    Returns:
        tuple: [description]

    Test:
    >>> split_fullname('Peter Parker')
    ('Peter', 'Parker')
    >>> split_fullname('Peter Parker  ')
    ('Peter', 'Parker')
    >>> split_fullname('Peter     Parker')
    ('Peter', 'Parker')
    >>> split_fullname('Peter J Parker')
    ('Peter', 'J Parker')
    >>> split_fullname('Peter\tParker')
    ('Peter', 'Parker')
    >>> split_fullname('')
    ('', '')
    """
    fullname = re.sub('\s{2,}', ' ', fullname.strip())
    parts = fullname.split(' ', maxsplit=1)
    if len(parts) == 2:
        fname, lname = parts
        return (fname, lname)
    else:
        return (fullname, '')


def ean13_check_digit(ean13: str) -> int:
    '''
    >>> ean13_check_digit('4006087085455')
    5
    >>> ean13_check_digit('400 608 708545 5')
    5
    >>> ean13_check_digit('400-608-708545 5')
    5
    >>> ean13_check_digit('8851234567898')
    8
    >>> ean13_check_digit('40060870854a')
    Traceback (most recent call last):
        ...
    ValueError: EAN13 length does not equal 13 characters
    '''
    ean13 = re.sub(r'\D', '', ean13)
    if len(ean13) != 13:
        raise ValueError('EAN13 length does not equal 13 characters')
    a = np.array(list(ean13), dtype=int)
    r = np.sum(a[:12:2]) + np.sum(a[1:12:2] * 3)
    return 0 if r % 10 == 0 else 10 - (r % 10)


if __name__ == "__main__":
    import doctest
    # doctest.testmod(verbose=False)
    doctest.testmod(verbose=True)

    # print(circle_area(1))
    # print(f'{circle_area(1):.4f}')
    # f=[c2f(celsius) for celsius in range(0,5)]
    # print(f)
