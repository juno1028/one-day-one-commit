# 부녀회장이 될테야
# 다음 층을 쌓는 함수


def construct_next_floor(prev_floor_list):
    next_floor_list = []
    for i in range(len(prev_floor_list)):
        next_floor_list.append(sum(prev_floor_list[0:i+1]))

    return next_floor_list


# case수, 층, 호 입력
case_number = int(input())
for _ in range(case_number):
    floor_number = int(input())
    ho_number = int(input())

    # 이전 층 temp(초기 값은 [0, 1, 2, 3, ~])
    constructed_floor = list(range(1, ho_number+1))

    # 층 수 만큼 함수 반복 실행
    for _ in range(floor_number):
        constructed_floor = construct_next_floor(constructed_floor)
        prev_temp_floor_list = constructed_floor

    print(constructed_floor[ho_number-1])
