# 핸드폰 번호 가리기

def solution(phone_number):
    answer = ''
    answer = phone_number.replace(phone_number[:-4], '*'*len(phone_number[:-4]))
    return answer


phone_number = "01033334444"
print(solution(phone_number))