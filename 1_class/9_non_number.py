# 없는숫자더하기-월간코드챌린지시즌3

def solution(numbers):
    answer = 0
    for n in range(0,10,1):
        if n not in numbers:
            answer += n
    
    return answer