# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# solved 20/4/20

def twoStrings(s1, s2):
    check = "NO"
    for c in "abcdefghijklmnopqrstuvwxyz":
        if c in s1 and c in s2:
            check = "YES"
            break
    return check
    
print(twoStrings("hello", "world"))