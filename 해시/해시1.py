# https://school.programmers.co.kr/learn/courses/30/lessons/42576

# 풀이1
# 효율성 떨어짐
# 예상 시간 복잡도 log n^2~3
'''
def solution(participants, completions):
    answer = ''

    for completion in completions:
        del participants[participants.index(completion)]

    answer = participants[0]

    return answer
'''
def solution(participants, completions):

    participants_dict = dict()
    for participant in participants:
        if not participants_dict.get(participant):
            participants_dict[participant] = 1
        else:
            participants_dict[participant] += 1

    completions_dict = dict()
    for completion in completions:
        if not completions_dict.get(completion):
            completions_dict[completion] = 1
        else:
            completions_dict[completion] += 1

    print(participants_dict)
    print(completions_dict)

    for completion in completions_dict:

        participants_dict[completion] = participants_dict[completion] - completions_dict[completion]
        if participants_dict[completion] == 1:
            answer = completion
            return answer

    for participant in participants_dict:
        if participants_dict[participant] == 1:
            answer = participant
            return answer