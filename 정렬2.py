def sort_alg(input_list, strnum):
    if strnum > 3:
        return []
    if len(input_list) <= 1:
        return input_list

    tmp = []
    for i in range(10):
        tmp1 = []
        for string in input_list:
            if len(string) > strnum:
                if string[strnum] == str(i):
                    tmp1.append(string)
        tmp.append(tmp1)

    if strnum > 0:
        tmp1 = []
        for string in input_list:
            if len(string) == strnum:
                tmp1.append(string)

        tmp.insert(int(string[strnum - 1]), tmp1)

    answer_list = []

    for i in range(10):
        answer_list += sort_alg(tmp[i], strnum + 1)

    return answer_list


def solution(numbers):
    answer = ""

    numbers = list(map(lambda x: str(x), numbers))

    words = sort_alg(numbers, 0)
    words.reverse()

    for word in words:
        answer += word

    return answer


solution([3, 30, 34, 5, 9])