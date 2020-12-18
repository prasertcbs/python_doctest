'''
doctest part 2
document: https://docs.python.org/3/library/doctest.html
'''
import math
import re


def circle_area(r: float) -> float:
    '''
    approx equal test techniques
    >>> circle_area(1)
    3.141592653589793
    >>> round(circle_area(1), 4)
    3.1416
    '''
    if r < 0:
        raise ValueError('r must be greater than 0')
    return math.pi * float(r) ** 2


def gen_email_address(fname, lname, domain):
    '''
    string result
    >>> gen_email_address('Tony', 'Stark', 'superhero.com')
    'tony.s@superhero.com'
    '''
    return f'{fname.lower()}.{lname[0].lower()}@{domain}'


def c2f(c: float) -> float:
    '''
    list result
    >>> c2f(100)
    212.0
    >>> c2f(36)
    96.8
    >>> [c2f(celsius) for celsius in range(0,5)]
    [32.0, 33.8, 35.6, 37.4, 39.2]
    >>> [c2f(celsius) for celsius in [0, 10, 15, 30, 100]]
    [32.0, 50.0, 59.0, 86.0, 212.0]
    '''
    return c / 5 * 9 + 32


def split_fullname(fullname: str) -> tuple:
    """extract first and last name

    Args:
        fullname (str): [description]

    Returns:
        tuple: (firstname, lastname)

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


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    # print(circle_area(5))
    # print([c2f(celsius) for celsius in range(0, 5)])
