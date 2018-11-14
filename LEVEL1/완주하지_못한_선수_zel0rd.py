def solution(participant, completion):
    participant.sort()
    completion.sort()
    #print(participant)
    #print(completion)
    for i in range(len(participant)-1):
        if participant[i] != completion[i]:
            return participant[i]
        elif participant[i] == completion[i]:
            pass
        else:
            return participant[-1]

"""
def solution(participant, completion):
    for i in completion:
        participant.remove(i)
    return participant[0]
