# 체육복 - 탐욕법(Greedy)

def solution(n, lost, reserve):
    student = 0
    for i in range(n):
        if i in lost:
            n -= 1
        
    for re in reserve:
        if (re+1) or (re-1) in lost:
            len(lost)-1
        

    answer = 0
    return answer




'''
n : 전체 학생 수
lost : 없는애
reserve : 2개 있는애

1) lost/reserve 에서 언급되지 않는 애들은 참가!
2) reserve + 1 or reserve - 1 중에 lost 가 있으면 +1 -> lost에서 받은애 지우고, reserve에서 준애 지우고
3) 이렇게 반복하다가 reserve + 1 or reserve - 1 중에 lost 가 없거나 / reserve가 없으면 => n에서 lost 수많큼 뺀 수가 참가 학생 수
'''