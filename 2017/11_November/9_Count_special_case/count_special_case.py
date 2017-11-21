
def count_special_strings(orderId):
    """

    Parameters
    ----------
    orderId

    Returns
    -------

    Tests
    -------
    >>> count_special_strings('aabaa')
    5
    >>> count_special_strings('ItaruratI')
    9

    """
    result = 0
    unique_lst = []
    i = 0
    while i < len(orderId):
        j = i
        while j < len(orderId):
            substr = orderId[i:j + 1]
            if substr == substr[::-1] and not substr in unique_lst:
                unique_lst.append(substr)
            j += 1
        i += 1
    return len(unique_lst)

if __name__ == '__main__':
    a = 'aabaa'
    print(count_special_strings(a))