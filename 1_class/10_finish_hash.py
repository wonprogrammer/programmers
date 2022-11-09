# 완주하지 못한 선수 – 해시

def solution(participant, completion):
    answer = ''
    for i in completion:
        if i in participant:
            participant.remove(i)
            answer = participant[0]
    
    return answer