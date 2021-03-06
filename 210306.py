# from itertools import combinations


def solution(clothes):
    clothes_dict = {}
    for cloth in clothes:
        if cloth[1] in clothes_dict:
            clothes_dict[cloth[1]] += 1
        else:
            clothes_dict[cloth[1]] = 1

    result = 1
    for clothes_value in clothes_dict.values():
        result *= clothes_value + 1

    result -= 1

    # 부분 집합 구해서 푸는 방법
#     total_combinations_list = []

#     for i in range(1,len(clothes_dict.keys())+1):
#         combination_list = list(combinations(clothes_dict.values(),i))
#         total_combinations_list.append(combination_list)

#     total_combinations_list_summed_result = 0

#     for combinations_list in total_combinations_list:
#         # 부분집합 내부 곱하기
#         for combination in combinations_list:
#             multiplied_result = 1
#             for elem in combination:
#                 multiplied_result *= elem
#             total_combinations_list_summed_result += multiplied_result

    return result
