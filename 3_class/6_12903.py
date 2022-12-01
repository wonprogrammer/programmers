# 가운데 글자 가져오기

def solution(s):
    answer = ''
    n = 0
    if len(s) % 2 == 0:
        n = len(s)//2
        answer = s[n-1]+s[n]
        return answer
    else :
        n = len(s)//2
        answer = s[n]
        return answer
