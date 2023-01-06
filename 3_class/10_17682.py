# 다트 게임 2018 KAKAO BLIND RECRUITMENT
# https://school.programmers.co.kr/learn/courses/30/lessons/17682

'''
def solution(dartResult):
    answer = 0
    return answer
'''


'''
다트 게임은 총 3번의 기회로 구성된다.
각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.
'''

def solution (dartResult):
    nums = []
    temp = 0
    strIdx = 0

    for i in dartResult:
        if "0" <= i <= "9":
            temp = temp * 10 + int (i)
        elif i == "S":
            nums. append(temp)
            temp = 0
            strIdx += 1 
        elif i == "D":
            nums.append (temp**2)
            temp = 0
            strIdx += 1 
        elif i == "T":
            nums.append(temp ** 3)
            temp = 0
            strIdx += 1 
        elif i == "*":
            if strIdx > 1:
                nums [strIdx - 2] *= 2
            nums [strIdx - 1] *= 2 
        elif i == "#":
            nums [strIdx - 1] *= -1
            
    return sum(nums)