# https://school.programmers.co.kr/learn/courses/30/lessons/42586
import math


def solution(progresses, speeds):
    answer = []
    q = []

    last_progresses = list(
        map(
            lambda x, d: math.ceil(x / d),
            list(map(lambda x: 100 - x, progresses)),
            speeds,
        )
    )
    # print(last_progresses)
    for prograss in last_progresses:
        if len(q) == 0:
            q.append(prograss)
        else:
            if prograss > q[0]:
                answer.append(len(q))
                q = [prograss]
            else:
                q.append(prograss)

        # print(q)

    if q:
        answer.append(len(q))

    return answer
