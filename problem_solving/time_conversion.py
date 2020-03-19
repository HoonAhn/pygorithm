# https://www.hackerrank.com/challenges/time-conversion/problem?h_r=next-challenge&h_v=zen
# solved 20/3/20

def timeConversion(s):
    timezone = s[-2:]
    hour = int(s[:2])
    if hour == 12:
        hour = 0
    if timezone == "PM":
        hour += 12
    if hour < 10:
        hourStr = "0{0}".format(hour)
    else:
        hourStr = "{0}".format(hour)
    return hourStr+s[2:-2]
