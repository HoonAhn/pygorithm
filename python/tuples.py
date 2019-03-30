# https://www.hackerrank.com/challenges/python-tuples/problem
# started   19/3/30
# solved    19/3/30

N = int(input())
print(hash(tuple(map(int,input().split()))))