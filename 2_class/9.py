# 실패율 - 2019 KAKAO BLIND RECRUITMENT

def solution(N, stages):
    fail = {}
    all_user = len(stages) # 전체 이용자 수

    for i in range(1, N+1):
        this_user = stages.count(i) # 해당 스테이지 user수

        if this_user == 0:  # 해당 스테이지 user가 없으면 실패율 = 0 
            fail[i] = 0
        else:
            fail[i]= this_user / all_user  # 해당 스테이지의 실패율
            all_user -= this_user   # user가 없으면 전체 사용자에서 빼줄 필요 없으므로 else 이후 부분에서만 this_user수를 빼줌

    s_fail= sorted(fail, key=fail.get, reverse=True)    # 이부분은 https://gomgomkim.tistory.com/26  참고함!

    return s_fail


'''
1. 전체 사용자 수 -> len으로 구함

2. 각 스테이지별 실패율 구하고 -> 해당 스테이지 만큼의 user를 전체 user수에서 빼준다. 
+ 제한 : 스테이지에 도달한 사용자가 0명인 경우 예외 처리.

3. 실패율을 내림차순으로 정렬한다. (https://gomgomkim.tistory.com/26  참고)
+ 제한 : 만약 실패율이 같은 스테이지가 있다면, 작은 번호의 스테이지가 먼저 오도록 한다.

+ 스테이지 번호, 실패율이 연관되어 있으므로 딕셔너리? key:스테이지번호, value:실패율 -> 실패율 내림차순하고 key불러와?
'''