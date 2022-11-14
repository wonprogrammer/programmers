# 나머지가1이되는수찾기-월간코드챌린지시즌3

def solution(n):
    answer = 0
    x = 1
    while x < n:
        if n % x == 1:
            answer = x
            break
        else:
            x += 1

    return answer