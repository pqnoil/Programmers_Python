def solution(phone_number):
    blind_len = len(phone_number) - 4
    phone_s = phone_number[-4:]
    answer = '*' * blind_len + phone_s
    return answer