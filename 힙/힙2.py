# https://school.programmers.co.kr/learn/courses/30/lessons/42627
from heapq import heapify
from heapq import heappop as pop
from heapq import heappush as push
def solution(jobs):
    answer, cnt, time, now = 0, 0, 0, 0
    cnt = len(jobs)

    if cnt == 0:
        return 0

    heap = []
    jobs.sort(reverse=True)

    if jobs:
        if jobs[0][0] < now:

            while jobs:
                if jobs[0][0] < now:
                    tmp = jobs.pop()
                    push(heap, (tmp[1], tmp[0]))
                else:
                    break

        else:
            tmp = jobs.pop()
            push(heap, (tmp[1], tmp[0]))

    while heap:
        tmp = pop(heap)

        if now < tmp[1]:
            now = tmp[1]

        now = now + tmp[0]

        time += now - tmp[1]

        if jobs:
            if jobs[0][0] < now:

                while jobs:
                    if jobs[0][0] < now:
                        tmp = jobs.pop()
                        push(heap, (tmp[1], tmp[0]))
                    else: break

            else:
                tmp = jobs.pop()
                push(heap, (tmp[1], tmp[0]))



    answer = time//cnt

    return answer


print(solution([[0, 3], [2, 3], [3, 3]]))  # 9
