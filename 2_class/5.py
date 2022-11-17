# 음양더하기-월간코드챌린지시즌2

def solution(absolutes, signs):
    answer = 0
    for i in range(0, len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]

    return answer


'''
# 1.
    for i in range(0, len(absolutes)):
        if signs[i] == 'true':
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    먼저 이렇게 정의했다가 음수로만 더해지는걸 보고,

# 2.
    for i in range(0, len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    이렇게 바꿔서 했더니 됨, 근데 'if signs[i]:' 이부분에서 true,false를 정의해주지 않아도 왜 실행이 잘 되는지 이해하지 못함
'''