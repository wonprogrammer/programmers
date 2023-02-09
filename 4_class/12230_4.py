# https://school.programmers.co.kr/learn/courses/30/parts/12230
# 카펫

def solution(brown, yellow):
    w = 0
    h = 0

    for i in range(yellow-1, 1, -1):
        if brown == ((i+2)+((yellow // i) + 2)):
            w = i+2
            h = (yellow // i) + 2
            break

    answer = [w,h]
    return answer


# yellow의 가로 세로 비율 중 {(가로 + 2)*2} + (세로 * 2) = brown 타일의 갯수와 같다면 
# [yellow의 가로+2 , yellow의 세로 +2] 가 정답