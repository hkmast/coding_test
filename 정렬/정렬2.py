# https://school.programmers.co.kr/learn/courses/30/lessons/42746


# 자릿수를 기반으로 분할 한뒤 순서를 정하는 알고리즘
# 앞에서 1번째 자릿수를 바탕으로 0~9 의 배열에 집어넣음
# 나눠진 각각의 배열들 내부의 값들을 다시 앞에서 2, 3, 4 자릿수 를 바탕으로 정렬
# 2 와 21의 경우 1번째 자리수는 같지만 2번째 자리수 (_과 1)를 비교하려면 빈값 처리를 해주어야 하는데
# 빈값의 경우 본인의 바로 앞자리를 참조하여 정렬함 (2_의 경우 _의 앞자리가 2 이므로 2를 이용하여 비교)

# 이럴경우 다양한 자릿수와 유사한 숫자가 여러개 있을경우 제대로 된 정렬이 불가능하고 재귀로 인해 속도가 느리다는 단점이 있음
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

# 본인의 값을 4번 반복하고 4자리만을 가지고 비교를 한다
# 1의 경우 1111, 45의 경우 4545, 345의 경우 3453 과 같이 사용한다
# 이유는 다음과 같다 1의 경우를 생각해 보면
# 모든 자릿수가 채워진 경우가 아닌것 끼리의 값 비교는 어렵다
# 그렇다면 이 값을 비교하기 위해서는 빈공간의 값을 적절히 채워 같은 길이로 만든 뒤 비교해 주어야 한다
# 이 빈공간을 채우는 값을 본인의 값으로 한 이유는 다음과 같다
# 12 와 1213을 비교해 보자 앞의 12를 본다면 같으니 뒤를 봐야 한다
# 12 다음에 올 수 있는 값은 120X, 1210, 1211, 1212 이므로 12의 경우 1212로 늘려주면
# 1212 < 1213 이므로 순사가 잘 맞게 된다
# ex) 12의 경우 3번째 값은 맨 앞의 값인 1보다 큰 값을 가진 값들은 더 큰 순서를 가진다 (12, 122의 경우 12122 보다 12212가 더 크므로)
def solution(numbers):
    answer = ""
    numbers.sort(key=lambda x: (str(x) * 4)[0:4], reverse=True)
    numbers = list(map(lambda x: str(x), numbers))

    print(numbers)

    answer = "".join(numbers)
    print(answer)

    if int(answer) == 0:
        answer = "0"

    return answer
