# 블랙잭
# index list를 생성해주는 함수


def index_generator(list_length):
    index_list = []
    for i in range(0, list_length-2):  # index_1은 0부터 시작해서 맨 뒤에서 두번째까지
        index_1 = i
        for j in range(i+1, list_length-1):
            index_2 = j
            for k in range(j+1, list_length):
                index_3 = k
                index_list.append([index_1, index_2, index_3])

    return index_list


# 1. 입력
list_length, criteria_num = map(int, input().split())
input_list = map(int, input().split())
# 2. 정렬(ASCENDING)
sorted_list = sorted(input_list)
# 3. 인덱스 리스트 생성
index_list = index_generator(list_length)
# 4. 모든 결과를 result_list에 저장 : BRUTE FORCE
result_list = []
for inner_index_list in index_list:
    result = sorted_list[inner_index_list[0]] + \
        sorted_list[inner_index_list[1]] + sorted_list[inner_index_list[2]]
    result_list.append(result)
result_list = sorted(result_list)
# 5. 결과 값을 하나씩 비교하여,
prev_result = 0
for result in result_list:
    # 기준 값보다 크면 break
    if result > criteria_num:
        break
    # 아니면, 이전 값을 갱신한다.
    else:
        prev_result = result
# 6. 출력 : 큰 결과 이전에 나온 마지막 값이 최종 정답
print(prev_result)
