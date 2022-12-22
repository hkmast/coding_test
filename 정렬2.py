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

    li = list(
        map(
            lambda x: (int(str(x) + (str(x)[len(str(x)) - 1]) * (4 - len(str(x)))), str(x)),
            numbers,
        )
    )

    print(li)

    ans = ''

    for n in range(len(li)):

        max = list(li[0])

        for x in li:
            #print(x)
            if max[0] <= x[0]:
                if max[1] > x[1]:
                    max = list(x)

        ans += max[1]

        print(f'max:{max}, list:{li}')
        del li[li.index(max)]


    print(ans)





solution([1, 10, 100, 1000, 818, 81, 898, 89, 0, 0])
