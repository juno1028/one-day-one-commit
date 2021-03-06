def solution(phone_book):
    # 1. 해시맵을 만든다.
    phone_map = {}
    # 2. 해시맵에 모든 전화번호를 넣는다.
    for phone_number in phone_book:
        phone_map[phone_number] = 1
    # 3. phone_book내의 phone_number를 하나씩 접두사가 있는지 확인한다.
    for phone_number in phone_book:
        temp = ""
        for number in phone_number[:-1]:
            temp += number
            if temp in phone_map:
                return False
    return True
