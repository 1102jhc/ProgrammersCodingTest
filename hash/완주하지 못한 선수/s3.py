participant = ["leo", "kiki", "eden"]
completion  = ["eden", "kiki"]

def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        print(dic)
        temp += hash(part)
        print(temp)
    print(dic)
    print(temp)

    for com in completion:
        temp -= hash(com)
    answer = dic[temp]
    print(temp)
    print(answer)

    return answer

solution(participant, completion)