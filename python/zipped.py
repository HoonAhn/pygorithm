# https://www.hackerrank.com/challenges/zipped/problem
# started 5/27
# solved  5/27

(N, X) = tuple(map(int,input().split(" ")))
scores = []
for i in range(X):
    score_list = list(map(float, input().split(" ")))
    scores.append(score_list)
student_score = zip(*scores)
for score in student_score:
    print("{0}".format(sum(score)/X))
