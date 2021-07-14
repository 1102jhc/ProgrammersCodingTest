phone_book = ["119", "97674223", "1195524421"]
# h1 = list(zip(phone_book, phone_book[1:]))
# print(h1)


def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    print(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        
        print(p1, p2)
      
    print(list(zip(phoneBook, phoneBook[1:])))

solution(phone_book)


# ["119", "97674223", "1195524421"]
# ["97674223", "1195524421"]
# [("119", "97674223"), ("97674223", "1195524421"), ("1195524421")]

# print(zip(phone_book, phone_book[1:]))

# def solution(phone_book):
#     phone_book.sort()

#     for prev, n in zip(phone_book, phone_book[1:]):
#         if n.startswith(prev):
#             return False
#     return True