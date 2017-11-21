

def solution(a):
    """

    >>> solution([9, 4, -3, -10])
    3
    >>> solution([2, 4, 18, -100, 91, 53])
    3
    """
    if(len(a) < 1):
        return -1
    sum = 0
    i = 0
    while i < len(a):
        sum += a[i]
        if a[i] < 0:
            a[i] *= -1
        i += 1

    avg = sum / len(a)

    max = 0
    index = 0
    i = 0
    while i < len(a):
        if a[i] - avg > max:
            max = a[i] - avg
            if max < 0:
                max *= -1
            index = i
        i += 1

    return index



if __name__ == '__main__':
    print('test')
    a = [9, 4, -3, -10]
    b = [2, 4, 18, -100, 91, 53]
    print (solution(b))