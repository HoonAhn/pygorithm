# https://www.hackerrank.com/challenges/merge-the-tools/problem
# started   19/4/11
# solved    19/4/11
import collections

def merge_the_tools(string, k):
    subseg = []
    for i in range(0,len(string),k):
        subseg.append(string[i:i+k])
    for seg in subseg:
        od = collections.OrderedDict.fromkeys(seg)
        print(''.join(od.keys()))

string, k = input(), int(input())
merge_the_tools(string, k)