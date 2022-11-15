# 소수 만들기 - Summer/Winter Coding(~2018)
from itertools import combinations

def solution(nums):
    count = 0
    random_nums = list(combinations(nums, 3))
    random_nums_cnt = len(random_nums)

    def is_prime_number(num):
        if num==0 or num==1:
            return False
        else:
            for n in range(2, (num//2)+1):
                if num % n == 0:
                    return False        
            return True
            
    for i in range(0, random_nums_cnt):
        num = sum(random_nums[i])

        if is_prime_number(num) == True:
            count += 1

    return count



'''
소수 : N이 N의 제곱근보다 크지 않은 어떤 소수로도 나눠지지 않는다. 수가 수를 나누면 몫이 발생하게 되는데 몫과 나누는 수, 둘 중 하나는 반드시 N의 제곱근 이하이기 때문입니다.

->  i * i ≤ n 일 때까지만 비교하면 됨

+ 튜터님 Tip!
#1. 소수 만들기 문항에서 'cominations'를 이용하면 훨씬 우아하게 풀 수 있습니다.
'from itertools import combinations' 로 import해서 사용하시면 되구요,
많이 사용되니 용례를 학습해보시면 좋을 것 같습니다.
(+ https://ourcstory.tistory.com/414 )

#2. 어떤 값이 소수인지 여부를 판단하는 간단한 함수
def is_prime_number(num):
    if num==0 or num==1:
        return False
    else:
        for n in range(2, (num//2)+1):
            if num % n == 0:
                return False        
        return True
'''