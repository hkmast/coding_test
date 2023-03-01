# 피로도
# https://school.programmers.co.kr/learn/courses/30/lessons/87946

def solution(k, dungeons):
    import itertools

    answer = -1

    for per_lists in list(itertools.permutations(dungeons, len(dungeons))):
        tmp = k
        cnt = 0
        for per_list in per_lists:
            if per_list[0] <= tmp:
                tmp -= per_list[1]
                cnt += 1

        if answer < cnt:
            answer = cnt

    return answer