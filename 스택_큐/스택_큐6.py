# 속도가 느림 -> 효율성 X
"""
def solution(prices):

    answer = []

    for idx, price in enumerate(prices):

        cnt = 0
        
        for comp_price in prices[idx+1:]:
            cnt += 1
            if price > comp_price:
                break

        answer.append(cnt)


    return answer
"""


def solution(prices):
    LENGTH = len(prices)

    answer = [0] * LENGTH

    print(answer)

    for i in range(0, LENGTH - 1):
        for j in range(i + 1, LENGTH):
            if prices[i] > prices[j]:
                answer[i] = j - i
                break
            answer[i] = j - i

    return answer


print(solution([1, 2, 3, 2, 3]))
