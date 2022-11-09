# 자연수 뒤집어 배열로 만들기

def solution(n):
    n = str(n)
    answer = []
    for i in n[::-1]:
        i = int(i)
        answer.append(i)

    return answer

'''
for문에서 뒤에서 부터 반복하는 [::-1]는 구글링을 통해 알아냄
'''