# https://school.programmers.co.kr/learn/courses/30/lessons/140108

def solution(s):
    answer = 0

    reset = 0
    start = ""
    start_cnt = 0
    other_cnt = 0

    for c in s:
        if reset == 0:
            start = c
            start_cnt = 1
            other_cnt = 0
            reset = 1
            answer += 1

        else:
            if c == start:
                start_cnt += 1
            else:
                other_cnt += 1

            if start_cnt == other_cnt:
                reset = 0
    return answer
