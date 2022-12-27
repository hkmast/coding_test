# https://school.programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    phone_hash = {}

    len_min = len(phone_book[0])
    for phone in phone_book:
        phone_hash[phone] = 1
        if len(phone) < len_min: len_min = len(phone)

    for phone in phone_hash:
        for i in range(len_min, len(phone)):
            if phone[:i] in phone_hash:
                return False

    return True