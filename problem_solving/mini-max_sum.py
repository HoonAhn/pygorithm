# https://www.hackerrank.com/challenges/mini-max-sum/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# solved 20/3/17

def miniMaxSum(arr):
    min_num = 1000000001
    max_num = 0
    total = 0
    for i in arr:
        if min_num > i:
            min_num = i
        if max_num < i:
            max_num = i
        total += i
    print(total-max_num, total-min_num)

    