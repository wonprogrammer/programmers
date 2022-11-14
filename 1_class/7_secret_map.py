# 비밀지도 - 2018 KAKAO BLIND RECRUITMENT

''' 처음시도 코드
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

# 1. 비트연산과 이진수 변환을 이용한 답안코드
def solution(n, arr1, arr2):
    answer = [''] * n
    for i in range(len(arr1)):
        bin1 = bin(arr1[i])[2:].zfill(n)
        bin2 = bin(arr2[i])[2:].zfill(n)
        for j in range(n):
            if bin1[j] == '0' and bin2[j] == '0':
                answer[i] += ' '
            else:
                answer[i] += '#'
    return answer
#한 문자열에 'n의 크기'만큼 들어가야 하므로 append로 넣어주게 되면 '하나'하나씩 들어가게 되어 원하는 값을 받을 수 없다


'''
벽# =1 - or
공백""=0 - and

bin함수는 구글링을 통해 습득
'''