# 한수
input_num = int(input())

counting = 0
for num in range(input_num, 0, -1):
    # 한자리나 두자리 수면 무조건 등차수열이므로 + 1
    if (len(str(num)) == 1) or (len(str(num)) == 2):
        counting += 1
    # 세자리 수인 경우,
    elif (len(str(num)) == 3):
        first_number_3, second_number_3, third_number_3 = map(int, str(num))
        if (first_number_3 - second_number_3) == (second_number_3 - third_number_3):
            counting += 1
    # 네자리 수인 경우,
    elif (len(str(num)) == 4):
        first_number_4, second_number_4, third_number_4, fourth_number_4 = map(
            int, str(num))
        first_minus_second = first_number_4 - second_number_4
        second_minus_third = second_number_4 - third_number_4
        third_minus_fourth = third_number_4 - fourth_number_4
        if (first_minus_second == second_minus_third) and (second_minus_third == third_minus_fourth):
            counting += 1

print(counting)
