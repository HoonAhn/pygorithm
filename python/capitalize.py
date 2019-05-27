# https://www.hackerrank.com/challenges/capitalize/problem
# started 13/5/2019
# started 27/5/2019

def solve(s):
    return " ".join(map(lambda a : a.capitalize(), s.split(" ")))
