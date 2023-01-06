# 올바른 괄호 - 스택/큐
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    answer = True
    if (s[0] == ')') or (s[-1] == '('):
        answer = False
    elif s.count('(') == s.count(')'):
        answer = True
    else:
        answer = False

    return answer

# 스택 -> 1)반드시 호출되는 함수  2) return값 있으면 호출됭 함수 삭제 -> 최종 return 값에 아무것도 업으면 쌍과, 순서가 모두 맞은것


def solution (s):
    stack = []

    for c in s:
        if c == "(":
            stack. append (c)
        else:
            if stack != []: # 쌍이 있다면
                stack.pop ()
            else:
                return False
    if stack != []:
        return False 
    
    return True
