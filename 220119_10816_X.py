# 숫자 카드 2
number_card_count = int(input())
number_card_list = list(map(int, input().split()))
calculation_work_count = int(input())
calculation_work_list = list(map(int, input().split()))

for calculation_work_number in calculation_work_list:
    print(number_card_list.count(calculation_work_number), end=' ')
