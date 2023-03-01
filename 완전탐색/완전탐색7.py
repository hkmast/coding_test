# 모음사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512


def solution(word):
    answer = 0

    word_dict = set()

    words = ["A", "E", "I", "O", "U", ""]

    for n1 in words:
        for n2 in words:
            for n3 in words:
                for n4 in words:
                    for n5 in words:
                        word_dict.add(n1 + n2 + n3 + n4 + n5)

    word_dict = list(word_dict)
    word_dict.sort()
    word_dict.pop(0)

    return word_dict.index(word) + 1
