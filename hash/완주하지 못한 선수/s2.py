import collections

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return answer.keys()