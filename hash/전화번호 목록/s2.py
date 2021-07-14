phone_book = ["119", "97674223", "1195524421"]

def solution(phone_book):
    answer = True
    dic = {}
    for b in phone_book:
        dic[b] = 1
        print(list(dic))
        print(dic)
    for b in phone_book:
        temp = ""
        for a in b:
            if temp != a & temp in dic:
                answer = False
    return answer
