# https://www.hackerrank.com/challenges/python-lists/problem
# Started   19/03/27
# Solved    19/03/27
# Improved  19/03/30

N = int(input())
result = []
for i in range(0, N):
    cmd = list(map(str, input().split()))
    f = cmd[0]
    arg = cmd[1:]
    if f=="print":
        eval("print(result)")
    else:
        arg_str = ""
        if len(arg)>0:
            arg_str = ",".join(arg)
        eval("result.{0}({1})".format(f,arg_str))