def second_largest(arr):
    """

   Parameters
   ----------
   arr

   Returns
   -------
    second_max

    Tests
    -----
    >>> second_largest([9, 4, -3, -10])
    4
    >>> second_largest([2, 4, 18, -100, 91, 53])
    53
    >>> second_largest([2, 3, 6, 6, 5])
    5
    >>> second_largest([-99, -99])
    -99
    >>> second_largest([0, 1, -1])
    0
    >>> second_largest([0, 0, -1])
    -1
    >>> second_largest([-2, -2, -1])
    -1
   """
    max_value = max(arr)
    diff = 201
    second_max = 0
    only_max = False
    for v in arr:
        t = max_value - v
        if (t < diff) and (not t == 0):
            second_max = v
            diff = t
            only_max = True
    if not only_max:
        second_max = max_value
    return second_max

    """
    max_value = max(arr)
    second_max = 0
    only_max = False
    if max_value > 0:
        for v in arr:
                if (not v == max_value) and (second_max <= v):
                    second_max = v
                    only_max = True
    else:
        for v in arr:
            if (not v == max_value) and (second_max >= v):
                second_max = v
                only_max = True
    if not only_max:
        second_max = max_value
    return second_max
    """


if __name__ == '__main__':
    a = [9, 4, -3, -10]
    b = [2, 4, 18, -100, 91, 53]
    c = [0, 1, -1]
    d = [0, 0, -1]
    e = [-2, -2, -1, 1]
    print(second_largest(e))
