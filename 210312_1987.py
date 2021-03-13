import sys

input_count = int(sys.stdin.readline())

number_list = list(map(int, sys.stdin.readline().split()))

not_primary_number_list = []

for number in number_list:
    if number == 1:
        not_primary_number_list.append(number)
    elif number == 2:
        continue
    else:
        for i in range(2, number):
            if number % i == 0:
                not_primary_number_list.append(number)
                break

print(len(number_list)-len(not_primary_number_list))
