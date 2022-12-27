def solution(babbling):
    answer = 0

    cans = ["aya", "ye", "woo", "ma"]

    for bab in babbling:
        while bab:
            if bab.startswith(cans[0]):
                bab = bab[len(cans[0]):]
            elif bab.startswith(cans[1]):
                bab = bab[len(cans[1]):]
            elif bab.startswith(cans[2]):
                bab = bab[len(cans[2]):]
            elif bab.startswith(cans[3]):
                bab = bab[len(cans[3]):]
            else:
                break
        else:
            answer += 1


    return answer