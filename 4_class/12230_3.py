# https://school.programmers.co.kr/learn/courses/30/parts/12230
# 소수찾기 (완전탐색 유형의 알고리즘 풀이를 주의 깊게 볼 것)


def is_prime_number(num):
    if num==0 or num==1:
        return False
    else:
        for n in range(2, (num//2)+1):
            if num % n == 0:
                return False        
        return True

def solution(numbers):
    n_len = len(numbers)

    answer = 0
    return answer
