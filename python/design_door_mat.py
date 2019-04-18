# https://www.hackerrank.com/challenges/designer-door-mat/problem
# started 19/4/15
# solved 19/4/18

N, M = map(int,input().split())

for i in range(N):
    line = ''
    if i == (int)(N/2):
        line = '-'*(int)((M-7)/2)+'WELCOME'+'-'*(int)((M-7)/2)
    else:
        m = min(i*2+1, (N-i-1)*2+1)
        line = "---" * (int)((N-m)/2) + (".|." * m) + '---' * (int)((N-m)/2)
    print(line)
