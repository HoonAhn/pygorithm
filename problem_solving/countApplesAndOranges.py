# https://www.hackerrank.com/challenges/apple-and-orange/problem?h_r=next-challenge&h_v=zen
# sovled 20/04/30

def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = 0
    oragne_count = 0
    for apple in apples:
        if a+apple >= s and a+apple <= t:
            apple_count += 1
    for orange in oranges:
        if b+orange <= t and b+orange >= s:
            oragne_count += 1
    print(apple_count)
    print(oragne_count)