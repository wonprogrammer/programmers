# 문자열내p와y의개수

def solution(s):
    count_x = 0
    count_y = 0

    for i in s:
        if (i == 'p') or (i == 'P'):
            count_x += 1
        elif (i == 'y') or (i == 'Y'):
            count_y += 1

    if count_x == count_y:
        answer = True
    elif count_x != count_y:
        answer = False

    return answer