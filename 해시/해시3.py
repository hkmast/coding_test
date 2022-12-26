# https://school.programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    answer = True

    phone_book_dic = {}

    for phone in phone_book:
        if not phone_book_dic.get(len(phone)):
            phone_book_dic[len(phone)] = [phone]
        else:
            phone_book_dic[len(phone)].append(phone)

    # print(phone_book_dic)

    for i in range(1, 20):
        if not phone_book_dic.get(i):
            continue
        else:
            for phone in phone_book_dic[i]:
                for j in range(i+1, 20 + 1):
                    if not phone_book_dic.get(j):
                        continue
                    else:
                        for phone2 in phone_book_dic[j]:
                            if phone == phone2[:len(phone)]:
                                answer = False
                                return answer


    return answer

print(solution(["119", "97674223", "1195524421"]))


