# https://school.programmers.co.kr/learn/courses/30/parts/12230
# 모의고사

def solution(answers):
    answer = []

    a_cnt = 0
    b_cnt = 0
    c_cnt = 0

    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        an = i % 5
        bn = i % 8
        cn = i % 10

        if answers[i] == a[an]:
            a_cnt += 1
        if answers[i] == b[bn]:
            b_cnt += 1 
        if answers[i] == c[cn]:
            c_cnt += 1 

    max_num = max(a_cnt, b_cnt, c_cnt)

    if max_num == a_cnt:
        answer.append(1)
    if max_num == b_cnt:
        answer.append(2)
    if max_num == c_cnt:
        answer.append(3)

    return answer

