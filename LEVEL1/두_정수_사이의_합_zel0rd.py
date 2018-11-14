def solution(a, b):
    answer = 0
    if(a > b):
        a , b = b , a
    for i in range(abs(a-b) + 1):
        answer = answer + a + i
    return answer
