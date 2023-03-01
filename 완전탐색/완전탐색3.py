# 소수찾기
# https://school.programmers.co.kr/learn/courses/30/lessons/42839


def is_prime_number(x):
    if x == 0: return False
    if x == 1: return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def solution(numbers):
    answer = 0
    nums = [x for x in numbers]

    from itertools import permutations
    st = set()

    for i in range(1, len(numbers) + 1):
        p_nums = list(permutations(nums, i))

        for p_num in p_nums:
            str = ''
            for p in p_num:
                str += p

            st.add(int(str))
    for i in st:
        if is_prime_number(i): answer += 1


    return answer