# https://school.programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    answer = []

    dic1 = dict()
    dic2 = dict()

    # o(n)
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if dic1.get(genre):
            dic1[genre] += play
        else:
            dic1[genre] = play

        if dic2.get(genre):
            dic2[genre].append([idx, play])
        else:
            dic2[genre] = [[idx, play]]

    # print(dic2)

    # o(n^2) ? sorted의 속도
    for top_genre in sorted(dic1, key=lambda x: dic1.get(x), reverse=True):
        print(top_genre)
        for top_music in sorted(dic2[top_genre], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(top_music[0])

    return answer


print(solution(["classic", "Newage", "pop", "classic", "classic", "pop", "Newage"], [500, 1700, 600, 150, 800, 2500, 1500] ))
