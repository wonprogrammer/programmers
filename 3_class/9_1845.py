# 폰켓몬-해시
# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    monster = list(set(nums)) 
    cnt=len(nums)//2# 기존에 뽑을 수 있는 만큼

    if len(monster) < cnt:
        return len(monster) # 중복 제거한 만큼
    
    return cnt
