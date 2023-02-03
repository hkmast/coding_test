# https://school.programmers.co.kr/learn/courses/30/lessons/133502

def solution(ingredient):
    answer = 0

    stack = []

    ham = [1, 2, 3, 1]

    for i in ingredient:
        stack.append(i)

        if len(stack) < 4:
            continue
        else:
            if stack[-4:] == ham:
                answer += 1
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()

    return answer