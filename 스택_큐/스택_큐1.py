# https://school.programmers.co.kr/learn/courses/30/lessons/12906
def solution(arr):
    answer = [arr[0]]

    for char in arr:
        if char != answer[-1]:
            answer.append(char)
        else:
            pass

    return answer
