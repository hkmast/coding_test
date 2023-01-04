# https://school.programmers.co.kr/learn/courses/30/lessons/42626
import heapq as hq
def solution(scoville, K):
    answer = 0

    hq.heapify(scoville)

    while True:
        if len(scoville) < 1: return -1
        else:
            if scoville[0] < K:
                tmp1 = hq.heappop(scoville)

                if len(scoville) < 1: return -1
                else:
                    tmp2 = hq.heappop(scoville)

                    hq.heappush(scoville, tmp1+(tmp2*2))
                    answer += 1

            else: return answer

    print(scoville)
    return answer

print(solution([1, 2, 3, 9, 10, 12, 5], 7))