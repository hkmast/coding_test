# https://school.programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    answer = []
    rank = []

    cnt = 0
    ans = [1, 2, 3, 4, 5]
    for idx, a in enumerate(answers):
        if ans[idx % len(ans)] == a:
            cnt += 1
    rank.append(cnt)

    cnt = 0
    ans = [2, 1, 2, 3, 2, 4, 2, 5]
    for idx, a in enumerate(answers):
        if ans[idx % len(ans)] == a:
            cnt += 1
    rank.append(cnt)

    cnt = 0
    ans = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for idx, a in enumerate(answers):
        if ans[idx % len(ans)] == a:
            cnt += 1
    rank.append(cnt)

    for i, r in enumerate(rank):
        if max(rank) == r:
            answer.append(i + 1)

    return answer
