# 콜라츠 추측

def solution(num):
    answer = 0
    count = 0
    while True:
        if num%2 == 0:
            num = num/2
            count += 1
            if num == 1:
                break
        else :
            num = (num*3)+1
            count += 1
            if num == 1:
                break
    
    if count >= 500 or num != 1:
        return -1
    else:
        return count

    
# TC : 13번 에러