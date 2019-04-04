# https://www.hackerrank.com/challenges/the-minion-game/problem?h_r=next-challenge&h_v=zen
# started 19/3/30

# 1. 자음/모음을 인덱스로 분류해서 저장
# 2. 각각 꺼내면서 +1 하며 단어를 만들고 dictionary에 있는지 검사
# 2-1. Dict에 없으면 생성
# 2-2. Dict에 있으면 +1

VOWEL = set(['A','E','I','O,','U'])

def isvowel(word: "str") -> bool:
    return word in VOWEL

def get_score(S, idx_list) -> int:
    l = len(S)
    word_dict = {}
    for idx in idx_list:
        for j in range(idx+1, l+1):
            if S[idx:j] in word_dict:
                word_dict[S[idx:j]] += 1
            else:
                word_dict[S[idx:j]] = 1
    return sum(word_dict.values())

string = input()
s_list = list(string)
vowel_idx = []
conso_idx = []

for i in range(0,len(s_list)):
    if isvowel(string[i]):
        vowel_idx.append(i)
    else: 
        conso_idx.append(i)

stuart = ("Stuart", get_score(string, conso_idx))
kevin = ("Kevin", get_score(string, vowel_idx))

if stuart[1] > kevin[1]:
    print("{0} {1}".format(stuart[0], stuart[1]))
else:
    print("{0} {1}".format(kevin[0], kevin[1]))



# def repeats(whole: "str", sub: "str") -> int:
#     whole_l = len(whole)
#     sub_l = len(sub)
#     repeat_count = 0
#     for i in range(0, whole_l-sub_l+1):
#         if sub == whole[i:i+sub_l]:
#             repeat_count += 1
#     return repeat_count