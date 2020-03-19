# https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# started 20/3/20

def birthdayCakeCandles(ar):
    tallest = -1
    count = 0
    for i in ar:
        if i > tallest:
            tallest = i
            count = 1
        elif i == tallest:
            count += 1
    return count
