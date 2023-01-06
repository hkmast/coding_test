# https://school.programmers.co.kr/learn/courses/30/lessons/12909
def solution(s):
    answer = True
    stack = []

    for c in s:
        if c == '(':
            stack.append(1)
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                return False

    if len(stack) != 0:
        return False

    return True

print(solution("(()("))
