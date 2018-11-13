def solution(n):
    if(n % 2 == 1):
        answer = int(n / 2) * "수박" + "수"
    else:
        answer = int(n / 2) * "수박"
    return answer
