# https://school.programmers.co.kr/learn/courses/30/lessons/1845

# 제일 깔끔한 버전
'''
def solution(nums):
    return min(len(nums)/2, len(set(nums)))
'''

def solution(nums):
    answer = 0
    N = len(nums)
    dic = dict()

    for num in nums:
        if not dic.get(num):
            dic[num] = 1
        else:
            dic[num] += 1

    cat = len(dic)

    answer = min(N/2, cat)

    return answer
