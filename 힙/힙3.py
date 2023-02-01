
def calculate(command, arr):
    c1, c2 = command.split()

    if c1 == 'I':
        arr.append(int(c2))

    elif c1 == 'D':
        if arr:
            if c2 == '1':
                arr.pop(arr.index(max(arr)))
            elif c2 == '-1':
                arr.pop(arr.index(min(arr)))

def solution(operations):
    arr = []
    answer = [0, 0]

    for command in operations:
        calculate(command, arr)

    if arr:
        answer = [max(arr), min(arr)]

    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))


