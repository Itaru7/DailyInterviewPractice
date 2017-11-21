from itertools import permutations


def permutation(lst, num = None):
    """

    Parameters
    ----------
    lst
    num

    Returns
    -------

    Tests
    ------
    >>> permutation([2, 6, 3, 8, 1])
    12368
    12386
    12638
    12683
    12836
    12863
    13268
    13286
    13628
    13682
    13826
    13862
    16238
    16283
    16328
    16382
    16823
    16832
    18236
    18263
    18326
    18362
    18623
    18632
    21368
    21386
    21638
    21683
    21836
    21863
    23168
    23186
    23618
    23681
    23816
    23861
    26138
    26183
    26318
    26381
    26813
    26831
    28136
    28163
    28316
    28361
    28613
    28631
    31268
    31286
    31628
    31682
    31826
    31862
    32168
    32186
    32618
    32681
    32816
    32861
    36128
    36182
    36218
    36281
    36812
    36821
    38126
    38162
    38216
    38261
    38612
    38621
    61238
    61283
    61328
    61382
    61823
    61832
    62138
    62183
    62318
    62381
    62813
    62831
    63128
    63182
    63218
    63281
    63812
    63821
    68123
    68132
    68213
    68231
    68312
    68321
    81236
    81263
    81326
    81362
    81623
    81632
    82136
    82163
    82316
    82361
    82613
    82631
    83126
    83162
    83216
    83261
    83612
    83621
    86123
    86132
    86213
    86231
    86312
    86321

    >>> permutation([1, 4, 5], 2)
    14
    15
    41
    45
    51
    54


    """
    perm = list(permutations(lst, num))
    perm.sort()

    for i in perm:
        print(''.join(str(x) for x in i))


if __name__ == '__main__':
    permutation([1, 4, 5], 2)
    #permutation([2, 6, 3, 8, 1])
