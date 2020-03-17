# https://www.hackerrank.com/challenges/staircase/problem?h_r=next-challenge&h_v=zen
# solved 20/3/17

def staircase(n):
    for i in range(n):
        print(" "*(n-1-i)+"#"*(i+1))