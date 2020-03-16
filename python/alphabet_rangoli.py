# https://www.hackerrank.com/challenges/alphabet-rangoli/problem
# started 19/4/24

N = int(input())

alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(1,N+1):
    line = '--'*(N-i)
    for j in range(i):
        
