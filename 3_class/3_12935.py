# 제일작은수제거하기

def solution(arr):
    answer = []
    if len(arr) > 1:
        arr.remove(min(arr))
        
        return arr
    else:
        answer.append(-1)
        return answer