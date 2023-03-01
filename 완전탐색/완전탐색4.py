# 카펫
# https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []

    for h in range(3, brown):
        w = (brown + yellow) / h
        if (w == int(w)) and (yellow == (w - 2) * (h - 2)):
            return [w, h]
