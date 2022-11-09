# 약수의개수와덧셈-월간코드챌린지시즌2

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        count = 0
        for n in range(1, i+1):
            if i % n == 0:
                count += 1
        if count % 2 == 1:
            i = -i
        
        answer += i

    return answer