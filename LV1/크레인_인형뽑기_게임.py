# https://school.programmers.co.kr/learn/courses/30/lessons/64061


def crain(board, move):
    pop_doll = 0

    for i in range(len(board)):
        if board[i][move - 1] != 0:
            pop_doll = board[i][move - 1]
            board[i][move - 1] = 0
            break

    return board, pop_doll


def insert_dolls(answer, dolls_list, pop_doll):

    if pop_doll:
        if dolls_list:
            last_doll = dolls_list.pop()
            if last_doll != pop_doll:
                dolls_list.append(last_doll)
                dolls_list.append(pop_doll)
            else:
                answer += 2
        else:
            dolls_list.append(pop_doll)

    return answer, dolls_list


def solution(board, moves):
    answer = 0
    dolls_list = []

    for move in moves:

        board, pop_doll = crain(board, move)
        answer, dolls_list = insert_dolls(answer, dolls_list, pop_doll)

    return answer


print(
    solution(
        [
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 3],
            [0, 2, 5, 0, 1],
            [4, 2, 4, 4, 2],
            [3, 5, 1, 3, 1],
        ],
        [1, 5, 3, 5, 1, 2, 1, 4],
    )
)
