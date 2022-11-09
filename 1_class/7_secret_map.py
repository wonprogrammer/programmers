# 비밀지도 - 2018 KAKAO BLIND RECRUITMENT

def solution(n, arr1, arr2):
    code = ''
    answer = []
    for i in range(n):
        x = arr1[i]
        y = arr2[i]

        x=bin(int(x))
        y=bin(int(y))

        if x[i] or y[i] == '1':
            code.append('#')
        elif x[i] and y[i] == '0':
            code.append(' ')
            
    return answer


'''
벽# =1 - or
공백""=0 - and

bin함수는 구글링을 통해 습득
'''