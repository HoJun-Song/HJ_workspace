def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        key = phone_book[i]
        target = phone_book[i + 1][:len(key)]
        if key == target:
            answer = False
            break
    return answer