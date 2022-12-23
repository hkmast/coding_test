def solution(citations):
    answer = 0

    length = len(citations)
    citations.sort(reverse=True)

    for i in range(0, length):
        h = citations[i]

        if i + 1 <= h:
            answer = i + 1

    # print(answer)
    return answer