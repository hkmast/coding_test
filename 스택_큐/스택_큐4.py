# https://school.programmers.co.kr/learn/courses/30/lessons/42587
def solution(priorities, location):

    answer = 0

    priorities = [(priorities[x], x == location) for x in range(len(priorities))]

    # print(priorities)

    cnt = 0

    while priorities:
        print(priorities, cnt)
        tmp = priorities.pop(0)
        if priorities:
            if tmp[0] < max(priorities)[0]:
                priorities.append(tmp)
            else:
                cnt += 1
                if tmp[1]:
                    break

        else:
            cnt += 1
            if tmp[1]:
                break

    answer = cnt

    return answer


print(solution([1, 1, 9, 1, 1, 1], 0))
