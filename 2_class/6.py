# 예산 - Summer/Winter Coding(~2018)

def solution(d, budget):
    count = 0
    d.sort()
    for i in range(0, len(d)):
        if budget >= d[i]:
            budget -= d[i]
            count += 1

    return count

'''
뽀인트 :  if budget >= d[i]
'''