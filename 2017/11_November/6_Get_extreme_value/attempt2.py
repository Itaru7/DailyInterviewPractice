

def solution(a):
    """Return index of the most extreme value of given list.

    Examples
    --------
    >>> solution([9, 4, -3, -10])
    3
    >>> solution([2, 4, 18, -100, 91, 53])
    3
    """
    if not a:
        return -1

    total_sum = 0
    for i, v in enumerate(a[:]):
        total_sum += v
        if a[i] < 0:
            a[i] *= -1

    avg = total_sum / len(a)
    index = 0
    max_value = 0
    for i, v in enumerate(a[:]):
        if a[i] - avg > max_value:
            max_value = a[i] - avg
            if max_value < 0:
                max_value *= -1
            index = i

    return index



if __name__ == '__main__':
    print('test')
    a = [9, 4, -3, -10]
    b = [2, 4, 18, -100, 91, 53]
    print(solution(b))