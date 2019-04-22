# https://www.hackerrank.com/challenges/python-string-formatting/problem
# started   19/4/22
# solved    19/4/22
number = int(input())
w = len("{0:b}".format(number))
for i in range(1, number+1):
    print(("{0:{w}d} {0:{w}o} {0:{w}x} {0:{w}b}".format(i, w=w)).upper())