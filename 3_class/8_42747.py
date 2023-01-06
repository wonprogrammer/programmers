# H-Index - 정렬
# https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    citations.sort()
    c_len = len(citations)
    c_half_len = len(citations) // 2

    if c_len%2 == 1:
        answer = citations[c_half_len]
    else:
        answer = citations[c_half_len - 1]
    return answer


'''
어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

citations : len = 논문갯수 / index = 인용횟수
해당 숫자 포함(보다큰) 갯수가 len중에 젤 많다면 그거임

-> h번 이상 인용된 h편의 논문 찾기!
알고리즘에서 빈번하게 쓰임 : enumerate
'''


def solution(citations):
    citations.sort(reverse=True)

    for idx , citation in enumerate (citations):
        if idx >= citation:
            return idx
    return len (citations)

print(solution ([3, 0, 6, 1, 5]))