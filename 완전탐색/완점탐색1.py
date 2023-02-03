# https://school.programmers.co.kr/learn/courses/30/lessons/86491
def solution(sizes):
    answer = 0
    max_1 = 0
    max_2 = 0

    for size in sizes:
        size_1 = max(size)
        size_2 = min(size)

        if max_1 < size_1:
            max_1 = size_1
        if max_2 < size_2:
            max_2 = size_2

    answer = max_1 * max_2
    return answer
