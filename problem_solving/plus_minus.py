# https://www.hackerrank.com/challenges/plus-minus/problem
# solved 20/3/17

def plusMinus(arr):
    postive = 0
    negative = 0
    zero = 0
    for i in arr:
        if i > 0:
            postive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1
    print("%5f" % (postive/len(arr)))
    print("%5f" % (negative/len(arr)))
    print("%5f" % (zero/len(arr)))