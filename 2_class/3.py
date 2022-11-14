# 정수 내림차순으로 배치하기

def solution(n):
    n = str(n)
    n = sorted(n, reverse=True) # reverse와 reversed의 차이?

    answer = "".join(n)
    answer = int(answer)

    return answer

print(solution(1652))


'''
리스트(배열)의 각 요소들을 하나로 합치는 것은 join() 함수로 할 수 있습니다. 그냥 하나로 합칠 수도 있고, 각 엘레멘트 사이에 구분자를 넣어서 합칠 수도 있습니다.


# 그냥 하나로 합치기
s = "".join(food)
print s
# 출력 결과: food속 원소들이 띄어쓰기 없이 합쳐짐


# 요소들 사이에 쉼표 넣기 (구분자는 콤마와 공백 1개)
s = ", ".join(food)
print s
# 출력 결과: food속 원소들이 ,로 구분되면서 합쳐짐

- http://mwultong.blogspot.com/2006/12/python-list-merge.html - 
'''