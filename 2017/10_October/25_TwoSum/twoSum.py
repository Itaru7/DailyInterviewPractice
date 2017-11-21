

def twoSum(targetNum, numList):
    """

    Parameters
    ----------
    targetNum
    numList

    Returns
    -------

    Tests
    ------
    >>> twoSum(6, [3, 3])
    [0, 1]
    >>> twoSum(9, [2, 7, 11, 15])
    [0, 1]

    """
    match = False
    index = 0
    temp = targetNum
    first = 0
    second = 0
    while not match:
        temp -= numList[index]
        for i, v in enumerate(numList):
            if (temp - v == 0) and (index != i):
                first = index
                second = i
                match = True
        temp = targetNum
        index += 1
    result =[first, second]
    return [first, second]

if __name__ == '__main__':
    number = input('Please Enter Numbers>>')
    numberlist = number.split()
    numberlist = [int(a) for a in numberlist]
    target = int(input('Please Enter Targeted Number>>'))
    print(twoSum(target, numberlist))