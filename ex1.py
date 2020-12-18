# doctest

def rectangle_area(w, h):
    '''
    >>> rectangle_area(5, 2)
    10
    >>> rectangle_area(10, 2.5)
    25.0
    >>> rectangle_area(-10, 2.5)
    Traceback (most recent call last):
        ...
    ValueError: w, h > 0
    '''
    if w < 0 or h < 0:
        raise ValueError('w, h > 0')
    return w * h

def triangle_area(b, h):
    """พื้นที่สามเหลี่ยม

    Args:
        b ([type]): ฐาน
        h ([type]): สูง

    Returns:
        [type]: triangle area

    Tests:
    >>> triangle_area(10, 5)
    25.0
    >>> triangle_area(4, 2)
    4.0
    """    
    return .5 * b * h

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    # a=rectangle_area(-10, 25)
    # a=rectangle_area()
    # print(rectangle_area(5, 2))
    # print(rectangle_area(10, 2.5))
