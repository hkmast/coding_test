# https://school.programmers.co.kr/learn/courses/30/lessons/147355


def solution(t, p):
    answer = 0

    # print('p', p)
    length = len(p)
    p = int(p)
    for i in range(0, len(t) - length + 1):
        t_sliced = int(t[i : i + length])
        # print('sliced', t_sliced)
        if t_sliced <= p:
            answer += 1

    # print('ans', answer)
    return answer
