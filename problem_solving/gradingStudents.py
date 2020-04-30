# https://www.hackerrank.com/challenges/grading/problem
# solved 20/04/30

def gradingStudents(grades):
    result = []
    for g in grades:
        next_grade = ((g//5)+1)*5
        if g < 38:
            result.append(g)
        elif next_grade - g < 3:
            result.append(next_grade)
        else:
            result.append(g)
    return result
