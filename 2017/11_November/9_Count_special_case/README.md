#Description

We consider a string "special" if it can be read the same way both forwards and backwards (e.g. abcba). The business team is asking us to write a program to help with this process. Complete the countSpecialStrings function in your editor. It has 1 parameter: an order ID, orderId. It must return an integer denoting the number of unique "special" substrings of orderId.

#Input Format

The locked stub code in your editor reads the following input from stdin and passes it to your function:

First line contains a string orderId consisting of lowercase ascii characters.

#Constraints
* Order Ids have at least 1 character and no more than 5000 characters: 1 ≤ size of orderId ≤ 5000 
* Order Ids consist of lowercase letters: 'a' ≤ orderId i ≤ 'z'

#Output Format

Your function must return an integer denoting the number of "special" sub-strings contained in the order ID.

This is printed to stdout by the locked stub code in your editor.

##Sample Case 0

###Sample Input

    aabaa

###Sample Output

    5

Explanation The special strings in the orderId are: a, a, a, a, b, aa, aa, aba, aabaa The unique special strings in the orderId are: a, aa, aabaa, aba, b The special string 'a' occurs 4 times, but we are looking for unique strings. Hence it is counted only once. Similarly, the string 'aa' occurs twice but is only counted once.