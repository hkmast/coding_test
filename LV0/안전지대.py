# https://school.programmers.co.kr/learn/courses/30/lessons/120866

def solution(board):
    answer = 0

    n = len(board)
    safeboard = []

    for i in range(0, n):
        tmp = []
        for j in range(0, n):
            tmp.append(1)
        safeboard.append(tmp)

    for i in range(0, n):
        for j in range(0, n):
            if board[i][j] == 1:
                safeboard[i][j] = 0
                if j + 1 < n:
                    safeboard[i][j + 1] = 0
                if j - 1 >= 0:
                    safeboard[i][j - 1] = 0
                if i - 1 >= 0:
                    safeboard[i - 1][j] = 0
                    if j + 1 < n:
                        safeboard[i - 1][j + 1] = 0
                    if j - 1 >= 0:
                        safeboard[i - 1][j - 1] = 0
                if i + 1 < n:
                    safeboard[i + 1][j] = 0
                    if j + 1 < n:
                        safeboard[i + 1][j + 1] = 0
                    if j - 1 >= 0:
                        safeboard[i + 1][j - 1] = 0

    # print(safeboard)

    for i in safeboard:
        answer += sum(i)

    return answer