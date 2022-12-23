"""def max_sort(inp, n):
    if n > 4:
        return []
    if len(inp) == 0:
        return []
    if len(inp) == 1:
        return inp


    tmp = []

    for i in range(10):
        tmp1 = []

        for st in inp:
            if len(st) >= n:

                if st[n - 1] == str(i):
                    tmp1.append(st)
        a = max_sort(tmp1, n + 1)
        if a:
            tmp.append(a)

    tmp1 = []
    for st in inp:
        if len(st) == n - 1: tmp1.append(st)

    if tmp1:
        if int(tmp1[0][n-2]) <= 0:
            tmp.insert(int(tmp1[0][n-2])+1, tmp1)
        else:
            tmp.insert(int(tmp1[0][n - 2]), tmp1)

    return tmp

def solution(numbers):

    numbers = list(map(lambda st: str(st), numbers))

    a= max_sort(numbers, 1)
    print(a)"""


def solution(numbers):
    answer = ""
    numbers.sort(
            key = lambda x: (str(x)*4)[0:4],
            reverse=  True
        )
    numbers = list(
        map(lambda x: str(x),
            numbers
            )
    )

    print(numbers)

    answer = ''.join(numbers)
    print(answer)

    if int(answer) == 0:
        answer = '0'

    return answer

