# 완주하지 못한 선수 – 해시

''' 처음시도 코드
def solution(participant, completion):
    answer = ''
    for i in completion:
        if i in participant:
            participant.remove(i)
            answer = participant[0]
    
    return answer
'''

# 1. 외부모듈 이용한 해결방법
import collections 
def solution(participant, completion): 
    answer = collections.Counter(participant) - collections.Counter(completion) 
    return list(answer.keys())[0]

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))

# 2. 딕셔너리 활용
def solution(participant, completion): 
    temp = {}
    for i in participant : 
        if i in temp :
            temp[i]+=1 
        else:
            temp[i] =1

    for i in completion : 
        if temp[i]==1 :
            del temp[i] 
        else :
            temp[i] -=1 
    
    return list(temp.keys())[0]