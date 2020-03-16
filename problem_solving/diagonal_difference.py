# https://www.hackerrank.com/challenges/diagonal-difference/problem
# solved 20/3/16

def diagonalDifference(arr):
    left = 0
    right = 0
    for i in range(int(len(arr)/2)):
        left += arr[i][i] - arr[i][len(arr)-1-i]
        right += arr[len(arr)-1-i][i] - arr[len(arr)-1-i][len(arr)-1-i]
    return abs(left-right)