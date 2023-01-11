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