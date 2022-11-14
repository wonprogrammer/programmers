# 같은숫자는싫어-스택/큐

def solution(arr):
    stack = [10]
    for i in range(0, len(arr)):
        if arr[i] != stack[-1]:
            stack.append(arr[i])
            
    stack.pop(0)

    return stack

'''
약간 야매로 품
'''