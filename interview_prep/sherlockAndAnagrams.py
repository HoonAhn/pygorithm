# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen
# started 20/04/20

# def isAnagram(s1,s2):
#     d = {}
#     for c in s1:
#         if c in d:
#             d[c] += 1
#         else:
#             d[c] = 1
#     for c in s2:
#         if c in d:
#             if d[c] > 1:
#                 d[c] -= 1
#             else:
#                 del(d[c])
#         else:
#             return False
#     if len(d.keys()) > 1:
#         return False
#     else: 
#         return True

# def sherlockAndAnagrams(s):
#     d = {}
#     count = 0
#     for i in range(len(s)):
#         for j in range(i+1, len(s)+1):
#             rev = make_reverse(s[i:j])
#             if rev in d:
#                 count+=1
#                 d[rev] = None
#             else :
#                 d[s[i:j]] = [i,j]
#     return count

def sherlockAndAnagrams(s): 
    combinations=[] 
    count=0 
    for i in range(1,len(s)+1): 
        for j in range(len(s)-i+1): 
            a = "".join(sorted(s[j:j+i])) 
            combinations.append(a)
    for i,s in zip(combinations,range(len(combinations))):
        for j in range(s+1,len(combinations)):
            if(i == combinations[j]):
                count+=1
    return(count)
print(sherlockAndAnagrams("ifaiuhkqq"))