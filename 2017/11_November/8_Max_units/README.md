# Description

In order to calculate this, we have obtained a list containing the number of units sold for a particular item over n consecutive days. Your task is to calculate the sum of the number of items sold in a sub period (i.e., across contiguous days) such that the sum is maximal.

Complete the maximumUnitsSold function in your editor. It has 1 parameter: an array of integers, unitsSold, representing the number of units sold across n consecutive days. It must return a long integer denoting the maximum sum for any contiguous time period in unitsSold.

# Input Format

The locked stub code in your editor reads the following input from stdin and passes it to your function:

The ﬁrst line contains an integer, n, denoting the size of array unitsSold.

Each line i of the n subsequent lines contains the number of units sold for day i in unitsSold.

# Constraints

   * The number of days in the data set will be less than 10^6 : 1 ≤ n ≤ 10^6 
   * The number of units sold for a given day will be between −10^7 and 10^7 : −10^7 ≤ unitsSold i ≤ 10^7

# Output Format

Your function must return a long integer denoting the maximum total number of units sold for any contiguous time period in unitsSold. This is printed to stdout by the locked stub code in your editor.

## Sample Case 0

### Sample Input

    4 
    -1 
    -2
    1
    3

### Sample Output

    4   

### Explanation

1/3 The maximum total number of units sold for any contiguous time period in [−1, −2, 1, 3] is 1 + 3 = 4


## Sample Case 1

### Sample Input

    4
    1
    2
    3 
    4

### Sample Output

    10

Explanation The maximum total number of units sold for any contiguous time period in [1, 2, 3, 4] is 1 + 2 + 3 + 4 = 10, so we return 10.