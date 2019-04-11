# https://www.hackerrank.com/challenges/the-minion-game/problem?h_r=next-challenge&h_v=zen
# started 19/3/30
# sovled 19/4/11

# substring의 개수를 세는 것은 함정이다.
# 규칙을 생각해보면 각 인덱스부터 한개씩 늘어나는 것은 무조건 카운트되기 때문에 
# 처음 자음/모음을 구분할 때 총 길이에서 뺀 만큼을 더해버리면 된다.

VOWEL = set(['A','E','I','O','U'])

string = input()
l = len(string)
vowel_sum = 0
conso_sum = 0

for i in range(l):
    if string[i] in VOWEL:
        vowel_sum += (l-i)
    else: 
        conso_sum += (l-i)

if conso_sum > vowel_sum:
    print("{0} {1}".format("Stuart", conso_sum))
elif conso_sum < vowel_sum:
    print("{0} {1}".format("Kevin", vowel_sum))
else:
    print("Draw")