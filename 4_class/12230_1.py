# https://school.programmers.co.kr/learn/courses/30/parts/12230
# 최소 직사각형

def solution(sizes):
    s_len = len(sizes)
    w = 0
    h = 0

    for i in range(s_len):
        sizes[i].sort()
        new_w = sizes[i][0]
        new_h = sizes[i][1]

        if new_w > w :
            w = new_w

        if new_h > h :
            h = new_h

    answer = w * h
    return answer

   

# 가로 세로 순으로 주어지지만 가로 세로를 바꿔 수납할 수 있기 때문에 주의 해야함
# 2차원 배열 

'''
sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
sizes[1].sort()
w = sizes[1][0]
print(w)

[[50, 60], [30, 70], [30, 60], [40, 80]]
'''