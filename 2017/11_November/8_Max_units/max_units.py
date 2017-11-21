def maximumUnitsSold(unitsSold):
    """

    Parameters
    ----------
    unitsSold

    Returns
    -------

    Tests
    ------
    >>> maximumUnitsSold([-1, -2, 1, 3, -9])
    4
    >>> maximumUnitsSold([-1, -2, 1, 3, -5, 10, 9])
    19
    >>> maximumUnitsSold([10, 2, -2, 2, 2])
    14

    """

    max = unitsSold[0]
    total = 0
    for i, v in enumerate(unitsSold):
        j = i + 1
        while j < len(unitsSold) + 1:
            for k, v2 in enumerate(unitsSold[i:j]):
                total += v2
            max = total if max < total else max
            total = 0
            j += 1
    return max


if __name__ == '__main__':
    a = [-1, -2, 1, 3, -5, 10, 9]
    print(maximumUnitsSold(a))
    res = maximumUnitsSold(a)
    print(str(res) + "\n")