# https://www.hackerrank.com/challenges/python-lists/problem
# Started 19/03/27
# Unsolved

N = int(input())
result = []
for i in range(0, N):
    cmd = list(map(str, input().split()))
    if len(cmd) == 1:
        if cmd[0]=="print":
            eval("print(result)")
        else:
            eval("result.{0}()".format(cmd[0]))
    elif len(cmd) == 2:
        eval("result.{0}({1})".format(cmd[0], cmd[1]))
    elif len(cmd) == 3:
        eval("result.{0}({1},{2})".format(cmd[0], cmd[1], cmd[2]))
    
    





