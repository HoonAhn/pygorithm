# https://engineering.linecorp.com/ko/blog/2019-firsthalf-line-internship-recruit-coding-test/?fbclid=IwAR1REqGafuf_XX_lv-qZhwf9WLSxaltrU7wGTsXxQe_cMIugxodFvPqaOrM


# B catch C : B wins
# C runs away: C wins
# return the min time game ends
#   
MAX_RANGE = 200000
MIN_RANGE = 0
# def catch_me_if_you_can(c:int, b:int):
#     sec = 0
#     cony = c
#     saved_cony = cony
#     brown = b
#     q = []
#     while cony > MAX_RANGE or cony == brown: 
#         sec += 1
#         cony += saved_cony + sec
#         brown +=1
    
#     if cony > MAX_RANGE :
#         return -1
#     elif cony == brown:
#         return sec
#     else:
#         print("what...")
#         return 0


def catch_me_if_you_can(c:int, b:int):
    time = 0
    q = []
    visit = [[0,0] for _ in range(MAX_RANGE+1)]
    q.append([b,0])

    while True :
        c += time
        if c > MAX_RANGE:
            return -1
        if (visit[c][time%2]):
            return time
        
        for _ in range(len(q)):
            current_position = q[0][0]
            new_time = (q[0][1]+1) % 2
            new_position = 0

            q.pop(0)

            new_position = current_position - 1
            if (new_position >= MIN_RANGE and visit[new_position][new_time] == False):
                visit[new_position][new_time] = True
                q.append([new_position,new_time])
            
            new_position = current_position + 1
            if (new_position <= MAX_RANGE and visit[new_position][new_time] == False):
                visit[new_position][new_time] = True
                q.append([new_position,new_time])

            new_position = current_position * 2
            if (new_position <= MAX_RANGE and visit[new_position][new_time] == False):
                visit[new_position][new_time] = True
                q.append([new_position,new_time])
        time += 1

print(catch_me_if_you_can(6, 3))