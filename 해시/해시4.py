# https://school.programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1

    clothes_dict = {}

    for clothe in clothes:
        if not clothes_dict.get(clothe[1]):
            clothes_dict[clothe[1]] = 1
        else:
            clothes_dict[clothe[1]] += 1

    for clothe in clothes_dict:
        answer *= (clothes_dict[clothe] + 1)

    answer -= 1

    return answer