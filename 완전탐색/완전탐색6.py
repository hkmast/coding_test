# 전력망을 둘로 나누기
# https://school.programmers.co.kr/learn/courses/30/lessons/86971

import copy


def DFS(start_num, node_list):

    stack = []
    done = dict()
    node_num = 0

    stack.append(start_num)

    while stack:
        node = stack.pop()

        if node in done:
            continue

        node_num += 1

        done[node] = True

        for idx, near_node in enumerate(node_list[node]):
            if near_node == 1:
                stack.append(idx)

    return node_num


def print_list(list):
    for i in list:
        print(i)


def solution(n, wires):

    answer = n

    node_list = [([0] * n) for _ in range(n)]

    for wire in wires:
        node_list[wire[0] - 1][wire[1] - 1] = 1
        node_list[wire[1] - 1][wire[0] - 1] = 1

    for i in range(0, n - 1):
        for j in range(1 + i, n):
            if node_list[i][j] == 1:

                tmp_node_list = copy.deepcopy(node_list)

                tmp_node_list[i][j] = 0
                tmp_node_list[j][i] = 0

                # print_list(tmp_node_list)

                gap = abs(DFS(i, tmp_node_list) - DFS(j, tmp_node_list))
                # print(gap)
                if gap < answer:
                    answer = gap
                    # print(gap)

    return answer


print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))
